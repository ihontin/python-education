drop table Engine cascade;
drop table Model cascade;
drop table Car cascade;
drop table Branch cascade;
drop table Car_orders cascade;
drop table Branch_phone cascade;
drop table Orders cascade;
drop table Phone cascade;
drop table Address cascade;
drop table Customer cascade;
drop table Customer_phone cascade;
drop table Customer_address cascade;
drop table City cascade;

insert into Customer
	select i, 'First_name' || i, 'Second_name' || i
	from generate_series(1, 1000) as i;
insert into City
	select i, 'City' || i
	from generate_series(1, 10) as i;
insert into Address 
	select i, ceil(random() * 10), 'Street' || i, 'House' || i
	from generate_series(1, 1000) as i;
update Address set city_fk_id = case 
	when address_id between 1 and 100 then 1
	when address_id between 101 and 200 then 2
	when address_id between 201 and 300 then 3
	when address_id between 301 and 400 then 4
	when address_id between 401 and 500 then 5
	when address_id between 501 and 600 then 6
	when address_id between 601 and 700 then 7
	when address_id between 701 and 800 then 8
	when address_id between 801 and 900 then 9
	when address_id between 901 and 1000 then 10
	else city_fk_id
end;
insert into Engine
	select i, 'Engine' || i
	from generate_series(1, 50) as i;
insert into Model
	select i + 50, 'Model' || i + 50, i
	from generate_series(1, 50) as i;
insert into Model
	select i, 'Model' || i, i
	from generate_series(1, 50) as i;
insert into Car
	select i, 'Licence' || i, i, (i + 10) / 10
	from generate_series(1, 99) as i;
insert into Car
	values(100, 'Licence100', 100, 1);
insert into Address 
	select i, i - 1000, 'Street' || i, 'House' || i
	from generate_series(1001, 1010) as i;
insert into customer_address 
	select i, 1001 - i
	from generate_series(1, 1000) as i;
insert into Phone 
	select i, 8050000 + i
	from generate_series(1, 1010) as i;
insert into Customer_phone 
	select i, i
	from generate_series(1, 1000) as i;
insert into Branch 
	select i, 'Branch_name' || i, 1000 + i
	from generate_series(1, 10) as i;
insert into branch_phone 
	select 1000 + i, i
	from generate_series(1, 10) as i;
insert into orders
	select i, i, (i + 100) / 100, 100 * (ceil(random() * (5))),
	date('2018-01-01') + i,
	ceil(random() * (5)) || 'days'
	from generate_series(1, 999) as i;
insert into orders
	select 1000, 1000, 10, 300, '2020-09-27', '1days'; --)
insert into car_orders 
	select i, (i + 100) / 100
	from generate_series(1, 999) as i;
insert into car_orders 
	values(1000, 1);
create table if not exists Engine
(
	engine_id serial not null primary key,
	engine varchar(25)
);
create table if not exists Model
(
	model_id serial not null primary key,
	model_name varchar(25),
	engine_fk_id int not null
);
create table if not exists Car
(
	car_id serial not null primary key,
	licence_plate varchar(25),
	model_fk_id int not null,
	branch_fk_id int not null
);
create table if not exists Branch
(
	branch_id serial not null primary key,
	branch_name varchar(25),
	address_fk_id int not null
);
create table if not exists Car_orders
(
	orders_fk_id int not null,
	car_fk_id int not null
);
create table if not exists Branch_phone
(
	phone_fk_id int not null,
	branch_fk_id int not null
);
create table if not exists Orders
(
	orders_id serial not null primary key,
	customer_fk_id int not null,
	branch_fk_id int not null,
	price int,
	rent_date date,
	rent_period varchar(25)
);
create table if not exists Phone
(
	phone_id serial not null primary key,
	phone_number bigint
);
create table if not exists Address
(
	address_id serial not null primary key,
	city_fk_id int not null,
	street varchar(25),
	building varchar(15)
);
create table if not exists Customer
(
	customer_id serial not null primary key,
	first_name varchar(25),
	second_name varchar(25)
);
create table if not exists Customer_phone
(
	customer_fk_id int not null,
	phone_fk_id int not null
);
create table if not exists Customer_address
(
	customer_fk_id int not null,
	address_fk_id int not null
);
create table if not exists City
(
	city_id serial not null primary key,
	city_name varchar(25)
);

alter table Customer_address add constraint Customer_address_customer_fk_id
	foreign key (customer_fk_id)
	references Customer(customer_id);
alter table Customer_address add constraint Customer_address_address_fk_id
	foreign key (address_fk_id)
	references Address(address_id);
alter table Customer_phone add constraint Customer_phone_phone_fk_id
	foreign key (phone_fk_id)
	references Phone(phone_id);
alter table Customer_phone add constraint Customer_phone_customer_fk_id
	foreign key (customer_fk_id)
	references Customer(customer_id);
alter table Address add constraint Address_city_fk_id
	foreign key (city_fk_id)
	references City(city_id);
alter table Orders add constraint Orders_customer_fk_id 
	foreign key (customer_fk_id)
	references Customer(customer_id);
alter table Orders add constraint Orders_branch_fk_id 
	foreign key (branch_fk_id)
	references Branch(branch_id);
alter table Branch_phone add constraint Branch_phone_phone_fk_id 
	foreign key (phone_fk_id)
	references Phone(phone_id);
alter table Branch_phone add constraint Branch_phone_branch_fk_id 
	foreign key (branch_fk_id)
	references Branch(branch_id);
alter table Car_orders add constraint Car_orders_orders_fk_id 
	foreign key (orders_fk_id)
	references Orders(orders_id);
alter table Car_orders add constraint Car_orders_car_fk_id 
	foreign key (car_fk_id)
	references Car(car_id);
alter table Branch add constraint branch_address_fk_id 
	foreign key (address_fk_id)
	references Address(address_id);
alter table Car add constraint car_branch_fk_id 
	foreign key (branch_fk_id)
	references Branch(branch_id);
alter table Car add constraint car_model_fk_id 
	foreign key (model_fk_id)
	references Model(model_id);
alter table Model add constraint model_engine_fk_id 
	foreign key (engine_fk_id)
	references Engine(engine_id);
