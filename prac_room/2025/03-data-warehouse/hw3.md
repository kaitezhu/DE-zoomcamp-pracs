## Question 1. What is count of records for the 2024 Yellow Taxi Data?

select count(1) from `dtc-de-course-449111.taxi_trips.yellow_taxi_external`;

output
--------
Row	f0_
1	20332093

Answer: C
20332093

## Question 2. Write a query to count the distinct number of PULocationIDs for the entire dataset on both the tables. What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?

select count(distinct PULocationID)
from `dtc-de-course-449111.taxi_trips.yellow_taxi_external`;

select count(distinct PULocationID)
from `dtc-de-course-449111.taxi_trips.yellow_taxi_materialized`; 

Answer: B
0 MB for the External Table and 155.12 MB for the Materialized Table

## Question 3. Write a query to retrieve the PULocationID from the table (not the external table) in BigQuery. Now write a query to retrieve the PULocationID and DOLocationID on the same table. Why are the estimated number of Bytes different?

select PULocationID
from `dtc-de-course-449111.taxi_trips.yellow_taxi_materialized`; 

select PULocationID, DOLocationID
from `dtc-de-course-449111.taxi_trips.yellow_taxi_materialized`; 

Answer: A
BigQuery is a columnar database, and it only scans the specific columns requested in the query. Querying two columns (PULocationID, DOLocationID) requires reading more data than querying one column (PULocationID), leading to a higher estimated number of bytes processed.

## Question 4. How many records have a fare_amount of 0?

select count(1)
from `dtc-de-course-449111.taxi_trips.yellow_taxi_materialized`
where fare_amount = 0;

Answer: D
8,333

## Question 5. What is the best strategy to make an optimized table in Big Query if your query will always filter based on tpep_dropoff_datetime and order the results by VendorID (Create a new table with this strategy)

CREATE TABLE `dtc-de-course-449111.taxi_trips.yellow_taxi_optimized`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID
AS
SELECT * FROM `dtc-de-course-449111.taxi_trips.yellow_taxi_materialized`;

Answer: A
Partition by tpep_dropoff_datetime and Cluster on VendorID

## Question 6. Estimated processed bytes

select distinct VendorID
from `dtc-de-course-449111.taxi_trips.yellow_taxi_materialized`
where tpep_dropoff_datetime between '2024-03-01' and '2024-03-15';

select distinct VendorID
from `dtc-de-course-449111.taxi_trips.yellow_taxi_optimized`
where tpep_dropoff_datetime between '2024-03-01' and '2024-03-15';

Answer: B
310.24 MB for non-partitioned table and 26.84 MB for the partitioned table

## Question 7. Where is the data stored in the External Table you created?

The most common external storage system used with BigQuery is Google Cloud Storage (GCS), where data is stored in buckets.

Answer: C
GCP Bucket

## Question 8. It is best practice in Big Query to always cluster your data

For very small tables where the performance gains would be negligible.

Answer: False