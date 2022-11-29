import os
from google.cloud import storage
import configparser

config = configparser.ConfigParser()
config.read_file(open('gcp.config'))

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'df8-naufal-key.json'

# Initiates Variable
project_id = config['GCP']['PROJECT_ID']
bucket_name = config['GCP']['BUCKET_NAME']
dest_name = config['GCP']['DESTINATION_NAME']
local_file_path = config['GCP']['LOCAL_FILE_PATH']

client = storage.Client(project_id)
print(local_file_path)

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    try:
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(source_file_name)
        print('File {} uploaded to {}.'.format(source_file_name, destination_blob_name))
    except Exception as e:
        print(e)

upload_blob(bucket_name, local_file_path, dest_name)

