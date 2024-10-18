# Mini Project: Complex SQL Query on Databricks
Adil Keku Gazder <br>
ag825, adil.gazder@duke.edu <br>
IDS 706: Data Engineering Systems <br>
Duke University, Fall 2024 <br >
##

### About the project
[![CI](https://github.com/nogibjj/ag825_SQL_complex/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/ag825_SQL_complex/actions/workflows/cicd.yml) <br>

The aim with this project was to read a .csv file, read it into a database (hosted on Databricks) and perform a complex operation on the database. We also use matrix testing to ensure that this file runs on the following versions of Python:
- Python 3.7
- Python 3.8
- Python 3.9

The problem statement is to understand the distribution of records that fall in one of two categories, whether the record is either above or below the average diameter value in the table. The output would look to populate the following table: 

| Diameter Category | Number of Records
|----------|----------|
| Above Average   | XXX   |
| Below Average   | XXX   |


The dataset used for this project was acquired from Kaggle (Cancer Data -> Cancer_Data.csv) and this dataset was modified to include only the following few columns:
- id
- diagnosis
- radius_mean
- texture_mean
- perimeter_mean
- area_mean
- smoothness_mean

Link to the dataset: (https://www.kaggle.com/datasets/erdemtaha/cancer-data/data?select=Cancer_Data.csv)

##
### Repository Structure
The structure of this file is as follows:
- .gitignore file
- .github/workflows file
    - Used to define an automated process which will run the pipeline before publishing
    - Will be defined using a YAML file
- Makefile
    - Compilation and maintainence of code
    - Helps manage dependinces
    - Install / Format / Lint / Test / Generate and Push
- Requirements file
    - Text file (.txt) detailing the required packages to be installed for this program to run
- extract.py: Houses the extract( ) function to extract data from the .csv file
- transform_load.py: Houses the load( ) function to create the database (.db file) and load data into the database
- query.py: Hosts query() which aims to give us the distribution of records which are on either side of the mean value of the Diameter. We achieve this by performing the following SQL query:
    - Join the table on itself by calculating the diameter from the given radius
        - We use id as the unique key for this operation
    - Add a CASE WHEN statement to categorize each record as above or below the mean diameter value
    - Aggregate values based on the category created in the step above and count the number of distinct IDs in each category
- main.py
    - extract( ): Extract data from the .csv file
    - load( ): Create the database (.db file) and load data into the database
    - crud( ): Perform the aggregating query
- testmain.py
    - Tests that the functions extract(), load() and query() function work as expected

