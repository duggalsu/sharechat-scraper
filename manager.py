from sharechat_scrapers import trending_content_scraper, fresh_content_scraper, ml_scraper, virality_scraper
import os
import requests
import pandas as pd
import numpy as np
import re
import datetime
from datetime import datetime, date
from IPython.display import Image, HTML
import time
from time import sleep
from random import uniform
import json
import urllib
import uuid
import boto
import boto3
from boto3 import client
from PIL import Image
import io
from dotenv import load_dotenv
load_dotenv() 
import pymongo
from pymongo import MongoClient
import wget
import sharechat_helper
import s3_mongo_helper 
import tempfile
from tempfile import mkdtemp
import shutil
import subprocess
import logging
import pickle
import selenium
from selenium import webdriver

def scraper_manager(scraper_params):
    try:
        if scraper_params["content_to_scrape"] == "trending":
            trending_content_scraper(USER_ID=scraper_params["USER_ID"],
                                     PASSCODE=scraper_params["PASSCODE"],
                                     tag_hashes=scraper_params["tag_hashes"],
                                     bucket_ids=scraper_params["bucket_ids"],
                                     pages=scraper_params["pages"],
                                     mode=scraper_params["mode"],
                                     targeting=scraper_params["targeting"])
        elif scraper_params["content_to_scrape"] == "fresh":
            if scraper_params["is_cron_job"] == True:
                scraper_params["unix_timestamp"] = str(time.time()).split(".")[0]
            else:
                pass
            fresh_content_scraper(USER_ID=scraper_params["USER_ID"],
                                            PASSCODE=scraper_params["PASSCODE"],
                                            tag_hashes=scraper_params["tag_hashes"],
                                            bucket_ids=scraper_params["bucket_ids"],
                                            pages=scraper_params["pages"],
                                            unix_timestamp=scraper_params["unix_timestamp"],
                                            mode=scraper_params["mode"],
                                            targeting=scraper_params["targeting"]
                                            )
        elif scraper_params["content_to_scrape"] == "virality":
            virality_scraper(USER_ID=scraper_params["USER_ID"], 
                            PASSCODE=scraper_params["PASSCODE"])
        elif scraper_params["content_to_scrape"] == "ml":
            ml_scraper(USER_ID=scraper_params["USER_ID"],
                       PASSCODE=scraper_params["PASSCODE"],
                       tag_hashes=scraper_params["tag_hashes"],
                       bucket_ids=scraper_params["bucket_ids"],
                       pages=scraper_params["pages"],
                       mode=scraper_params["mode"],
                       targeting=scraper_params["targeting"])
        else:
            raise ValueError("Invalid value entered for content_to_scrape. Select one from: trending, fresh, virality, ml")
    except Exception as e:
        print(logging.traceback.format_exc())
