
DROP TABLE IF EXISTS menu_table;

CREATE TABLE menu_table(
  id SERIAL PRIMARY KEY,
  food TEXT NOT NULL,
  drink TEXT NOT NULL,
  price VARCHAR(10),
  tax DECIMAL DEFAULT 0.7
);

INSERT INTO menu_table(food, drink, price) VALUES
  ('burger', 'soda', '5.0'),
  ('steak', 'red wine', '25.0'),
  ('quiche', 'champagne', '20.0'),
  ('lasgana', 'Sangiovese', '18.0'),
  ('tempura', 'sake', '22.0'),
  ('hot and sour soup', 'water', '7.0'),
  ('steak and kidney pie', 'guinness', '19.0')
;

-- Restart our primary key sequences here so inserting id=DEFAULT won't collide
--ALTER SEQUENCE example_table_id_seq RESTART 1000;
DROP TABLE IF EXISTS BOOKS;
CREATE TABLE BOOKS (
  ID SERIAL PRIMARY KEY,
  AUTHOR VARCHAR(200),
  TITLE VARCHAR(200),
  SUMMARY VARCHAR(200),
  TYPE VARCHAR(30)
);

INSERT INTO BOOKS (TITLE, AUTHOR, SUMMARY, TYPE) VALUES 
('Nicholas Nickleby','Charles Dickens','Trials and Tribulations of the Nickelby family', 'Fiction'),
('Oliver Twist','Charles Dickens','Fagin: Child Labour purveyor','Fiction'),
('2001: A Space Odyssey','Arthur C. Clarke','Hal - Please open the doors','Fiction'),
('Do Androids Dream of Electric Sheep','Philip K. Dick','Voight-Kampf or CAPTCHA?','Fiction'),
('I, Robot','Isaac Asimov','The three laws of Robotics','Fiction'),
('A Hitchhikers Guide to the Galaxy','Douglas Adams','Don''t panic','Fiction'),
('Roots: The Saga of an American Family','Alex Haley','Gripping and enlightening','Fiction'),
('Cosmos','Carl Sagan','Billions and Billions','Non-Fiction'),
('A Brief History of Time','Stephen Hawking','Any physical theory is always provisional','Non-Fiction'),
('In Cold Blood','Truman Capote','In school we only learn to recognize the words and to spell','Non-Fiction'),
('The Sixth Extinction: An Unnatural History','Elizabeth Kolbert','Are we seeing this happen in front of our eyes?','Non-Fiction'),
('On the Clock: What Low-Wage Work Did to Me and How It Drives America Insane','Emily Guendelsberger' ,'Why we need unions', 'Non-Fiction'),
('A Study In Scarlet','Arthur Conan Doyle','Elementary!  We see, but we do not observe','Fiction'),
('Nightfall and other stories','Isaac Asimov','Darkness is coming','Fiction'),
('Foundation','Isaac Asimov','Psychohistory - the prediction of group thinking','Fiction');


