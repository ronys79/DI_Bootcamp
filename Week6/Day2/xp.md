SELECT * FROM items ORDER BY price ASC;

WHERE price > 80 ORDER BY price DESC;

SELECT first_name, last_name FROM customers ORDER BY first_name DESC LIMIT 3;

SELECT last_name FROM customers ORDER BY first_name DESC LIMIT 3;

SELECT last_name FROM customers ORDER BY first_name ASC;

CREATE TABLE purchases(
id SERIAL,
customer_id INT NOT NULL,
item_id INT NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (customer_id) REFERENCES customers (item_id),
FOREIGN KEY (item_id) REFERENCES items (item_id)
);

Add 5 rows which reference existing customers and items.

INSERT INTO purchase (items_id, customers_id) VALUES ((SELECT customers_id from customers WHERE customers_id = 1), (SELECT items_id from items WHERE items_id = 1))
INSERT INTO purchase (items_id, customers_id) VALUES ((SELECT customers_id from customers WHERE customers_id = 2), (SELECT items_id from items WHERE items_id = 2))
INSERT INTO purchase (items_id, customers_id) VALUES ((SELECT customers_id from customers WHERE customers_id = 3), (SELECT items_id from items WHERE items_id = 3))
INSERT INTO purchase (items_id, customers_id) VALUES ((SELECT customers_id from customers WHERE customers_id = 4), (SELECT items_id from items WHERE items_id = 4))
INSERT INTO purchase (items_id, customers_id) VALUES ((SELECT customers_id from customers WHERE customers_id = 5), (SELECT items_id from items WHERE items_id = 5));


SELECT customers.first_name, customer.last_name, items.item FROM customers
INNER JOIN purchases
ON customers.customers_id = purchase.customer_id
INNER JOIN items
ON purchases.item_id = items.item_id;


select * from purchases where cust_id=4

select items.name_item,purchases.id from items inner join purchases on items.item_id=purchases.item_id where items.name_item = 'Small Desk' or items.name_item='Large Desk';

INSERT INTO items (name_item, price) VALUES ('Hard Drive',250); INSERT INTO purchases (cust_id,item_id) VALUES ( (SELECT cust_id from customer WHERE first_name='Scott'),(SELECT item_id from items WHERE name_item='Hard Drive'));

SELECT customer.first_name,customer.last_name,items.name_item FROM purchases INNER JOIN customer ON purchases.cust_id = customer.cust_id INNER JOIN items ON purchases.item_id = items.item_id;

select * from customer

select concat(first_name,' ',last_name) as full_name from customer

SELECT DISTINCT create_date FROM customer;

select * from customer order by first_name desc

select film_id,title,description,release_year,rental_rate from film order by rental_rate asc

select address,phone,district from address where district = 'Texas';

select * from film where film_id = 15 or film_id=150

select film_id,title,description,length,rental_rate from film where title = 'Baked Cleopatra';

select film_id,title,description,length,rental_rate from film where title like 'Ba%';

select title from film order by rental_rate asc limit 10

select title from film order by rental_rate asc limit 10 offset 10

SELECT concat(customer.first_name,' ',customer.last_name) as customer_name,payment.amount,payment.payment_date FROM payment INNER JOIN customer ON payment.customer_id=customer.customer_id order by payment.customer_id asc;

select film.title from film join inventory on film.film_id=inventory.film_id where film.film_id not in (inventory.film_id)

select film.title from film join inventory on film.film_id=inventory.film_id where film.film_id not in (select film_id from inventory)

select city.city,country.country from city join country on city.country_id=country.country_id