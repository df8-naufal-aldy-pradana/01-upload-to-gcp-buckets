from src.gcpupload import upload_blob_filename, upload_blob_string
import urllib.request
import configparser
import os

# Initiate variables from config file
config = configparser.ConfigParser()
config.read_file(open('gcp.config'))
bucket_name = config['GCP']['BUCKET_NAME']
dest_name = config['GCP']['DESTINATION_NAME']
local_file_path = config['GCP']['LOCAL_FILE_PATH']

# File from internet
random_internet_img = 'https://images.unsplash.com/photo-1669639070423-462483f0211b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80'
file = urllib.request.urlopen(random_internet_img)


def main():
    # Call function to upload file from local assets to GCP
    for img in os.listdir(local_file_path):
        upload_blob_filename(bucket_name, local_file_path + img, dest_name + img)

    # Call function to upload file from internet to GCP
    upload_blob_string(bucket_name, file.read(), dest_name + 'random_internet_img.jpg')

if __name__ == "__main__":
    main()