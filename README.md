# Sporify AWS end-to-end BI Engineering Project

## Introduction:
In this project, we will build an ETL (Extract, Transform, Load) pipeline using the Spotify API on AWS. The pipeline will retrieve data from the Spotify API, transform it to a desired format, and load it into an AWS data store.

**Client needs:** 
* Build ETL Pipilines
* Build a large dataset, update it every week, and from there, generate insight

**Objective:**
Seamlessly integrated Spotify API to extract and analyze music data. 🎶 Leveraging Python, Amazon Web Services (AWS), and Amazon Quicksight, by building an end-to-end data pipeline to process, transform, and visualize Spotify's rich music data.
The primary objective was to extract valuable insights from Spotify's extensive music catalog while constructing a comprehensive data pipeline to automate the entire process.

## Architecture:



## Service used:
**Amazon S3 (Storage):** Amazon S3 is a highly scalable object storage service that enables you to store and retrieve data of any size from anywhere on the web. It is commonly used for storing and distributing large media files, data backups, and static website files. 

**AWS Lambda (Compute):** AWS Lambda is a serverless computing service that allows you to run code without the need to manage servers. You can use Lambda to execute code in response to various events, such as changes in Amazon S3, DynamoDB, or other AWS services.

**Amazon CloudWatch (Logs/Trigger):** Amazon CloudWatch is a monitoring service for AWS resources and the applications you run on them. It provides the capability to track metrics, collect and monitor log files, and set up alarms for your resources.

**AWS Glue Crawler (Data Crawler):** AWS Glue Crawler is a fully managed service that automatically scans your data sources, identifies data, and creates an AWS Glue Data Catalog.

**AWS Glue Data Catalog (Data Catalog):** AWS Glue Data Catalog is a fully managed metadata repository that simplifies data discovery and management. You can easily integrate the Glue Data Catalog with other AWS services, such as Athena.

**Amazon Athena (Analytics Query):** Amazon Athena is an interactive query service that simplifies the analysis of data in Amazon S3 using standard SQL. You can use it to analyze data stored in your Glue Data Catalog or other S3 buckets.


## Tech Stack

**Programming Language**
- Python 

**AWS cloud** 
- AWS Simple Storage (S3)
- AWS Lambda
- AWS Cloudwatch Events
- AWS Crawler
- AWS Glue
- AWS Athena

**Data Visualization** 
- Amazon Quicksight

## Pipeline

1. Data Extraction
- AWS Lambda function triggered daily by CloudWatch
- Fetches the latest data from Spotify
- Uploads raw data upon successful extraction
2. Data Transformation
- Triggered automatically after data extraction
- Transforms newly uploaded raw data
- Moves transformed data to respective folders
- Removes raw data to keep it clean
3. Data Loading
- Loads transformed data into AWS Athena
- Provides a centralized database for analytics
- Enables generating insights and reports

## Project description
- Step 1: Using Jupyter Notebook, test data and read JSON: RapidAPI -> Format dataframe -> planning structure. 
- Step 2: Create a trigger and run a cronjob every day to receive messages. 
- Step 3: Design a Lambda function to receive the trigger and extract the data. 
- Step 4: Save data to S3 storage as raw data for later transformation. 
- Step 5: Add a trigger to receive event and store the object in S3. 
- Step 6: Write a Lambda function that receives object triggers and converts data to structure format (CSV).
- Step 7: Save the data as transformation data to S3. 
- Step 8: Build a crawler to collect data for anthena. 
- Step 9: Define the schema with AWS Glue. 
- Step 10: Analysing data with Athena. 
- Step 11: Use Amazon Quicksight to visualize data.

## Conclusion

This end-to-end data pipeline project provided great experience in designing and implementing an automated ETL process using AWS cloud services. 

Building the extraction, transformation, and loading modules required learning new skills like AWS Lambda, CloudWatch, S3, Glue, Athena, and Python. The project demonstrated how these services can be integrated to ingest, process, store, and analyze data efficiently at scale.

Automating the pipeline with triggers and schedulers was an important learning. This ensures latest data is processed daily without any manual intervention.

Transforming the raw JSON data into an optimized CSV structure required problem-solving skills to parse and clean the data into the target schema.

Loading the processed data into S3 and Athena enabled running SQL queries on terabytes of data and generating insights rapidly. These are powerful big data capabilities unlocked by the pipeline.

Overall, this project provided hands-on experience in architecting, developing, and deploying a robust data pipeline on AWS. The skills learned will be invaluable for tackling more complex data engineering challenges in the future.


