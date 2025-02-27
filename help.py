import streamlit as st
from tokenize import String
from pymongo import MongoClient
from pprint import pprint
import pandas as pd
import json
import os

#-------------------------------#
#--------Initialization---------#
#-------------------------------#

##initialize connection to the database (will not exist until something is loaded into it)
# MongoDB Connection
MONGO_URI = "mongodb+srv://Sean:12345@magicdahtebahse.lfcpi.mongodb.net/"
client = MongoClient(MONGO_URI)

#Choosing the database and the collection
db = client["mtgdb"]
collection = db["cards"]

