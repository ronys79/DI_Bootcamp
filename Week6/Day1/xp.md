CREATE TABLE items(
item_id SERIAL PRIMARY KEY,
item VARCHAR (50) NOT NULL,
price DECIMAL(10,2) NOT NULL
);

CREATE TABLE customers(
item_id SERIAL PRIMARY KEY,
first_name VARCHAR (100) NOT NULL,
last_name VARCHAR (100) NOT NULL
);

INSERT INTO items (item, price)
VALUES
('Small Desk', 100),
('Large desk', 300),
('Fan', 80);
	
INSERT INTO customers (first_name, last_name)
VALUES
('Greg', 'Jones'),
('Sandra', 'Jones'),
('Scott', 'Scott'),
('Trevor', 'Green'),
('Melanie', 'Johnson');

-- All the items.
SELECT * FROM items;

-- All the items with a price above 80 (80 not included).
SELECT * FROM items WHERE price > 80;

-- All the items with a price below 300. (300 included)
SELECT * FROM items WHERE price <= 300;

-- All customers whose last name is ‘Smith’ (What will be your outcome?).
SELECT * FROM customers WHERE last_name LIKE 'Smith';

-- All customers whose last name is ‘Jones’.
SELECT * FROM customers WHERE last_name LIKE 'Jones';

-- All customers whose firstname is not ‘Scott’.
SELECT * FROM customers WHERE last_name != 'Scott';