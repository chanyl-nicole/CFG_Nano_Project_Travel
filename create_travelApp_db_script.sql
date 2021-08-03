CREATE DATABASE travelApp;
USE travelApp;

##############

### For option 3: RapidAPI - calculates COVID safety index

CREATE TABLE `CovidSafetyInfo` (
  `DestinationCountry` varchar(45) NOT NULL,
  `DestinationCity` varchar(45) NOT NULL,
  `WarningColor` varchar(10) NOT NULL, # green, yellow, red
  `SafetyIndex` int DEFAULT '0' NOT NULL, # between 0 and 10, 10 is safest
  `RiskLevel` varchar(10) NOT NULL, # Low, Medium, High
  `TravelRestrictions` varchar(???) NOT NULL,
  PRIMARY KEY (`DestinationCountry`,`DestinationCity`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
# ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

#### For option 2: Travel Advice API - gives back info on Covid requirements
    # I dont see a clear API output for vaccine requirements!

CREATE TABLE `CovidSafetyRequirements` (
  `OriginCity` varchar(45) NOT NULL,
  `DestinationCity` varchar(45) NOT NULL,
  `TestRequired` bit(1) '0' NOT NULL,                # bit for boolean, 0 for FALSE, 1 for TRUE
  `QuarantineRequired` bit(1) '0' NOT NULL,                # bit for boolean, 0 for FALSE, 1 for TRUE
  `MaskRequired` bit(1) '0' NOT NULL,                # bit for boolean, 0 for FALSE, 1 for TRUE
  `Recommendations` varchar(???) NOT NULL,  # I would not add this, output is really long
  PRIMARY KEY (`OriginCity`,`DestinationCity`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
# ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

## For adding weather API component plus essential items if we decide to

CREATE TABLE `DestinationWeather` (
    `DestinationCity` varchar(45) NOT NULL,
    `RainyWeather` bit(1) '0' NOT NULL,              # yes/no
    `AvgMaxTemperature` int DEFAULT '0' NOT NULL, # optional
    `AvgMinTemperature` int DEFAULT '0' NOT NULL,  # optional
    `AverageDailyTemperature` int DEFAULT '0' NOT NULL, # ??
    )

# Example top destinations in Europe: Paris, London, Rome, Florence, Barcelona, Swiss Alps, Amsterdam, Santorini.
# Might not need API for this

CREATE TABLE `CityWeatherByMonth` (
    `Month` varchar(45) NOT NULL, # month must be a special data type (check)
    `DestinationCity` varchar(45) NOT NULL,
    `WeatherType` varchar(45) NOT NULL, # should be: Rainy-hot, Rainy-cold, Dry-hot, Dry-cold
    )

INSERT INTO `CityWeatherByMonth`
(`Month`, `DestinationCity`, `WeatherType`)
VALUES
('January', 'Paris', 'Dry-cold'),
('January', 'London', 'Rainy-cold'), ......

CREATE TABLE `EssentialItems` (
    `EssentialItem` varchar(45) NOT NULL,
    `RainyHotWeather` bit(1) '0' NOT NULL,              # yes/no  # for example, if Avg temp > 15; or AvgMaxTemp > 20
    `RainyColdWeather` bit(1) '0' NOT NULL,              # yes/no # for example, if Avg temp < 15
    `DryHotWeather` bit(1) '0' NOT NULL,              # yes/no
    `DryColdWeather` bit(1) '0' NOT NULL,              # yes/no
    `ItemNeeded` bit(1) '0' NOT NULL,                # yes/no
    )

INSERT INTO `EssentialItemsNeeded`
(`EssentialItem`, `RainyHotWeather`, `RainyColdWeather`, `DryHotWeather`,
 `DryColdWeather`)
VALUES
('Umbrella', 1, 1, 0, 0),
('RainJacket', 1, 1, 0, 0),
('DryBag', 1, 1, 0, 0),
('WaterProofShoes', 0, 1, 0, 1),
('Coat', 0, 1, 0, 1),
('WarmBaseLayer', 0, 1, 0, 1),
('Buff', 0, 1, 0, 1),
('Gloves', 0, 1, 0, 1),
('Moisturiser', 0, 0, 1, 1),
('LipBalm', 0, 0, 1, 1),
('SunScreen', 1, 0, 1, 1),
('AfterSunCream', 1, 0, 1, 1),
('Sunglasses', 1, 0, 1, 1),
('Hat', 1, 0, 1, 1),
('MoistureWickingClothing', 1, 0, 1, 1),
('CollapsibleWaterBottle', 1, 0, 1, 0,
('PortableMiniFan', 1, 0, 1, 0),
('TravelTowel', 1, 0, 1, 0),
('CoolingTowel', 1, 0, 1, 0),
('CoolingFacialMist', 1, 0, 1, 0),
('InsectRepellent', 1, 0, 0, 0);

###########################################  OTHER  GENERAL STUFF BELOW

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
