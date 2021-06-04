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

### Get a list of documents
Run the command.
```
$ python discovery-docs-tool.py docslist
```
#### output example
```
                                     id  result_metadata.confidence  result_metadata.score   extracted_metadata.filename
0    8daac09bce0a793064xxxxxxxxxxxxxxxx                           0                      1              sample-docs.json
1      e55b213a9dfb91bcdddddddddddddddd                           0                      1    2020-callforcode-intro.pdf
2      290b6f7cc2e3f70aaaaaaaaaaaaaaaaa                           0                      1  telework-advice-testdata.csv
3  90652dbc-966a-4bbbbbbbbbbbbbbbbbbbbb                           0                      1                   sample.html
4  b15dd4a8-86ca-cccccccccccccccccccccc                           0                      1               kaishi-web.html
5  dbd41633-354b-eeeeeeeeeeeeeeeeeeeeee                           0                      1                    ジェイソン.json
6  b4cdefca-0c17-ffffffffffffffffffffff                           0                      1                   sample.html
7  8a1e13db-0a3f-gggggggggggggggggggggg                           0                      1               jsonsample.json
```

### Delete a document
Run the command. Please get a document-id from "Get a list of documents" command.
```
$ python discovery-docs-tool.py delete document-id
```
#### example
```
$ python discovery-docs-tool.py delete f627e521-d9fe-458d-xxxxxxxxxxxxx
```
