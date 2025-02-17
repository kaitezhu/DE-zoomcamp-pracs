## Question 1. dlt Version

Answer: dlt 1.6.1


## Question 2. Define & Run the Pipeline (NYC Taxi API)
Output:
index,database,schema,name,column_names,column_types,temporary
0,ny_taxi_pipeline,ny_taxi_data,_dlt_loads,['load_id' 'schema_name' 'status' 'inserted_at' 'schema_version_hash'],['VARCHAR' 'VARCHAR' 'BIGINT' 'TIMESTAMP WITH TIME ZONE' 'VARCHAR'],false
1,ny_taxi_pipeline,ny_taxi_data,_dlt_pipeline_state,"['version' 'engine_version' 'pipeline_name' 'state' 'created_at'
 'version_hash' '_dlt_load_id' '_dlt_id']","['BIGINT' 'BIGINT' 'VARCHAR' 'VARCHAR' 'TIMESTAMP WITH TIME ZONE'
 'VARCHAR' 'VARCHAR' 'VARCHAR']",false
2,ny_taxi_pipeline,ny_taxi_data,_dlt_version,"['version' 'engine_version' 'inserted_at' 'schema_name' 'version_hash'
 'schema']","['BIGINT' 'BIGINT' 'TIMESTAMP WITH TIME ZONE' 'VARCHAR' 'VARCHAR'
 'VARCHAR']",false
3,ny_taxi_pipeline,ny_taxi_data,rides,"['end_lat' 'end_lon' 'fare_amt' 'passenger_count' 'payment_type'
 'start_lat' 'start_lon' 'tip_amt' 'tolls_amt' 'total_amt' 'trip_distance'
 'trip_dropoff_date_time' 'trip_pickup_date_time' 'surcharge'
 'vendor_name' '_dlt_load_id' '_dlt_id' 'store_and_forward']","['DOUBLE' 'DOUBLE' 'DOUBLE' 'BIGINT' 'VARCHAR' 'DOUBLE' 'DOUBLE' 'DOUBLE'
 'DOUBLE' 'DOUBLE' 'DOUBLE' 'TIMESTAMP WITH TIME ZONE'
 'TIMESTAMP WITH TIME ZONE' 'DOUBLE' 'VARCHAR' 'VARCHAR' 'VARCHAR'
 'DOUBLE']",false

 Answer: 4

 ## Question 3. The total number of records extracted?

Output:
df.shape
(10000, 18)

Answer: 10000

 ## Question 4. Average trip duration

 Output: [(12.3049,)]
 
 Answer: 12.3049
