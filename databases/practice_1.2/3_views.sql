--Задание 3
--Создать 3 представления (1 из них должно быть материализированным и хранить данные от "тяжелого" запроса).

drop view if exists car_model_engin;
create or replace view car_model_engin as
	select m.model_name, c.licence_plate, e.engine from car c
		left join model m on c.model_fk_id = m.model_id 
		left join engine e on m.engine_fk_id = e.engine_id 
	order by m.model_id;

select * from car_model_engin;

drop view if exists customer_phone_view;
create or replace view customer_phone_view as
	select c.first_name as customer, p.phone_number from customer c 
		left join customer_phone cp on c.customer_id = cp.customer_fk_id 
		left join phone p on cp.phone_fk_id = p.phone_id 
		order by p.phone_id;
	
select * from customer_phone_view;

drop materialized view if exists top_ordered_cars;
create materialized view top_ordered_cars as
	select m.model_name as car,
	o.rent_period as rent, o.price,
	c.first_name || ', ' || c.second_name as customer,
	count(co.car_fk_id) over (partition by car.car_id) as ordered
	from customer c 
	left join orders o on c.customer_id = o.customer_fk_id
	left join car_orders co on o.orders_id = co.orders_fk_id 
	left join car on co.car_fk_id = car.car_id
	left join model m on car.model_fk_id = m.model_id
	order by ordered desc
	limit 1000
	with data;

select * from top_ordered_cars;

refresh materialized view top_ordered_cars;
