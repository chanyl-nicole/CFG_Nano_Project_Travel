CREATE DATABASE travelApp;
USE travelApp;

### Stuff for adding weather and essential items feature if we decide to do so

# Top 8 destinations in Europe: Paris, London, Rome, Florence, Barcelona, Swiss Alps, Amsterdam, Santorini.

# NOTES:
# Data for the summer months (June, July, August, September) for the top 8 holiday destinations in Europe
#   Warm weather considered that with average maximum temperature = or < 15C ; Cold weather < 15C
#   Wet weather considered that with average rainfall = > 50 mm ; Dry weather < 50 mm

CREATE TABLE `CityWeatherByMonth` (
    `Month` varchar(20) NOT NULL, # month must be a special data type (check)
    `DestinationCity` varchar(45) NOT NULL,
    `WeatherType` varchar(45) NOT NULL, # Options: RainyWarm, RainyCold, DryWarm, DryCold
    CONSTRAINT PK_month_destination PRIMARY KEY (`Month`,`DestinationCity`)
    );

    # This table has a composite primary key to identify unique entries

INSERT INTO `CityWeatherByMonth`
(`Month`, `DestinationCity`, `WeatherType`)
VALUES
('June', 'Paris', 'RainyWarm'),
('June', 'London', 'RainyWarm'),
('June', 'Rome', 'DryWarm'),
('June', 'Florence', 'RainyWarm'),
('June', 'Barcelona', 'DryWarm'),
('June', 'Swiss Alps', 'RainyCold'),
('June', 'Amsterdam', 'RainyWarm'),
('June', 'Santorini', 'DryWarm'),
('July', 'Paris', 'RainyWarm'),
('July', 'London', 'DryWarm'),
('July', 'Rome', 'DryWarm'),
('July', 'Florence', 'DryWarm'),
('July', 'Barcelona', 'DryWarm'),
('July', 'Swiss Alps', 'RainyCold'),
('July', 'Amsterdam', 'RainyWarm'),
('July', 'Santorini', 'DryWarm'),
('August', 'Paris', 'DryWarm'),
('August', 'London', 'RainyWarm'),
('August', 'Rome', 'DryWarm'),
('August', 'Florence', 'RainyWarm'),
('August', 'Barcelona', 'DryWarm'),
('August', 'Swiss Alps', 'RainyCold'),
('August', 'Amsterdam', 'RainyWarm'),
('August', 'Santorini', 'DryWarm'),
('September', 'Paris', 'DryWarm'),
('September', 'London', 'RainyWarm'),
('September', 'Rome', 'RainyWarm'),
('September', 'Florence', 'RainyWarm'),
('September', 'Barcelona', 'RainyWarm'),
('September', 'Swiss Alps', 'RainyCold'),
('September', 'Amsterdam', 'RainyWarm'),
('September', 'Santorini', 'DryWarm');

CREATE TABLE `EssentialItems` (
    `EssentialItem` varchar(45) NOT NULL,
    `WeatherType` varchar(45) NOT NULL, # Options: RainyWarm, RainyCold, DryWarm, DryCold
    `ItemNeeded` bit(1) '0' NOT NULL,   # Item needed yes (1) / no (0) -- need to delete the '0'
    CONSTRAINT PK_EssentialItem_weather PRIMARY KEY (`EssentialItem`, `WeatherType`)
    );

ALTER TABLE `EssentialItems`. -- I couldn't get this bit to work with the Foreign Key
ADD CONSTRAINT
fk_weather_type
FOREIGN KEY
(`WeatherType`)
REFERENCES
`CityWeatherByMonth`
(`WeatherType`);

INSERT INTO `EssentialItemsNeeded`
(`EssentialItem`, `WeatherType`, `ItemNeeded`)
VALUES
('Umbrella', 'RainyWarm', 1),
('Umbrella', 'RainyCold', 1),
('Umbrella', 'DryWarm', 0),
('Umbrella', 'DryCold', 0),
('RainJacket', 'RainyWarm', 1),
('RainJacket', 'RainyCold', 1),
('RainJacket', 'DryWarm', 0),
('RainJacket', 'DryCold', 0),
('DryBag', 'RainyWarm', 1),
('DryBag', 'RainyCold', 1),
('DryBag', 'DryWarm', 0),
('DryBag', 'DryCold', 0),
('WaterProofShoes', 'RainyWarm', 1),
('WaterProofShoes', 'RainyCold', 1),
('WaterProofShoes', 'DryWarm', 0),
('WaterProofShoes', 'DryCold', 0),
('Coat', 'RainyWarm', 0),
('Coat', 'RainyCold', 1),
('Coat', 'DryWarm', 0),
('Coat', 'DryCold', 1),
('WarmBaseLayer', 'RainyWarm', 0),
('WarmBaseLayer', 'RainyCold', 1),
('WarmBaseLayer', 'DryWarm', 0),
('WarmBaseLayer', 'DryCold', 1),
('Buff', 'RainyWarm', 0),
('Buff', 'RainyCold', 1),
('Buff', 'DryWarm', 0),
('Buff', 'DryCold', 1),
('Gloves', 'RainyWarm', 0),
('Gloves', 'RainyCold', 1),
('Gloves', 'DryWarm', 0),
('Gloves', 'DryCold', 1),
('Moisturiser', 'RainyWarm', 0),
('Moisturiser', 'RainyCold', 0),
('Moisturiser', 'DryWarm', 1),
('Moisturiser', 'DryCold', 1),
('LipBalm', 'RainyWarm', 0),
('LipBalm', 'RainyCold', 0),
('LipBalm', 'DryWarm', 1),
('LipBalm', 'DryCold', 1),
('SunScreen', 'RainyWarm', 1),
('SunScreen', 'RainyCold', 0),
('SunScreen', 'DryWarm', 1),
('SunScreen', 'DryCold', 1),
('AfterSunCream', 'RainyWarm', 1),
('AfterSunCream', 'RainyCold', 0),
('AfterSunCream', 'DryWarm', 1),
('AfterSunCream', 'DryCold', 1),
('Sunglasses', 'RainyWarm', 1),
('Sunglasses', 'RainyCold', 0),
('Sunglasses', 'DryWarm', 1),
('Sunglasses', 'DryCold', 1),
('Hat', 'RainyWarm', 1),
('Hat', 'RainyCold', 0),
('Hat', 'DryWarm', 1),
('Hat', 'DryCold', 1),
('Sandals', 'RainyWarm', 1),
('Sandals', 'RainyCold', 0),
('Sandals', 'DryWarm', 1),
('Sandals', 'DryCold', 0),
('PortableMiniFan', 'RainyWarm', 1),
('PortableMiniFan', 'RainyCold', 0),
('PortableMiniFan', 'DryWarm', 1),
('PortableMiniFan', 'DryCold', 0),
('TravelTowel', 'RainyWarm', 1),
('TravelTowel', 'RainyCold', 0),
('TravelTowel', 'DryWarm', 1),
('TravelTowel', 'DryCold', 0),
('CoolingTowel', 'RainyWarm', 1),
('CoolingTowel', 'RainyCold', 0),
('CoolingTowel', 'DryWarm', 1),
('CoolingTowel', 'DryCold', 0),
('CoolingFacialMist', 'RainyWarm', 1),
('CoolingFacialMist', 'RainyCold', 0),
('CoolingFacialMist', 'DryWarm', 1),
('CoolingFacialMist', 'DryCold', 0),
('MoistureWickingClothing', 'RainyWarm', 1),
('MoistureWickingClothing', 'RainyCold', 0),
('MoistureWickingClothing', 'DryWarm', 1),
('MoistureWickingClothing', 'DryCold', 1),
('CollapsibleWaterBottle', 'RainyWarm', 1),
('CollapsibleWaterBottle', 'RainyCold', 0),
('CollapsibleWaterBottle', 'DryWarm', 1),
('CollapsibleWaterBottle', 'DryCold', 0),
('InsectRepellent', 'RainyWarm', 1),
('InsectRepellent', 'RainyCold', 0),
('InsectRepellent', 'DryWarm', 0),
('InsectRepellent', 'DryCold', 0);


####################

## A different option to store the data...we need to chose the one that works when we try to query the DB with python

CREATE TABLE `EssentialItems` (
    `EssentialItem` varchar(45) NOT NULL,
    `RainyWarmWeather` bit(1) '0' NOT NULL,   # Item needed yes (1) / no (0)
    `RainyColdWeather` bit(1) '0' NOT NULL,   # Item needed yes (1) / no (0)
    `DryWarmWeather` bit(1) '0' NOT NULL,     # Item needed yes (1) / no (0)
    `DryColdWeather` bit(1) '0' NOT NULL,     # Item needed yes (1) / no (0)
    CONSTRAINT PK_essential_item PRIMARY KEY (`EssentialItem`)
    );

INSERT INTO `EssentialItemsNeeded`
(`EssentialItem`, `RainyWarmWeather`, `RainyColdWeather`, `DryWarmWeather`,
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

CREATE TABLE `DestinationWeather` (
    `DestinationCity` varchar(45) NOT NULL,
    `RainyWeather` bit(1) '0' NOT NULL,              # yes/no
    `AvgMaxTemperature` int DEFAULT '0' NOT NULL, # optional
    `AvgMinTemperature` int DEFAULT '0' NOT NULL,  # optional
    `AverageDailyTemperature` int DEFAULT '0' NOT NULL, # ??
    )

##############  COVID STUFF

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
