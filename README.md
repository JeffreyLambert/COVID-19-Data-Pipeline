# COVID-19-Data-Pipeline

## Description
This project contains a python class used to interact with the COVID Tracking Project API.  
It was inspired by work tracking COVID outbreaks near major Charles Schwab corporate locations.
This project is intended to be the data source for a friend and I as we learn to host data applications
on AWS.


## Usage

```python
from covid_pipeline.etl import Pipeline
from covid_pipeline.config import OUTPUT_PATH

etl = Pipeline()

etl.retrieve_current()

etl.clean_dates()

etl.write_csv(OUTPUT_PATH)
```


## Motivation & Details
This project was inspired by work tracking COVID outbreaks near major Charles Schwab corporate locations and is intended
to be the data source I use as I learn to host web applications with Amazon Web Services.  

In March of 2020 I was asked to help our executive leadership forecast and understand the spread of COVID-19 near our 
major corporate locations.  While we have been able to perform the majority of our work remotely, there are some areas
of the business which could not perform their work remotely.  Thus, any impact of COVID-19 to these locations posed
a substantial risk to our company and our clients.  

To help track the spread of COVID-19 and its impact on Schwab, I created a Tableau dashboard providing
daily updates regarding the number of cases within 100 miles of our major corporate locations.

Project work:
1. Geocode the locations of our major corporate offices
2. Set up Bash scripts which retrieved data from 
    - NY Times
    - US Census Bureau
    - COVID Tracking Project
    - IHME COVID-19 Projections
    
3. Use the latitude / longitude of each corporate office location to draw a 100 mile radius around each location
4. Tabulate the number of cases within the 100 mile radius of each branch
5. Calculate 14 and 7 day rolling averages of positive test rates.
5. Store this data into a SQL database for later use within Tableau.

Technologies utilized
- Bash
- SQL
- Python

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Project Status
Future updates to this code base will be made should we decide to add more
information to our AWS application.