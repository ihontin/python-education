set transaction isolation level READ COMMITTED;

--work with a first table

begin;

select * from potential_customers
order by id asc
limit 4;


update potential_customers 
	set customer_name = 'Babushka', surname = 'Zina' 
where id = 1;

savepoint update_names;

alter table potential_customers 
	rename customer_name to first_name;

savepoint alter_rename;

delete from potential_customers where id = 2;

savepoint delete_id2;

insert into potential_customers (id, email, first_name, surname, second_name, city)
values
	(2, 'my_mail@mail.com', 'new_name1', 'new_lats_name', 'new_middle_name', 'cicity1');

release savepoint delete_id2;
release savepoint alter_rename;
release savepoint update_names;
rollback to savepoint update_names;
rollback;
commit;

--work with a second table

begin;

select p.product_id, p.product_title, p.price, p.in_stock, c.category_title from products p
left join categories c on p.category_id = c.category_id
order by p.product_id asc;

update products set product_title =
	case
	when in_stock < 20
	then product_title ||' (discount)'
	when in_stock >= 20
	then product_title ||' (20% discount)'
	end
where category_id = 6 or category_id = 4;

update products set product_title =
	case
	when product_id < 10
	then left(product_title, 9)
	when product_id < 100
	then left(product_title, 10)
	when product_id < 1000
	then left(product_title, 11)
	when product_id > 999
	then left(product_title, 12)
	end
where category_id = 6 or category_id = 4;

savepoint nothing_to_lose;

insert into products (product_id, product_title, product_description, in_stock, price, slug, category_id)
	select product_id + 50, 'New '||product_title, 'New '||product_description, in_stock, price, slug, category_id from products 
		where product_id > 3950;
	
savepoint insert_50product;

delete from products where product_id > 4000;
		
release savepoint insert_50product;
release savepoint nothing_to_lose;

rollback to savepoint insert_50product;
rollback to savepoint nothing_to_lose;

rollback;
commit;

--work with a third table

begin;

select * from orders;

alter table users add sex varchar(6) default 'male';
alter table users alter sex type char(6);
alter table users drop column sex; -- no need to use

update users 
	set sex = 'female'
	where user_id % 2 = 0
	RETURNING * ;

delete from orders where carts_cart_id in 
	(select cart_id from carts where users_user_id % 2 = 1);
delete from cart_product where carts_cart_id in 
	(select cart_id from carts where users_user_id % 2 = 1);
delete from carts where cart_id % 2 = 1;
delete from users where user_id % 2 = 1;

select user_id, first_name, sex from users
order by user_id asc;

savepoint alter_users;

truncate orders;
copy Orders from '/usr/src/orders.csv' with delimiter ',' csv;

savepoint truncate_orders;

DROP TABLE IF EXISTS orders;

savepoint DROP_orders;

insert into orders 
values(1502, 1, 1, 60, 222.22,'2020-12-13 00:00:00.000', '2020-09-04 00:00:00.000');

release savepoint DROP_orders;
release savepoint truncate_orders;
release savepoint alter_users;

rollback to savepoint alter_users;
rollback;



commit;
