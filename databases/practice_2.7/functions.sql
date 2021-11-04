--1. Создать функцию, которая сетит shipping_total = 0 в таблице order,
-- если город юзера равен x. Использовать IF clause.

drop function if exists shipping_to_zero(varchar(255));

create or replace function shipping_to_zero(x varchar(255))
returns void
language plpgsql
as
$$
declare
	zero_shipping orders.shipping_total%type = 0;
	save_order orders%rowtype;
begin
	select o.* from orders o 
		right join carts c on o.carts_cart_id = c.cart_id 
		right join users u on c.users_user_id = u.user_id 
	where u.city = x
	into save_order;

	if not found then 
		raise notice 'The city is not found';
	else
		raise notice 'Founded! shipping_total = 0 in order %', save_order.order_id;
		update orders set shipping_total = zero_shipping
			where order_id = save_order.order_id;
	end if;
end;
$$;

begin;

select shipping_to_zero('city 02');

select o.* from orders o 
		right join carts c on o.carts_cart_id = c.cart_id 
		right join users u on c.users_user_id = u.user_id 
	order by order_id 
	limit 10;

rollback;



--2. Написать 2 любые хранимые процедуры с использованием условий, циклов и транзакций.

drop table if exists garden;

create temporary table garden 
(
	fruit_id serial not null primary key,
	fruin_name varchar(255),
	price int,
	in_stock int
);

insert into garden(fruin_name, price, in_stock)
values 
('apple', 23, 2),
('pears', 42, 5),
('plums', 31, 3);

drop procedure buy_fruit;

create or replace procedure buy_fruit(chenge_fruit int, cash int)
language plpgsql
as $$
<<outer_block>>
declare 
	num_of_stock int;
begin
	update garden
	set in_stock = in_stock - cash / price
	where fruit_id = chenge_fruit
	returning in_stock
	into num_of_stock;
	if num_of_stock >= 0 then
		<<inner_block>>
		declare 
			rec record;
		begin
			for rec in select * from garden
			loop
				if rec.fruit_id = chenge_fruit then
			    	raise notice 'We should to order %', rec.fruin_name;	
			  	end if;
			end loop;
		end inner_block;
	else
		raise notice 'We should to order fruits';	
		rollback;
	end if;
end outer_block;
$$;

select * from garden order by fruit_id;


call buy_fruit(2, 84);


--3

drop procedure add_fruit;

create or replace procedure add_fruit(
	new_fruin_name varchar(255),
	new_price int,
	new_in_stock int
)
language plpgsql
as $$
declare 
	counter int := 0;
begin
	insert into garden(fruin_name, price, in_stock)
	values(new_fruin_name, new_price, new_in_stock);

	select count(g.fruit_id) from garden g
	into counter;
	if counter <= 5 then
		while counter > 0
		loop
			raise notice 'Fruit %', counter;
			counter := counter - 1;
		end loop;
	else
		raise notice 'No more than five fruits.';
		rollback;
	end if;
end;
$$;

select * from garden order by fruit_id;

call add_fruit('pineapple', 67, 6);
call add_fruit('peach', 55, 9);
call add_fruit('banana', 38, 1);

