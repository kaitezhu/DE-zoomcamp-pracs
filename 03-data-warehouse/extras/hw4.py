import requests
from google.cloud import storage
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/ktzhu/code/dtc-de-course-449111-8fc1a261220d.json"

# Initialize a storage client
storage_client = storage.Client()
print("Storage client initialized.")

# Get your bucket
bucket = storage_client.get_bucket('de_hw4_ktzhu')
print("Bucket 'de_hw4_ktzhu' accessed.")

# Define the base URLs for the data
base_urls = {
    'yellow': 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_',
    'green': 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_',
    'fhv': 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/fhv/fhv_tripdata_'
}

# Define the years and months to download
years = ['2019', '2020']
months = [str(month).zfill(2) for month in range(1, 13)]

# Download the data and upload to GCS
for taxi_type, base_url in base_urls.items():
    print(f"Processing taxi type: {taxi_type}")
    for year in years:
        for month in months:
            if taxi_type == 'fhv' and year == '2020':
                print(f"Skipping FHV data for year {year}")
                continue
            url = f"{base_url}{year}-{month}.csv.gz"
            try:
                print(f"Fetching data from: {url}")
                response = requests.get(url)
                response.raise_for_status()  # Will raise an exception for bad status codes
                blob = bucket.blob(f"{taxi_type}_tripdata_{year}-{month}.csv.gz")
                blob.upload_from_string(response.content)
                print(f"Successfully uploaded {taxi_type}_tripdata_{year}-{month}.csv.gz to GCS")
            except requests.RequestException as e:
                print(f"Error downloading {url}: {e}")
            except Exception as e:
                print(f"An error occurred while processing {url}: {e}")