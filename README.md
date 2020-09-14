# Airline Flight Delay Analysis and Prediction

## Introduction

Business air travel is essential part of managing a company successfully even with the availability of feature-rich, remote collaboration software, such as WebEx, Zoom, and Slack. According to David Brown founder and CEO of TechStars, business travel is essential because face to face interactions cannot be replaced. Remote work groups and individuals “start to become too far removed from the business objective” without periodic face to face communication that requires business travel. [[1]](#references) The essential nature of face to face contact for effective business management is reinforced by research cited in the Harvard business review. This research found that in person requests were 34 time more effective than those made by text or email and suggests that a manager “could be a more effective communicator by having conversations in person.” [[2]](#references) Business travel also has a significant positive affect on GDP growth. A study by Harvard business school’s Growth Lab, found that “business travel actually causes economic growth.” The research states that business travel by US companies contributed 1.07% to the global GDP (142 Trillion 2019) [[3]](#references) in 2019 which amounts to 1.5 Trillion dollars. [[4]](#references) From the airline industry’s perspective, their financial stability is heavily depended on the revenue from the business traveler. Only 12% of airline passengers are business travelers, but they represent up to 75% of an airline’s profit [[5]](#references).


Because business air travel is an essential part managing a business successfully and has a significant positive effect on economic growth, airline flight delays, in turn, result in lost business productivity and a reduction of the economy's GDP. Research by the FAA found that “inefficiency in the air transportation sector increases the cost of doing business for other sectors, making the associated business less productive.” [[6]](#references) In 2018, the cost of flight delays including reduced GDP and increased airline operating expenses was $28 billion dollars. [[7]](#references) Given these facts on the negative effects of flight delays, just how often will a business traveler encounter a flight delay? Data on flight delays from Bureau of Transportation Statistics show that between 2011 and 2019 on average 18.33% of all flights were delayed. If the percentage of cancelled flights are also included, the cumulative data shows that on average 20% of flights fail to make their destination on time or at all. [[8]](#references) This mean that a business traveler will experience a flight delay every one out of five flights.

<p align="center">
  <img align="center" src="data_charts_tables/flight_delayed_canceled_table.png" title="Flight Delay Canceled Data Table" alt="Flight Delay Canceled Data Table" height="300" width="600">
</p>

<p align="center">
  <img align="center" src="data_charts_tables/flight_delay_percent_plot.png" title="Flight Delay Bar Chart" alt="Flight Delay Bar Chart" height="200" width="300">
</p>

<p align="center">
  <img align="center" src="data_charts_tables/flight_canceled_percent_plot.png" title="Flight Cenceled Bar Chart" alt="Flight Canceled Bar Chart" height="250" width="300">
  <br/>
</p>

[[8]](#references)

### Conclusion

Business travel is integral to managing businesses successfully and to maintaining the GDP output of the economy. Research on flight delays clearly shows that they have a significant negative effect on both. Businesses would benefit from having the ability to predict future flight delays so that they can schedule business travel when the probability of a flight delay is low and minimize the lost productivity that flight delays cause. In addition, if a majority of business in the economy are successful in  minimize productivity losses from flight delays it will have the follow on effect of also minimizing the overall GDP loss that is attributed to flight delays in the aggregate.

## Project 

### Overview

This project will develop a machine learning model that will predicts flight delays. 

### Purpose

This project has two objectives. 

The first objective is to create a machine learning model that can predict flight delays so that businesses can use this model to plan business travel when the probability of flight delays is the lowest and reduce the productivity losses attributed to flight delays.

The second objective is to determine the factors that are most correlated with flight delays. This information will enable the FAA and regional government organizations that manage the aviation infrastructure to focus resources on reducing and eliminating the biggest factors that cause flight delays. 

### Model Source Data

The data on flight delays for the machine learning model comes from the Federal Bureau of Transportation Statistics. The data contains commercial carrier flight information for the months of January 2019 and January 2020. The 2019 file contains data for 583,985 flights and the 2020 contains data for 607,346 flight for a total of 1,191,331 flights. The features included in the data are:

* Day of the Month
* Day of the Week
* Airline
* Plane Identifier
* Departure Airport Code
* Arrival Airport Code
* Departure Time
* Departure Delayed Indicator
* Departure Time Classification
* Arrival Time
* Arrival Delayed Indicator
* Canceled Indication
* Diverted Indicator 
* Flight Distance

The FAA considers a flight delayed if it departs the origin airport or it arrives at the destination airport more than 15 minutes after the scheduled time.

The project is also planning to incorporate in the model weather data at the departure airport and arrival airport during the scheduled time of the flight

The flight data files contains departure and arrival airport code fields. These fields contain the three letter FAA airport code, such as ORD for Chicago O'Hare airport. An additional file is included in the project data files that contains the city or name of the airport associate with the three letter airport code. 


### Project Deliverable Description

| File Name | Directory | Description|
|-----------|-----------|------------|
|**Flight Data Files**|||
|Flights_Data.ipynb|Database|Jupyter notebook to clean and select features from raw January 2019 and 2020 flight data files|
|599747_1080724_compressed_Jan_2019_ontime.csv.zip|Flight_data_files|zipped raw January 2019 flight data file|
|Jan_2019_ontime.csv|Flight_data_files|raw January 2019 flight data file|
|jan_19_clean_data.csv|Database/Data/|cleaned January 2019 flight data file|
|599747_1080724_compressed_Jan_2020_ontime.csv.zip|Flight_data_files|zipped raw January 2020 flight data file|
|Jan_2020_ontime.csv|Flight_data_files|raw January 2020 flight data|
|jan_20_clean_data.csv|Database/Data/|cleaned January 2020 flight data file|
|**Airport Code City/Airport Name Files**|||
|airport_code_city.ipynb| root|Jupyter notebook to clean raw code airport city/name data file files|
|airport_codes_city_raw.txt|Flight_data_files|Raw airport code airport city/name data file|
|airport_codes_city.csv|Flight_data_files|cleaned airport code airport city/name data file|
|**Aircraft Type Data File**|||
|ReleasableAircraft.zip|Flight_data_files|zipped file containing aircraft identification number and aircraft type|
|**Exploratory Data**|||
|eploratory_testing.ipynb Jupyter Notebook
|Percentage of delay per airline|exploratoy_testing Jupyter Notebook|bar graph containing delays and not delayed flight information and percentage of delay per airline|
|Percentage of delay per aiport|exploratoy_testing Jupyter Notebook|bar graph containing delays and not delayed flight information and percentage of delay per airport|
|Percentage of delay per departure time block|exploratoy_testing Jupyter Notebook|bar graph containing delays and not delayed flight information and percentage of delay per time block|
|Percentage of delay per flight distance|exploratoy_testing Jupyter Notebook|bar graph containing delays and not delayed flight information and percentage of delay per distance|
|Percentage of delay per weekday|exploratoy_testing Jupyter Notebook|bar graph containing delays and not delayed flight information and percentage of delay per weekday|
|**Machine Learning Model File**|||
|Seg_one_model .ipynb|root|Jupyter notebook contining the machine leaning model implementation code|
|**Readme Graphics Files**|||
|flight_delayed_canceled_table.png|data_charts_table|readme data table containing flight on-time, delayed, and canceled statistics|
|flight_delay_percent_plot.png|data_charts_table|readme bar chart of % flight delays 2011-19|
|flight_canceled_percent_plot.png|data_charts_table|readme bar char of % flight canceled 2011-2019|

### Presentation Slides
The presentation that outlines the steps performed in this project is available on Google Slides and can be found by clicking on the below link:

[Final Project Presentation](https://docs.google.com/presentation/d/1HSP1glrp1soaLvSLndOQSudrSzysDYgPzm5htyLGAaI/edit#slide=id.p)

### Dashboard

<img align="center" src="data_charts_tables/dashboard.gif" title="Flight Delay Dashboard">
  
[Dashboad on AWS](http://flight-delay-predict-env.eba-2u2jw4ht.us-east-2.elasticbeanstalk.com)

#### Technical Design

The dashboard is a single page web application. The dashboard user interface uses JavaScript d2.json() requests to request and receive flight selection and flight delay prediction information from the webserver. The webserver used the Flask web application framework. The dashboard web application has three layers of components

* Presentation Layer Components
* Logic Layer Components
* Data Source Layer Components

Presentation layer components respond to user input from the dashboard and request data from the flight delay prediction system. The presentation layer components either make data requests for flight selection data such as origin state airports or requests flight delay prediction data from the machine learning model. 

The logic layer components receive requests from presentation layer for either flight selection information or flight delay prediction information. Flight selection information request are processed by calling the data source layer to get the requested data. Flight delay prediction information requests are processed by inputting the delay prediction parameters from the dashboard into the machine learning model and returning the delay prediction data to the dashboard presentation layer. 

The data source layer component receives flight or weather data requests from a logic level component, retrieves requested information from the data source, and returns data to the calling logic level component.

#### Exploratory Data

The exploratory data is contained in the Jupyter Notebook called exploratory_testing. 

Pyplot in Matplotlib was used to get visuals on 

  - Percentage of delay per airline
  - Percentage of delay per aiport
  - Percentage of delay per departure time block
  - Percentage of delay per flight distance
  - Percentage of delay per weekday

#### Machine Learning Model

The dashboard machine learning model is contained in the Python file Dashboard/FlightDelayPredictorModel.py
The data to populate the model is stored in the folowing files

<table>
    <thead>
        <tr>
            <th>File Name</th>
            <th>Model Component</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Dashboard/pickel_files/Origin_encoder.pkl</td>
            <td>origin encoder</td>
        </tr>
        <tr>
            <td>Dashboard/pickel_files/Dest_encoder.pkl</td>
            <td>destination encoder</td>
        </tr>
        <tr>
            <td>Dashboard/pickel_files/scaler.pkl</td>
            <td>feature scaler</td>
        </tr>
        <tr>
            <td>Dashboard/pickel_files/model_dt.pkl</td>
            <td>model initializer</td>
        </tr>
    </tbody>
</table>



#### Web Application Layer Components

<table>
    <thead>
        <tr>
            <th>Layer</th>
            <th>Component Name</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Presentation</td>
            <td>Dashboard/templates/FlightDelayPredictor.html</td>
        </tr>
        <tr>
            <td></td>
            <td>Dashboard/static/js/FlightDelayPredictor.js</td>
        </tr>
        <tr>
            <td></td>
            <td>Dashboard/static/js/FlightDataDisplay.js</td>
        </tr>
        <tr>
            <td></td>
            <td>Dashboard/static/css/FlightDelayPredictor.css</td>
        </tr>
        <tr>
            <td></td>
            <td>Dashboard/application.py</td>
        </tr>
        <tr>
            <td></td>
            <td>Dashboard/application_config.py</td>
        </tr>
        <tr>
            <td></td>
            <td>Dashboard/DatabaseConfig.py</td>
        </tr>
        <tr>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Logic</td>
            <td>Dashboard/FlightDelayPredictor.py</td>
        </tr>
        <tr>
            <td></td>
            <td>Dashboard/FlightDelayPredictorModel.py</td>
        </tr>
        <tr>
            <td></td>
            <td>Dashboard/pickle_files/Dest_encoder.pkl</td>
        </tr>
        <tr>
            <td></td>
            <td>Dashboard/pickle_files/Origin_encoder.pkl</td>
        </tr>
        <tr>
            <td></td>
            <td>Dashboard/pickle_files/model_dt.pkl</td>
        </tr>
        <tr>
            <td></td>
            <td>Dashboard/pickle_files/scaler.pkl</td>
        </tr>        
        <tr>
            <td></td>
            <td>Dashboard/AirportWeather.py</td>
        </tr>
        <tr>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Data Source</td>
            <td>Dashboard/DatabaseDataSource.py</td>
        </tr>
        <tr>
            <td></td>
            <td>Dashboard/AirportWeatherDS.py</td>
        </tr>
        <tr>
            <td></td>
            <td>Dashboard/FlightDelayPredictorDS.py</td>
        </tr>
    </tbody>
</table>
    

### Database

<img align="center" src="Database/database.erd.png" title="Dashboard Database ERD">

[Database Create SQL](Database/database.create.sql)

[Database Dashboard Select SQL](Database/database.selects.sql)

This query get the list of states of all the airport in the system
```
SELECT DISTINCT state 
FROM   airports
ORDER BY state
```

This query gets all the airports for the specified origin state
```
SELECT city, code 
FROM   airports 
WHERE  state = '{origin_state}'
```

This query gets all the states that can be be flown 
to from the specified origin airport
```
SELECT 	DISTINCT b.state
FROM    airports_routes a
INNER JOIN
        airports b
ON      a.dest_code = b.code
WHERE 	a.origin_code = '{origin_airport_code}'
ORDER BY b.state
```

This query gets all the airports in the specified destination 
state that can be flown to from the specified origin airport
```
SELECT DISTINCT b.city, b.code 
FROM   airports_routes a 
INNER JOIN 
       airports b 
ON     a.dest_code = b.code 
WHERE  a.origin_code = '{origin_airport_code}' 
AND    b.state = '{dest_state}' 
ORDER BY b.city
```

This query gets the name of the airlines that fly from the
specified origin airport to the specified destination airport
```
SELECT DISTINCT a.op_carrier_name, a.op_unique_carrier 
FROM   airlines a 
INNER JOIN 
       airline_routes b 
ON     a.op_carrier_airline_id = b.op_carrier_airline_id 
WHERE  b.origin_code = '{origin_airport_code}' 
AND    b.dest_code = '{dest_airport_code}' 
ORDER BY op_carrier_name
```

This query gets the hourly weather for a specified airport and date
```
SELECT cloudcover, precipitation, windspeed, humidity, visibility
FROM   airport_weather
WHERE  code = '{airport_code}'
AND    date = '{date}'
ORDER BY HOUR
```

```
From Python file Dashboard/DatabaseDataSource.py


from  sqlalchemy import create_engine

class DatabaseDataSource:

    def __init__(self, databaseConfig):

        # Get database configuration parameters
        user          = databaseConfig["user"]
        password      = databaseConfig["password"]
        host          = databaseConfig["host"]
        port          = databaseConfig["port"]
        database      = databaseConfig["database"]
        database_type = databaseConfig["database_type"]

        # Generate database connection url
        url = "{}://{}:{}@{}:{}/{}".format(database_type, user, password, host, port, database)

        # create SQLAlcheme engine
        self.engine = create_engine(url)

fully qualified connect string postgresql://USER:PASSWORD@flightsdata.XXXXXXX.us-XXXXX-XXX.rds.amazonaws.com:5432/flightsdata

```
### References

[[1]](https://www.inc.com/david-brown/why-travel-is-essential-to-running-a-successful-business.html) Why Travel Is Essential to Running a Successful BusinessFace-to-face interactions can never be replaced, *Inc., David Brown Oct 4, 2017*


[[2]](https://hbr.org/2017/04/a-face-to-face-request-is-34-times-more-successful-than-an-email) A Face-to-Face Request Is 34 Times More Successful Than an Email, *Harvard Business Review, Vanessa K. Bohns, April 11, 2017*


[[3]](https://www.statista.com/statistics/268750/global-gross-domestic-product-gdp/) Global gross domestic product (GDP) at current prices from 2009 to 2021, *statista.com, H. Plecher, Jun 3, 2020*


[[4]](https://www.nature.com/articles/s41562-020-0922-x) Knowledge diffusion in the network of international business travel, *Nature Human Behaviour, Michele Coscia, Frank M. H. Neffke & Ricardo Hausmann, The Growth Lab, Harvard Center for International development, 10 August 2020*


[[5]](https://www.investopedia.com/ask/answers/041315/how-much-revenue-airline-industry-comes-business-travelers-compared-leisure-travelers.asp) How Much of Airlines' Revenue Comes From Business Travelers? *investopedia.com, Jul 15, 2019*

 
[[6]](https://cpb-us-e1.wpmucdn.com/blog.umd.edu/dist/9/604/files/2019/09/TDI_Report_Final_11_03_10.pdf) Total Delay Impact Study A Comprehensive Assessment of the Costs and Impacts of Flight Delay in the United States, *National Center of Excellence for Aviation Operations Research (NEXTOR), November, 2010*


[[7]](https://www.airlines.org/dataset/per-minute-cost-of-delays-to-u-s-airlines/#) U.S. Passenger Carrier Delay Costs, *airlines.org*


[[8]](https://www.transtats.bts.gov/HomeDrillChart.asp) On-Time Performance - Flight Delays at a Glance, *Bureau of Transportation Statistics*
