[English version](https://github.com/kolinz/discovery-admin/blob/main/README.md)

# discovery-admin
このツールは、Watson Discovery向けのドキュメント管理ツールです。Watson Discoveryで、ドキュメントの削除や更新を行う際には、「API」経由で実施する前提になっております。
システムを運用する人は、必ずしも開発者ではないため、API利用をサポートするツールとして作成しました。

## 出来ること
- コレクション内のドキュメント情報を一覧表示
- トレーニングデータの一覧表示
- 自然文検索(Natural Language Query)
- コレクション内のドキュメント削除
- コレクションに、ドキュメント追加(アップロード)
- コレクション内のドキュメント更新(アップデート)

## 参考資料
Watson Discovery API : https://cloud.ibm.com/apidocs/discovery

## 確認済み環境
- Ubuntu 20.04 LTS / Server版およびDesktop版で確認。
- Python 3.8.5
- pip 21.1.2
- pythonとpipのエイリアスを設定


pythonとpipのエイリアス設定例 : bashrc
```
alias python="python3" 
alias pip="pip3" 
```

## 事前準備
### ステップ1
本ツール実行に必要なソフトウェアのインストール
```
$ pip install ibm-watson
$ pip install python-dotenv
$ pip install pandas
```
### ステップ2
本ツールをダウンロードし、ディレクトリに移動
```
$ git clone https://github.com/kolinz/discovery-admin.git
$ cd discovery-admin
```
### ステップ3
.env ファイルの編集
```
apikey = "リソースリストからアクセスできるWatson Discoveryの管理に表示される「API鍵」"
url = "リソースリストからアクセスできるWatson Discoveryの管理に表示される「URL」"
environment_id = "Watson Discoveryのコレクション内で確認できる「environment_id」"
collection_id = "Watson Discoveryのコレクション内で確認できる「collection_id」"
```
## 使い方
### コレクション内のドキュメント情報を一覧表示
コマンドを実行
```
$ python discovery-docs-tool.py docslist
```
実行結果例
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

### トレーニングデータの一覧表示
コマンドを実行
```
$ python discovery-docs-tool.py traindata
```
実行結果例
```
                        collection_id                       environment_id                                            queries
0  b2abe765-b072-4806-8c7a-collection  52c60672-bf2a-469b-96dc-environment  [{'natural_language_query': 'Watson Health', '...
```

### 自然文検索(Natural Language Query)
コマンドを実行
```
$ python discovery-docs-tool-test.py search keyword
```
実行例
```
$ python discovery-docs-tool-test.py search "Watson Health"
```
実行結果例
```
                                     id  result_metadata.confidence  result_metadata.score extracted_metadata.filename
0  90652dbc-966a-401d-99a8-xxxxxxxxxxxx                    0.375145               4.428401                 sample.html
1  b4cdefca-0c17-4d08-a33a-aaaaaaaaaaaa                    0.375145               4.428401                 sample.html
```

### コレクション内のドキュメント削除
コマンドを実行
- 利用にあたり必要となる「ドキュメントID」は、「自然文検索」や「コレクション内のドキュメント情報を一覧表示」から取得します。
```
$ python discovery-docs-tool.py delete document-id
```
実行例
```
$ python discovery-docs-tool.py delete 8daac09bce0a793064a8d9bbbbbbbbbb_b
```

### コレクションに、ドキュメント追加(アップロード)
コマンドを実行
```
$ python discovery-docs-tool.py add file-path
```
実行例
```
$ python discovery-docs-tool.py add /home/user1/sample.json
```
エラー情報 (2021年6月現在)
本ツールで、日本語ファイル名のPDFをアップロードした場合に、エラーになることがあります。JSONやHTML形式のドキュメントの場合はエラーは発生しておりません。

### コレクション内のドキュメント更新(アップデート)
コマンドを実行
```
$ python discovery-docs-tool.py update file-path document-id
```
実行例
```
$ python discovery-docs-tool.py update /home/user1/sample.json 90652dbc-966a-401d-99a8-xxxxxxxxxxxx
```
