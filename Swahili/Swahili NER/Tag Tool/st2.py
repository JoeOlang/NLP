import streamlit as st
import random
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# FIRE STORE DB
cred = credentials.Certificate("credentials.json")

# confirm credentials exist, else terminate entire program
if not cred:
    print("No credentials found. Please check your credentials.json file")
    exit()

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()