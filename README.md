# Sporify AWS end-to-end BI Engineering Project

## Introduction:
In this project, we will build an ETL (Extract, Transform, Load) pipeline using the Spotify API on AWS. The pipeline will retrieve data from the Spotify API, transform it to a desired format, and load it into an AWS data store.

**Client needs:** 
* Build ETL Pipilines
* Build a large dataset, update it every week, and from there, generate insight

**Objective:**
Seamlessly integrated Spotify API to extract and analyze music data. 🎶 Leveraging Python, Amazon Web Services (AWS), and Snowflake, by building an end-to-end data pipeline to process, transform, and visualize Spotify's rich music data.
The primary objective was to extract valuable insights from Spotify's extensive music catalog while constructing a comprehensive data pipeline to automate the entire process.

## Architecture:



## Service used:
**Amazon S3 (Storage):** Amazon S3 is a highly scalable object storage service that enables you to store and retrieve data of any size from anywhere on the web. It is commonly used for storing and distributing large media files, data backups, and static website files. 

**AWS Lambda (Compute):** AWS Lambda is a serverless computing service that allows you to run code without the need to manage servers. You can use Lambda to execute code in response to various events, such as changes in Amazon S3, DynamoDB, or other AWS services.

**Amazon CloudWatch (Logs/Trigger):** Amazon CloudWatch is a monitoring service for AWS resources and the applications you run on them. It provides the capability to track metrics, collect and monitor log files, and set up alarms for your resources.

**AWS Glue Crawler (Data Crawler):** AWS Glue Crawler is a fully managed service that automatically scans your data sources, identifies data, and creates an AWS Glue Data Catalog.

**AWS Glue Data Catalog (Data Catalog):** AWS Glue Data Catalog is a fully managed metadata repository that simplifies data discovery and management. You can easily integrate the Glue Data Catalog with other AWS services, such as Athena.

**Amazon Athena (Analytics Query):** Amazon Athena is an interactive query service that simplifies the analysis of data in Amazon S3 using standard SQL. You can use it to analyze data stored in your Glue Data Catalog or other S3 buckets.








## Project Components:

**Data Extraction:** Python code, aided by the Spotify library, fetched music data directly from Spotify, and subsequently, it was stored in AWS S3.

**Automated Data Transformation:** I designed AWS Lambda functions to efficiently convert JSON data into structured tables, encompassing songs, albums, and artists.

**AWS Lambda Functions:** These serverless functions automated the entire data processing pipeline whenever new data became available.

**Amazon S3** Transformed data was stored in AWS S3
