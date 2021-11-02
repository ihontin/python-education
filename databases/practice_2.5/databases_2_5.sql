set enable_seqscan = on;

--1 request: select or join

select first_name from users where user_id in
(select users_user_id from carts where total > 1000 and timestamp_ > date('2021-03-13 07:53:43.000'));

select u.first_name from users u 
	left join carts c on u.user_id = c.users_user_id
where c.total > 1000 and c.timestamp_ > date('2021-03-13 07:53:43.000');

explain analyze select first_name from users where user_id in
(select users_user_id from carts where total > 1000 and timestamp_ > date('2021-03-13 07:53:43.000'));

explain analyze select u.first_name from users u 
	left join carts c on u.user_id = c.users_user_id
where c.total > 1000 and c.timestamp_ > date('2021-03-13 07:53:43.000');

create index if not exists idx_carts_total_timestamp_
	on carts using btree(total, timestamp_);
drop index if exists idx_carts_total_timestamp_;

--2 request:

select price, category_id from products
where category_id in(3,16)
order by price desc
limit 10;

explain select price, category_id from products
where category_id in(3,16)
order by price desc
limit 10;

create index if not exists idx_product_category_id_price on products 
	using btree(category_id, price) where category_id in(3, 16);
drop index if exists idx_product_category_id_price;
	
--3 request:

select * from orders
	where round(total) = 1003;

explain analyze select round(total) from orders
	where round(total) = 1003;

create index if not exists idx_orders_total on orders
	using btree(round(total));
drop index if exists idx_orders_total;

--4 request:

begin;

set enable_seqscan = on;
set enable_indexscan = off;

select product_title, price from products
where category_id = 7
order by price desc;

explain select product_title, price from products
where category_id = 7
order by price desc;

explain update products set price = price + ((price / 100) * 5)
where category_id = 7;

create index if not exists idx_products_category_id on products using btree(category_id);
drop index idx_products_category_id;

rollback;


