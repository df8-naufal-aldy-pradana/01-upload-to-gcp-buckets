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
bucket_name = config['GCP']['BUCKET_NAME']
dest_name = config['GCP']['DESTINATION_NAME']
local_file_path = config['GCP']['LOCAL_FILE_PATH']

# File from internet
random_internet_img = 'https://images.unsplash.com/photo-1669639070423-462483f0211b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80'
file = urllib.request.urlopen(random_internet_img)

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

# Call function to upload file from local assets to GCP
for img in os.listdir(local_file_path):
    upload_blob_filename(bucket_name, local_file_path + img, dest_name + img)

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

# Call function to upload file from internet to GCP
upload_blob_string(bucket_name, file.read(), dest_name + 'random_internet_img.jpg')