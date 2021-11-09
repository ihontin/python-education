--Задание 5
--Написать 2 любые хранимые процедуры. 
--В них использовать транзакции для insert, update, delete.
begin;
drop procedure add_new_car(name_car varchar(25), modification int);

create or replace procedure add_new_car(name_car varchar(25), modification int)
language plpgsql
as $$
declare 
	name_of_car car.licence_plate%type;
	new_plate varchar(15) := '123456789';
begin
	update car set licence_plate = new_plate
		where licence_plate = name_car
		returning licence_plate
		into name_of_car;
	if name_of_car is not null then
		commit;
		raise notice 'New licence plate of the car is %', name_of_car;
		update car set model_fk_id = modification
		where licence_plate = new_plate;
		commit;
	else
		commit;
		raise notice 'Licence plate of the new car is %', new_plate;
		insert into car (car_id, licence_plate, model_fk_id, branch_fk_id)
			values(101, new_plate, 100, 10);
		commit;
	end if;
end;
$$;

rollback;

call add_new_car('Licenсe1', 2)

select * from car
order by car_id;

--2

begin;

drop procedure if exists dell_old_phone(id_of_phone int);

create or replace procedure dell_old_phone(id_of_phone int, new_phone int)
language plpgsql
as $$
declare
	save_id_cp phone.phone_id%type;
	save_id phone.phone_id%type;
begin
	select * from customer_phone cp 
		where phone_fk_id =  id_of_phone
		into save_id_cp;
	
	if save_id_cp is not null then
		delete from customer_phone
			where phone_fk_id = id_of_phone;
		
		select * from phone
			where phone_id =  id_of_phone
			into save_id;
		
		if save_id is null then
			rollback;
		else
			delete from phone
				where phone_id = id_of_phone;
		end if;
	else
		insert into phone(phone_id, phone_number)
			values(id_of_phone, new_phone);
		commit;
	end if;
end;
$$;

call dell_old_phone(1, 1199911);

select * from phone p
	left join customer_phone cp on p.phone_id = cp.phone_fk_id 
order by phone_id;

rollback;
