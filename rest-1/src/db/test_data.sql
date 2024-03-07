
DROP TABLE IF EXISTS pairings_menu cascade;
DROP TABLE IF EXISTS food cascade;
DROP TABLE IF EXISTS drink cascade;

CREATE TABLE pairings_menu(
  id SERIAL PRIMARY KEY,
  food_id INT NOT NULL,
  drink_id INT NOT NULL,
  price FLOAT,
  tax DECIMAL DEFAULT 0.7
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
  (1, 'guinness');

ALTER SEQUENCE drink_id_seq RESTART 8;

INSERT INTO pairings_menu(food_id, drink_id, price) VALUES
  (1, 7, '5.0'),
  (2, 6, '25.0'),
  (3, 5, '20.0'),
  (4, 4, '18.0'),
  (5, 3, '22.0'),
  (6, 2, '7.0'),
  (7, 1, '19.0');



DROP TABLE IF EXISTS dates_x;
CREATE TABLE dates_x(
  id SERIAL PRIMARY KEY,
  name VARCHAR(256),
  the_date DATE
);
INSERT INTO dates_x (id, name, the_date) VALUES (1, 'Albert Camus', '04/14/1945');