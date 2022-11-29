# Scripts to Upload Files into GCP's Bucket
Simple python scripts to upload local files into GCP's bucket containerized with docker.

## How to run:
```bash
# Clone this repo
1. git clone https://github.com/iykra-projects-naufal/01-upload-to-gcp-buckets.git

# Replace your gcp credentials, refer to to this docs: https://developers.google.com/workspace/guides/create-credentials
2. Replace gcp credentials on gcp-upload.py

# Build docker image
3. docker build -t "your_tagname" .

# Run docker container
4. docker run "your_tagname"

-----------------------------------------------------------------------------------------------------
If you dont have docker installed:
-----------------------------------------------------------------------------------------------------

# Install requirements
1. pip install -r requirements.txt

# Run script
2. python gcp-upload.py
```
