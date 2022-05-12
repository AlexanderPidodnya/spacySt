import streamlit as st
import numpy as np
import pandas as pd
import pytesseract
from pdf2image import convert_from_path, convert_from_bytes
from fastapi import FastAPI, File
from io import BytesIO
import json
import spacy as spacy
from spacy.tokens import Span
from spacy.matcher import Matcher
from datetime import datetime

app = FastAPI()

def appendLogEvent(methName, desc):
    logFile = r'C:\Users\alex1c\sources\spacySt\StauffInvoices\log\log.txt'
    with open(logFile, 'a') as logFile:
        #print(datetime.datetime.now())
        logFile.write(str(datetime.now()) + ' ' + ' method: ' + methName + ', event: ' + desc + '\n')

@app.get('/get_test/')
def func_get_test(first: int = 0, second: str=''):
    appendLogEvent('func_get_test', str({first : second}))
    return {first : second}