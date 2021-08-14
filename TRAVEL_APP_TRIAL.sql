-- DROP DATABASE travelApp;

CREATE DATABASE travelApptrial;
USE travelApptrial;

-- # NOTES:
-- # Top 8 destinations in Europe: Paris, London, Rome, Florence, Barcelona, Swiss Alps, Amsterdam, Santorini.
-- # Data for the summer months (June, July, August, September) for the top 8 holiday destinations in Europe
-- #   Warm weather considered that with average maximum temperature = or < 15C ; Cold weather < 15C
-- #   Wet weather considered that with average rainfall = > 50 mm ; Dry weather < 50 mm



CREATE TABLE City (
    City_id INT PRIMARY KEY AUTO_INCREMENT,
    City VARCHAR(50) NOT NULL,
    Country_id INT NOT NULL,
    FOREIGN KEY (Country)
        REFERENCES Country (Country_id),
    Month_id INT NOT NULL,
    Weather_type_id INT NOT NULL,
    FOREIGN KEY (Weather_type_id)
        REFERENCES weather (weather_type_id),
    FOREIGN KEY (Month_id)
        REFERENCES Months (month_id)
);

INSERT INTO CITY(City, Country,Month_id, Weather_type_id)
VALUES  ('Paris',1,1,1),('Paris',1,2,1),('Paris',1,3,3),('Paris',1,4,3),
('London',2,1,1), ('London',2,2,1),('London',2,3,3),('London',2,4,1),
('Rome',3,1,3),('Rome',3,2,3),('Rome',3,3,3),('Rome',3,4,1),
('Florence',3,1,1),('Florence',3,2,1),('Florence',3,3,3),('Florence',3,4,1),
('Santorini',5,1,3), ('Santorini',5,2,3),('Santorini',5,3,3),('Santorini',5,4,3),
('Swiss Alps',4,1,2), ('Swiss Alps',4,2,2),('Swiss Alps',4,3,2),('Swiss Alps',4,4,2),
('Barcelona',6,1,3), ('Barcelona',6,2,3), ('Barcelona',6,3,3),('Barcelona',6,4,1),
('Amsterdam',7,1,1),('Amsterdam',7,2,1),('Amsterdam',7,3,1),('Amsterdam',7,4,1);


CREATE TABLE Weather (
    Weather_type_id INT PRIMARY KEY AUTO_INCREMENT,
    Weather_type TEXT NOT NULL
);
INSERT INTO Weather(Weather_type)
VALUES('Rainy and Warm'),('Rainy and Cold'),('Dry and Warm'),('Dry and Cold');

drop table months;
CREATE TABLE Months (
    month_id INT PRIMARY KEY AUTO_INCREMENT,
    Month VARCHAR(20) NOT NULL
);
 INSERT INTO Months(Month)
VALUES('June'),('July'),('August'),('September');
  SELECT Country FROM Countries  as cnt
                    JOIN City as c ON c.Country_id =cnt.country_id
                    where c.city = 'London';

CREATE TABLE Country (
    Country_id INT PRIMARY KEY AUTO_INCREMENT,
    Country VARCHAR(50) NOT NULL
);
 INSERT INTO Country(Country)
 VALUES('France'),('United Kingdom'),('Italy'),('Switzerland'),
 ('Greece'),('Spain'),('Netherlands');

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

CREATE TABLE My_Essentials (
    MyEssentialItem VARCHAR(45),
    CONSTRAINT PK_item PRIMARY KEY (MyEssentialItem)
);

--
-- ##############  COVID STUFF
--
-- ### For option 3: RapidAPI - calculates COVID safety index
--
-- CREATE TABLE `CovidSafetyInfo` (
--  `DestinationCountry` varchar(45) NOT NULL,
--  `DestinationCity` varchar(45) NOT NULL,
--  `WarningColor` varchar(10) NOT NULL, # green, yellow, red
--  `SafetyIndex` int DEFAULT '0' NOT NULL, # between 0 and 10, 10 is safest
--  `RiskLevel` varchar(10) NOT NULL, # Low, Medium, High
--  `TravelRestrictions` varchar(???) NOT NULL,
--  PRIMARY KEY (`DestinationCountry`,`DestinationCity`)
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- # ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
--
-- #### For option 2: Travel Advice API - gives back info on Covid requirements
--    # I dont see a clear API output for vaccine requirements!
--
-- CREATE TABLE `CovidSafetyRequirements` (
--  `OriginCity` varchar(45) NOT NULL,
--  `DestinationCity` varchar(45) NOT NULL,
--  `TestRequired` bit(1) '0' NOT NULL,                # bit for boolean, 0 for FALSE, 1 for TRUE
--  `QuarantineRequired` bit(1) '0' NOT NULL,                # bit for boolean, 0 for FALSE, 1 for TRUE
--  `MaskRequired` bit(1) '0' NOT NULL,                # bit for boolean, 0 for FALSE, 1 for TRUE
--  `Recommendations` varchar(???) NOT NULL,  # I would not add this, output is really long
--  PRIMARY KEY (`OriginCity`,`DestinationCity`)
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- # ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
--
-- ###########################################  OTHER  GENERAL STUFF BELOW
--
-- CREATE TABLE `CovidRestrictionsByCountry` (
--  `DestinationCountry` varchar(45) NOT NULL,
--  `VaccineRequired` bit(1) '0' NOT NULL,                # bit for boolean, 0 for FALSE, 1 for TRUE
--  `TimePostVaccination` int DEFAULT '0' NOT NULL,
--  `PCRrequired` bit(1) '0' NOT NULL,
--  `PCRvalidTime` int DEFAULT '0',                       # should be hours
--  `IsolationPeriod` int DEFAULT '0' NOT NULL,           # should be days
--  `HotelIsolation` bit(1) '0' NOT NULL,                 # bit for boolean, 0 for FALSE, 1 for TRUE
--  `NumberTestRequired` int DEFAULT '0' NOT NULL,
--  `DateTest1` date,
--  `DateTest2` date,
--  PRIMARY KEY (``,``,``)
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- # ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
--
-- # normalisation and relational integrity
-- # define primary keys, foreign keys as needed
--
-- ####### Ideas to make smaller tables and then relate them somehow .....
--
-- CREATE TABLE `Vaccination` (
--  `DestinationCountry` varchar(45) NOT NULL,
--  `VaccineRequired` bit(1) '0' NOT NULL,                # bit for boolean, 0 for FALSE, 1 for TRUE
--  `TimePostVaccination` int DEFAULT '0' NOT NULL
--  )
--
-- CREATE TABLE `Quarantine` (
--  `DestinationCountry` varchar(45) NOT NULL,
--  `IsolationPeriod` int DEFAULT '0' NOT NULL,           # should be days
--  `HotelIsolation` bit(1) '0' NOT NULL,                 # bit for boolean, 0 for FALSE, 1 for TRUE
--    )
--
-- CREATE TABLE `PreArrivalTest` (
--  `DestinationCountry` varchar(45) NOT NULL,
--  `TestRequired` bit(1) '0' NOT NULL,
--  `TestType` varchar(45) NOT NULL
--    )
--
-- CREATE TABLE `PreArrivalTestPCR` (
--  `DestinationCountry` varchar(45) NOT NULL,
--  `PCRrequired` bit(1) '0' NOT NULL,
--  `PCRvalidTimeFrame` int DEFAULT '0',                       # should be hours
--    )
--
-- CREATE TABLE `PreArrivalTestAntigen` (
--  `DestinationCountry` varchar(45) NOT NULL,
--  `AgTestRequired` bit(1) '0' NOT NULL,
--  `AgTestValidTimeFrame` int DEFAULT '0',                       # should be hours
--    )
--
-- CREATE TABLE `PostArrivalTest` (
--  `DestinationCountry` varchar(45) NOT NULL,
--  `TestRequired` bit(1) '0' NOT NULL,
--  `NumberTestRequired` int DEFAULT '0',
--  `DateTest1` date,
--  `DateTest2` date.....
--    )
