--Задание 6
--Добавить 2 триггера (один из них ДО операции по изменению данных, второй после)
--и функции или процедуры-обработчики к ним.


drop view engine_view;
create or replace view engine_view as
	select * from engine;

drop function show_messege cascade;

create or replace function show_messege() 
	returns trigger
	language plpgsql
as
$$
begin 
	if TG_OP = 'INSERT' then 
		raise notice 'insert did not work';
		return old;
	elsif TG_OP = 'UPDATE' then
		raise notice 'update did not work';
		return old;
	elsif TG_OP = 'DELETE' then
		raise notice 'delete did not work';
		return old;
	end if;
end;
$$;

drop trigger show_insted on engine_view;

create trigger show_insted
	instead of insert or update or delete
	on engine_view
	for each row
	execute procedure show_messege();

begin;

insert into engine_view(engine_id, engine)
	values(101, 'Engine' || 101)
	
update engine_view set engine = 'Engine' || 101
	where engine_id = 1;

delete from engine_view where engine_id = 1;
	
select * from engine
order by engine_id;

rollback;

--2---------------------

drop table old_address;

create temporary table old_address
(
	past_address_id serial not null primary key,
	city_fk_id int not null,
	street varchar(25),
	building varchar(15),
	time_of_change timestamp 
);

drop function save_old_address cascade;

create or replace function save_old_address()
returns trigger 
language plpgsql
as
$$
begin 
	if new.street <> old.street or new.building <> old.building then 
		insert into old_address(city_fk_id, street, building, time_of_change)
		values(old.city_fk_id, old.street, old.building, now());
	else
		raise notice 'Maybe the same address in the new city?';
	end if;
	return new;
end;
$$;

drop trigger should_save_old_address on address;

create or replace trigger should_save_old_address
	before update
	on address 
	for each row 
	execute procedure save_old_address();

begin;

update address set street = 'Lenina', building = '24'
where address_id = 1;

select * from address
	order by address_id;

select * from old_address
	order by past_address_id;

rollback;
