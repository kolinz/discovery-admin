# discovery-admin
IBM Watson Discovery document management tool. Currently, add & delete function has been implemented.

## Confirmed environment
```
$ python -V
Python 3.8.5
$ pip -V
pip 21.1.2
```
## Prerequisite
### step1
```
$ pip install ibm-watson
$ pip install python-dotenv
```
### step2
```
$ git clone https://github.com/kolinz/discovery-admin.git
$ cd discovery-admin
```
### step3
Edit .env file
```
apikey = "your watson discovery apikey"
url = "your watson discovery url"
environment_id = "your environment_id in Watson discovery"
collection_id = "your collection_id in Watson discovery"
```
- apikey and url >> Copy the credentials to authenticate to your service instance.
- environment_id and collection_id >> Copy the values from "View API Details" in your collection.

## Usage
### Add(Upload) a document
Run the command.
```
$ python discovery-docs-tool.py add file-path
```
#### example
```
$ python discovery-docs-tool.py add /home/user1/sample.json
```
#### Error information
- The Error occurred in PDF with Japanese file name. But I was able to upload a JSON or HTML file with a Japanese file name.

### Delete a document
Run the command. Get a document-id in your web console of Watson Discovery Service.
```
$ python discovery-docs-tool.py delete document-id
```
#### example
```
$ python discovery-docs-tool.py delete f627e521-d9fe-458d-xxxxxxxxxxxxx
```
### Get a list of documents
Run the command.
```
$ python discovery-docs-tool.py docslist metadata_field
```
#### example
```
$ python discovery-docs-tool.py docslist extracted_metadata.filename
```
