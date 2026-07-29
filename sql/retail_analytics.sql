use retail_analytics;

show tables;

describe customers;

select count(*) as total_customers from customers;

select * from customers limit 10;

describe products;

select count(*) as total_products from products;

select * from products limit 10;

describe orders;

select count(*) as total_orders from orders;

select * from orders limit 10;

describe order_items;

select count(*) as total_order_items from order_items;

select * from order_items limit 10;

select count(*) from orders;

select count(*) from customers;

select count(*) from products;

select count(*) from order_items;

select o.order_id, o.order_date, c.customer_id, c.country from orders o join customers c on o.customer_id = c.customer_id limit 20;

select oi.order_id, oi.product_id, p.product_name, oi.quantity, oi.unit_price from order_items oi join products p on oi.product_id = p.product_id limit 20;