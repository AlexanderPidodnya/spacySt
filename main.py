import string, os
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

directory = r"C:\Users\alex1c\sources\spacySt\StauffInvoices"
strSeparator = '\n#########################################################\n'

def appendLogEvent(methName, desc):
    logFile = r'C:\Users\alex1c\sources\spacySt\StauffInvoices\log\log.txt'
    with open(logFile, 'a') as logFile:
        #print(datetime.datetime.now())
        logFile.write(str(datetime.now()) + ' ' + ' method: ' + methName + ', event: ' + desc + '\n')

def saveIntermediateResult(f_name, content):
    with open(f_name, 'w') as txtFile:
        #print(datetime.datetime.now())
        txtFile.write(content) 

def getDocName(f_name = ''):
    return f_name.split('\\')[-1].split('.')[0]

def getTimeSuffix():
    return str(datetime.now()).replace('-','_').replace(':','_').replace('.','_').replace(' ','_')

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

def fixRandomSubstitutions(text):
    text = text.replace('А', 'A').replace('В', 'B').replace('С', 'C').replace('Е', 'E').replace('Н', 'H')
    text = text.replace('К', 'K').replace('М', 'M').replace('О', 'O').replace('Р', 'P').replace('Т', 'T').replace('Х', 'X')
    text = text.replace('а', 'a').replace('с', 'c').replace('е', 'e').replace('о', 'o').replace('р', 'p')
    text = text.replace('п', 'n').replace('х', 'x')
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
    #fixRandomSubstitutions(text)

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
                txt = txt + strSeparator + doc[pageinfo['STARTPAGE']:pageinfo['ENDPAGE']].text 
            pageinfo = {'ABOUTNOPAGE':0, 'STARTPAGE':0, 'ENDPAGE':0}
            npage += 1


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
    matches = matcher(doc1)
    spans = [Span(doc1, start, end, label=match_id) for match_id, start, end in matches]

    startSpan = 0
    endSpan = 0
    docs = []
#    pos2PC = 0
    for sp in spans:
        if sp.label_  == 'PTRPURCHASE':
            startSpan = sp.start
        elif sp.label_  == 'PTRCOUNTRY':
            endSpan = sp.end
            docs.append(doc1[startSpan:endSpan].text)
            
    return docs

def text2spans26(rtest):
    rtest = rtest.replace(strSeparator, '')

    nlp = spacy.blank("en")
    fullDoc = nlp(rtest)
    matcher = Matcher(nlp.vocab)

    patternNOrder = [{'LOWER': 'order'}, {'LOWER':'number'}, {'LOWER':':'}, {'LIKE_NUM': True}]
    matcher.add('NORDER', [patternNOrder])
    matches = matcher(fullDoc)
    prepSpans = [Span(fullDoc, start, end, label=match_id) for match_id, start, end in matches]
    stPos = 0
    pos = 0
    docs = []
    for prepItem in prepSpans:
        if stPos == 0:
            stPos = prepItem.start
        else:
            doc1 = fullDoc[stPos : prepItem.start].text
            docs.append(doc1)
            pos += 1
            stPos = prepItem.start 
    if stPos !=0:
        doc1 = fullDoc[stPos:].text
        docs.append(doc1)

    return docs

def transferByModel(fName, nlp_):
    dirName = getDocName(fName)
    fullDirName = os.path.join(directory, dirName)
    #print(fullDirName)
    if not os.path.exists(fullDirName):
        #print(fullDirName)
        os.makedirs(fullDirName)   
    comPartFname = getTimeSuffix()

    matchedFiles = [x for x in os.listdir(fullDirName) if '_shorten.txt' in x] 
    if len(matchedFiles) !=0:
        recPDF = os.path.join(fullDirName, matchedFiles[0])
        print(recPDF)
        #if os.path.exists(recPDF):
        with open(recPDF, 'r') as txtFile:
            #print(datetime.datetime.now())
            txtS = txtFile.read() 
            print("Found shorten text ", recPDF) 
    else:   
        matchedFiles = [x for x in os.listdir(fullDirName) if '_text.txt' in x]
        
        if len(matchedFiles) !=0:
            recPDF = os.path.join(fullDirName, matchedFiles[0])
            print(recPDF)
            #if os.path.exists(recPDF):
            with open(recPDF, 'r') as txtFile:
                #print(datetime.datetime.now())
                text = txtFile.read()  
                print("Found recognized text ", recPDF)
        else:   
            text = pdfDocToString(f_name=fName)
            saveIntermediateResult(os.path.join(fullDirName, comPartFname + '_text.txt'), text)
            print("Recognize pdf to text")
    
        txtS = shortening(text)
        saveIntermediateResult(os.path.join(fullDirName, comPartFname + '_shorten.txt'), txtS)
        print("Shortened  text")

    #text = pdfDocToString(f_name=fName)
    #saveIntermediateResult(os.path.join(fullDirName, comPartFname + '_text.txt'), text)
    #txtS = shortening(text)
    #saveIntermediateResult(os.path.join(fullDirName, comPartFname + '_shorten.txt'), txtS)
    docs = text2spans26(txtS)
    #nlp_ = spacy.load(r"C:\Users\alex1c\sources\spacySt\output_1\model-best")
    answer = []
    processing = ''

    for doc in docs:
        processing += doc + '\n'
        docx = nlp_(doc)
        res = []
        ner = ''
        for ent in docx.ents:
            try:
                ner += '#' + ent.label_ + ':' + ent.text+'\n'
            except:
                print(ent.label_, ent.text, type(ent.label_), type(ent.text))
                ner += '#ERR' + str(ent.label_)+ ':' + str(ent.text)+'\n'
            res.append((ent.label_, ent.text))
        answer.append(res)
        processing += 'NER' + ner
    saveIntermediateResult(os.path.join(fullDirName, comPartFname + '_proc.txt'), processing)
    jsonStr = json.dumps(answer) 
    return jsonStr

def transfer(fName):
    nlp_ = spacy.load(r"C:\Users\alex1c\sources\spacySt\output_1\model-best")
    return transferByModel(fName, nlp_)

    dirName = getDocName(fName)
    fullDirName = os.path.join(directory, dirName)
    #print(fullDirName)
    if not os.path.exists(fullDirName):
        #print(fullDirName)
        os.makedirs(fullDirName)   
    comPartFname = getTimeSuffix()

    text = pdfDocToString(f_name=fName)
    saveIntermediateResult(os.path.join(fullDirName, comPartFname + '_text.txt'), text)
    txtS = shortening(text)
    saveIntermediateResult(os.path.join(fullDirName, comPartFname + '_sh_text.txt'), txtS)
    docs = text2spans(txtS)
    nlp_ = spacy.load(r"C:\Users\alex1c\sources\spacySt\output_1\model-best")
    answer = []
    processing = ''

    for doc in docs:
        processing += doc + '\n'
        docx = nlp_(doc)
        res = []
        ner = ''
        for ent in docx.ents:
            try:
                ner += '#' + ent.label_ + ':' + ent.text+'\n'
            except:
                print(ent.label_, ent.text, type(ent.label_), type(ent.text))
            res.append((ent.label_, ent.text))
        answer.append(res)
        processing += 'NER' + ner
    saveIntermediateResult(os.path.join(fullDirName, comPartFname + '_proc.txt'), processing)
    jsonStr = json.dumps(answer) 
    return jsonStr

def transfer26(fName):
    nlp_ = spacy.load(r"C:\Users\alex1c\sources\spacySt\output26\model-best")
    return transferByModel(fName, nlp_)


    text = pdfDocToString(f_name=fName)
    txtS = shortening(text)
    docs = text2spans26(txtS)
    nlp_ = spacy.load(r"C:\Users\alex1c\sources\spacySt\output26\model-best")
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

@app.get("/stauff1/")
async def recognise_stauffe_file1(file: str):
    #file = file.replace("/", "\\")
    res = ''
    with open(file, 'r') as f:
        print('stauff_get ', f.name)
        res = transfer(file)
    #print('stauff26_get ', str(file))
    appendLogEvent('stauff_get', str(f.name))
    return {"result" : res}
    #return {"result": transfer(file)}

@app.get("/stauff26/")
async def recognise_stauffe_file1(file: str):
    #file = file.replace("/", "\\")
    res = ''
    with open(file, 'r') as f:
        print('stauff26_get ', f.name)
        res = transfer26(file)
    #print('stauff26_get ', str(file))
    appendLogEvent('stauff26_get', str(f.name))
    return {"result" : res}
    #return {"result": transfer(file)}

@app.post("/stauff")
#async def recognise_stauffe_file(file: bytes = File(...)):
async def recognise_stauffe_file(file: str = ''):
    appendLogEvent('stauff', file)
    print('test', file)
    return {"result" : file}
    #return {"result": transfer(file)}

@app.get("/stauff26_get/")
def recognise_stauffe_file26(file: bytes = File(...)):
    #file = file.replace("/", "\\")
    print('stauff26_get ', str(file))
    appendLogEvent('stauff26_get', str(file))
   
    return {"result1" : file}
    #return {"result": transfer26(file)}

@app.post("/stauff26")
async def recognise_stauffe_file26(file: bytes = File(...)):
#async def recognise_stauffe_file26(file: str):
    #print('stauff26_get ', file)
    appendLogEvent('stauff26_get', str(file))
    return {"result": transfer26(file)}

@app.get("/test2")
def read_root():
    return {'Hello world!'}

@app.get("/test")
def read_root():
    return {'Hello Simon!'}

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
