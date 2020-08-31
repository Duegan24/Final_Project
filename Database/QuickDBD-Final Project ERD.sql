-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/uFbkmq
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


SET XACT_ABORT ON

BEGIN TRANSACTION QUICKDBD

CREATE TABLE [weather] (
    [location] CHAR(40)  NOT NULL ,
    [date_time] DATE  NOT NULL ,
    [precipMM] FLOAT  NOT NULL ,
    [visibility] INT  NOT NULL ,
    [cloudcover] INT  NOT NULL ,
    [windspeedKmph] INT  NOT NULL ,
    [humidity] INT  NOT NULL 
)

CREATE TABLE [airlines] (
    [op_carrier_airline_id] VARCHAR(10)  NOT NULL ,
    [op_unique_carrier] CHAR(2)  NOT NULL ,
    [op_carrier_name] VARCHAR  NOT NULL ,
    CONSTRAINT [PK_airlines] PRIMARY KEY CLUSTERED (
        [op_carrier_airline_id] ASC
    )
)

CREATE TABLE [airports] (
    [code] CHAR(3)  NOT NULL ,
    [city] CHAR(30)  NOT NULL ,
    [state] CHAR(2)  NOT NULL ,
    CONSTRAINT [PK_airports] PRIMARY KEY CLUSTERED (
        [code] ASC,[city] ASC
    )
)

CREATE TABLE [flight_data] (
    [ORIGIN] CHAR(3),  NOT NULL ,
    [ORIGIN_CITY] CHAR(40),  NOT NULL ,
    [DAY_OF_MONTH] DATE,  NOT NULL ,
    [DAY_OF_WEEK] INT,  NOT NULL ,
    [OP_CARRIER_AIRLINE_ID] VARCHAR(5),  NOT NULL ,
    [OP_CARRIER] CHAR(2),  NOT NULL ,
    [TAIL_NUM] VARCHAR(6),  NOT NULL ,
    [OP_CARRIER_FL_NUM] VARCHAR(4),  NOT NULL ,
    [ORIGIN_AIRPORT_ID] VARCHAR(5),  NOT NULL ,
    [ORIGIN_AIRPORT_SEQ_ID] VARCHAR(7),  NOT NULL ,
    [DEST_AIRPORT_ID] VARCHAR(5),  NOT NULL ,
    [DEST_AIRPORT_SEQ_ID] VARCHAR(7),  NOT NULL ,
    [DEST] CHAR(3),  NOT NULL ,
    [DEP_TIME] FLOAT,  NOT NULL ,
    [DEP_DEL15] FLOAT,  NOT NULL ,
    [DEP_TIME_BLK] VARCHAR(9),  NOT NULL ,
    [ARR_TIME] FLOAT,  NOT NULL ,
    [ARR_DEL15] FLOAT,  NOT NULL ,
    [CANCELLED] FLOAT,  NOT NULL ,
    [DIVERTED] FLOAT,  NOT NULL ,
    [DISTANCE] INT,  NOT NULL ,
    [DEST_CITY] CHAR(40)  NOT NULL 
)

ALTER TABLE [flight_data] WITH CHECK ADD CONSTRAINT [FK_flight_data_ORIGIN] FOREIGN KEY([ORIGIN])
REFERENCES [airports] ([code])

ALTER TABLE [flight_data] CHECK CONSTRAINT [FK_flight_data_ORIGIN]

ALTER TABLE [flight_data] WITH CHECK ADD CONSTRAINT [FK_flight_data_ORIGIN_CITY_DAY_OF_MONTH] FOREIGN KEY([ORIGIN_CITY], [DAY_OF_MONTH])
REFERENCES [weather] ([location], [date_time])

ALTER TABLE [flight_data] CHECK CONSTRAINT [FK_flight_data_ORIGIN_CITY_DAY_OF_MONTH]

ALTER TABLE [flight_data] WITH CHECK ADD CONSTRAINT [FK_flight_data_OP_CARRIER_AIRLINE_ID_OP_CARRIER] FOREIGN KEY([OP_CARRIER_AIRLINE_ID], [OP_CARRIER])
REFERENCES [airlines] ([op_carrier_airline_id], [op_unique_carrier])

ALTER TABLE [flight_data] CHECK CONSTRAINT [FK_flight_data_OP_CARRIER_AIRLINE_ID_OP_CARRIER]

ALTER TABLE [flight_data] WITH CHECK ADD CONSTRAINT [FK_flight_data_DEST] FOREIGN KEY([DEST])
REFERENCES [airports] ([code])

ALTER TABLE [flight_data] CHECK CONSTRAINT [FK_flight_data_DEST]

ALTER TABLE [flight_data] WITH CHECK ADD CONSTRAINT [FK_flight_data_DEP_TIME] FOREIGN KEY([DEP_TIME])
REFERENCES [weather] ([date_time])

ALTER TABLE [flight_data] CHECK CONSTRAINT [FK_flight_data_DEP_TIME]

ALTER TABLE [flight_data] WITH CHECK ADD CONSTRAINT [FK_flight_data_ARR_TIME] FOREIGN KEY([ARR_TIME])
REFERENCES [weather] ([date_time])

ALTER TABLE [flight_data] CHECK CONSTRAINT [FK_flight_data_ARR_TIME]

ALTER TABLE [flight_data] WITH CHECK ADD CONSTRAINT [FK_flight_data_DEST_CITY] FOREIGN KEY([DEST_CITY])
REFERENCES [airports] ([code])

ALTER TABLE [flight_data] CHECK CONSTRAINT [FK_flight_data_DEST_CITY]

COMMIT TRANSACTION QUICKDBD