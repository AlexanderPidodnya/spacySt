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

strSeparator = '\n#########################################################\n'

def pdfDocToString(f_name):
    size = 2400
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    f_pdf = open(f_name, 'rb').read()
    images = convert_from_bytes(f_pdf, dpi = 300, size=size)
    images = convert_from_path(f_name, dpi = 300)
    text = ''
    for img in images:
        text += pytesseract.image_to_string(img , lang='rus+eng', config='--psm 4' )
    return text

def pdfDocToStringRu(f_name):
    size = 2400
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    f_pdf = open(f_name, 'rb').read()
    images = convert_from_bytes(f_pdf, dpi = 300, size=size)
    images = convert_from_path(f_name, dpi = 300)
    text = ''
    for img in images:
        text += pytesseract.image_to_string(img , lang='rus', config='--psm 4' )
    return text

def pdfDocToStringEn(f_name):
    size = 2400
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    f_pdf = open(f_name, 'rb').read()
    images = convert_from_bytes(f_pdf, dpi = 300, size=size)
    images = convert_from_path(f_name, dpi = 300)
    text = ''
    for img in images:
        text += pytesseract.image_to_string(img , lang='eng', config='--psm 4' )
    return text


def shortening(text):
    nlp = spacy.blank("en")

    doc = nlp(text)

    matcher = Matcher(nlp.vocab)

    pattern3 = [
        {'LOWER':'CONTRIBUTING'.lower()},
        {'LOWER':'TO'.lower()}, 
        {'LOWER':'YOUR'.lower()}, 
        {'LOWER':'SUCCESS'.lower()}
        ]
    matcher.add('ENDPAGE', [pattern3])

    pattern4 = [
        {'LOWER':'article'},
        {'LOWER':'code'}, 
        {'LOWER':'price'}, 
        {'LOWER':'eur'},
        {'LOWER':'unit'},
        {'LOWER':'amount'},
        {'LOWER':'eur'}
    ]

    pattern4_ = [{'LOWER':'russische'}, {'LOWER':'foed'}]
    matcher.add('STARTPAGE', [pattern4, pattern4_])

    pattern5  = [
        {'LOWER':'doc.no'},
        {'LOWER':'.'},
        {'LOWER':'/'},
        {'LOWER':'date'},
        {'LOWER':'page'}
    ]
    
    pattern6  = [
        {'LOWER':'doc.по'},
        {'LOWER':'.'},
        {'LOWER':'/'},
        {'LOWER':'date'},
        {'LOWER':'page'}
    ] 
    matcher.add('ABOUTNOPAGE', [pattern5, pattern6])

    doc = nlp(text)

    matches = matcher(doc)
    spans = [Span(doc, start, end, label=match_id) for match_id, start, end in matches]

    paging = []

    pageinfo = {'ABOUTNOPAGE':0, 'STARTPAGE':0, 'ENDPAGE':0}
    shortenText = ''
    firstPage = True
    txt = '''import spacy
    from spacy.tokens import Span

    nlp = spacy.blank("en")\n'''
    docs  = []
    npos = 0
    npage = 0
    for sp in spans:
        if sp.label_  == 'ABOUTNOPAGE':
            pageinfo[sp.label_] = sp.end
        elif sp.label_  == 'STARTPAGE':
            pageinfo[sp.label_] = sp.end
        elif sp.label_  == 'ENDPAGE':
            pageinfo[sp.label_] = sp.start
            paging.append(pageinfo)
            
            if firstPage ==True:
                shortenText = doc[:pageinfo['ENDPAGE']].text
                firstPage = False
                docs.append(doc[:pageinfo['ENDPAGE']].text)
                txt = txt + strSeparator + doc[:pageinfo['ENDPAGE']].text 
            else:
                shortenText = shortenText +  doc[pageinfo['STARTPAGE']:pageinfo['ENDPAGE']].text
                docs.append(doc[pageinfo['STARTPAGE']:pageinfo['ENDPAGE']].text)
                #print(pageinfo, pageinfo['ENDPAGE'] - pageinfo['STARTPAGE'])
                txt = txt + strSeparator + doc[pageinfo['STARTPAGE']:pageinfo['ENDPAGE']].text 

                
                #break
            pageinfo = {'ABOUTNOPAGE':0, 'STARTPAGE':0, 'ENDPAGE':0}
            npage += 1

        #print(pageinfo)
    #print(txt)
    #print(len(paging))
    return shortenText

def run_OCR2(f_name):

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

def text2spans(rtest):
    rtest = rtest.replace(strSeparator, '')

    nlp = spacy.blank("en")
    matcher = Matcher(nlp.vocab)

    patternPurchase = [{'LOWER': 'purchase'}, 
        {'LOWER':'order'}, 
        {'LOWER':'number'}, 
        {'LOWER': ':'}]
    matcher.add('PTRPURCHASE', [patternPurchase])

    patternTariff = [{'LOWER': 'customs'}, 
        {'LOWER':'tariff'}, 
        {'IS_ALPHA': True},
        {'IS_PUNCT': True, 'OP': '*'}, 
        {'IS_DIGIT': True}]
    matcher.add('PTRTARIFF', [patternTariff])

    patternCountry = [{'LOWER': 'country'}, 
        {'LOWER':'of'} , 
        {'LOWER': 'origin'}, 
        {'LOWER': ':'}, 
        {'IS_ALPHA': True}]
    matcher.add('PTRCOUNTRY', [patternCountry])

    patternPC = [{'LIKE_NUM': True}, {'LIKE_NUM': True},
        {'LOWER' : {'in' : ['pc', 'рс']}},
        {'LIKE_NUM':True}    ] 

    matcher.add('PTROFPC', [patternPC])

    doc1 = nlp(rtest)

    #print("Verbs:", [token.text for token in doc1[45:54]])

    matches = matcher(doc1)
    spans = [Span(doc1, start, end, label=match_id) for match_id, start, end in matches]

    startSpan = 0
    endSpan = 0
    #posTariff = 0
    #txt2 = 'import json \nimport spacy \nfrom spacy.matcher import Matcher \nfrom spacy.tokens import Span, DocBin \ndocs = [] \n'
    #nPos = 0
    docs = []
    pos2PC = 0
    for sp in spans:
        if sp.label_  == 'PTRPURCHASE':
            startSpan = sp.start
            
        #elif sp.label_  == 'PTRTARIFF':             posTariff = sp.end-1
            
        #elif sp.label_  == 'PTROFPC':             pos2PC = sp.start
        
        elif sp.label_  == 'PTRCOUNTRY':
            endSpan = sp.end
            #pos2PC = pos2PC - startSpan  
            

            docs.append(doc1[startSpan:endSpan].text)
            
    return docs

def transfer(fName):
    text = pdfDocToString(f_name=fName)
    txtS = shortening(text)
    docs = text2spans(txtS)
    nlp_ = spacy.load(r"C:\Users\AdminAsus\source\python\spacyST\spacySt-1\output\model-best")
    answer = []
    for doc in docs:
        docx = nlp_(doc)
        #print(docx.ents)
        res = []
        for ent in docx.ents:
            res.append((ent.label_, ent.text))
        answer.append(res)
    jsonStr = json.dumps(answer) 
    return jsonStr

app = FastAPI()

@app.post("/stauff")
async def recognise_stauffe_file(file: bytes = File(...)):
    #return {'result' : file}
    return {"result": transfer(file)}

@app.get("/test2")
def read_root():
    return {'Hello world!'}

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

@app.post("/predict2")
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
