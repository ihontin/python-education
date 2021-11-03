--view to products and cart_products tables 

create or replace view times_ordered as
select p.product_id as ordered_id, count(cp.products_product_id) as ordered from cart_product cp
	right join products p on p.product_id = cp.products_product_id 
group by p.product_id 
	order by p.product_id asc;

drop view if exists times_ordered cascade;

select * from times_ordered;

create or replace view products_table as
	select p.product_id as id, 
	p.product_title ||': '|| p.product_description as product,
	p.in_stock as quantity, tor.ordered, p.price,
	'Category: ' || cast(p.category_id as char(2)) 
	from products p inner join times_ordered tor
		on p.product_id = tor.ordered_id;

explain select * from products_table
	where ordered > 8;

drop view if exists products_table;

--view to products and category tables 

create or replace view products_view as
select p.*, count(cp.products_product_id) as ordered from products p 
	left join cart_product cp on p.product_id = cp.products_product_id 
	group by p.product_id 
	order by p.product_id;

select * from products_view;
drop view if exists products_view cascade; 

create or replace view add_category as
select pv.product_title, pv.ordered,
	case 
		when pv.ordered = 0 
		then 'Super mega NEW ' ||cat.category_title
		when pv.ordered in(1,2) 
		then 'Super NEW ' ||cat.category_title
		when pv.ordered = 3 
		then 'NEW ' ||cat.category_title
		else cat.category_title
	end,
	cat.category_description from products_view pv
	left join categories cat on pv.category_id = cat.category_id
order by pv.product_id;
	
select * from add_category;
drop view if exists add_category; 

--view to order_status and order tables 

begin;

create or replace view status_table as
	select * from order_status
	with check option;

insert into status_table(status_name)
	values('Delivered');

select * from status_table;

rollback;

select * from status_table;

drop view if exists status_table cascade;

create or replace view orders_table as
	select * from orders;

select * from orders_table;

drop view if exists orders_table cascade;

create or replace view orders_with_status as
	select ot.order_id as id, ot.carts_cart_id as cart,
	ot.total, st.status_name as status
	from orders_table ot 
		left join status_table st 
		on ot.order_status_order_status_id = st.order_status_id
	where st.status_name ='Canceled'
	order by ot.order_status_order_status_id desc;

alter view orders_with_status rename to orders_and_status;

select * from orders_and_status;

drop view if exists orders_and_status cascade;

--Создать материализированное представление для "тяжелого" запроса на свое усмотрение

create materialized view users_fail as
select u.first_name as castumer, c.total as sum_of_order, max(p.price), os.status_name from users u
	left join carts c on c.users_user_id = u.user_id 
	left join orders o on o.carts_cart_id = c.cart_id 
	left join order_status os on o.order_status_order_status_id = os.order_status_id 
	left join cart_product cp on cp.carts_cart_id = c.cart_id 
	left join products p on cp.products_product_id = p.product_id 
where o.order_status_order_status_id = 5
group by u.user_id, c.total, os.status_name
with no data;

refresh materialized view users_fail;

select * from users_fail;

drop materialized view users_fail;



