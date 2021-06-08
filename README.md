# discovery-admin
IBM Watson Discovery document management tool. 
- View Documents list in your collection
- List training data
- Search : Natural Language Query 
- Delete a document
- Add (upload) a document
- Update a document

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
$ pip install pandas
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
### List training data
Run a command.
```
$ python discovery-docs-tool.py traindata
```
#### output example
Lists the training data for the specified collection.
```
                        collection_id                       environment_id                                            queries
0  b2abe765-b072-4806-8c7a-collection  52c60672-bf2a-469b-96dc-environment  [{'natural_language_query': 'Watson Health', '...
```

### Search : Natural Language Query 
Run a command.
```
$ python discovery-docs-tool-test.py search keyword
```
#### example
```
$ python discovery-docs-tool-test.py search "Watson Health"
```
#### output example
```
                                     id  result_metadata.confidence  result_metadata.score extracted_metadata.filename
0  90652dbc-966a-401d-99a8-xxxxxxxxxxxx                    0.375145               4.428401                 sample.html
1  b4cdefca-0c17-4d08-a33a-aaaaaaaaaaaa                    0.375145               4.428401                 sample.html
2    8daac09bce0a793064a8d9bbbbbbbbbb_b                    0.000000               1.473007            sample-docs.json
```

### Search : Natural Language Query (Output format : JSON) 
#### example
```
$ python discovery-docs-tool-test.py searchjson "Watson Health"
```
#### output example
```
{
  "id":{
    "0":"90652dbc-966a-401d-99a8-xxxxxxxxxxxx",
    "1":"b4cdefca-0c17-4d08-a33a-aaaaaaaaaaaa",
    "2":"8daac09bce0a793064a8d9bbbbbbbbbb_b"
  },
  "result_metadata.confidence":{
    "0":0.3751451698,
    "1":0.3751451698,
    "2":0.0                                                                                                                                                         },
  "result_metadata.score":{
    "0":4.428401,
    "1":4.428401,
    "2":1.4730074
  },
  "extracted_metadata.filename":{
    "0":"sample.html",
    "1":"sample.html",
    "2":"sample-docs.json"
  }
}

```
### Delete a document
Run a command. Please get a document-id from "Get a list of documents" command.
```
$ python discovery-docs-tool.py delete document-id
```
#### example
```
$ python discovery-docs-tool.py delete 8daac09bce0a793064a8d9bbbbbbbbbb_b
```
### Add(Upload) a document
Run a command.
```
$ python discovery-docs-tool.py add file-path
```
#### example
```
$ python discovery-docs-tool.py add /home/user1/sample.json
```
#### Error information
- The Error occurred in PDF with Japanese file name. But I was able to upload a JSON or HTML file with a Japanese file name.

### Update a document
Run a command.
```
$ python discovery-docs-tool.py update file-path document-id
```
#### example
```
$ python discovery-docs-tool.py update /home/user1/sample.json 90652dbc-966a-401d-99a8-xxxxxxxxxxxx
```
