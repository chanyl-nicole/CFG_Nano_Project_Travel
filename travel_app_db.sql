-- DROP DATABASE travelApp;

CREATE DATABASE travelApp;
USE travelApp;

-- # NOTES:
-- # Top 8 destinations in Europe: Paris, London, Rome, Florence, Barcelona, Swiss Alps, Amsterdam, Santorini.
-- # Data for the summer months (June, July, August, September) for the top 8 holiday destinations in Europe
-- #   Warm weather considered that with average maximum temperature = or < 15C ; Cold weather < 15C
-- #   Wet weather considered that with average rainfall = > 50 mm ; Dry weather < 50 mm

CREATE TABLE Country (
    Country_id INT PRIMARY KEY AUTO_INCREMENT,
    Country VARCHAR(50) NOT NULL
);
 INSERT INTO Country(Country)
 VALUES('France'),('United Kingdom'),('Italy'),('Switzerland'),
 ('Greece'),('Spain'),('Netherlands');

CREATE TABLE Months (
    month_id INT PRIMARY KEY AUTO_INCREMENT,
    Month VARCHAR(20) NOT NULL
);
 INSERT INTO Months(Month)
VALUES('June'),('July'),('August'),('September');

CREATE TABLE Weather (
    Weather_type_id INT PRIMARY KEY AUTO_INCREMENT,
    Weather_type TEXT NOT NULL
);
INSERT INTO Weather(Weather_type)
VALUES('Rainy and Warm'),('Rainy and Cold'),('Dry and Warm'),('Dry and Cold');



CREATE TABLE Essential_Items (
    Item_id INT PRIMARY KEY AUTO_INCREMENT,
    Item TEXT NOT NULL,
    Suitable_weather INT NOT NULL,
    FOREIGN KEY (Suitable_weather)
        REFERENCES weather (weather_type_id)
);

INSERT INTO Essential_Items(Item, Suitable_weather)
VALUES
('Umbrella',1),('Umbrella',2),('Rain Jacket',1),('Rain Jacket',2),
('Dry Bag',1),('Dry Bag',2), ('Waterproof Shoes',1),('Waterproof Shoes',2),
('Coat',2),('Coat',4),('Warm Base Layer',2),('Warm Base Layer',4),('Buff',2),('Buff',4),
('Gloves',2),('Gloves',4),('Moisturiser',3), ('Moisturiser',4),('LipBalm',3),('LipBalm',4),
('SunScreen',3),('SunScreen',4),('After-Sun Cream',1),('After-Sun Cream',3),
('After-Sun Cream',4),('Sunglasses',1),('Sunglasses',3),('Sunglasses',4),
('Hat',1),('Hat',3),('Hat',4),('Sandals',1),('Sandals',3),
('Portable Mini Fan',1),('Portable Mini Fan',3),('Travel Towel',1),('Travel Towel',3),
('Cooling Towel',1),('Cooling Towel',3),('Cooling Facial Mist',1),('Cooling Facial Mist',3),
('Moisture-Wicking Clothing',1),('Moisture-Wicking Clothing',3),('Moisture-Wicking Clothing',4),
('Collapsible Water Bottle',1), ('Collapsible Water Bottle',3),('Insect Repellent',1);

CREATE TABLE City (
    City_id INT PRIMARY KEY AUTO_INCREMENT,
    City VARCHAR(50) NOT NULL,
    Country_id INT NOT NULL,
    FOREIGN KEY (Country_id)
        REFERENCES Country (Country_id),
    Month_id INT NOT NULL,
    Weather_type_id INT NOT NULL,
    FOREIGN KEY (Weather_type_id)
        REFERENCES weather (weather_type_id),
    FOREIGN KEY (Month_id)
        REFERENCES Months (month_id)
);

INSERT INTO CITY(City, Country_id,Month_id, Weather_type_id)
VALUES  ('Paris',1,1,1),('Paris',1,2,1),('Paris',1,3,3),('Paris',1,4,3),
('London',2,1,1), ('London',2,2,1),('London',2,3,3),('London',2,4,1),
('Rome',3,1,3),('Rome',3,2,3),('Rome',3,3,3),('Rome',3,4,1),
('Florence',3,1,1),('Florence',3,2,1),('Florence',3,3,3),('Florence',3,4,1),
('Santorini',5,1,3), ('Santorini',5,2,3),('Santorini',5,3,3),('Santorini',5,4,3),
('Swiss Alps',4,1,2), ('Swiss Alps',4,2,2),('Swiss Alps',4,3,2),('Swiss Alps',4,4,2),
('Barcelona',6,1,3), ('Barcelona',6,2,3), ('Barcelona',6,3,3),('Barcelona',6,4,1),
('Amsterdam',7,1,1),('Amsterdam',7,2,1),('Amsterdam',7,3,1),('Amsterdam',7,4,1);




CREATE TABLE My_Essentials (
    MyEssentialItem VARCHAR(45),
    CONSTRAINT PK_item PRIMARY KEY (MyEssentialItem)
);
