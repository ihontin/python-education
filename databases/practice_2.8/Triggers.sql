--2.8

select c.category_title, p.product_title, p.price, avg(p.price) over 
	(partition by c.category_id)
	from products p left join categories c 
		on p.category_id = c.category_id;
	
drop table old_price;

create temporary table old_price(
	old_price_id serial not null primary key,
	product_title varchar(255),
	price float4
);

drop function save_old_price cascade;

create or replace function save_old_price()
  returns trigger
  language plpgsql
  as
$$
begin
	if new.price <> old.price then 
		insert into old_price(old_price_id, product_title, price)
		values(old.product_id, old.product_title, old.price);
	end if;
	return new;
end;
$$;

drop trigger save_old_price on old_price;

create trigger saved_old_price_before
	before update 
	on products
	for each row 
	execute procedure save_old_price();  

--second trigger
drop function del_messege cascade;

create or replace function del_messege()
  returns trigger
  language plpgsql
  as
$$
begin 
	raise 'Old prices deleted in %', now();
	return new;
end;
$$;

drop trigger drop_products on products;

create trigger drop_products
	before delete 
	on old_price
	for statement
	execute procedure del_messege();

begin;

select * from old_price;

update products set price = 90.90909090
	where price > 105 and category_id = 1;

select * from old_price;

savepoint befor_delete;

delete from old_price
	where price > 105;

select * from old_price;

release savepoint befor_delete;
rollback to savepoint befor_delete;
rollback;
--commit;
