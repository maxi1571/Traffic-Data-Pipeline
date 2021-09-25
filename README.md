# Data warehouse tech stack with MySQL, DBT, Airflow

## Introduction

We aim to construct an AI company that installs sensors in enterprises and gathers
data from all areas of the industry, such as people's activities, household sensors in
the building, the surroundings, and other important information. Our company is in
charge of implementing all of the required sensors, collecting a continuous stream
of information from them, and evaluating the information to deliver critical business
insights.

## Objective
Our objective is to reduce the cost of running the client facility as well as to increase
the livability and productivity of workers by creating a scalable data warehouse
tech-stack that will help us provide the AI service to the client.

## Overview of Dataset

The data contains all of the 30-second raw sensor data from January to October
2016 for the location of the I80 corridor near Davis, CA.

    * Summary statistics for each station can be found here.
    * Median of total flow for each weekday. Could be used to make animation can
      be found here.
    * 30-second time series for a single station (Richards Ave) near downtown Davis
      can be found here.● The medians for each observation grouped by (station, weekday, hour, half a
      minute) can be found here.
    * Metadata is small- just 53 stations can be found here.
    * The main data is around 35 million observations can be found here.

## Techniques Used

The main goal of this project is to create a data warehouse tech stack. The Tech
Technologies used are Airflow(DAG), dbt, DWH(Mysql), redash, and power BI(data
visualization tool).
The process I followed is first I import the data files into my database, To do that I
first established a DAG in Airflow that employs the python operator. The short-circuit
python operator, which allows a workflow to continue only if a condition is met, was
utilized. Otherwise, the workflow will “short-circuit,” skipping downstream operations.
Then I linked dbt to the data warehouse and created data transformation codes.
Then I created documentation for the data models so that they can be presented
using the dbt docs UI. I then connected the reporting environment and used the
data to generate a dashboard.

![image](https://user-images.githubusercontent.com/42535161/134764888-c65b84b1-cd54-441e-bf6c-8435ff755c19.png)


## Challenges
One of the difficulties I've encountered while working on this project is
understanding the dataset. The datasets don’t have a lot of description to do data
manipulation and transformation and the lack of information made it hard to do that
much analysis. In addition, limited processing capability was an issue. When I tried to
run airflow It created multiple containers which slowed down my pc to eventually
stacking it numerous times.

## Improvement in time
If given more time, checking other dbt modules that can help with data quality
monitoring and better data processing would be possible and doable. The dataset
was complex, and with more time, there could have been a lot more exploration and
a good transformation, and dbt could have been put to good use.

## References
* [How to build a data extraction pipeline with Apache Airflow](https://towardsdatascience.com/how-to-build-a-data-extraction-pipeline-with-apache-airflow-fa83cb8dbcdf)
* [A docker tutorial for beginners](https://greatexpectations.io/blog/ge-data-warehouse/)
* [Data Building Tool (dbt) introduction and full youtube tutorial](https://www.youtube.com/playlist?list=PLy4OcwImJzBLJzLYxpxaPUmCWp8j1esvT)
* [Ensuring data quality in a data warehouse environment with Great Expectations](https://greatexpectations.io/blog/ge-data-warehouse/)
