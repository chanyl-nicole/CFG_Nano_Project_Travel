CREATE DATABASE travelApp;
USE travelApp;

CREATE TABLE `CovidRestrictionsByCountry` (
  `DestinationCountry` varchar(45) NOT NULL,
  `VaccineRequired` bit(1) '0' NOT NULL,                # bit for boolean, 0 for FALSE, 1 for TRUE
  `TimePostVaccination` int DEFAULT '0' NOT NULL,
  `PCRrequired` bit(1) '0' NOT NULL,
  `PCRvalidTime` int DEFAULT '0',                       # should be hours
  `IsolationPeriod` int DEFAULT '0' NOT NULL,           # should be days
  `HotelIsolation` bit(1) '0' NOT NULL,                 # bit for boolean, 0 for FALSE, 1 for TRUE
  `NumberTestRequired` int DEFAULT '0' NOT NULL,
  `DateTest1` date,
  `DateTest2` date,
  PRIMARY KEY (``,``,``)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
# ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

# normalisation and relational integrity
# define primary keys, foreign keys as needed

####### Ideas to make smaller tables and then relate them somehow .....

CREATE TABLE `Vaccination` (
  `DestinationCountry` varchar(45) NOT NULL,
  `VaccineRequired` bit(1) '0' NOT NULL,                # bit for boolean, 0 for FALSE, 1 for TRUE
  `TimePostVaccination` int DEFAULT '0' NOT NULL
  )

CREATE TABLE `Quarantine` (
  `DestinationCountry` varchar(45) NOT NULL,
  `IsolationPeriod` int DEFAULT '0' NOT NULL,           # should be days
  `HotelIsolation` bit(1) '0' NOT NULL,                 # bit for boolean, 0 for FALSE, 1 for TRUE
  `NumberTestRequired` int DEFAULT '0' NOT NULL
    )

CREATE TABLE `PreArrivalTest` (
  `DestinationCountry` varchar(45) NOT NULL,
  `TestRequired` bit(1) '0' NOT NULL,
  `TestType` varchar(45) NOT NULL
    )

CREATE TABLE `PreArrivalTestPCR` (
  `DestinationCountry` varchar(45) NOT NULL,
  `PCRrequired` bit(1) '0' NOT NULL,
  `PCRvalidTimeFrame` int DEFAULT '0',                       # should be hours
    )

CREATE TABLE `PreArrivalTestAntigen` (
  `DestinationCountry` varchar(45) NOT NULL,
  `AgTestRequired` bit(1) '0' NOT NULL,
  `AgTestValidTimeFrame` int DEFAULT '0',                       # should be hours
    )

CREATE TABLE `PostArrivalTest` (
  `DestinationCountry` varchar(45) NOT NULL,
  `TestRequired` bit(1) '0' NOT NULL,
  `NumberTestRequired` int DEFAULT '0',
  `DateTest1` date,
  `DateTest2` date.....
    )

######## OPTIONAL  STUFF  (just ideas, not sure about fields etc)

CREATE TABLE `DestinationWeather` (
    `DestinationCountry` varchar(45) NOT NULL,
    `RainyWeather` bit(1) '0' NOT NULL,              # yes/no
    `MaxTemperature` int DEFAULT '0' NOT NULL,
    `MinTemperature` int DEFAULT '0' NOT NULL
    )

CREATE TABLE `EssentialItems` (
    `EssentialItem` varchar(45) NOT NULL,
    `RainyHotWeather` bit(1) '0' NOT NULL,              # yes/no
    `RainyColdWeather` bit(1) '0' NOT NULL,              # yes/no
    `DryHotWeather` bit(1) '0' NOT NULL,              # yes/no
    `DryColdWeather` bit(1) '0' NOT NULL,              # yes/no
    `ItemNeeded` bit(1) '0' NOT NULL,                # yes/no
    )
