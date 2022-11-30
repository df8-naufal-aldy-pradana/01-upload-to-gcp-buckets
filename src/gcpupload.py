import os
from google.cloud import storage
import configparser
import urllib.request

config = configparser.ConfigParser()
config.read_file(open('gcp.config'))

# Replace with your own credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'df8-naufal-key.json'

# Initiates Variable from config file
project_id = config['GCP']['PROJECT_ID']

client = storage.Client(project_id)

# Define function to upload file to GCP from local assets
def upload_blob_filename(bucket_name, source_file_name, destination_blob_name):
    try:
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(source_file_name)
        print('File {} uploaded to {}.'.format(source_file_name, destination_blob_name))
    except Exception as e:
        print(e)
        print('File {} failed to upload to {}.'.format(source_file_name, destination_blob_name))

# Define function to upload file to GCP from internet
def upload_blob_string(bucket_name, source_file, destination_blob_name):
    try:
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_string(source_file, content_type='image/jpeg')
        print('File {} uploaded to {}.'.format("Random Internet Image", destination_blob_name))
    except Exception as e:
        print(e)
        print('File {} failed to upload to {}.'.format(source_file, destination_blob_name))
