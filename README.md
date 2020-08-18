# Airline Flight Delay Analysis and Prediction

## Introduction

Business air travel is essential part of managing a company successfully even with the availability of feature-rich, remote collaboration software, such as WebEx, Zoom, and Slack. According to David Brown founder and CEO of  TechStars, business travel is essential because face to face interactions cannot be replaced. Remote work groups and individuals “start to become too far removed from the business objective” without periodic face to face communication that requires business travel. [[1]](#references) The essential nature of face to fact contact for effective business management is reinforced by research cited in the Harvard business review. This research found in person requests were 34 time more effective than those made by text or email and suggests that a manager “could be a more effective communicator by having conversations in person.” [[2]](#references) Business travel also has a significant positive affect on GDP growth. A study by Harvard business school’s Growth Lab, found that “that business travel actually causes economic growth.” Data from the research shows that business travel by US companies contributed 1.07% to the global GDP (142 Trillion 2019) [[3]](#references) in 2019 which amounts to 1.5 Trillion dollars. [[4]](#references) From the airline industry’s perspective, their financial stability is heavily depended on the revenue from the business traveler. Only 12% of airline passengers are business travelers, but they represent up to 75% of an airline’s profit [[5]](#references).


Because business air travel is an essential part managing a business successfully and has a significant positive effect on economic growth, airline flight delays, in turn, result in lost business productivity and a reduction of the economy's GDP. Research by the FAA found that “inefficiency in the air transportation sector increases the cost of doing business for other sectors, making the associated business less productive.” [[6]](#references) In 2018, the cost of flight delays including reduced GDP and increased airline operating costs was $28 billion dollars. [[7]](#references) Given these facts on the negative effects of flight delays, how often will a business traveler encounter a flight delay? Data on flight delays from Bureau of Transportation Statistics show that between 2011 and 2019 on average 18.33% of all flights were delayed. If the percentage of cancelled flights are included, the cumulative data shows that on average 20% of flights failed to make their destination on time or at all. [[8]](#references) This mean that a business traveler will be experience a flight delay every one out of five flights.


<p align="center">
  <img align="center" src="https://github.com/Duegan24/Final_Project/blob/deans_branch/data_charts_tables/flight_delayed_canceled_table.png" title="Flight Delay Canceled Data Table" alt="Flight Delay Canceled Data Table" height="300" width="600">
</p>

<p align="center">
  <img align="center" src="https://github.com/Duegan24/Final_Project/blob/deans_branch/data_charts_tables/flight_delay_percent_plot.png" title="Flight Delay Bar Chart" alt="Flight Delay Bar Chart" height="200" width="300">
</p>

<p align="center">
  <img align="center" src="https://github.com/Duegan24/Final_Project/blob/deans_branch/data_charts_tables/flight_canceled_percent_plot.png" title="Flight Cenceled Bar Chart" alt="Flight Canceled Bar Chart" height="250" width="300">
  <br/>
</p>

[[8]](#references)


Given how integral business travel is to business success and the overall economy's GDP output and how flight delays have a significant negative effect on both, having the ability to predict future flight delays will enable businesses to schedule travel when the probability of flight delay is low. This will enable businesses to minimize its lost productivity due to flight delays. I will also minimize the lost GDP output of the economy as a whole caused by flight delays.

## Project 

### Overview

This project will develop a machine learning model using linear regression that predicts flight delays and gives a numerical estimate of the duration of the flight delay. 

### Purpose

This project has two objectives. 

The first objective is to create a machine learning model that can predict flight delays so that businees can use this model to plan business travel when the probability of flight delays is the lowest. 

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

The FAA considers a flight delayed if it departs the orgin airport or it arrives at the destination airport more that 15 mimutes after the scheduled time.

The project is also planning to incorporate in the model weather data at the departure airport and arrival airport during the scheduled time of the flight

The flight data files contains departure and arrival airport code fields. These fields contain the three letter FAA airport code, such as ORD for Chicago O'Hare airport. An additional file is included in the project data files that contains the city or name of the airport associate with the three letter airport code. 

### Communication Protocol

The primary method project communication is through a Slack group direct message channel. All project team member have the Slack application on our phones so that messages between a team member and the project team will be received in a timely manner. If the need for more involved group collaboration arises, a Zoom session will be initiated by one of the project team member which will be joined by the remaining team members.

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
|**Machine Learning Model File**|||
|Seg_one_model .ipynb|root|Jupyter notebook contining the machine leaning model implementation code|
|**Readme Graphics Files**|||
|flight_delayed_canceled_table.png|data_charts_table|readme data table containing flight on-time, delayed, and canceled statistics|
|flight_delay_percent_plot.png|data_charts_table|readme bar chart of % flight delays 2011-19|
|flight_canceled_percent_plot.png|data_charts_table|readme bar char of % flight canceled 2011-2019|

### References

[[1]](https://www.inc.com/david-brown/why-travel-is-essential-to-running-a-successful-business.html) Why Travel Is Essential to Running a Successful BusinessFace-to-face interactions can never be replaced, *Inc., David Brown Oct 4, 2017*


[[2]](https://hbr.org/2017/04/a-face-to-face-request-is-34-times-more-successful-than-an-email) A Face-to-Face Request Is 34 Times More Successful Than an Email, *Harvard Business Review, Vanessa K. Bohns, April 11, 2017*


[[3]](https://www.statista.com/statistics/268750/global-gross-domestic-product-gdp/) Global gross domestic product (GDP) at current prices from 2009 to 2021, *statista.com, H. Plecher, Jun 3, 2020*


[[4]](https://www.nature.com/articles/s41562-020-0922-x) Knowledge diffusion in the network of international business travel, *Nature Human Behaviour, Michele Coscia, Frank M. H. Neffke & Ricardo Hausmann, The Growth Lab, Harvard Center for International development, 10 August 2020*


[[5]](https://www.investopedia.com/ask/answers/041315/how-much-revenue-airline-industry-comes-business-travelers-compared-leisure-travelers.asp) How Much of Airlines' Revenue Comes From Business Travelers? *investopedia.com, Jul 15, 2019*

 
[[6]](https://cpb-us-e1.wpmucdn.com/blog.umd.edu/dist/9/604/files/2019/09/TDI_Report_Final_11_03_10.pdf) Total Delay Impact Study A Comprehensive Assessment of the Costs and Impacts of Flight Delay in the United States, *National Center of Excellence for Aviation Operations Research (NEXTOR), November, 2010*


[[7]](https://www.airlines.org/dataset/per-minute-cost-of-delays-to-u-s-airlines/#) U.S. Passenger Carrier Delay Costs, *airlines.org*


[[8]](https://www.transtats.bts.gov/HomeDrillChart.asp) On-Time Performance - Flight Delays at a Glance, *Bureau of Transportation Statistics*
