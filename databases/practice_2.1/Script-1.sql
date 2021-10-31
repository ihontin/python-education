CREATE TABLE if not exists Order_status 
(
	order_status_id serial not null PRIMARY key ,
	status_name VARCHAR(255)
);

CREATE TABLE if not exists Users
(
	user_id serial not null PRIMARY KEY,
	email VARCHAR(255),
	e_password VARCHAR(255),
	first_name VARCHAR(255),
	last_name VARCHAR(255),
	middle_name VARCHAR(255),
	is_staff int2,
	country VARCHAR(255),
	city VARCHAR(255),
	address TEXT
);
CREATE TABLE if not exists Orders 
(
	order_id serial not null PRIMARY key,
	Carts_cart_id INT,
	Order_status_order_status_id INT,
	shipping_total DECIMAL,
	total DECIMAL,
	created_at TIMESTAMP(2),
	updated_at TIMESTAMP(2),
	foreign key (Carts_cart_id) references Carts(cart_id),
	foreign key (Order_status_order_status_id) references Order_status(order_status_id)
);
CREATE TABLE if not exists Carts
(
	cart_id serial not null PRIMARY KEY,
	Users_user_id INT,
	subtotal DECIMAL,
	total DECIMAL,
	timestamp_ TIMESTAMP(2),
	foreign key (Users_user_id) references Users(user_id)
);
CREATE TABLE if not exists Cart_product
(
	carts_cart_id INT,
	products_product_id INT,
	foreign key (carts_cart_id) references Carts(cart_id),
	foreign key (products_product_id) references Products(product_id)
);
CREATE TABLE if not exists Categories
(
	category_id serial not null primary key,
	category_title VARCHAR(255),
	category_description TEXT
);
CREATE TABLE if not exists Products
(
	product_id serial not null primary key,
	product_title VARCHAR(255),
	product_description text,
	in_stock INT,
	price float4,
	slug VARCHAR(45),
	category_id INT,
	foreign key (category_id) references Categories(category_id)
);
--2.1practice 4. заполнить таблицу данными
copy Users from '/usr/src/users.csv' with delimiter ',' csv;
copy Order_status from '/usr/src/order_statuses.csv' with delimiter ',' csv;
copy Categories from '/usr/src/categories.csv' with delimiter ',' csv;
copy Carts from '/usr/src/carts.csv' with delimiter ',' csv;
copy Orders from '/usr/src/orders.csv' with delimiter ',' csv;
copy Products from '/usr/src/products.csv' with delimiter ',' csv;
copy Cart_product from '/usr/src/cart_products.csv' with delimiter ',' csv;
--2.1practice 1. добавьте в таблицу users колонку phone_number (int)
--2. поменяйте тип данных в таблице users колонка phone_number с int на varchar
alter table Users add phone_number INT NOT NULL DEFAULT 0;
alter table Users alter column phone_number type VARCHAR(15);
--2.1practice 1. в таблице products увеличьте цену в 2 раза
UPDATE Products SET price = price * 2;














