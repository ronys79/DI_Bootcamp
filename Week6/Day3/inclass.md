CREATE TABLE actors (
  actor_id SERIAL PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  birthdate DATE, 
  number_oscars INTEGER
);

CREATE TABLE country (
    country_id SERIAL PRIMARY KEY,
    country_name VARCHAR(50));

INSERT INTO country (country_name)
VALUES
('France'),
('Spain'),
('Italy'),
('Israel'),
('China');

INSERT into actors (first_name, last_name, birthdate, number_oscars)
VALUES
('Brad', 'Pitt', '05-05-1950', 5),
('Matt', 'Damon', '01-01-1960',1),
('Jack', 'Nicholson', '01-01-1940', 6),
('Al', 'Pacino', '05-03-1957', 5);

-- JOIN TYPE 

SELECT t_left.country_id, t_right.actor_id, t_left.country_name, t_right.first_name, t_right.last_name
FROM country  t_left
INNER JOIN actors t_right
ON t_left.country_id = t_right.actor_id;

SELECT t_left.country_id country, t_right.actor_id id_, t_left.country_name, t_right.first_name, t_right.last_name
FROM country t_left
FULL OUTER JOIN actors t_right
ON t_left.country_id = t_right.actor_id;

SELECT t_left.country_id country, t_right.actor_id id_, t_left.country_name, t_right.first_name, t_right.last_name
FROM country t_left
LEFT OUTER JOIN actors t_right
ON t_left.country_id = t_right.actor_id;

SELECT t_left.country_id country, t_right.actor_id id_, t_left.country_name, t_right.first_name, t_right.last_name
FROM country t_left
RIGHT OUTER JOIN actors t_right
ON t_left.country_id = t_right.actor_id;

--DROP TABLE actors;

-- ON DELETE RESTRICT/CASCADE
CREATE TABLE colors(
color_id SERIAL PRIMARY KEY,
color_name TEXT);
INSERT INTO colors (color_name)
VALUES ('yellow'), ('black'), ('orange'), ('white');
CREATE TABLE cars(
car_id SERIAL PRIMARY KEY,
-- car_color INTEGER REFERENCES colors (color_id) ON DELETE RESTRICT,
car_color INTEGER REFERENCES colors (color_id) ON DELETE CASCADE,
car_name TEXT);
INSERT INTO cars (car_color, car_name)
VALUES (1, 'Mazda'), (2, 'Peugeot'), (4, 'Toyota');
SELECT * FROM cars;
DELETE FROM colors where color_name = 'yellow';
--DROP TABLE colors, cars;
--SELECT * FROM colors;
-- JOIN + GROUP BY + HAVING CMD
SELECT cars.car_name, colors.color_name, COUNT(car_color) as color 
FROM cars 
INNER JOIN colors 
ON cars.car_color = colors.color_id
GROUP BY cars.car_name, colors.color_name
HAVING colors.color_name = 'white';
SELECT * FROM cars;
INSERT INTO cars (car_color, car_name) VALUES ('4', 'Toyota'), ('4', 'Toyota'), ('4', 'Toyota'),('4', 'Toyota');
INSERT INTO cars (car_color, car_name) VALUES ('4', 'Peugeot');
-- UNION CMD
SELECT
    car_name
FROM
    cars
UNION
SELECT
    color_name
FROM
    colors
ORDER BY 
 car_name ASC ;