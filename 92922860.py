import json 
import spacy 
from spacy.matcher import Matcher 
from spacy.tokens import Span, DocBin 
docs = [] 


doc0 = nlp('''Purchase order number: N SR-1-06 604
1200 4 РС 6100074594 (*) 13,79 1 РС 55,16

QRC-FF-19-M-22L-BP-W3

FF19-2-L2230

packed per each item

Export - Customs tariff no.: 84812010
Country of origin: Germany''')
#doc0SR-1-06 604 1200 4 6100074594 13,79 1  84812010 Germany
print("doc0",doc0[5: 8], doc0[8: 9], doc0[10: 11], doc0[11: 12], doc0[13: 14], doc0[17:18], doc0[18:19] ,doc0[20:21], doc0[50: 51], doc0[56: 57]) 
doc0.ents = [Span(doc0, 5, 8, label="CONTRACT"), 
    Span(doc0, 8, 9, label="CONTRACT1"), 
    Span(doc0, 10, 11, label="POS"), 
    Span(doc0, 11, 12, label="AMOUNT"), 
    Span(doc0, 13, 14, label="ARTICLE"), 
    Span(doc0, 17, 18, label="PRICE"), 
    Span(doc0, 18, 19, label="UNIT"), 
    Span(doc0, 20, 21, label="SUM"), 
    Span(doc0, 50, 51, label="TARIFF"), 
    Span(doc0, 56, 57, label="COUNTRY")] 
docs.append(doc0)


doc1 = nlp('''Purchase order number: N SR-1-06 711
1300 50 PC 6010003476 (*) 237,81 100 PC 118,91

FI-EWD-15L-V-W3-DKO
FI-EWD-15L-B-W3-DKO

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc1SR-1-06 711 1300 50 6010003476 237,81 100  73079910 Germany
print("doc1",doc1[5: 8], doc1[8: 9], doc1[10: 11], doc1[11: 12], doc1[13: 14], doc1[17:18], doc1[18:19] ,doc1[20:21], doc1[59: 60], doc1[65: 66]) 
doc1.ents = [Span(doc1, 5, 8, label="CONTRACT"), 
    Span(doc1, 8, 9, label="CONTRACT1"), 
    Span(doc1, 10, 11, label="POS"), 
    Span(doc1, 11, 12, label="AMOUNT"), 
    Span(doc1, 13, 14, label="ARTICLE"), 
    Span(doc1, 17, 18, label="PRICE"), 
    Span(doc1, 18, 19, label="UNIT"), 
    Span(doc1, 20, 21, label="SUM"), 
    Span(doc1, 59, 60, label="TARIFF"), 
    Span(doc1, 65, 66, label="COUNTRY")] 
docs.append(doc1)


doc2 = nlp('''Purchase order number: N SR-1-06 923
1400 100 PC 6100049574 (*) 1,96 1 РС 196,00
HCS-25-DKO-28L-S-OR-B-M-W3
11221N25

packed per each item

Product description: connector

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc2SR-1-06 923 1400 100 6100049574 1,96 1  73079910 Germany
print("doc2",doc2[5: 8], doc2[8: 9], doc2[10: 11], doc2[11: 12], doc2[13: 14], doc2[17:18], doc2[18:19] ,doc2[20:21], doc2[55: 56], doc2[61: 62]) 
doc2.ents = [Span(doc2, 5, 8, label="CONTRACT"), 
    Span(doc2, 8, 9, label="CONTRACT1"), 
    Span(doc2, 10, 11, label="POS"), 
    Span(doc2, 11, 12, label="AMOUNT"), 
    Span(doc2, 13, 14, label="ARTICLE"), 
    Span(doc2, 17, 18, label="PRICE"), 
    Span(doc2, 18, 19, label="UNIT"), 
    Span(doc2, 20, 21, label="SUM"), 
    Span(doc2, 55, 56, label="TARIFF"), 
    Span(doc2, 61, 62, label="COUNTRY")] 
docs.append(doc2)


doc3 = nlp('''Purchase order number: N SR-1-06 933
1500 300 PC 6100049574 (*) 1,96 1 РС 588,00
HCS-25-DKO-28L-S-OR-B-M-W3
11221N25

packed per each item

Product description: connector

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc3SR-1-06 933 1500 300 6100049574 1,96 1  73079910 Germany
print("doc3",doc3[5: 8], doc3[8: 9], doc3[10: 11], doc3[11: 12], doc3[13: 14], doc3[17:18], doc3[18:19] ,doc3[20:21], doc3[55: 56], doc3[61: 62]) 
doc3.ents = [Span(doc3, 5, 8, label="CONTRACT"), 
    Span(doc3, 8, 9, label="CONTRACT1"), 
    Span(doc3, 10, 11, label="POS"), 
    Span(doc3, 11, 12, label="AMOUNT"), 
    Span(doc3, 13, 14, label="ARTICLE"), 
    Span(doc3, 17, 18, label="PRICE"), 
    Span(doc3, 18, 19, label="UNIT"), 
    Span(doc3, 20, 21, label="SUM"), 
    Span(doc3, 55, 56, label="TARIFF"), 
    Span(doc3, 61, 62, label="COUNTRY")] 
docs.append(doc3)


doc4 = nlp('''Purchase order number: N SR-1-06 942
1600 481 PC 6100076765 (*) 3,85 1 РС 1.851,85

ОКС-НР-12-Е-М201К-В-М/З
HP10-1-X0041N

packed per each item

Customer ID-No.: 6100076765
Product description: coupling

Export - Customs tariff no.: 84812010
Country of origin: Germany''')
#doc4SR-1-06 942 1600 481 6100076765 3,85 1  84812010 Germany
print("doc4",doc4[5: 8], doc4[8: 9], doc4[10: 11], doc4[11: 12], doc4[13: 14], doc4[17:18], doc4[18:19] ,doc4[20:21], doc4[67: 68], doc4[73: 74]) 
doc4.ents = [Span(doc4, 5, 8, label="CONTRACT"), 
    Span(doc4, 8, 9, label="CONTRACT1"), 
    Span(doc4, 10, 11, label="POS"), 
    Span(doc4, 11, 12, label="AMOUNT"), 
    Span(doc4, 13, 14, label="ARTICLE"), 
    Span(doc4, 17, 18, label="PRICE"), 
    Span(doc4, 18, 19, label="UNIT"), 
    Span(doc4, 20, 21, label="SUM"), 
    Span(doc4, 67, 68, label="TARIFF"), 
    Span(doc4, 73, 74, label="COUNTRY")] 
docs.append(doc4)


doc5 = nlp('''Purchase order number: N SR-1-06 1015
1700 7 РС 9910000425 2,00 1 РС 14,00

CAT-5-QUICK-RELEASE CPLNGS-ENG
Kat-5-Schnellverschlusskupplungen-ENG
packed per each item

Product description: sales catalogue
Export - Customs tariff по.: 49111010
Country of origin: Germany''')
#doc5SR-1-06 1015 1700 7 9910000425 2,00 1  49111010 Germany
print("doc5",doc5[5: 8], doc5[8: 9], doc5[10: 11], doc5[11: 12], doc5[13: 14], doc5[14:15], doc5[15:16] ,doc5[17:18], doc5[52: 53], doc5[58: 59]) 
doc5.ents = [Span(doc5, 5, 8, label="CONTRACT"), 
    Span(doc5, 8, 9, label="CONTRACT1"), 
    Span(doc5, 10, 11, label="POS"), 
    Span(doc5, 11, 12, label="AMOUNT"), 
    Span(doc5, 13, 14, label="ARTICLE"), 
    Span(doc5, 14, 15, label="PRICE"), 
    Span(doc5, 15, 16, label="UNIT"), 
    Span(doc5, 17, 18, label="SUM"), 
    Span(doc5, 52, 53, label="TARIFF"), 
    Span(doc5, 58, 59, label="COUNTRY")] 
docs.append(doc5)


doc6 = nlp('''Purchase order number: N SR-1-06 1043
1800 5 PC 9910000425 2,00 1 РС 10,00

CAT-5-QUICK-RELEASE CPLNGS-ENG
Kat-5-Schnellverschlusskupplungen-ENG
packed per each item

Product description: sales catalogue
Export - Customs tariff по.: 49111010
Country of origin: Germany''')
#doc6SR-1-06 1043 1800 5 9910000425 2,00 1  49111010 Germany
print("doc6",doc6[5: 8], doc6[8: 9], doc6[10: 11], doc6[11: 12], doc6[13: 14], doc6[14:15], doc6[15:16] ,doc6[17:18], doc6[52: 53], doc6[58: 59]) 
doc6.ents = [Span(doc6, 5, 8, label="CONTRACT"), 
    Span(doc6, 8, 9, label="CONTRACT1"), 
    Span(doc6, 10, 11, label="POS"), 
    Span(doc6, 11, 12, label="AMOUNT"), 
    Span(doc6, 13, 14, label="ARTICLE"), 
    Span(doc6, 14, 15, label="PRICE"), 
    Span(doc6, 15, 16, label="UNIT"), 
    Span(doc6, 17, 18, label="SUM"), 
    Span(doc6, 52, 53, label="TARIFF"), 
    Span(doc6, 58, 59, label="COUNTRY")] 
docs.append(doc6)


doc7 = nlp('''Purchase order number: N SR-1-06 1178
1900 2 РС 6100232260 140,25 1 РС 280,50

SFA-030-G-20-V-T-G12-B-V

packed per each item

Product description: filter element
Export - Customs tariff по.: 84212980
Country of origin: Germany''')
#doc7SR-1-06 1178 1900 2 6100232260 140,25 1  84212980 Germany
print("doc7",doc7[5: 8], doc7[8: 9], doc7[10: 11], doc7[11: 12], doc7[13: 14], doc7[14:15], doc7[15:16] ,doc7[17:18], doc7[51: 52], doc7[57: 58]) 
doc7.ents = [Span(doc7, 5, 8, label="CONTRACT"), 
    Span(doc7, 8, 9, label="CONTRACT1"), 
    Span(doc7, 10, 11, label="POS"), 
    Span(doc7, 11, 12, label="AMOUNT"), 
    Span(doc7, 13, 14, label="ARTICLE"), 
    Span(doc7, 14, 15, label="PRICE"), 
    Span(doc7, 15, 16, label="UNIT"), 
    Span(doc7, 17, 18, label="SUM"), 
    Span(doc7, 51, 52, label="TARIFF"), 
    Span(doc7, 57, 58, label="COUNTRY")] 
docs.append(doc7)


doc8 = nlp('''Purchase order number: N SR-1-06 1231
2500 40 РС 6010003710 (*) 393,09 100 PC 157,24


Description

FI-ELD-1 5L-V-W3-DKO
FI-ELD-15L-B-W3-DKO

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc8SR-1-06 1231 2500 40 6010003710 393,09 100  73079910 Germany
print("doc8",doc8[5: 8], doc8[8: 9], doc8[10: 11], doc8[11: 12], doc8[13: 14], doc8[17:18], doc8[18:19] ,doc8[20:21], doc8[62: 63], doc8[68: 69]) 
doc8.ents = [Span(doc8, 5, 8, label="CONTRACT"), 
    Span(doc8, 8, 9, label="CONTRACT1"), 
    Span(doc8, 10, 11, label="POS"), 
    Span(doc8, 11, 12, label="AMOUNT"), 
    Span(doc8, 13, 14, label="ARTICLE"), 
    Span(doc8, 17, 18, label="PRICE"), 
    Span(doc8, 18, 19, label="UNIT"), 
    Span(doc8, 20, 21, label="SUM"), 
    Span(doc8, 62, 63, label="TARIFF"), 
    Span(doc8, 68, 69, label="COUNTRY")] 
docs.append(doc8)


doc9 = nlp('''Purchase order number: N SR-1-06 1267
2600 1 РС 6100122987 0,49 1 РС 0,49

QRC-FF-10-DF-30-K-RD

FF10-9-RT001

packed per each item

Product description: cap

Export - Customs tariff no.: 39235090
Country of origin: Italy''')
#doc9SR-1-06 1267 2600 1 6100122987 0,49 1  39235090 Italy
print("doc9",doc9[5: 8], doc9[8: 9], doc9[10: 11], doc9[11: 12], doc9[13: 14], doc9[14:15], doc9[15:16] ,doc9[17:18], doc9[52: 53], doc9[58: 59]) 
doc9.ents = [Span(doc9, 5, 8, label="CONTRACT"), 
    Span(doc9, 8, 9, label="CONTRACT1"), 
    Span(doc9, 10, 11, label="POS"), 
    Span(doc9, 11, 12, label="AMOUNT"), 
    Span(doc9, 13, 14, label="ARTICLE"), 
    Span(doc9, 14, 15, label="PRICE"), 
    Span(doc9, 15, 16, label="UNIT"), 
    Span(doc9, 17, 18, label="SUM"), 
    Span(doc9, 52, 53, label="TARIFF"), 
    Span(doc9, 58, 59, label="COUNTRY")] 
docs.append(doc9)


doc10 = nlp('''Purchase order number: N SR-1-06 1362
2700 400 PC 2012031318 (*) 0,25 1 РС 100,00
HF-1000-06-W3
15011NO06

packed per each item
Export - Customs tariff no.: 73079980
Country of origin: Germany''')
#doc10SR-1-06 1362 2700 400 2012031318 0,25 1  73079980 Germany
print("doc10",doc10[5: 8], doc10[8: 9], doc10[10: 11], doc10[11: 12], doc10[13: 14], doc10[17:18], doc10[18:19] ,doc10[20:21], doc10[42: 43], doc10[48: 49]) 
doc10.ents = [Span(doc10, 5, 8, label="CONTRACT"), 
    Span(doc10, 8, 9, label="CONTRACT1"), 
    Span(doc10, 10, 11, label="POS"), 
    Span(doc10, 11, 12, label="AMOUNT"), 
    Span(doc10, 13, 14, label="ARTICLE"), 
    Span(doc10, 17, 18, label="PRICE"), 
    Span(doc10, 18, 19, label="UNIT"), 
    Span(doc10, 20, 21, label="SUM"), 
    Span(doc10, 42, 43, label="TARIFF"), 
    Span(doc10, 48, 49, label="COUNTRY")] 
docs.append(doc10)


doc11 = nlp('''Purchase order number: N SR-1-06 1432
2800 474 РС 6100079873 8,49 1 РС 4.024,26
RTE-58-D-25-B


Description

RTE-58D25B

packed per each item

Product description: filter element
Export - Customs tariff по.: 84212980
Country of origin: Italy''')
#doc11SR-1-06 1432 2800 474 6100079873 8,49 1  84212980 Italy
print("doc11",doc11[5: 8], doc11[8: 9], doc11[10: 11], doc11[11: 12], doc11[13: 14], doc11[14:15], doc11[15:16] ,doc11[17:18], doc11[47: 48], doc11[53: 54]) 
doc11.ents = [Span(doc11, 5, 8, label="CONTRACT"), 
    Span(doc11, 8, 9, label="CONTRACT1"), 
    Span(doc11, 10, 11, label="POS"), 
    Span(doc11, 11, 12, label="AMOUNT"), 
    Span(doc11, 13, 14, label="ARTICLE"), 
    Span(doc11, 14, 15, label="PRICE"), 
    Span(doc11, 15, 16, label="UNIT"), 
    Span(doc11, 17, 18, label="SUM"), 
    Span(doc11, 47, 48, label="TARIFF"), 
    Span(doc11, 53, 54, label="COUNTRY")] 
docs.append(doc11)


doc12 = nlp('''Purchase order number: N SR-1-06 1426
2900 12 РС 6010000239 (*) 715,29 100 PC 85,83

FI-RVZ-15LR-WD-B-W3-1

packed per each item

Product description: valve

Export - Customs tariff no.: 84813091
Country of origin: Germany''')
#doc12SR-1-06 1426 2900 12 6010000239 715,29 100  84813091 Germany
print("doc12",doc12[5: 8], doc12[8: 9], doc12[10: 11], doc12[11: 12], doc12[13: 14], doc12[17:18], doc12[18:19] ,doc12[20:21], doc12[51: 52], doc12[57: 58]) 
doc12.ents = [Span(doc12, 5, 8, label="CONTRACT"), 
    Span(doc12, 8, 9, label="CONTRACT1"), 
    Span(doc12, 10, 11, label="POS"), 
    Span(doc12, 11, 12, label="AMOUNT"), 
    Span(doc12, 13, 14, label="ARTICLE"), 
    Span(doc12, 17, 18, label="PRICE"), 
    Span(doc12, 18, 19, label="UNIT"), 
    Span(doc12, 20, 21, label="SUM"), 
    Span(doc12, 51, 52, label="TARIFF"), 
    Span(doc12, 57, 58, label="COUNTRY")] 
docs.append(doc12)


doc13 = nlp('''Purchase order number: N SR-1-06 1448
3000 40 РС 6010003710 (*) 393,09 100 PC 157,24

FI-ELD-1 5L-V-W3-DKO
FI-ELD-15L-B-W3-DKO

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc13SR-1-06 1448 3000 40 6010003710 393,09 100  73079910 Germany
print("doc13",doc13[5: 8], doc13[8: 9], doc13[10: 11], doc13[11: 12], doc13[13: 14], doc13[17:18], doc13[18:19] ,doc13[20:21], doc13[60: 61], doc13[66: 67]) 
doc13.ents = [Span(doc13, 5, 8, label="CONTRACT"), 
    Span(doc13, 8, 9, label="CONTRACT1"), 
    Span(doc13, 10, 11, label="POS"), 
    Span(doc13, 11, 12, label="AMOUNT"), 
    Span(doc13, 13, 14, label="ARTICLE"), 
    Span(doc13, 17, 18, label="PRICE"), 
    Span(doc13, 18, 19, label="UNIT"), 
    Span(doc13, 20, 21, label="SUM"), 
    Span(doc13, 60, 61, label="TARIFF"), 
    Span(doc13, 66, 67, label="COUNTRY")] 
docs.append(doc13)


doc14 = nlp('''Purchase order number: N SR-1-06 1457
3100 1 РС 6100068507 61,88 1 РС 61,88


Description

QRC-FH-19-M-G16-VT-W5
FH19-2-IGF16VA

packed per each item

Export - Customs tariff no.: 84812010
Country of origin: Germany''')
#doc14SR-1-06 1457 3100 1 6100068507 61,88 1  84812010 Germany
print("doc14",doc14[5: 8], doc14[8: 9], doc14[10: 11], doc14[11: 12], doc14[13: 14], doc14[14:15], doc14[15:16] ,doc14[17:18], doc14[51: 52], doc14[57: 58]) 
doc14.ents = [Span(doc14, 5, 8, label="CONTRACT"), 
    Span(doc14, 8, 9, label="CONTRACT1"), 
    Span(doc14, 10, 11, label="POS"), 
    Span(doc14, 11, 12, label="AMOUNT"), 
    Span(doc14, 13, 14, label="ARTICLE"), 
    Span(doc14, 14, 15, label="PRICE"), 
    Span(doc14, 15, 16, label="UNIT"), 
    Span(doc14, 17, 18, label="SUM"), 
    Span(doc14, 51, 52, label="TARIFF"), 
    Span(doc14, 57, 58, label="COUNTRY")] 
docs.append(doc14)


doc15 = nlp('''Purchase order number: N SR-1-06 1546
3200 10 PC 1910000098 (*) 20,13 1 РС 201,30

SNA-127-B-S-T1C-12

SNA 127 B-S-T1C-12

packed per each item

Product description: level gauge
Export - Customs tariff no.: 90261089
Country of origin: Germany''')
#doc15SR-1-06 1546 3200 10 1910000098 20,13 1  90261089 Germany
print("doc15",doc15[5: 8], doc15[8: 9], doc15[10: 11], doc15[11: 12], doc15[13: 14], doc15[17:18], doc15[18:19] ,doc15[20:21], doc15[56: 57], doc15[62: 63]) 
doc15.ents = [Span(doc15, 5, 8, label="CONTRACT"), 
    Span(doc15, 8, 9, label="CONTRACT1"), 
    Span(doc15, 10, 11, label="POS"), 
    Span(doc15, 11, 12, label="AMOUNT"), 
    Span(doc15, 13, 14, label="ARTICLE"), 
    Span(doc15, 17, 18, label="PRICE"), 
    Span(doc15, 18, 19, label="UNIT"), 
    Span(doc15, 20, 21, label="SUM"), 
    Span(doc15, 56, 57, label="TARIFF"), 
    Span(doc15, 62, 63, label="COUNTRY")] 
docs.append(doc15)


doc16 = nlp('''Purchase order number: N SR-1-06 1547
3300 3 PC 1020013837 60,28 1 РС 180,84
SF-6702-MG
SF6702-MG

packed per each item

Product description: filter element
Export - Customs tariff по.: 84212980
Country of origin: USA''')
#doc16SR-1-06 1547 3300 3 1020013837 60,28 1  84212980 USA
print("doc16",doc16[5: 8], doc16[8: 9], doc16[10: 11], doc16[11: 12], doc16[13: 14], doc16[14:15], doc16[15:16] ,doc16[17:18], doc16[45: 46], doc16[51: 52]) 
doc16.ents = [Span(doc16, 5, 8, label="CONTRACT"), 
    Span(doc16, 8, 9, label="CONTRACT1"), 
    Span(doc16, 10, 11, label="POS"), 
    Span(doc16, 11, 12, label="AMOUNT"), 
    Span(doc16, 13, 14, label="ARTICLE"), 
    Span(doc16, 14, 15, label="PRICE"), 
    Span(doc16, 15, 16, label="UNIT"), 
    Span(doc16, 17, 18, label="SUM"), 
    Span(doc16, 45, 46, label="TARIFF"), 
    Span(doc16, 51, 52, label="COUNTRY")] 
docs.append(doc16)



doc18 = nlp('''Purchase order number: N SR-1-06 1622
3500 11 РС 1010002404 25,79 1 РС 283,69

ВРЕВ-022-О-О-В-С16-О-С16-110
RFBO22...B/B/O/G/L10

packed per each item

Product description: filter housing
Export - Customs tariff по.: 84212980
Country of origin: China''')
#doc18SR-1-06 1622 3500 11 1010002404 25,79 1  84212980 China
print("doc18",doc18[5: 8], doc18[8: 9], doc18[10: 11], doc18[11: 12], doc18[13: 14], doc18[14:15], doc18[15:16] ,doc18[17:18], doc18[65: 66], doc18[71: 72]) 
doc18.ents = [Span(doc18, 5, 8, label="CONTRACT"), 
    Span(doc18, 8, 9, label="CONTRACT1"), 
    Span(doc18, 10, 11, label="POS"), 
    Span(doc18, 11, 12, label="AMOUNT"), 
    Span(doc18, 13, 14, label="ARTICLE"), 
    Span(doc18, 14, 15, label="PRICE"), 
    Span(doc18, 15, 16, label="UNIT"), 
    Span(doc18, 17, 18, label="SUM"), 
    Span(doc18, 65, 66, label="TARIFF"), 
    Span(doc18, 71, 72, label="COUNTRY")] 
docs.append(doc18)


doc19 = nlp('''Purchase order number: N SR-1-06 1650
3600 300 PC 6100076765 (*) 3,85 1 РС 1.155,00

ОКС-НР-12-Е-М201К-В-М/З
HP10-1-X0041N

packed per each item

Customer ID-No.: 6100076765
Product description: coupling

Export - Customs tariff no.: 84812010
Country of origin: Germany''')
#doc19SR-1-06 1650 3600 300 6100076765 3,85 1  84812010 Germany
print("doc19",doc19[5: 8], doc19[8: 9], doc19[10: 11], doc19[11: 12], doc19[13: 14], doc19[17:18], doc19[18:19] ,doc19[20:21], doc19[67: 68], doc19[73: 74]) 
doc19.ents = [Span(doc19, 5, 8, label="CONTRACT"), 
    Span(doc19, 8, 9, label="CONTRACT1"), 
    Span(doc19, 10, 11, label="POS"), 
    Span(doc19, 11, 12, label="AMOUNT"), 
    Span(doc19, 13, 14, label="ARTICLE"), 
    Span(doc19, 17, 18, label="PRICE"), 
    Span(doc19, 18, 19, label="UNIT"), 
    Span(doc19, 20, 21, label="SUM"), 
    Span(doc19, 67, 68, label="TARIFF"), 
    Span(doc19, 73, 74, label="COUNTRY")] 
docs.append(doc19)


doc20 = nlp('''Purchase order number: N SR-1-06 1651
3700 1.000 PC 6100076765 (*) 3,85 1 РС 3.850,00

ОКС-НР-12-Е-М201К-В-М/З
HP10-1-X0041N

packed per each item

Customer ID-No.: 6100076765
Product description: coupling

Export - Customs tariff no.: 84812010
Country of origin: Germany''')
#doc20SR-1-06 1651 3700 1.000 6100076765 3,85 1  84812010 Germany
print("doc20",doc20[5: 8], doc20[8: 9], doc20[10: 11], doc20[11: 12], doc20[13: 14], doc20[17:18], doc20[18:19] ,doc20[20:21], doc20[67: 68], doc20[73: 74]) 
doc20.ents = [Span(doc20, 5, 8, label="CONTRACT"), 
    Span(doc20, 8, 9, label="CONTRACT1"), 
    Span(doc20, 10, 11, label="POS"), 
    Span(doc20, 11, 12, label="AMOUNT"), 
    Span(doc20, 13, 14, label="ARTICLE"), 
    Span(doc20, 17, 18, label="PRICE"), 
    Span(doc20, 18, 19, label="UNIT"), 
    Span(doc20, 20, 21, label="SUM"), 
    Span(doc20, 67, 68, label="TARIFF"), 
    Span(doc20, 73, 74, label="COUNTRY")] 
docs.append(doc20)


doc21 = nlp('''Purchase order number: N SR-1-06 1693
3800 100 PC 1120001249 35,37 100 PC 35,37
SPV-2-M-W3
SPV 2 М МЗ
packed per each item
Product description: weld plate
Export - Customs tariff no.: 73269098
Country of origin: Germany''')
#doc21SR-1-06 1693 3800 100 1120001249 35,37 100  73269098 Germany
print("doc21",doc21[5: 8], doc21[8: 9], doc21[10: 11], doc21[11: 12], doc21[13: 14], doc21[14:15], doc21[15:16] ,doc21[17:18], doc21[48: 49], doc21[54: 55]) 
doc21.ents = [Span(doc21, 5, 8, label="CONTRACT"), 
    Span(doc21, 8, 9, label="CONTRACT1"), 
    Span(doc21, 10, 11, label="POS"), 
    Span(doc21, 11, 12, label="AMOUNT"), 
    Span(doc21, 13, 14, label="ARTICLE"), 
    Span(doc21, 14, 15, label="PRICE"), 
    Span(doc21, 15, 16, label="UNIT"), 
    Span(doc21, 17, 18, label="SUM"), 
    Span(doc21, 48, 49, label="TARIFF"), 
    Span(doc21, 54, 55, label="COUNTRY")] 
docs.append(doc21)


doc22 = nlp('''Purchase order number: N SR-1-06 1712
3900 20 РС 6010001039 (*) 2.430,90 100 PC 486,18

FI-T-20/10/20S-W3-MS

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc22SR-1-06 1712 3900 20 6010001039 2.430,90 100  73079910 Germany
print("doc22",doc22[5: 8], doc22[8: 9], doc22[10: 11], doc22[11: 12], doc22[13: 14], doc22[17:18], doc22[18:19] ,doc22[20:21], doc22[47: 48], doc22[53: 54]) 
doc22.ents = [Span(doc22, 5, 8, label="CONTRACT"), 
    Span(doc22, 8, 9, label="CONTRACT1"), 
    Span(doc22, 10, 11, label="POS"), 
    Span(doc22, 11, 12, label="AMOUNT"), 
    Span(doc22, 13, 14, label="ARTICLE"), 
    Span(doc22, 17, 18, label="PRICE"), 
    Span(doc22, 18, 19, label="UNIT"), 
    Span(doc22, 20, 21, label="SUM"), 
    Span(doc22, 47, 48, label="TARIFF"), 
    Span(doc22, 53, 54, label="COUNTRY")] 
docs.append(doc22)


doc23 = nlp('''Purchase order number: N SR-1-06 1726
4000 50 РС 1120001175 39,46 100 РС 19,73
SP-6-M-W2
SP 6 М W2
packed per each item
Product description: weld plate
Export - Customs tariff no.: 73269098
Country of origin: Germany''')
#doc23SR-1-06 1726 4000 50 1120001175 39,46 100  73269098 Germany
print("doc23",doc23[5: 8], doc23[8: 9], doc23[10: 11], doc23[11: 12], doc23[13: 14], doc23[14:15], doc23[15:16] ,doc23[17:18], doc23[48: 49], doc23[54: 55]) 
doc23.ents = [Span(doc23, 5, 8, label="CONTRACT"), 
    Span(doc23, 8, 9, label="CONTRACT1"), 
    Span(doc23, 10, 11, label="POS"), 
    Span(doc23, 11, 12, label="AMOUNT"), 
    Span(doc23, 13, 14, label="ARTICLE"), 
    Span(doc23, 14, 15, label="PRICE"), 
    Span(doc23, 15, 16, label="UNIT"), 
    Span(doc23, 17, 18, label="SUM"), 
    Span(doc23, 48, 49, label="TARIFF"), 
    Span(doc23, 54, 55, label="COUNTRY")] 
docs.append(doc23)


doc24 = nlp('''Purchase order number: N SR-1-06 1737
4100 50 РС 6100069512 (*) 12,60 1 РС 630,00

QRC-HS-25-M-28L-B-W66
HS20-2-L2836

packed per each item

Product description: coupling

Export - Customs tariff no.: 84812010
Country of origin: Germany''')
#doc24SR-1-06 1737 4100 50 6100069512 12,60 1  84812010 Germany
print("doc24",doc24[5: 8], doc24[8: 9], doc24[10: 11], doc24[11: 12], doc24[13: 14], doc24[17:18], doc24[18:19] ,doc24[20:21], doc24[55: 56], doc24[61: 62]) 
doc24.ents = [Span(doc24, 5, 8, label="CONTRACT"), 
    Span(doc24, 8, 9, label="CONTRACT1"), 
    Span(doc24, 10, 11, label="POS"), 
    Span(doc24, 11, 12, label="AMOUNT"), 
    Span(doc24, 13, 14, label="ARTICLE"), 
    Span(doc24, 17, 18, label="PRICE"), 
    Span(doc24, 18, 19, label="UNIT"), 
    Span(doc24, 20, 21, label="SUM"), 
    Span(doc24, 55, 56, label="TARIFF"), 
    Span(doc24, 61, 62, label="COUNTRY")] 
docs.append(doc24)


doc25 = nlp('''Purchase order number: N SR-1-06 1743
4200 100 PC 1910003377 (*) 61,63 1 РС 6.163,00

SNK-305-V-C-T1C-12

SNK 305 V-C-T1C-12

packed per each item

Product description: level gauge
Export - Customs tariff no.: 90261089
Country of origin: Germany''')
#doc25SR-1-06 1743 4200 100 1910003377 61,63 1  90261089 Germany
print("doc25",doc25[5: 8], doc25[8: 9], doc25[10: 11], doc25[11: 12], doc25[13: 14], doc25[17:18], doc25[18:19] ,doc25[20:21], doc25[56: 57], doc25[62: 63]) 
doc25.ents = [Span(doc25, 5, 8, label="CONTRACT"), 
    Span(doc25, 8, 9, label="CONTRACT1"), 
    Span(doc25, 10, 11, label="POS"), 
    Span(doc25, 11, 12, label="AMOUNT"), 
    Span(doc25, 13, 14, label="ARTICLE"), 
    Span(doc25, 17, 18, label="PRICE"), 
    Span(doc25, 18, 19, label="UNIT"), 
    Span(doc25, 20, 21, label="SUM"), 
    Span(doc25, 56, 57, label="TARIFF"), 
    Span(doc25, 62, 63, label="COUNTRY")] 
docs.append(doc25)


doc26 = nlp('''Purchase order number: N SR-1-06 1753
4300 6 РС 1020022269 169,52 1 РС 1.017,12

NR-1000-E-03-B/4

NR-1000E03B/4

packed per each item

Product description: filter element
Export - Customs tariff no.: 84219990
Country of origin: Germany''')
#doc26SR-1-06 1753 4300 6 1020022269 169,52 1  84219990 Germany
print("doc26",doc26[5: 8], doc26[8: 9], doc26[10: 11], doc26[11: 12], doc26[13: 14], doc26[14:15], doc26[15:16] ,doc26[17:18], doc26[45: 46], doc26[51: 52]) 
doc26.ents = [Span(doc26, 5, 8, label="CONTRACT"), 
    Span(doc26, 8, 9, label="CONTRACT1"), 
    Span(doc26, 10, 11, label="POS"), 
    Span(doc26, 11, 12, label="AMOUNT"), 
    Span(doc26, 13, 14, label="ARTICLE"), 
    Span(doc26, 14, 15, label="PRICE"), 
    Span(doc26, 15, 16, label="UNIT"), 
    Span(doc26, 17, 18, label="SUM"), 
    Span(doc26, 45, 46, label="TARIFF"), 
    Span(doc26, 51, 52, label="COUNTRY")] 
docs.append(doc26)


doc27 = nlp('''Purchase order number: N SR-1-06 1761
4400 1 РС 1910000612 270,31 1 РС 270,31

SDM-750-A-120-T

SDM 750-A-120-T

Flow Indicator

packed per each item

Product description: flowmeter

Export - Customs tariff no.: 90261081
Country of origin: Great''')
#doc27SR-1-06 1761 4400 1 1910000612 270,31 1  90261081 Great
print("doc27",doc27[5: 8], doc27[8: 9], doc27[10: 11], doc27[11: 12], doc27[13: 14], doc27[14:15], doc27[15:16] ,doc27[17:18], doc27[52: 53], doc27[58: 59]) 
doc27.ents = [Span(doc27, 5, 8, label="CONTRACT"), 
    Span(doc27, 8, 9, label="CONTRACT1"), 
    Span(doc27, 10, 11, label="POS"), 
    Span(doc27, 11, 12, label="AMOUNT"), 
    Span(doc27, 13, 14, label="ARTICLE"), 
    Span(doc27, 14, 15, label="PRICE"), 
    Span(doc27, 15, 16, label="UNIT"), 
    Span(doc27, 17, 18, label="SUM"), 
    Span(doc27, 52, 53, label="TARIFF"), 
    Span(doc27, 58, 59, label="COUNTRY")] 
docs.append(doc27)


doc28 = nlp('''Purchase order number: N SR-1-06 1763
4500 5 PC 1020003767 26,42 1 РС 132,10
RE-070-N-20-B/2
RE-070N20B/2

packed per each item

Product description: filter element
Export - Customs tariff no.: 84219990
Country of origin: Germany''')
#doc28SR-1-06 1763 4500 5 1020003767 26,42 1  84219990 Germany
print("doc28",doc28[5: 8], doc28[8: 9], doc28[10: 11], doc28[11: 12], doc28[13: 14], doc28[14:15], doc28[15:16] ,doc28[17:18], doc28[45: 46], doc28[51: 52]) 
doc28.ents = [Span(doc28, 5, 8, label="CONTRACT"), 
    Span(doc28, 8, 9, label="CONTRACT1"), 
    Span(doc28, 10, 11, label="POS"), 
    Span(doc28, 11, 12, label="AMOUNT"), 
    Span(doc28, 13, 14, label="ARTICLE"), 
    Span(doc28, 14, 15, label="PRICE"), 
    Span(doc28, 15, 16, label="UNIT"), 
    Span(doc28, 17, 18, label="SUM"), 
    Span(doc28, 45, 46, label="TARIFF"), 
    Span(doc28, 51, 52, label="COUNTRY")] 
docs.append(doc28)


doc29 = nlp('''Purchase order number: N SR-1-06 1754
4600 10 PC 1210005780 56,10 1 РС 561,00

SMK-20-22L-B-G-W5-MS
SMK20-22L-PG-V4A

packed per each item

Product description: coupling

Export - Customs tariff no.: 84812010
Country of origin: Germany''')
#doc29SR-1-06 1754 4600 10 1210005780 56,10 1  84812010 Germany
print("doc29",doc29[5: 8], doc29[8: 9], doc29[10: 11], doc29[11: 12], doc29[13: 14], doc29[14:15], doc29[15:16] ,doc29[17:18], doc29[56: 57], doc29[62: 63]) 
doc29.ents = [Span(doc29, 5, 8, label="CONTRACT"), 
    Span(doc29, 8, 9, label="CONTRACT1"), 
    Span(doc29, 10, 11, label="POS"), 
    Span(doc29, 11, 12, label="AMOUNT"), 
    Span(doc29, 13, 14, label="ARTICLE"), 
    Span(doc29, 14, 15, label="PRICE"), 
    Span(doc29, 15, 16, label="UNIT"), 
    Span(doc29, 17, 18, label="SUM"), 
    Span(doc29, 56, 57, label="TARIFF"), 
    Span(doc29, 62, 63, label="COUNTRY")] 
docs.append(doc29)


doc30 = nlp('''Purchase order number: N SR-1-06 1773
4700 80 РС 1130002876 103,32 100 РС 82,66
DPAL-6S-W3
DPAL 6 S W3

packed per each item

Product description: cover plate

Export - Customs tariff no.: 73182900
Country of origin: Germany''')
#doc30SR-1-06 1773 4700 80 1130002876 103,32 100  73182900 Germany
print("doc30",doc30[5: 8], doc30[8: 9], doc30[10: 11], doc30[11: 12], doc30[13: 14], doc30[14:15], doc30[15:16] ,doc30[17:18], doc30[46: 47], doc30[52: 53]) 
doc30.ents = [Span(doc30, 5, 8, label="CONTRACT"), 
    Span(doc30, 8, 9, label="CONTRACT1"), 
    Span(doc30, 10, 11, label="POS"), 
    Span(doc30, 11, 12, label="AMOUNT"), 
    Span(doc30, 13, 14, label="ARTICLE"), 
    Span(doc30, 14, 15, label="PRICE"), 
    Span(doc30, 15, 16, label="UNIT"), 
    Span(doc30, 17, 18, label="SUM"), 
    Span(doc30, 46, 47, label="TARIFF"), 
    Span(doc30, 52, 53, label="COUNTRY")] 
docs.append(doc30)


doc31 = nlp('''Purchase order number: N SR-1-06 1774
4800 160 PC 1130002876 103,32 100 PC 165,31
DPAL-6S-W3
DPAL 6 S W3

packed per each item

Product description: cover plate

Export - Customs tariff no.: 73182900
Country of origin: Germany''')
#doc31SR-1-06 1774 4800 160 1130002876 103,32 100  73182900 Germany
print("doc31",doc31[5: 8], doc31[8: 9], doc31[10: 11], doc31[11: 12], doc31[13: 14], doc31[14:15], doc31[15:16] ,doc31[17:18], doc31[46: 47], doc31[52: 53]) 
doc31.ents = [Span(doc31, 5, 8, label="CONTRACT"), 
    Span(doc31, 8, 9, label="CONTRACT1"), 
    Span(doc31, 10, 11, label="POS"), 
    Span(doc31, 11, 12, label="AMOUNT"), 
    Span(doc31, 13, 14, label="ARTICLE"), 
    Span(doc31, 14, 15, label="PRICE"), 
    Span(doc31, 15, 16, label="UNIT"), 
    Span(doc31, 17, 18, label="SUM"), 
    Span(doc31, 46, 47, label="TARIFF"), 
    Span(doc31, 52, 53, label="COUNTRY")] 
docs.append(doc31)


doc32 = nlp('''Purchase order number: N SR-1-06 1779

4900 4 РС 1020023743 (*) 418,34 1 РС 1.673,36
SE-300-H-10-B/4
SE-300H10B/4

packed per each item

Product description: filter element
Export - Customs tariff no.: 84219990
Country of origin: Germany''')
#doc32SR-1-06 1779 4900 4 1020023743 418,34 1  84219990 Germany
print("doc32",doc32[5: 8], doc32[8: 9], doc32[10: 11], doc32[11: 12], doc32[13: 14], doc32[17:18], doc32[18:19] ,doc32[20:21], doc32[48: 49], doc32[54: 55]) 
doc32.ents = [Span(doc32, 5, 8, label="CONTRACT"), 
    Span(doc32, 8, 9, label="CONTRACT1"), 
    Span(doc32, 10, 11, label="POS"), 
    Span(doc32, 11, 12, label="AMOUNT"), 
    Span(doc32, 13, 14, label="ARTICLE"), 
    Span(doc32, 17, 18, label="PRICE"), 
    Span(doc32, 18, 19, label="UNIT"), 
    Span(doc32, 20, 21, label="SUM"), 
    Span(doc32, 48, 49, label="TARIFF"), 
    Span(doc32, 54, 55, label="COUNTRY")] 
docs.append(doc32)


doc33 = nlp('''Purchase order number: N SR-1-06 1783
5000 2 РС 6010001229 (*) 772,99 100 PC 15,46

FI-GA-12LR1/4-W3-MS

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc33SR-1-06 1783 5000 2 6010001229 772,99 100  73079910 Germany
print("doc33",doc33[5: 8], doc33[8: 9], doc33[10: 11], doc33[11: 12], doc33[13: 14], doc33[17:18], doc33[18:19] ,doc33[20:21], doc33[47: 48], doc33[53: 54]) 
doc33.ents = [Span(doc33, 5, 8, label="CONTRACT"), 
    Span(doc33, 8, 9, label="CONTRACT1"), 
    Span(doc33, 10, 11, label="POS"), 
    Span(doc33, 11, 12, label="AMOUNT"), 
    Span(doc33, 13, 14, label="ARTICLE"), 
    Span(doc33, 17, 18, label="PRICE"), 
    Span(doc33, 18, 19, label="UNIT"), 
    Span(doc33, 20, 21, label="SUM"), 
    Span(doc33, 47, 48, label="TARIFF"), 
    Span(doc33, 53, 54, label="COUNTRY")] 
docs.append(doc33)


doc34 = nlp('''Purchase order number: N SR-1-06 1783
5100 4 РС 6010007862 (*) 257,85 100 PC 10,31

FI-WAS-12L-W159-MS

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079319
Country of origin: Germany''')
#doc34SR-1-06 1783 5100 4 6010007862 257,85 100  73079319 Germany
print("doc34",doc34[5: 8], doc34[8: 9], doc34[10: 11], doc34[11: 12], doc34[13: 14], doc34[17:18], doc34[18:19] ,doc34[20:21], doc34[47: 48], doc34[53: 54]) 
doc34.ents = [Span(doc34, 5, 8, label="CONTRACT"), 
    Span(doc34, 8, 9, label="CONTRACT1"), 
    Span(doc34, 10, 11, label="POS"), 
    Span(doc34, 11, 12, label="AMOUNT"), 
    Span(doc34, 13, 14, label="ARTICLE"), 
    Span(doc34, 17, 18, label="PRICE"), 
    Span(doc34, 18, 19, label="UNIT"), 
    Span(doc34, 20, 21, label="SUM"), 
    Span(doc34, 47, 48, label="TARIFF"), 
    Span(doc34, 53, 54, label="COUNTRY")] 
docs.append(doc34)


doc35 = nlp('''Purchase order number: N SR-1-06 1783
5200 4 РС 6010008214 (*) 416,80 100 PC 16,67

FI-WEE-12LR-OK-B-W3-MS

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079290
Country of origin: Germany''')
#doc35SR-1-06 1783 5200 4 6010008214 416,80 100  73079290 Germany
print("doc35",doc35[5: 8], doc35[8: 9], doc35[10: 11], doc35[11: 12], doc35[13: 14], doc35[17:18], doc35[18:19] ,doc35[20:21], doc35[51: 52], doc35[57: 58]) 
doc35.ents = [Span(doc35, 5, 8, label="CONTRACT"), 
    Span(doc35, 8, 9, label="CONTRACT1"), 
    Span(doc35, 10, 11, label="POS"), 
    Span(doc35, 11, 12, label="AMOUNT"), 
    Span(doc35, 13, 14, label="ARTICLE"), 
    Span(doc35, 17, 18, label="PRICE"), 
    Span(doc35, 18, 19, label="UNIT"), 
    Span(doc35, 20, 21, label="SUM"), 
    Span(doc35, 51, 52, label="TARIFF"), 
    Span(doc35, 57, 58, label="COUNTRY")] 
docs.append(doc35)


doc36 = nlp('''Purchase order number: N SR-1-06 1808
5300 40 РС 1210026041 (*) 4,72 1 РС 188,80

SMK-20-12L-B-K-W3
SMK20-12L-PK-C6F

packed per each item

Product description: coupling

Export - Customs tariff no.: 84812010
Country of origin: Germany''')
#doc36SR-1-06 1808 5300 40 1210026041 4,72 1  84812010 Germany
print("doc36",doc36[5: 8], doc36[8: 9], doc36[10: 11], doc36[11: 12], doc36[13: 14], doc36[17:18], doc36[18:19] ,doc36[20:21], doc36[57: 58], doc36[63: 64]) 
doc36.ents = [Span(doc36, 5, 8, label="CONTRACT"), 
    Span(doc36, 8, 9, label="CONTRACT1"), 
    Span(doc36, 10, 11, label="POS"), 
    Span(doc36, 11, 12, label="AMOUNT"), 
    Span(doc36, 13, 14, label="ARTICLE"), 
    Span(doc36, 17, 18, label="PRICE"), 
    Span(doc36, 18, 19, label="UNIT"), 
    Span(doc36, 20, 21, label="SUM"), 
    Span(doc36, 57, 58, label="TARIFF"), 
    Span(doc36, 63, 64, label="COUNTRY")] 
docs.append(doc36)


doc37 = nlp('''Purchase order number: N SR-1-06 1808
5400 50 РС 1210026116 (*) 4,51 1 РС 225,50

SMK-20-G1/4-B-C-W3
SMK20-G1/4-PC-C6F

packed per each item

Product description: coupling

Export - Customs tariff no.: 84812010
Country of origin: Germany''')
#doc37SR-1-06 1808 5400 50 1210026116 4,51 1  84812010 Germany
print("doc37",doc37[5: 8], doc37[8: 9], doc37[10: 11], doc37[11: 12], doc37[13: 14], doc37[17:18], doc37[18:19] ,doc37[20:21], doc37[57: 58], doc37[63: 64]) 
doc37.ents = [Span(doc37, 5, 8, label="CONTRACT"), 
    Span(doc37, 8, 9, label="CONTRACT1"), 
    Span(doc37, 10, 11, label="POS"), 
    Span(doc37, 11, 12, label="AMOUNT"), 
    Span(doc37, 13, 14, label="ARTICLE"), 
    Span(doc37, 17, 18, label="PRICE"), 
    Span(doc37, 18, 19, label="UNIT"), 
    Span(doc37, 20, 21, label="SUM"), 
    Span(doc37, 57, 58, label="TARIFF"), 
    Span(doc37, 63, 64, label="COUNTRY")] 
docs.append(doc37)


doc38 = nlp('''Purchase order number: N SR-1-06 1808
5500 50 PC 1020023990 42,38 1 РС 2.119,00

SN-045-E-20-B/4

SN-045E20B/4

packed per each item

Product description: filter element
Export - Customs tariff no.: 84219990
Country of origin: Germany''')
#doc38SR-1-06 1808 5500 50 1020023990 42,38 1  84219990 Germany
print("doc38",doc38[5: 8], doc38[8: 9], doc38[10: 11], doc38[11: 12], doc38[13: 14], doc38[14:15], doc38[15:16] ,doc38[17:18], doc38[45: 46], doc38[51: 52]) 
doc38.ents = [Span(doc38, 5, 8, label="CONTRACT"), 
    Span(doc38, 8, 9, label="CONTRACT1"), 
    Span(doc38, 10, 11, label="POS"), 
    Span(doc38, 11, 12, label="AMOUNT"), 
    Span(doc38, 13, 14, label="ARTICLE"), 
    Span(doc38, 14, 15, label="PRICE"), 
    Span(doc38, 15, 16, label="UNIT"), 
    Span(doc38, 17, 18, label="SUM"), 
    Span(doc38, 45, 46, label="TARIFF"), 
    Span(doc38, 51, 52, label="COUNTRY")] 
docs.append(doc38)


doc39 = nlp('''Purchase order number: N SR-1-06 1809
5600 40 РС 1130002876 103,32 100 РС 41,33
DPAL-6S-W3
DPAL 6 S W3
packed per each item
Product description: cover plate
Export - Customs tariff no.: 73182900
Country of origin: Germany''')
#doc39SR-1-06 1809 5600 40 1130002876 103,32 100  73182900 Germany
print("doc39",doc39[5: 8], doc39[8: 9], doc39[10: 11], doc39[11: 12], doc39[13: 14], doc39[14:15], doc39[15:16] ,doc39[17:18], doc39[46: 47], doc39[52: 53]) 
doc39.ents = [Span(doc39, 5, 8, label="CONTRACT"), 
    Span(doc39, 8, 9, label="CONTRACT1"), 
    Span(doc39, 10, 11, label="POS"), 
    Span(doc39, 11, 12, label="AMOUNT"), 
    Span(doc39, 13, 14, label="ARTICLE"), 
    Span(doc39, 14, 15, label="PRICE"), 
    Span(doc39, 15, 16, label="UNIT"), 
    Span(doc39, 17, 18, label="SUM"), 
    Span(doc39, 46, 47, label="TARIFF"), 
    Span(doc39, 52, 53, label="COUNTRY")] 
docs.append(doc39)


doc40 = nlp('''Purchase order number: N SR-1-06 1810
5700 20 РС 1130002876 103,32 100 РС 20,66
DPAL-6S-W3
DPAL 6 S W3

packed per each item

Product description: cover plate

Export - Customs tariff no.: 73182900
Country of origin: Germany''')
#doc40SR-1-06 1810 5700 20 1130002876 103,32 100  73182900 Germany
print("doc40",doc40[5: 8], doc40[8: 9], doc40[10: 11], doc40[11: 12], doc40[13: 14], doc40[14:15], doc40[15:16] ,doc40[17:18], doc40[46: 47], doc40[52: 53]) 
doc40.ents = [Span(doc40, 5, 8, label="CONTRACT"), 
    Span(doc40, 8, 9, label="CONTRACT1"), 
    Span(doc40, 10, 11, label="POS"), 
    Span(doc40, 11, 12, label="AMOUNT"), 
    Span(doc40, 13, 14, label="ARTICLE"), 
    Span(doc40, 14, 15, label="PRICE"), 
    Span(doc40, 15, 16, label="UNIT"), 
    Span(doc40, 17, 18, label="SUM"), 
    Span(doc40, 46, 47, label="TARIFF"), 
    Span(doc40, 52, 53, label="COUNTRY")] 
docs.append(doc40)


doc41 = nlp('''Purchase order number: N SR-1-06 1811
5800 20 РС 1130002876 103,32 100 РС 20,66
DPAL-6S-W3
DPAL 6 S W3

packed per each item

Product description: cover plate

Export - Customs tariff no.: 73182900
Country of origin: Germany''')
#doc41SR-1-06 1811 5800 20 1130002876 103,32 100  73182900 Germany
print("doc41",doc41[5: 8], doc41[8: 9], doc41[10: 11], doc41[11: 12], doc41[13: 14], doc41[14:15], doc41[15:16] ,doc41[17:18], doc41[46: 47], doc41[52: 53]) 
doc41.ents = [Span(doc41, 5, 8, label="CONTRACT"), 
    Span(doc41, 8, 9, label="CONTRACT1"), 
    Span(doc41, 10, 11, label="POS"), 
    Span(doc41, 11, 12, label="AMOUNT"), 
    Span(doc41, 13, 14, label="ARTICLE"), 
    Span(doc41, 14, 15, label="PRICE"), 
    Span(doc41, 15, 16, label="UNIT"), 
    Span(doc41, 17, 18, label="SUM"), 
    Span(doc41, 46, 47, label="TARIFF"), 
    Span(doc41, 52, 53, label="COUNTRY")] 
docs.append(doc41)


doc42 = nlp('''Purchase order number: N SR-1-06 1813
5900 80 PC 6020000495 (*) 122,25 100 PC 97,80

FI-GE-14SR-WD-B-W3

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc42SR-1-06 1813 5900 80 6020000495 122,25 100  73079910 Germany
print("doc42",doc42[5: 8], doc42[8: 9], doc42[10: 11], doc42[11: 12], doc42[13: 14], doc42[17:18], doc42[18:19] ,doc42[20:21], doc42[49: 50], doc42[55: 56]) 
doc42.ents = [Span(doc42, 5, 8, label="CONTRACT"), 
    Span(doc42, 8, 9, label="CONTRACT1"), 
    Span(doc42, 10, 11, label="POS"), 
    Span(doc42, 11, 12, label="AMOUNT"), 
    Span(doc42, 13, 14, label="ARTICLE"), 
    Span(doc42, 17, 18, label="PRICE"), 
    Span(doc42, 18, 19, label="UNIT"), 
    Span(doc42, 20, 21, label="SUM"), 
    Span(doc42, 49, 50, label="TARIFF"), 
    Span(doc42, 55, 56, label="COUNTRY")] 
docs.append(doc42)


doc43 = nlp('''Purchase order number: N SR-1-06 1814
6000 1 РС 1910000612 270,31 1 РС 270,31

SDM-750-A-120-T

SDM 750-A-120-T

Flow Indicator

packed per each item

Product description: flowmeter

Export - Customs tariff no.: 90261081
Country of origin: Great''')
#doc43SR-1-06 1814 6000 1 1910000612 270,31 1  90261081 Great
print("doc43",doc43[5: 8], doc43[8: 9], doc43[10: 11], doc43[11: 12], doc43[13: 14], doc43[14:15], doc43[15:16] ,doc43[17:18], doc43[52: 53], doc43[58: 59]) 
doc43.ents = [Span(doc43, 5, 8, label="CONTRACT"), 
    Span(doc43, 8, 9, label="CONTRACT1"), 
    Span(doc43, 10, 11, label="POS"), 
    Span(doc43, 11, 12, label="AMOUNT"), 
    Span(doc43, 13, 14, label="ARTICLE"), 
    Span(doc43, 14, 15, label="PRICE"), 
    Span(doc43, 15, 16, label="UNIT"), 
    Span(doc43, 17, 18, label="SUM"), 
    Span(doc43, 52, 53, label="TARIFF"), 
    Span(doc43, 58, 59, label="COUNTRY")] 
docs.append(doc43)


doc44 = nlp('''Purchase order number: N SR-1-06 1824
6100 2.800 PC 6030003814 15,60 100 PC 436,80
FI-M-12L-W3

packed per each item

Product description: nuts

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc44SR-1-06 1824 6100 2.800 6030003814 15,60 100  73079910 Germany
print("doc44",doc44[5: 8], doc44[8: 9], doc44[10: 11], doc44[11: 12], doc44[13: 14], doc44[14:15], doc44[15:16] ,doc44[17:18], doc44[42: 43], doc44[48: 49]) 
doc44.ents = [Span(doc44, 5, 8, label="CONTRACT"), 
    Span(doc44, 8, 9, label="CONTRACT1"), 
    Span(doc44, 10, 11, label="POS"), 
    Span(doc44, 11, 12, label="AMOUNT"), 
    Span(doc44, 13, 14, label="ARTICLE"), 
    Span(doc44, 14, 15, label="PRICE"), 
    Span(doc44, 15, 16, label="UNIT"), 
    Span(doc44, 17, 18, label="SUM"), 
    Span(doc44, 42, 43, label="TARIFF"), 
    Span(doc44, 48, 49, label="COUNTRY")] 
docs.append(doc44)


doc45 = nlp('''Purchase order number: N SR-1-06 1824
6200 1.600 PC 6010001858 (*) 58,36 100 PC 933,76

FI-VS-R3/8-WD-B-W3

packed per each item

Product description: Plug

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc45SR-1-06 1824 6200 1.600 6010001858 58,36 100  73079910 Germany
print("doc45",doc45[5: 8], doc45[8: 9], doc45[10: 11], doc45[11: 12], doc45[13: 14], doc45[17:18], doc45[18:19] ,doc45[20:21], doc45[51: 52], doc45[57: 58]) 
doc45.ents = [Span(doc45, 5, 8, label="CONTRACT"), 
    Span(doc45, 8, 9, label="CONTRACT1"), 
    Span(doc45, 10, 11, label="POS"), 
    Span(doc45, 11, 12, label="AMOUNT"), 
    Span(doc45, 13, 14, label="ARTICLE"), 
    Span(doc45, 17, 18, label="PRICE"), 
    Span(doc45, 18, 19, label="UNIT"), 
    Span(doc45, 20, 21, label="SUM"), 
    Span(doc45, 51, 52, label="TARIFF"), 
    Span(doc45, 57, 58, label="COUNTRY")] 
docs.append(doc45)


doc46 = nlp('''Purchase order number: N SR-1-06 1817
6300 100 РС 6030003827 71,45 100 PC 71,45
FI-M-20S-W3

packed per each item

Product description: nuts

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc46SR-1-06 1817 6300 100 6030003827 71,45 100  73079910 Germany
print("doc46",doc46[5: 8], doc46[8: 9], doc46[10: 11], doc46[11: 12], doc46[13: 14], doc46[14:15], doc46[15:16] ,doc46[17:18], doc46[42: 43], doc46[48: 49]) 
doc46.ents = [Span(doc46, 5, 8, label="CONTRACT"), 
    Span(doc46, 8, 9, label="CONTRACT1"), 
    Span(doc46, 10, 11, label="POS"), 
    Span(doc46, 11, 12, label="AMOUNT"), 
    Span(doc46, 13, 14, label="ARTICLE"), 
    Span(doc46, 14, 15, label="PRICE"), 
    Span(doc46, 15, 16, label="UNIT"), 
    Span(doc46, 17, 18, label="SUM"), 
    Span(doc46, 42, 43, label="TARIFF"), 
    Span(doc46, 48, 49, label="COUNTRY")] 
docs.append(doc46)


doc48 = nlp('''Purchase order number: N SR-1-06 1829
6500 2 РС 1020022269 169,52 1 РС 339,04

NR-1000-E-03-B/4

NR-1000E03B/4

packed per each item

Product description: filter element
Export - Customs tariff no.: 84219990
Country of origin: Germany''')
#doc48SR-1-06 1829 6500 2 1020022269 169,52 1  84219990 Germany
print("doc48",doc48[5: 8], doc48[8: 9], doc48[10: 11], doc48[11: 12], doc48[13: 14], doc48[14:15], doc48[15:16] ,doc48[17:18], doc48[45: 46], doc48[51: 52]) 
doc48.ents = [Span(doc48, 5, 8, label="CONTRACT"), 
    Span(doc48, 8, 9, label="CONTRACT1"), 
    Span(doc48, 10, 11, label="POS"), 
    Span(doc48, 11, 12, label="AMOUNT"), 
    Span(doc48, 13, 14, label="ARTICLE"), 
    Span(doc48, 14, 15, label="PRICE"), 
    Span(doc48, 15, 16, label="UNIT"), 
    Span(doc48, 17, 18, label="SUM"), 
    Span(doc48, 45, 46, label="TARIFF"), 
    Span(doc48, 51, 52, label="COUNTRY")] 
docs.append(doc48)


doc49 = nlp('''Purchase order number: N SR-1-06 1834
6600 42 РС 1130004238 483,62 100 РС 203,12
DPAL-9S-W2
DPAL 9 S W2
packed per each item
Product description: cover plate
Export - Customs tariff no.: 73182900
Country of origin: Germany''')
#doc49SR-1-06 1834 6600 42 1130004238 483,62 100  73182900 Germany
print("doc49",doc49[5: 8], doc49[8: 9], doc49[10: 11], doc49[11: 12], doc49[13: 14], doc49[14:15], doc49[15:16] ,doc49[17:18], doc49[46: 47], doc49[52: 53]) 
doc49.ents = [Span(doc49, 5, 8, label="CONTRACT"), 
    Span(doc49, 8, 9, label="CONTRACT1"), 
    Span(doc49, 10, 11, label="POS"), 
    Span(doc49, 11, 12, label="AMOUNT"), 
    Span(doc49, 13, 14, label="ARTICLE"), 
    Span(doc49, 14, 15, label="PRICE"), 
    Span(doc49, 15, 16, label="UNIT"), 
    Span(doc49, 17, 18, label="SUM"), 
    Span(doc49, 46, 47, label="TARIFF"), 
    Span(doc49, 52, 53, label="COUNTRY")] 
docs.append(doc49)


doc50 = nlp('''Purchase order number: N SR-1-06 1834
6700 26 РС 1120022879 1.016,68 100 PC 264,34

SPAL-9S-M-W2/2

SPAL 9 S M W2 /2

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 73269098
Country of origin: Germany''')
#doc50SR-1-06 1834 6700 26 1120022879 1.016,68 100  73269098 Germany
print("doc50",doc50[5: 8], doc50[8: 9], doc50[10: 11], doc50[11: 12], doc50[13: 14], doc50[14:15], doc50[15:16] ,doc50[17:18], doc50[50: 51], doc50[56: 57]) 
doc50.ents = [Span(doc50, 5, 8, label="CONTRACT"), 
    Span(doc50, 8, 9, label="CONTRACT1"), 
    Span(doc50, 10, 11, label="POS"), 
    Span(doc50, 11, 12, label="AMOUNT"), 
    Span(doc50, 13, 14, label="ARTICLE"), 
    Span(doc50, 14, 15, label="PRICE"), 
    Span(doc50, 15, 16, label="UNIT"), 
    Span(doc50, 17, 18, label="SUM"), 
    Span(doc50, 50, 51, label="TARIFF"), 
    Span(doc50, 56, 57, label="COUNTRY")] 
docs.append(doc50)


doc51 = nlp('''Purchase order number: N SR-1-06 1828
6800 2.040 PC 6030003817 63,90 100 PC 1.303,56
FI-M-22L-W3

packed per each item

Product description: nuts

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc51SR-1-06 1828 6800 2.040 6030003817 63,90 100  73079910 Germany
print("doc51",doc51[5: 8], doc51[8: 9], doc51[10: 11], doc51[11: 12], doc51[13: 14], doc51[14:15], doc51[15:16] ,doc51[17:18], doc51[42: 43], doc51[48: 49]) 
doc51.ents = [Span(doc51, 5, 8, label="CONTRACT"), 
    Span(doc51, 8, 9, label="CONTRACT1"), 
    Span(doc51, 10, 11, label="POS"), 
    Span(doc51, 11, 12, label="AMOUNT"), 
    Span(doc51, 13, 14, label="ARTICLE"), 
    Span(doc51, 14, 15, label="PRICE"), 
    Span(doc51, 15, 16, label="UNIT"), 
    Span(doc51, 17, 18, label="SUM"), 
    Span(doc51, 42, 43, label="TARIFF"), 
    Span(doc51, 48, 49, label="COUNTRY")] 
docs.append(doc51)


doc52 = nlp('''Purchase order number: N SR-1-06 1828
6900 1.900 PC 6030003818 122,25 100 PC 2.322,75
FI-M-28L-W3

packed per each item

Product description: nuts

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc52SR-1-06 1828 6900 1.900 6030003818 122,25 100  73079910 Germany
print("doc52",doc52[5: 8], doc52[8: 9], doc52[10: 11], doc52[11: 12], doc52[13: 14], doc52[14:15], doc52[15:16] ,doc52[17:18], doc52[42: 43], doc52[48: 49]) 
doc52.ents = [Span(doc52, 5, 8, label="CONTRACT"), 
    Span(doc52, 8, 9, label="CONTRACT1"), 
    Span(doc52, 10, 11, label="POS"), 
    Span(doc52, 11, 12, label="AMOUNT"), 
    Span(doc52, 13, 14, label="ARTICLE"), 
    Span(doc52, 14, 15, label="PRICE"), 
    Span(doc52, 15, 16, label="UNIT"), 
    Span(doc52, 17, 18, label="SUM"), 
    Span(doc52, 42, 43, label="TARIFF"), 
    Span(doc52, 48, 49, label="COUNTRY")] 
docs.append(doc52)


doc53 = nlp('''Purchase order number: N SR-1-06 1828
7000 2.000 PC 6030004273 (*) 25,66 100 PC 513,20


Description

FI-DS-22L-W3

packed per each item

Product description: ring

Export - Customs tariff no.: 73269098
Country of origin: Germany''')
#doc53SR-1-06 1828 7000 2.000 6030004273 25,66 100  73269098 Germany
print("doc53",doc53[5: 8], doc53[8: 9], doc53[10: 11], doc53[11: 12], doc53[13: 14], doc53[17:18], doc53[18:19] ,doc53[20:21], doc53[47: 48], doc53[53: 54]) 
doc53.ents = [Span(doc53, 5, 8, label="CONTRACT"), 
    Span(doc53, 8, 9, label="CONTRACT1"), 
    Span(doc53, 10, 11, label="POS"), 
    Span(doc53, 11, 12, label="AMOUNT"), 
    Span(doc53, 13, 14, label="ARTICLE"), 
    Span(doc53, 17, 18, label="PRICE"), 
    Span(doc53, 18, 19, label="UNIT"), 
    Span(doc53, 20, 21, label="SUM"), 
    Span(doc53, 47, 48, label="TARIFF"), 
    Span(doc53, 53, 54, label="COUNTRY")] 
docs.append(doc53)


doc54 = nlp('''Purchase order number: N SR-1-06 1828
7100 2.000 PC 6030004274 (*) 30,18 100 PC 603,60
FI-DS-28L-W3

packed per each item

Product description: ring

Export - Customs tariff no.: 73269098
Country of origin: Germany''')
#doc54SR-1-06 1828 7100 2.000 6030004274 30,18 100  73269098 Germany
print("doc54",doc54[5: 8], doc54[8: 9], doc54[10: 11], doc54[11: 12], doc54[13: 14], doc54[17:18], doc54[18:19] ,doc54[20:21], doc54[45: 46], doc54[51: 52]) 
doc54.ents = [Span(doc54, 5, 8, label="CONTRACT"), 
    Span(doc54, 8, 9, label="CONTRACT1"), 
    Span(doc54, 10, 11, label="POS"), 
    Span(doc54, 11, 12, label="AMOUNT"), 
    Span(doc54, 13, 14, label="ARTICLE"), 
    Span(doc54, 17, 18, label="PRICE"), 
    Span(doc54, 18, 19, label="UNIT"), 
    Span(doc54, 20, 21, label="SUM"), 
    Span(doc54, 45, 46, label="TARIFF"), 
    Span(doc54, 51, 52, label="COUNTRY")] 
docs.append(doc54)


doc55 = nlp('''Purchase order number: N SR-1-06 1830
7200 160 РС 1120003494 (*) 83,02 100 PC 132,83
AF-4S-M-W2

AF 4 S M W2 M10x40

packed per each item

Product description: screw

Export - Customs tariff по.: 73181588
Country of origin: Germany''')
#doc55SR-1-06 1830 7200 160 1120003494 83,02 100  73181588 Germany
print("doc55",doc55[5: 8], doc55[8: 9], doc55[10: 11], doc55[11: 12], doc55[13: 14], doc55[17:18], doc55[18:19] ,doc55[20:21], doc55[52: 53], doc55[58: 59]) 
doc55.ents = [Span(doc55, 5, 8, label="CONTRACT"), 
    Span(doc55, 8, 9, label="CONTRACT1"), 
    Span(doc55, 10, 11, label="POS"), 
    Span(doc55, 11, 12, label="AMOUNT"), 
    Span(doc55, 13, 14, label="ARTICLE"), 
    Span(doc55, 17, 18, label="PRICE"), 
    Span(doc55, 18, 19, label="UNIT"), 
    Span(doc55, 20, 21, label="SUM"), 
    Span(doc55, 52, 53, label="TARIFF"), 
    Span(doc55, 58, 59, label="COUNTRY")] 
docs.append(doc55)


doc56 = nlp('''Purchase order number: N SR-1-06 1830
7300 200 РС 1130004169 11,33 100 PC 22,66

AS-M10x45-DIN931/933-8.8-W3
AS-M10X45-DIN931/933-8.8-W3


Description

packed per each item

Product description: screw

Export - Customs tariff по.: 73181588
Country of origin: Croatia''')
#doc56SR-1-06 1830 7300 200 1130004169 11,33 100  73181588 Croatia
print("doc56",doc56[5: 8], doc56[8: 9], doc56[10: 11], doc56[11: 12], doc56[13: 14], doc56[14:15], doc56[15:16] ,doc56[17:18], doc56[58: 59], doc56[64: 65]) 
doc56.ents = [Span(doc56, 5, 8, label="CONTRACT"), 
    Span(doc56, 8, 9, label="CONTRACT1"), 
    Span(doc56, 10, 11, label="POS"), 
    Span(doc56, 11, 12, label="AMOUNT"), 
    Span(doc56, 13, 14, label="ARTICLE"), 
    Span(doc56, 14, 15, label="PRICE"), 
    Span(doc56, 15, 16, label="UNIT"), 
    Span(doc56, 17, 18, label="SUM"), 
    Span(doc56, 58, 59, label="TARIFF"), 
    Span(doc56, 64, 65, label="COUNTRY")] 
docs.append(doc56)


doc57 = nlp('''Purchase order number: N SR-1-06 1830
7400 180 РС 1130004170 13,10 100 РС 23,58

AS-M10x60-DIN931/933-8.8-W3
AS-M10X60-DIN931/933-8.8-W3
packed per each item

Product description: screw

Export - Customs tariff по.: 73181588
Country of origin: Origin''')
#doc57SR-1-06 1830 7400 180 1130004170 13,10 100  73181588 Origin
print("doc57",doc57[5: 8], doc57[8: 9], doc57[10: 11], doc57[11: 12], doc57[13: 14], doc57[14:15], doc57[15:16] ,doc57[17:18], doc57[56: 57], doc57[62: 63]) 
doc57.ents = [Span(doc57, 5, 8, label="CONTRACT"), 
    Span(doc57, 8, 9, label="CONTRACT1"), 
    Span(doc57, 10, 11, label="POS"), 
    Span(doc57, 11, 12, label="AMOUNT"), 
    Span(doc57, 13, 14, label="ARTICLE"), 
    Span(doc57, 14, 15, label="PRICE"), 
    Span(doc57, 15, 16, label="UNIT"), 
    Span(doc57, 17, 18, label="SUM"), 
    Span(doc57, 56, 57, label="TARIFF"), 
    Span(doc57, 62, 63, label="COUNTRY")] 
docs.append(doc57)


doc58 = nlp('''Purchase order number: N SR-1-06 1830
7500 80 РС 1130005435 83,97 100 РС 67,18
3008-РА
3008 РА

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc58SR-1-06 1830 7500 80 1130005435 83,97 100  39269097 Germany
print("doc58",doc58[5: 8], doc58[8: 9], doc58[10: 11], doc58[11: 12], doc58[13: 14], doc58[14:15], doc58[15:16] ,doc58[17:18], doc58[44: 45], doc58[50: 51]) 
doc58.ents = [Span(doc58, 5, 8, label="CONTRACT"), 
    Span(doc58, 8, 9, label="CONTRACT1"), 
    Span(doc58, 10, 11, label="POS"), 
    Span(doc58, 11, 12, label="AMOUNT"), 
    Span(doc58, 13, 14, label="ARTICLE"), 
    Span(doc58, 14, 15, label="PRICE"), 
    Span(doc58, 15, 16, label="UNIT"), 
    Span(doc58, 17, 18, label="SUM"), 
    Span(doc58, 44, 45, label="TARIFF"), 
    Span(doc58, 50, 51, label="COUNTRY")] 
docs.append(doc58)


doc59 = nlp('''Purchase order number: N SR-1-06 1830
7600 120 PC 1130005715 109,78 100 PC 131,74
4025-PA
4025 PA


Description

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc59SR-1-06 1830 7600 120 1130005715 109,78 100  39269097 Germany
print("doc59",doc59[5: 8], doc59[8: 9], doc59[10: 11], doc59[11: 12], doc59[13: 14], doc59[14:15], doc59[15:16] ,doc59[17:18], doc59[46: 47], doc59[52: 53]) 
doc59.ents = [Span(doc59, 5, 8, label="CONTRACT"), 
    Span(doc59, 8, 9, label="CONTRACT1"), 
    Span(doc59, 10, 11, label="POS"), 
    Span(doc59, 11, 12, label="AMOUNT"), 
    Span(doc59, 13, 14, label="ARTICLE"), 
    Span(doc59, 14, 15, label="PRICE"), 
    Span(doc59, 15, 16, label="UNIT"), 
    Span(doc59, 17, 18, label="SUM"), 
    Span(doc59, 46, 47, label="TARIFF"), 
    Span(doc59, 52, 53, label="COUNTRY")] 
docs.append(doc59)


doc60 = nlp('''Purchase order number: N SR-1-06 1830
7700 80 PC 1130002873 33,39 100 PC 26,71
DPAL-3S-W3
DPAL 3 S W3

packed per each item

Product description: cover plate

Export - Customs tariff no.: 73182900
Country of origin: Germany''')
#doc60SR-1-06 1830 7700 80 1130002873 33,39 100  73182900 Germany
print("doc60",doc60[5: 8], doc60[8: 9], doc60[10: 11], doc60[11: 12], doc60[13: 14], doc60[14:15], doc60[15:16] ,doc60[17:18], doc60[46: 47], doc60[52: 53]) 
doc60.ents = [Span(doc60, 5, 8, label="CONTRACT"), 
    Span(doc60, 8, 9, label="CONTRACT1"), 
    Span(doc60, 10, 11, label="POS"), 
    Span(doc60, 11, 12, label="AMOUNT"), 
    Span(doc60, 13, 14, label="ARTICLE"), 
    Span(doc60, 14, 15, label="PRICE"), 
    Span(doc60, 15, 16, label="UNIT"), 
    Span(doc60, 17, 18, label="SUM"), 
    Span(doc60, 46, 47, label="TARIFF"), 
    Span(doc60, 52, 53, label="COUNTRY")] 
docs.append(doc60)


doc61 = nlp('''Purchase order number: N SR-1-06 1830
7800 100 PC 1130000711 39,46 100 PC 39,46
DPAL-4S-W3
DPAL 4 S W3

packed per each item

Product description: cover plate

Export - Customs tariff no.: 73182900
Country of origin: Germany''')
#doc61SR-1-06 1830 7800 100 1130000711 39,46 100  73182900 Germany
print("doc61",doc61[5: 8], doc61[8: 9], doc61[10: 11], doc61[11: 12], doc61[13: 14], doc61[14:15], doc61[15:16] ,doc61[17:18], doc61[46: 47], doc61[52: 53]) 
doc61.ents = [Span(doc61, 5, 8, label="CONTRACT"), 
    Span(doc61, 8, 9, label="CONTRACT1"), 
    Span(doc61, 10, 11, label="POS"), 
    Span(doc61, 11, 12, label="AMOUNT"), 
    Span(doc61, 13, 14, label="ARTICLE"), 
    Span(doc61, 14, 15, label="PRICE"), 
    Span(doc61, 15, 16, label="UNIT"), 
    Span(doc61, 17, 18, label="SUM"), 
    Span(doc61, 46, 47, label="TARIFF"), 
    Span(doc61, 52, 53, label="COUNTRY")] 
docs.append(doc61)


doc62 = nlp('''Purchase order number: N SR-1-06 1830
7900 40 РС 1130000838 51,55 100 PC 20,62
SIP-4S-W2
ЯР 4 $ W2


Description

packed per each item

Product description: locking plate
Export - Customs tariff по.: 73182100
Country of origin: Germany''')
#doc62SR-1-06 1830 7900 40 1130000838 51,55 100  73182100 Germany
print("doc62",doc62[5: 8], doc62[8: 9], doc62[10: 11], doc62[11: 12], doc62[13: 14], doc62[14:15], doc62[15:16] ,doc62[17:18], doc62[48: 49], doc62[54: 55]) 
doc62.ents = [Span(doc62, 5, 8, label="CONTRACT"), 
    Span(doc62, 8, 9, label="CONTRACT1"), 
    Span(doc62, 10, 11, label="POS"), 
    Span(doc62, 11, 12, label="AMOUNT"), 
    Span(doc62, 13, 14, label="ARTICLE"), 
    Span(doc62, 14, 15, label="PRICE"), 
    Span(doc62, 15, 16, label="UNIT"), 
    Span(doc62, 17, 18, label="SUM"), 
    Span(doc62, 48, 49, label="TARIFF"), 
    Span(doc62, 54, 55, label="COUNTRY")] 
docs.append(doc62)


doc63 = nlp('''Purchase order number: N SR-1-06 1830
8000 80 РС 1120001947 66,80 100 РС 53,44
SPAL-3S-M-W2

SPAL 3 S M W2

packed per each item

Product description: weld plate

Export - Customs tariff no.: 73269098
Country of origin: Germany''')
#doc63SR-1-06 1830 8000 80 1120001947 66,80 100  73269098 Germany
print("doc63",doc63[5: 8], doc63[8: 9], doc63[10: 11], doc63[11: 12], doc63[13: 14], doc63[14:15], doc63[15:16] ,doc63[17:18], doc63[49: 50], doc63[55: 56]) 
doc63.ents = [Span(doc63, 5, 8, label="CONTRACT"), 
    Span(doc63, 8, 9, label="CONTRACT1"), 
    Span(doc63, 10, 11, label="POS"), 
    Span(doc63, 11, 12, label="AMOUNT"), 
    Span(doc63, 13, 14, label="ARTICLE"), 
    Span(doc63, 14, 15, label="PRICE"), 
    Span(doc63, 15, 16, label="UNIT"), 
    Span(doc63, 17, 18, label="SUM"), 
    Span(doc63, 49, 50, label="TARIFF"), 
    Span(doc63, 55, 56, label="COUNTRY")] 
docs.append(doc63)


doc64 = nlp('''Purchase order number: N SR-1-06 1830
8100 100 PC 1120001950 76,42 100 PC 76,42
SPAL-4S-M-W2

SPAL 4 S M W2

packed per each item

Product description: weld plate

Export - Customs tariff no.: 73269098
Country of origin: Germany''')
#doc64SR-1-06 1830 8100 100 1120001950 76,42 100  73269098 Germany
print("doc64",doc64[5: 8], doc64[8: 9], doc64[10: 11], doc64[11: 12], doc64[13: 14], doc64[14:15], doc64[15:16] ,doc64[17:18], doc64[49: 50], doc64[55: 56]) 
doc64.ents = [Span(doc64, 5, 8, label="CONTRACT"), 
    Span(doc64, 8, 9, label="CONTRACT1"), 
    Span(doc64, 10, 11, label="POS"), 
    Span(doc64, 11, 12, label="AMOUNT"), 
    Span(doc64, 13, 14, label="ARTICLE"), 
    Span(doc64, 14, 15, label="PRICE"), 
    Span(doc64, 15, 16, label="UNIT"), 
    Span(doc64, 17, 18, label="SUM"), 
    Span(doc64, 49, 50, label="TARIFF"), 
    Span(doc64, 55, 56, label="COUNTRY")] 
docs.append(doc64)


doc65 = nlp('''Purchase order number: N SR-1-06 1832
8200 50 РС 2012031333 (*) 1,42 1 РС 71,00

HCS-12-DKR-08-090-S-M-W3
11501N12129-DKR90-DN12-1/2#


Description

packed per each item
Export - Customs tariff no.: 73079290
Country of origin: Germany''')
#doc65SR-1-06 1832 8200 50 2012031333 1,42 1  73079290 Germany
print("doc65",doc65[5: 8], doc65[8: 9], doc65[10: 11], doc65[11: 12], doc65[13: 14], doc65[17:18], doc65[18:19] ,doc65[20:21], doc65[57: 58], doc65[63: 64]) 
doc65.ents = [Span(doc65, 5, 8, label="CONTRACT"), 
    Span(doc65, 8, 9, label="CONTRACT1"), 
    Span(doc65, 10, 11, label="POS"), 
    Span(doc65, 11, 12, label="AMOUNT"), 
    Span(doc65, 13, 14, label="ARTICLE"), 
    Span(doc65, 17, 18, label="PRICE"), 
    Span(doc65, 18, 19, label="UNIT"), 
    Span(doc65, 20, 21, label="SUM"), 
    Span(doc65, 57, 58, label="TARIFF"), 
    Span(doc65, 63, 64, label="COUNTRY")] 
docs.append(doc65)


doc66 = nlp('''Purchase order number: N SR-1-06 1836
8300 80 РС 6100109445 (*) 10,22 1 РС 817,60
QRC-FF-12-F-G12-BT-W3
FF12-1-IGF12

packed per each item

Product description: coupling

Export - Customs tariff no.: 84812010
Country of origin: Germany''')
#doc66SR-1-06 1836 8300 80 6100109445 10,22 1  84812010 Germany
print("doc66",doc66[5: 8], doc66[8: 9], doc66[10: 11], doc66[11: 12], doc66[13: 14], doc66[17:18], doc66[18:19] ,doc66[20:21], doc66[57: 58], doc66[63: 64]) 
doc66.ents = [Span(doc66, 5, 8, label="CONTRACT"), 
    Span(doc66, 8, 9, label="CONTRACT1"), 
    Span(doc66, 10, 11, label="POS"), 
    Span(doc66, 11, 12, label="AMOUNT"), 
    Span(doc66, 13, 14, label="ARTICLE"), 
    Span(doc66, 17, 18, label="PRICE"), 
    Span(doc66, 18, 19, label="UNIT"), 
    Span(doc66, 20, 21, label="SUM"), 
    Span(doc66, 57, 58, label="TARIFF"), 
    Span(doc66, 63, 64, label="COUNTRY")] 
docs.append(doc66)


doc67 = nlp('''Purchase order number: N SR-1-06 1836
8400 90 PC 6100074551 (*) 6,82 1 РС 613,80
QRC-FF-12-M-G12-BP-W3
FF12-2-IGF12
packed per each item
Product description: coupling
Export - Customs tariff no.: 84812010
Country of origin: Germany''')
#doc67SR-1-06 1836 8400 90 6100074551 6,82 1  84812010 Germany
print("doc67",doc67[5: 8], doc67[8: 9], doc67[10: 11], doc67[11: 12], doc67[13: 14], doc67[17:18], doc67[18:19] ,doc67[20:21], doc67[57: 58], doc67[63: 64]) 
doc67.ents = [Span(doc67, 5, 8, label="CONTRACT"), 
    Span(doc67, 8, 9, label="CONTRACT1"), 
    Span(doc67, 10, 11, label="POS"), 
    Span(doc67, 11, 12, label="AMOUNT"), 
    Span(doc67, 13, 14, label="ARTICLE"), 
    Span(doc67, 17, 18, label="PRICE"), 
    Span(doc67, 18, 19, label="UNIT"), 
    Span(doc67, 20, 21, label="SUM"), 
    Span(doc67, 57, 58, label="TARIFF"), 
    Span(doc67, 63, 64, label="COUNTRY")] 
docs.append(doc67)


doc68 = nlp('''Purchase order number: N SR-1-06 1837
8500 120 PC 6100109447 (*) 10,22 1 РС 1.226,40

QRC-FF-12-F-G08-BT-W3


Description

FF12-1-IGFO8

packed per each item

Product description: coupling

Export - Customs tariff no.: 84812010
Country of origin: Germany''')
#doc68SR-1-06 1837 8500 120 6100109447 10,22 1  84812010 Germany
print("doc68",doc68[5: 8], doc68[8: 9], doc68[10: 11], doc68[11: 12], doc68[13: 14], doc68[17:18], doc68[18:19] ,doc68[20:21], doc68[59: 60], doc68[65: 66]) 
doc68.ents = [Span(doc68, 5, 8, label="CONTRACT"), 
    Span(doc68, 8, 9, label="CONTRACT1"), 
    Span(doc68, 10, 11, label="POS"), 
    Span(doc68, 11, 12, label="AMOUNT"), 
    Span(doc68, 13, 14, label="ARTICLE"), 
    Span(doc68, 17, 18, label="PRICE"), 
    Span(doc68, 18, 19, label="UNIT"), 
    Span(doc68, 20, 21, label="SUM"), 
    Span(doc68, 59, 60, label="TARIFF"), 
    Span(doc68, 65, 66, label="COUNTRY")] 
docs.append(doc68)


doc69 = nlp('''Purchase order number: N SR-1-06 1837
8600 120 PC 6100109445 (*) 10,22 1 РС 1.226,40
QRC-FF-12-F-G12-BT-W3
FF12-1-IGF12
packed per each item
Product description: coupling
Export - Customs tariff no.: 84812010
Country of origin: Germany''')
#doc69SR-1-06 1837 8600 120 6100109445 10,22 1  84812010 Germany
print("doc69",doc69[5: 8], doc69[8: 9], doc69[10: 11], doc69[11: 12], doc69[13: 14], doc69[17:18], doc69[18:19] ,doc69[20:21], doc69[57: 58], doc69[63: 64]) 
doc69.ents = [Span(doc69, 5, 8, label="CONTRACT"), 
    Span(doc69, 8, 9, label="CONTRACT1"), 
    Span(doc69, 10, 11, label="POS"), 
    Span(doc69, 11, 12, label="AMOUNT"), 
    Span(doc69, 13, 14, label="ARTICLE"), 
    Span(doc69, 17, 18, label="PRICE"), 
    Span(doc69, 18, 19, label="UNIT"), 
    Span(doc69, 20, 21, label="SUM"), 
    Span(doc69, 57, 58, label="TARIFF"), 
    Span(doc69, 63, 64, label="COUNTRY")] 
docs.append(doc69)


doc70 = nlp('''Purchase order number: N SR-1-06 1837
8700 250 PC 6100074550 (*) 6,82 1 РС 1.705,00
QRC-FF-12-M-G08-BP-W3
FF12-2-IGF08
packed per each item
Product description: coupling
Export - Customs tariff no.: 84812010
Country of origin: Germany''')
#doc70SR-1-06 1837 8700 250 6100074550 6,82 1  84812010 Germany
print("doc70",doc70[5: 8], doc70[8: 9], doc70[10: 11], doc70[11: 12], doc70[13: 14], doc70[17:18], doc70[18:19] ,doc70[20:21], doc70[57: 58], doc70[63: 64]) 
doc70.ents = [Span(doc70, 5, 8, label="CONTRACT"), 
    Span(doc70, 8, 9, label="CONTRACT1"), 
    Span(doc70, 10, 11, label="POS"), 
    Span(doc70, 11, 12, label="AMOUNT"), 
    Span(doc70, 13, 14, label="ARTICLE"), 
    Span(doc70, 17, 18, label="PRICE"), 
    Span(doc70, 18, 19, label="UNIT"), 
    Span(doc70, 20, 21, label="SUM"), 
    Span(doc70, 57, 58, label="TARIFF"), 
    Span(doc70, 63, 64, label="COUNTRY")] 
docs.append(doc70)


doc71 = nlp('''Purchase order number: N SR-1-06 1837
8800 80 PC 6100074551 (*) 6,82 1 РС 545,60
QRC-FF-12-M-G12-BP-W3
FF12-2-IGF12

packed per each item

Product description: coupling

Export - Customs tariff no.: 84812010
Country of origin: Germany''')
#doc71SR-1-06 1837 8800 80 6100074551 6,82 1  84812010 Germany
print("doc71",doc71[5: 8], doc71[8: 9], doc71[10: 11], doc71[11: 12], doc71[13: 14], doc71[17:18], doc71[18:19] ,doc71[20:21], doc71[57: 58], doc71[63: 64]) 
doc71.ents = [Span(doc71, 5, 8, label="CONTRACT"), 
    Span(doc71, 8, 9, label="CONTRACT1"), 
    Span(doc71, 10, 11, label="POS"), 
    Span(doc71, 11, 12, label="AMOUNT"), 
    Span(doc71, 13, 14, label="ARTICLE"), 
    Span(doc71, 17, 18, label="PRICE"), 
    Span(doc71, 18, 19, label="UNIT"), 
    Span(doc71, 20, 21, label="SUM"), 
    Span(doc71, 57, 58, label="TARIFF"), 
    Span(doc71, 63, 64, label="COUNTRY")] 
docs.append(doc71)


doc72 = nlp('''Purchase order number: N SR-1-06 1838
8900 160 PC 6100109445 (*) 10,22 1 РС 1.635,20
QRC-FF-12-F-G12-BT-W3
FF12-1-IGF12
packed per each item
Product description: coupling
Export - Customs tariff no.: 84812010
Country of origin: Germany''')
#doc72SR-1-06 1838 8900 160 6100109445 10,22 1  84812010 Germany
print("doc72",doc72[5: 8], doc72[8: 9], doc72[10: 11], doc72[11: 12], doc72[13: 14], doc72[17:18], doc72[18:19] ,doc72[20:21], doc72[57: 58], doc72[63: 64]) 
doc72.ents = [Span(doc72, 5, 8, label="CONTRACT"), 
    Span(doc72, 8, 9, label="CONTRACT1"), 
    Span(doc72, 10, 11, label="POS"), 
    Span(doc72, 11, 12, label="AMOUNT"), 
    Span(doc72, 13, 14, label="ARTICLE"), 
    Span(doc72, 17, 18, label="PRICE"), 
    Span(doc72, 18, 19, label="UNIT"), 
    Span(doc72, 20, 21, label="SUM"), 
    Span(doc72, 57, 58, label="TARIFF"), 
    Span(doc72, 63, 64, label="COUNTRY")] 
docs.append(doc72)


doc73 = nlp('''Purchase order number: N SR-1-06 1838
9000 150 PC 6100074551 (*) 6,82 1 РС 1.023,00
QRC-FF-12-M-G12-BP-W3
FF12-2-IGF12
packed per each item
Product description: coupling
Export - Customs tariff no.: 84812010
Country of origin: Germany''')
#doc73SR-1-06 1838 9000 150 6100074551 6,82 1  84812010 Germany
print("doc73",doc73[5: 8], doc73[8: 9], doc73[10: 11], doc73[11: 12], doc73[13: 14], doc73[17:18], doc73[18:19] ,doc73[20:21], doc73[57: 58], doc73[63: 64]) 
doc73.ents = [Span(doc73, 5, 8, label="CONTRACT"), 
    Span(doc73, 8, 9, label="CONTRACT1"), 
    Span(doc73, 10, 11, label="POS"), 
    Span(doc73, 11, 12, label="AMOUNT"), 
    Span(doc73, 13, 14, label="ARTICLE"), 
    Span(doc73, 17, 18, label="PRICE"), 
    Span(doc73, 18, 19, label="UNIT"), 
    Span(doc73, 20, 21, label="SUM"), 
    Span(doc73, 57, 58, label="TARIFF"), 
    Span(doc73, 63, 64, label="COUNTRY")] 
docs.append(doc73)


doc74 = nlp('''Purchase order number: N SR-1-06 1841
9100 100 PC 1130004169 11,33 100 PC 11,33

AS-M10x45-DIN931/933-8.8-W3
AS-M10X45-DIN931/933-8.8-W3
packed per each item

Product description: screw

Export - Customs tariff по.: 73181588
Country of origin: Croatia''')
#doc74SR-1-06 1841 9100 100 1130004169 11,33 100  73181588 Croatia
print("doc74",doc74[5: 8], doc74[8: 9], doc74[10: 11], doc74[11: 12], doc74[13: 14], doc74[14:15], doc74[15:16] ,doc74[17:18], doc74[56: 57], doc74[62: 63]) 
doc74.ents = [Span(doc74, 5, 8, label="CONTRACT"), 
    Span(doc74, 8, 9, label="CONTRACT1"), 
    Span(doc74, 10, 11, label="POS"), 
    Span(doc74, 11, 12, label="AMOUNT"), 
    Span(doc74, 13, 14, label="ARTICLE"), 
    Span(doc74, 14, 15, label="PRICE"), 
    Span(doc74, 15, 16, label="UNIT"), 
    Span(doc74, 17, 18, label="SUM"), 
    Span(doc74, 56, 57, label="TARIFF"), 
    Span(doc74, 62, 63, label="COUNTRY")] 
docs.append(doc74)


doc75 = nlp('''Purchase order number: N SR-1-06 1841
9200 90 РС 1130004170 13,10 100 PC 11,79

AS-M10x60-DIN931/933-8.8-W3
AS-M10X60-DIN931/933-8.8-W3
packed per each item

Product description: screw

Export - Customs tariff по.: 73181588
Country of origin: Origin''')
#doc75SR-1-06 1841 9200 90 1130004170 13,10 100  73181588 Origin
print("doc75",doc75[5: 8], doc75[8: 9], doc75[10: 11], doc75[11: 12], doc75[13: 14], doc75[14:15], doc75[15:16] ,doc75[17:18], doc75[56: 57], doc75[62: 63]) 
doc75.ents = [Span(doc75, 5, 8, label="CONTRACT"), 
    Span(doc75, 8, 9, label="CONTRACT1"), 
    Span(doc75, 10, 11, label="POS"), 
    Span(doc75, 11, 12, label="AMOUNT"), 
    Span(doc75, 13, 14, label="ARTICLE"), 
    Span(doc75, 14, 15, label="PRICE"), 
    Span(doc75, 15, 16, label="UNIT"), 
    Span(doc75, 17, 18, label="SUM"), 
    Span(doc75, 56, 57, label="TARIFF"), 
    Span(doc75, 62, 63, label="COUNTRY")] 
docs.append(doc75)


doc76 = nlp('''Purchase order number: N SR-1-06 1841
9300 100 PC 1130004171 15,03 100 PC 15,03

AS-M10x70-DIN931/933-8.8-W3
AS-M10X70-DIN931/933-8.8-W3
packed per each item

Product description: screw

Export - Customs tariff по.: 73181588
Country of origin: Poland''')
#doc76SR-1-06 1841 9300 100 1130004171 15,03 100  73181588 Poland
print("doc76",doc76[5: 8], doc76[8: 9], doc76[10: 11], doc76[11: 12], doc76[13: 14], doc76[14:15], doc76[15:16] ,doc76[17:18], doc76[56: 57], doc76[62: 63]) 
doc76.ents = [Span(doc76, 5, 8, label="CONTRACT"), 
    Span(doc76, 8, 9, label="CONTRACT1"), 
    Span(doc76, 10, 11, label="POS"), 
    Span(doc76, 11, 12, label="AMOUNT"), 
    Span(doc76, 13, 14, label="ARTICLE"), 
    Span(doc76, 14, 15, label="PRICE"), 
    Span(doc76, 15, 16, label="UNIT"), 
    Span(doc76, 17, 18, label="SUM"), 
    Span(doc76, 56, 57, label="TARIFF"), 
    Span(doc76, 62, 63, label="COUNTRY")] 
docs.append(doc76)


doc77 = nlp('''Purchase order number: N SR-1-06 1841
9400 8 РС 1130004281 5,67 100 РС 0,45

AS-M8x45-DIN931/933-8.8-W3
AS-M8X45-DIN931/933-8.8-W3
packed per each item

Product description: screw

Export - Customs tariff по.: 73181588
Country of origin: Thailand''')
#doc77SR-1-06 1841 9400 8 1130004281 5,67 100  73181588 Thailand
print("doc77",doc77[5: 8], doc77[8: 9], doc77[10: 11], doc77[11: 12], doc77[13: 14], doc77[14:15], doc77[15:16] ,doc77[17:18], doc77[56: 57], doc77[62: 63]) 
doc77.ents = [Span(doc77, 5, 8, label="CONTRACT"), 
    Span(doc77, 8, 9, label="CONTRACT1"), 
    Span(doc77, 10, 11, label="POS"), 
    Span(doc77, 11, 12, label="AMOUNT"), 
    Span(doc77, 13, 14, label="ARTICLE"), 
    Span(doc77, 14, 15, label="PRICE"), 
    Span(doc77, 15, 16, label="UNIT"), 
    Span(doc77, 17, 18, label="SUM"), 
    Span(doc77, 56, 57, label="TARIFF"), 
    Span(doc77, 62, 63, label="COUNTRY")] 
docs.append(doc77)


doc78 = nlp('''Purchase order number: N SR-1-06 1841
9500 20 РС 1130005466 45,12 100 РС 9,02
3014-РР
3014 РР

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc78SR-1-06 1841 9500 20 1130005466 45,12 100  39269097 Germany
print("doc78",doc78[5: 8], doc78[8: 9], doc78[10: 11], doc78[11: 12], doc78[13: 14], doc78[14:15], doc78[15:16] ,doc78[17:18], doc78[44: 45], doc78[50: 51]) 
doc78.ents = [Span(doc78, 5, 8, label="CONTRACT"), 
    Span(doc78, 8, 9, label="CONTRACT1"), 
    Span(doc78, 10, 11, label="POS"), 
    Span(doc78, 11, 12, label="AMOUNT"), 
    Span(doc78, 13, 14, label="ARTICLE"), 
    Span(doc78, 14, 15, label="PRICE"), 
    Span(doc78, 15, 16, label="UNIT"), 
    Span(doc78, 17, 18, label="SUM"), 
    Span(doc78, 44, 45, label="TARIFF"), 
    Span(doc78, 50, 51, label="COUNTRY")] 
docs.append(doc78)


doc79 = nlp('''Purchase order number: N SR-1-06 1841
9600 25 РС 1130005659 37,50 100 PC 9,38
325/25-PP
325/25 PP

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc79SR-1-06 1841 9600 25 1130005659 37,50 100  39269097 Germany
print("doc79",doc79[5: 8], doc79[8: 9], doc79[10: 11], doc79[11: 12], doc79[13: 14], doc79[14:15], doc79[15:16] ,doc79[17:18], doc79[44: 45], doc79[50: 51]) 
doc79.ents = [Span(doc79, 5, 8, label="CONTRACT"), 
    Span(doc79, 8, 9, label="CONTRACT1"), 
    Span(doc79, 10, 11, label="POS"), 
    Span(doc79, 11, 12, label="AMOUNT"), 
    Span(doc79, 13, 14, label="ARTICLE"), 
    Span(doc79, 14, 15, label="PRICE"), 
    Span(doc79, 15, 16, label="UNIT"), 
    Span(doc79, 17, 18, label="SUM"), 
    Span(doc79, 44, 45, label="TARIFF"), 
    Span(doc79, 50, 51, label="COUNTRY")] 
docs.append(doc79)


doc80 = nlp('''Purchase order number: N SR-1-06 1841
9700 60 РС 1130005718 58,60 100 PC 35,16
4025-PP
4025 PP
packed per each item
Product description: Pipe clamp
Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc80SR-1-06 1841 9700 60 1130005718 58,60 100  39269097 Germany
print("doc80",doc80[5: 8], doc80[8: 9], doc80[10: 11], doc80[11: 12], doc80[13: 14], doc80[14:15], doc80[15:16] ,doc80[17:18], doc80[44: 45], doc80[50: 51]) 
doc80.ents = [Span(doc80, 5, 8, label="CONTRACT"), 
    Span(doc80, 8, 9, label="CONTRACT1"), 
    Span(doc80, 10, 11, label="POS"), 
    Span(doc80, 11, 12, label="AMOUNT"), 
    Span(doc80, 13, 14, label="ARTICLE"), 
    Span(doc80, 14, 15, label="PRICE"), 
    Span(doc80, 15, 16, label="UNIT"), 
    Span(doc80, 17, 18, label="SUM"), 
    Span(doc80, 44, 45, label="TARIFF"), 
    Span(doc80, 50, 51, label="COUNTRY")] 
docs.append(doc80)


doc81 = nlp('''Purchase order number: N SR-1-06 1841
9800 20 РС 1130005887 83,61 100 РС 16,72
5033.7-PP
5033,7 PP

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc81SR-1-06 1841 9800 20 1130005887 83,61 100  39269097 Germany
print("doc81",doc81[5: 8], doc81[8: 9], doc81[10: 11], doc81[11: 12], doc81[13: 14], doc81[14:15], doc81[15:16] ,doc81[17:18], doc81[44: 45], doc81[50: 51]) 
doc81.ents = [Span(doc81, 5, 8, label="CONTRACT"), 
    Span(doc81, 8, 9, label="CONTRACT1"), 
    Span(doc81, 10, 11, label="POS"), 
    Span(doc81, 11, 12, label="AMOUNT"), 
    Span(doc81, 13, 14, label="ARTICLE"), 
    Span(doc81, 14, 15, label="PRICE"), 
    Span(doc81, 15, 16, label="UNIT"), 
    Span(doc81, 17, 18, label="SUM"), 
    Span(doc81, 44, 45, label="TARIFF"), 
    Span(doc81, 50, 51, label="COUNTRY")] 
docs.append(doc81)


doc82 = nlp('''Purchase order number: N SR-1-06 1841
9900 20 РС 1130002873 33,39 100 РС 6,68
DPAL-3S-W3
DPAL 3 S W3

packed per each item

Product description: cover plate

Export - Customs tariff no.: 73182900
Country of origin: Germany''')
#doc82SR-1-06 1841 9900 20 1130002873 33,39 100  73182900 Germany
print("doc82",doc82[5: 8], doc82[8: 9], doc82[10: 11], doc82[11: 12], doc82[13: 14], doc82[14:15], doc82[15:16] ,doc82[17:18], doc82[46: 47], doc82[52: 53]) 
doc82.ents = [Span(doc82, 5, 8, label="CONTRACT"), 
    Span(doc82, 8, 9, label="CONTRACT1"), 
    Span(doc82, 10, 11, label="POS"), 
    Span(doc82, 11, 12, label="AMOUNT"), 
    Span(doc82, 13, 14, label="ARTICLE"), 
    Span(doc82, 14, 15, label="PRICE"), 
    Span(doc82, 15, 16, label="UNIT"), 
    Span(doc82, 17, 18, label="SUM"), 
    Span(doc82, 46, 47, label="TARIFF"), 
    Span(doc82, 52, 53, label="COUNTRY")] 
docs.append(doc82)


doc83 = nlp('''Purchase order number: N SR-1-06 1841
10000 60 РС 1130000711 39,46 100 PC 23,68
DPAL-4S-W3
DPAL 4 S W3
packed per each item
Product description: cover plate
Export - Customs tariff no.: 73182900
Country of origin: Germany''')
#doc83SR-1-06 1841 10000 60 1130000711 39,46 100  73182900 Germany
print("doc83",doc83[5: 8], doc83[8: 9], doc83[10: 11], doc83[11: 12], doc83[13: 14], doc83[14:15], doc83[15:16] ,doc83[17:18], doc83[46: 47], doc83[52: 53]) 
doc83.ents = [Span(doc83, 5, 8, label="CONTRACT"), 
    Span(doc83, 8, 9, label="CONTRACT1"), 
    Span(doc83, 10, 11, label="POS"), 
    Span(doc83, 11, 12, label="AMOUNT"), 
    Span(doc83, 13, 14, label="ARTICLE"), 
    Span(doc83, 14, 15, label="PRICE"), 
    Span(doc83, 15, 16, label="UNIT"), 
    Span(doc83, 17, 18, label="SUM"), 
    Span(doc83, 46, 47, label="TARIFF"), 
    Span(doc83, 52, 53, label="COUNTRY")] 
docs.append(doc83)


doc84 = nlp('''Purchase order number: N SR-1-06 1841
10100 60 PC 1130002875 47,10 100 PC 28,26
DPAL-5S-W3
DPAL 5 S W3

packed per each item

Product description: cover plate

Export - Customs tariff no.: 73182900
Country of origin: Germany''')
#doc84SR-1-06 1841 10100 60 1130002875 47,10 100  73182900 Germany
print("doc84",doc84[5: 8], doc84[8: 9], doc84[10: 11], doc84[11: 12], doc84[13: 14], doc84[14:15], doc84[15:16] ,doc84[17:18], doc84[46: 47], doc84[52: 53]) 
doc84.ents = [Span(doc84, 5, 8, label="CONTRACT"), 
    Span(doc84, 8, 9, label="CONTRACT1"), 
    Span(doc84, 10, 11, label="POS"), 
    Span(doc84, 11, 12, label="AMOUNT"), 
    Span(doc84, 13, 14, label="ARTICLE"), 
    Span(doc84, 14, 15, label="PRICE"), 
    Span(doc84, 15, 16, label="UNIT"), 
    Span(doc84, 17, 18, label="SUM"), 
    Span(doc84, 46, 47, label="TARIFF"), 
    Span(doc84, 52, 53, label="COUNTRY")] 
docs.append(doc84)


doc85 = nlp('''Purchase order number: N SR-1-06 1841
10200 20 РС 1120001947 66,80 100 PC 13,36
SPAL-3S-M-W2

SPAL 3 S M W2

packed per each item

Product description: weld plate

Export - Customs tariff no.: 73269098
Country of origin: Germany''')
#doc85SR-1-06 1841 10200 20 1120001947 66,80 100  73269098 Germany
print("doc85",doc85[5: 8], doc85[8: 9], doc85[10: 11], doc85[11: 12], doc85[13: 14], doc85[14:15], doc85[15:16] ,doc85[17:18], doc85[49: 50], doc85[55: 56]) 
doc85.ents = [Span(doc85, 5, 8, label="CONTRACT"), 
    Span(doc85, 8, 9, label="CONTRACT1"), 
    Span(doc85, 10, 11, label="POS"), 
    Span(doc85, 11, 12, label="AMOUNT"), 
    Span(doc85, 13, 14, label="ARTICLE"), 
    Span(doc85, 14, 15, label="PRICE"), 
    Span(doc85, 15, 16, label="UNIT"), 
    Span(doc85, 17, 18, label="SUM"), 
    Span(doc85, 49, 50, label="TARIFF"), 
    Span(doc85, 55, 56, label="COUNTRY")] 
docs.append(doc85)


doc86 = nlp('''Purchase order number: N SR-1-06 1841
10300 60 PC 1120001950 76,42 100 PC 45,85
SPAL-4S-M-W2

SPAL 4 S M W2

packed per each item

Product description: weld plate

Export - Customs tariff no.: 73269098
Country of origin: Germany''')
#doc86SR-1-06 1841 10300 60 1120001950 76,42 100  73269098 Germany
print("doc86",doc86[5: 8], doc86[8: 9], doc86[10: 11], doc86[11: 12], doc86[13: 14], doc86[14:15], doc86[15:16] ,doc86[17:18], doc86[49: 50], doc86[55: 56]) 
doc86.ents = [Span(doc86, 5, 8, label="CONTRACT"), 
    Span(doc86, 8, 9, label="CONTRACT1"), 
    Span(doc86, 10, 11, label="POS"), 
    Span(doc86, 11, 12, label="AMOUNT"), 
    Span(doc86, 13, 14, label="ARTICLE"), 
    Span(doc86, 14, 15, label="PRICE"), 
    Span(doc86, 15, 16, label="UNIT"), 
    Span(doc86, 17, 18, label="SUM"), 
    Span(doc86, 49, 50, label="TARIFF"), 
    Span(doc86, 55, 56, label="COUNTRY")] 
docs.append(doc86)


doc87 = nlp('''Purchase order number: N SR-1-06 1841
10400 3 PC 1910000571 (*) 9,27 1 РС 27,81

ЗМА-176-В-$-0-12

SNA 176 B-S-O-12

packed per each item

Product description: level gauge
Export - Customs tariff no.: 90261089
Country of origin: Germany''')
#doc87SR-1-06 1841 10400 3 1910000571 9,27 1  90261089 Germany
print("doc87",doc87[5: 8], doc87[8: 9], doc87[10: 11], doc87[11: 12], doc87[13: 14], doc87[17:18], doc87[18:19] ,doc87[20:21], doc87[54: 55], doc87[60: 61]) 
doc87.ents = [Span(doc87, 5, 8, label="CONTRACT"), 
    Span(doc87, 8, 9, label="CONTRACT1"), 
    Span(doc87, 10, 11, label="POS"), 
    Span(doc87, 11, 12, label="AMOUNT"), 
    Span(doc87, 13, 14, label="ARTICLE"), 
    Span(doc87, 17, 18, label="PRICE"), 
    Span(doc87, 18, 19, label="UNIT"), 
    Span(doc87, 20, 21, label="SUM"), 
    Span(doc87, 54, 55, label="TARIFF"), 
    Span(doc87, 60, 61, label="COUNTRY")] 
docs.append(doc87)


doc88 = nlp('''Purchase order number: N SR-1-06 1842
10500 50 PC 6010000766 (*) 88,80 100 PC 44,40

FI-G-08S-W3-MS

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc88SR-1-06 1842 10500 50 6010000766 88,80 100  73079910 Germany
print("doc88",doc88[5: 8], doc88[8: 9], doc88[10: 11], doc88[11: 12], doc88[13: 14], doc88[17:18], doc88[18:19] ,doc88[20:21], doc88[47: 48], doc88[53: 54]) 
doc88.ents = [Span(doc88, 5, 8, label="CONTRACT"), 
    Span(doc88, 8, 9, label="CONTRACT1"), 
    Span(doc88, 10, 11, label="POS"), 
    Span(doc88, 11, 12, label="AMOUNT"), 
    Span(doc88, 13, 14, label="ARTICLE"), 
    Span(doc88, 17, 18, label="PRICE"), 
    Span(doc88, 18, 19, label="UNIT"), 
    Span(doc88, 20, 21, label="SUM"), 
    Span(doc88, 47, 48, label="TARIFF"), 
    Span(doc88, 53, 54, label="COUNTRY")] 
docs.append(doc88)


doc89 = nlp('''Purchase order number: N SR-1-06 1843
10600 1 РС 1020023641 (*) 124,70 1 РС 124,70
SE-090-H-10-B/4
SE-090H10B/4

packed per each item

Product description: filter element
Export - Customs tariff no.: 84219990
Country of origin: Germany''')
#doc89SR-1-06 1843 10600 1 1020023641 124,70 1  84219990 Germany
print("doc89",doc89[5: 8], doc89[8: 9], doc89[10: 11], doc89[11: 12], doc89[13: 14], doc89[17:18], doc89[18:19] ,doc89[20:21], doc89[48: 49], doc89[54: 55]) 
doc89.ents = [Span(doc89, 5, 8, label="CONTRACT"), 
    Span(doc89, 8, 9, label="CONTRACT1"), 
    Span(doc89, 10, 11, label="POS"), 
    Span(doc89, 11, 12, label="AMOUNT"), 
    Span(doc89, 13, 14, label="ARTICLE"), 
    Span(doc89, 17, 18, label="PRICE"), 
    Span(doc89, 18, 19, label="UNIT"), 
    Span(doc89, 20, 21, label="SUM"), 
    Span(doc89, 48, 49, label="TARIFF"), 
    Span(doc89, 54, 55, label="COUNTRY")] 
docs.append(doc89)


doc90 = nlp('''Purchase order number: N SR-1-06 1843
10700 1 РС 1020022243 112,15 1 РС 112,15

NL-630-E-10-B/4

NL-630E10B/4

packed per each item

Product description: filter element
Export - Customs tariff no.: 84219990
Country of origin: Germany''')
#doc90SR-1-06 1843 10700 1 1020022243 112,15 1  84219990 Germany
print("doc90",doc90[5: 8], doc90[8: 9], doc90[10: 11], doc90[11: 12], doc90[13: 14], doc90[14:15], doc90[15:16] ,doc90[17:18], doc90[45: 46], doc90[51: 52]) 
doc90.ents = [Span(doc90, 5, 8, label="CONTRACT"), 
    Span(doc90, 8, 9, label="CONTRACT1"), 
    Span(doc90, 10, 11, label="POS"), 
    Span(doc90, 11, 12, label="AMOUNT"), 
    Span(doc90, 13, 14, label="ARTICLE"), 
    Span(doc90, 14, 15, label="PRICE"), 
    Span(doc90, 15, 16, label="UNIT"), 
    Span(doc90, 17, 18, label="SUM"), 
    Span(doc90, 45, 46, label="TARIFF"), 
    Span(doc90, 51, 52, label="COUNTRY")] 
docs.append(doc90)


doc91 = nlp('''Purchase order number: N SR-1-06 1845
10800 100 PC 1130004169 11,33 100 PC 11,33

AS-M10x45-DIN931/933-8.8-W3
AS-M10X45-DIN931/933-8.8-W3
packed per each item

Product description: screw

Export - Customs tariff по.: 73181588
Country of origin: Croatia''')
#doc91SR-1-06 1845 10800 100 1130004169 11,33 100  73181588 Croatia
print("doc91",doc91[5: 8], doc91[8: 9], doc91[10: 11], doc91[11: 12], doc91[13: 14], doc91[14:15], doc91[15:16] ,doc91[17:18], doc91[56: 57], doc91[62: 63]) 
doc91.ents = [Span(doc91, 5, 8, label="CONTRACT"), 
    Span(doc91, 8, 9, label="CONTRACT1"), 
    Span(doc91, 10, 11, label="POS"), 
    Span(doc91, 11, 12, label="AMOUNT"), 
    Span(doc91, 13, 14, label="ARTICLE"), 
    Span(doc91, 14, 15, label="PRICE"), 
    Span(doc91, 15, 16, label="UNIT"), 
    Span(doc91, 17, 18, label="SUM"), 
    Span(doc91, 56, 57, label="TARIFF"), 
    Span(doc91, 62, 63, label="COUNTRY")] 
docs.append(doc91)


doc92 = nlp('''Purchase order number: N SR-1-06 1845
10900 140 PC 1130004170 13,10 100 PC 18,34

AS-M10x60-DIN931/933-8.8-W3
AS-M10X60-DIN931/933-8.8-W3
packed per each item

Product description: screw

Export - Customs tariff по.: 73181588
Country of origin: Origin''')
#doc92SR-1-06 1845 10900 140 1130004170 13,10 100  73181588 Origin
print("doc92",doc92[5: 8], doc92[8: 9], doc92[10: 11], doc92[11: 12], doc92[13: 14], doc92[14:15], doc92[15:16] ,doc92[17:18], doc92[56: 57], doc92[62: 63]) 
doc92.ents = [Span(doc92, 5, 8, label="CONTRACT"), 
    Span(doc92, 8, 9, label="CONTRACT1"), 
    Span(doc92, 10, 11, label="POS"), 
    Span(doc92, 11, 12, label="AMOUNT"), 
    Span(doc92, 13, 14, label="ARTICLE"), 
    Span(doc92, 14, 15, label="PRICE"), 
    Span(doc92, 15, 16, label="UNIT"), 
    Span(doc92, 17, 18, label="SUM"), 
    Span(doc92, 56, 57, label="TARIFF"), 
    Span(doc92, 62, 63, label="COUNTRY")] 
docs.append(doc92)


doc93 = nlp('''Purchase order number: N SR-1-06 1845
11000 400 РС 1130004171 15,03 100 PC 60,12

AS-M10x70-DIN931/933-8.8-W3
AS-M10X70-DIN931/933-8.8-W3
packed per each item

Product description: screw

Export - Customs tariff по.: 73181588
Country of origin: Poland''')
#doc93SR-1-06 1845 11000 400 1130004171 15,03 100  73181588 Poland
print("doc93",doc93[5: 8], doc93[8: 9], doc93[10: 11], doc93[11: 12], doc93[13: 14], doc93[14:15], doc93[15:16] ,doc93[17:18], doc93[56: 57], doc93[62: 63]) 
doc93.ents = [Span(doc93, 5, 8, label="CONTRACT"), 
    Span(doc93, 8, 9, label="CONTRACT1"), 
    Span(doc93, 10, 11, label="POS"), 
    Span(doc93, 11, 12, label="AMOUNT"), 
    Span(doc93, 13, 14, label="ARTICLE"), 
    Span(doc93, 14, 15, label="PRICE"), 
    Span(doc93, 15, 16, label="UNIT"), 
    Span(doc93, 17, 18, label="SUM"), 
    Span(doc93, 56, 57, label="TARIFF"), 
    Span(doc93, 62, 63, label="COUNTRY")] 
docs.append(doc93)


doc94 = nlp('''Purchase order number: N SR-1-06 1845
11100 40 РС 1130004173 28,30 100 РС 11,32

AS-M12x100-DIN931/933-8.8-W3
AS-M12X100-DIN931/933-8.8-W3
packed per each item

Product description: screw

Export - Customs tariff по.: 73181588
Country of origin: Thailand''')
#doc94SR-1-06 1845 11100 40 1130004173 28,30 100  73181588 Thailand
print("doc94",doc94[5: 8], doc94[8: 9], doc94[10: 11], doc94[11: 12], doc94[13: 14], doc94[14:15], doc94[15:16] ,doc94[17:18], doc94[56: 57], doc94[62: 63]) 
doc94.ents = [Span(doc94, 5, 8, label="CONTRACT"), 
    Span(doc94, 8, 9, label="CONTRACT1"), 
    Span(doc94, 10, 11, label="POS"), 
    Span(doc94, 11, 12, label="AMOUNT"), 
    Span(doc94, 13, 14, label="ARTICLE"), 
    Span(doc94, 14, 15, label="PRICE"), 
    Span(doc94, 15, 16, label="UNIT"), 
    Span(doc94, 17, 18, label="SUM"), 
    Span(doc94, 56, 57, label="TARIFF"), 
    Span(doc94, 62, 63, label="COUNTRY")] 
docs.append(doc94)


doc95 = nlp('''Purchase order number: N SR-1-06 1845
11200 560 РС 1130000075 (*) 59,97 100 PC 335,83

GMV-3-5S-M-W3/2

GMV 3-5 $ /2 М МЗ

packed per each item

Product description: nuts

Export - Customs tariff no.: 73181692
Country of origin: India''')
#doc95SR-1-06 1845 11200 560 1130000075 59,97 100  73181692 India
print("doc95",doc95[5: 8], doc95[8: 9], doc95[10: 11], doc95[11: 12], doc95[13: 14], doc95[17:18], doc95[18:19] ,doc95[20:21], doc95[56: 57], doc95[62: 63]) 
doc95.ents = [Span(doc95, 5, 8, label="CONTRACT"), 
    Span(doc95, 8, 9, label="CONTRACT1"), 
    Span(doc95, 10, 11, label="POS"), 
    Span(doc95, 11, 12, label="AMOUNT"), 
    Span(doc95, 13, 14, label="ARTICLE"), 
    Span(doc95, 17, 18, label="PRICE"), 
    Span(doc95, 18, 19, label="UNIT"), 
    Span(doc95, 20, 21, label="SUM"), 
    Span(doc95, 56, 57, label="TARIFF"), 
    Span(doc95, 62, 63, label="COUNTRY")] 
docs.append(doc95)


doc96 = nlp('''Purchase order number: N SR-1-06 1845
11300 60 РС 1130005699 58,60 100 PC 35,16
4021.3-PP
4021,3 PP

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc96SR-1-06 1845 11300 60 1130005699 58,60 100  39269097 Germany
print("doc96",doc96[5: 8], doc96[8: 9], doc96[10: 11], doc96[11: 12], doc96[13: 14], doc96[14:15], doc96[15:16] ,doc96[17:18], doc96[44: 45], doc96[50: 51]) 
doc96.ents = [Span(doc96, 5, 8, label="CONTRACT"), 
    Span(doc96, 8, 9, label="CONTRACT1"), 
    Span(doc96, 10, 11, label="POS"), 
    Span(doc96, 11, 12, label="AMOUNT"), 
    Span(doc96, 13, 14, label="ARTICLE"), 
    Span(doc96, 14, 15, label="PRICE"), 
    Span(doc96, 15, 16, label="UNIT"), 
    Span(doc96, 17, 18, label="SUM"), 
    Span(doc96, 44, 45, label="TARIFF"), 
    Span(doc96, 50, 51, label="COUNTRY")] 
docs.append(doc96)


doc97 = nlp('''Purchase order number: N SR-1-06 1845
11400 20 РС 1130005733 58,60 100 PC 11,72
4026.9-PP
4026,9 PP

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc97SR-1-06 1845 11400 20 1130005733 58,60 100  39269097 Germany
print("doc97",doc97[5: 8], doc97[8: 9], doc97[10: 11], doc97[11: 12], doc97[13: 14], doc97[14:15], doc97[15:16] ,doc97[17:18], doc97[44: 45], doc97[50: 51]) 
doc97.ents = [Span(doc97, 5, 8, label="CONTRACT"), 
    Span(doc97, 8, 9, label="CONTRACT1"), 
    Span(doc97, 10, 11, label="POS"), 
    Span(doc97, 11, 12, label="AMOUNT"), 
    Span(doc97, 13, 14, label="ARTICLE"), 
    Span(doc97, 14, 15, label="PRICE"), 
    Span(doc97, 15, 16, label="UNIT"), 
    Span(doc97, 17, 18, label="SUM"), 
    Span(doc97, 44, 45, label="TARIFF"), 
    Span(doc97, 50, 51, label="COUNTRY")] 
docs.append(doc97)


doc98 = nlp('''Purchase order number: N SR-1-06 1845
11500 40 РС 1130005887 83,61 100 РС 33,44
5033.7-PP
5033,7 PP
packed per each item
Product description: Pipe clamp
Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc98SR-1-06 1845 11500 40 1130005887 83,61 100  39269097 Germany
print("doc98",doc98[5: 8], doc98[8: 9], doc98[10: 11], doc98[11: 12], doc98[13: 14], doc98[14:15], doc98[15:16] ,doc98[17:18], doc98[44: 45], doc98[50: 51]) 
doc98.ents = [Span(doc98, 5, 8, label="CONTRACT"), 
    Span(doc98, 8, 9, label="CONTRACT1"), 
    Span(doc98, 10, 11, label="POS"), 
    Span(doc98, 11, 12, label="AMOUNT"), 
    Span(doc98, 13, 14, label="ARTICLE"), 
    Span(doc98, 14, 15, label="PRICE"), 
    Span(doc98, 15, 16, label="UNIT"), 
    Span(doc98, 17, 18, label="SUM"), 
    Span(doc98, 44, 45, label="TARIFF"), 
    Span(doc98, 50, 51, label="COUNTRY")] 
docs.append(doc98)


doc99 = nlp('''Purchase order number: N SR-1-06 1845
11600 160 PC 1130005933 83,61 100 PC 133,78
5042-РР
5042 РР

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc99SR-1-06 1845 11600 160 1130005933 83,61 100  39269097 Germany
print("doc99",doc99[5: 8], doc99[8: 9], doc99[10: 11], doc99[11: 12], doc99[13: 14], doc99[14:15], doc99[15:16] ,doc99[17:18], doc99[44: 45], doc99[50: 51]) 
doc99.ents = [Span(doc99, 5, 8, label="CONTRACT"), 
    Span(doc99, 8, 9, label="CONTRACT1"), 
    Span(doc99, 10, 11, label="POS"), 
    Span(doc99, 11, 12, label="AMOUNT"), 
    Span(doc99, 13, 14, label="ARTICLE"), 
    Span(doc99, 14, 15, label="PRICE"), 
    Span(doc99, 15, 16, label="UNIT"), 
    Span(doc99, 17, 18, label="SUM"), 
    Span(doc99, 44, 45, label="TARIFF"), 
    Span(doc99, 50, 51, label="COUNTRY")] 
docs.append(doc99)


doc100 = nlp('''Purchase order number: N SR-1-06 1845
11700 20 РС 1130003103 168,56 100 РС 33,71
6048.3-PP
6048,3 PP

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc100SR-1-06 1845 11700 20 1130003103 168,56 100  39269097 Germany
print("doc100",doc100[5: 8], doc100[8: 9], doc100[10: 11], doc100[11: 12], doc100[13: 14], doc100[14:15], doc100[15:16] ,doc100[17:18], doc100[44: 45], doc100[50: 51]) 
doc100.ents = [Span(doc100, 5, 8, label="CONTRACT"), 
    Span(doc100, 8, 9, label="CONTRACT1"), 
    Span(doc100, 10, 11, label="POS"), 
    Span(doc100, 11, 12, label="AMOUNT"), 
    Span(doc100, 13, 14, label="ARTICLE"), 
    Span(doc100, 14, 15, label="PRICE"), 
    Span(doc100, 15, 16, label="UNIT"), 
    Span(doc100, 17, 18, label="SUM"), 
    Span(doc100, 44, 45, label="TARIFF"), 
    Span(doc100, 50, 51, label="COUNTRY")] 
docs.append(doc100)


doc101 = nlp('''Purchase order number: N SR-1-06 1845
11800 30 PC 1130004258 474,63 100 PC 142,39
STSV-1M-W1
STSV-1m W1

packed per each item

Product description: mounting rail
Export - Customs tariff по.: 72166110
Country of origin: Germany''')
#doc101SR-1-06 1845 11800 30 1130004258 474,63 100  72166110 Germany
print("doc101",doc101[5: 8], doc101[8: 9], doc101[10: 11], doc101[11: 12], doc101[13: 14], doc101[14:15], doc101[15:16] ,doc101[17:18], doc101[45: 46], doc101[51: 52]) 
doc101.ents = [Span(doc101, 5, 8, label="CONTRACT"), 
    Span(doc101, 8, 9, label="CONTRACT1"), 
    Span(doc101, 10, 11, label="POS"), 
    Span(doc101, 11, 12, label="AMOUNT"), 
    Span(doc101, 13, 14, label="ARTICLE"), 
    Span(doc101, 14, 15, label="PRICE"), 
    Span(doc101, 15, 16, label="UNIT"), 
    Span(doc101, 17, 18, label="SUM"), 
    Span(doc101, 45, 46, label="TARIFF"), 
    Span(doc101, 51, 52, label="COUNTRY")] 
docs.append(doc101)


doc102 = nlp('''Purchase order number: N SR-1-06 1845
11900 40 РС 1130002873 33,39 100 РС 13,36
DPAL-3S-W3
DPAL 3 S W3

packed per each item

Product description: cover plate

Export - Customs tariff no.: 73182900
Country of origin: Germany''')
#doc102SR-1-06 1845 11900 40 1130002873 33,39 100  73182900 Germany
print("doc102",doc102[5: 8], doc102[8: 9], doc102[10: 11], doc102[11: 12], doc102[13: 14], doc102[14:15], doc102[15:16] ,doc102[17:18], doc102[46: 47], doc102[52: 53]) 
doc102.ents = [Span(doc102, 5, 8, label="CONTRACT"), 
    Span(doc102, 8, 9, label="CONTRACT1"), 
    Span(doc102, 10, 11, label="POS"), 
    Span(doc102, 11, 12, label="AMOUNT"), 
    Span(doc102, 13, 14, label="ARTICLE"), 
    Span(doc102, 14, 15, label="PRICE"), 
    Span(doc102, 15, 16, label="UNIT"), 
    Span(doc102, 17, 18, label="SUM"), 
    Span(doc102, 46, 47, label="TARIFF"), 
    Span(doc102, 52, 53, label="COUNTRY")] 
docs.append(doc102)


doc103 = nlp('''Purchase order number: N SR-1-06 1845
12000 80 РС 1130000711 39,46 100 РС 31,57
DPAL-4S-W3
DPAL 4 S W3

packed per each item

Product description: cover plate

Export - Customs tariff no.: 73182900
Country of origin: Germany''')
#doc103SR-1-06 1845 12000 80 1130000711 39,46 100  73182900 Germany
print("doc103",doc103[5: 8], doc103[8: 9], doc103[10: 11], doc103[11: 12], doc103[13: 14], doc103[14:15], doc103[15:16] ,doc103[17:18], doc103[46: 47], doc103[52: 53]) 
doc103.ents = [Span(doc103, 5, 8, label="CONTRACT"), 
    Span(doc103, 8, 9, label="CONTRACT1"), 
    Span(doc103, 10, 11, label="POS"), 
    Span(doc103, 11, 12, label="AMOUNT"), 
    Span(doc103, 13, 14, label="ARTICLE"), 
    Span(doc103, 14, 15, label="PRICE"), 
    Span(doc103, 15, 16, label="UNIT"), 
    Span(doc103, 17, 18, label="SUM"), 
    Span(doc103, 46, 47, label="TARIFF"), 
    Span(doc103, 52, 53, label="COUNTRY")] 
docs.append(doc103)


doc104 = nlp('''Purchase order number: N SR-1-06 1845
12100 180 PC 1130002875 47,10 100 PC 84,78
DPAL-5S-W3
DPAL 5 S W3
packed per each item
Product description: cover plate
Export - Customs tariff no.: 73182900
Country of origin: Germany''')
#doc104SR-1-06 1845 12100 180 1130002875 47,10 100  73182900 Germany
print("doc104",doc104[5: 8], doc104[8: 9], doc104[10: 11], doc104[11: 12], doc104[13: 14], doc104[14:15], doc104[15:16] ,doc104[17:18], doc104[46: 47], doc104[52: 53]) 
doc104.ents = [Span(doc104, 5, 8, label="CONTRACT"), 
    Span(doc104, 8, 9, label="CONTRACT1"), 
    Span(doc104, 10, 11, label="POS"), 
    Span(doc104, 11, 12, label="AMOUNT"), 
    Span(doc104, 13, 14, label="ARTICLE"), 
    Span(doc104, 14, 15, label="PRICE"), 
    Span(doc104, 15, 16, label="UNIT"), 
    Span(doc104, 17, 18, label="SUM"), 
    Span(doc104, 46, 47, label="TARIFF"), 
    Span(doc104, 52, 53, label="COUNTRY")] 
docs.append(doc104)


doc105 = nlp('''Purchase order number: N SR-1-06 1845
12200 20 РС 1130002876 103,32 100 РС 20,66
DPAL-6S-W3
DPAL 6 S W3

packed per each item

Product description: cover plate

Export - Customs tariff no.: 73182900
Country of origin: Germany''')
#doc105SR-1-06 1845 12200 20 1130002876 103,32 100  73182900 Germany
print("doc105",doc105[5: 8], doc105[8: 9], doc105[10: 11], doc105[11: 12], doc105[13: 14], doc105[14:15], doc105[15:16] ,doc105[17:18], doc105[46: 47], doc105[52: 53]) 
doc105.ents = [Span(doc105, 5, 8, label="CONTRACT"), 
    Span(doc105, 8, 9, label="CONTRACT1"), 
    Span(doc105, 10, 11, label="POS"), 
    Span(doc105, 11, 12, label="AMOUNT"), 
    Span(doc105, 13, 14, label="ARTICLE"), 
    Span(doc105, 14, 15, label="PRICE"), 
    Span(doc105, 15, 16, label="UNIT"), 
    Span(doc105, 17, 18, label="SUM"), 
    Span(doc105, 46, 47, label="TARIFF"), 
    Span(doc105, 52, 53, label="COUNTRY")] 
docs.append(doc105)


doc106 = nlp('''Purchase order number: N SR-1-06 1846
12300 20 РС 1130003978 12,89 100 РС 2,58

15-М6Х20-1$04762-70-\/4

packed per each item

Product description: screw

Export - Customs tariff по.: 73181562
Country of origin: Malaysia''')
#doc106SR-1-06 1846 12300 20 1130003978 12,89 100  73181562 Malaysia
print("doc106",doc106[5: 8], doc106[8: 9], doc106[10: 11], doc106[11: 12], doc106[13: 14], doc106[14:15], doc106[15:16] ,doc106[17:18], doc106[44: 45], doc106[50: 51]) 
doc106.ents = [Span(doc106, 5, 8, label="CONTRACT"), 
    Span(doc106, 8, 9, label="CONTRACT1"), 
    Span(doc106, 10, 11, label="POS"), 
    Span(doc106, 11, 12, label="AMOUNT"), 
    Span(doc106, 13, 14, label="ARTICLE"), 
    Span(doc106, 14, 15, label="PRICE"), 
    Span(doc106, 15, 16, label="UNIT"), 
    Span(doc106, 17, 18, label="SUM"), 
    Span(doc106, 44, 45, label="TARIFF"), 
    Span(doc106, 50, 51, label="COUNTRY")] 
docs.append(doc106)


doc107 = nlp('''Purchase order number: N SR-1-06 1846
12400 60 PC 1130003971 4,51 100 PC 2,71

IS-M6X25-ISO4762-8.8-W3

packed per each item

Product description: screw

Export - Customs tariff no.: 73181568
Country of origin: Taiwan''')
#doc107SR-1-06 1846 12400 60 1130003971 4,51 100  73181568 Taiwan
print("doc107",doc107[5: 8], doc107[8: 9], doc107[10: 11], doc107[11: 12], doc107[13: 14], doc107[14:15], doc107[15:16] ,doc107[17:18], doc107[46: 47], doc107[52: 53]) 
doc107.ents = [Span(doc107, 5, 8, label="CONTRACT"), 
    Span(doc107, 8, 9, label="CONTRACT1"), 
    Span(doc107, 10, 11, label="POS"), 
    Span(doc107, 11, 12, label="AMOUNT"), 
    Span(doc107, 13, 14, label="ARTICLE"), 
    Span(doc107, 14, 15, label="PRICE"), 
    Span(doc107, 15, 16, label="UNIT"), 
    Span(doc107, 17, 18, label="SUM"), 
    Span(doc107, 46, 47, label="TARIFF"), 
    Span(doc107, 52, 53, label="COUNTRY")] 
docs.append(doc107)


doc108 = nlp('''Purchase order number: N SR-1-06 1846
12500 50 PC 1120001230 30,47 100 PC 15,24
SPV-2-M-W2
SPV 2 M W2

packed per each item

Product description: weld plate

Export - Customs tariff no.: 73269098
Country of origin: Germany''')
#doc108SR-1-06 1846 12500 50 1120001230 30,47 100  73269098 Germany
print("doc108",doc108[5: 8], doc108[8: 9], doc108[10: 11], doc108[11: 12], doc108[13: 14], doc108[14:15], doc108[15:16] ,doc108[17:18], doc108[48: 49], doc108[54: 55]) 
doc108.ents = [Span(doc108, 5, 8, label="CONTRACT"), 
    Span(doc108, 8, 9, label="CONTRACT1"), 
    Span(doc108, 10, 11, label="POS"), 
    Span(doc108, 11, 12, label="AMOUNT"), 
    Span(doc108, 13, 14, label="ARTICLE"), 
    Span(doc108, 14, 15, label="PRICE"), 
    Span(doc108, 15, 16, label="UNIT"), 
    Span(doc108, 17, 18, label="SUM"), 
    Span(doc108, 48, 49, label="TARIFF"), 
    Span(doc108, 54, 55, label="COUNTRY")] 
docs.append(doc108)


doc109 = nlp('''Purchase order number: N SR-1-06 1847
12600 60 РС 6100038382 1,08 1 РС 64,80

ОКС-Н$-10-ОЕ-23-К-КО

HS08-0-RT001

packed per each item

Export - Customs tariff no.: 39235090
Country of origin: Germany''')
#doc109SR-1-06 1847 12600 60 6100038382 1,08 1  39235090 Germany
print("doc109",doc109[5: 8], doc109[8: 9], doc109[10: 11], doc109[11: 12], doc109[13: 14], doc109[14:15], doc109[15:16] ,doc109[17:18], doc109[47: 48], doc109[53: 54]) 
doc109.ents = [Span(doc109, 5, 8, label="CONTRACT"), 
    Span(doc109, 8, 9, label="CONTRACT1"), 
    Span(doc109, 10, 11, label="POS"), 
    Span(doc109, 11, 12, label="AMOUNT"), 
    Span(doc109, 13, 14, label="ARTICLE"), 
    Span(doc109, 14, 15, label="PRICE"), 
    Span(doc109, 15, 16, label="UNIT"), 
    Span(doc109, 17, 18, label="SUM"), 
    Span(doc109, 47, 48, label="TARIFF"), 
    Span(doc109, 53, 54, label="COUNTRY")] 
docs.append(doc109)


doc110 = nlp('''Purchase order number: N SR-1-06 1847
12700 60 РС 6100038383 1,08 1 РС 64,80

QRC-HS-10-DM-23-K-RD

HS08-9-RT001

packed per each item

Export - Customs tariff no.: 39235090
Country of origin: Germany''')
#doc110SR-1-06 1847 12700 60 6100038383 1,08 1  39235090 Germany
print("doc110",doc110[5: 8], doc110[8: 9], doc110[10: 11], doc110[11: 12], doc110[13: 14], doc110[14:15], doc110[15:16] ,doc110[17:18], doc110[47: 48], doc110[53: 54]) 
doc110.ents = [Span(doc110, 5, 8, label="CONTRACT"), 
    Span(doc110, 8, 9, label="CONTRACT1"), 
    Span(doc110, 10, 11, label="POS"), 
    Span(doc110, 11, 12, label="AMOUNT"), 
    Span(doc110, 13, 14, label="ARTICLE"), 
    Span(doc110, 14, 15, label="PRICE"), 
    Span(doc110, 15, 16, label="UNIT"), 
    Span(doc110, 17, 18, label="SUM"), 
    Span(doc110, 47, 48, label="TARIFF"), 
    Span(doc110, 53, 54, label="COUNTRY")] 
docs.append(doc110)


doc111 = nlp('''Purchase order number: N SR-1-06 1847
12800 60 РС 6100069209 (*) 5,32 1 РС 319,20

QRC-HS-10-M-08S-B-W66
HS08-2-S0816

packed per each item

Product description: coupling

Export - Customs tariff no.: 84812010
Country of origin: Germany''')
#doc111SR-1-06 1847 12800 60 6100069209 5,32 1  84812010 Germany
print("doc111",doc111[5: 8], doc111[8: 9], doc111[10: 11], doc111[11: 12], doc111[13: 14], doc111[17:18], doc111[18:19] ,doc111[20:21], doc111[55: 56], doc111[61: 62]) 
doc111.ents = [Span(doc111, 5, 8, label="CONTRACT"), 
    Span(doc111, 8, 9, label="CONTRACT1"), 
    Span(doc111, 10, 11, label="POS"), 
    Span(doc111, 11, 12, label="AMOUNT"), 
    Span(doc111, 13, 14, label="ARTICLE"), 
    Span(doc111, 17, 18, label="PRICE"), 
    Span(doc111, 18, 19, label="UNIT"), 
    Span(doc111, 20, 21, label="SUM"), 
    Span(doc111, 55, 56, label="TARIFF"), 
    Span(doc111, 61, 62, label="COUNTRY")] 
docs.append(doc111)


doc112 = nlp('''Purchase order number: N SR-1-06 1848
12900 4 РС 1020023685 (*) 156,60 1 РС 626,40

SE-130-H-10-B/4

SE-130H10B/4

packed per each item

Product description: filter element
Export - Customs tariff no.: 84219990
Country of origin: Germany''')
#doc112SR-1-06 1848 12900 4 1020023685 156,60 1  84219990 Germany
print("doc112",doc112[5: 8], doc112[8: 9], doc112[10: 11], doc112[11: 12], doc112[13: 14], doc112[17:18], doc112[18:19] ,doc112[20:21], doc112[48: 49], doc112[54: 55]) 
doc112.ents = [Span(doc112, 5, 8, label="CONTRACT"), 
    Span(doc112, 8, 9, label="CONTRACT1"), 
    Span(doc112, 10, 11, label="POS"), 
    Span(doc112, 11, 12, label="AMOUNT"), 
    Span(doc112, 13, 14, label="ARTICLE"), 
    Span(doc112, 17, 18, label="PRICE"), 
    Span(doc112, 18, 19, label="UNIT"), 
    Span(doc112, 20, 21, label="SUM"), 
    Span(doc112, 48, 49, label="TARIFF"), 
    Span(doc112, 54, 55, label="COUNTRY")] 
docs.append(doc112)


doc113 = nlp('''Purchase order number: N SR-1-06 1849
13000 25 PC 1930000207 0,07 1 РС 1,75
SRF-08-PP

packed per each item

Product description: seal

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc113SR-1-06 1849 13000 25 1930000207 0,07 1  39269097 Germany
print("doc113",doc113[5: 8], doc113[8: 9], doc113[10: 11], doc113[11: 12], doc113[13: 14], doc113[14:15], doc113[15:16] ,doc113[17:18], doc113[40: 41], doc113[46: 47]) 
doc113.ents = [Span(doc113, 5, 8, label="CONTRACT"), 
    Span(doc113, 8, 9, label="CONTRACT1"), 
    Span(doc113, 10, 11, label="POS"), 
    Span(doc113, 11, 12, label="AMOUNT"), 
    Span(doc113, 13, 14, label="ARTICLE"), 
    Span(doc113, 14, 15, label="PRICE"), 
    Span(doc113, 15, 16, label="UNIT"), 
    Span(doc113, 17, 18, label="SUM"), 
    Span(doc113, 40, 41, label="TARIFF"), 
    Span(doc113, 46, 47, label="COUNTRY")] 
docs.append(doc113)


doc114 = nlp('''Purchase order number: N SR-1-06 1850
13100 50 РС 1130005333 21,69 100 РС 10,85
216-PP
216 PP

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc114SR-1-06 1850 13100 50 1130005333 21,69 100  39269097 Germany
print("doc114",doc114[5: 8], doc114[8: 9], doc114[10: 11], doc114[11: 12], doc114[13: 14], doc114[14:15], doc114[15:16] ,doc114[17:18], doc114[44: 45], doc114[50: 51]) 
doc114.ents = [Span(doc114, 5, 8, label="CONTRACT"), 
    Span(doc114, 8, 9, label="CONTRACT1"), 
    Span(doc114, 10, 11, label="POS"), 
    Span(doc114, 11, 12, label="AMOUNT"), 
    Span(doc114, 13, 14, label="ARTICLE"), 
    Span(doc114, 14, 15, label="PRICE"), 
    Span(doc114, 15, 16, label="UNIT"), 
    Span(doc114, 17, 18, label="SUM"), 
    Span(doc114, 44, 45, label="TARIFF"), 
    Span(doc114, 50, 51, label="COUNTRY")] 
docs.append(doc114)


doc115 = nlp('''Purchase order number: N SR-1-06 1850
13200 50 РС 1120001256 176,78 100 PC 88,39
SPV-2-M-W4
SPV 2 М W4

packed per each item

Product description: weld plate

Export - Customs tariff no.: 73269098
Country of origin: Germany''')
#doc115SR-1-06 1850 13200 50 1120001256 176,78 100  73269098 Germany
print("doc115",doc115[5: 8], doc115[8: 9], doc115[10: 11], doc115[11: 12], doc115[13: 14], doc115[14:15], doc115[15:16] ,doc115[17:18], doc115[48: 49], doc115[54: 55]) 
doc115.ents = [Span(doc115, 5, 8, label="CONTRACT"), 
    Span(doc115, 8, 9, label="CONTRACT1"), 
    Span(doc115, 10, 11, label="POS"), 
    Span(doc115, 11, 12, label="AMOUNT"), 
    Span(doc115, 13, 14, label="ARTICLE"), 
    Span(doc115, 14, 15, label="PRICE"), 
    Span(doc115, 15, 16, label="UNIT"), 
    Span(doc115, 17, 18, label="SUM"), 
    Span(doc115, 48, 49, label="TARIFF"), 
    Span(doc115, 54, 55, label="COUNTRY")] 
docs.append(doc115)


doc116 = nlp('''Purchase order number: N SR-1-06 1851
13300 25 РС 1120001230 30,47 100 РС 7,62
SPV-2-M-W2
SPV 2 M W2

packed per each item

Product description: weld plate

Export - Customs tariff no.: 73269098
Country of origin: Germany''')
#doc116SR-1-06 1851 13300 25 1120001230 30,47 100  73269098 Germany
print("doc116",doc116[5: 8], doc116[8: 9], doc116[10: 11], doc116[11: 12], doc116[13: 14], doc116[14:15], doc116[15:16] ,doc116[17:18], doc116[48: 49], doc116[54: 55]) 
doc116.ents = [Span(doc116, 5, 8, label="CONTRACT"), 
    Span(doc116, 8, 9, label="CONTRACT1"), 
    Span(doc116, 10, 11, label="POS"), 
    Span(doc116, 11, 12, label="AMOUNT"), 
    Span(doc116, 13, 14, label="ARTICLE"), 
    Span(doc116, 14, 15, label="PRICE"), 
    Span(doc116, 15, 16, label="UNIT"), 
    Span(doc116, 17, 18, label="SUM"), 
    Span(doc116, 48, 49, label="TARIFF"), 
    Span(doc116, 54, 55, label="COUNTRY")] 
docs.append(doc116)


doc117 = nlp('''Purchase order number: N SR-1-06 1854
13400 27 РС 6100068634 (*) 47,20 1 РС 1.274,40
QRC-FT-19-F-G12-BT-W3
FT19-1-IGF12

packed per each item
Export - Customs tariff no.: 84812010
Country of origin: Germany''')
#doc117SR-1-06 1854 13400 27 6100068634 47,20 1  84812010 Germany
print("doc117",doc117[5: 8], doc117[8: 9], doc117[10: 11], doc117[11: 12], doc117[13: 14], doc117[17:18], doc117[18:19] ,doc117[20:21], doc117[52: 53], doc117[58: 59]) 
doc117.ents = [Span(doc117, 5, 8, label="CONTRACT"), 
    Span(doc117, 8, 9, label="CONTRACT1"), 
    Span(doc117, 10, 11, label="POS"), 
    Span(doc117, 11, 12, label="AMOUNT"), 
    Span(doc117, 13, 14, label="ARTICLE"), 
    Span(doc117, 17, 18, label="PRICE"), 
    Span(doc117, 18, 19, label="UNIT"), 
    Span(doc117, 20, 21, label="SUM"), 
    Span(doc117, 52, 53, label="TARIFF"), 
    Span(doc117, 58, 59, label="COUNTRY")] 
docs.append(doc117)


doc118 = nlp('''Purchase order number: N SR-1-06 1854
13500 22 PC 6100068643 (*) 61,74 1 РС 1.358,28
QRC-FT-19-M-G12-BT-W3
FT19-2-IGF12
packed per each item
Export - Customs tariff no.: 84812010
Country of origin: Germany''')
#doc118SR-1-06 1854 13500 22 6100068643 61,74 1  84812010 Germany
print("doc118",doc118[5: 8], doc118[8: 9], doc118[10: 11], doc118[11: 12], doc118[13: 14], doc118[17:18], doc118[18:19] ,doc118[20:21], doc118[52: 53], doc118[58: 59]) 
doc118.ents = [Span(doc118, 5, 8, label="CONTRACT"), 
    Span(doc118, 8, 9, label="CONTRACT1"), 
    Span(doc118, 10, 11, label="POS"), 
    Span(doc118, 11, 12, label="AMOUNT"), 
    Span(doc118, 13, 14, label="ARTICLE"), 
    Span(doc118, 17, 18, label="PRICE"), 
    Span(doc118, 18, 19, label="UNIT"), 
    Span(doc118, 20, 21, label="SUM"), 
    Span(doc118, 52, 53, label="TARIFF"), 
    Span(doc118, 58, 59, label="COUNTRY")] 
docs.append(doc118)


doc119 = nlp('''Purchase order number: N SR-1-06 1854
13600 27 РС 6100038404 19,68 1 РС 531,36
QRC-FT-19-DF-46-W89-SI
ЕТ19-9-$1001

packed per each item
Export - Customs tariff no.: 76090000
Country of origin: China''')
#doc119SR-1-06 1854 13600 27 6100038404 19,68 1  76090000 China
print("doc119",doc119[5: 8], doc119[8: 9], doc119[10: 11], doc119[11: 12], doc119[13: 14], doc119[14:15], doc119[15:16] ,doc119[17:18], doc119[45: 46], doc119[51: 52]) 
doc119.ents = [Span(doc119, 5, 8, label="CONTRACT"), 
    Span(doc119, 8, 9, label="CONTRACT1"), 
    Span(doc119, 10, 11, label="POS"), 
    Span(doc119, 11, 12, label="AMOUNT"), 
    Span(doc119, 13, 14, label="ARTICLE"), 
    Span(doc119, 14, 15, label="PRICE"), 
    Span(doc119, 15, 16, label="UNIT"), 
    Span(doc119, 17, 18, label="SUM"), 
    Span(doc119, 45, 46, label="TARIFF"), 
    Span(doc119, 51, 52, label="COUNTRY")] 
docs.append(doc119)


doc120 = nlp('''Purchase order number: N SR-1-06 1854
13700 27 РС 6100038403 19,68 1 РС 531,36
QRC-FT-19-DM-46-W89-SI
ЕТ19-0-$1001
packed per each item
Export - Customs tariff no.: 76090000
Country of origin: China''')
#doc120SR-1-06 1854 13700 27 6100038403 19,68 1  76090000 China
print("doc120",doc120[5: 8], doc120[8: 9], doc120[10: 11], doc120[11: 12], doc120[13: 14], doc120[14:15], doc120[15:16] ,doc120[17:18], doc120[45: 46], doc120[51: 52]) 
doc120.ents = [Span(doc120, 5, 8, label="CONTRACT"), 
    Span(doc120, 8, 9, label="CONTRACT1"), 
    Span(doc120, 10, 11, label="POS"), 
    Span(doc120, 11, 12, label="AMOUNT"), 
    Span(doc120, 13, 14, label="ARTICLE"), 
    Span(doc120, 14, 15, label="PRICE"), 
    Span(doc120, 15, 16, label="UNIT"), 
    Span(doc120, 17, 18, label="SUM"), 
    Span(doc120, 45, 46, label="TARIFF"), 
    Span(doc120, 51, 52, label="COUNTRY")] 
docs.append(doc120)


doc121 = nlp('''Purchase order number: N SR-1-06 1855
13800 12 PC 1130004022 4,30 100 PC 0,52

AS-M6x40-DIN931/933-8.8-W3
AS-M6X40-DIN931/933-8.8-W3
packed per each item

Product description: screw

Export - Customs tariff по.: 73181588
Country of origin: Taiwan''')
#doc121SR-1-06 1855 13800 12 1130004022 4,30 100  73181588 Taiwan
print("doc121",doc121[5: 8], doc121[8: 9], doc121[10: 11], doc121[11: 12], doc121[13: 14], doc121[14:15], doc121[15:16] ,doc121[17:18], doc121[56: 57], doc121[62: 63]) 
doc121.ents = [Span(doc121, 5, 8, label="CONTRACT"), 
    Span(doc121, 8, 9, label="CONTRACT1"), 
    Span(doc121, 10, 11, label="POS"), 
    Span(doc121, 11, 12, label="AMOUNT"), 
    Span(doc121, 13, 14, label="ARTICLE"), 
    Span(doc121, 14, 15, label="PRICE"), 
    Span(doc121, 15, 16, label="UNIT"), 
    Span(doc121, 17, 18, label="SUM"), 
    Span(doc121, 56, 57, label="TARIFF"), 
    Span(doc121, 62, 63, label="COUNTRY")] 
docs.append(doc121)


doc122 = nlp('''Purchase order number: N SR-1-06 1855
13900 12 PC 1130004024 5,48 100 PC 0,66

AS-M6x60-DIN931/933-8.8-W3
AS-M6X60-DIN931/933-8.8-W3
packed per each item

Product description: screw

Export - Customs tariff по.: 73181588
Country of origin: Turkey''')
#doc122SR-1-06 1855 13900 12 1130004024 5,48 100  73181588 Turkey
print("doc122",doc122[5: 8], doc122[8: 9], doc122[10: 11], doc122[11: 12], doc122[13: 14], doc122[14:15], doc122[15:16] ,doc122[17:18], doc122[56: 57], doc122[62: 63]) 
doc122.ents = [Span(doc122, 5, 8, label="CONTRACT"), 
    Span(doc122, 8, 9, label="CONTRACT1"), 
    Span(doc122, 10, 11, label="POS"), 
    Span(doc122, 11, 12, label="AMOUNT"), 
    Span(doc122, 13, 14, label="ARTICLE"), 
    Span(doc122, 14, 15, label="PRICE"), 
    Span(doc122, 15, 16, label="UNIT"), 
    Span(doc122, 17, 18, label="SUM"), 
    Span(doc122, 56, 57, label="TARIFF"), 
    Span(doc122, 62, 63, label="COUNTRY")] 
docs.append(doc122)


doc123 = nlp('''Purchase order number: N SR-1-06 1855
14000 10 PC 1130004283 9,19 100 PC 0,92

AS-M8x60-DIN931/933-8.8-W3
AS-M8X60-DIN931/933-8.8-W3
packed per each item

Product description: screw

Export - Customs tariff по.: 73181588
Country of origin: Taiwan''')
#doc123SR-1-06 1855 14000 10 1130004283 9,19 100  73181588 Taiwan
print("doc123",doc123[5: 8], doc123[8: 9], doc123[10: 11], doc123[11: 12], doc123[13: 14], doc123[14:15], doc123[15:16] ,doc123[17:18], doc123[56: 57], doc123[62: 63]) 
doc123.ents = [Span(doc123, 5, 8, label="CONTRACT"), 
    Span(doc123, 8, 9, label="CONTRACT1"), 
    Span(doc123, 10, 11, label="POS"), 
    Span(doc123, 11, 12, label="AMOUNT"), 
    Span(doc123, 13, 14, label="ARTICLE"), 
    Span(doc123, 14, 15, label="PRICE"), 
    Span(doc123, 15, 16, label="UNIT"), 
    Span(doc123, 17, 18, label="SUM"), 
    Span(doc123, 56, 57, label="TARIFF"), 
    Span(doc123, 62, 63, label="COUNTRY")] 
docs.append(doc123)


doc124 = nlp('''Purchase order number: N SR-1-06 1855
14100 25 РС 1130005630 26,77 100 РС 6,69
325-РР
325 РР

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc124SR-1-06 1855 14100 25 1130005630 26,77 100  39269097 Germany
print("doc124",doc124[5: 8], doc124[8: 9], doc124[10: 11], doc124[11: 12], doc124[13: 14], doc124[14:15], doc124[15:16] ,doc124[17:18], doc124[44: 45], doc124[50: 51]) 
doc124.ents = [Span(doc124, 5, 8, label="CONTRACT"), 
    Span(doc124, 8, 9, label="CONTRACT1"), 
    Span(doc124, 10, 11, label="POS"), 
    Span(doc124, 11, 12, label="AMOUNT"), 
    Span(doc124, 13, 14, label="ARTICLE"), 
    Span(doc124, 14, 15, label="PRICE"), 
    Span(doc124, 15, 16, label="UNIT"), 
    Span(doc124, 17, 18, label="SUM"), 
    Span(doc124, 44, 45, label="TARIFF"), 
    Span(doc124, 50, 51, label="COUNTRY")] 
docs.append(doc124)


doc125 = nlp('''Purchase order number: N SR-1-06 1855
14200 10 PC 1130006078 70,50 100 PC 7,05
542/42-PP
542/42 PP

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc125SR-1-06 1855 14200 10 1130006078 70,50 100  39269097 Germany
print("doc125",doc125[5: 8], doc125[8: 9], doc125[10: 11], doc125[11: 12], doc125[13: 14], doc125[14:15], doc125[15:16] ,doc125[17:18], doc125[44: 45], doc125[50: 51]) 
doc125.ents = [Span(doc125, 5, 8, label="CONTRACT"), 
    Span(doc125, 8, 9, label="CONTRACT1"), 
    Span(doc125, 10, 11, label="POS"), 
    Span(doc125, 11, 12, label="AMOUNT"), 
    Span(doc125, 13, 14, label="ARTICLE"), 
    Span(doc125, 14, 15, label="PRICE"), 
    Span(doc125, 15, 16, label="UNIT"), 
    Span(doc125, 17, 18, label="SUM"), 
    Span(doc125, 44, 45, label="TARIFF"), 
    Span(doc125, 50, 51, label="COUNTRY")] 
docs.append(doc125)


doc126 = nlp('''Purchase order number: N SR-1-06 1857
14300 300 PC 1130004169 11,33 100 PC 33,99

AS-M10x45-DIN931/933-8.8-W3
AS-M10X45-DIN931/933-8.8-W3
packed per each item

Product description: screw

Export - Customs tariff по.: 73181588
Country of origin: Croatia''')
#doc126SR-1-06 1857 14300 300 1130004169 11,33 100  73181588 Croatia
print("doc126",doc126[5: 8], doc126[8: 9], doc126[10: 11], doc126[11: 12], doc126[13: 14], doc126[14:15], doc126[15:16] ,doc126[17:18], doc126[56: 57], doc126[62: 63]) 
doc126.ents = [Span(doc126, 5, 8, label="CONTRACT"), 
    Span(doc126, 8, 9, label="CONTRACT1"), 
    Span(doc126, 10, 11, label="POS"), 
    Span(doc126, 11, 12, label="AMOUNT"), 
    Span(doc126, 13, 14, label="ARTICLE"), 
    Span(doc126, 14, 15, label="PRICE"), 
    Span(doc126, 15, 16, label="UNIT"), 
    Span(doc126, 17, 18, label="SUM"), 
    Span(doc126, 56, 57, label="TARIFF"), 
    Span(doc126, 62, 63, label="COUNTRY")] 
docs.append(doc126)


doc127 = nlp('''Purchase order number: N SR-1-06 1857
14400 40 РС 1130005466 45,12 100 РС 18,05
3014-РР
3014 РР

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc127SR-1-06 1857 14400 40 1130005466 45,12 100  39269097 Germany
print("doc127",doc127[5: 8], doc127[8: 9], doc127[10: 11], doc127[11: 12], doc127[13: 14], doc127[14:15], doc127[15:16] ,doc127[17:18], doc127[44: 45], doc127[50: 51]) 
doc127.ents = [Span(doc127, 5, 8, label="CONTRACT"), 
    Span(doc127, 8, 9, label="CONTRACT1"), 
    Span(doc127, 10, 11, label="POS"), 
    Span(doc127, 11, 12, label="AMOUNT"), 
    Span(doc127, 13, 14, label="ARTICLE"), 
    Span(doc127, 14, 15, label="PRICE"), 
    Span(doc127, 15, 16, label="UNIT"), 
    Span(doc127, 17, 18, label="SUM"), 
    Span(doc127, 44, 45, label="TARIFF"), 
    Span(doc127, 50, 51, label="COUNTRY")] 
docs.append(doc127)


doc128 = nlp('''Purchase order number: N SR-1-06 1857
14500 120 PC 1130005479 45,12 100 PC 54,14
3016-PP
3016 PP

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc128SR-1-06 1857 14500 120 1130005479 45,12 100  39269097 Germany
print("doc128",doc128[5: 8], doc128[8: 9], doc128[10: 11], doc128[11: 12], doc128[13: 14], doc128[14:15], doc128[15:16] ,doc128[17:18], doc128[44: 45], doc128[50: 51]) 
doc128.ents = [Span(doc128, 5, 8, label="CONTRACT"), 
    Span(doc128, 8, 9, label="CONTRACT1"), 
    Span(doc128, 10, 11, label="POS"), 
    Span(doc128, 11, 12, label="AMOUNT"), 
    Span(doc128, 13, 14, label="ARTICLE"), 
    Span(doc128, 14, 15, label="PRICE"), 
    Span(doc128, 15, 16, label="UNIT"), 
    Span(doc128, 17, 18, label="SUM"), 
    Span(doc128, 44, 45, label="TARIFF"), 
    Span(doc128, 50, 51, label="COUNTRY")] 
docs.append(doc128)


doc129 = nlp('''Purchase order number: N SR-1-06 1857
14600 60 РС 1130005491 45,12 100 PC 27,07
3018-PP
3018 PP

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc129SR-1-06 1857 14600 60 1130005491 45,12 100  39269097 Germany
print("doc129",doc129[5: 8], doc129[8: 9], doc129[10: 11], doc129[11: 12], doc129[13: 14], doc129[14:15], doc129[15:16] ,doc129[17:18], doc129[44: 45], doc129[50: 51]) 
doc129.ents = [Span(doc129, 5, 8, label="CONTRACT"), 
    Span(doc129, 8, 9, label="CONTRACT1"), 
    Span(doc129, 10, 11, label="POS"), 
    Span(doc129, 11, 12, label="AMOUNT"), 
    Span(doc129, 13, 14, label="ARTICLE"), 
    Span(doc129, 14, 15, label="PRICE"), 
    Span(doc129, 15, 16, label="UNIT"), 
    Span(doc129, 17, 18, label="SUM"), 
    Span(doc129, 44, 45, label="TARIFF"), 
    Span(doc129, 50, 51, label="COUNTRY")] 
docs.append(doc129)


doc130 = nlp('''Purchase order number: N SR-1-06 1857
14700 180 PC 1130002873 33,39 100 PC 60,10
DPAL-3S-W3
DPAL 3 S W3

packed per each item

Product description: cover plate

Export - Customs tariff no.: 73182900
Country of origin: Germany''')
#doc130SR-1-06 1857 14700 180 1130002873 33,39 100  73182900 Germany
print("doc130",doc130[5: 8], doc130[8: 9], doc130[10: 11], doc130[11: 12], doc130[13: 14], doc130[14:15], doc130[15:16] ,doc130[17:18], doc130[46: 47], doc130[52: 53]) 
doc130.ents = [Span(doc130, 5, 8, label="CONTRACT"), 
    Span(doc130, 8, 9, label="CONTRACT1"), 
    Span(doc130, 10, 11, label="POS"), 
    Span(doc130, 11, 12, label="AMOUNT"), 
    Span(doc130, 13, 14, label="ARTICLE"), 
    Span(doc130, 14, 15, label="PRICE"), 
    Span(doc130, 15, 16, label="UNIT"), 
    Span(doc130, 17, 18, label="SUM"), 
    Span(doc130, 46, 47, label="TARIFF"), 
    Span(doc130, 52, 53, label="COUNTRY")] 
docs.append(doc130)


doc131 = nlp('''Purchase order number: N SR-1-06 1857

14800 180 РС 1120001947 66,80 100 РС 120,24
SPAL-3S-M-W2

SPAL 3 S M W2

packed per each item

Product description: weld plate

Export - Customs tariff no.: 73269098
Country of origin: Germany''')
#doc131SR-1-06 1857 14800 180 1120001947 66,80 100  73269098 Germany
print("doc131",doc131[5: 8], doc131[8: 9], doc131[10: 11], doc131[11: 12], doc131[13: 14], doc131[14:15], doc131[15:16] ,doc131[17:18], doc131[49: 50], doc131[55: 56]) 
doc131.ents = [Span(doc131, 5, 8, label="CONTRACT"), 
    Span(doc131, 8, 9, label="CONTRACT1"), 
    Span(doc131, 10, 11, label="POS"), 
    Span(doc131, 11, 12, label="AMOUNT"), 
    Span(doc131, 13, 14, label="ARTICLE"), 
    Span(doc131, 14, 15, label="PRICE"), 
    Span(doc131, 15, 16, label="UNIT"), 
    Span(doc131, 17, 18, label="SUM"), 
    Span(doc131, 49, 50, label="TARIFF"), 
    Span(doc131, 55, 56, label="COUNTRY")] 
docs.append(doc131)


doc132 = nlp('''Purchase order number: N SR-1-06 1857
14900 3 PC 6010001215 (*) 706,83 100 PC 21,20

FI-ES-14S-W159-MS

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc132SR-1-06 1857 14900 3 6010001215 706,83 100  73079910 Germany
print("doc132",doc132[5: 8], doc132[8: 9], doc132[10: 11], doc132[11: 12], doc132[13: 14], doc132[17:18], doc132[18:19] ,doc132[20:21], doc132[47: 48], doc132[53: 54]) 
doc132.ents = [Span(doc132, 5, 8, label="CONTRACT"), 
    Span(doc132, 8, 9, label="CONTRACT1"), 
    Span(doc132, 10, 11, label="POS"), 
    Span(doc132, 11, 12, label="AMOUNT"), 
    Span(doc132, 13, 14, label="ARTICLE"), 
    Span(doc132, 17, 18, label="PRICE"), 
    Span(doc132, 18, 19, label="UNIT"), 
    Span(doc132, 20, 21, label="SUM"), 
    Span(doc132, 47, 48, label="TARIFF"), 
    Span(doc132, 53, 54, label="COUNTRY")] 
docs.append(doc132)


doc133 = nlp('''Purchase order number: N SR-1-06 1857
15000 5 PC 6010001216 (*) 678,92 100 PC 33,95

FI-ES-16S-W159-MS

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc133SR-1-06 1857 15000 5 6010001216 678,92 100  73079910 Germany
print("doc133",doc133[5: 8], doc133[8: 9], doc133[10: 11], doc133[11: 12], doc133[13: 14], doc133[17:18], doc133[18:19] ,doc133[20:21], doc133[47: 48], doc133[53: 54]) 
doc133.ents = [Span(doc133, 5, 8, label="CONTRACT"), 
    Span(doc133, 8, 9, label="CONTRACT1"), 
    Span(doc133, 10, 11, label="POS"), 
    Span(doc133, 11, 12, label="AMOUNT"), 
    Span(doc133, 13, 14, label="ARTICLE"), 
    Span(doc133, 17, 18, label="PRICE"), 
    Span(doc133, 18, 19, label="UNIT"), 
    Span(doc133, 20, 21, label="SUM"), 
    Span(doc133, 47, 48, label="TARIFF"), 
    Span(doc133, 53, 54, label="COUNTRY")] 
docs.append(doc133)


doc134 = nlp('''Purchase order number: N SR-1-06 1857
15100 7 PC 6010001206 (*) 622,07 100 PC 43,54


Description

FI-ES-18L-W159-MS

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc134SR-1-06 1857 15100 7 6010001206 622,07 100  73079910 Germany
print("doc134",doc134[5: 8], doc134[8: 9], doc134[10: 11], doc134[11: 12], doc134[13: 14], doc134[17:18], doc134[18:19] ,doc134[20:21], doc134[49: 50], doc134[55: 56]) 
doc134.ents = [Span(doc134, 5, 8, label="CONTRACT"), 
    Span(doc134, 8, 9, label="CONTRACT1"), 
    Span(doc134, 10, 11, label="POS"), 
    Span(doc134, 11, 12, label="AMOUNT"), 
    Span(doc134, 13, 14, label="ARTICLE"), 
    Span(doc134, 17, 18, label="PRICE"), 
    Span(doc134, 18, 19, label="UNIT"), 
    Span(doc134, 20, 21, label="SUM"), 
    Span(doc134, 49, 50, label="TARIFF"), 
    Span(doc134, 55, 56, label="COUNTRY")] 
docs.append(doc134)


doc135 = nlp('''Purchase order number: N SR-1-06 1857
15200 80 PC 6010000757 (*) 83,52 100 PC 66,82

FI-G-10L-W3-MS

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc135SR-1-06 1857 15200 80 6010000757 83,52 100  73079910 Germany
print("doc135",doc135[5: 8], doc135[8: 9], doc135[10: 11], doc135[11: 12], doc135[13: 14], doc135[17:18], doc135[18:19] ,doc135[20:21], doc135[47: 48], doc135[53: 54]) 
doc135.ents = [Span(doc135, 5, 8, label="CONTRACT"), 
    Span(doc135, 8, 9, label="CONTRACT1"), 
    Span(doc135, 10, 11, label="POS"), 
    Span(doc135, 11, 12, label="AMOUNT"), 
    Span(doc135, 13, 14, label="ARTICLE"), 
    Span(doc135, 17, 18, label="PRICE"), 
    Span(doc135, 18, 19, label="UNIT"), 
    Span(doc135, 20, 21, label="SUM"), 
    Span(doc135, 47, 48, label="TARIFF"), 
    Span(doc135, 53, 54, label="COUNTRY")] 
docs.append(doc135)


doc136 = nlp('''Purchase order number: N SR-1-06 1857
15300 2 РС 6010000816 (*) 484,22 100 PC 9,68

FI-G-16/14S-W3-MS

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc136SR-1-06 1857 15300 2 6010000816 484,22 100  73079910 Germany
print("doc136",doc136[5: 8], doc136[8: 9], doc136[10: 11], doc136[11: 12], doc136[13: 14], doc136[17:18], doc136[18:19] ,doc136[20:21], doc136[47: 48], doc136[53: 54]) 
doc136.ents = [Span(doc136, 5, 8, label="CONTRACT"), 
    Span(doc136, 8, 9, label="CONTRACT1"), 
    Span(doc136, 10, 11, label="POS"), 
    Span(doc136, 11, 12, label="AMOUNT"), 
    Span(doc136, 13, 14, label="ARTICLE"), 
    Span(doc136, 17, 18, label="PRICE"), 
    Span(doc136, 18, 19, label="UNIT"), 
    Span(doc136, 20, 21, label="SUM"), 
    Span(doc136, 47, 48, label="TARIFF"), 
    Span(doc136, 53, 54, label="COUNTRY")] 
docs.append(doc136)


doc137 = nlp('''Purchase order number: N SR-1-06 1857
15400 35 PC 6010000760 (*) 218,60 100 PC 76,51

FI-G-18L-W3-MS
packed per each item
Product description: fitting


Description

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc137SR-1-06 1857 15400 35 6010000760 218,60 100  73079910 Germany
print("doc137",doc137[5: 8], doc137[8: 9], doc137[10: 11], doc137[11: 12], doc137[13: 14], doc137[17:18], doc137[18:19] ,doc137[20:21], doc137[49: 50], doc137[55: 56]) 
doc137.ents = [Span(doc137, 5, 8, label="CONTRACT"), 
    Span(doc137, 8, 9, label="CONTRACT1"), 
    Span(doc137, 10, 11, label="POS"), 
    Span(doc137, 11, 12, label="AMOUNT"), 
    Span(doc137, 13, 14, label="ARTICLE"), 
    Span(doc137, 17, 18, label="PRICE"), 
    Span(doc137, 18, 19, label="UNIT"), 
    Span(doc137, 20, 21, label="SUM"), 
    Span(doc137, 49, 50, label="TARIFF"), 
    Span(doc137, 55, 56, label="COUNTRY")] 
docs.append(doc137)


doc138 = nlp('''Purchase order number: N SR-1-06 1857
15500 5 PC 6010008915 (*) 728,74 100 PC 36,44

FI-SNV-18L/16S-V-W3-DKO
FI-SNV-18L/16S-B-W3-DKO

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc138SR-1-06 1857 15500 5 6010008915 728,74 100  73079910 Germany
print("doc138",doc138[5: 8], doc138[8: 9], doc138[10: 11], doc138[11: 12], doc138[13: 14], doc138[17:18], doc138[18:19] ,doc138[20:21], doc138[59: 60], doc138[65: 66]) 
doc138.ents = [Span(doc138, 5, 8, label="CONTRACT"), 
    Span(doc138, 8, 9, label="CONTRACT1"), 
    Span(doc138, 10, 11, label="POS"), 
    Span(doc138, 11, 12, label="AMOUNT"), 
    Span(doc138, 13, 14, label="ARTICLE"), 
    Span(doc138, 17, 18, label="PRICE"), 
    Span(doc138, 18, 19, label="UNIT"), 
    Span(doc138, 20, 21, label="SUM"), 
    Span(doc138, 59, 60, label="TARIFF"), 
    Span(doc138, 65, 66, label="COUNTRY")] 
docs.append(doc138)


doc139 = nlp('''Purchase order number: N SR-1-06 1857
15600 2 РС 6010000970 (*) 521,71 100 PC 10,43

FI-T-18L-W3-MS

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc139SR-1-06 1857 15600 2 6010000970 521,71 100  73079910 Germany
print("doc139",doc139[5: 8], doc139[8: 9], doc139[10: 11], doc139[11: 12], doc139[13: 14], doc139[17:18], doc139[18:19] ,doc139[20:21], doc139[47: 48], doc139[53: 54]) 
doc139.ents = [Span(doc139, 5, 8, label="CONTRACT"), 
    Span(doc139, 8, 9, label="CONTRACT1"), 
    Span(doc139, 10, 11, label="POS"), 
    Span(doc139, 11, 12, label="AMOUNT"), 
    Span(doc139, 13, 14, label="ARTICLE"), 
    Span(doc139, 17, 18, label="PRICE"), 
    Span(doc139, 18, 19, label="UNIT"), 
    Span(doc139, 20, 21, label="SUM"), 
    Span(doc139, 47, 48, label="TARIFF"), 
    Span(doc139, 53, 54, label="COUNTRY")] 
docs.append(doc139)


doc140 = nlp('''Purchase order number: N SR-1-06 1858
15700 100 PC 1130004169 11,33 100 PC 11,33

AS-M10x45-DIN931/933-8.8-W3
AS-M10X45-DIN931/933-8.8-W3
packed per each item

Product description: screw

Export - Customs tariff по.: 73181588


Description

Country of origin: Croatia''')
#doc140SR-1-06 1858 15700 100 1130004169 11,33 100  73181588 Croatia
print("doc140",doc140[5: 8], doc140[8: 9], doc140[10: 11], doc140[11: 12], doc140[13: 14], doc140[14:15], doc140[15:16] ,doc140[17:18], doc140[56: 57], doc140[64: 65]) 
doc140.ents = [Span(doc140, 5, 8, label="CONTRACT"), 
    Span(doc140, 8, 9, label="CONTRACT1"), 
    Span(doc140, 10, 11, label="POS"), 
    Span(doc140, 11, 12, label="AMOUNT"), 
    Span(doc140, 13, 14, label="ARTICLE"), 
    Span(doc140, 14, 15, label="PRICE"), 
    Span(doc140, 15, 16, label="UNIT"), 
    Span(doc140, 17, 18, label="SUM"), 
    Span(doc140, 56, 57, label="TARIFF"), 
    Span(doc140, 64, 65, label="COUNTRY")] 
docs.append(doc140)


doc141 = nlp('''Purchase order number: N SR-1-06 1858
15800 360 PC 1130004170 13,10 100 PC 47,16

AS-M10x60-DIN931/933-8.8-W3
AS-M10X60-DIN931/933-8.8-W3
packed per each item

Product description: screw

Export - Customs tariff по.: 73181588
Country of origin: Origin''')
#doc141SR-1-06 1858 15800 360 1130004170 13,10 100  73181588 Origin
print("doc141",doc141[5: 8], doc141[8: 9], doc141[10: 11], doc141[11: 12], doc141[13: 14], doc141[14:15], doc141[15:16] ,doc141[17:18], doc141[56: 57], doc141[62: 63]) 
doc141.ents = [Span(doc141, 5, 8, label="CONTRACT"), 
    Span(doc141, 8, 9, label="CONTRACT1"), 
    Span(doc141, 10, 11, label="POS"), 
    Span(doc141, 11, 12, label="AMOUNT"), 
    Span(doc141, 13, 14, label="ARTICLE"), 
    Span(doc141, 14, 15, label="PRICE"), 
    Span(doc141, 15, 16, label="UNIT"), 
    Span(doc141, 17, 18, label="SUM"), 
    Span(doc141, 56, 57, label="TARIFF"), 
    Span(doc141, 62, 63, label="COUNTRY")] 
docs.append(doc141)


doc142 = nlp('''Purchase order number: N SR-1-06 1858
15900 50 РС 1130004280 5,08 100 PC 2,54

AS-M8x35-DIN931/933-8.8-W3
AS-M8X35-DIN931/933-8.8-W3
packed per each item

Product description: screw

Export - Customs tariff по.: 73181588
Country of origin: Origin''')
#doc142SR-1-06 1858 15900 50 1130004280 5,08 100  73181588 Origin
print("doc142",doc142[5: 8], doc142[8: 9], doc142[10: 11], doc142[11: 12], doc142[13: 14], doc142[14:15], doc142[15:16] ,doc142[17:18], doc142[56: 57], doc142[62: 63]) 
doc142.ents = [Span(doc142, 5, 8, label="CONTRACT"), 
    Span(doc142, 8, 9, label="CONTRACT1"), 
    Span(doc142, 10, 11, label="POS"), 
    Span(doc142, 11, 12, label="AMOUNT"), 
    Span(doc142, 13, 14, label="ARTICLE"), 
    Span(doc142, 14, 15, label="PRICE"), 
    Span(doc142, 15, 16, label="UNIT"), 
    Span(doc142, 17, 18, label="SUM"), 
    Span(doc142, 56, 57, label="TARIFF"), 
    Span(doc142, 62, 63, label="COUNTRY")] 
docs.append(doc142)


doc143 = nlp('''Purchase order number: N SR-1-06 1858
16000 50 РС 1130005284 28,91 100 РС 14,46
214/14-PP
214/14 PP

packed per each item
Product description: Pipe clamp
Export - Customs tariff no.: 39269097


Description

Country of origin: Germany''')
#doc143SR-1-06 1858 16000 50 1130005284 28,91 100  39269097 Germany
print("doc143",doc143[5: 8], doc143[8: 9], doc143[10: 11], doc143[11: 12], doc143[13: 14], doc143[14:15], doc143[15:16] ,doc143[17:18], doc143[44: 45], doc143[52: 53]) 
doc143.ents = [Span(doc143, 5, 8, label="CONTRACT"), 
    Span(doc143, 8, 9, label="CONTRACT1"), 
    Span(doc143, 10, 11, label="POS"), 
    Span(doc143, 11, 12, label="AMOUNT"), 
    Span(doc143, 13, 14, label="ARTICLE"), 
    Span(doc143, 14, 15, label="PRICE"), 
    Span(doc143, 15, 16, label="UNIT"), 
    Span(doc143, 17, 18, label="SUM"), 
    Span(doc143, 44, 45, label="TARIFF"), 
    Span(doc143, 52, 53, label="COUNTRY")] 
docs.append(doc143)


doc144 = nlp('''Purchase order number: N SR-1-06 1858
16100 20 РС 1130005491 45,12 100 PC 9,02
3018-PP
3018 PP

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc144SR-1-06 1858 16100 20 1130005491 45,12 100  39269097 Germany
print("doc144",doc144[5: 8], doc144[8: 9], doc144[10: 11], doc144[11: 12], doc144[13: 14], doc144[14:15], doc144[15:16] ,doc144[17:18], doc144[44: 45], doc144[50: 51]) 
doc144.ents = [Span(doc144, 5, 8, label="CONTRACT"), 
    Span(doc144, 8, 9, label="CONTRACT1"), 
    Span(doc144, 10, 11, label="POS"), 
    Span(doc144, 11, 12, label="AMOUNT"), 
    Span(doc144, 13, 14, label="ARTICLE"), 
    Span(doc144, 14, 15, label="PRICE"), 
    Span(doc144, 15, 16, label="UNIT"), 
    Span(doc144, 17, 18, label="SUM"), 
    Span(doc144, 44, 45, label="TARIFF"), 
    Span(doc144, 50, 51, label="COUNTRY")] 
docs.append(doc144)


doc145 = nlp('''Purchase order number: N SR-1-06 1858
16200 160 PC 1130005707 58,60 100 PC 93,76
4022-PP
4022 PP

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc145SR-1-06 1858 16200 160 1130005707 58,60 100  39269097 Germany
print("doc145",doc145[5: 8], doc145[8: 9], doc145[10: 11], doc145[11: 12], doc145[13: 14], doc145[14:15], doc145[15:16] ,doc145[17:18], doc145[44: 45], doc145[50: 51]) 
doc145.ents = [Span(doc145, 5, 8, label="CONTRACT"), 
    Span(doc145, 8, 9, label="CONTRACT1"), 
    Span(doc145, 10, 11, label="POS"), 
    Span(doc145, 11, 12, label="AMOUNT"), 
    Span(doc145, 13, 14, label="ARTICLE"), 
    Span(doc145, 14, 15, label="PRICE"), 
    Span(doc145, 15, 16, label="UNIT"), 
    Span(doc145, 17, 18, label="SUM"), 
    Span(doc145, 44, 45, label="TARIFF"), 
    Span(doc145, 50, 51, label="COUNTRY")] 
docs.append(doc145)


doc146 = nlp('''Purchase order number: N SR-1-06 1858
16300 20 РС 1130002873 33,39 100 РС 6,68
DPAL-3S-W3
DPAL 3 S W3

packed per each item
Product description: cover plate
Export - Customs tariff no.: 73182900


Description

Country of origin: Germany''')
#doc146SR-1-06 1858 16300 20 1130002873 33,39 100  73182900 Germany
print("doc146",doc146[5: 8], doc146[8: 9], doc146[10: 11], doc146[11: 12], doc146[13: 14], doc146[14:15], doc146[15:16] ,doc146[17:18], doc146[46: 47], doc146[54: 55]) 
doc146.ents = [Span(doc146, 5, 8, label="CONTRACT"), 
    Span(doc146, 8, 9, label="CONTRACT1"), 
    Span(doc146, 10, 11, label="POS"), 
    Span(doc146, 11, 12, label="AMOUNT"), 
    Span(doc146, 13, 14, label="ARTICLE"), 
    Span(doc146, 14, 15, label="PRICE"), 
    Span(doc146, 15, 16, label="UNIT"), 
    Span(doc146, 17, 18, label="SUM"), 
    Span(doc146, 46, 47, label="TARIFF"), 
    Span(doc146, 54, 55, label="COUNTRY")] 
docs.append(doc146)


doc147 = nlp('''Purchase order number: N SR-1-06 1858
16400 140 PC 1130000711 39,46 100 PC 55,24
DPAL-4S-W3
DPAL 4 S W3

packed per each item

Product description: cover plate

Export - Customs tariff no.: 73182900
Country of origin: Germany''')
#doc147SR-1-06 1858 16400 140 1130000711 39,46 100  73182900 Germany
print("doc147",doc147[5: 8], doc147[8: 9], doc147[10: 11], doc147[11: 12], doc147[13: 14], doc147[14:15], doc147[15:16] ,doc147[17:18], doc147[46: 47], doc147[52: 53]) 
doc147.ents = [Span(doc147, 5, 8, label="CONTRACT"), 
    Span(doc147, 8, 9, label="CONTRACT1"), 
    Span(doc147, 10, 11, label="POS"), 
    Span(doc147, 11, 12, label="AMOUNT"), 
    Span(doc147, 13, 14, label="ARTICLE"), 
    Span(doc147, 14, 15, label="PRICE"), 
    Span(doc147, 15, 16, label="UNIT"), 
    Span(doc147, 17, 18, label="SUM"), 
    Span(doc147, 46, 47, label="TARIFF"), 
    Span(doc147, 52, 53, label="COUNTRY")] 
docs.append(doc147)


doc148 = nlp('''Purchase order number: N SR-1-06 1858
16500 20 РС 1120001947 66,80 100 PC 13,36
SPAL-3S-M-W2

SPAL 3 S M W2

packed per each item

Product description: weld plate

Export - Customs tariff no.: 73269098
Country of origin: Germany''')
#doc148SR-1-06 1858 16500 20 1120001947 66,80 100  73269098 Germany
print("doc148",doc148[5: 8], doc148[8: 9], doc148[10: 11], doc148[11: 12], doc148[13: 14], doc148[14:15], doc148[15:16] ,doc148[17:18], doc148[49: 50], doc148[55: 56]) 
doc148.ents = [Span(doc148, 5, 8, label="CONTRACT"), 
    Span(doc148, 8, 9, label="CONTRACT1"), 
    Span(doc148, 10, 11, label="POS"), 
    Span(doc148, 11, 12, label="AMOUNT"), 
    Span(doc148, 13, 14, label="ARTICLE"), 
    Span(doc148, 14, 15, label="PRICE"), 
    Span(doc148, 15, 16, label="UNIT"), 
    Span(doc148, 17, 18, label="SUM"), 
    Span(doc148, 49, 50, label="TARIFF"), 
    Span(doc148, 55, 56, label="COUNTRY")] 
docs.append(doc148)


doc149 = nlp('''Purchase order number: N SR-1-06 1858
16600 160 PC 1120001950 76,42 100 PC 122,27
SPAL-4S-M-W2

SPAL 4 S M W2

packed per each item

Product description: weld plate

Export - Customs tariff no.: 73269098


Description

Country of origin: Germany''')
#doc149SR-1-06 1858 16600 160 1120001950 76,42 100  73269098 Germany
print("doc149",doc149[5: 8], doc149[8: 9], doc149[10: 11], doc149[11: 12], doc149[13: 14], doc149[14:15], doc149[15:16] ,doc149[17:18], doc149[49: 50], doc149[57: 58]) 
doc149.ents = [Span(doc149, 5, 8, label="CONTRACT"), 
    Span(doc149, 8, 9, label="CONTRACT1"), 
    Span(doc149, 10, 11, label="POS"), 
    Span(doc149, 11, 12, label="AMOUNT"), 
    Span(doc149, 13, 14, label="ARTICLE"), 
    Span(doc149, 14, 15, label="PRICE"), 
    Span(doc149, 15, 16, label="UNIT"), 
    Span(doc149, 17, 18, label="SUM"), 
    Span(doc149, 49, 50, label="TARIFF"), 
    Span(doc149, 57, 58, label="COUNTRY")] 
docs.append(doc149)


doc150 = nlp('''Purchase order number: N SR-1-06 1858
16700 120 PC 6010000756 (*) 71,45 100 PC 85,74

FI-G-08L-W3-MS

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc150SR-1-06 1858 16700 120 6010000756 71,45 100  73079910 Germany
print("doc150",doc150[5: 8], doc150[8: 9], doc150[10: 11], doc150[11: 12], doc150[13: 14], doc150[17:18], doc150[18:19] ,doc150[20:21], doc150[47: 48], doc150[53: 54]) 
doc150.ents = [Span(doc150, 5, 8, label="CONTRACT"), 
    Span(doc150, 8, 9, label="CONTRACT1"), 
    Span(doc150, 10, 11, label="POS"), 
    Span(doc150, 11, 12, label="AMOUNT"), 
    Span(doc150, 13, 14, label="ARTICLE"), 
    Span(doc150, 17, 18, label="PRICE"), 
    Span(doc150, 18, 19, label="UNIT"), 
    Span(doc150, 20, 21, label="SUM"), 
    Span(doc150, 47, 48, label="TARIFF"), 
    Span(doc150, 53, 54, label="COUNTRY")] 
docs.append(doc150)


doc151 = nlp('''Purchase order number: N SR-1-06 1858
16800 35 PC 6010000760 (*) 218,60 100 PC 76,51

FI-G-18L-W3-MS

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc151SR-1-06 1858 16800 35 6010000760 218,60 100  73079910 Germany
print("doc151",doc151[5: 8], doc151[8: 9], doc151[10: 11], doc151[11: 12], doc151[13: 14], doc151[17:18], doc151[18:19] ,doc151[20:21], doc151[47: 48], doc151[53: 54]) 
doc151.ents = [Span(doc151, 5, 8, label="CONTRACT"), 
    Span(doc151, 8, 9, label="CONTRACT1"), 
    Span(doc151, 10, 11, label="POS"), 
    Span(doc151, 11, 12, label="AMOUNT"), 
    Span(doc151, 13, 14, label="ARTICLE"), 
    Span(doc151, 17, 18, label="PRICE"), 
    Span(doc151, 18, 19, label="UNIT"), 
    Span(doc151, 20, 21, label="SUM"), 
    Span(doc151, 47, 48, label="TARIFF"), 
    Span(doc151, 53, 54, label="COUNTRY")] 
docs.append(doc151)


doc152 = nlp('''Purchase order number: N SR-1-06 1858
16900 75 РС 6010001473 (*) 73,72 100 PC 55,29

FI-GE-10LR-WD-B-W3-MS

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc152SR-1-06 1858 16900 75 6010001473 73,72 100  73079910 Germany
print("doc152",doc152[5: 8], doc152[8: 9], doc152[10: 11], doc152[11: 12], doc152[13: 14], doc152[17:18], doc152[18:19] ,doc152[20:21], doc152[51: 52], doc152[57: 58]) 
doc152.ents = [Span(doc152, 5, 8, label="CONTRACT"), 
    Span(doc152, 8, 9, label="CONTRACT1"), 
    Span(doc152, 10, 11, label="POS"), 
    Span(doc152, 11, 12, label="AMOUNT"), 
    Span(doc152, 13, 14, label="ARTICLE"), 
    Span(doc152, 17, 18, label="PRICE"), 
    Span(doc152, 18, 19, label="UNIT"), 
    Span(doc152, 20, 21, label="SUM"), 
    Span(doc152, 51, 52, label="TARIFF"), 
    Span(doc152, 57, 58, label="COUNTRY")] 
docs.append(doc152)


doc153 = nlp('''Purchase order number: N SR-1-06 1858
17000 3 PC 6010001403 (*) 173,06 100 PC 5,19

FI-GE-18LM18x1.5-WD-B-W3-MS
FI-GE-18LM18x1,5-WD-B-W3-MS
packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc153SR-1-06 1858 17000 3 6010001403 173,06 100  73079910 Germany
print("doc153",doc153[5: 8], doc153[8: 9], doc153[10: 11], doc153[11: 12], doc153[13: 14], doc153[17:18], doc153[18:19] ,doc153[20:21], doc153[63: 64], doc153[69: 70]) 
doc153.ents = [Span(doc153, 5, 8, label="CONTRACT"), 
    Span(doc153, 8, 9, label="CONTRACT1"), 
    Span(doc153, 10, 11, label="POS"), 
    Span(doc153, 11, 12, label="AMOUNT"), 
    Span(doc153, 13, 14, label="ARTICLE"), 
    Span(doc153, 17, 18, label="PRICE"), 
    Span(doc153, 18, 19, label="UNIT"), 
    Span(doc153, 20, 21, label="SUM"), 
    Span(doc153, 63, 64, label="TARIFF"), 
    Span(doc153, 69, 70, label="COUNTRY")] 
docs.append(doc153)


doc154 = nlp('''Purchase order number: N SR-1-06 1858
17100 5 PC 6010000957 (*) 895,25 100 PC 44,76

FI-W-25S-W3-MS

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079290
Country of origin: Germany''')
#doc154SR-1-06 1858 17100 5 6010000957 895,25 100  73079290 Germany
print("doc154",doc154[5: 8], doc154[8: 9], doc154[10: 11], doc154[11: 12], doc154[13: 14], doc154[17:18], doc154[18:19] ,doc154[20:21], doc154[47: 48], doc154[53: 54]) 
doc154.ents = [Span(doc154, 5, 8, label="CONTRACT"), 
    Span(doc154, 8, 9, label="CONTRACT1"), 
    Span(doc154, 10, 11, label="POS"), 
    Span(doc154, 11, 12, label="AMOUNT"), 
    Span(doc154, 13, 14, label="ARTICLE"), 
    Span(doc154, 17, 18, label="PRICE"), 
    Span(doc154, 18, 19, label="UNIT"), 
    Span(doc154, 20, 21, label="SUM"), 
    Span(doc154, 47, 48, label="TARIFF"), 
    Span(doc154, 53, 54, label="COUNTRY")] 
docs.append(doc154)


doc155 = nlp('''Purchase order number: N SR-1-06 1860
17200 4 PC 1020022803 180,76 1 РС 723,04

RE-600-G-10-B/5-NB
RE-600G10B/5-1613

packed per each item

Product description: filter element
Export - Customs tariff no.: 84219990
Country of origin: Germany''')
#doc155SR-1-06 1860 17200 4 1020022803 180,76 1  84219990 Germany
print("doc155",doc155[5: 8], doc155[8: 9], doc155[10: 11], doc155[11: 12], doc155[13: 14], doc155[14:15], doc155[15:16] ,doc155[17:18], doc155[49: 50], doc155[55: 56]) 
doc155.ents = [Span(doc155, 5, 8, label="CONTRACT"), 
    Span(doc155, 8, 9, label="CONTRACT1"), 
    Span(doc155, 10, 11, label="POS"), 
    Span(doc155, 11, 12, label="AMOUNT"), 
    Span(doc155, 13, 14, label="ARTICLE"), 
    Span(doc155, 14, 15, label="PRICE"), 
    Span(doc155, 15, 16, label="UNIT"), 
    Span(doc155, 17, 18, label="SUM"), 
    Span(doc155, 49, 50, label="TARIFF"), 
    Span(doc155, 55, 56, label="COUNTRY")] 
docs.append(doc155)


doc156 = nlp('''Purchase order number: N SR-1-06 1859
17300 1 РС 6010001626 (*) 1.168,93 100 PC 11,69

FI-RV-16S-W3-1-MS
FI-RV-16S-W3-MS-1

packed per each item

Product description: valve

Export - Customs tariff no.: 84813091
Country of origin: Germany''')
#doc156SR-1-06 1859 17300 1 6010001626 1.168,93 100  84813091 Germany
print("doc156",doc156[5: 8], doc156[8: 9], doc156[10: 11], doc156[11: 12], doc156[13: 14], doc156[17:18], doc156[18:19] ,doc156[20:21], doc156[57: 58], doc156[63: 64]) 
doc156.ents = [Span(doc156, 5, 8, label="CONTRACT"), 
    Span(doc156, 8, 9, label="CONTRACT1"), 
    Span(doc156, 10, 11, label="POS"), 
    Span(doc156, 11, 12, label="AMOUNT"), 
    Span(doc156, 13, 14, label="ARTICLE"), 
    Span(doc156, 17, 18, label="PRICE"), 
    Span(doc156, 18, 19, label="UNIT"), 
    Span(doc156, 20, 21, label="SUM"), 
    Span(doc156, 57, 58, label="TARIFF"), 
    Span(doc156, 63, 64, label="COUNTRY")] 
docs.append(doc156)


doc157 = nlp('''Purchase order number: N SR-1-06 1859
17400 20 РС 6010000287 (*) 1.694,89 100 PC 338,98
FI-RV-20S-W3-1

packed per each item

Product description: valve

Export - Customs tariff no.: 84813091
Country of origin: Germany''')
#doc157SR-1-06 1859 17400 20 6010000287 1.694,89 100  84813091 Germany
print("doc157",doc157[5: 8], doc157[8: 9], doc157[10: 11], doc157[11: 12], doc157[13: 14], doc157[17:18], doc157[18:19] ,doc157[20:21], doc157[47: 48], doc157[53: 54]) 
doc157.ents = [Span(doc157, 5, 8, label="CONTRACT"), 
    Span(doc157, 8, 9, label="CONTRACT1"), 
    Span(doc157, 10, 11, label="POS"), 
    Span(doc157, 11, 12, label="AMOUNT"), 
    Span(doc157, 13, 14, label="ARTICLE"), 
    Span(doc157, 17, 18, label="PRICE"), 
    Span(doc157, 18, 19, label="UNIT"), 
    Span(doc157, 20, 21, label="SUM"), 
    Span(doc157, 47, 48, label="TARIFF"), 
    Span(doc157, 53, 54, label="COUNTRY")] 
docs.append(doc157)


doc158 = nlp('''Purchase order number: N SR-1-06 1859
17500 1 PC 6010000280 (*) 3.364,37 100 PC 33,64
FI-RV-42L-W3-1

packed per each item

Product description: valve

Export - Customs tariff no.: 84813091
Country of origin: Germany''')
#doc158SR-1-06 1859 17500 1 6010000280 3.364,37 100  84813091 Germany
print("doc158",doc158[5: 8], doc158[8: 9], doc158[10: 11], doc158[11: 12], doc158[13: 14], doc158[17:18], doc158[18:19] ,doc158[20:21], doc158[47: 48], doc158[53: 54]) 
doc158.ents = [Span(doc158, 5, 8, label="CONTRACT"), 
    Span(doc158, 8, 9, label="CONTRACT1"), 
    Span(doc158, 10, 11, label="POS"), 
    Span(doc158, 11, 12, label="AMOUNT"), 
    Span(doc158, 13, 14, label="ARTICLE"), 
    Span(doc158, 17, 18, label="PRICE"), 
    Span(doc158, 18, 19, label="UNIT"), 
    Span(doc158, 20, 21, label="SUM"), 
    Span(doc158, 47, 48, label="TARIFF"), 
    Span(doc158, 53, 54, label="COUNTRY")] 
docs.append(doc158)


doc159 = nlp('''Purchase order number: N SR-1-06 1859
17600 20 РС 6010000210 (*) 1.088,67 100 PC 217,73

FI-RVV-16SR-WD-B-W3-1

packed per each item

Product description: valve

Export - Customs tariff no.: 84813091
Country of origin: Germany''')
#doc159SR-1-06 1859 17600 20 6010000210 1.088,67 100  84813091 Germany
print("doc159",doc159[5: 8], doc159[8: 9], doc159[10: 11], doc159[11: 12], doc159[13: 14], doc159[17:18], doc159[18:19] ,doc159[20:21], doc159[51: 52], doc159[57: 58]) 
doc159.ents = [Span(doc159, 5, 8, label="CONTRACT"), 
    Span(doc159, 8, 9, label="CONTRACT1"), 
    Span(doc159, 10, 11, label="POS"), 
    Span(doc159, 11, 12, label="AMOUNT"), 
    Span(doc159, 13, 14, label="ARTICLE"), 
    Span(doc159, 17, 18, label="PRICE"), 
    Span(doc159, 18, 19, label="UNIT"), 
    Span(doc159, 20, 21, label="SUM"), 
    Span(doc159, 51, 52, label="TARIFF"), 
    Span(doc159, 57, 58, label="COUNTRY")] 
docs.append(doc159)


doc160 = nlp('''Purchase order number: N SR-1-06 1861
17700 1 РС 1910000191 101,13 1 РС 101,13
DRV-25-B-G
DRV-25-P-B
Flow control valve (in-line mounting)
packed per each item
Product description: valve
Export - Customs tariff no.: 84812010
Country of origin: Germany''')
#doc160SR-1-06 1861 17700 1 1910000191 101,13 1  84812010 Germany
print("doc160",doc160[5: 8], doc160[8: 9], doc160[10: 11], doc160[11: 12], doc160[13: 14], doc160[14:15], doc160[15:16] ,doc160[17:18], doc160[58: 59], doc160[64: 65]) 
doc160.ents = [Span(doc160, 5, 8, label="CONTRACT"), 
    Span(doc160, 8, 9, label="CONTRACT1"), 
    Span(doc160, 10, 11, label="POS"), 
    Span(doc160, 11, 12, label="AMOUNT"), 
    Span(doc160, 13, 14, label="ARTICLE"), 
    Span(doc160, 14, 15, label="PRICE"), 
    Span(doc160, 15, 16, label="UNIT"), 
    Span(doc160, 17, 18, label="SUM"), 
    Span(doc160, 58, 59, label="TARIFF"), 
    Span(doc160, 64, 65, label="COUNTRY")] 
docs.append(doc160)


doc161 = nlp('''Purchase order number: N SR-1-06 1862
17800 100 PC 1130004021 4,09 100 PC 4,09

AS-M6x35-DIN931/933-8.8-W3
AS-M6X35-DIN931/933-8.8-W3
packed per each item

Product description: screw

Export - Customs tariff по.: 73181588


Description

Country of origin: Turkey''')
#doc161SR-1-06 1862 17800 100 1130004021 4,09 100  73181588 Turkey
print("doc161",doc161[5: 8], doc161[8: 9], doc161[10: 11], doc161[11: 12], doc161[13: 14], doc161[14:15], doc161[15:16] ,doc161[17:18], doc161[56: 57], doc161[64: 65]) 
doc161.ents = [Span(doc161, 5, 8, label="CONTRACT"), 
    Span(doc161, 8, 9, label="CONTRACT1"), 
    Span(doc161, 10, 11, label="POS"), 
    Span(doc161, 11, 12, label="AMOUNT"), 
    Span(doc161, 13, 14, label="ARTICLE"), 
    Span(doc161, 14, 15, label="PRICE"), 
    Span(doc161, 15, 16, label="UNIT"), 
    Span(doc161, 17, 18, label="SUM"), 
    Span(doc161, 56, 57, label="TARIFF"), 
    Span(doc161, 64, 65, label="COUNTRY")] 
docs.append(doc161)


doc162 = nlp('''Purchase order number: N SR-1-06 1862
17900 50 PC 1130000261 7,39 100 PC 3,70
DP-2-W3
DP 2 W3

packed per each item

Product description: cover plate

Export - Customs tariff no.: 73269098
Country of origin: Germany''')
#doc162SR-1-06 1862 17900 50 1130000261 7,39 100  73269098 Germany
print("doc162",doc162[5: 8], doc162[8: 9], doc162[10: 11], doc162[11: 12], doc162[13: 14], doc162[14:15], doc162[15:16] ,doc162[17:18], doc162[45: 46], doc162[51: 52]) 
doc162.ents = [Span(doc162, 5, 8, label="CONTRACT"), 
    Span(doc162, 8, 9, label="CONTRACT1"), 
    Span(doc162, 10, 11, label="POS"), 
    Span(doc162, 11, 12, label="AMOUNT"), 
    Span(doc162, 13, 14, label="ARTICLE"), 
    Span(doc162, 14, 15, label="PRICE"), 
    Span(doc162, 15, 16, label="UNIT"), 
    Span(doc162, 17, 18, label="SUM"), 
    Span(doc162, 45, 46, label="TARIFF"), 
    Span(doc162, 51, 52, label="COUNTRY")] 
docs.append(doc162)


doc163 = nlp('''Purchase order number: N SR-1-06 1862
18000 75 РС 1120001230 30,47 100 РС 22,85
SPV-2-M-W2
SPV 2 M W2

packed per each item

Product description: weld plate

Export - Customs tariff no.: 73269098
Country of origin: Germany''')
#doc163SR-1-06 1862 18000 75 1120001230 30,47 100  73269098 Germany
print("doc163",doc163[5: 8], doc163[8: 9], doc163[10: 11], doc163[11: 12], doc163[13: 14], doc163[14:15], doc163[15:16] ,doc163[17:18], doc163[48: 49], doc163[54: 55]) 
doc163.ents = [Span(doc163, 5, 8, label="CONTRACT"), 
    Span(doc163, 8, 9, label="CONTRACT1"), 
    Span(doc163, 10, 11, label="POS"), 
    Span(doc163, 11, 12, label="AMOUNT"), 
    Span(doc163, 13, 14, label="ARTICLE"), 
    Span(doc163, 14, 15, label="PRICE"), 
    Span(doc163, 15, 16, label="UNIT"), 
    Span(doc163, 17, 18, label="SUM"), 
    Span(doc163, 48, 49, label="TARIFF"), 
    Span(doc163, 54, 55, label="COUNTRY")] 
docs.append(doc163)


doc164 = nlp('''Purchase order number: N SR-1-06 1864
18100 3 PC 1920000044 (*) 46,16 1 РС 138,48

TS-SNA/SNK-O-60

packed per each item

Product description: temperature switch
Export - Customs tariff no.: 85437090
Country of origin: Germany''')
#doc164SR-1-06 1864 18100 3 1920000044 46,16 1  85437090 Germany
print("doc164",doc164[5: 8], doc164[8: 9], doc164[10: 11], doc164[11: 12], doc164[13: 14], doc164[17:18], doc164[18:19] ,doc164[20:21], doc164[48: 49], doc164[54: 55]) 
doc164.ents = [Span(doc164, 5, 8, label="CONTRACT"), 
    Span(doc164, 8, 9, label="CONTRACT1"), 
    Span(doc164, 10, 11, label="POS"), 
    Span(doc164, 11, 12, label="AMOUNT"), 
    Span(doc164, 13, 14, label="ARTICLE"), 
    Span(doc164, 17, 18, label="PRICE"), 
    Span(doc164, 18, 19, label="UNIT"), 
    Span(doc164, 20, 21, label="SUM"), 
    Span(doc164, 48, 49, label="TARIFF"), 
    Span(doc164, 54, 55, label="COUNTRY")] 
docs.append(doc164)


doc165 = nlp('''Purchase order number: N SR-1-06 1863
18200 20 PC 1910000919 15,54 1 РС 310,80

SUS-102-G32-200-125-P-B0.2
SUS-P-102-B32F-200-125-3

packed per each item

Product description: suction strainer
Export - Customs tariff по.: 84212980
Country of origin: China''')
#doc165SR-1-06 1863 18200 20 1910000919 15,54 1  84212980 China
print("doc165",doc165[5: 8], doc165[8: 9], doc165[10: 11], doc165[11: 12], doc165[13: 14], doc165[14:15], doc165[15:16] ,doc165[17:18], doc165[59: 60], doc165[65: 66]) 
doc165.ents = [Span(doc165, 5, 8, label="CONTRACT"), 
    Span(doc165, 8, 9, label="CONTRACT1"), 
    Span(doc165, 10, 11, label="POS"), 
    Span(doc165, 11, 12, label="AMOUNT"), 
    Span(doc165, 13, 14, label="ARTICLE"), 
    Span(doc165, 14, 15, label="PRICE"), 
    Span(doc165, 15, 16, label="UNIT"), 
    Span(doc165, 17, 18, label="SUM"), 
    Span(doc165, 59, 60, label="TARIFF"), 
    Span(doc165, 65, 66, label="COUNTRY")] 
docs.append(doc165)



doc167 = nlp('''Purchase order number: N SR-1-06 1867
18400 240 РС 1130004022 4,30 100 PC 10,32

AS-M6x40-DIN931/933-8.8-W3
AS-M6X40-DIN931/933-8.8-W3
packed per each item

Product description: screw

Export - Customs tariff по.: 73181588
Country of origin: Taiwan''')
#doc167SR-1-06 1867 18400 240 1130004022 4,30 100  73181588 Taiwan
print("doc167",doc167[5: 8], doc167[8: 9], doc167[10: 11], doc167[11: 12], doc167[13: 14], doc167[14:15], doc167[15:16] ,doc167[17:18], doc167[56: 57], doc167[62: 63]) 
doc167.ents = [Span(doc167, 5, 8, label="CONTRACT"), 
    Span(doc167, 8, 9, label="CONTRACT1"), 
    Span(doc167, 10, 11, label="POS"), 
    Span(doc167, 11, 12, label="AMOUNT"), 
    Span(doc167, 13, 14, label="ARTICLE"), 
    Span(doc167, 14, 15, label="PRICE"), 
    Span(doc167, 15, 16, label="UNIT"), 
    Span(doc167, 17, 18, label="SUM"), 
    Span(doc167, 56, 57, label="TARIFF"), 
    Span(doc167, 62, 63, label="COUNTRY")] 
docs.append(doc167)


doc168 = nlp('''Purchase order number: N SR-1-06 1867
18500 240 PC 6100152347 12,73 100 PC 30,55

SM-1-8/1D-M-W3/2

packed per each item

Customer ID-No.: 000000001120001932
Product description: nuts

Export - Customs tariff no.: 73181692
Country of origin: Germany''')
#doc168SR-1-06 1867 18500 240 6100152347 12,73 100  73181692 Germany
print("doc168",doc168[5: 8], doc168[8: 9], doc168[10: 11], doc168[11: 12], doc168[13: 14], doc168[14:15], doc168[15:16] ,doc168[17:18], doc168[52: 53], doc168[58: 59]) 
doc168.ents = [Span(doc168, 5, 8, label="CONTRACT"), 
    Span(doc168, 8, 9, label="CONTRACT1"), 
    Span(doc168, 10, 11, label="POS"), 
    Span(doc168, 11, 12, label="AMOUNT"), 
    Span(doc168, 13, 14, label="ARTICLE"), 
    Span(doc168, 14, 15, label="PRICE"), 
    Span(doc168, 15, 16, label="UNIT"), 
    Span(doc168, 17, 18, label="SUM"), 
    Span(doc168, 52, 53, label="TARIFF"), 
    Span(doc168, 58, 59, label="COUNTRY")] 
docs.append(doc168)


doc169 = nlp('''Purchase order number: N SR-1-06 1867
18600 125 PC 1130005533 41,59 100 PC 51,99
320-РА
320 РА

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc169SR-1-06 1867 18600 125 1130005533 41,59 100  39269097 Germany
print("doc169",doc169[5: 8], doc169[8: 9], doc169[10: 11], doc169[11: 12], doc169[13: 14], doc169[14:15], doc169[15:16] ,doc169[17:18], doc169[44: 45], doc169[50: 51]) 
doc169.ents = [Span(doc169, 5, 8, label="CONTRACT"), 
    Span(doc169, 8, 9, label="CONTRACT1"), 
    Span(doc169, 10, 11, label="POS"), 
    Span(doc169, 11, 12, label="AMOUNT"), 
    Span(doc169, 13, 14, label="ARTICLE"), 
    Span(doc169, 14, 15, label="PRICE"), 
    Span(doc169, 15, 16, label="UNIT"), 
    Span(doc169, 17, 18, label="SUM"), 
    Span(doc169, 44, 45, label="TARIFF"), 
    Span(doc169, 50, 51, label="COUNTRY")] 
docs.append(doc169)


doc170 = nlp('''Purchase order number: N SR-1-06 1867
18700 50 РС 6010000761 (*) 296,82 100 PC 148,41

FI-G-22L-W3-MS

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc170SR-1-06 1867 18700 50 6010000761 296,82 100  73079910 Germany
print("doc170",doc170[5: 8], doc170[8: 9], doc170[10: 11], doc170[11: 12], doc170[13: 14], doc170[17:18], doc170[18:19] ,doc170[20:21], doc170[47: 48], doc170[53: 54]) 
doc170.ents = [Span(doc170, 5, 8, label="CONTRACT"), 
    Span(doc170, 8, 9, label="CONTRACT1"), 
    Span(doc170, 10, 11, label="POS"), 
    Span(doc170, 11, 12, label="AMOUNT"), 
    Span(doc170, 13, 14, label="ARTICLE"), 
    Span(doc170, 17, 18, label="PRICE"), 
    Span(doc170, 18, 19, label="UNIT"), 
    Span(doc170, 20, 21, label="SUM"), 
    Span(doc170, 47, 48, label="TARIFF"), 
    Span(doc170, 53, 54, label="COUNTRY")] 
docs.append(doc170)


doc171 = nlp('''Purchase order number: N SR-1-06 1867
18800 60 РС 6010000762 (*) 535,56 100 PC 321,34

FI-G-28L-W3-MS

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc171SR-1-06 1867 18800 60 6010000762 535,56 100  73079910 Germany
print("doc171",doc171[5: 8], doc171[8: 9], doc171[10: 11], doc171[11: 12], doc171[13: 14], doc171[17:18], doc171[18:19] ,doc171[20:21], doc171[47: 48], doc171[53: 54]) 
doc171.ents = [Span(doc171, 5, 8, label="CONTRACT"), 
    Span(doc171, 8, 9, label="CONTRACT1"), 
    Span(doc171, 10, 11, label="POS"), 
    Span(doc171, 11, 12, label="AMOUNT"), 
    Span(doc171, 13, 14, label="ARTICLE"), 
    Span(doc171, 17, 18, label="PRICE"), 
    Span(doc171, 18, 19, label="UNIT"), 
    Span(doc171, 20, 21, label="SUM"), 
    Span(doc171, 47, 48, label="TARIFF"), 
    Span(doc171, 53, 54, label="COUNTRY")] 
docs.append(doc171)


doc172 = nlp('''Purchase order number: N SR-1-06 1867
18900 50 РС 6010001526 (*) 91,05 100 PC 45,53

FI-GE-1 0LR3/8-WD-B-W3-MS

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc172SR-1-06 1867 18900 50 6010001526 91,05 100  73079910 Germany
print("doc172",doc172[5: 8], doc172[8: 9], doc172[10: 11], doc172[11: 12], doc172[13: 14], doc172[17:18], doc172[18:19] ,doc172[20:21], doc172[52: 53], doc172[58: 59]) 
doc172.ents = [Span(doc172, 5, 8, label="CONTRACT"), 
    Span(doc172, 8, 9, label="CONTRACT1"), 
    Span(doc172, 10, 11, label="POS"), 
    Span(doc172, 11, 12, label="AMOUNT"), 
    Span(doc172, 13, 14, label="ARTICLE"), 
    Span(doc172, 17, 18, label="PRICE"), 
    Span(doc172, 18, 19, label="UNIT"), 
    Span(doc172, 20, 21, label="SUM"), 
    Span(doc172, 52, 53, label="TARIFF"), 
    Span(doc172, 58, 59, label="COUNTRY")] 
docs.append(doc172)


doc173 = nlp('''Purchase order number: N SR-1-06 1867
19000 100 PC 6010001477 (*) 128,05 100 PC 128,05

FI-GE-15LR-WD-B-W3-MS

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc173SR-1-06 1867 19000 100 6010001477 128,05 100  73079910 Germany
print("doc173",doc173[5: 8], doc173[8: 9], doc173[10: 11], doc173[11: 12], doc173[13: 14], doc173[17:18], doc173[18:19] ,doc173[20:21], doc173[51: 52], doc173[57: 58]) 
doc173.ents = [Span(doc173, 5, 8, label="CONTRACT"), 
    Span(doc173, 8, 9, label="CONTRACT1"), 
    Span(doc173, 10, 11, label="POS"), 
    Span(doc173, 11, 12, label="AMOUNT"), 
    Span(doc173, 13, 14, label="ARTICLE"), 
    Span(doc173, 17, 18, label="PRICE"), 
    Span(doc173, 18, 19, label="UNIT"), 
    Span(doc173, 20, 21, label="SUM"), 
    Span(doc173, 51, 52, label="TARIFF"), 
    Span(doc173, 57, 58, label="COUNTRY")] 
docs.append(doc173)


doc175 = nlp('''Purchase order number: N SR-1-06 1867
19200 40 РС 6010000944 (*) 277,71 100 PC 111,08

FI-W-15L-W3-MS

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079290
Country of origin: Germany''')
#doc175SR-1-06 1867 19200 40 6010000944 277,71 100  73079290 Germany
print("doc175",doc175[5: 8], doc175[8: 9], doc175[10: 11], doc175[11: 12], doc175[13: 14], doc175[17:18], doc175[18:19] ,doc175[20:21], doc175[47: 48], doc175[53: 54]) 
doc175.ents = [Span(doc175, 5, 8, label="CONTRACT"), 
    Span(doc175, 8, 9, label="CONTRACT1"), 
    Span(doc175, 10, 11, label="POS"), 
    Span(doc175, 11, 12, label="AMOUNT"), 
    Span(doc175, 13, 14, label="ARTICLE"), 
    Span(doc175, 17, 18, label="PRICE"), 
    Span(doc175, 18, 19, label="UNIT"), 
    Span(doc175, 20, 21, label="SUM"), 
    Span(doc175, 47, 48, label="TARIFF"), 
    Span(doc175, 53, 54, label="COUNTRY")] 
docs.append(doc175)


doc176 = nlp('''Purchase order number: N SR-1-06 1867
19300 30 PC 6010001167 (*) 413,80 100 PC 124,14

FI-WS-15L-W3-OGR-SKM-MS

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079290
Country of origin: Germany''')
#doc176SR-1-06 1867 19300 30 6010001167 413,80 100  73079290 Germany
print("doc176",doc176[5: 8], doc176[8: 9], doc176[10: 11], doc176[11: 12], doc176[13: 14], doc176[17:18], doc176[18:19] ,doc176[20:21], doc176[51: 52], doc176[57: 58]) 
doc176.ents = [Span(doc176, 5, 8, label="CONTRACT"), 
    Span(doc176, 8, 9, label="CONTRACT1"), 
    Span(doc176, 10, 11, label="POS"), 
    Span(doc176, 11, 12, label="AMOUNT"), 
    Span(doc176, 13, 14, label="ARTICLE"), 
    Span(doc176, 17, 18, label="PRICE"), 
    Span(doc176, 18, 19, label="UNIT"), 
    Span(doc176, 20, 21, label="SUM"), 
    Span(doc176, 51, 52, label="TARIFF"), 
    Span(doc176, 57, 58, label="COUNTRY")] 
docs.append(doc176)


doc177 = nlp('''Purchase order number: N SR-1-06 1868
19400 25 PC 1930000207 0,07 1 РС 1,75
SRF-08-PP

packed per each item


Description

Product description: seal
Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc177SR-1-06 1868 19400 25 1930000207 0,07 1  39269097 Germany
print("doc177",doc177[5: 8], doc177[8: 9], doc177[10: 11], doc177[11: 12], doc177[13: 14], doc177[14:15], doc177[15:16] ,doc177[17:18], doc177[42: 43], doc177[48: 49]) 
doc177.ents = [Span(doc177, 5, 8, label="CONTRACT"), 
    Span(doc177, 8, 9, label="CONTRACT1"), 
    Span(doc177, 10, 11, label="POS"), 
    Span(doc177, 11, 12, label="AMOUNT"), 
    Span(doc177, 13, 14, label="ARTICLE"), 
    Span(doc177, 14, 15, label="PRICE"), 
    Span(doc177, 15, 16, label="UNIT"), 
    Span(doc177, 17, 18, label="SUM"), 
    Span(doc177, 42, 43, label="TARIFF"), 
    Span(doc177, 48, 49, label="COUNTRY")] 
docs.append(doc177)


doc178 = nlp('''Purchase order number: N SR-1-06 1868
19500 50 РС 1130005264 52,17 100 РС 26,09

213.5/13.5-РА

213,5/13,5 РА

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc178SR-1-06 1868 19500 50 1130005264 52,17 100  39269097 Germany
print("doc178",doc178[5: 8], doc178[8: 9], doc178[10: 11], doc178[11: 12], doc178[13: 14], doc178[14:15], doc178[15:16] ,doc178[17:18], doc178[44: 45], doc178[50: 51]) 
doc178.ents = [Span(doc178, 5, 8, label="CONTRACT"), 
    Span(doc178, 8, 9, label="CONTRACT1"), 
    Span(doc178, 10, 11, label="POS"), 
    Span(doc178, 11, 12, label="AMOUNT"), 
    Span(doc178, 13, 14, label="ARTICLE"), 
    Span(doc178, 14, 15, label="PRICE"), 
    Span(doc178, 15, 16, label="UNIT"), 
    Span(doc178, 17, 18, label="SUM"), 
    Span(doc178, 44, 45, label="TARIFF"), 
    Span(doc178, 50, 51, label="COUNTRY")] 
docs.append(doc178)


doc179 = nlp('''Purchase order number: N SR-1-06 1868
19600 25 РС 1130005318 52,17 100 РС 13,04
215/15-PA
215/15 PA

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc179SR-1-06 1868 19600 25 1130005318 52,17 100  39269097 Germany
print("doc179",doc179[5: 8], doc179[8: 9], doc179[10: 11], doc179[11: 12], doc179[13: 14], doc179[14:15], doc179[15:16] ,doc179[17:18], doc179[44: 45], doc179[50: 51]) 
doc179.ents = [Span(doc179, 5, 8, label="CONTRACT"), 
    Span(doc179, 8, 9, label="CONTRACT1"), 
    Span(doc179, 10, 11, label="POS"), 
    Span(doc179, 11, 12, label="AMOUNT"), 
    Span(doc179, 13, 14, label="ARTICLE"), 
    Span(doc179, 14, 15, label="PRICE"), 
    Span(doc179, 15, 16, label="UNIT"), 
    Span(doc179, 17, 18, label="SUM"), 
    Span(doc179, 44, 45, label="TARIFF"), 
    Span(doc179, 50, 51, label="COUNTRY")] 
docs.append(doc179)


doc180 = nlp('''Purchase order number: N SR-1-06 1868
19700 50 РС 1130005357 52,17 100 РС 26,09
216/16-РА
216/16 РА

packed per each item


Description

Product description: Pipe clamp
Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc180SR-1-06 1868 19700 50 1130005357 52,17 100  39269097 Germany
print("doc180",doc180[5: 8], doc180[8: 9], doc180[10: 11], doc180[11: 12], doc180[13: 14], doc180[14:15], doc180[15:16] ,doc180[17:18], doc180[46: 47], doc180[52: 53]) 
doc180.ents = [Span(doc180, 5, 8, label="CONTRACT"), 
    Span(doc180, 8, 9, label="CONTRACT1"), 
    Span(doc180, 10, 11, label="POS"), 
    Span(doc180, 11, 12, label="AMOUNT"), 
    Span(doc180, 13, 14, label="ARTICLE"), 
    Span(doc180, 14, 15, label="PRICE"), 
    Span(doc180, 15, 16, label="UNIT"), 
    Span(doc180, 17, 18, label="SUM"), 
    Span(doc180, 46, 47, label="TARIFF"), 
    Span(doc180, 52, 53, label="COUNTRY")] 
docs.append(doc180)


doc181 = nlp('''Purchase order number: N SR-1-06 1869
19800 6 РС 1130004188 278,34 100 РС 16,70

AS-M24x220-DIN931/933-8.8-W1
AS-M24X220-DIN931/933-8.8-W1
packed per each item

Product description: screw

Export - Customs tariff по.: 73181588
Country of origin: Vietnam''')
#doc181SR-1-06 1869 19800 6 1130004188 278,34 100  73181588 Vietnam
print("doc181",doc181[5: 8], doc181[8: 9], doc181[10: 11], doc181[11: 12], doc181[13: 14], doc181[14:15], doc181[15:16] ,doc181[17:18], doc181[56: 57], doc181[62: 63]) 
doc181.ents = [Span(doc181, 5, 8, label="CONTRACT"), 
    Span(doc181, 8, 9, label="CONTRACT1"), 
    Span(doc181, 10, 11, label="POS"), 
    Span(doc181, 11, 12, label="AMOUNT"), 
    Span(doc181, 13, 14, label="ARTICLE"), 
    Span(doc181, 14, 15, label="PRICE"), 
    Span(doc181, 15, 16, label="UNIT"), 
    Span(doc181, 17, 18, label="SUM"), 
    Span(doc181, 56, 57, label="TARIFF"), 
    Span(doc181, 62, 63, label="COUNTRY")] 
docs.append(doc181)


doc182 = nlp('''Purchase order number: N SR-1-06 1869
19900 368 PC 1130004024 5,48 100 PC 20,17

AS-M6x60-DIN931/933-8.8-W3
AS-M6X60-DIN931/933-8.8-W3
packed per each item

Product description: screw

Export - Customs tariff по.: 73181588
Country of origin: Turkey''')
#doc182SR-1-06 1869 19900 368 1130004024 5,48 100  73181588 Turkey
print("doc182",doc182[5: 8], doc182[8: 9], doc182[10: 11], doc182[11: 12], doc182[13: 14], doc182[14:15], doc182[15:16] ,doc182[17:18], doc182[56: 57], doc182[62: 63]) 
doc182.ents = [Span(doc182, 5, 8, label="CONTRACT"), 
    Span(doc182, 8, 9, label="CONTRACT1"), 
    Span(doc182, 10, 11, label="POS"), 
    Span(doc182, 11, 12, label="AMOUNT"), 
    Span(doc182, 13, 14, label="ARTICLE"), 
    Span(doc182, 14, 15, label="PRICE"), 
    Span(doc182, 15, 16, label="UNIT"), 
    Span(doc182, 17, 18, label="SUM"), 
    Span(doc182, 56, 57, label="TARIFF"), 
    Span(doc182, 62, 63, label="COUNTRY")] 
docs.append(doc182)


doc183 = nlp('''Purchase order number: N SR-1-06 1869
20000 175 PC 1130005980 51,18 100 PC 89,57
533.7-PP
533,7 PP

packed per each item


Description

Product description: Pipe clamp
Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc183SR-1-06 1869 20000 175 1130005980 51,18 100  39269097 Germany
print("doc183",doc183[5: 8], doc183[8: 9], doc183[10: 11], doc183[11: 12], doc183[13: 14], doc183[14:15], doc183[15:16] ,doc183[17:18], doc183[46: 47], doc183[52: 53]) 
doc183.ents = [Span(doc183, 5, 8, label="CONTRACT"), 
    Span(doc183, 8, 9, label="CONTRACT1"), 
    Span(doc183, 10, 11, label="POS"), 
    Span(doc183, 11, 12, label="AMOUNT"), 
    Span(doc183, 13, 14, label="ARTICLE"), 
    Span(doc183, 14, 15, label="PRICE"), 
    Span(doc183, 15, 16, label="UNIT"), 
    Span(doc183, 17, 18, label="SUM"), 
    Span(doc183, 46, 47, label="TARIFF"), 
    Span(doc183, 52, 53, label="COUNTRY")] 
docs.append(doc183)


doc184 = nlp('''Purchase order number: N SR-1-06 1869
20100 3 РС 1130006277 1.167,09 100 PC 35,01
9140-PP
9140 PP

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc184SR-1-06 1869 20100 3 1130006277 1.167,09 100  39269097 Germany
print("doc184",doc184[5: 8], doc184[8: 9], doc184[10: 11], doc184[11: 12], doc184[13: 14], doc184[14:15], doc184[15:16] ,doc184[17:18], doc184[44: 45], doc184[50: 51]) 
doc184.ents = [Span(doc184, 5, 8, label="CONTRACT"), 
    Span(doc184, 8, 9, label="CONTRACT1"), 
    Span(doc184, 10, 11, label="POS"), 
    Span(doc184, 11, 12, label="AMOUNT"), 
    Span(doc184, 13, 14, label="ARTICLE"), 
    Span(doc184, 14, 15, label="PRICE"), 
    Span(doc184, 15, 16, label="UNIT"), 
    Span(doc184, 17, 18, label="SUM"), 
    Span(doc184, 44, 45, label="TARIFF"), 
    Span(doc184, 50, 51, label="COUNTRY")] 
docs.append(doc184)


doc185 = nlp('''Purchase order number: N SR-1-06 1869
20200 3 РС 1130000730 483,44 100 PC 14,50
DPAL-9S-W1
DPAL 9 $ W1

packed per each item

Product description: cover plate

Export - Customs tariff no.: 73182900
Country of origin: Germany''')
#doc185SR-1-06 1869 20200 3 1130000730 483,44 100  73182900 Germany
print("doc185",doc185[5: 8], doc185[8: 9], doc185[10: 11], doc185[11: 12], doc185[13: 14], doc185[14:15], doc185[15:16] ,doc185[17:18], doc185[46: 47], doc185[52: 53]) 
doc185.ents = [Span(doc185, 5, 8, label="CONTRACT"), 
    Span(doc185, 8, 9, label="CONTRACT1"), 
    Span(doc185, 10, 11, label="POS"), 
    Span(doc185, 11, 12, label="AMOUNT"), 
    Span(doc185, 13, 14, label="ARTICLE"), 
    Span(doc185, 14, 15, label="PRICE"), 
    Span(doc185, 15, 16, label="UNIT"), 
    Span(doc185, 17, 18, label="SUM"), 
    Span(doc185, 46, 47, label="TARIFF"), 
    Span(doc185, 52, 53, label="COUNTRY")] 
docs.append(doc185)


doc186 = nlp('''Purchase order number: N SR-1-06 1869
20300 3 РС 1120022877 1.016,68 100 PC 30,50

SPAL-9S-M-W1/2
SPAL 9 $ М W1 /2
packed per each item


Description

Product description: weld plate
Export - Customs tariff no.: 73269098
Country of origin: Italy''')
#doc186SR-1-06 1869 20300 3 1120022877 1.016,68 100  73269098 Italy
print("doc186",doc186[5: 8], doc186[8: 9], doc186[10: 11], doc186[11: 12], doc186[13: 14], doc186[14:15], doc186[15:16] ,doc186[17:18], doc186[52: 53], doc186[58: 59]) 
doc186.ents = [Span(doc186, 5, 8, label="CONTRACT"), 
    Span(doc186, 8, 9, label="CONTRACT1"), 
    Span(doc186, 10, 11, label="POS"), 
    Span(doc186, 11, 12, label="AMOUNT"), 
    Span(doc186, 13, 14, label="ARTICLE"), 
    Span(doc186, 14, 15, label="PRICE"), 
    Span(doc186, 15, 16, label="UNIT"), 
    Span(doc186, 17, 18, label="SUM"), 
    Span(doc186, 52, 53, label="TARIFF"), 
    Span(doc186, 58, 59, label="COUNTRY")] 
docs.append(doc186)


doc187 = nlp('''Purchase order number: N SR-1-06 1869
20400 175 PC 1120001237 33,99 100 PC 59,48
SPV-5-M-W2
SPV 5 М W2

packed per each item

Product description: weld plate

Export - Customs tariff no.: 73269098
Country of origin: Germany''')
#doc187SR-1-06 1869 20400 175 1120001237 33,99 100  73269098 Germany
print("doc187",doc187[5: 8], doc187[8: 9], doc187[10: 11], doc187[11: 12], doc187[13: 14], doc187[14:15], doc187[15:16] ,doc187[17:18], doc187[48: 49], doc187[54: 55]) 
doc187.ents = [Span(doc187, 5, 8, label="CONTRACT"), 
    Span(doc187, 8, 9, label="CONTRACT1"), 
    Span(doc187, 10, 11, label="POS"), 
    Span(doc187, 11, 12, label="AMOUNT"), 
    Span(doc187, 13, 14, label="ARTICLE"), 
    Span(doc187, 14, 15, label="PRICE"), 
    Span(doc187, 15, 16, label="UNIT"), 
    Span(doc187, 17, 18, label="SUM"), 
    Span(doc187, 48, 49, label="TARIFF"), 
    Span(doc187, 54, 55, label="COUNTRY")] 
docs.append(doc187)


doc188 = nlp('''Purchase order number: N SR-1-06 1870
20500 200 РС 1130004020 3,93 100 РС 7,86

AS-M6x30-DIN931/933-8.8-W3
AS-M6X30-DIN931/933-8.8-W3
packed per each item

Product description: screw

Export - Customs tariff по.: 73181588
Country of origin: Turkey''')
#doc188SR-1-06 1870 20500 200 1130004020 3,93 100  73181588 Turkey
print("doc188",doc188[5: 8], doc188[8: 9], doc188[10: 11], doc188[11: 12], doc188[13: 14], doc188[14:15], doc188[15:16] ,doc188[17:18], doc188[56: 57], doc188[62: 63]) 
doc188.ents = [Span(doc188, 5, 8, label="CONTRACT"), 
    Span(doc188, 8, 9, label="CONTRACT1"), 
    Span(doc188, 10, 11, label="POS"), 
    Span(doc188, 11, 12, label="AMOUNT"), 
    Span(doc188, 13, 14, label="ARTICLE"), 
    Span(doc188, 14, 15, label="PRICE"), 
    Span(doc188, 15, 16, label="UNIT"), 
    Span(doc188, 17, 18, label="SUM"), 
    Span(doc188, 56, 57, label="TARIFF"), 
    Span(doc188, 62, 63, label="COUNTRY")] 
docs.append(doc188)


doc189 = nlp('''Purchase order number: N SR-1-06 1870
20600 600 РС 1130004022 4,30 100 PC 25,80

AS-M6x40-DIN931/933-8.8-W3
AS-M6X40-DIN931/933-8.8-W3
packed per each item


Description

Product description: screw
Export - Customs tariff по.: 73181588
Country of origin: Taiwan''')
#doc189SR-1-06 1870 20600 600 1130004022 4,30 100  73181588 Taiwan
print("doc189",doc189[5: 8], doc189[8: 9], doc189[10: 11], doc189[11: 12], doc189[13: 14], doc189[14:15], doc189[15:16] ,doc189[17:18], doc189[58: 59], doc189[64: 65]) 
doc189.ents = [Span(doc189, 5, 8, label="CONTRACT"), 
    Span(doc189, 8, 9, label="CONTRACT1"), 
    Span(doc189, 10, 11, label="POS"), 
    Span(doc189, 11, 12, label="AMOUNT"), 
    Span(doc189, 13, 14, label="ARTICLE"), 
    Span(doc189, 14, 15, label="PRICE"), 
    Span(doc189, 15, 16, label="UNIT"), 
    Span(doc189, 17, 18, label="SUM"), 
    Span(doc189, 58, 59, label="TARIFF"), 
    Span(doc189, 64, 65, label="COUNTRY")] 
docs.append(doc189)


doc190 = nlp('''Purchase order number: N SR-1-06 1870
20700 100 PC 1130004023 4,51 100 PC 4,51

AS-M6x45-DIN931/933-8.8-W3
AS-M6X45-DIN931/933-8.8-W3
packed per each item

Product description: screw

Export - Customs tariff по.: 73181588
Country of origin: Turkey''')
#doc190SR-1-06 1870 20700 100 1130004023 4,51 100  73181588 Turkey
print("doc190",doc190[5: 8], doc190[8: 9], doc190[10: 11], doc190[11: 12], doc190[13: 14], doc190[14:15], doc190[15:16] ,doc190[17:18], doc190[56: 57], doc190[62: 63]) 
doc190.ents = [Span(doc190, 5, 8, label="CONTRACT"), 
    Span(doc190, 8, 9, label="CONTRACT1"), 
    Span(doc190, 10, 11, label="POS"), 
    Span(doc190, 11, 12, label="AMOUNT"), 
    Span(doc190, 13, 14, label="ARTICLE"), 
    Span(doc190, 14, 15, label="PRICE"), 
    Span(doc190, 15, 16, label="UNIT"), 
    Span(doc190, 17, 18, label="SUM"), 
    Span(doc190, 56, 57, label="TARIFF"), 
    Span(doc190, 62, 63, label="COUNTRY")] 
docs.append(doc190)


doc191 = nlp('''Purchase order number: N SR-1-06 1870
20800 900 РС 6100152347 12,73 100 PC 114,57

SM-1-8/1D-M-W3/2

packed per each item

Customer ID-No.: 000000001120001932
Product description: nuts

Export - Customs tariff no.: 73181692
Country of origin: Germany''')
#doc191SR-1-06 1870 20800 900 6100152347 12,73 100  73181692 Germany
print("doc191",doc191[5: 8], doc191[8: 9], doc191[10: 11], doc191[11: 12], doc191[13: 14], doc191[14:15], doc191[15:16] ,doc191[17:18], doc191[52: 53], doc191[58: 59]) 
doc191.ents = [Span(doc191, 5, 8, label="CONTRACT"), 
    Span(doc191, 8, 9, label="CONTRACT1"), 
    Span(doc191, 10, 11, label="POS"), 
    Span(doc191, 11, 12, label="AMOUNT"), 
    Span(doc191, 13, 14, label="ARTICLE"), 
    Span(doc191, 14, 15, label="PRICE"), 
    Span(doc191, 15, 16, label="UNIT"), 
    Span(doc191, 17, 18, label="SUM"), 
    Span(doc191, 52, 53, label="TARIFF"), 
    Span(doc191, 58, 59, label="COUNTRY")] 
docs.append(doc191)


doc192 = nlp('''Purchase order number: N SR-1-06 1870
20900 100 PC 1130005145 32,99 100 PC 32,99
110a-PA
110a PA

packed per each item


Description

Product description: Pipe clamp
Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc192SR-1-06 1870 20900 100 1130005145 32,99 100  39269097 Germany
print("doc192",doc192[5: 8], doc192[8: 9], doc192[10: 11], doc192[11: 12], doc192[13: 14], doc192[14:15], doc192[15:16] ,doc192[17:18], doc192[46: 47], doc192[52: 53]) 
doc192.ents = [Span(doc192, 5, 8, label="CONTRACT"), 
    Span(doc192, 8, 9, label="CONTRACT1"), 
    Span(doc192, 10, 11, label="POS"), 
    Span(doc192, 11, 12, label="AMOUNT"), 
    Span(doc192, 13, 14, label="ARTICLE"), 
    Span(doc192, 14, 15, label="PRICE"), 
    Span(doc192, 15, 16, label="UNIT"), 
    Span(doc192, 17, 18, label="SUM"), 
    Span(doc192, 46, 47, label="TARIFF"), 
    Span(doc192, 52, 53, label="COUNTRY")] 
docs.append(doc192)


doc193 = nlp('''Purchase order number: N SR-1-06 1870
21000 200 РС 1130005533 41,59 100 PC 83,18
320-РА
320 РА

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc193SR-1-06 1870 21000 200 1130005533 41,59 100  39269097 Germany
print("doc193",doc193[5: 8], doc193[8: 9], doc193[10: 11], doc193[11: 12], doc193[13: 14], doc193[14:15], doc193[15:16] ,doc193[17:18], doc193[44: 45], doc193[50: 51]) 
doc193.ents = [Span(doc193, 5, 8, label="CONTRACT"), 
    Span(doc193, 8, 9, label="CONTRACT1"), 
    Span(doc193, 10, 11, label="POS"), 
    Span(doc193, 11, 12, label="AMOUNT"), 
    Span(doc193, 13, 14, label="ARTICLE"), 
    Span(doc193, 14, 15, label="PRICE"), 
    Span(doc193, 15, 16, label="UNIT"), 
    Span(doc193, 17, 18, label="SUM"), 
    Span(doc193, 44, 45, label="TARIFF"), 
    Span(doc193, 50, 51, label="COUNTRY")] 
docs.append(doc193)


doc194 = nlp('''Purchase order number: N SR-1-06 1870
21100 100 PC 1130005628 41,59 100 PC 41,59
325-РА
325 РА

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc194SR-1-06 1870 21100 100 1130005628 41,59 100  39269097 Germany
print("doc194",doc194[5: 8], doc194[8: 9], doc194[10: 11], doc194[11: 12], doc194[13: 14], doc194[14:15], doc194[15:16] ,doc194[17:18], doc194[44: 45], doc194[50: 51]) 
doc194.ents = [Span(doc194, 5, 8, label="CONTRACT"), 
    Span(doc194, 8, 9, label="CONTRACT1"), 
    Span(doc194, 10, 11, label="POS"), 
    Span(doc194, 11, 12, label="AMOUNT"), 
    Span(doc194, 13, 14, label="ARTICLE"), 
    Span(doc194, 14, 15, label="PRICE"), 
    Span(doc194, 15, 16, label="UNIT"), 
    Span(doc194, 17, 18, label="SUM"), 
    Span(doc194, 44, 45, label="TARIFF"), 
    Span(doc194, 50, 51, label="COUNTRY")] 
docs.append(doc194)


doc195 = nlp('''Purchase order number: N SR-1-06 1870
21200 50 РС 1130009399 60,74 100 PC 30,37
432-PA
432 PA

packed per each item


Description

Product description: Pipe clamp
Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc195SR-1-06 1870 21200 50 1130009399 60,74 100  39269097 Germany
print("doc195",doc195[5: 8], doc195[8: 9], doc195[10: 11], doc195[11: 12], doc195[13: 14], doc195[14:15], doc195[15:16] ,doc195[17:18], doc195[46: 47], doc195[52: 53]) 
doc195.ents = [Span(doc195, 5, 8, label="CONTRACT"), 
    Span(doc195, 8, 9, label="CONTRACT1"), 
    Span(doc195, 10, 11, label="POS"), 
    Span(doc195, 11, 12, label="AMOUNT"), 
    Span(doc195, 13, 14, label="ARTICLE"), 
    Span(doc195, 14, 15, label="PRICE"), 
    Span(doc195, 15, 16, label="UNIT"), 
    Span(doc195, 17, 18, label="SUM"), 
    Span(doc195, 46, 47, label="TARIFF"), 
    Span(doc195, 52, 53, label="COUNTRY")] 
docs.append(doc195)


doc196 = nlp('''Purchase order number: N SR-1-06 1870
21300 100 PC 1130000258 6,83 100 PC 6,83
DP-1a-W3
DP 1a W3

packed per each item

Product description: cover plate

Export - Customs tariff no.: 73269098
Country of origin: Germany''')
#doc196SR-1-06 1870 21300 100 1130000258 6,83 100  73269098 Germany
print("doc196",doc196[5: 8], doc196[8: 9], doc196[10: 11], doc196[11: 12], doc196[13: 14], doc196[14:15], doc196[15:16] ,doc196[17:18], doc196[45: 46], doc196[51: 52]) 
doc196.ents = [Span(doc196, 5, 8, label="CONTRACT"), 
    Span(doc196, 8, 9, label="CONTRACT1"), 
    Span(doc196, 10, 11, label="POS"), 
    Span(doc196, 11, 12, label="AMOUNT"), 
    Span(doc196, 13, 14, label="ARTICLE"), 
    Span(doc196, 14, 15, label="PRICE"), 
    Span(doc196, 15, 16, label="UNIT"), 
    Span(doc196, 17, 18, label="SUM"), 
    Span(doc196, 45, 46, label="TARIFF"), 
    Span(doc196, 51, 52, label="COUNTRY")] 
docs.append(doc196)


doc197 = nlp('''Purchase order number: N SR-1-06 1870
21400 50 PC 1130000267 9,76 100 PC 4,88
DP-4-W3
DP 4 W3

packed per each item

Product description: cover plate

Export - Customs tariff no.: 73269098
Country of origin: Germany''')
#doc197SR-1-06 1870 21400 50 1130000267 9,76 100  73269098 Germany
print("doc197",doc197[5: 8], doc197[8: 9], doc197[10: 11], doc197[11: 12], doc197[13: 14], doc197[14:15], doc197[15:16] ,doc197[17:18], doc197[45: 46], doc197[51: 52]) 
doc197.ents = [Span(doc197, 5, 8, label="CONTRACT"), 
    Span(doc197, 8, 9, label="CONTRACT1"), 
    Span(doc197, 10, 11, label="POS"), 
    Span(doc197, 11, 12, label="AMOUNT"), 
    Span(doc197, 13, 14, label="ARTICLE"), 
    Span(doc197, 14, 15, label="PRICE"), 
    Span(doc197, 15, 16, label="UNIT"), 
    Span(doc197, 17, 18, label="SUM"), 
    Span(doc197, 45, 46, label="TARIFF"), 
    Span(doc197, 51, 52, label="COUNTRY")] 
docs.append(doc197)


doc198 = nlp('''Purchase order number: N SR-1-06 1871
21500 25 РС 1130005358 63,10 100 РС 15,78
216/16-РА-Н
216/16 РАН

packed per each item


Description

Product description: Pipe clamp
Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc198SR-1-06 1871 21500 25 1130005358 63,10 100  39269097 Germany
print("doc198",doc198[5: 8], doc198[8: 9], doc198[10: 11], doc198[11: 12], doc198[13: 14], doc198[14:15], doc198[15:16] ,doc198[17:18], doc198[48: 49], doc198[54: 55]) 
doc198.ents = [Span(doc198, 5, 8, label="CONTRACT"), 
    Span(doc198, 8, 9, label="CONTRACT1"), 
    Span(doc198, 10, 11, label="POS"), 
    Span(doc198, 11, 12, label="AMOUNT"), 
    Span(doc198, 13, 14, label="ARTICLE"), 
    Span(doc198, 14, 15, label="PRICE"), 
    Span(doc198, 15, 16, label="UNIT"), 
    Span(doc198, 17, 18, label="SUM"), 
    Span(doc198, 48, 49, label="TARIFF"), 
    Span(doc198, 54, 55, label="COUNTRY")] 
docs.append(doc198)


doc199 = nlp('''Purchase order number: N SR-1-06 1872
21600 50 PC 1120003536 (*) 15,03 100 PC 7,52
AF-2-M-W3

AF 2 М W3 M6x25

packed per each item

Product description: screw

Export - Customs tariff по.: 73181588
Country of origin: Germany''')
#doc199SR-1-06 1872 21600 50 1120003536 15,03 100  73181588 Germany
print("doc199",doc199[5: 8], doc199[8: 9], doc199[10: 11], doc199[11: 12], doc199[13: 14], doc199[17:18], doc199[18:19] ,doc199[20:21], doc199[51: 52], doc199[57: 58]) 
doc199.ents = [Span(doc199, 5, 8, label="CONTRACT"), 
    Span(doc199, 8, 9, label="CONTRACT1"), 
    Span(doc199, 10, 11, label="POS"), 
    Span(doc199, 11, 12, label="AMOUNT"), 
    Span(doc199, 13, 14, label="ARTICLE"), 
    Span(doc199, 17, 18, label="PRICE"), 
    Span(doc199, 18, 19, label="UNIT"), 
    Span(doc199, 20, 21, label="SUM"), 
    Span(doc199, 51, 52, label="TARIFF"), 
    Span(doc199, 57, 58, label="COUNTRY")] 
docs.append(doc199)


doc200 = nlp('''Purchase order number: N SR-1-06 1872
21700 10 PC 1020013540 5,23 1 РС 52,30
SF-6310-18
SF6310-18

packed per each item

Product description: filter element
Export - Customs tariff по.: 84212980
Country of origin: Brazil''')
#doc200SR-1-06 1872 21700 10 1020013540 5,23 1  84212980 Brazil
print("doc200",doc200[5: 8], doc200[8: 9], doc200[10: 11], doc200[11: 12], doc200[13: 14], doc200[14:15], doc200[15:16] ,doc200[17:18], doc200[45: 46], doc200[51: 52]) 
doc200.ents = [Span(doc200, 5, 8, label="CONTRACT"), 
    Span(doc200, 8, 9, label="CONTRACT1"), 
    Span(doc200, 10, 11, label="POS"), 
    Span(doc200, 11, 12, label="AMOUNT"), 
    Span(doc200, 13, 14, label="ARTICLE"), 
    Span(doc200, 14, 15, label="PRICE"), 
    Span(doc200, 15, 16, label="UNIT"), 
    Span(doc200, 17, 18, label="SUM"), 
    Span(doc200, 45, 46, label="TARIFF"), 
    Span(doc200, 51, 52, label="COUNTRY")] 
docs.append(doc200)


doc201 = nlp('''Purchase order number: N SR-1-06 1873
21800 48 РС 1130004021 4,09 100 PC 1,96

AS-M6x35-DIN931/933-8.8-W3
AS-M6X35-DIN931/933-8.8-W3


Description

packed per each item

Product description: screw

Export - Customs tariff по.: 73181588
Country of origin: Turkey''')
#doc201SR-1-06 1873 21800 48 1130004021 4,09 100  73181588 Turkey
print("doc201",doc201[5: 8], doc201[8: 9], doc201[10: 11], doc201[11: 12], doc201[13: 14], doc201[14:15], doc201[15:16] ,doc201[17:18], doc201[58: 59], doc201[64: 65]) 
doc201.ents = [Span(doc201, 5, 8, label="CONTRACT"), 
    Span(doc201, 8, 9, label="CONTRACT1"), 
    Span(doc201, 10, 11, label="POS"), 
    Span(doc201, 11, 12, label="AMOUNT"), 
    Span(doc201, 13, 14, label="ARTICLE"), 
    Span(doc201, 14, 15, label="PRICE"), 
    Span(doc201, 15, 16, label="UNIT"), 
    Span(doc201, 17, 18, label="SUM"), 
    Span(doc201, 58, 59, label="TARIFF"), 
    Span(doc201, 64, 65, label="COUNTRY")] 
docs.append(doc201)


doc202 = nlp('''Purchase order number: N SR-1-06 1873
21900 2 РС 6100068279 84,76 1 РС 169,52

QRC-FH-12-F-G08-VT-W5
FH12-1-IGFO8VA

packed per each item

Product description: coupling

Export - Customs tariff no.: 84812010
Country of origin: Germany''')
#doc202SR-1-06 1873 21900 2 6100068279 84,76 1  84812010 Germany
print("doc202",doc202[5: 8], doc202[8: 9], doc202[10: 11], doc202[11: 12], doc202[13: 14], doc202[14:15], doc202[15:16] ,doc202[17:18], doc202[54: 55], doc202[60: 61]) 
doc202.ents = [Span(doc202, 5, 8, label="CONTRACT"), 
    Span(doc202, 8, 9, label="CONTRACT1"), 
    Span(doc202, 10, 11, label="POS"), 
    Span(doc202, 11, 12, label="AMOUNT"), 
    Span(doc202, 13, 14, label="ARTICLE"), 
    Span(doc202, 14, 15, label="PRICE"), 
    Span(doc202, 15, 16, label="UNIT"), 
    Span(doc202, 17, 18, label="SUM"), 
    Span(doc202, 54, 55, label="TARIFF"), 
    Span(doc202, 60, 61, label="COUNTRY")] 
docs.append(doc202)


doc203 = nlp('''Purchase order number: N SR-1-06 1873
22000 12 PC 6100068356 51,37 1 РС 616,44

QRC-FH-12-M-G08-VT-W5
FH12-2-IGFO8VA

packed per each item

Product description: coupling

Export - Customs tariff no.: 84812010
Country of origin: Germany''')
#doc203SR-1-06 1873 22000 12 6100068356 51,37 1  84812010 Germany
print("doc203",doc203[5: 8], doc203[8: 9], doc203[10: 11], doc203[11: 12], doc203[13: 14], doc203[14:15], doc203[15:16] ,doc203[17:18], doc203[54: 55], doc203[60: 61]) 
doc203.ents = [Span(doc203, 5, 8, label="CONTRACT"), 
    Span(doc203, 8, 9, label="CONTRACT1"), 
    Span(doc203, 10, 11, label="POS"), 
    Span(doc203, 11, 12, label="AMOUNT"), 
    Span(doc203, 13, 14, label="ARTICLE"), 
    Span(doc203, 14, 15, label="PRICE"), 
    Span(doc203, 15, 16, label="UNIT"), 
    Span(doc203, 17, 18, label="SUM"), 
    Span(doc203, 54, 55, label="TARIFF"), 
    Span(doc203, 60, 61, label="COUNTRY")] 
docs.append(doc203)


doc204 = nlp('''Purchase order number: N SR-1-06 1873
22100 2 РС 6100068236 0,64 1 РС 1,28


Description

QRC-FH-12-DF-36-K-RD

FH12-9-RT001

packed per each item

Product description: cap

Export - Customs tariff no.: 39235090
Country of origin: Germany''')
#doc204SR-1-06 1873 22100 2 6100068236 0,64 1  39235090 Germany
print("doc204",doc204[5: 8], doc204[8: 9], doc204[10: 11], doc204[11: 12], doc204[13: 14], doc204[14:15], doc204[15:16] ,doc204[17:18], doc204[54: 55], doc204[60: 61]) 
doc204.ents = [Span(doc204, 5, 8, label="CONTRACT"), 
    Span(doc204, 8, 9, label="CONTRACT1"), 
    Span(doc204, 10, 11, label="POS"), 
    Span(doc204, 11, 12, label="AMOUNT"), 
    Span(doc204, 13, 14, label="ARTICLE"), 
    Span(doc204, 14, 15, label="PRICE"), 
    Span(doc204, 15, 16, label="UNIT"), 
    Span(doc204, 17, 18, label="SUM"), 
    Span(doc204, 54, 55, label="TARIFF"), 
    Span(doc204, 60, 61, label="COUNTRY")] 
docs.append(doc204)


doc205 = nlp('''Purchase order number: N SR-1-06 1873
22200 25 РС 1130000261 7,39 100 PC 1,85
DP-2-W3
DP 2 W3
packed per each item
Product description: cover plate
Export - Customs tariff no.: 73269098
Country of origin: Germany''')
#doc205SR-1-06 1873 22200 25 1130000261 7,39 100  73269098 Germany
print("doc205",doc205[5: 8], doc205[8: 9], doc205[10: 11], doc205[11: 12], doc205[13: 14], doc205[14:15], doc205[15:16] ,doc205[17:18], doc205[45: 46], doc205[51: 52]) 
doc205.ents = [Span(doc205, 5, 8, label="CONTRACT"), 
    Span(doc205, 8, 9, label="CONTRACT1"), 
    Span(doc205, 10, 11, label="POS"), 
    Span(doc205, 11, 12, label="AMOUNT"), 
    Span(doc205, 13, 14, label="ARTICLE"), 
    Span(doc205, 14, 15, label="PRICE"), 
    Span(doc205, 15, 16, label="UNIT"), 
    Span(doc205, 17, 18, label="SUM"), 
    Span(doc205, 45, 46, label="TARIFF"), 
    Span(doc205, 51, 52, label="COUNTRY")] 
docs.append(doc205)


doc206 = nlp('''Purchase order number: N SR-1-06 1873
22300 25 РС 1120001156 26,58 100 РС 6,65
SP-2-M-W2
SP 2 M W2

packed per each item

Product description: weld plate

Export - Customs tariff no.: 73269098
Country of origin: Germany''')
#doc206SR-1-06 1873 22300 25 1120001156 26,58 100  73269098 Germany
print("doc206",doc206[5: 8], doc206[8: 9], doc206[10: 11], doc206[11: 12], doc206[13: 14], doc206[14:15], doc206[15:16] ,doc206[17:18], doc206[48: 49], doc206[54: 55]) 
doc206.ents = [Span(doc206, 5, 8, label="CONTRACT"), 
    Span(doc206, 8, 9, label="CONTRACT1"), 
    Span(doc206, 10, 11, label="POS"), 
    Span(doc206, 11, 12, label="AMOUNT"), 
    Span(doc206, 13, 14, label="ARTICLE"), 
    Span(doc206, 14, 15, label="PRICE"), 
    Span(doc206, 15, 16, label="UNIT"), 
    Span(doc206, 17, 18, label="SUM"), 
    Span(doc206, 48, 49, label="TARIFF"), 
    Span(doc206, 54, 55, label="COUNTRY")] 
docs.append(doc206)


doc208 = nlp('''Purchase order number: N SR-1-06 1874
22500 20 РС 1130004186 52,76 100 PC 10,55

AS-M16x130-DIN931/933-8.8-W1
AS-M16X130-DIN931/933-8.8-W1
packed per each item

Product description: screw

Export - Customs tariff по.: 73181588
Country of origin: Germany''')
#doc208SR-1-06 1874 22500 20 1130004186 52,76 100  73181588 Germany
print("doc208",doc208[5: 8], doc208[8: 9], doc208[10: 11], doc208[11: 12], doc208[13: 14], doc208[14:15], doc208[15:16] ,doc208[17:18], doc208[56: 57], doc208[62: 63]) 
doc208.ents = [Span(doc208, 5, 8, label="CONTRACT"), 
    Span(doc208, 8, 9, label="CONTRACT1"), 
    Span(doc208, 10, 11, label="POS"), 
    Span(doc208, 11, 12, label="AMOUNT"), 
    Span(doc208, 13, 14, label="ARTICLE"), 
    Span(doc208, 14, 15, label="PRICE"), 
    Span(doc208, 15, 16, label="UNIT"), 
    Span(doc208, 17, 18, label="SUM"), 
    Span(doc208, 56, 57, label="TARIFF"), 
    Span(doc208, 62, 63, label="COUNTRY")] 
docs.append(doc208)


doc209 = nlp('''Purchase order number: N SR-1-06 1874
22600 10 PC 1130006617 202,17 100 PC 20,22
6065-PP-H
6065 PPH

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc209SR-1-06 1874 22600 10 1130006617 202,17 100  39269097 Germany
print("doc209",doc209[5: 8], doc209[8: 9], doc209[10: 11], doc209[11: 12], doc209[13: 14], doc209[14:15], doc209[15:16] ,doc209[17:18], doc209[46: 47], doc209[52: 53]) 
doc209.ents = [Span(doc209, 5, 8, label="CONTRACT"), 
    Span(doc209, 8, 9, label="CONTRACT1"), 
    Span(doc209, 10, 11, label="POS"), 
    Span(doc209, 11, 12, label="AMOUNT"), 
    Span(doc209, 13, 14, label="ARTICLE"), 
    Span(doc209, 14, 15, label="PRICE"), 
    Span(doc209, 15, 16, label="UNIT"), 
    Span(doc209, 17, 18, label="SUM"), 
    Span(doc209, 46, 47, label="TARIFF"), 
    Span(doc209, 52, 53, label="COUNTRY")] 
docs.append(doc209)


doc211 = nlp('''Purchase order number: N SR-1-06 1874
22800 3 РС 1130000718 73,62 100 PC 2,21
DPAL-6S-W2
DPAL 6 S W2

packed per each item

Product description: cover plate

Export - Customs tariff no.: 73182900
Country of origin: Germany''')
#doc211SR-1-06 1874 22800 3 1130000718 73,62 100  73182900 Germany
print("doc211",doc211[5: 8], doc211[8: 9], doc211[10: 11], doc211[11: 12], doc211[13: 14], doc211[14:15], doc211[15:16] ,doc211[17:18], doc211[46: 47], doc211[52: 53]) 
doc211.ents = [Span(doc211, 5, 8, label="CONTRACT"), 
    Span(doc211, 8, 9, label="CONTRACT1"), 
    Span(doc211, 10, 11, label="POS"), 
    Span(doc211, 11, 12, label="AMOUNT"), 
    Span(doc211, 13, 14, label="ARTICLE"), 
    Span(doc211, 14, 15, label="PRICE"), 
    Span(doc211, 15, 16, label="UNIT"), 
    Span(doc211, 17, 18, label="SUM"), 
    Span(doc211, 46, 47, label="TARIFF"), 
    Span(doc211, 52, 53, label="COUNTRY")] 
docs.append(doc211)


doc212 = nlp('''Purchase order number: N SR-1-06 1874
22900 10 PC 1120000290 276,38 100 PC 27,64

SPAL-DUEB-6S-M-W2

SPAL/DUEB 6 S M W2

packed per each item

Product description: weld plate

Export - Customs tariff no.: 73269098
Country of origin: Germany''')
#doc212SR-1-06 1874 22900 10 1120000290 276,38 100  73269098 Germany
print("doc212",doc212[5: 8], doc212[8: 9], doc212[10: 11], doc212[11: 12], doc212[13: 14], doc212[14:15], doc212[15:16] ,doc212[17:18], doc212[53: 54], doc212[59: 60]) 
doc212.ents = [Span(doc212, 5, 8, label="CONTRACT"), 
    Span(doc212, 8, 9, label="CONTRACT1"), 
    Span(doc212, 10, 11, label="POS"), 
    Span(doc212, 11, 12, label="AMOUNT"), 
    Span(doc212, 13, 14, label="ARTICLE"), 
    Span(doc212, 14, 15, label="PRICE"), 
    Span(doc212, 15, 16, label="UNIT"), 
    Span(doc212, 17, 18, label="SUM"), 
    Span(doc212, 53, 54, label="TARIFF"), 
    Span(doc212, 59, 60, label="COUNTRY")] 
docs.append(doc212)


doc214 = nlp('''Purchase order number: N SR-1-06 1878
23100 56 РС 1130004021 4,09 100 РС 2,29

AS-M6x35-DIN931/933-8.8-W3
AS-M6X35-DIN931/933-8.8-W3
packed per each item

Product description: screw

Export - Customs tariff по.: 73181588
Country of origin: Turkey''')
#doc214SR-1-06 1878 23100 56 1130004021 4,09 100  73181588 Turkey
print("doc214",doc214[5: 8], doc214[8: 9], doc214[10: 11], doc214[11: 12], doc214[13: 14], doc214[14:15], doc214[15:16] ,doc214[17:18], doc214[56: 57], doc214[62: 63]) 
doc214.ents = [Span(doc214, 5, 8, label="CONTRACT"), 
    Span(doc214, 8, 9, label="CONTRACT1"), 
    Span(doc214, 10, 11, label="POS"), 
    Span(doc214, 11, 12, label="AMOUNT"), 
    Span(doc214, 13, 14, label="ARTICLE"), 
    Span(doc214, 14, 15, label="PRICE"), 
    Span(doc214, 15, 16, label="UNIT"), 
    Span(doc214, 17, 18, label="SUM"), 
    Span(doc214, 56, 57, label="TARIFF"), 
    Span(doc214, 62, 63, label="COUNTRY")] 
docs.append(doc214)


doc215 = nlp('''Purchase order number: N SR-1-06 1878
23200 48 РС 1130004280 5,08 100 РС 2,44

AS-M8x35-DIN931/933-8.8-W3
AS-M8X35-DIN931/933-8.8-W3
packed per each item

Product description: screw

Export - Customs tariff по.: 73181588
Country of origin: Origin''')
#doc215SR-1-06 1878 23200 48 1130004280 5,08 100  73181588 Origin
print("doc215",doc215[5: 8], doc215[8: 9], doc215[10: 11], doc215[11: 12], doc215[13: 14], doc215[14:15], doc215[15:16] ,doc215[17:18], doc215[56: 57], doc215[62: 63]) 
doc215.ents = [Span(doc215, 5, 8, label="CONTRACT"), 
    Span(doc215, 8, 9, label="CONTRACT1"), 
    Span(doc215, 10, 11, label="POS"), 
    Span(doc215, 11, 12, label="AMOUNT"), 
    Span(doc215, 13, 14, label="ARTICLE"), 
    Span(doc215, 14, 15, label="PRICE"), 
    Span(doc215, 15, 16, label="UNIT"), 
    Span(doc215, 17, 18, label="SUM"), 
    Span(doc215, 56, 57, label="TARIFF"), 
    Span(doc215, 62, 63, label="COUNTRY")] 
docs.append(doc215)


doc216 = nlp('''Purchase order number: N SR-1-06 1878
23300 25 РС 1130005333 21,69 100 РС 5,42


Description

216-PP

216 PP

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc216SR-1-06 1878 23300 25 1130005333 21,69 100  39269097 Germany
print("doc216",doc216[5: 8], doc216[8: 9], doc216[10: 11], doc216[11: 12], doc216[13: 14], doc216[14:15], doc216[15:16] ,doc216[17:18], doc216[46: 47], doc216[52: 53]) 
doc216.ents = [Span(doc216, 5, 8, label="CONTRACT"), 
    Span(doc216, 8, 9, label="CONTRACT1"), 
    Span(doc216, 10, 11, label="POS"), 
    Span(doc216, 11, 12, label="AMOUNT"), 
    Span(doc216, 13, 14, label="ARTICLE"), 
    Span(doc216, 14, 15, label="PRICE"), 
    Span(doc216, 15, 16, label="UNIT"), 
    Span(doc216, 17, 18, label="SUM"), 
    Span(doc216, 46, 47, label="TARIFF"), 
    Span(doc216, 52, 53, label="COUNTRY")] 
docs.append(doc216)


doc217 = nlp('''Purchase order number: N SR-1-06 1878
23400 50 PC 1130000261 7,39 100 PC 3,70
DP-2-W3
DP 2 W3

packed per each item

Product description: cover plate

Export - Customs tariff no.: 73269098
Country of origin: Germany''')
#doc217SR-1-06 1878 23400 50 1130000261 7,39 100  73269098 Germany
print("doc217",doc217[5: 8], doc217[8: 9], doc217[10: 11], doc217[11: 12], doc217[13: 14], doc217[14:15], doc217[15:16] ,doc217[17:18], doc217[45: 46], doc217[51: 52]) 
doc217.ents = [Span(doc217, 5, 8, label="CONTRACT"), 
    Span(doc217, 8, 9, label="CONTRACT1"), 
    Span(doc217, 10, 11, label="POS"), 
    Span(doc217, 11, 12, label="AMOUNT"), 
    Span(doc217, 13, 14, label="ARTICLE"), 
    Span(doc217, 14, 15, label="PRICE"), 
    Span(doc217, 15, 16, label="UNIT"), 
    Span(doc217, 17, 18, label="SUM"), 
    Span(doc217, 45, 46, label="TARIFF"), 
    Span(doc217, 51, 52, label="COUNTRY")] 
docs.append(doc217)


doc218 = nlp('''Purchase order number: N SR-1-06 1878
23500 50 РС 1120001156 26,58 100 РС 13,29
SP-2-M-W2
SP 2 M W2

packed per each item

Product description: weld plate

Export - Customs tariff no.: 73269098
Country of origin: Germany''')
#doc218SR-1-06 1878 23500 50 1120001156 26,58 100  73269098 Germany
print("doc218",doc218[5: 8], doc218[8: 9], doc218[10: 11], doc218[11: 12], doc218[13: 14], doc218[14:15], doc218[15:16] ,doc218[17:18], doc218[48: 49], doc218[54: 55]) 
doc218.ents = [Span(doc218, 5, 8, label="CONTRACT"), 
    Span(doc218, 8, 9, label="CONTRACT1"), 
    Span(doc218, 10, 11, label="POS"), 
    Span(doc218, 11, 12, label="AMOUNT"), 
    Span(doc218, 13, 14, label="ARTICLE"), 
    Span(doc218, 14, 15, label="PRICE"), 
    Span(doc218, 15, 16, label="UNIT"), 
    Span(doc218, 17, 18, label="SUM"), 
    Span(doc218, 48, 49, label="TARIFF"), 
    Span(doc218, 54, 55, label="COUNTRY")] 
docs.append(doc218)


doc219 = nlp('''Purchase order number: N SR-1-06 1878
23600 160 PC 6010000757 (*) 83,52 100 PC 133,63


Description

FI-G-10L-W3-MS

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc219SR-1-06 1878 23600 160 6010000757 83,52 100  73079910 Germany
print("doc219",doc219[5: 8], doc219[8: 9], doc219[10: 11], doc219[11: 12], doc219[13: 14], doc219[17:18], doc219[18:19] ,doc219[20:21], doc219[49: 50], doc219[55: 56]) 
doc219.ents = [Span(doc219, 5, 8, label="CONTRACT"), 
    Span(doc219, 8, 9, label="CONTRACT1"), 
    Span(doc219, 10, 11, label="POS"), 
    Span(doc219, 11, 12, label="AMOUNT"), 
    Span(doc219, 13, 14, label="ARTICLE"), 
    Span(doc219, 17, 18, label="PRICE"), 
    Span(doc219, 18, 19, label="UNIT"), 
    Span(doc219, 20, 21, label="SUM"), 
    Span(doc219, 49, 50, label="TARIFF"), 
    Span(doc219, 55, 56, label="COUNTRY")] 
docs.append(doc219)


doc220 = nlp('''Purchase order number: N SR-1-06 1878
23700 60 РС 6010000768 (*) 124,51 100 PC 74,71

FI-G-12S-W3-MS

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc220SR-1-06 1878 23700 60 6010000768 124,51 100  73079910 Germany
print("doc220",doc220[5: 8], doc220[8: 9], doc220[10: 11], doc220[11: 12], doc220[13: 14], doc220[17:18], doc220[18:19] ,doc220[20:21], doc220[47: 48], doc220[53: 54]) 
doc220.ents = [Span(doc220, 5, 8, label="CONTRACT"), 
    Span(doc220, 8, 9, label="CONTRACT1"), 
    Span(doc220, 10, 11, label="POS"), 
    Span(doc220, 11, 12, label="AMOUNT"), 
    Span(doc220, 13, 14, label="ARTICLE"), 
    Span(doc220, 17, 18, label="PRICE"), 
    Span(doc220, 18, 19, label="UNIT"), 
    Span(doc220, 20, 21, label="SUM"), 
    Span(doc220, 47, 48, label="TARIFF"), 
    Span(doc220, 53, 54, label="COUNTRY")] 
docs.append(doc220)


doc221 = nlp('''Purchase order number: N SR-1-06 1878
23800 35 PC 6010000760 (*) 218,60 100 PC 76,51

FI-G-18L-W3-MS

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc221SR-1-06 1878 23800 35 6010000760 218,60 100  73079910 Germany
print("doc221",doc221[5: 8], doc221[8: 9], doc221[10: 11], doc221[11: 12], doc221[13: 14], doc221[17:18], doc221[18:19] ,doc221[20:21], doc221[47: 48], doc221[53: 54]) 
doc221.ents = [Span(doc221, 5, 8, label="CONTRACT"), 
    Span(doc221, 8, 9, label="CONTRACT1"), 
    Span(doc221, 10, 11, label="POS"), 
    Span(doc221, 11, 12, label="AMOUNT"), 
    Span(doc221, 13, 14, label="ARTICLE"), 
    Span(doc221, 17, 18, label="PRICE"), 
    Span(doc221, 18, 19, label="UNIT"), 
    Span(doc221, 20, 21, label="SUM"), 
    Span(doc221, 47, 48, label="TARIFF"), 
    Span(doc221, 53, 54, label="COUNTRY")] 
docs.append(doc221)


doc222 = nlp('''Purchase order number: N SR-1-06 1878
23900 6 PC 6010001403 (*) 173,06 100 PC 10,38

FI-GE-18LM18x1.5-WD-B-W3-MS
FI-GE-18LM18x1,5-WD-B-W3-MS
packed per each item


Description

Product description: fitting
Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc222SR-1-06 1878 23900 6 6010001403 173,06 100  73079910 Germany
print("doc222",doc222[5: 8], doc222[8: 9], doc222[10: 11], doc222[11: 12], doc222[13: 14], doc222[17:18], doc222[18:19] ,doc222[20:21], doc222[65: 66], doc222[71: 72]) 
doc222.ents = [Span(doc222, 5, 8, label="CONTRACT"), 
    Span(doc222, 8, 9, label="CONTRACT1"), 
    Span(doc222, 10, 11, label="POS"), 
    Span(doc222, 11, 12, label="AMOUNT"), 
    Span(doc222, 13, 14, label="ARTICLE"), 
    Span(doc222, 17, 18, label="PRICE"), 
    Span(doc222, 18, 19, label="UNIT"), 
    Span(doc222, 20, 21, label="SUM"), 
    Span(doc222, 65, 66, label="TARIFF"), 
    Span(doc222, 71, 72, label="COUNTRY")] 
docs.append(doc222)


doc223 = nlp('''Purchase order number: N SR-1-06 1878
24000 12 PC 6010001524 (*) 371,79 100 PC 44,61

FI-GE-22LR1/2-WD-B-W3-MS

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc223SR-1-06 1878 24000 12 6010001524 371,79 100  73079910 Germany
print("doc223",doc223[5: 8], doc223[8: 9], doc223[10: 11], doc223[11: 12], doc223[13: 14], doc223[17:18], doc223[18:19] ,doc223[20:21], doc223[51: 52], doc223[57: 58]) 
doc223.ents = [Span(doc223, 5, 8, label="CONTRACT"), 
    Span(doc223, 8, 9, label="CONTRACT1"), 
    Span(doc223, 10, 11, label="POS"), 
    Span(doc223, 11, 12, label="AMOUNT"), 
    Span(doc223, 13, 14, label="ARTICLE"), 
    Span(doc223, 17, 18, label="PRICE"), 
    Span(doc223, 18, 19, label="UNIT"), 
    Span(doc223, 20, 21, label="SUM"), 
    Span(doc223, 51, 52, label="TARIFF"), 
    Span(doc223, 57, 58, label="COUNTRY")] 
docs.append(doc223)


doc224 = nlp('''Purchase order number: N SR-1-06 1879
24100 2 РС 6010001909 (*) 526,22 100 PC 10,52

FI-REDS-30/20S-W3-SV

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc224SR-1-06 1879 24100 2 6010001909 526,22 100  73079910 Germany
print("doc224",doc224[5: 8], doc224[8: 9], doc224[10: 11], doc224[11: 12], doc224[13: 14], doc224[17:18], doc224[18:19] ,doc224[20:21], doc224[47: 48], doc224[53: 54]) 
doc224.ents = [Span(doc224, 5, 8, label="CONTRACT"), 
    Span(doc224, 8, 9, label="CONTRACT1"), 
    Span(doc224, 10, 11, label="POS"), 
    Span(doc224, 11, 12, label="AMOUNT"), 
    Span(doc224, 13, 14, label="ARTICLE"), 
    Span(doc224, 17, 18, label="PRICE"), 
    Span(doc224, 18, 19, label="UNIT"), 
    Span(doc224, 20, 21, label="SUM"), 
    Span(doc224, 47, 48, label="TARIFF"), 
    Span(doc224, 53, 54, label="COUNTRY")] 
docs.append(doc224)


doc225 = nlp('''Purchase order number: N SR-1-06 1880
24200 2 РС 1910000388 11,23 1 РС 22,46

SPG-063-00250-01 -S-B04

SPG 063-00250-01-S-B04
PRESSURE GAUGE

packed per each item

Product description: Pressure gauge


Description

Export - Customs tariff no.: 90262040
Country of origin: Poland''')
#doc225SR-1-06 1880 24200 2 1910000388 11,23 1  90262040 Poland
print("doc225",doc225[5: 8], doc225[8: 9], doc225[10: 11], doc225[11: 12], doc225[13: 14], doc225[14:15], doc225[15:16] ,doc225[17:18], doc225[62: 63], doc225[68: 69]) 
doc225.ents = [Span(doc225, 5, 8, label="CONTRACT"), 
    Span(doc225, 8, 9, label="CONTRACT1"), 
    Span(doc225, 10, 11, label="POS"), 
    Span(doc225, 11, 12, label="AMOUNT"), 
    Span(doc225, 13, 14, label="ARTICLE"), 
    Span(doc225, 14, 15, label="PRICE"), 
    Span(doc225, 15, 16, label="UNIT"), 
    Span(doc225, 17, 18, label="SUM"), 
    Span(doc225, 62, 63, label="TARIFF"), 
    Span(doc225, 68, 69, label="COUNTRY")] 
docs.append(doc225)


doc226 = nlp('''Purchase order number: N SR-1-06 1880
24300 2 РС 6010003938 (*) 459,81 100 PC 9,20

FI-REDSD-16/14S-V-W3-DKO
FI-REDSD-16/14S-B-W3-DKO

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc226SR-1-06 1880 24300 2 6010003938 459,81 100  73079910 Germany
print("doc226",doc226[5: 8], doc226[8: 9], doc226[10: 11], doc226[11: 12], doc226[13: 14], doc226[17:18], doc226[18:19] ,doc226[20:21], doc226[59: 60], doc226[65: 66]) 
doc226.ents = [Span(doc226, 5, 8, label="CONTRACT"), 
    Span(doc226, 8, 9, label="CONTRACT1"), 
    Span(doc226, 10, 11, label="POS"), 
    Span(doc226, 11, 12, label="AMOUNT"), 
    Span(doc226, 13, 14, label="ARTICLE"), 
    Span(doc226, 17, 18, label="PRICE"), 
    Span(doc226, 18, 19, label="UNIT"), 
    Span(doc226, 20, 21, label="SUM"), 
    Span(doc226, 59, 60, label="TARIFF"), 
    Span(doc226, 65, 66, label="COUNTRY")] 
docs.append(doc226)


doc227 = nlp('''Purchase order number: N SR-1-06 1880
24400 2 РС 6010004089 (*) 657,79 100 PC 13,16

FI-REDSD-20/14S-V-W3-DKO
FI-REDSD-20/14S-B-W3-DKO

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc227SR-1-06 1880 24400 2 6010004089 657,79 100  73079910 Germany
print("doc227",doc227[5: 8], doc227[8: 9], doc227[10: 11], doc227[11: 12], doc227[13: 14], doc227[17:18], doc227[18:19] ,doc227[20:21], doc227[59: 60], doc227[65: 66]) 
doc227.ents = [Span(doc227, 5, 8, label="CONTRACT"), 
    Span(doc227, 8, 9, label="CONTRACT1"), 
    Span(doc227, 10, 11, label="POS"), 
    Span(doc227, 11, 12, label="AMOUNT"), 
    Span(doc227, 13, 14, label="ARTICLE"), 
    Span(doc227, 17, 18, label="PRICE"), 
    Span(doc227, 18, 19, label="UNIT"), 
    Span(doc227, 20, 21, label="SUM"), 
    Span(doc227, 59, 60, label="TARIFF"), 
    Span(doc227, 65, 66, label="COUNTRY")] 
docs.append(doc227)


doc228 = nlp('''Purchase order number: N SR-1-06 1880
24500 2 PC 6010003975 (*) 1.099,49 100 PC 21,99

FI-REDSD-30/14S-V-W3-DKO
FI-REDSD-30/14S-B-W3-DKO
packed per each item


Description

Product description: fitting
Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc228SR-1-06 1880 24500 2 6010003975 1.099,49 100  73079910 Germany
print("doc228",doc228[5: 8], doc228[8: 9], doc228[10: 11], doc228[11: 12], doc228[13: 14], doc228[17:18], doc228[18:19] ,doc228[20:21], doc228[61: 62], doc228[67: 68]) 
doc228.ents = [Span(doc228, 5, 8, label="CONTRACT"), 
    Span(doc228, 8, 9, label="CONTRACT1"), 
    Span(doc228, 10, 11, label="POS"), 
    Span(doc228, 11, 12, label="AMOUNT"), 
    Span(doc228, 13, 14, label="ARTICLE"), 
    Span(doc228, 17, 18, label="PRICE"), 
    Span(doc228, 18, 19, label="UNIT"), 
    Span(doc228, 20, 21, label="SUM"), 
    Span(doc228, 61, 62, label="TARIFF"), 
    Span(doc228, 67, 68, label="COUNTRY")] 
docs.append(doc228)


doc229 = nlp('''Purchase order number: N SR-1-06 1880
24600 1 PC 6030002479 (*) 1.826,46 100 PC 18,26

FI-GA-30SM-W3

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc229SR-1-06 1880 24600 1 6030002479 1.826,46 100  73079910 Germany
print("doc229",doc229[5: 8], doc229[8: 9], doc229[10: 11], doc229[11: 12], doc229[13: 14], doc229[17:18], doc229[18:19] ,doc229[20:21], doc229[45: 46], doc229[51: 52]) 
doc229.ents = [Span(doc229, 5, 8, label="CONTRACT"), 
    Span(doc229, 8, 9, label="CONTRACT1"), 
    Span(doc229, 10, 11, label="POS"), 
    Span(doc229, 11, 12, label="AMOUNT"), 
    Span(doc229, 13, 14, label="ARTICLE"), 
    Span(doc229, 17, 18, label="PRICE"), 
    Span(doc229, 18, 19, label="UNIT"), 
    Span(doc229, 20, 21, label="SUM"), 
    Span(doc229, 45, 46, label="TARIFF"), 
    Span(doc229, 51, 52, label="COUNTRY")] 
docs.append(doc229)


doc230 = nlp('''Purchase order number: N SR-1-06 1880
24700 2 РС 6030003859 324,75 100 PC 6,50
FI-T-16S-W3

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc230SR-1-06 1880 24700 2 6030003859 324,75 100  73079910 Germany
print("doc230",doc230[5: 8], doc230[8: 9], doc230[10: 11], doc230[11: 12], doc230[13: 14], doc230[14:15], doc230[15:16] ,doc230[17:18], doc230[42: 43], doc230[48: 49]) 
doc230.ents = [Span(doc230, 5, 8, label="CONTRACT"), 
    Span(doc230, 8, 9, label="CONTRACT1"), 
    Span(doc230, 10, 11, label="POS"), 
    Span(doc230, 11, 12, label="AMOUNT"), 
    Span(doc230, 13, 14, label="ARTICLE"), 
    Span(doc230, 14, 15, label="PRICE"), 
    Span(doc230, 15, 16, label="UNIT"), 
    Span(doc230, 17, 18, label="SUM"), 
    Span(doc230, 42, 43, label="TARIFF"), 
    Span(doc230, 48, 49, label="COUNTRY")] 
docs.append(doc230)


doc231 = nlp('''Purchase order number: N SR-1-06 1881
24800 216 PC 1130004020 3,93 100 PC 8,49

AS-M6x30-DIN931/933-8.8-W3
AS-M6X30-DIN931/933-8.8-W3
packed per each item

Product description: screw

Export - Customs tariff по.: 73181588


Description

Country of origin: Turkey''')
#doc231SR-1-06 1881 24800 216 1130004020 3,93 100  73181588 Turkey
print("doc231",doc231[5: 8], doc231[8: 9], doc231[10: 11], doc231[11: 12], doc231[13: 14], doc231[14:15], doc231[15:16] ,doc231[17:18], doc231[56: 57], doc231[64: 65]) 
doc231.ents = [Span(doc231, 5, 8, label="CONTRACT"), 
    Span(doc231, 8, 9, label="CONTRACT1"), 
    Span(doc231, 10, 11, label="POS"), 
    Span(doc231, 11, 12, label="AMOUNT"), 
    Span(doc231, 13, 14, label="ARTICLE"), 
    Span(doc231, 14, 15, label="PRICE"), 
    Span(doc231, 15, 16, label="UNIT"), 
    Span(doc231, 17, 18, label="SUM"), 
    Span(doc231, 56, 57, label="TARIFF"), 
    Span(doc231, 64, 65, label="COUNTRY")] 
docs.append(doc231)


doc232 = nlp('''Purchase order number: N SR-1-06 1881
24900 136 PC 1130004021 4,09 100 PC 5,56

AS-M6x35-DIN931/933-8.8-W3
AS-M6X35-DIN931/933-8.8-W3
packed per each item

Product description: screw

Export - Customs tariff по.: 73181588
Country of origin: Turkey''')
#doc232SR-1-06 1881 24900 136 1130004021 4,09 100  73181588 Turkey
print("doc232",doc232[5: 8], doc232[8: 9], doc232[10: 11], doc232[11: 12], doc232[13: 14], doc232[14:15], doc232[15:16] ,doc232[17:18], doc232[56: 57], doc232[62: 63]) 
doc232.ents = [Span(doc232, 5, 8, label="CONTRACT"), 
    Span(doc232, 8, 9, label="CONTRACT1"), 
    Span(doc232, 10, 11, label="POS"), 
    Span(doc232, 11, 12, label="AMOUNT"), 
    Span(doc232, 13, 14, label="ARTICLE"), 
    Span(doc232, 14, 15, label="PRICE"), 
    Span(doc232, 15, 16, label="UNIT"), 
    Span(doc232, 17, 18, label="SUM"), 
    Span(doc232, 56, 57, label="TARIFF"), 
    Span(doc232, 62, 63, label="COUNTRY")] 
docs.append(doc232)


doc233 = nlp('''Purchase order number: N SR-1-06 1881
25000 40 РС 1130004022 4,30 100 PC 1,72

AS-M6x40-DIN931/933-8.8-W3
AS-M6X40-DIN931/933-8.8-W3
packed per each item

Product description: screw

Export - Customs tariff по.: 73181588
Country of origin: Taiwan''')
#doc233SR-1-06 1881 25000 40 1130004022 4,30 100  73181588 Taiwan
print("doc233",doc233[5: 8], doc233[8: 9], doc233[10: 11], doc233[11: 12], doc233[13: 14], doc233[14:15], doc233[15:16] ,doc233[17:18], doc233[56: 57], doc233[62: 63]) 
doc233.ents = [Span(doc233, 5, 8, label="CONTRACT"), 
    Span(doc233, 8, 9, label="CONTRACT1"), 
    Span(doc233, 10, 11, label="POS"), 
    Span(doc233, 11, 12, label="AMOUNT"), 
    Span(doc233, 13, 14, label="ARTICLE"), 
    Span(doc233, 14, 15, label="PRICE"), 
    Span(doc233, 15, 16, label="UNIT"), 
    Span(doc233, 17, 18, label="SUM"), 
    Span(doc233, 56, 57, label="TARIFF"), 
    Span(doc233, 62, 63, label="COUNTRY")] 
docs.append(doc233)


doc234 = nlp('''Purchase order number: N SR-1-06 1881
25100 88 РС 1130004024 5,48 100 PC 4,82

AS-M6x60-DIN931/933-8.8-W3
AS-M6X60-DIN931/933-8.8-W3
packed per each item

Product description: screw

Export - Customs tariff по.: 73181588


Description

Country of origin: Turkey''')
#doc234SR-1-06 1881 25100 88 1130004024 5,48 100  73181588 Turkey
print("doc234",doc234[5: 8], doc234[8: 9], doc234[10: 11], doc234[11: 12], doc234[13: 14], doc234[14:15], doc234[15:16] ,doc234[17:18], doc234[56: 57], doc234[64: 65]) 
doc234.ents = [Span(doc234, 5, 8, label="CONTRACT"), 
    Span(doc234, 8, 9, label="CONTRACT1"), 
    Span(doc234, 10, 11, label="POS"), 
    Span(doc234, 11, 12, label="AMOUNT"), 
    Span(doc234, 13, 14, label="ARTICLE"), 
    Span(doc234, 14, 15, label="PRICE"), 
    Span(doc234, 15, 16, label="UNIT"), 
    Span(doc234, 17, 18, label="SUM"), 
    Span(doc234, 56, 57, label="TARIFF"), 
    Span(doc234, 64, 65, label="COUNTRY")] 
docs.append(doc234)


doc235 = nlp('''Purchase order number: N SR-1-06 1881
25200 400 PC 6030003814 15,60 100 PC 62,40
FI-M-12L-W3

packed per each item

Product description: nuts

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc235SR-1-06 1881 25200 400 6030003814 15,60 100  73079910 Germany
print("doc235",doc235[5: 8], doc235[8: 9], doc235[10: 11], doc235[11: 12], doc235[13: 14], doc235[14:15], doc235[15:16] ,doc235[17:18], doc235[42: 43], doc235[48: 49]) 
doc235.ents = [Span(doc235, 5, 8, label="CONTRACT"), 
    Span(doc235, 8, 9, label="CONTRACT1"), 
    Span(doc235, 10, 11, label="POS"), 
    Span(doc235, 11, 12, label="AMOUNT"), 
    Span(doc235, 13, 14, label="ARTICLE"), 
    Span(doc235, 14, 15, label="PRICE"), 
    Span(doc235, 15, 16, label="UNIT"), 
    Span(doc235, 17, 18, label="SUM"), 
    Span(doc235, 42, 43, label="TARIFF"), 
    Span(doc235, 48, 49, label="COUNTRY")] 
docs.append(doc235)


doc236 = nlp('''Purchase order number: N SR-1-06 1881
25300 400 PC 6030003816 46,28 100 PC 185,12
FI-M-18L-W3

packed per each item

Product description: nuts

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc236SR-1-06 1881 25300 400 6030003816 46,28 100  73079910 Germany
print("doc236",doc236[5: 8], doc236[8: 9], doc236[10: 11], doc236[11: 12], doc236[13: 14], doc236[14:15], doc236[15:16] ,doc236[17:18], doc236[42: 43], doc236[48: 49]) 
doc236.ents = [Span(doc236, 5, 8, label="CONTRACT"), 
    Span(doc236, 8, 9, label="CONTRACT1"), 
    Span(doc236, 10, 11, label="POS"), 
    Span(doc236, 11, 12, label="AMOUNT"), 
    Span(doc236, 13, 14, label="ARTICLE"), 
    Span(doc236, 14, 15, label="PRICE"), 
    Span(doc236, 15, 16, label="UNIT"), 
    Span(doc236, 17, 18, label="SUM"), 
    Span(doc236, 42, 43, label="TARIFF"), 
    Span(doc236, 48, 49, label="COUNTRY")] 
docs.append(doc236)


doc237 = nlp('''Purchase order number: N SR-1-06 1881
25400 120 PC 6030003817 63,90 100 PC 76,68
FI-M-22L-W3

packed per each item

Product description: nuts

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc237SR-1-06 1881 25400 120 6030003817 63,90 100  73079910 Germany
print("doc237",doc237[5: 8], doc237[8: 9], doc237[10: 11], doc237[11: 12], doc237[13: 14], doc237[14:15], doc237[15:16] ,doc237[17:18], doc237[42: 43], doc237[48: 49]) 
doc237.ents = [Span(doc237, 5, 8, label="CONTRACT"), 
    Span(doc237, 8, 9, label="CONTRACT1"), 
    Span(doc237, 10, 11, label="POS"), 
    Span(doc237, 11, 12, label="AMOUNT"), 
    Span(doc237, 13, 14, label="ARTICLE"), 
    Span(doc237, 14, 15, label="PRICE"), 
    Span(doc237, 15, 16, label="UNIT"), 
    Span(doc237, 17, 18, label="SUM"), 
    Span(doc237, 42, 43, label="TARIFF"), 
    Span(doc237, 48, 49, label="COUNTRY")] 
docs.append(doc237)


doc238 = nlp('''Purchase order number: N SR-1-06 1881
25500 150 PC 6030003819 152,44 100 PC 228,66
FI-M-35L-W3

packed per each item

Product description: nuts

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc238SR-1-06 1881 25500 150 6030003819 152,44 100  73079910 Germany
print("doc238",doc238[5: 8], doc238[8: 9], doc238[10: 11], doc238[11: 12], doc238[13: 14], doc238[14:15], doc238[15:16] ,doc238[17:18], doc238[42: 43], doc238[48: 49]) 
doc238.ents = [Span(doc238, 5, 8, label="CONTRACT"), 
    Span(doc238, 8, 9, label="CONTRACT1"), 
    Span(doc238, 10, 11, label="POS"), 
    Span(doc238, 11, 12, label="AMOUNT"), 
    Span(doc238, 13, 14, label="ARTICLE"), 
    Span(doc238, 14, 15, label="PRICE"), 
    Span(doc238, 15, 16, label="UNIT"), 
    Span(doc238, 17, 18, label="SUM"), 
    Span(doc238, 42, 43, label="TARIFF"), 
    Span(doc238, 48, 49, label="COUNTRY")] 
docs.append(doc238)


doc239 = nlp('''Purchase order number: N SR-1-06 1881
25600 480 PC 6100152347 12,73 100 PC 61,10

SM-1-8/1D-M-W3/2

packed per each item

Customer ID-No.: 000000001120001932
Product description: nuts

Export - Customs tariff no.: 73181692
Country of origin: Germany''')
#doc239SR-1-06 1881 25600 480 6100152347 12,73 100  73181692 Germany
print("doc239",doc239[5: 8], doc239[8: 9], doc239[10: 11], doc239[11: 12], doc239[13: 14], doc239[14:15], doc239[15:16] ,doc239[17:18], doc239[52: 53], doc239[58: 59]) 
doc239.ents = [Span(doc239, 5, 8, label="CONTRACT"), 
    Span(doc239, 8, 9, label="CONTRACT1"), 
    Span(doc239, 10, 11, label="POS"), 
    Span(doc239, 11, 12, label="AMOUNT"), 
    Span(doc239, 13, 14, label="ARTICLE"), 
    Span(doc239, 14, 15, label="PRICE"), 
    Span(doc239, 15, 16, label="UNIT"), 
    Span(doc239, 17, 18, label="SUM"), 
    Span(doc239, 52, 53, label="TARIFF"), 
    Span(doc239, 58, 59, label="COUNTRY")] 
docs.append(doc239)


doc240 = nlp('''Purchase order number: N SR-1-06 1881
25700 8 РС 1130021630 71,56 100 РС 5,72

DIN1593-43-W66

DIN 1593-43 W66

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 73269098
Country of origin: Germany''')
#doc240SR-1-06 1881 25700 8 1130021630 71,56 100  73269098 Germany
print("doc240",doc240[5: 8], doc240[8: 9], doc240[10: 11], doc240[11: 12], doc240[13: 14], doc240[14:15], doc240[15:16] ,doc240[17:18], doc240[49: 50], doc240[55: 56]) 
doc240.ents = [Span(doc240, 5, 8, label="CONTRACT"), 
    Span(doc240, 8, 9, label="CONTRACT1"), 
    Span(doc240, 10, 11, label="POS"), 
    Span(doc240, 11, 12, label="AMOUNT"), 
    Span(doc240, 13, 14, label="ARTICLE"), 
    Span(doc240, 14, 15, label="PRICE"), 
    Span(doc240, 15, 16, label="UNIT"), 
    Span(doc240, 17, 18, label="SUM"), 
    Span(doc240, 49, 50, label="TARIFF"), 
    Span(doc240, 55, 56, label="COUNTRY")] 
docs.append(doc240)


doc241 = nlp('''Purchase order number: N SR-1-06 1881
25800 50 РС 1130005383 36,71 100 РС 18,36
218-РА
218 РА
packed per each item
Product description: Pipe clamp
Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc241SR-1-06 1881 25800 50 1130005383 36,71 100  39269097 Germany
print("doc241",doc241[5: 8], doc241[8: 9], doc241[10: 11], doc241[11: 12], doc241[13: 14], doc241[14:15], doc241[15:16] ,doc241[17:18], doc241[44: 45], doc241[50: 51]) 
doc241.ents = [Span(doc241, 5, 8, label="CONTRACT"), 
    Span(doc241, 8, 9, label="CONTRACT1"), 
    Span(doc241, 10, 11, label="POS"), 
    Span(doc241, 11, 12, label="AMOUNT"), 
    Span(doc241, 13, 14, label="ARTICLE"), 
    Span(doc241, 14, 15, label="PRICE"), 
    Span(doc241, 15, 16, label="UNIT"), 
    Span(doc241, 17, 18, label="SUM"), 
    Span(doc241, 44, 45, label="TARIFF"), 
    Span(doc241, 50, 51, label="COUNTRY")] 
docs.append(doc241)


doc242 = nlp('''Purchase order number: N SR-1-06 1881
25900 25 РС 1130005577 41,59 100 РС 10,40
322-РА
322 РА

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc242SR-1-06 1881 25900 25 1130005577 41,59 100  39269097 Germany
print("doc242",doc242[5: 8], doc242[8: 9], doc242[10: 11], doc242[11: 12], doc242[13: 14], doc242[14:15], doc242[15:16] ,doc242[17:18], doc242[44: 45], doc242[50: 51]) 
doc242.ents = [Span(doc242, 5, 8, label="CONTRACT"), 
    Span(doc242, 8, 9, label="CONTRACT1"), 
    Span(doc242, 10, 11, label="POS"), 
    Span(doc242, 11, 12, label="AMOUNT"), 
    Span(doc242, 13, 14, label="ARTICLE"), 
    Span(doc242, 14, 15, label="PRICE"), 
    Span(doc242, 15, 16, label="UNIT"), 
    Span(doc242, 17, 18, label="SUM"), 
    Span(doc242, 44, 45, label="TARIFF"), 
    Span(doc242, 50, 51, label="COUNTRY")] 
docs.append(doc242)


doc243 = nlp('''Purchase order number: N SR-1-06 1881
26000 50 РС 1130006066 85,35 100 PC 42,68
542-РА
542 РА

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc243SR-1-06 1881 26000 50 1130006066 85,35 100  39269097 Germany
print("doc243",doc243[5: 8], doc243[8: 9], doc243[10: 11], doc243[11: 12], doc243[13: 14], doc243[14:15], doc243[15:16] ,doc243[17:18], doc243[44: 45], doc243[50: 51]) 
doc243.ents = [Span(doc243, 5, 8, label="CONTRACT"), 
    Span(doc243, 8, 9, label="CONTRACT1"), 
    Span(doc243, 10, 11, label="POS"), 
    Span(doc243, 11, 12, label="AMOUNT"), 
    Span(doc243, 13, 14, label="ARTICLE"), 
    Span(doc243, 14, 15, label="PRICE"), 
    Span(doc243, 15, 16, label="UNIT"), 
    Span(doc243, 17, 18, label="SUM"), 
    Span(doc243, 44, 45, label="TARIFF"), 
    Span(doc243, 50, 51, label="COUNTRY")] 
docs.append(doc243)


doc244 = nlp('''Purchase order number: N SR-1-06 1881
26100 125 PC 1130000258 6,83 100 PC 8,54
DP-1a-W3
DP 1a W3
packed per each item
Product description: cover plate
Export - Customs tariff no.: 73269098
Country of origin: Germany''')
#doc244SR-1-06 1881 26100 125 1130000258 6,83 100  73269098 Germany
print("doc244",doc244[5: 8], doc244[8: 9], doc244[10: 11], doc244[11: 12], doc244[13: 14], doc244[14:15], doc244[15:16] ,doc244[17:18], doc244[45: 46], doc244[51: 52]) 
doc244.ents = [Span(doc244, 5, 8, label="CONTRACT"), 
    Span(doc244, 8, 9, label="CONTRACT1"), 
    Span(doc244, 10, 11, label="POS"), 
    Span(doc244, 11, 12, label="AMOUNT"), 
    Span(doc244, 13, 14, label="ARTICLE"), 
    Span(doc244, 14, 15, label="PRICE"), 
    Span(doc244, 15, 16, label="UNIT"), 
    Span(doc244, 17, 18, label="SUM"), 
    Span(doc244, 45, 46, label="TARIFF"), 
    Span(doc244, 51, 52, label="COUNTRY")] 
docs.append(doc244)


doc245 = nlp('''Purchase order number: N SR-1-06 1881
26200 75 РС 1130000261 7,39 100 РС 5,54
DP-2-W3
DP 2 W3

packed per each item

Product description: cover plate

Export - Customs tariff no.: 73269098
Country of origin: Germany''')
#doc245SR-1-06 1881 26200 75 1130000261 7,39 100  73269098 Germany
print("doc245",doc245[5: 8], doc245[8: 9], doc245[10: 11], doc245[11: 12], doc245[13: 14], doc245[14:15], doc245[15:16] ,doc245[17:18], doc245[45: 46], doc245[51: 52]) 
doc245.ents = [Span(doc245, 5, 8, label="CONTRACT"), 
    Span(doc245, 8, 9, label="CONTRACT1"), 
    Span(doc245, 10, 11, label="POS"), 
    Span(doc245, 11, 12, label="AMOUNT"), 
    Span(doc245, 13, 14, label="ARTICLE"), 
    Span(doc245, 14, 15, label="PRICE"), 
    Span(doc245, 15, 16, label="UNIT"), 
    Span(doc245, 17, 18, label="SUM"), 
    Span(doc245, 45, 46, label="TARIFF"), 
    Span(doc245, 51, 52, label="COUNTRY")] 
docs.append(doc245)


doc246 = nlp('''Purchase order number: N SR-1-06 1881
26300 6 PC 6030002937 (*) 98,62 100 PC 5,92

FI-RED-R3/8-R1/2-W3

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc246SR-1-06 1881 26300 6 6030002937 98,62 100  73079910 Germany
print("doc246",doc246[5: 8], doc246[8: 9], doc246[10: 11], doc246[11: 12], doc246[13: 14], doc246[17:18], doc246[18:19] ,doc246[20:21], doc246[49: 50], doc246[55: 56]) 
doc246.ents = [Span(doc246, 5, 8, label="CONTRACT"), 
    Span(doc246, 8, 9, label="CONTRACT1"), 
    Span(doc246, 10, 11, label="POS"), 
    Span(doc246, 11, 12, label="AMOUNT"), 
    Span(doc246, 13, 14, label="ARTICLE"), 
    Span(doc246, 17, 18, label="PRICE"), 
    Span(doc246, 18, 19, label="UNIT"), 
    Span(doc246, 20, 21, label="SUM"), 
    Span(doc246, 49, 50, label="TARIFF"), 
    Span(doc246, 55, 56, label="COUNTRY")] 
docs.append(doc246)


doc247 = nlp('''Purchase order number: N SR-1-06 1881
26400 16 PC 6010001896 (*) 355,94 100 PC 56,95

FI-REDS-14/12S-W3-SV

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc247SR-1-06 1881 26400 16 6010001896 355,94 100  73079910 Germany
print("doc247",doc247[5: 8], doc247[8: 9], doc247[10: 11], doc247[11: 12], doc247[13: 14], doc247[17:18], doc247[18:19] ,doc247[20:21], doc247[47: 48], doc247[53: 54]) 
doc247.ents = [Span(doc247, 5, 8, label="CONTRACT"), 
    Span(doc247, 8, 9, label="CONTRACT1"), 
    Span(doc247, 10, 11, label="POS"), 
    Span(doc247, 11, 12, label="AMOUNT"), 
    Span(doc247, 13, 14, label="ARTICLE"), 
    Span(doc247, 17, 18, label="PRICE"), 
    Span(doc247, 18, 19, label="UNIT"), 
    Span(doc247, 20, 21, label="SUM"), 
    Span(doc247, 47, 48, label="TARIFF"), 
    Span(doc247, 53, 54, label="COUNTRY")] 
docs.append(doc247)


doc248 = nlp('''Purchase order number: N SR-1-06 1881
26500 4 РС 6010001882 (*) 210,05 100 PC 8,40

FI-REDS-22/12L-W3-SV

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc248SR-1-06 1881 26500 4 6010001882 210,05 100  73079910 Germany
print("doc248",doc248[5: 8], doc248[8: 9], doc248[10: 11], doc248[11: 12], doc248[13: 14], doc248[17:18], doc248[18:19] ,doc248[20:21], doc248[47: 48], doc248[53: 54]) 
doc248.ents = [Span(doc248, 5, 8, label="CONTRACT"), 
    Span(doc248, 8, 9, label="CONTRACT1"), 
    Span(doc248, 10, 11, label="POS"), 
    Span(doc248, 11, 12, label="AMOUNT"), 
    Span(doc248, 13, 14, label="ARTICLE"), 
    Span(doc248, 17, 18, label="PRICE"), 
    Span(doc248, 18, 19, label="UNIT"), 
    Span(doc248, 20, 21, label="SUM"), 
    Span(doc248, 47, 48, label="TARIFF"), 
    Span(doc248, 53, 54, label="COUNTRY")] 
docs.append(doc248)


doc249 = nlp('''Purchase order number: N SR-1-06 1881
26600 8 PC 6010001884 (*) 210,05 100 PC 16,80

FI-REDS-22/18L-W3-SV

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc249SR-1-06 1881 26600 8 6010001884 210,05 100  73079910 Germany
print("doc249",doc249[5: 8], doc249[8: 9], doc249[10: 11], doc249[11: 12], doc249[13: 14], doc249[17:18], doc249[18:19] ,doc249[20:21], doc249[47: 48], doc249[53: 54]) 
doc249.ents = [Span(doc249, 5, 8, label="CONTRACT"), 
    Span(doc249, 8, 9, label="CONTRACT1"), 
    Span(doc249, 10, 11, label="POS"), 
    Span(doc249, 11, 12, label="AMOUNT"), 
    Span(doc249, 13, 14, label="ARTICLE"), 
    Span(doc249, 17, 18, label="PRICE"), 
    Span(doc249, 18, 19, label="UNIT"), 
    Span(doc249, 20, 21, label="SUM"), 
    Span(doc249, 47, 48, label="TARIFF"), 
    Span(doc249, 53, 54, label="COUNTRY")] 
docs.append(doc249)


doc250 = nlp('''Purchase order number: N SR-1-06 1881
26700 6 PC 6010003971 (*) 1.699,17 100 PC 101,95

FI-REDSD-35/12L-V-W3-DKO


Description

FI-REDSD-35/12L-B-W3-DKO

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc250SR-1-06 1881 26700 6 6010003971 1.699,17 100  73079910 Germany
print("doc250",doc250[5: 8], doc250[8: 9], doc250[10: 11], doc250[11: 12], doc250[13: 14], doc250[17:18], doc250[18:19] ,doc250[20:21], doc250[61: 62], doc250[67: 68]) 
doc250.ents = [Span(doc250, 5, 8, label="CONTRACT"), 
    Span(doc250, 8, 9, label="CONTRACT1"), 
    Span(doc250, 10, 11, label="POS"), 
    Span(doc250, 11, 12, label="AMOUNT"), 
    Span(doc250, 13, 14, label="ARTICLE"), 
    Span(doc250, 17, 18, label="PRICE"), 
    Span(doc250, 18, 19, label="UNIT"), 
    Span(doc250, 20, 21, label="SUM"), 
    Span(doc250, 61, 62, label="TARIFF"), 
    Span(doc250, 67, 68, label="COUNTRY")] 
docs.append(doc250)


doc251 = nlp('''Purchase order number: N SR-1-06 1881
26800 12 PC 6010001888 (*) 622,07 100 PC 74,65

FI-REDS-35/18L-W3-SV

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc251SR-1-06 1881 26800 12 6010001888 622,07 100  73079910 Germany
print("doc251",doc251[5: 8], doc251[8: 9], doc251[10: 11], doc251[11: 12], doc251[13: 14], doc251[17:18], doc251[18:19] ,doc251[20:21], doc251[47: 48], doc251[53: 54]) 
doc251.ents = [Span(doc251, 5, 8, label="CONTRACT"), 
    Span(doc251, 8, 9, label="CONTRACT1"), 
    Span(doc251, 10, 11, label="POS"), 
    Span(doc251, 11, 12, label="AMOUNT"), 
    Span(doc251, 13, 14, label="ARTICLE"), 
    Span(doc251, 17, 18, label="PRICE"), 
    Span(doc251, 18, 19, label="UNIT"), 
    Span(doc251, 20, 21, label="SUM"), 
    Span(doc251, 47, 48, label="TARIFF"), 
    Span(doc251, 53, 54, label="COUNTRY")] 
docs.append(doc251)


doc252 = nlp('''Purchase order number: N SR-1-06 1881
26900 4 РС 6010001894 (*) 771,22 100 PC 30,85

FI-REDS-42/35L-W3-SV

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc252SR-1-06 1881 26900 4 6010001894 771,22 100  73079910 Germany
print("doc252",doc252[5: 8], doc252[8: 9], doc252[10: 11], doc252[11: 12], doc252[13: 14], doc252[17:18], doc252[18:19] ,doc252[20:21], doc252[47: 48], doc252[53: 54]) 
doc252.ents = [Span(doc252, 5, 8, label="CONTRACT"), 
    Span(doc252, 8, 9, label="CONTRACT1"), 
    Span(doc252, 10, 11, label="POS"), 
    Span(doc252, 11, 12, label="AMOUNT"), 
    Span(doc252, 13, 14, label="ARTICLE"), 
    Span(doc252, 17, 18, label="PRICE"), 
    Span(doc252, 18, 19, label="UNIT"), 
    Span(doc252, 20, 21, label="SUM"), 
    Span(doc252, 47, 48, label="TARIFF"), 
    Span(doc252, 53, 54, label="COUNTRY")] 
docs.append(doc252)


doc253 = nlp('''Purchase order number: N SR-1-06 1881
27000 6 PC 6010002135 (*) 781,79 100 PC 46,91

FI-EGE-35LR-W3-SV
packed per each item
Product description: fitting


Description

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc253SR-1-06 1881 27000 6 6010002135 781,79 100  73079910 Germany
print("doc253",doc253[5: 8], doc253[8: 9], doc253[10: 11], doc253[11: 12], doc253[13: 14], doc253[17:18], doc253[18:19] ,doc253[20:21], doc253[49: 50], doc253[55: 56]) 
doc253.ents = [Span(doc253, 5, 8, label="CONTRACT"), 
    Span(doc253, 8, 9, label="CONTRACT1"), 
    Span(doc253, 10, 11, label="POS"), 
    Span(doc253, 11, 12, label="AMOUNT"), 
    Span(doc253, 13, 14, label="ARTICLE"), 
    Span(doc253, 17, 18, label="PRICE"), 
    Span(doc253, 18, 19, label="UNIT"), 
    Span(doc253, 20, 21, label="SUM"), 
    Span(doc253, 49, 50, label="TARIFF"), 
    Span(doc253, 55, 56, label="COUNTRY")] 
docs.append(doc253)


doc254 = nlp('''Purchase order number: N SR-1-06 1881
27100 35 PC 6010002088 (*) 278,97 100 PC 97,64

FI-EL-12L-W3-SV

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc254SR-1-06 1881 27100 35 6010002088 278,97 100  73079910 Germany
print("doc254",doc254[5: 8], doc254[8: 9], doc254[10: 11], doc254[11: 12], doc254[13: 14], doc254[17:18], doc254[18:19] ,doc254[20:21], doc254[47: 48], doc254[53: 54]) 
doc254.ents = [Span(doc254, 5, 8, label="CONTRACT"), 
    Span(doc254, 8, 9, label="CONTRACT1"), 
    Span(doc254, 10, 11, label="POS"), 
    Span(doc254, 11, 12, label="AMOUNT"), 
    Span(doc254, 13, 14, label="ARTICLE"), 
    Span(doc254, 17, 18, label="PRICE"), 
    Span(doc254, 18, 19, label="UNIT"), 
    Span(doc254, 20, 21, label="SUM"), 
    Span(doc254, 47, 48, label="TARIFF"), 
    Span(doc254, 53, 54, label="COUNTRY")] 
docs.append(doc254)


doc255 = nlp('''Purchase order number: N SR-1-06 1881
27200 25 PC 6010002090 (*) 472,15 100 PC 118,04

FI-EL-1 81-М/3-$\/

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc255SR-1-06 1881 27200 25 6010002090 472,15 100  73079910 Germany
print("doc255",doc255[5: 8], doc255[8: 9], doc255[10: 11], doc255[11: 12], doc255[13: 14], doc255[17:18], doc255[18:19] ,doc255[20:21], doc255[46: 47], doc255[52: 53]) 
doc255.ents = [Span(doc255, 5, 8, label="CONTRACT"), 
    Span(doc255, 8, 9, label="CONTRACT1"), 
    Span(doc255, 10, 11, label="POS"), 
    Span(doc255, 11, 12, label="AMOUNT"), 
    Span(doc255, 13, 14, label="ARTICLE"), 
    Span(doc255, 17, 18, label="PRICE"), 
    Span(doc255, 18, 19, label="UNIT"), 
    Span(doc255, 20, 21, label="SUM"), 
    Span(doc255, 46, 47, label="TARIFF"), 
    Span(doc255, 52, 53, label="COUNTRY")] 
docs.append(doc255)


doc256 = nlp('''Purchase order number: N SR-1-06 1881
27300 10 PC 6010002093 (*) 1.486,10 100 PC 148,61

FI-EL-35L-W3-SV

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc256SR-1-06 1881 27300 10 6010002093 1.486,10 100  73079910 Germany
print("doc256",doc256[5: 8], doc256[8: 9], doc256[10: 11], doc256[11: 12], doc256[13: 14], doc256[17:18], doc256[18:19] ,doc256[20:21], doc256[47: 48], doc256[53: 54]) 
doc256.ents = [Span(doc256, 5, 8, label="CONTRACT"), 
    Span(doc256, 8, 9, label="CONTRACT1"), 
    Span(doc256, 10, 11, label="POS"), 
    Span(doc256, 11, 12, label="AMOUNT"), 
    Span(doc256, 13, 14, label="ARTICLE"), 
    Span(doc256, 17, 18, label="PRICE"), 
    Span(doc256, 18, 19, label="UNIT"), 
    Span(doc256, 20, 21, label="SUM"), 
    Span(doc256, 47, 48, label="TARIFF"), 
    Span(doc256, 53, 54, label="COUNTRY")] 
docs.append(doc256)


doc257 = nlp('''Purchase order number: N SR-1-06 1881
27400 2 РС 6010002053 (*) 1.451,65 100 PC 29,03

FI-ET-35L-W3-SV

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc257SR-1-06 1881 27400 2 6010002053 1.451,65 100  73079910 Germany
print("doc257",doc257[5: 8], doc257[8: 9], doc257[10: 11], doc257[11: 12], doc257[13: 14], doc257[17:18], doc257[18:19] ,doc257[20:21], doc257[47: 48], doc257[53: 54]) 
doc257.ents = [Span(doc257, 5, 8, label="CONTRACT"), 
    Span(doc257, 8, 9, label="CONTRACT1"), 
    Span(doc257, 10, 11, label="POS"), 
    Span(doc257, 11, 12, label="AMOUNT"), 
    Span(doc257, 13, 14, label="ARTICLE"), 
    Span(doc257, 17, 18, label="PRICE"), 
    Span(doc257, 18, 19, label="UNIT"), 
    Span(doc257, 20, 21, label="SUM"), 
    Span(doc257, 47, 48, label="TARIFF"), 
    Span(doc257, 53, 54, label="COUNTRY")] 
docs.append(doc257)


doc258 = nlp('''Purchase order number: N SR-1-06 1881
27500 160 PC 6010002008 (*) 205,51 100 PC 328,82

FI-EW-12L-W3-SV

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079290
Country of origin: Germany''')
#doc258SR-1-06 1881 27500 160 6010002008 205,51 100  73079290 Germany
print("doc258",doc258[5: 8], doc258[8: 9], doc258[10: 11], doc258[11: 12], doc258[13: 14], doc258[17:18], doc258[18:19] ,doc258[20:21], doc258[47: 48], doc258[53: 54]) 
doc258.ents = [Span(doc258, 5, 8, label="CONTRACT"), 
    Span(doc258, 8, 9, label="CONTRACT1"), 
    Span(doc258, 10, 11, label="POS"), 
    Span(doc258, 11, 12, label="AMOUNT"), 
    Span(doc258, 13, 14, label="ARTICLE"), 
    Span(doc258, 17, 18, label="PRICE"), 
    Span(doc258, 18, 19, label="UNIT"), 
    Span(doc258, 20, 21, label="SUM"), 
    Span(doc258, 47, 48, label="TARIFF"), 
    Span(doc258, 53, 54, label="COUNTRY")] 
docs.append(doc258)


doc259 = nlp('''Purchase order number: N SR-1-06 1881
27600 4 РС 6010002019 (*) 337,07 100 PC 13,48

FI-EW-14S-W3-SV

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079290
Country of origin: Germany''')
#doc259SR-1-06 1881 27600 4 6010002019 337,07 100  73079290 Germany
print("doc259",doc259[5: 8], doc259[8: 9], doc259[10: 11], doc259[11: 12], doc259[13: 14], doc259[17:18], doc259[18:19] ,doc259[20:21], doc259[47: 48], doc259[53: 54]) 
doc259.ents = [Span(doc259, 5, 8, label="CONTRACT"), 
    Span(doc259, 8, 9, label="CONTRACT1"), 
    Span(doc259, 10, 11, label="POS"), 
    Span(doc259, 11, 12, label="AMOUNT"), 
    Span(doc259, 13, 14, label="ARTICLE"), 
    Span(doc259, 17, 18, label="PRICE"), 
    Span(doc259, 18, 19, label="UNIT"), 
    Span(doc259, 20, 21, label="SUM"), 
    Span(doc259, 47, 48, label="TARIFF"), 
    Span(doc259, 53, 54, label="COUNTRY")] 
docs.append(doc259)


doc260 = nlp('''Purchase order number: N SR-1-06 1881
27700 35 РС 6010002010 (*) 328,02 100 PC 114,81

FI-EW-18L-W3-SV

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079290
Country of origin: Germany''')
#doc260SR-1-06 1881 27700 35 6010002010 328,02 100  73079290 Germany
print("doc260",doc260[5: 8], doc260[8: 9], doc260[10: 11], doc260[11: 12], doc260[13: 14], doc260[17:18], doc260[18:19] ,doc260[20:21], doc260[47: 48], doc260[53: 54]) 
doc260.ents = [Span(doc260, 5, 8, label="CONTRACT"), 
    Span(doc260, 8, 9, label="CONTRACT1"), 
    Span(doc260, 10, 11, label="POS"), 
    Span(doc260, 11, 12, label="AMOUNT"), 
    Span(doc260, 13, 14, label="ARTICLE"), 
    Span(doc260, 17, 18, label="PRICE"), 
    Span(doc260, 18, 19, label="UNIT"), 
    Span(doc260, 20, 21, label="SUM"), 
    Span(doc260, 47, 48, label="TARIFF"), 
    Span(doc260, 53, 54, label="COUNTRY")] 
docs.append(doc260)


doc261 = nlp('''Purchase order number: N SR-1-06 1881
27800 30 PC 6010002013 (*) 1.095,49 100 PC 328,65

FI-EW-35L-W3-SV

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079290
Country of origin: Germany''')
#doc261SR-1-06 1881 27800 30 6010002013 1.095,49 100  73079290 Germany
print("doc261",doc261[5: 8], doc261[8: 9], doc261[10: 11], doc261[11: 12], doc261[13: 14], doc261[17:18], doc261[18:19] ,doc261[20:21], doc261[47: 48], doc261[53: 54]) 
doc261.ents = [Span(doc261, 5, 8, label="CONTRACT"), 
    Span(doc261, 8, 9, label="CONTRACT1"), 
    Span(doc261, 10, 11, label="POS"), 
    Span(doc261, 11, 12, label="AMOUNT"), 
    Span(doc261, 13, 14, label="ARTICLE"), 
    Span(doc261, 17, 18, label="PRICE"), 
    Span(doc261, 18, 19, label="UNIT"), 
    Span(doc261, 20, 21, label="SUM"), 
    Span(doc261, 47, 48, label="TARIFF"), 
    Span(doc261, 53, 54, label="COUNTRY")] 
docs.append(doc261)


doc262 = nlp('''Purchase order number: N SR-1-06 1881
27900 8 PC 6030003286 (*) 278,97 100 PC 22,32

FI-G-22/18L-W3

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc262SR-1-06 1881 27900 8 6030003286 278,97 100  73079910 Germany
print("doc262",doc262[5: 8], doc262[8: 9], doc262[10: 11], doc262[11: 12], doc262[13: 14], doc262[17:18], doc262[18:19] ,doc262[20:21], doc262[45: 46], doc262[51: 52]) 
doc262.ents = [Span(doc262, 5, 8, label="CONTRACT"), 
    Span(doc262, 8, 9, label="CONTRACT1"), 
    Span(doc262, 10, 11, label="POS"), 
    Span(doc262, 11, 12, label="AMOUNT"), 
    Span(doc262, 13, 14, label="ARTICLE"), 
    Span(doc262, 17, 18, label="PRICE"), 
    Span(doc262, 18, 19, label="UNIT"), 
    Span(doc262, 20, 21, label="SUM"), 
    Span(doc262, 45, 46, label="TARIFF"), 
    Span(doc262, 51, 52, label="COUNTRY")] 
docs.append(doc262)


doc263 = nlp('''Purchase order number: N SR-1-06 1881
28000 50 PC 6030003251 (*) 117,72 100 PC 58,86
FI-G-22L-W3


Description

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc263SR-1-06 1881 28000 50 6030003251 117,72 100  73079910 Germany
print("doc263",doc263[5: 8], doc263[8: 9], doc263[10: 11], doc263[11: 12], doc263[13: 14], doc263[17:18], doc263[18:19] ,doc263[20:21], doc263[47: 48], doc263[53: 54]) 
doc263.ents = [Span(doc263, 5, 8, label="CONTRACT"), 
    Span(doc263, 8, 9, label="CONTRACT1"), 
    Span(doc263, 10, 11, label="POS"), 
    Span(doc263, 11, 12, label="AMOUNT"), 
    Span(doc263, 13, 14, label="ARTICLE"), 
    Span(doc263, 17, 18, label="PRICE"), 
    Span(doc263, 18, 19, label="UNIT"), 
    Span(doc263, 20, 21, label="SUM"), 
    Span(doc263, 47, 48, label="TARIFF"), 
    Span(doc263, 53, 54, label="COUNTRY")] 
docs.append(doc263)


doc264 = nlp('''Purchase order number: N SR-1-06 1881
28100 16 PC 6030002475 (*) 618,54 100 PC 98,97

FI-GA-14SM-W3

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc264SR-1-06 1881 28100 16 6030002475 618,54 100  73079910 Germany
print("doc264",doc264[5: 8], doc264[8: 9], doc264[10: 11], doc264[11: 12], doc264[13: 14], doc264[17:18], doc264[18:19] ,doc264[20:21], doc264[45: 46], doc264[51: 52]) 
doc264.ents = [Span(doc264, 5, 8, label="CONTRACT"), 
    Span(doc264, 8, 9, label="CONTRACT1"), 
    Span(doc264, 10, 11, label="POS"), 
    Span(doc264, 11, 12, label="AMOUNT"), 
    Span(doc264, 13, 14, label="ARTICLE"), 
    Span(doc264, 17, 18, label="PRICE"), 
    Span(doc264, 18, 19, label="UNIT"), 
    Span(doc264, 20, 21, label="SUM"), 
    Span(doc264, 45, 46, label="TARIFF"), 
    Span(doc264, 51, 52, label="COUNTRY")] 
docs.append(doc264)


doc265 = nlp('''Purchase order number: N SR-1-06 1881
28200 2 PC 6030003556 (*) 950,09 100 PC 19,00
FI-GA-35LR-W3

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc265SR-1-06 1881 28200 2 6030003556 950,09 100  73079910 Germany
print("doc265",doc265[5: 8], doc265[8: 9], doc265[10: 11], doc265[11: 12], doc265[13: 14], doc265[17:18], doc265[18:19] ,doc265[20:21], doc265[45: 46], doc265[51: 52]) 
doc265.ents = [Span(doc265, 5, 8, label="CONTRACT"), 
    Span(doc265, 8, 9, label="CONTRACT1"), 
    Span(doc265, 10, 11, label="POS"), 
    Span(doc265, 11, 12, label="AMOUNT"), 
    Span(doc265, 13, 14, label="ARTICLE"), 
    Span(doc265, 17, 18, label="PRICE"), 
    Span(doc265, 18, 19, label="UNIT"), 
    Span(doc265, 20, 21, label="SUM"), 
    Span(doc265, 45, 46, label="TARIFF"), 
    Span(doc265, 51, 52, label="COUNTRY")] 
docs.append(doc265)


doc266 = nlp('''Purchase order number: N SR-1-06 1881
28300 4 РС 6030003192 (*) 221,36 100 PC 8,85

FI-GE-18LR3/8-W3

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910


Description

Country of origin: Germany''')
#doc266SR-1-06 1881 28300 4 6030003192 221,36 100  73079910 Germany
print("doc266",doc266[5: 8], doc266[8: 9], doc266[10: 11], doc266[11: 12], doc266[13: 14], doc266[17:18], doc266[18:19] ,doc266[20:21], doc266[45: 46], doc266[53: 54]) 
doc266.ents = [Span(doc266, 5, 8, label="CONTRACT"), 
    Span(doc266, 8, 9, label="CONTRACT1"), 
    Span(doc266, 10, 11, label="POS"), 
    Span(doc266, 11, 12, label="AMOUNT"), 
    Span(doc266, 13, 14, label="ARTICLE"), 
    Span(doc266, 17, 18, label="PRICE"), 
    Span(doc266, 18, 19, label="UNIT"), 
    Span(doc266, 20, 21, label="SUM"), 
    Span(doc266, 45, 46, label="TARIFF"), 
    Span(doc266, 53, 54, label="COUNTRY")] 
docs.append(doc266)


doc267 = nlp('''Purchase order number: N SR-1-06 1881
28400 50 PC 6030003196 (*) 116,20 100 PC 58,10
FI-GE-22LR-W3

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc267SR-1-06 1881 28400 50 6030003196 116,20 100  73079910 Germany
print("doc267",doc267[5: 8], doc267[8: 9], doc267[10: 11], doc267[11: 12], doc267[13: 14], doc267[17:18], doc267[18:19] ,doc267[20:21], doc267[45: 46], doc267[51: 52]) 
doc267.ents = [Span(doc267, 5, 8, label="CONTRACT"), 
    Span(doc267, 8, 9, label="CONTRACT1"), 
    Span(doc267, 10, 11, label="POS"), 
    Span(doc267, 11, 12, label="AMOUNT"), 
    Span(doc267, 13, 14, label="ARTICLE"), 
    Span(doc267, 17, 18, label="PRICE"), 
    Span(doc267, 18, 19, label="UNIT"), 
    Span(doc267, 20, 21, label="SUM"), 
    Span(doc267, 45, 46, label="TARIFF"), 
    Span(doc267, 51, 52, label="COUNTRY")] 
docs.append(doc267)


doc268 = nlp('''Purchase order number: N SR-1-06 1881
28500 4 РС 6030003204 (*) 332,53 100 PC 13,30
FI-GE-35LR-W3

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc268SR-1-06 1881 28500 4 6030003204 332,53 100  73079910 Germany
print("doc268",doc268[5: 8], doc268[8: 9], doc268[10: 11], doc268[11: 12], doc268[13: 14], doc268[17:18], doc268[18:19] ,doc268[20:21], doc268[45: 46], doc268[51: 52]) 
doc268.ents = [Span(doc268, 5, 8, label="CONTRACT"), 
    Span(doc268, 8, 9, label="CONTRACT1"), 
    Span(doc268, 10, 11, label="POS"), 
    Span(doc268, 11, 12, label="AMOUNT"), 
    Span(doc268, 13, 14, label="ARTICLE"), 
    Span(doc268, 17, 18, label="PRICE"), 
    Span(doc268, 18, 19, label="UNIT"), 
    Span(doc268, 20, 21, label="SUM"), 
    Span(doc268, 45, 46, label="TARIFF"), 
    Span(doc268, 51, 52, label="COUNTRY")] 
docs.append(doc268)


doc269 = nlp('''Purchase order number: N SR-1-06 1881
28600 30 PC 6030003203 (*) 878,13 100 PC 263,44

FI-GE-35LR1-W3.

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc269SR-1-06 1881 28600 30 6030003203 878,13 100  73079910 Germany
print("doc269",doc269[5: 8], doc269[8: 9], doc269[10: 11], doc269[11: 12], doc269[13: 14], doc269[17:18], doc269[18:19] ,doc269[20:21], doc269[46: 47], doc269[52: 53]) 
doc269.ents = [Span(doc269, 5, 8, label="CONTRACT"), 
    Span(doc269, 8, 9, label="CONTRACT1"), 
    Span(doc269, 10, 11, label="POS"), 
    Span(doc269, 11, 12, label="AMOUNT"), 
    Span(doc269, 13, 14, label="ARTICLE"), 
    Span(doc269, 17, 18, label="PRICE"), 
    Span(doc269, 18, 19, label="UNIT"), 
    Span(doc269, 20, 21, label="SUM"), 
    Span(doc269, 46, 47, label="TARIFF"), 
    Span(doc269, 52, 53, label="COUNTRY")] 
docs.append(doc269)


doc270 = nlp('''Purchase order number: N SR-1-06 1881
28700 10 PC 6030003208 (*) 914,35 100 PC 91,44

FI-GE-42LR1-1/4-W3

FI-GE-42LR1 1/4-W3

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc270SR-1-06 1881 28700 10 6030003208 914,35 100  73079910 Germany
print("doc270",doc270[5: 8], doc270[8: 9], doc270[10: 11], doc270[11: 12], doc270[13: 14], doc270[17:18], doc270[18:19] ,doc270[20:21], doc270[54: 55], doc270[60: 61]) 
doc270.ents = [Span(doc270, 5, 8, label="CONTRACT"), 
    Span(doc270, 8, 9, label="CONTRACT1"), 
    Span(doc270, 10, 11, label="POS"), 
    Span(doc270, 11, 12, label="AMOUNT"), 
    Span(doc270, 13, 14, label="ARTICLE"), 
    Span(doc270, 17, 18, label="PRICE"), 
    Span(doc270, 18, 19, label="UNIT"), 
    Span(doc270, 20, 21, label="SUM"), 
    Span(doc270, 54, 55, label="TARIFF"), 
    Span(doc270, 60, 61, label="COUNTRY")] 
docs.append(doc270)


doc271 = nlp('''Purchase order number: N SR-1-06 1881
28800 20 PC 6020000204 (*) 390,15 100 PC 78,03

FI-GS-22L-W3-SKM

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc271SR-1-06 1881 28800 20 6020000204 390,15 100  73079910 Germany
print("doc271",doc271[5: 8], doc271[8: 9], doc271[10: 11], doc271[11: 12], doc271[13: 14], doc271[17:18], doc271[18:19] ,doc271[20:21], doc271[47: 48], doc271[53: 54]) 
doc271.ents = [Span(doc271, 5, 8, label="CONTRACT"), 
    Span(doc271, 8, 9, label="CONTRACT1"), 
    Span(doc271, 10, 11, label="POS"), 
    Span(doc271, 11, 12, label="AMOUNT"), 
    Span(doc271, 13, 14, label="ARTICLE"), 
    Span(doc271, 17, 18, label="PRICE"), 
    Span(doc271, 18, 19, label="UNIT"), 
    Span(doc271, 20, 21, label="SUM"), 
    Span(doc271, 47, 48, label="TARIFF"), 
    Span(doc271, 53, 54, label="COUNTRY")] 
docs.append(doc271)


doc272 = nlp('''Purchase order number: N SR-1-06 1881
28900 10 PC 6020000206 (*) 930,46 100 PC 93,05

FI-GS-35L-W3-SKM

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc272SR-1-06 1881 28900 10 6020000206 930,46 100  73079910 Germany
print("doc272",doc272[5: 8], doc272[8: 9], doc272[10: 11], doc272[11: 12], doc272[13: 14], doc272[17:18], doc272[18:19] ,doc272[20:21], doc272[47: 48], doc272[53: 54]) 
doc272.ents = [Span(doc272, 5, 8, label="CONTRACT"), 
    Span(doc272, 8, 9, label="CONTRACT1"), 
    Span(doc272, 10, 11, label="POS"), 
    Span(doc272, 11, 12, label="AMOUNT"), 
    Span(doc272, 13, 14, label="ARTICLE"), 
    Span(doc272, 17, 18, label="PRICE"), 
    Span(doc272, 18, 19, label="UNIT"), 
    Span(doc272, 20, 21, label="SUM"), 
    Span(doc272, 47, 48, label="TARIFF"), 
    Span(doc272, 53, 54, label="COUNTRY")] 
docs.append(doc272)


doc273 = nlp('''Purchase order number: N SR-1-06 1881

29000 2 PC 6030002444 952,09 100 PC 19,04
FI-K-18L-W3

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc273SR-1-06 1881 29000 2 6030002444 952,09 100  73079910 Germany
print("doc273",doc273[5: 8], doc273[8: 9], doc273[10: 11], doc273[11: 12], doc273[13: 14], doc273[14:15], doc273[15:16] ,doc273[17:18], doc273[42: 43], doc273[48: 49]) 
doc273.ents = [Span(doc273, 5, 8, label="CONTRACT"), 
    Span(doc273, 8, 9, label="CONTRACT1"), 
    Span(doc273, 10, 11, label="POS"), 
    Span(doc273, 11, 12, label="AMOUNT"), 
    Span(doc273, 13, 14, label="ARTICLE"), 
    Span(doc273, 14, 15, label="PRICE"), 
    Span(doc273, 15, 16, label="UNIT"), 
    Span(doc273, 17, 18, label="SUM"), 
    Span(doc273, 42, 43, label="TARIFF"), 
    Span(doc273, 48, 49, label="COUNTRY")] 
docs.append(doc273)


doc274 = nlp('''Purchase order number: N SR-1-06 1881
29100 10 PC 6030002445 1.384,75 100 PC 138,48
FI-K-22L-W3

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc274SR-1-06 1881 29100 10 6030002445 1.384,75 100  73079910 Germany
print("doc274",doc274[5: 8], doc274[8: 9], doc274[10: 11], doc274[11: 12], doc274[13: 14], doc274[14:15], doc274[15:16] ,doc274[17:18], doc274[42: 43], doc274[48: 49]) 
doc274.ents = [Span(doc274, 5, 8, label="CONTRACT"), 
    Span(doc274, 8, 9, label="CONTRACT1"), 
    Span(doc274, 10, 11, label="POS"), 
    Span(doc274, 11, 12, label="AMOUNT"), 
    Span(doc274, 13, 14, label="ARTICLE"), 
    Span(doc274, 14, 15, label="PRICE"), 
    Span(doc274, 15, 16, label="UNIT"), 
    Span(doc274, 17, 18, label="SUM"), 
    Span(doc274, 42, 43, label="TARIFF"), 
    Span(doc274, 48, 49, label="COUNTRY")] 
docs.append(doc274)


doc275 = nlp('''Purchase order number: N SR-1-06 1881
29200 8 PC 6010000056 (*) 3.515,05 100 PC 281,20

FI-RSW-42LR-DK-B-W3

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc275SR-1-06 1881 29200 8 6010000056 3.515,05 100  73079910 Germany
print("doc275",doc275[5: 8], doc275[8: 9], doc275[10: 11], doc275[11: 12], doc275[13: 14], doc275[17:18], doc275[18:19] ,doc275[20:21], doc275[49: 50], doc275[55: 56]) 
doc275.ents = [Span(doc275, 5, 8, label="CONTRACT"), 
    Span(doc275, 8, 9, label="CONTRACT1"), 
    Span(doc275, 10, 11, label="POS"), 
    Span(doc275, 11, 12, label="AMOUNT"), 
    Span(doc275, 13, 14, label="ARTICLE"), 
    Span(doc275, 17, 18, label="PRICE"), 
    Span(doc275, 18, 19, label="UNIT"), 
    Span(doc275, 20, 21, label="SUM"), 
    Span(doc275, 49, 50, label="TARIFF"), 
    Span(doc275, 55, 56, label="COUNTRY")] 
docs.append(doc275)


doc276 = nlp('''Purchase order number: N SR-1-06 1881
29300 30 PC 6010014179 (*) 565,22 100 PC 169,57

FI-RSWND-18LR-DK-W3


Description

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc276SR-1-06 1881 29300 30 6010014179 565,22 100  73079910 Germany
print("doc276",doc276[5: 8], doc276[8: 9], doc276[10: 11], doc276[11: 12], doc276[13: 14], doc276[17:18], doc276[18:19] ,doc276[20:21], doc276[49: 50], doc276[55: 56]) 
doc276.ents = [Span(doc276, 5, 8, label="CONTRACT"), 
    Span(doc276, 8, 9, label="CONTRACT1"), 
    Span(doc276, 10, 11, label="POS"), 
    Span(doc276, 11, 12, label="AMOUNT"), 
    Span(doc276, 13, 14, label="ARTICLE"), 
    Span(doc276, 17, 18, label="PRICE"), 
    Span(doc276, 18, 19, label="UNIT"), 
    Span(doc276, 20, 21, label="SUM"), 
    Span(doc276, 49, 50, label="TARIFF"), 
    Span(doc276, 55, 56, label="COUNTRY")] 
docs.append(doc276)


doc277 = nlp('''Purchase order number: N SR-1-06 1881
29400 16 PC 6030003852 1.003,65 100 PC 160,58
FI-T-35L-W3

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc277SR-1-06 1881 29400 16 6030003852 1.003,65 100  73079910 Germany
print("doc277",doc277[5: 8], doc277[8: 9], doc277[10: 11], doc277[11: 12], doc277[13: 14], doc277[14:15], doc277[15:16] ,doc277[17:18], doc277[42: 43], doc277[48: 49]) 
doc277.ents = [Span(doc277, 5, 8, label="CONTRACT"), 
    Span(doc277, 8, 9, label="CONTRACT1"), 
    Span(doc277, 10, 11, label="POS"), 
    Span(doc277, 11, 12, label="AMOUNT"), 
    Span(doc277, 13, 14, label="ARTICLE"), 
    Span(doc277, 14, 15, label="PRICE"), 
    Span(doc277, 15, 16, label="UNIT"), 
    Span(doc277, 17, 18, label="SUM"), 
    Span(doc277, 42, 43, label="TARIFF"), 
    Span(doc277, 48, 49, label="COUNTRY")] 
docs.append(doc277)


doc278 = nlp('''Purchase order number: N SR-1-06 1881
29500 10 PC 6030005497 6.724,47 100 PC 672,45

FI-T-42/22/42L-W3

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc278SR-1-06 1881 29500 10 6030005497 6.724,47 100  73079910 Germany
print("doc278",doc278[5: 8], doc278[8: 9], doc278[10: 11], doc278[11: 12], doc278[13: 14], doc278[14:15], doc278[15:16] ,doc278[17:18], doc278[42: 43], doc278[48: 49]) 
doc278.ents = [Span(doc278, 5, 8, label="CONTRACT"), 
    Span(doc278, 8, 9, label="CONTRACT1"), 
    Span(doc278, 10, 11, label="POS"), 
    Span(doc278, 11, 12, label="AMOUNT"), 
    Span(doc278, 13, 14, label="ARTICLE"), 
    Span(doc278, 14, 15, label="PRICE"), 
    Span(doc278, 15, 16, label="UNIT"), 
    Span(doc278, 17, 18, label="SUM"), 
    Span(doc278, 42, 43, label="TARIFF"), 
    Span(doc278, 48, 49, label="COUNTRY")] 
docs.append(doc278)


doc279 = nlp('''Purchase order number: N SR-1-06 1881
29600 6 РС 6030007801 6.342,62 100 PC 380,56

FI-T-42/35/42L-W3

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910


Description

Country of origin: Germany''')
#doc279SR-1-06 1881 29600 6 6030007801 6.342,62 100  73079910 Germany
print("doc279",doc279[5: 8], doc279[8: 9], doc279[10: 11], doc279[11: 12], doc279[13: 14], doc279[14:15], doc279[15:16] ,doc279[17:18], doc279[42: 43], doc279[50: 51]) 
doc279.ents = [Span(doc279, 5, 8, label="CONTRACT"), 
    Span(doc279, 8, 9, label="CONTRACT1"), 
    Span(doc279, 10, 11, label="POS"), 
    Span(doc279, 11, 12, label="AMOUNT"), 
    Span(doc279, 13, 14, label="ARTICLE"), 
    Span(doc279, 14, 15, label="PRICE"), 
    Span(doc279, 15, 16, label="UNIT"), 
    Span(doc279, 17, 18, label="SUM"), 
    Span(doc279, 42, 43, label="TARIFF"), 
    Span(doc279, 50, 51, label="COUNTRY")] 
docs.append(doc279)


doc280 = nlp('''Purchase order number: N SR-1-06 1881
29700 5 PC 6030003853 1.583,46 100 PC 79,17
FI-T-42L-W3

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc280SR-1-06 1881 29700 5 6030003853 1.583,46 100  73079910 Germany
print("doc280",doc280[5: 8], doc280[8: 9], doc280[10: 11], doc280[11: 12], doc280[13: 14], doc280[14:15], doc280[15:16] ,doc280[17:18], doc280[42: 43], doc280[48: 49]) 
doc280.ents = [Span(doc280, 5, 8, label="CONTRACT"), 
    Span(doc280, 8, 9, label="CONTRACT1"), 
    Span(doc280, 10, 11, label="POS"), 
    Span(doc280, 11, 12, label="AMOUNT"), 
    Span(doc280, 13, 14, label="ARTICLE"), 
    Span(doc280, 14, 15, label="PRICE"), 
    Span(doc280, 15, 16, label="UNIT"), 
    Span(doc280, 17, 18, label="SUM"), 
    Span(doc280, 42, 43, label="TARIFF"), 
    Span(doc280, 48, 49, label="COUNTRY")] 
docs.append(doc280)


doc281 = nlp('''Purchase order number: N SR-1-06 1881
29800 150 PC 6030003434 145,90 100 PC 218,85
FI-W-12L-W3

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079290
Country of origin: Germany''')
#doc281SR-1-06 1881 29800 150 6030003434 145,90 100  73079290 Germany
print("doc281",doc281[5: 8], doc281[8: 9], doc281[10: 11], doc281[11: 12], doc281[13: 14], doc281[14:15], doc281[15:16] ,doc281[17:18], doc281[42: 43], doc281[48: 49]) 
doc281.ents = [Span(doc281, 5, 8, label="CONTRACT"), 
    Span(doc281, 8, 9, label="CONTRACT1"), 
    Span(doc281, 10, 11, label="POS"), 
    Span(doc281, 11, 12, label="AMOUNT"), 
    Span(doc281, 13, 14, label="ARTICLE"), 
    Span(doc281, 14, 15, label="PRICE"), 
    Span(doc281, 15, 16, label="UNIT"), 
    Span(doc281, 17, 18, label="SUM"), 
    Span(doc281, 42, 43, label="TARIFF"), 
    Span(doc281, 48, 49, label="COUNTRY")] 
docs.append(doc281)


doc282 = nlp('''Purchase order number: N SR-1-06 1881
29900 175 PC 6030003436 244,49 100 PC 427,86
FI-W-18L-W3

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079290
Country of origin: Germany''')
#doc282SR-1-06 1881 29900 175 6030003436 244,49 100  73079290 Germany
print("doc282",doc282[5: 8], doc282[8: 9], doc282[10: 11], doc282[11: 12], doc282[13: 14], doc282[14:15], doc282[15:16] ,doc282[17:18], doc282[42: 43], doc282[48: 49]) 
doc282.ents = [Span(doc282, 5, 8, label="CONTRACT"), 
    Span(doc282, 8, 9, label="CONTRACT1"), 
    Span(doc282, 10, 11, label="POS"), 
    Span(doc282, 11, 12, label="AMOUNT"), 
    Span(doc282, 13, 14, label="ARTICLE"), 
    Span(doc282, 14, 15, label="PRICE"), 
    Span(doc282, 15, 16, label="UNIT"), 
    Span(doc282, 17, 18, label="SUM"), 
    Span(doc282, 42, 43, label="TARIFF"), 
    Span(doc282, 48, 49, label="COUNTRY")] 
docs.append(doc282)


doc283 = nlp('''Purchase order number: N SR-1-06 1881
30000 50 PC 6030003437 350,65 100 PC 175,33
FI-W-22L-W3

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079290
Country of origin: Germany''')
#doc283SR-1-06 1881 30000 50 6030003437 350,65 100  73079290 Germany
print("doc283",doc283[5: 8], doc283[8: 9], doc283[10: 11], doc283[11: 12], doc283[13: 14], doc283[14:15], doc283[15:16] ,doc283[17:18], doc283[42: 43], doc283[48: 49]) 
doc283.ents = [Span(doc283, 5, 8, label="CONTRACT"), 
    Span(doc283, 8, 9, label="CONTRACT1"), 
    Span(doc283, 10, 11, label="POS"), 
    Span(doc283, 11, 12, label="AMOUNT"), 
    Span(doc283, 13, 14, label="ARTICLE"), 
    Span(doc283, 14, 15, label="PRICE"), 
    Span(doc283, 15, 16, label="UNIT"), 
    Span(doc283, 17, 18, label="SUM"), 
    Span(doc283, 42, 43, label="TARIFF"), 
    Span(doc283, 48, 49, label="COUNTRY")] 
docs.append(doc283)


doc284 = nlp('''Purchase order number: N SR-1-06 1881
30100 20 PC 6030003439 816,01 100 PC 163,20
FI-W-35L-W3

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079290
Country of origin: Germany''')
#doc284SR-1-06 1881 30100 20 6030003439 816,01 100  73079290 Germany
print("doc284",doc284[5: 8], doc284[8: 9], doc284[10: 11], doc284[11: 12], doc284[13: 14], doc284[14:15], doc284[15:16] ,doc284[17:18], doc284[42: 43], doc284[48: 49]) 
doc284.ents = [Span(doc284, 5, 8, label="CONTRACT"), 
    Span(doc284, 8, 9, label="CONTRACT1"), 
    Span(doc284, 10, 11, label="POS"), 
    Span(doc284, 11, 12, label="AMOUNT"), 
    Span(doc284, 13, 14, label="ARTICLE"), 
    Span(doc284, 14, 15, label="PRICE"), 
    Span(doc284, 15, 16, label="UNIT"), 
    Span(doc284, 17, 18, label="SUM"), 
    Span(doc284, 42, 43, label="TARIFF"), 
    Span(doc284, 48, 49, label="COUNTRY")] 
docs.append(doc284)


doc285 = nlp('''Purchase order number: N SR-1-06 1881
30200 20 PC 6030003440 1.141,76 100 PC 228,35
FI-W-42L-W3

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079290
Country of origin: Germany''')
#doc285SR-1-06 1881 30200 20 6030003440 1.141,76 100  73079290 Germany
print("doc285",doc285[5: 8], doc285[8: 9], doc285[10: 11], doc285[11: 12], doc285[13: 14], doc285[14:15], doc285[15:16] ,doc285[17:18], doc285[42: 43], doc285[48: 49]) 
doc285.ents = [Span(doc285, 5, 8, label="CONTRACT"), 
    Span(doc285, 8, 9, label="CONTRACT1"), 
    Span(doc285, 10, 11, label="POS"), 
    Span(doc285, 11, 12, label="AMOUNT"), 
    Span(doc285, 13, 14, label="ARTICLE"), 
    Span(doc285, 14, 15, label="PRICE"), 
    Span(doc285, 15, 16, label="UNIT"), 
    Span(doc285, 17, 18, label="SUM"), 
    Span(doc285, 42, 43, label="TARIFF"), 
    Span(doc285, 48, 49, label="COUNTRY")] 
docs.append(doc285)


doc287 = nlp('''Purchase order number: N SR-1-06 1895
30400 10 PC 1130006262 193,59 100 PC 19,36
888.9-PP
888,9 PP

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc287SR-1-06 1895 30400 10 1130006262 193,59 100  39269097 Germany
print("doc287",doc287[5: 8], doc287[8: 9], doc287[10: 11], doc287[11: 12], doc287[13: 14], doc287[14:15], doc287[15:16] ,doc287[17:18], doc287[44: 45], doc287[50: 51]) 
doc287.ents = [Span(doc287, 5, 8, label="CONTRACT"), 
    Span(doc287, 8, 9, label="CONTRACT1"), 
    Span(doc287, 10, 11, label="POS"), 
    Span(doc287, 11, 12, label="AMOUNT"), 
    Span(doc287, 13, 14, label="ARTICLE"), 
    Span(doc287, 14, 15, label="PRICE"), 
    Span(doc287, 15, 16, label="UNIT"), 
    Span(doc287, 17, 18, label="SUM"), 
    Span(doc287, 44, 45, label="TARIFF"), 
    Span(doc287, 50, 51, label="COUNTRY")] 
docs.append(doc287)


doc288 = nlp('''Purchase order number: N SR-1-06 1895
30500 10 PC 1130001505 47,66 100 PC 4,77
DP-8-W3
DP 8 W3

packed per each item

Product description: cover plate

Export - Customs tariff no.: 73269098
Country of origin: Germany''')
#doc288SR-1-06 1895 30500 10 1130001505 47,66 100  73269098 Germany
print("doc288",doc288[5: 8], doc288[8: 9], doc288[10: 11], doc288[11: 12], doc288[13: 14], doc288[14:15], doc288[15:16] ,doc288[17:18], doc288[45: 46], doc288[51: 52]) 
doc288.ents = [Span(doc288, 5, 8, label="CONTRACT"), 
    Span(doc288, 8, 9, label="CONTRACT1"), 
    Span(doc288, 10, 11, label="POS"), 
    Span(doc288, 11, 12, label="AMOUNT"), 
    Span(doc288, 13, 14, label="ARTICLE"), 
    Span(doc288, 14, 15, label="PRICE"), 
    Span(doc288, 15, 16, label="UNIT"), 
    Span(doc288, 17, 18, label="SUM"), 
    Span(doc288, 45, 46, label="TARIFF"), 
    Span(doc288, 51, 52, label="COUNTRY")] 
docs.append(doc288)


doc290 = nlp('''Purchase order number: N SR-1-06 1894
30700 18 PC 6100074194 (*) 7,83 1 РС 140,94
QRC-IA-25-DF-41/CN-W89I-SI
1А25-9-$1001

packed per each item
Export - Customs tariff no.: 76169990
Country of origin: Italy''')
#doc290SR-1-06 1894 30700 18 6100074194 7,83 1  76169990 Italy
print("doc290",doc290[5: 8], doc290[8: 9], doc290[10: 11], doc290[11: 12], doc290[13: 14], doc290[17:18], doc290[18:19] ,doc290[20:21], doc290[50: 51], doc290[56: 57]) 
doc290.ents = [Span(doc290, 5, 8, label="CONTRACT"), 
    Span(doc290, 8, 9, label="CONTRACT1"), 
    Span(doc290, 10, 11, label="POS"), 
    Span(doc290, 11, 12, label="AMOUNT"), 
    Span(doc290, 13, 14, label="ARTICLE"), 
    Span(doc290, 17, 18, label="PRICE"), 
    Span(doc290, 18, 19, label="UNIT"), 
    Span(doc290, 20, 21, label="SUM"), 
    Span(doc290, 50, 51, label="TARIFF"), 
    Span(doc290, 56, 57, label="COUNTRY")] 
docs.append(doc290)


doc291 = nlp('''Purchase order number: N SR-1-06 1894
30800 14 PC 6100074195 (*) 11,07 1 РС 154,98
QRC-IA-25-DM-41/CN-W89I-SI
1А25-0-$1001

packed per each item
Export - Customs tariff no.: 76169990
Country of origin: Italy''')
#doc291SR-1-06 1894 30800 14 6100074195 11,07 1  76169990 Italy
print("doc291",doc291[5: 8], doc291[8: 9], doc291[10: 11], doc291[11: 12], doc291[13: 14], doc291[17:18], doc291[18:19] ,doc291[20:21], doc291[50: 51], doc291[56: 57]) 
doc291.ents = [Span(doc291, 5, 8, label="CONTRACT"), 
    Span(doc291, 8, 9, label="CONTRACT1"), 
    Span(doc291, 10, 11, label="POS"), 
    Span(doc291, 11, 12, label="AMOUNT"), 
    Span(doc291, 13, 14, label="ARTICLE"), 
    Span(doc291, 17, 18, label="PRICE"), 
    Span(doc291, 18, 19, label="UNIT"), 
    Span(doc291, 20, 21, label="SUM"), 
    Span(doc291, 50, 51, label="TARIFF"), 
    Span(doc291, 56, 57, label="COUNTRY")] 
docs.append(doc291)


doc292 = nlp('''Purchase order number: N SR-1-06 1894
30900 10 PC 6100201508 8,87 1 РС 88,70


Description

QRC-IA-25-F-G16-BT-W3AA
packed per each item

Export - Customs tariff no.: 84812010
Country of origin: China''')
#doc292SR-1-06 1894 30900 10 6100201508 8,87 1  84812010 China
print("doc292",doc292[5: 8], doc292[8: 9], doc292[10: 11], doc292[11: 12], doc292[13: 14], doc292[14:15], doc292[15:16] ,doc292[17:18], doc292[45: 46], doc292[51: 52]) 
doc292.ents = [Span(doc292, 5, 8, label="CONTRACT"), 
    Span(doc292, 8, 9, label="CONTRACT1"), 
    Span(doc292, 10, 11, label="POS"), 
    Span(doc292, 11, 12, label="AMOUNT"), 
    Span(doc292, 13, 14, label="ARTICLE"), 
    Span(doc292, 14, 15, label="PRICE"), 
    Span(doc292, 15, 16, label="UNIT"), 
    Span(doc292, 17, 18, label="SUM"), 
    Span(doc292, 45, 46, label="TARIFF"), 
    Span(doc292, 51, 52, label="COUNTRY")] 
docs.append(doc292)


doc293 = nlp('''Purchase order number: N SR-1-06 1894
31000 5 PC 6100201509 3,81 1 РС 19,05

QRC-IA-25-M-G16-B-W3AA

packed per each item

Export - Customs tariff no.: 84812010
Country of origin: China''')
#doc293SR-1-06 1894 31000 5 6100201509 3,81 1  84812010 China
print("doc293",doc293[5: 8], doc293[8: 9], doc293[10: 11], doc293[11: 12], doc293[13: 14], doc293[14:15], doc293[15:16] ,doc293[17:18], doc293[43: 44], doc293[49: 50]) 
doc293.ents = [Span(doc293, 5, 8, label="CONTRACT"), 
    Span(doc293, 8, 9, label="CONTRACT1"), 
    Span(doc293, 10, 11, label="POS"), 
    Span(doc293, 11, 12, label="AMOUNT"), 
    Span(doc293, 13, 14, label="ARTICLE"), 
    Span(doc293, 14, 15, label="PRICE"), 
    Span(doc293, 15, 16, label="UNIT"), 
    Span(doc293, 17, 18, label="SUM"), 
    Span(doc293, 43, 44, label="TARIFF"), 
    Span(doc293, 49, 50, label="COUNTRY")] 
docs.append(doc293)


doc294 = nlp('''Purchase order number: N SR-1-06 1894
31100 30 PC 6030003830 249,78 100 PC 74,93
FI-M-38S-W3

packed per each item

Product description: nuts

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc294SR-1-06 1894 31100 30 6030003830 249,78 100  73079910 Germany
print("doc294",doc294[5: 8], doc294[8: 9], doc294[10: 11], doc294[11: 12], doc294[13: 14], doc294[14:15], doc294[15:16] ,doc294[17:18], doc294[42: 43], doc294[48: 49]) 
doc294.ents = [Span(doc294, 5, 8, label="CONTRACT"), 
    Span(doc294, 8, 9, label="CONTRACT1"), 
    Span(doc294, 10, 11, label="POS"), 
    Span(doc294, 11, 12, label="AMOUNT"), 
    Span(doc294, 13, 14, label="ARTICLE"), 
    Span(doc294, 14, 15, label="PRICE"), 
    Span(doc294, 15, 16, label="UNIT"), 
    Span(doc294, 17, 18, label="SUM"), 
    Span(doc294, 42, 43, label="TARIFF"), 
    Span(doc294, 48, 49, label="COUNTRY")] 
docs.append(doc294)


doc295 = nlp('''Purchase order number: N SR-1-06 1894
31200 50 PC 6020000616 (*) 27,42 100 PC 13,71

FI-VD-08L/S-V-W3
FI-VD-08L/S-B-W3
packed per each item


Description

Product description: Plug
Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc295SR-1-06 1894 31200 50 6020000616 27,42 100  73079910 Germany
print("doc295",doc295[5: 8], doc295[8: 9], doc295[10: 11], doc295[11: 12], doc295[13: 14], doc295[17:18], doc295[18:19] ,doc295[20:21], doc295[61: 62], doc295[67: 68]) 
doc295.ents = [Span(doc295, 5, 8, label="CONTRACT"), 
    Span(doc295, 8, 9, label="CONTRACT1"), 
    Span(doc295, 10, 11, label="POS"), 
    Span(doc295, 11, 12, label="AMOUNT"), 
    Span(doc295, 13, 14, label="ARTICLE"), 
    Span(doc295, 17, 18, label="PRICE"), 
    Span(doc295, 18, 19, label="UNIT"), 
    Span(doc295, 20, 21, label="SUM"), 
    Span(doc295, 61, 62, label="TARIFF"), 
    Span(doc295, 67, 68, label="COUNTRY")] 
docs.append(doc295)


doc296 = nlp('''Purchase order number: N SR-1-06 1894
31300 30 PC 6020000618 (*) 36,49 100 PC 10,95

FI-VD-12L/S-V-W3

FI-VD-12L/S-B-W3

packed per each item

Product description: Plug

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc296SR-1-06 1894 31300 30 6020000618 36,49 100  73079910 Germany
print("doc296",doc296[5: 8], doc296[8: 9], doc296[10: 11], doc296[11: 12], doc296[13: 14], doc296[17:18], doc296[18:19] ,doc296[20:21], doc296[59: 60], doc296[65: 66]) 
doc296.ents = [Span(doc296, 5, 8, label="CONTRACT"), 
    Span(doc296, 8, 9, label="CONTRACT1"), 
    Span(doc296, 10, 11, label="POS"), 
    Span(doc296, 11, 12, label="AMOUNT"), 
    Span(doc296, 13, 14, label="ARTICLE"), 
    Span(doc296, 17, 18, label="PRICE"), 
    Span(doc296, 18, 19, label="UNIT"), 
    Span(doc296, 20, 21, label="SUM"), 
    Span(doc296, 59, 60, label="TARIFF"), 
    Span(doc296, 65, 66, label="COUNTRY")] 
docs.append(doc296)


doc297 = nlp('''Purchase order number: N SR-1-06 1894
31400 50 PC 6020000630 (*) 50,31 100 PC 25,16

FI-VD-16S-V-W3

FI-VD-16S-B-W3

packed per each item

Product description: Plug

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc297SR-1-06 1894 31400 50 6020000630 50,31 100  73079910 Germany
print("doc297",doc297[5: 8], doc297[8: 9], doc297[10: 11], doc297[11: 12], doc297[13: 14], doc297[17:18], doc297[18:19] ,doc297[20:21], doc297[55: 56], doc297[61: 62]) 
doc297.ents = [Span(doc297, 5, 8, label="CONTRACT"), 
    Span(doc297, 8, 9, label="CONTRACT1"), 
    Span(doc297, 10, 11, label="POS"), 
    Span(doc297, 11, 12, label="AMOUNT"), 
    Span(doc297, 13, 14, label="ARTICLE"), 
    Span(doc297, 17, 18, label="PRICE"), 
    Span(doc297, 18, 19, label="UNIT"), 
    Span(doc297, 20, 21, label="SUM"), 
    Span(doc297, 55, 56, label="TARIFF"), 
    Span(doc297, 61, 62, label="COUNTRY")] 
docs.append(doc297)


doc298 = nlp('''Purchase order number: N SR-1-06 1894
31500 50 РС 6010001854 (*) 45,54 100 PC 22,77

FI-VS-R1/8-WD-B-W3
packed per each item
Product description: Plug


Description

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc298SR-1-06 1894 31500 50 6010001854 45,54 100  73079910 Germany
print("doc298",doc298[5: 8], doc298[8: 9], doc298[10: 11], doc298[11: 12], doc298[13: 14], doc298[17:18], doc298[18:19] ,doc298[20:21], doc298[53: 54], doc298[59: 60]) 
doc298.ents = [Span(doc298, 5, 8, label="CONTRACT"), 
    Span(doc298, 8, 9, label="CONTRACT1"), 
    Span(doc298, 10, 11, label="POS"), 
    Span(doc298, 11, 12, label="AMOUNT"), 
    Span(doc298, 13, 14, label="ARTICLE"), 
    Span(doc298, 17, 18, label="PRICE"), 
    Span(doc298, 18, 19, label="UNIT"), 
    Span(doc298, 20, 21, label="SUM"), 
    Span(doc298, 53, 54, label="TARIFF"), 
    Span(doc298, 59, 60, label="COUNTRY")] 
docs.append(doc298)


doc299 = nlp('''Purchase order number: N SR-1-06 1894
31600 50 PC 6030003785 (*) 76,71 100 PC 38,36
FI-VSK-08L-W3

packed per each item

Product description: Plug

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc299SR-1-06 1894 31600 50 6030003785 76,71 100  73079910 Germany
print("doc299",doc299[5: 8], doc299[8: 9], doc299[10: 11], doc299[11: 12], doc299[13: 14], doc299[17:18], doc299[18:19] ,doc299[20:21], doc299[45: 46], doc299[51: 52]) 
doc299.ents = [Span(doc299, 5, 8, label="CONTRACT"), 
    Span(doc299, 8, 9, label="CONTRACT1"), 
    Span(doc299, 10, 11, label="POS"), 
    Span(doc299, 11, 12, label="AMOUNT"), 
    Span(doc299, 13, 14, label="ARTICLE"), 
    Span(doc299, 17, 18, label="PRICE"), 
    Span(doc299, 18, 19, label="UNIT"), 
    Span(doc299, 20, 21, label="SUM"), 
    Span(doc299, 45, 46, label="TARIFF"), 
    Span(doc299, 51, 52, label="COUNTRY")] 
docs.append(doc299)


doc300 = nlp('''Purchase order number: N SR-1-06 1894
31700 50 PC 6030003795 (*) 93,83 100 PC 46,92
FI-VSK-08S-W3

packed per each item

Product description: Plug

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc300SR-1-06 1894 31700 50 6030003795 93,83 100  73079910 Germany
print("doc300",doc300[5: 8], doc300[8: 9], doc300[10: 11], doc300[11: 12], doc300[13: 14], doc300[17:18], doc300[18:19] ,doc300[20:21], doc300[45: 46], doc300[51: 52]) 
doc300.ents = [Span(doc300, 5, 8, label="CONTRACT"), 
    Span(doc300, 8, 9, label="CONTRACT1"), 
    Span(doc300, 10, 11, label="POS"), 
    Span(doc300, 11, 12, label="AMOUNT"), 
    Span(doc300, 13, 14, label="ARTICLE"), 
    Span(doc300, 17, 18, label="PRICE"), 
    Span(doc300, 18, 19, label="UNIT"), 
    Span(doc300, 20, 21, label="SUM"), 
    Span(doc300, 45, 46, label="TARIFF"), 
    Span(doc300, 51, 52, label="COUNTRY")] 
docs.append(doc300)


doc301 = nlp('''Purchase order number: N SR-1-06 1894
31800 30 PC 6030003797 (*) 127,28 100 PC 38,18
FI-VSK-12S-W3

packed per each item

Product description: Plug

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc301SR-1-06 1894 31800 30 6030003797 127,28 100  73079910 Germany
print("doc301",doc301[5: 8], doc301[8: 9], doc301[10: 11], doc301[11: 12], doc301[13: 14], doc301[17:18], doc301[18:19] ,doc301[20:21], doc301[45: 46], doc301[51: 52]) 
doc301.ents = [Span(doc301, 5, 8, label="CONTRACT"), 
    Span(doc301, 8, 9, label="CONTRACT1"), 
    Span(doc301, 10, 11, label="POS"), 
    Span(doc301, 11, 12, label="AMOUNT"), 
    Span(doc301, 13, 14, label="ARTICLE"), 
    Span(doc301, 17, 18, label="PRICE"), 
    Span(doc301, 18, 19, label="UNIT"), 
    Span(doc301, 20, 21, label="SUM"), 
    Span(doc301, 45, 46, label="TARIFF"), 
    Span(doc301, 51, 52, label="COUNTRY")] 
docs.append(doc301)


doc302 = nlp('''Purchase order number: N SR-1-06 1894
31900 50 PC 6030003799 (*) 232,43 100 PC 116,22
FI-VSK-16S-W3

packed per each item

Product description: Plug

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc302SR-1-06 1894 31900 50 6030003799 232,43 100  73079910 Germany
print("doc302",doc302[5: 8], doc302[8: 9], doc302[10: 11], doc302[11: 12], doc302[13: 14], doc302[17:18], doc302[18:19] ,doc302[20:21], doc302[45: 46], doc302[51: 52]) 
doc302.ents = [Span(doc302, 5, 8, label="CONTRACT"), 
    Span(doc302, 8, 9, label="CONTRACT1"), 
    Span(doc302, 10, 11, label="POS"), 
    Span(doc302, 11, 12, label="AMOUNT"), 
    Span(doc302, 13, 14, label="ARTICLE"), 
    Span(doc302, 17, 18, label="PRICE"), 
    Span(doc302, 18, 19, label="UNIT"), 
    Span(doc302, 20, 21, label="SUM"), 
    Span(doc302, 45, 46, label="TARIFF"), 
    Span(doc302, 51, 52, label="COUNTRY")] 
docs.append(doc302)


doc303 = nlp('''Purchase order number: N SR-1-06 1894
32000 30 PC 6030003800 (*) 350,16 100 PC 105,05
FI-VSK-20S-W3

packed per each item

Product description: Plug

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc303SR-1-06 1894 32000 30 6030003800 350,16 100  73079910 Germany
print("doc303",doc303[5: 8], doc303[8: 9], doc303[10: 11], doc303[11: 12], doc303[13: 14], doc303[17:18], doc303[18:19] ,doc303[20:21], doc303[45: 46], doc303[51: 52]) 
doc303.ents = [Span(doc303, 5, 8, label="CONTRACT"), 
    Span(doc303, 8, 9, label="CONTRACT1"), 
    Span(doc303, 10, 11, label="POS"), 
    Span(doc303, 11, 12, label="AMOUNT"), 
    Span(doc303, 13, 14, label="ARTICLE"), 
    Span(doc303, 17, 18, label="PRICE"), 
    Span(doc303, 18, 19, label="UNIT"), 
    Span(doc303, 20, 21, label="SUM"), 
    Span(doc303, 45, 46, label="TARIFF"), 
    Span(doc303, 51, 52, label="COUNTRY")] 
docs.append(doc303)


doc304 = nlp('''Purchase order number: N SR-1-06 1894
32100 10 PC 6020000933 (*) 3.023,53 100 PC 302,35

FI-RED-R2-WD-R1 -1/2-B-W3
FI-RED-R2-WD-R1 1/2-B-W3

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc304SR-1-06 1894 32100 10 6020000933 3.023,53 100  73079910 Germany
print("doc304",doc304[5: 8], doc304[8: 9], doc304[10: 11], doc304[11: 12], doc304[13: 14], doc304[17:18], doc304[18:19] ,doc304[20:21], doc304[69: 70], doc304[75: 76]) 
doc304.ents = [Span(doc304, 5, 8, label="CONTRACT"), 
    Span(doc304, 8, 9, label="CONTRACT1"), 
    Span(doc304, 10, 11, label="POS"), 
    Span(doc304, 11, 12, label="AMOUNT"), 
    Span(doc304, 13, 14, label="ARTICLE"), 
    Span(doc304, 17, 18, label="PRICE"), 
    Span(doc304, 18, 19, label="UNIT"), 
    Span(doc304, 20, 21, label="SUM"), 
    Span(doc304, 69, 70, label="TARIFF"), 
    Span(doc304, 75, 76, label="COUNTRY")] 
docs.append(doc304)


doc305 = nlp('''Purchase order number: N SR-1-06 1894
32200 10 PC 6020000934 (*) 3.106,81 100 PC 310,68

FI-RED-R2-WD-R1 -1/4-B-W3
FI-RED-R2-WD-R1 1/4-B-W3

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc305SR-1-06 1894 32200 10 6020000934 3.106,81 100  73079910 Germany
print("doc305",doc305[5: 8], doc305[8: 9], doc305[10: 11], doc305[11: 12], doc305[13: 14], doc305[17:18], doc305[18:19] ,doc305[20:21], doc305[69: 70], doc305[75: 76]) 
doc305.ents = [Span(doc305, 5, 8, label="CONTRACT"), 
    Span(doc305, 8, 9, label="CONTRACT1"), 
    Span(doc305, 10, 11, label="POS"), 
    Span(doc305, 11, 12, label="AMOUNT"), 
    Span(doc305, 13, 14, label="ARTICLE"), 
    Span(doc305, 17, 18, label="PRICE"), 
    Span(doc305, 18, 19, label="UNIT"), 
    Span(doc305, 20, 21, label="SUM"), 
    Span(doc305, 69, 70, label="TARIFF"), 
    Span(doc305, 75, 76, label="COUNTRY")] 
docs.append(doc305)


doc306 = nlp('''Purchase order number: N SR-1-06 1894
32300 10 PC 6010003566 (*) 1.726,57 100 PC 172,66

FI-EWD-38S-V-W3-DKO
FI-EWD-38S-B-W3-DKO

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc306SR-1-06 1894 32300 10 6010003566 1.726,57 100  73079910 Germany
print("doc306",doc306[5: 8], doc306[8: 9], doc306[10: 11], doc306[11: 12], doc306[13: 14], doc306[17:18], doc306[18:19] ,doc306[20:21], doc306[59: 60], doc306[65: 66]) 
doc306.ents = [Span(doc306, 5, 8, label="CONTRACT"), 
    Span(doc306, 8, 9, label="CONTRACT1"), 
    Span(doc306, 10, 11, label="POS"), 
    Span(doc306, 11, 12, label="AMOUNT"), 
    Span(doc306, 13, 14, label="ARTICLE"), 
    Span(doc306, 17, 18, label="PRICE"), 
    Span(doc306, 18, 19, label="UNIT"), 
    Span(doc306, 20, 21, label="SUM"), 
    Span(doc306, 59, 60, label="TARIFF"), 
    Span(doc306, 65, 66, label="COUNTRY")] 
docs.append(doc306)


doc307 = nlp('''Purchase order number: N SR-1-06 1894
32400 10 PC 6010003506 (*) 1.689,35 100 PC 168,94

FI-EWD-42L-V-W3-DKO
FI-EWD-42L-B-W3-DKO

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc307SR-1-06 1894 32400 10 6010003506 1.689,35 100  73079910 Germany
print("doc307",doc307[5: 8], doc307[8: 9], doc307[10: 11], doc307[11: 12], doc307[13: 14], doc307[17:18], doc307[18:19] ,doc307[20:21], doc307[59: 60], doc307[65: 66]) 
doc307.ents = [Span(doc307, 5, 8, label="CONTRACT"), 
    Span(doc307, 8, 9, label="CONTRACT1"), 
    Span(doc307, 10, 11, label="POS"), 
    Span(doc307, 11, 12, label="AMOUNT"), 
    Span(doc307, 13, 14, label="ARTICLE"), 
    Span(doc307, 17, 18, label="PRICE"), 
    Span(doc307, 18, 19, label="UNIT"), 
    Span(doc307, 20, 21, label="SUM"), 
    Span(doc307, 59, 60, label="TARIFF"), 
    Span(doc307, 65, 66, label="COUNTRY")] 
docs.append(doc307)


doc308 = nlp('''Purchase order number: N SR-1-06 1894
32500 100 PC 6020000471 (*) 49,81 100 PC 49,81

FI-GE-10LR-WD-B-W3

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc308SR-1-06 1894 32500 100 6020000471 49,81 100  73079910 Germany
print("doc308",doc308[5: 8], doc308[8: 9], doc308[10: 11], doc308[11: 12], doc308[13: 14], doc308[17:18], doc308[18:19] ,doc308[20:21], doc308[49: 50], doc308[55: 56]) 
doc308.ents = [Span(doc308, 5, 8, label="CONTRACT"), 
    Span(doc308, 8, 9, label="CONTRACT1"), 
    Span(doc308, 10, 11, label="POS"), 
    Span(doc308, 11, 12, label="AMOUNT"), 
    Span(doc308, 13, 14, label="ARTICLE"), 
    Span(doc308, 17, 18, label="PRICE"), 
    Span(doc308, 18, 19, label="UNIT"), 
    Span(doc308, 20, 21, label="SUM"), 
    Span(doc308, 49, 50, label="TARIFF"), 
    Span(doc308, 55, 56, label="COUNTRY")] 
docs.append(doc308)


doc309 = nlp('''Purchase order number: N SR-1-06 1894
32600 10 PC 6020000548 (*) 634,39 100 PC 63,44

FI-GE-38 SR1 -1/4-WD-B-W3

FI-GE-38SR1_ 1/4-WD-B-W3

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc309SR-1-06 1894 32600 10 6020000548 634,39 100  73079910 Germany
print("doc309",doc309[5: 8], doc309[8: 9], doc309[10: 11], doc309[11: 12], doc309[13: 14], doc309[17:18], doc309[18:19] ,doc309[20:21], doc309[63: 64], doc309[69: 70]) 
doc309.ents = [Span(doc309, 5, 8, label="CONTRACT"), 
    Span(doc309, 8, 9, label="CONTRACT1"), 
    Span(doc309, 10, 11, label="POS"), 
    Span(doc309, 11, 12, label="AMOUNT"), 
    Span(doc309, 13, 14, label="ARTICLE"), 
    Span(doc309, 17, 18, label="PRICE"), 
    Span(doc309, 18, 19, label="UNIT"), 
    Span(doc309, 20, 21, label="SUM"), 
    Span(doc309, 63, 64, label="TARIFF"), 
    Span(doc309, 69, 70, label="COUNTRY")] 
docs.append(doc309)


doc310 = nlp('''Purchase order number: N SR-1-06 1894
32700 10 PC 6020000555 (*) 550,36 100 PC 55,04

FI-GE-42LR1 -1/4-WD-B-W3

FI-GE-42LR1 1/4-WD-B-W3

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc310SR-1-06 1894 32700 10 6020000555 550,36 100  73079910 Germany
print("doc310",doc310[5: 8], doc310[8: 9], doc310[10: 11], doc310[11: 12], doc310[13: 14], doc310[17:18], doc310[18:19] ,doc310[20:21], doc310[61: 62], doc310[67: 68]) 
doc310.ents = [Span(doc310, 5, 8, label="CONTRACT"), 
    Span(doc310, 8, 9, label="CONTRACT1"), 
    Span(doc310, 10, 11, label="POS"), 
    Span(doc310, 11, 12, label="AMOUNT"), 
    Span(doc310, 13, 14, label="ARTICLE"), 
    Span(doc310, 17, 18, label="PRICE"), 
    Span(doc310, 18, 19, label="UNIT"), 
    Span(doc310, 20, 21, label="SUM"), 
    Span(doc310, 61, 62, label="TARIFF"), 
    Span(doc310, 67, 68, label="COUNTRY")] 
docs.append(doc310)


doc311 = nlp('''Purchase order number: N SR-1-06 1894
32800 10 PC 6020000564 (*) 714,63 100 PC 71,46

FI-GE-42LR1-WD-B-W3

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc311SR-1-06 1894 32800 10 6020000564 714,63 100  73079910 Germany
print("doc311",doc311[5: 8], doc311[8: 9], doc311[10: 11], doc311[11: 12], doc311[13: 14], doc311[17:18], doc311[18:19] ,doc311[20:21], doc311[49: 50], doc311[55: 56]) 
doc311.ents = [Span(doc311, 5, 8, label="CONTRACT"), 
    Span(doc311, 8, 9, label="CONTRACT1"), 
    Span(doc311, 10, 11, label="POS"), 
    Span(doc311, 11, 12, label="AMOUNT"), 
    Span(doc311, 13, 14, label="ARTICLE"), 
    Span(doc311, 17, 18, label="PRICE"), 
    Span(doc311, 18, 19, label="UNIT"), 
    Span(doc311, 20, 21, label="SUM"), 
    Span(doc311, 49, 50, label="TARIFF"), 
    Span(doc311, 55, 56, label="COUNTRY")] 
docs.append(doc311)


doc312 = nlp('''Purchase order number: N SR-1-06 1894
32900 10 PC 6010003220 (*) 1.152,06 100 PC 115,21

FI-SNV-38S-V-W3-DKO
FI-SNV-38S-B-W3-DKO

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc312SR-1-06 1894 32900 10 6010003220 1.152,06 100  73079910 Germany
print("doc312",doc312[5: 8], doc312[8: 9], doc312[10: 11], doc312[11: 12], doc312[13: 14], doc312[17:18], doc312[18:19] ,doc312[20:21], doc312[59: 60], doc312[65: 66]) 
doc312.ents = [Span(doc312, 5, 8, label="CONTRACT"), 
    Span(doc312, 8, 9, label="CONTRACT1"), 
    Span(doc312, 10, 11, label="POS"), 
    Span(doc312, 11, 12, label="AMOUNT"), 
    Span(doc312, 13, 14, label="ARTICLE"), 
    Span(doc312, 17, 18, label="PRICE"), 
    Span(doc312, 18, 19, label="UNIT"), 
    Span(doc312, 20, 21, label="SUM"), 
    Span(doc312, 59, 60, label="TARIFF"), 
    Span(doc312, 65, 66, label="COUNTRY")] 
docs.append(doc312)


doc313 = nlp('''Purchase order number: N SR-1-06 1892
33000 100 PC 6030002403 (*) 40,23 100 PC 40,23

FI-DKI-R1/2-W3-WOB

packed per each item

Product description: ring

Export - Customs tariff no.: 73182900
Country of origin: Germany''')
#doc313SR-1-06 1892 33000 100 6030002403 40,23 100  73182900 Germany
print("doc313",doc313[5: 8], doc313[8: 9], doc313[10: 11], doc313[11: 12], doc313[13: 14], doc313[17:18], doc313[18:19] ,doc313[20:21], doc313[49: 50], doc313[55: 56]) 
doc313.ents = [Span(doc313, 5, 8, label="CONTRACT"), 
    Span(doc313, 8, 9, label="CONTRACT1"), 
    Span(doc313, 10, 11, label="POS"), 
    Span(doc313, 11, 12, label="AMOUNT"), 
    Span(doc313, 13, 14, label="ARTICLE"), 
    Span(doc313, 17, 18, label="PRICE"), 
    Span(doc313, 18, 19, label="UNIT"), 
    Span(doc313, 20, 21, label="SUM"), 
    Span(doc313, 49, 50, label="TARIFF"), 
    Span(doc313, 55, 56, label="COUNTRY")] 
docs.append(doc313)


doc314 = nlp('''Purchase order number: N SR-1-06 1891
33100 6 PC 6010001888 (*) 622,07 100 PC 37,32


Description

FI-REDS-35/18L-W3-SV

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc314SR-1-06 1891 33100 6 6010001888 622,07 100  73079910 Germany
print("doc314",doc314[5: 8], doc314[8: 9], doc314[10: 11], doc314[11: 12], doc314[13: 14], doc314[17:18], doc314[18:19] ,doc314[20:21], doc314[49: 50], doc314[55: 56]) 
doc314.ents = [Span(doc314, 5, 8, label="CONTRACT"), 
    Span(doc314, 8, 9, label="CONTRACT1"), 
    Span(doc314, 10, 11, label="POS"), 
    Span(doc314, 11, 12, label="AMOUNT"), 
    Span(doc314, 13, 14, label="ARTICLE"), 
    Span(doc314, 17, 18, label="PRICE"), 
    Span(doc314, 18, 19, label="UNIT"), 
    Span(doc314, 20, 21, label="SUM"), 
    Span(doc314, 49, 50, label="TARIFF"), 
    Span(doc314, 55, 56, label="COUNTRY")] 
docs.append(doc314)


doc315 = nlp('''Purchase order number: N SR-1-06 1891
33200 35 РС 6010002010 (*) 328,02 100 PC 114,81

FI-EW-18L-W3-SV

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079290
Country of origin: Germany''')
#doc315SR-1-06 1891 33200 35 6010002010 328,02 100  73079290 Germany
print("doc315",doc315[5: 8], doc315[8: 9], doc315[10: 11], doc315[11: 12], doc315[13: 14], doc315[17:18], doc315[18:19] ,doc315[20:21], doc315[47: 48], doc315[53: 54]) 
doc315.ents = [Span(doc315, 5, 8, label="CONTRACT"), 
    Span(doc315, 8, 9, label="CONTRACT1"), 
    Span(doc315, 10, 11, label="POS"), 
    Span(doc315, 11, 12, label="AMOUNT"), 
    Span(doc315, 13, 14, label="ARTICLE"), 
    Span(doc315, 17, 18, label="PRICE"), 
    Span(doc315, 18, 19, label="UNIT"), 
    Span(doc315, 20, 21, label="SUM"), 
    Span(doc315, 47, 48, label="TARIFF"), 
    Span(doc315, 53, 54, label="COUNTRY")] 
docs.append(doc315)


doc316 = nlp('''Purchase order number: N SR-1-06 1891
33300 8 PC 6030003852 1.003,65 100 PC 80,29
FI-T-35L-W3

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc316SR-1-06 1891 33300 8 6030003852 1.003,65 100  73079910 Germany
print("doc316",doc316[5: 8], doc316[8: 9], doc316[10: 11], doc316[11: 12], doc316[13: 14], doc316[14:15], doc316[15:16] ,doc316[17:18], doc316[42: 43], doc316[48: 49]) 
doc316.ents = [Span(doc316, 5, 8, label="CONTRACT"), 
    Span(doc316, 8, 9, label="CONTRACT1"), 
    Span(doc316, 10, 11, label="POS"), 
    Span(doc316, 11, 12, label="AMOUNT"), 
    Span(doc316, 13, 14, label="ARTICLE"), 
    Span(doc316, 14, 15, label="PRICE"), 
    Span(doc316, 15, 16, label="UNIT"), 
    Span(doc316, 17, 18, label="SUM"), 
    Span(doc316, 42, 43, label="TARIFF"), 
    Span(doc316, 48, 49, label="COUNTRY")] 
docs.append(doc316)


doc317 = nlp('''Purchase order number: N SR-1-06 1889
33400 40 РС 6100152347 12,73 100 РС 5,09

SM-1-8/1D-M-W3/2
packed per each item
Customer ID-No.: 000000001120001932


Description

Product description: nuts
Export - Customs tariff no.: 73181692
Country of origin: Germany''')
#doc317SR-1-06 1889 33400 40 6100152347 12,73 100  73181692 Germany
print("doc317",doc317[5: 8], doc317[8: 9], doc317[10: 11], doc317[11: 12], doc317[13: 14], doc317[14:15], doc317[15:16] ,doc317[17:18], doc317[54: 55], doc317[60: 61]) 
doc317.ents = [Span(doc317, 5, 8, label="CONTRACT"), 
    Span(doc317, 8, 9, label="CONTRACT1"), 
    Span(doc317, 10, 11, label="POS"), 
    Span(doc317, 11, 12, label="AMOUNT"), 
    Span(doc317, 13, 14, label="ARTICLE"), 
    Span(doc317, 14, 15, label="PRICE"), 
    Span(doc317, 15, 16, label="UNIT"), 
    Span(doc317, 17, 18, label="SUM"), 
    Span(doc317, 54, 55, label="TARIFF"), 
    Span(doc317, 60, 61, label="COUNTRY")] 
docs.append(doc317)


doc318 = nlp('''Purchase order number: N SR-1-06 1888
33500 1 РС 1020022803 180,76 1 РС 180,76

RE-600-G-10-B/5-NB
RE-600G10B/5-1613

packed per each item

Product description: filter element
Export - Customs tariff no.: 84219990
Country of origin: Germany''')
#doc318SR-1-06 1888 33500 1 1020022803 180,76 1  84219990 Germany
print("doc318",doc318[5: 8], doc318[8: 9], doc318[10: 11], doc318[11: 12], doc318[13: 14], doc318[14:15], doc318[15:16] ,doc318[17:18], doc318[49: 50], doc318[55: 56]) 
doc318.ents = [Span(doc318, 5, 8, label="CONTRACT"), 
    Span(doc318, 8, 9, label="CONTRACT1"), 
    Span(doc318, 10, 11, label="POS"), 
    Span(doc318, 11, 12, label="AMOUNT"), 
    Span(doc318, 13, 14, label="ARTICLE"), 
    Span(doc318, 14, 15, label="PRICE"), 
    Span(doc318, 15, 16, label="UNIT"), 
    Span(doc318, 17, 18, label="SUM"), 
    Span(doc318, 49, 50, label="TARIFF"), 
    Span(doc318, 55, 56, label="COUNTRY")] 
docs.append(doc318)


doc319 = nlp('''Purchase order number: N SR-1-06 1886
33600 40 РС 1130005956 61,13 100 РС 24,45
532-РР-Н
532 РРН
packed per each item
Product description: Pipe clamp
Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc319SR-1-06 1886 33600 40 1130005956 61,13 100  39269097 Germany
print("doc319",doc319[5: 8], doc319[8: 9], doc319[10: 11], doc319[11: 12], doc319[13: 14], doc319[14:15], doc319[15:16] ,doc319[17:18], doc319[46: 47], doc319[52: 53]) 
doc319.ents = [Span(doc319, 5, 8, label="CONTRACT"), 
    Span(doc319, 8, 9, label="CONTRACT1"), 
    Span(doc319, 10, 11, label="POS"), 
    Span(doc319, 11, 12, label="AMOUNT"), 
    Span(doc319, 13, 14, label="ARTICLE"), 
    Span(doc319, 14, 15, label="PRICE"), 
    Span(doc319, 15, 16, label="UNIT"), 
    Span(doc319, 17, 18, label="SUM"), 
    Span(doc319, 46, 47, label="TARIFF"), 
    Span(doc319, 52, 53, label="COUNTRY")] 
docs.append(doc319)


doc320 = nlp('''Purchase order number: N SR-1-06 1885
33700 10 PC 1930000207 0,07 1 РС 0,70
SRF-08-PP

packed per each item


Description

Product description: seal
Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc320SR-1-06 1885 33700 10 1930000207 0,07 1  39269097 Germany
print("doc320",doc320[5: 8], doc320[8: 9], doc320[10: 11], doc320[11: 12], doc320[13: 14], doc320[14:15], doc320[15:16] ,doc320[17:18], doc320[42: 43], doc320[48: 49]) 
doc320.ents = [Span(doc320, 5, 8, label="CONTRACT"), 
    Span(doc320, 8, 9, label="CONTRACT1"), 
    Span(doc320, 10, 11, label="POS"), 
    Span(doc320, 11, 12, label="AMOUNT"), 
    Span(doc320, 13, 14, label="ARTICLE"), 
    Span(doc320, 14, 15, label="PRICE"), 
    Span(doc320, 15, 16, label="UNIT"), 
    Span(doc320, 17, 18, label="SUM"), 
    Span(doc320, 42, 43, label="TARIFF"), 
    Span(doc320, 48, 49, label="COUNTRY")] 
docs.append(doc320)


doc321 = nlp('''Purchase order number: N SR-1-06 1885
33800 50 РС 1130005264 52,17 100 РС 26,09

213.5/13.5-РА

213,5/13,5 РА

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc321SR-1-06 1885 33800 50 1130005264 52,17 100  39269097 Germany
print("doc321",doc321[5: 8], doc321[8: 9], doc321[10: 11], doc321[11: 12], doc321[13: 14], doc321[14:15], doc321[15:16] ,doc321[17:18], doc321[44: 45], doc321[50: 51]) 
doc321.ents = [Span(doc321, 5, 8, label="CONTRACT"), 
    Span(doc321, 8, 9, label="CONTRACT1"), 
    Span(doc321, 10, 11, label="POS"), 
    Span(doc321, 11, 12, label="AMOUNT"), 
    Span(doc321, 13, 14, label="ARTICLE"), 
    Span(doc321, 14, 15, label="PRICE"), 
    Span(doc321, 15, 16, label="UNIT"), 
    Span(doc321, 17, 18, label="SUM"), 
    Span(doc321, 44, 45, label="TARIFF"), 
    Span(doc321, 50, 51, label="COUNTRY")] 
docs.append(doc321)


doc322 = nlp('''Purchase order number: N SR-1-06 1885
33900 25 РС 1130005318 52,17 100 РС 13,04
215/15-PA
215/15 PA

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc322SR-1-06 1885 33900 25 1130005318 52,17 100  39269097 Germany
print("doc322",doc322[5: 8], doc322[8: 9], doc322[10: 11], doc322[11: 12], doc322[13: 14], doc322[14:15], doc322[15:16] ,doc322[17:18], doc322[44: 45], doc322[50: 51]) 
doc322.ents = [Span(doc322, 5, 8, label="CONTRACT"), 
    Span(doc322, 8, 9, label="CONTRACT1"), 
    Span(doc322, 10, 11, label="POS"), 
    Span(doc322, 11, 12, label="AMOUNT"), 
    Span(doc322, 13, 14, label="ARTICLE"), 
    Span(doc322, 14, 15, label="PRICE"), 
    Span(doc322, 15, 16, label="UNIT"), 
    Span(doc322, 17, 18, label="SUM"), 
    Span(doc322, 44, 45, label="TARIFF"), 
    Span(doc322, 50, 51, label="COUNTRY")] 
docs.append(doc322)


doc323 = nlp('''Purchase order number: N SR-1-06 1885
34000 50 РС 1130005357 52,17 100 РС 26,09
216/16-РА
216/16 РА

packed per each item


Description

Product description: Pipe clamp
Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc323SR-1-06 1885 34000 50 1130005357 52,17 100  39269097 Germany
print("doc323",doc323[5: 8], doc323[8: 9], doc323[10: 11], doc323[11: 12], doc323[13: 14], doc323[14:15], doc323[15:16] ,doc323[17:18], doc323[46: 47], doc323[52: 53]) 
doc323.ents = [Span(doc323, 5, 8, label="CONTRACT"), 
    Span(doc323, 8, 9, label="CONTRACT1"), 
    Span(doc323, 10, 11, label="POS"), 
    Span(doc323, 11, 12, label="AMOUNT"), 
    Span(doc323, 13, 14, label="ARTICLE"), 
    Span(doc323, 14, 15, label="PRICE"), 
    Span(doc323, 15, 16, label="UNIT"), 
    Span(doc323, 17, 18, label="SUM"), 
    Span(doc323, 46, 47, label="TARIFF"), 
    Span(doc323, 52, 53, label="COUNTRY")] 
docs.append(doc323)


doc324 = nlp('''Purchase order number: N SR-1-06 1884
34100 2 PC 6020000331 (*) 111,43 100 PC 2,23

FI-RED-R3/4-WD-R3/8-B-W3

packed per each item

Product description: fitting

Export - Customs tariff no.: 73079910
Country of origin: Germany''')
#doc324SR-1-06 1884 34100 2 6020000331 111,43 100  73079910 Germany
print("doc324",doc324[5: 8], doc324[8: 9], doc324[10: 11], doc324[11: 12], doc324[13: 14], doc324[17:18], doc324[18:19] ,doc324[20:21], doc324[53: 54], doc324[59: 60]) 
doc324.ents = [Span(doc324, 5, 8, label="CONTRACT"), 
    Span(doc324, 8, 9, label="CONTRACT1"), 
    Span(doc324, 10, 11, label="POS"), 
    Span(doc324, 11, 12, label="AMOUNT"), 
    Span(doc324, 13, 14, label="ARTICLE"), 
    Span(doc324, 17, 18, label="PRICE"), 
    Span(doc324, 18, 19, label="UNIT"), 
    Span(doc324, 20, 21, label="SUM"), 
    Span(doc324, 53, 54, label="TARIFF"), 
    Span(doc324, 59, 60, label="COUNTRY")] 
docs.append(doc324)


doc325 = nlp('''Purchase order number: N SR-1-06 1883
34200 20 РС 1130004024 5,48 100 PC 1,10

AS-M6x60-DIN931/933-8.8-W3
AS-M6X60-DIN931/933-8.8-W3
packed per each item

Product description: screw

Export - Customs tariff по.: 73181588
Country of origin: Turkey''')
#doc325SR-1-06 1883 34200 20 1130004024 5,48 100  73181588 Turkey
print("doc325",doc325[5: 8], doc325[8: 9], doc325[10: 11], doc325[11: 12], doc325[13: 14], doc325[14:15], doc325[15:16] ,doc325[17:18], doc325[56: 57], doc325[62: 63]) 
doc325.ents = [Span(doc325, 5, 8, label="CONTRACT"), 
    Span(doc325, 8, 9, label="CONTRACT1"), 
    Span(doc325, 10, 11, label="POS"), 
    Span(doc325, 11, 12, label="AMOUNT"), 
    Span(doc325, 13, 14, label="ARTICLE"), 
    Span(doc325, 14, 15, label="PRICE"), 
    Span(doc325, 15, 16, label="UNIT"), 
    Span(doc325, 17, 18, label="SUM"), 
    Span(doc325, 56, 57, label="TARIFF"), 
    Span(doc325, 62, 63, label="COUNTRY")] 
docs.append(doc325)


doc326 = nlp('''Purchase order number: N SR-1-06 1882
34300 160 РС 1120003494 (*) 83,02 100 PC 132,83
AF-4S-M-W2

AF 4 S M W2 M10x40
packed per each item
Product description: screw


Description

Export - Customs tariff по.: 73181588
Country of origin: Germany''')
#doc326SR-1-06 1882 34300 160 1120003494 83,02 100  73181588 Germany
print("doc326",doc326[5: 8], doc326[8: 9], doc326[10: 11], doc326[11: 12], doc326[13: 14], doc326[17:18], doc326[18:19] ,doc326[20:21], doc326[54: 55], doc326[60: 61]) 
doc326.ents = [Span(doc326, 5, 8, label="CONTRACT"), 
    Span(doc326, 8, 9, label="CONTRACT1"), 
    Span(doc326, 10, 11, label="POS"), 
    Span(doc326, 11, 12, label="AMOUNT"), 
    Span(doc326, 13, 14, label="ARTICLE"), 
    Span(doc326, 17, 18, label="PRICE"), 
    Span(doc326, 18, 19, label="UNIT"), 
    Span(doc326, 20, 21, label="SUM"), 
    Span(doc326, 54, 55, label="TARIFF"), 
    Span(doc326, 60, 61, label="COUNTRY")] 
docs.append(doc326)


doc327 = nlp('''Purchase order number: N SR-1-06 1882
34400 100 PC 1130005688 58,60 100 PC 58,60
4020-PP
4020 PP

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc327SR-1-06 1882 34400 100 1130005688 58,60 100  39269097 Germany
print("doc327",doc327[5: 8], doc327[8: 9], doc327[10: 11], doc327[11: 12], doc327[13: 14], doc327[14:15], doc327[15:16] ,doc327[17:18], doc327[44: 45], doc327[50: 51]) 
doc327.ents = [Span(doc327, 5, 8, label="CONTRACT"), 
    Span(doc327, 8, 9, label="CONTRACT1"), 
    Span(doc327, 10, 11, label="POS"), 
    Span(doc327, 11, 12, label="AMOUNT"), 
    Span(doc327, 13, 14, label="ARTICLE"), 
    Span(doc327, 14, 15, label="PRICE"), 
    Span(doc327, 15, 16, label="UNIT"), 
    Span(doc327, 17, 18, label="SUM"), 
    Span(doc327, 44, 45, label="TARIFF"), 
    Span(doc327, 50, 51, label="COUNTRY")] 
docs.append(doc327)


doc328 = nlp('''Purchase order number: N SR-1-06 1882
34500 80 РС 1130000838 51,55 100 PC 41,24
SIP-4S-W2
ЯР 4 $ W2

packed per each item

Product description: locking plate
Export - Customs tariff по.: 73182100
Country of origin: Germany''')
#doc328SR-1-06 1882 34500 80 1130000838 51,55 100  73182100 Germany
print("doc328",doc328[5: 8], doc328[8: 9], doc328[10: 11], doc328[11: 12], doc328[13: 14], doc328[14:15], doc328[15:16] ,doc328[17:18], doc328[46: 47], doc328[52: 53]) 
doc328.ents = [Span(doc328, 5, 8, label="CONTRACT"), 
    Span(doc328, 8, 9, label="CONTRACT1"), 
    Span(doc328, 10, 11, label="POS"), 
    Span(doc328, 11, 12, label="AMOUNT"), 
    Span(doc328, 13, 14, label="ARTICLE"), 
    Span(doc328, 14, 15, label="PRICE"), 
    Span(doc328, 15, 16, label="UNIT"), 
    Span(doc328, 17, 18, label="SUM"), 
    Span(doc328, 46, 47, label="TARIFF"), 
    Span(doc328, 52, 53, label="COUNTRY")] 
docs.append(doc328)


doc329 = nlp('''Purchase order number: N SR-1-06 1882
34600 80 РС 1120001950 76,42 100 РС 61,14
SPAL-4S-M-W2

SPAL 4 S M W2
packed per each item
Product description: weld plate


Description

Export - Customs tariff no.: 73269098
Country of origin: Germany''')
#doc329SR-1-06 1882 34600 80 1120001950 76,42 100  73269098 Germany
print("doc329",doc329[5: 8], doc329[8: 9], doc329[10: 11], doc329[11: 12], doc329[13: 14], doc329[14:15], doc329[15:16] ,doc329[17:18], doc329[51: 52], doc329[57: 58]) 
doc329.ents = [Span(doc329, 5, 8, label="CONTRACT"), 
    Span(doc329, 8, 9, label="CONTRACT1"), 
    Span(doc329, 10, 11, label="POS"), 
    Span(doc329, 11, 12, label="AMOUNT"), 
    Span(doc329, 13, 14, label="ARTICLE"), 
    Span(doc329, 14, 15, label="PRICE"), 
    Span(doc329, 15, 16, label="UNIT"), 
    Span(doc329, 17, 18, label="SUM"), 
    Span(doc329, 51, 52, label="TARIFF"), 
    Span(doc329, 57, 58, label="COUNTRY")] 
docs.append(doc329)


doc330 = nlp('''Purchase order number: N SR-1-06 1898
34700 50 РС 1130005997 51,18 100 PC 25,59
535-PP
535 PP

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc330SR-1-06 1898 34700 50 1130005997 51,18 100  39269097 Germany
print("doc330",doc330[5: 8], doc330[8: 9], doc330[10: 11], doc330[11: 12], doc330[13: 14], doc330[14:15], doc330[15:16] ,doc330[17:18], doc330[44: 45], doc330[50: 51]) 
doc330.ents = [Span(doc330, 5, 8, label="CONTRACT"), 
    Span(doc330, 8, 9, label="CONTRACT1"), 
    Span(doc330, 10, 11, label="POS"), 
    Span(doc330, 11, 12, label="AMOUNT"), 
    Span(doc330, 13, 14, label="ARTICLE"), 
    Span(doc330, 14, 15, label="PRICE"), 
    Span(doc330, 15, 16, label="UNIT"), 
    Span(doc330, 17, 18, label="SUM"), 
    Span(doc330, 44, 45, label="TARIFF"), 
    Span(doc330, 50, 51, label="COUNTRY")] 
docs.append(doc330)


doc331 = nlp('''Purchase order number: N SR-1-06 1898
34800 25 РС 1130003563 87,67 100 РС 21,92
654-РР
654 РР

packed per each item

Product description: Pipe clamp

Export - Customs tariff no.: 39269097
Country of origin: Germany''')
#doc331SR-1-06 1898 34800 25 1130003563 87,67 100  39269097 Germany
print("doc331",doc331[5: 8], doc331[8: 9], doc331[10: 11], doc331[11: 12], doc331[13: 14], doc331[14:15], doc331[15:16] ,doc331[17:18], doc331[44: 45], doc331[50: 51]) 
doc331.ents = [Span(doc331, 5, 8, label="CONTRACT"), 
    Span(doc331, 8, 9, label="CONTRACT1"), 
    Span(doc331, 10, 11, label="POS"), 
    Span(doc331, 11, 12, label="AMOUNT"), 
    Span(doc331, 13, 14, label="ARTICLE"), 
    Span(doc331, 14, 15, label="PRICE"), 
    Span(doc331, 15, 16, label="UNIT"), 
    Span(doc331, 17, 18, label="SUM"), 
    Span(doc331, 44, 45, label="TARIFF"), 
    Span(doc331, 50, 51, label="COUNTRY")] 
docs.append(doc331)


doc332 = nlp('''Purchase order number: N SR-1-06 1897
34900 10 PC 1730000063 3,84 1 РС 38,40
DB-604-W66
DB-604

Qty/Unit PC = Pair
packed per each item


Description

Product description: flange
Export - Customs tariff no.: 73079100
Country of origin: Italy''')
#doc332SR-1-06 1897 34900 10 1730000063 3,84 1  73079100 Italy
print("doc332",doc332[5: 8], doc332[8: 9], doc332[10: 11], doc332[11: 12], doc332[13: 14], doc332[14:15], doc332[15:16] ,doc332[17:18], doc332[51: 52], doc332[57: 58]) 
doc332.ents = [Span(doc332, 5, 8, label="CONTRACT"), 
    Span(doc332, 8, 9, label="CONTRACT1"), 
    Span(doc332, 10, 11, label="POS"), 
    Span(doc332, 11, 12, label="AMOUNT"), 
    Span(doc332, 13, 14, label="ARTICLE"), 
    Span(doc332, 14, 15, label="PRICE"), 
    Span(doc332, 15, 16, label="UNIT"), 
    Span(doc332, 17, 18, label="SUM"), 
    Span(doc332, 51, 52, label="TARIFF"), 
    Span(doc332, 57, 58, label="COUNTRY")] 
docs.append(doc332)


doc333 = nlp('''Purchase order number: N SR-1-06 1897
35000 10 PC 1730000051 21,63 100 PC 2,16

O-Ring-37.69x3.53-B90

O-Ring NBR-37,69x3,53-SH90

packed per each item

Product description: seal

Export - Customs tariff no.: 40169300
Country of origin: China''')
#doc333SR-1-06 1897 35000 10 1730000051 21,63 100  40169300 China
print("doc333",doc333[5: 8], doc333[8: 9], doc333[10: 11], doc333[11: 12], doc333[13: 14], doc333[14:15], doc333[15:16] ,doc333[17:18], doc333[49: 50], doc333[55: 56]) 
doc333.ents = [Span(doc333, 5, 8, label="CONTRACT"), 
    Span(doc333, 8, 9, label="CONTRACT1"), 
    Span(doc333, 10, 11, label="POS"), 
    Span(doc333, 11, 12, label="AMOUNT"), 
    Span(doc333, 13, 14, label="ARTICLE"), 
    Span(doc333, 14, 15, label="PRICE"), 
    Span(doc333, 15, 16, label="UNIT"), 
    Span(doc333, 17, 18, label="SUM"), 
    Span(doc333, 49, 50, label="TARIFF"), 
    Span(doc333, 55, 56, label="COUNTRY")] 
docs.append(doc333)
doc_bin = DocBin(docs = docs[:250])
doc_bin.to_disk('./train.spacy')

doc_bin = DocBin(docs = docs[250:])
doc_bin.to_disk('./dev.spacy')