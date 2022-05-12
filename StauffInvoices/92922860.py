import json 
import spacy 
from spacy.matcher import Matcher 
from spacy.tokens import Span, DocBin 
docs = [] 


doc0 = nlp('''Purchase order number: N SR-1-06 1178
1900 2 РС 6100232260 140,25 1 РС 280,50

SFA-030-G-20-V-T-G12-B-V

packed per each item

Product description: filter element
Export - Customs tariff по.: 84212980
Country of origin: Great Britain

Material Surcharge 8,90''')
#doc0 c:SR-1-06 c1:1178 pos:1900 a:2 art:6100232260 pr:6100232260 u:1 s:280,50 trf:84212980 cnt:: Great Britain chr:Surcharge chrS:% TTL:
print("doc0",doc0[5: 8], doc0[8: 9], doc0[10: 11], doc0[11: 12], doc0[13: 14], doc0[14:15], doc0[15:16] ,doc0[17:18], doc0[52: 53], doc0[57: 60]), doc0[62: 63], doc0[64: 65], doc0[66: 67]  
doc0.ents = [Span(doc0, 5, 8, label="CONTRACT"), 
    Span(doc0, 8, 9, label="CONTRACT1"), 
    Span(doc0, 10, 11, label="POS"), 
    Span(doc0, 11, 12, label="AMOUNT"), 
    Span(doc0, 14, 15, label="ARTICLE"), 
    Span(doc0, 14, 15, label="PRICE"), 
    Span(doc0, 15, 16, label="UNIT"), 
    Span(doc0, 17, 18, label="SUM"), 
    Span(doc0, 52, 53, label="TARIFF"), 
    Span(doc0, 57, 60, label="COUNTRY"), 
    Span(doc0, 62, 63, label="CHARGE"), 
    Span(doc0, 64, 65, label="CHARGES"), 
    Span(doc0, 66, 67, label="TOTAL") 
docs.append(doc0)
doc_bin = DocBin(docs = docs)
doc_bin.to_disk('./train.spacy')