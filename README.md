# Surf_up Analysis

![Screen Shot 2022-10-12 at 9 18 36 PM](https://user-images.githubusercontent.com/110786136/195483819-886ab064-a857-45d5-984b-ac204c4f2fc7.png)


## Overview

Run some analytics weather dataset to demonstrate that Hawaii, Ohau Island have the perfect weather to open a surf -ice cream shop business.

## Purpose

Use Sqlite , SQLAlchemy, Python, Pandas, Matplotlib and Flask to analyze 12 months of weather stations, temperature and precipitation levels to show the cold, hard, data that proves Oahu Island is suitable place for the new surf shop. Investor will be able to find solid statistical analysis—such as weather mean, standard deviation, minimum, maximum and visualization plots. 


## Results: Provide a bulleted list with three major points from the two analysis deliverables. Use images as support where needed.

###  Summary Statistics for June process

- Import the sqlalchemy extract function.

- Write a query that filters the Measurement table to retrieve the temperatures for the month of June

- Convert the June temperatures to a list.

- Create a DataFrame from the list of temperatures for the month of June

- Calculate and print out the summary statistics for the June temperature DataFrame with describe function

### Summary Statistics for December process

- Write a query that filters the Measurement table to retrieve the temperatures for the month of December

- Convert the December temperatures to a list

- Create a DataFrame from the list of temperatures for the month of December

- Calculate and print out the summary statistics for the December temperature DataFrame with describe function

> *Summary Statistics* 

![Screen Shot 2022-10-12 at 8 48 29 PM](https://user-images.githubusercontent.com/110786136/195483835-21feddc2-6700-4bc9-a32c-3219d662c840.png)

> *Comparative Line Graph*

![statistics](https://user-images.githubusercontent.com/110786136/195483925-c0f78b2b-983f-45bd-8736-d89e1270e998.png)

### Key differences in weather between June and December Summary Statistics

- June Temperature have 183 more data count than December
- December minimum temperature is 8 degrees lower than June minimum temperature
- June maximum temperature is 2 degrees higher than December maximum temperature
- June have the higher temperature average with 3 degress of diferrence

## Summary: Additional queries that collect an annual average of June and December precipication 

![Screen Shot 2022-10-12 at 8 50 10 PM](https://user-images.githubusercontent.com/110786136/195487198-19b9c524-c52c-4d23-9e48-3d18c1c1086d.png)

> *June and December Annual Precipitation Average Line Graph* 
![Precipicattion PM](https://user-images.githubusercontent.com/110786136/195487276-a5d35522-b5c0-46b8-8d97-1c3e131db0f3.png)

Above visualization provide June and December precipitation trends during the past 8 years. Both months average precipitation have less than 0.3 which indicate an average of light rain per year, making Ohau Island an ideal place to open and invest in a surf -ice cream shop. 

Temperature and precipitation data trends determinate that surf shop business have a high possibility to be sustainable year-round.






