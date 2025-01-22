# NYC Yellow Taxi Data Pipeline - Improved Version
import pandas as pd
from sqlalchemy import create_engine
from time import time

def setup_database():
    """Create database connection and initialize table"""
    engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')
    
    # Load sample to get schema
    df_sample = pd.read_csv('yellow_tripdata_2021-01.csv', nrows=100)
    df_sample.tpep_pickup_datetime = pd.to_datetime(df_sample.tpep_pickup_datetime)
    df_sample.tpep_dropoff_datetime = pd.to_datetime(df_sample.tpep_dropoff_datetime)
    
    # Create empty table
    df_sample.head(n=0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')
    
    return engine

def process_taxi_data(engine, chunk_size=100000):
    """Process taxi data in chunks and load to database"""
    df_iter = pd.read_csv('yellow_tripdata_2021-01.csv', iterator=True, chunksize=chunk_size)
    total_chunks = 0
    
    try:
        while True:
            t_start = time()
            
            # Process chunk
            df = next(df_iter)
            df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
            df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
            
            # Load to database
            df.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')
            
            # Log progress
            total_chunks += 1
            t_end = time()
            print(f'Chunk {total_chunks}: Inserted {len(df)} rows, took {(t_end - t_start):.3f} seconds')
            
    except StopIteration:
        print(f"\nCompleted! Processed {total_chunks} chunks")
    except Exception as e:
        print(f"Error occurred: {str(e)}")
    finally:
        if 'df_iter' in locals():
            df_iter.close()

if __name__ == "__main__":
    engine = setup_database()
    process_taxi_data(engine)