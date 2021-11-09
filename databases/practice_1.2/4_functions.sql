--Задание 4
--Создать 2 функции (одна из них должна возвращать таблицу,
--одна из них должна использовать циклы, одна из них должна использовать курсор).

drop function if exists customers_in_city;
create or replace function  customers_in_city (n int)
returns table(customers varchar(25), address varchar(40))
language plpgsql
as $$
declare 
	rec record;
begin 
	for rec in (
		select c.first_name || ', ' || c.second_name as client,
			ci.city_name as city,
			a.street || ', ' || a.building as address
		from customer c
			left join customer_address ca on c.customer_id = ca.customer_fk_id 
			left join address a on ca.address_fk_id = a.address_id 
			left join city ci on a.city_fk_id = ci.city_id
			where ci.city_id = n	
	)	loop 
			customers := rec.client;
			address := upper(rec.city) || ', ' || rec.address;
		return next;
		end loop;
end;
$$;

select * from customers_in_city(7);


drop function if exists search_phones;

begin;

create or replace function search_phones (search_number int, new_number int)
returns void
language plpgsql
as $$
declare 
	cur cursor for select * from phone;
begin
	for rec in cur loop
		if rec.phone_id = search_number then
			raise notice 'The phone % is found', rec;
			update phone set phone_number = new_number
				where phone_id = search_number;
		end if;
		if not found then
			raise notice 'The phone not found';
			rollback;
		end if;
	end loop;
end;
$$;

select * from search_phones(1, 1000001);

select * from phone
	order by phone_id;

rollback;

