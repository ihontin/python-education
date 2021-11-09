--2.3 practice Задание 1
--Создайте новую таблицу potential customers с полями id, email, name, surname, second_name, city
CREATE TABLE if not exists potential_customers 
(
  id SERIAL not null primary key,
  email VARCHAR(25),
  customer_name VARCHAR(25),
  surname VARCHAR(25),
  second_name VARCHAR(25),
  city VARCHAR(255)
);
--Заполните данными таблицу.
insert into potential_customers
(email, customer_name, surname, second_name, city)
select email ||'p', first_name||'1', last_name||'1', middle_name||'1', city||'1'
from Users;
--Выведите имена и электронную почту потенциальных и существующих пользователей из города city 17
select U.first_name, U.email from Users U 
where U.city = 'city 17'
union 
select p.customer_name, p.email from potential_customers p
where p.city = 'city 17';
--Задание 2
--Вывести имена и электронные адреса всех users отсортированных по городам и по имени (по алфавиту)
select U.first_name, U.email from Users U 
order by city, first_name asc;
--Задание 3
--Вывести наименование группы товаров, общее количество по группе товаров в порядке убывания количества
select c.category_title, count(p.category_id) from categories c
left join products p on p.category_id = c.category_id 
group by c.category_title 
order by count(p.category_id) desc;
--Задание 4
--1. Вывести продукты, которые ни разу не попадали в корзину.
select * from products where product_id not in 
(
	select distinct products_product_id from cart_product cp 
);
--2. Вывести все продукты, которые так и не попали ни в 1 заказ. (но в корзину попасть могли).
select distinct p.* from products p
	left join cart_product cp on cp.products_product_id = p.product_id 
	left join carts c on cp.carts_cart_id = c.cart_id 
	left join orders o on c.cart_id = o.carts_cart_id
--where c.cart_id not in (select carts_cart_id from orders) or product_id  not in 
--	(select distinct products_product_id from cart_product)
where o.order_id is null 
order by p.product_id ASC;
--3. Вывести топ 10 продуктов, которые добавляли в корзины чаще всего.
select * from products where product_id in
(
	select products_product_id from cart_product
	group by products_product_id
	order by count(products_product_id) desc
	LIMIT 10
);
--4. Вывести топ 10 продуктов, которые не только добавляли в корзины, но и оформляли заказы чаще всего.
select distinct p.product_id, count(cp.products_product_id) from products p
	left join cart_product cp on cp.products_product_id = p.product_id 
	left join carts c on cp.carts_cart_id = c.cart_id 
	left join orders o on c.cart_id = o.carts_cart_id
where o.order_status_order_status_id <> 5
	group by p.product_id
	order by count(cp.products_product_id) desc;
--5. Вывести топ 5 юзеров, которые потратили больше всего денег (total в заказе).
select u.*, c.total from users u right join carts c
on u.user_id = c.users_user_id 
order by c.total desc
limit 5;
--6. Вывести топ 5 юзеров, которые сделали больше всего заказов (кол-во заказов).
select u.*, count(o.order_id), count(c.cart_id) from users u left join carts c
on u.user_id = c.users_user_id left join orders o 
on c.cart_id = o.carts_cart_id
group by u.user_id
order by count(o.order_id) desc
limit 5;
--7. Вывести топ 5 юзеров, которые создали корзины, но так и не сделали заказы.
select u.*, count(o.order_id), count(c.cart_id) from users u left join carts c
on u.user_id = c.users_user_id left join orders o 
on c.cart_id = o.carts_cart_id
group by u.user_id
order by count(o.order_id), count(c.cart_id) desc
limit 5;











