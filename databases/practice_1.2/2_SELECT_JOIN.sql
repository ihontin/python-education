--Задание 2
--Придумать 3 различных запроса SELECT с осмысленным использованием разных видов JOIN.
--Используя explain добавить только необходимые индексы для уменьшения стоимости (cost) запросов.

select c.licence_plate || ', ' || m.model_name || ', ' || e.engine as Car_by_engine from car c
	left join model m on c.model_fk_id = m.model_id 
	left join engine e on m.engine_fk_id = e.engine_id
	where e.engine_id between 2 and 4
	order by e.engine_id;

explain select c.licence_plate || ', ' || m.model_name || ', ' || e.engine as Car_by_engine from car c
	left join model m on c.model_fk_id = m.model_id 
	left join engine e on m.engine_fk_id = e.engine_id
	where e.engine_id between 2 and 4
	order by e.engine_id;
	
select c.first_name, c.second_name, o.price, o.rent_period, 
ceil(AVG (price) over (partition by o.rent_period)) as price_avg,
row_number() over (partition by o.rent_period order by o.price)
	from Customer c 
	right join orders o on c.customer_id = o.customer_fk_id
where o.price = 400 and o.rent_period = '2days';

explain select c.first_name, c.second_name, o.price, o.rent_period, 
ceil(AVG (o.price) over (partition by o.rent_period)) as price_avg,
row_number() over (partition by o.rent_period order by o.price)
	from Customer c 
	right join orders o on c.customer_id = o.customer_fk_id
where o.price = 400 and o.rent_period = '2days';

create index if not exists idx_orders_price_rent_period on orders using btree(price, rent_period);
drop index idx_orders_price_rent_period;

select b.branch_name, a.street, a.building, c.first_name, c.second_name from branch b 
	full join address a on b.address_fk_id = a.address_id 
	full join customer_address ca on a.address_id = ca.address_fk_id 
	full join customer c on ca.customer_fk_id = c.customer_id
	where a.street = 'Street1' or a.street = 'Street1001'
	order by a.street ;

explain select b.branch_name, a.street, a.building, c.first_name, c.second_name from branch b 
	full join address a on b.address_fk_id = a.address_id 
	full join customer_address ca on a.address_id = ca.address_fk_id 
	full join customer c on ca.customer_fk_id = c.customer_id
	where a.street = 'Street1' or a.street = 'Street1001'
	order by a.street;

create index if not exists idx_address_street on address using btree(street);
drop index idx_address_street;
