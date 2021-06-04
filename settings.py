# coding: UTF-8
import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

apikey = os.environ.get("apikey")
url = os.environ.get("url")
environment_id = os.environ.get("environment_id")
collection_id = os.environ.get("collection_id")