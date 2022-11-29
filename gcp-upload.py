import os
from google.cloud import storage
import configparser

config = configparser.ConfigParser()
config.read_file(open('gcp.config'))

# Replace with your own credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'df8-naufal-key.json'

# Initiates Variable from config file
project_id = config['GCP']['PROJECT_ID']
bucket_name = config['GCP']['BUCKET_NAME']
dest_name = config['GCP']['DESTINATION_NAME']
local_file_path = config['GCP']['LOCAL_FILE_PATH']

client = storage.Client(project_id)

# Define function to upload file to GCP
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    try:
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(source_file_name)
        print('File {} uploaded to {}.'.format(source_file_name, destination_blob_name))
    except Exception as e:
        print(e)
        print('File {} failed to upload to {}.'.format(source_file_name, destination_blob_name))

# Call function to upload file to GCP
for file in os.listdir(local_file_path):
    upload_blob(bucket_name, local_file_path + file, dest_name + file)
