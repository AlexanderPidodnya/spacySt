import streamlit as st
import numpy as np
import pandas as pd
import pytesseract
from pdf2image import convert_from_path, convert_from_bytes
from fastapi import FastAPI, File
from io import BytesIO

def run_OCR2(f_name):

    #f_name = r'F:\Python\OCR_diploma\docs_base\StauffInvoices\363285.pdf' 
    #f_name = r'F:\Python\OCR_diploma\docs_base\acts_raw\170 акт.pdf'
    #f_name = r'F:\Python\OCR_diploma\docs_base\invoices\GOJ000184_СЧФ_6664_01042021.pdf'
    size = 2400
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    f_pdf = open(f_name, 'rb').read()
    images = convert_from_bytes(f_pdf, dpi = 300, size=size)
    res = []
    for img in images:
        strings = pytesseract.image_to_string(img , lang='rus+eng')
        res.append(strings)
        
    #strings = '1234567890' + str(image_file)
        
    return strings

app = FastAPI()

@app.get("/test")
def read_root():
    return {'Hello world!'}

@app.get("/runOCR")    
def run_OCR():

    f_name = r'F:\Python\OCR_diploma\docs_base\StauffInvoices\363285.pdf' 
    f_name = r'F:\Python\OCR_diploma\docs_base\acts_raw\170 акт.pdf'
    f_name = r'F:\Python\OCR_diploma\docs_base\invoices\GOJ000184_СЧФ_6664_01042021.pdf'
    size = 2400
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    f_pdf = open(f_name, 'rb').read()
    images = convert_from_bytes(f_pdf, dpi = 300, size=size)
    res = []
    for img in images:
        strings = pytesseract.image_to_string(img , lang='rus+eng')
        res.append(strings)
        
    return strings

@app.post("/predict")
async def create_file(file: bytes = File(...)):
    return {"result": run_OCR2(file)}

'''

def run_OCR2(f_pdf):

    #f_name = r'F:\Python\OCR_diploma\docs_base\StauffInvoices\363285.pdf' 
    #f_name = r'F:\Python\OCR_diploma\docs_base\acts_raw\170 акт.pdf'
    #f_name = r'F:\Python\OCR_diploma\docs_base\invoices\GOJ000184_СЧФ_6664_01042021.pdf'
    size = 2400
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    #f_pdf = open(f_name, 'rb').read()
    images = convert_from_bytes(f_pdf, dpi = 300, size=size)
    res = []
    for img in images:
        strings = pytesseract.image_to_string(img , lang='rus+eng')
        res.append(strings)
        
    return strings

app = FastAPI()

@app.get("/test")
def read_root():
    return {'Hello world!'}

@app.get("/runOCR")  
def run_OCR():

    #f_name = r'F:\Python\OCR_diploma\docs_base\StauffInvoices\363285.pdf' 
    f_name = r'F:\Python\OCR_diploma\docs_base\acts_raw\170 акт.pdf'
    #f_name = r'F:\Python\OCR_diploma\docs_base\invoices\GOJ000184_СЧФ_6664_01042021.pdf'
    size = 2400
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    f_pdf = open(f_name, 'rb').read()
    images = convert_from_bytes(f_pdf, dpi = 300, size=size)
    res = []
    for img in images:
        strings = pytesseract.image_to_string(img , lang='rus+eng')
        res.append(strings)
        
    return strings

@app.get("/runOCR2") 
async def recognize(file: bytes = File(...)):
    return {'result': run_OCR(file)}
'''
