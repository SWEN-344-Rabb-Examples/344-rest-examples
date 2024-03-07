
DROP TABLE IF EXISTS food;
DROP TABLE IF EXISTS drink;
DROP TABLE IF EXISTS pairings_menu;
DROP TABLE IF EXISTS menu_orders;

CREATE TABLE pairings_menu(
  id SERIAL PRIMARY KEY,
  food_id INT NOT NULL,
  drink_id INT NOT NULL,
  price FLOAT,
  tax DECIMAL DEFAULT 0.7
);

CREATE TABLE menu_orders(
  id SERIAL PRIMARY KEY,
  menu_id INT NOT NULL,
  coupon_code VARCHAR(256),
  final_price FLOAT
);

CREATE TABLE food(
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL
);

CREATE TABLE drink(
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL
);

INSERT INTO food(id,name) VALUES
  (1,'burger'),
  (2,'steak'),
  (3,'quiche'),
  (4,'lasgana'),
  (5,'tempura'),
  (6,'hot and sour soup'),
  (7,'steak and kidney pie');
-- Restart our primary key sequences here so inserting new record id won't collide
ALTER SEQUENCE food_id_seq RESTART 8;

INSERT INTO drink(id, name) VALUES
  (7,'soda'),
  (6,'red wine'),
  (5, 'champagne'),
  (4, 'Sangiovese'),
  (3, 'sake'),
  (2, 'water'),
  (1, 'guinness'),
  (8, 'kirin');

ALTER SEQUENCE drink_id_seq RESTART 9;

INSERT INTO pairings_menu(food_id, drink_id, price) VALUES
  (1, 7, '5.0'),
  (2, 6, '25.0'),
  (3, 5, '20.0'),
  (4, 4, '18.0'),
  (5, 3, '22.0'),
  (6, 2, '7.0'),
  (7, 1, '19.0');

