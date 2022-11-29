# Scripts to Upload Files into GCP's Bucket
Simple python scripts to upload local files into GCP's bucket containerized with docker.

## How to run:
1. Replace gcp credentials on gcp-upload.py
2. docker build -t "your_tagname" .
3. docker run "your_tagname"