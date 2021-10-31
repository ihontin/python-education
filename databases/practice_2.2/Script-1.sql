--2.2practice Задание 1
--  1. всех юзеров, 2. все продукты, 3. все статусы заказов
select * from Users; 
select * from Products;
select * from Order_status;
--2.2practice  Задание 2
--Вывести заказы, которые успешно доставлены и оплачены
select * from orders where Order_status_order_status_id in(1, 3)
order by total desc;
--2.2practice Задание 3
--1. Продукты, цена которых больше 80.00 и меньше или равно 150.00
select * from Products where price between 80.001 and 150.00
order by price desc;
--2. заказы совершенные после 01.10.2020 (поле created_at)
select * from Orders where DATE(created_at) > '2020.11.10'
order by created_at asc;
--3. заказы полученные за первое полугодие 2020 года
select * from Orders where created_at between '2020.01.01  00:00:00' and '2020.05.30  00:00:00'
order by created_at asc;
select * from Orders where cast(created_at as date) >= '2020.01.01' and DATE(created_at) <= '2020.05.30'
order by created_at asc;
--4. подукты следующих категорий Category 7, Category 11, Category 18
select * from Products where category_id in(7, 11, 18)
order by product_id asc;
--5. незавершенные заказы по состоянию на 31.12.2020
select * from Orders where DATE(created_at) = '2020.12.31' and Order_status_order_status_id not in(4, 5)
order by total asc;
--6.Вывести все корзины, которые были созданы, но заказ так и не был оформлен.
select * from Carts where cart_id in
(
	select Carts_cart_id from Orders where Order_status_order_status_id not in(1, 2, 3, 4)
);
--2.2practice Задание 4
--1. среднюю сумму всех завершенных сделок
select SUM(total)/COUNT(order_id) as average from Orders where Order_status_order_status_id = 4;
--2. вывести максимальную сумму сделки за 3 квартал 2020
select MAX(total) as total_max from Orders where created_at
between '2020.07.01  00:00:00' and '2020.09.30  00:00:00';















