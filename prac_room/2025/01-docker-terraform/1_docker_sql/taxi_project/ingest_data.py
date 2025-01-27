import pandas as pd
from sqlalchemy import create_engine
from time import time
import argparse
import os


def main(params, chunk_size=100000):
    """Main function to setup database connection and process taxi data"""
    # Extract parameters
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    csv_name = url.split("/")[-1]

    os.system(f"wget {url} -O {csv_name}")

    # Create database connection
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    
    # Initialize table with schema
    df_sample = pd.read_csv(csv_name, nrows=100)
    # df_sample.tpep_pickup_datetime = pd.to_datetime(df_sample.tpep_pickup_datetime)
    # df_sample.tpep_dropoff_datetime = pd.to_datetime(df_sample.tpep_dropoff_datetime)
    df_sample.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=chunk_size)
    total_chunks = 0
    
    try:
        while True:
            t_start = time()
            
            # Process chunk
            df = next(df_iter)
            # df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
            # df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
            
            # Load to database
            df.to_sql(name=table_name, con=engine, if_exists='append')
            
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
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database name for postgres')
    parser.add_argument('--table_name', help='name of the table where we will write the results to')
    parser.add_argument('--url', help='url of the csv file')

    args = parser.parse_args()
    main(args, chunk_size=100000)