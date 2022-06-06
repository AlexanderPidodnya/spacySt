import json 
import spacy 
from spacy.matcher import Matcher 
from spacy.tokens import Span, DocBin 
docs = []
print("doc0, 77, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 100; AMOUNT 600; ARTICLE 1730002340; PRICE 2,24; UNIT 1; SUMMA 1.344,00; TARIFF 73181568; COUNTRY Taiwan; PR_SURCH 15,50; SURCHARGE 208,32; PR_ESURCH 3,50; ESURCHARGE 47,04; TOTAL 1.599,36; ")
doc0 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 100 600 PC 1730002340 2,24 1 PC 1.344,00 IS-1/2-1 3 UNCx3 -3/4-AB18.3-GR8-W1 IS-1/2-13x3#3/4UNC-AB18.3-GR8-W1 packed per each item Product description: screw Export - Customs tariff no.: 73181568 Country of origin: Taiwan Material Surcharge 15,50 % 208,32  Energy Surcharge 3,50 % 47,04 1.599,36''')
doc0.ents = [
   Span(doc0, 3, 4, label ="NORDER"),
   Span(doc0, 9, 12, label ="CONTRACT"),
   Span(doc0, 12, 13, label ="CONTRACT1"),
   Span(doc0, 15, 16, label ="POS"),
   Span(doc0, 16, 17, label ="AMOUNT"),
   Span(doc0, 18, 19, label ="ARTICLE"),
   Span(doc0, 19, 20, label ="PRICE"),
   Span(doc0, 20, 21, label ="UNIT"),
   Span(doc0, 22, 23, label ="SUMMA"),
   Span(doc0, 59, 60, label ="TARIFF"),
   Span(doc0, 64, 65, label ="COUNTRY"),
   Span(doc0, 67, 68, label ="PR_SURCH"),
   Span(doc0, 69, 70, label ="SURCHARGE"),
   Span(doc0, 73, 74, label ="PR_ESURCH"),
   Span(doc0, 75, 76, label ="ESURCHARGE"),
   Span(doc0, 76, 77, label ="TOTAL")]
docs.append(doc0)
print("doc1, 75, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 200; AMOUNT 6.250; ARTICLE 1130022786; PRICE 23,28; UNIT 100; SUMMA 1.455,00; TARIFF 73079980; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 165,87; PR_ESURCH 3,50; ESURCHARGE 50,93; TOTAL 1.671,80; ")
doc1 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 200 6.250 PC 1130022786 23,28 100 PC 1.455,00 LBBU-HUE-1/1D-PM-M8/U5/16-W3 LBBU-HUE 1/1D PM M8-U5/16 W3 packed per each item Product description: sleeve Export - Customs tariff no.: 73079980 Country of origin: Germany Material Surcharge 11,40 % 165,87 Energy Surcharge 3,50 % 50,93 1.671,80''')
doc1.ents = [
   Span(doc1, 3, 4, label ="NORDER"),
   Span(doc1, 9, 12, label ="CONTRACT"),
   Span(doc1, 12, 13, label ="CONTRACT1"),
   Span(doc1, 15, 16, label ="POS"),
   Span(doc1, 16, 17, label ="AMOUNT"),
   Span(doc1, 18, 19, label ="ARTICLE"),
   Span(doc1, 19, 20, label ="PRICE"),
   Span(doc1, 20, 21, label ="UNIT"),
   Span(doc1, 22, 23, label ="SUMMA"),
   Span(doc1, 58, 59, label ="TARIFF"),
   Span(doc1, 63, 64, label ="COUNTRY"),
   Span(doc1, 66, 67, label ="PR_SURCH"),
   Span(doc1, 68, 69, label ="SURCHARGE"),
   Span(doc1, 71, 72, label ="PR_ESURCH"),
   Span(doc1, 73, 74, label ="ESURCHARGE"),
   Span(doc1, 74, 75, label ="TOTAL")]
docs.append(doc1)
print("doc2, 77, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 300; AMOUNT 10.000; ARTICLE 1130022886; PRICE 23,28; UNIT 100; SUMMA 2.328,00; TARIFF 73079980; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 265,39; PR_ESURCH 3,50; ESURCHARGE 81,48; TOTAL 2.674; ")
doc2 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 300 10.000 PC 1130022886 23,28 100 PC 2.328,00 LBBU-HUE-1/1D-SP-M8/U5/16-W3 LBBU-HUE 1/1D SP M8-U5/16 W3 packed per each item Product description: sleeve Export - Customs tariff no.: 73079980 Country of origin: Germany Material Surcharge 11,40 % 265,39 Energy Surcharge 3,50 % 81,48 2.674 ,87''')
doc2.ents = [
   Span(doc2, 3, 4, label ="NORDER"),
   Span(doc2, 9, 12, label ="CONTRACT"),
   Span(doc2, 12, 13, label ="CONTRACT1"),
   Span(doc2, 15, 16, label ="POS"),
   Span(doc2, 16, 17, label ="AMOUNT"),
   Span(doc2, 18, 19, label ="ARTICLE"),
   Span(doc2, 19, 20, label ="PRICE"),
   Span(doc2, 20, 21, label ="UNIT"),
   Span(doc2, 22, 23, label ="SUMMA"),
   Span(doc2, 58, 59, label ="TARIFF"),
   Span(doc2, 63, 64, label ="COUNTRY"),
   Span(doc2, 66, 67, label ="PR_SURCH"),
   Span(doc2, 68, 69, label ="SURCHARGE"),
   Span(doc2, 71, 72, label ="PR_ESURCH"),
   Span(doc2, 73, 74, label ="ESURCHARGE"),
   Span(doc2, 74, 75, label ="TOTAL")]
docs.append(doc2)
print("doc3, 76, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 400; AMOUNT 500; ARTICLE 1130022787; PRICE 23,28; UNIT 100; SUMMA 116,40; TARIFF 73079980; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 13,27; PR_ESURCH 3,50; ESURCHARGE 4,07; TOTAL 133,74; ")
doc3 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 400 500 PC 1130022787 23,28 100 PC 116,40 LBBU-HUE-2/2D-PM-M8/U5/16-W3 LBBU-HUE 2/2D PM M8-U5/16 W3 packed per each item Product description: sleeve Export - Customs tariff no.: 73079980    Country of origin: Germany Material Surcharge 11,40 % 13,27 Energy Surcharge 3,50 % 4,07 133,74''')
doc3.ents = [
   Span(doc3, 3, 4, label ="NORDER"),
   Span(doc3, 9, 12, label ="CONTRACT"),
   Span(doc3, 12, 13, label ="CONTRACT1"),
   Span(doc3, 15, 16, label ="POS"),
   Span(doc3, 16, 17, label ="AMOUNT"),
   Span(doc3, 18, 19, label ="ARTICLE"),
   Span(doc3, 19, 20, label ="PRICE"),
   Span(doc3, 20, 21, label ="UNIT"),
   Span(doc3, 22, 23, label ="SUMMA"),
   Span(doc3, 58, 59, label ="TARIFF"),
   Span(doc3, 64, 65, label ="COUNTRY"),
   Span(doc3, 67, 68, label ="PR_SURCH"),
   Span(doc3, 69, 70, label ="SURCHARGE"),
   Span(doc3, 72, 73, label ="PR_ESURCH"),
   Span(doc3, 74, 75, label ="ESURCHARGE"),
   Span(doc3, 75, 76, label ="TOTAL")]
docs.append(doc3)
print("doc4, 76, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 500; AMOUNT 750; ARTICLE 1130024670; PRICE 35,34; UNIT 100; SUMMA 265,05; TARIFF 73079980; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 30,22; PR_ESURCH 3,50; ESURCHARGE 9,28; TOTAL 304,55; ")
doc4 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 500 750 PC 1130024670 35,34 100 PC 265,05 LBBU-HUE-3/3 D-PM-M8/U5/16-W3 LBBU-HUE 3/3D PM M8-U5/16 W3 packed per each item Product description: sleeve Export - Customs tariff no.: 73079980 Country of origin: Germany Material Surcharge 11,40 % 30,22 Energy Surcharge 3,50 % 9,28 304,55''')
doc4.ents = [
   Span(doc4, 3, 4, label ="NORDER"),
   Span(doc4, 9, 12, label ="CONTRACT"),
   Span(doc4, 12, 13, label ="CONTRACT1"),
   Span(doc4, 15, 16, label ="POS"),
   Span(doc4, 16, 17, label ="AMOUNT"),
   Span(doc4, 18, 19, label ="ARTICLE"),
   Span(doc4, 19, 20, label ="PRICE"),
   Span(doc4, 20, 21, label ="UNIT"),
   Span(doc4, 22, 23, label ="SUMMA"),
   Span(doc4, 59, 60, label ="TARIFF"),
   Span(doc4, 64, 65, label ="COUNTRY"),
   Span(doc4, 67, 68, label ="PR_SURCH"),
   Span(doc4, 69, 70, label ="SURCHARGE"),
   Span(doc4, 72, 73, label ="PR_ESURCH"),
   Span(doc4, 74, 75, label ="ESURCHARGE"),
   Span(doc4, 75, 76, label ="TOTAL")]
docs.append(doc4)
print("doc5, 76, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 600; AMOUNT 600; ARTICLE 1210026027; PRICE 3,86; UNIT 1; SUMMA 2.316,00; TARIFF 84818073; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 264,02; PR_ESURCH 3,50; ESURCHARGE 81,06; TOTAL 2.661; ")
doc5 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 600 600 PC 1210026027 (*) 3,86 1 PC 2.316,00 SMK-20-08L-B-K-W3 SMK20-08L-PK-C6F packed per each item Product description: coupling Export - Customs tariff no.: 84818073 Country of origin: Germany Material Surcharge 11,40 % 264,02 Energy Surcharge 3,50 % 81,06 2.661 ,08''')
doc5.ents = [
   Span(doc5, 3, 4, label ="NORDER"),
   Span(doc5, 9, 12, label ="CONTRACT"),
   Span(doc5, 12, 13, label ="CONTRACT1"),
   Span(doc5, 15, 16, label ="POS"),
   Span(doc5, 16, 17, label ="AMOUNT"),
   Span(doc5, 18, 19, label ="ARTICLE"),
   Span(doc5, 22, 23, label ="PRICE"),
   Span(doc5, 23, 24, label ="UNIT"),
   Span(doc5, 25, 26, label ="SUMMA"),
   Span(doc5, 57, 58, label ="TARIFF"),
   Span(doc5, 62, 63, label ="COUNTRY"),
   Span(doc5, 65, 66, label ="PR_SURCH"),
   Span(doc5, 67, 68, label ="SURCHARGE"),
   Span(doc5, 70, 71, label ="PR_ESURCH"),
   Span(doc5, 72, 73, label ="ESURCHARGE"),
   Span(doc5, 73, 74, label ="TOTAL")]
docs.append(doc5)
print("doc6, 76, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 700; AMOUNT 200; ARTICLE 1210026041; PRICE 4,72; UNIT 1; SUMMA 944,00; TARIFF 84818073; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 107,62; PR_ESURCH 3,50; ESURCHARGE 33,04; TOTAL 1.084,66; ")
doc6 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 700 200 PC 1210026041 (*) 4,72 1 PC 944,00 SMK-20-12L-B-K-W3 SMK20-1 2L-PK-C6F    packed per each item Product description: coupling Export - Customs tariff no.: 84818073 Country of origin: Germany Material Surcharge 11,40 % 107,62 Energy Surcharge 3,50 % 33,04 1.084,66''')
doc6.ents = [
   Span(doc6, 3, 4, label ="NORDER"),
   Span(doc6, 9, 12, label ="CONTRACT"),
   Span(doc6, 12, 13, label ="CONTRACT1"),
   Span(doc6, 15, 16, label ="POS"),
   Span(doc6, 16, 17, label ="AMOUNT"),
   Span(doc6, 18, 19, label ="ARTICLE"),
   Span(doc6, 22, 23, label ="PRICE"),
   Span(doc6, 23, 24, label ="UNIT"),
   Span(doc6, 25, 26, label ="SUMMA"),
   Span(doc6, 59, 60, label ="TARIFF"),
   Span(doc6, 64, 65, label ="COUNTRY"),
   Span(doc6, 67, 68, label ="PR_SURCH"),
   Span(doc6, 69, 70, label ="SURCHARGE"),
   Span(doc6, 72, 73, label ="PR_ESURCH"),
   Span(doc6, 74, 75, label ="ESURCHARGE"),
   Span(doc6, 75, 76, label ="TOTAL")]
docs.append(doc6)
print("doc7, 62, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 900; AMOUNT 125; ARTICLE 1130000261; PRICE 5,49; UNIT 100; SUMMA 6,86; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,78; PR_ESURCH 3,50; ESURCHARGE 0,24; TOTAL 7,88; ")
doc7 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 900 125 PC 1130000261 5,49 100 PC 6,86 DP-2-W3 DP 2 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 0,78 Energy Surcharge 3,50 % 0,24 7,88''')
doc7.ents = [
   Span(doc7, 3, 4, label ="NORDER"),
   Span(doc7, 9, 12, label ="CONTRACT"),
   Span(doc7, 12, 13, label ="CONTRACT1"),
   Span(doc7, 15, 16, label ="POS"),
   Span(doc7, 16, 17, label ="AMOUNT"),
   Span(doc7, 18, 19, label ="ARTICLE"),
   Span(doc7, 19, 20, label ="PRICE"),
   Span(doc7, 20, 21, label ="UNIT"),
   Span(doc7, 22, 23, label ="SUMMA"),
   Span(doc7, 45, 46, label ="TARIFF"),
   Span(doc7, 50, 51, label ="COUNTRY"),
   Span(doc7, 53, 54, label ="PR_SURCH"),
   Span(doc7, 55, 56, label ="SURCHARGE"),
   Span(doc7, 58, 59, label ="PR_ESURCH"),
   Span(doc7, 60, 61, label ="ESURCHARGE"),
   Span(doc7, 61, 62, label ="TOTAL")]
docs.append(doc7)
print("doc8, 62, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 1000; AMOUNT 100; ARTICLE 1130000264; PRICE 6,22; UNIT 100; SUMMA 6,22; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,71; PR_ESURCH 3,50; ESURCHARGE 0,22; TOTAL 7,15; ")
doc8 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 1000 100 PC 1130000264 6,22 100 PC 6,22 DP-3-W3 DP 3 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 0,71 Energy Surcharge 3,50 % 0,22 7,15''')
doc8.ents = [
   Span(doc8, 3, 4, label ="NORDER"),
   Span(doc8, 9, 12, label ="CONTRACT"),
   Span(doc8, 12, 13, label ="CONTRACT1"),
   Span(doc8, 15, 16, label ="POS"),
   Span(doc8, 16, 17, label ="AMOUNT"),
   Span(doc8, 18, 19, label ="ARTICLE"),
   Span(doc8, 19, 20, label ="PRICE"),
   Span(doc8, 20, 21, label ="UNIT"),
   Span(doc8, 22, 23, label ="SUMMA"),
   Span(doc8, 45, 46, label ="TARIFF"),
   Span(doc8, 50, 51, label ="COUNTRY"),
   Span(doc8, 53, 54, label ="PR_SURCH"),
   Span(doc8, 55, 56, label ="SURCHARGE"),
   Span(doc8, 58, 59, label ="PR_ESURCH"),
   Span(doc8, 60, 61, label ="ESURCHARGE"),
   Span(doc8, 61, 62, label ="TOTAL")]
docs.append(doc8)
print("doc9, 63, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 1100; AMOUNT 700; ARTICLE 1130000267; PRICE 7,25; UNIT 100; SUMMA 50,75; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 5,79; PR_ESURCH 3,50; ESURCHARGE 1,78; TOTAL 58,32; ")
doc9 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23**    1100 700 PC 1130000267 7,25 100 PC 50,75 DP-4-W3 DP 4 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 5,79 Energy Surcharge 3,50 % 1,78 58,32''')
doc9.ents = [
   Span(doc9, 3, 4, label ="NORDER"),
   Span(doc9, 9, 12, label ="CONTRACT"),
   Span(doc9, 12, 13, label ="CONTRACT1"),
   Span(doc9, 16, 17, label ="POS"),
   Span(doc9, 17, 18, label ="AMOUNT"),
   Span(doc9, 19, 20, label ="ARTICLE"),
   Span(doc9, 20, 21, label ="PRICE"),
   Span(doc9, 21, 22, label ="UNIT"),
   Span(doc9, 23, 24, label ="SUMMA"),
   Span(doc9, 46, 47, label ="TARIFF"),
   Span(doc9, 51, 52, label ="COUNTRY"),
   Span(doc9, 54, 55, label ="PR_SURCH"),
   Span(doc9, 56, 57, label ="SURCHARGE"),
   Span(doc9, 59, 60, label ="PR_ESURCH"),
   Span(doc9, 61, 62, label ="ESURCHARGE"),
   Span(doc9, 62, 63, label ="TOTAL")]
docs.append(doc9)
print("doc10, 62, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 1200; AMOUNT 1.000; ARTICLE 1130000273; PRICE 14,05; UNIT 100; SUMMA 140,50; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 16,02; PR_ESURCH 3,50; ESURCHARGE 4,92; TOTAL 161,44; ")
doc10 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 1200 1.000 PC 1130000273 14,05 100 PC 140,50 DP-6-W3 DP 6 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 16,02 Energy Surcharge 3,50 % 4,92 161,44''')
doc10.ents = [
   Span(doc10, 3, 4, label ="NORDER"),
   Span(doc10, 9, 12, label ="CONTRACT"),
   Span(doc10, 12, 13, label ="CONTRACT1"),
   Span(doc10, 15, 16, label ="POS"),
   Span(doc10, 16, 17, label ="AMOUNT"),
   Span(doc10, 18, 19, label ="ARTICLE"),
   Span(doc10, 19, 20, label ="PRICE"),
   Span(doc10, 20, 21, label ="UNIT"),
   Span(doc10, 22, 23, label ="SUMMA"),
   Span(doc10, 45, 46, label ="TARIFF"),
   Span(doc10, 50, 51, label ="COUNTRY"),
   Span(doc10, 53, 54, label ="PR_SURCH"),
   Span(doc10, 55, 56, label ="SURCHARGE"),
   Span(doc10, 58, 59, label ="PR_ESURCH"),
   Span(doc10, 60, 61, label ="ESURCHARGE"),
   Span(doc10, 61, 62, label ="TOTAL")]
docs.append(doc10)
print("doc11, 63, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 1300; AMOUNT 2.700; ARTICLE 1130001959; PRICE 5,12; UNIT 100; SUMMA 138,24; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 15,76; PR_ESURCH 3,50; ESURCHARGE 4,84; TOTAL 158,84; ")
doc11 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 1300 2.700 PC 1130001959 5,12 100 PC 138,24 DPL-2-W3 DPL 2 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 15,76 Energy Surcharge 3,50 % 4,84 158,84    ''')
doc11.ents = [
   Span(doc11, 3, 4, label ="NORDER"),
   Span(doc11, 9, 12, label ="CONTRACT"),
   Span(doc11, 12, 13, label ="CONTRACT1"),
   Span(doc11, 15, 16, label ="POS"),
   Span(doc11, 16, 17, label ="AMOUNT"),
   Span(doc11, 18, 19, label ="ARTICLE"),
   Span(doc11, 19, 20, label ="PRICE"),
   Span(doc11, 20, 21, label ="UNIT"),
   Span(doc11, 22, 23, label ="SUMMA"),
   Span(doc11, 45, 46, label ="TARIFF"),
   Span(doc11, 50, 51, label ="COUNTRY"),
   Span(doc11, 53, 54, label ="PR_SURCH"),
   Span(doc11, 55, 56, label ="SURCHARGE"),
   Span(doc11, 58, 59, label ="PR_ESURCH"),
   Span(doc11, 60, 61, label ="ESURCHARGE"),
   Span(doc11, 61, 62, label ="TOTAL")]
docs.append(doc11)
print("doc12, 62, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 1400; AMOUNT 300; ARTICLE 1130001960; PRICE 5,65; UNIT 100; SUMMA 16,95; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 1,93; PR_ESURCH 3,50; ESURCHARGE 0,59; TOTAL 19,47; ")
doc12 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 1400 300 PC 1130001960 5,65 100 PC 16,95 DPL-3-W3 DPL 3 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 1,93 Energy Surcharge 3,50 % 0,59 19,47''')
doc12.ents = [
   Span(doc12, 3, 4, label ="NORDER"),
   Span(doc12, 9, 12, label ="CONTRACT"),
   Span(doc12, 12, 13, label ="CONTRACT1"),
   Span(doc12, 15, 16, label ="POS"),
   Span(doc12, 16, 17, label ="AMOUNT"),
   Span(doc12, 18, 19, label ="ARTICLE"),
   Span(doc12, 19, 20, label ="PRICE"),
   Span(doc12, 20, 21, label ="UNIT"),
   Span(doc12, 22, 23, label ="SUMMA"),
   Span(doc12, 45, 46, label ="TARIFF"),
   Span(doc12, 50, 51, label ="COUNTRY"),
   Span(doc12, 53, 54, label ="PR_SURCH"),
   Span(doc12, 55, 56, label ="SURCHARGE"),
   Span(doc12, 58, 59, label ="PR_ESURCH"),
   Span(doc12, 60, 61, label ="ESURCHARGE"),
   Span(doc12, 61, 62, label ="TOTAL")]
docs.append(doc12)
print("doc13, 62, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 1500; AMOUNT 700; ARTICLE 1130001961; PRICE 6,49; UNIT 100; SUMMA 45,43; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 5,18; PR_ESURCH 3,50; ESURCHARGE 1,59; TOTAL 52,20; ")
doc13 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 1500 700 PC 1130001961 6,49 100 PC 45,43 DPL-4-W3 DPL 4 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 5,18 Energy Surcharge 3,50 % 1,59 52,20''')
doc13.ents = [
   Span(doc13, 3, 4, label ="NORDER"),
   Span(doc13, 9, 12, label ="CONTRACT"),
   Span(doc13, 12, 13, label ="CONTRACT1"),
   Span(doc13, 15, 16, label ="POS"),
   Span(doc13, 16, 17, label ="AMOUNT"),
   Span(doc13, 18, 19, label ="ARTICLE"),
   Span(doc13, 19, 20, label ="PRICE"),
   Span(doc13, 20, 21, label ="UNIT"),
   Span(doc13, 22, 23, label ="SUMMA"),
   Span(doc13, 45, 46, label ="TARIFF"),
   Span(doc13, 50, 51, label ="COUNTRY"),
   Span(doc13, 53, 54, label ="PR_SURCH"),
   Span(doc13, 55, 56, label ="SURCHARGE"),
   Span(doc13, 58, 59, label ="PR_ESURCH"),
   Span(doc13, 60, 61, label ="ESURCHARGE"),
   Span(doc13, 61, 62, label ="TOTAL")]
docs.append(doc13)
print("doc14, 64, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 1600; AMOUNT 50; ARTICLE 1130000764; PRICE 10,43; UNIT 100; SUMMA 5,22; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,60; PR_ESURCH 3,50; ESURCHARGE 0,18; TOTAL 6,00; ")
doc14 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 1600 50 PC 1130000764 10,43 100 PC 5,22 GD-2D-W3 GD 2 D W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 0,60   Energy Surcharge 3,50 % 0,18 6,00''')
doc14.ents = [
   Span(doc14, 3, 4, label ="NORDER"),
   Span(doc14, 9, 12, label ="CONTRACT"),
   Span(doc14, 12, 13, label ="CONTRACT1"),
   Span(doc14, 15, 16, label ="POS"),
   Span(doc14, 16, 17, label ="AMOUNT"),
   Span(doc14, 18, 19, label ="ARTICLE"),
   Span(doc14, 19, 20, label ="PRICE"),
   Span(doc14, 20, 21, label ="UNIT"),
   Span(doc14, 22, 23, label ="SUMMA"),
   Span(doc14, 46, 47, label ="TARIFF"),
   Span(doc14, 51, 52, label ="COUNTRY"),
   Span(doc14, 54, 55, label ="PR_SURCH"),
   Span(doc14, 56, 57, label ="SURCHARGE"),
   Span(doc14, 60, 61, label ="PR_ESURCH"),
   Span(doc14, 62, 63, label ="ESURCHARGE"),
   Span(doc14, 63, 64, label ="TOTAL")]
docs.append(doc14)
print("doc15, 63, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 1700; AMOUNT 50; ARTICLE 1130000765; PRICE 11,44; UNIT 100; SUMMA 5,72; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,65; PR_ESURCH 3,50; ESURCHARGE 0,20; TOTAL 6,57; ")
doc15 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 1700 50 PC 1130000765 11,44 100 PC 5,72 GD-3D-W3 GD 3 D W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 0,65 Energy Surcharge 3,50 % 0,20 6,57''')
doc15.ents = [
   Span(doc15, 3, 4, label ="NORDER"),
   Span(doc15, 9, 12, label ="CONTRACT"),
   Span(doc15, 12, 13, label ="CONTRACT1"),
   Span(doc15, 15, 16, label ="POS"),
   Span(doc15, 16, 17, label ="AMOUNT"),
   Span(doc15, 18, 19, label ="ARTICLE"),
   Span(doc15, 19, 20, label ="PRICE"),
   Span(doc15, 20, 21, label ="UNIT"),
   Span(doc15, 22, 23, label ="SUMMA"),
   Span(doc15, 46, 47, label ="TARIFF"),
   Span(doc15, 51, 52, label ="COUNTRY"),
   Span(doc15, 54, 55, label ="PR_SURCH"),
   Span(doc15, 56, 57, label ="SURCHARGE"),
   Span(doc15, 59, 60, label ="PR_ESURCH"),
   Span(doc15, 61, 62, label ="ESURCHARGE"),
   Span(doc15, 62, 63, label ="TOTAL")]
docs.append(doc15)
print("doc16, 63, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 1800; AMOUNT 400; ARTICLE 1130000766; PRICE 12,62; UNIT 100; SUMMA 50,48; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 5,75; PR_ESURCH 3,50; ESURCHARGE 1,77; TOTAL 58,00; ")
doc16 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 1800 400 PC 1130000766 12,62 100 PC 50,48 GD-4D-W3 GD 4 D W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 5,75 Energy Surcharge 3,50 % 1,77 58,00''')
doc16.ents = [
   Span(doc16, 3, 4, label ="NORDER"),
   Span(doc16, 9, 12, label ="CONTRACT"),
   Span(doc16, 12, 13, label ="CONTRACT1"),
   Span(doc16, 15, 16, label ="POS"),
   Span(doc16, 16, 17, label ="AMOUNT"),
   Span(doc16, 18, 19, label ="ARTICLE"),
   Span(doc16, 19, 20, label ="PRICE"),
   Span(doc16, 20, 21, label ="UNIT"),
   Span(doc16, 22, 23, label ="SUMMA"),
   Span(doc16, 46, 47, label ="TARIFF"),
   Span(doc16, 51, 52, label ="COUNTRY"),
   Span(doc16, 54, 55, label ="PR_SURCH"),
   Span(doc16, 56, 57, label ="SURCHARGE"),
   Span(doc16, 59, 60, label ="PR_ESURCH"),
   Span(doc16, 61, 62, label ="ESURCHARGE"),
   Span(doc16, 62, 63, label ="TOTAL")]
docs.append(doc16)
print("doc17, 64, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 1900; AMOUNT 1.000; ARTICLE 1130000767; PRICE 14,20; UNIT 100; SUMMA 142,00; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 16,19; PR_ESURCH 3,50; ESURCHARGE 4,97; TOTAL 163,16; ")
doc17 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 1900 1.000 PC 1130000767 14,20 100 PC 142,00 GD-5D-W3 GD 5 D W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098    Country of origin: Germany Material Surcharge 11,40 % 16,19 Energy Surcharge 3,50 % 4,97 163,16''')
doc17.ents = [
   Span(doc17, 3, 4, label ="NORDER"),
   Span(doc17, 9, 12, label ="CONTRACT"),
   Span(doc17, 12, 13, label ="CONTRACT1"),
   Span(doc17, 15, 16, label ="POS"),
   Span(doc17, 16, 17, label ="AMOUNT"),
   Span(doc17, 18, 19, label ="ARTICLE"),
   Span(doc17, 19, 20, label ="PRICE"),
   Span(doc17, 20, 21, label ="UNIT"),
   Span(doc17, 22, 23, label ="SUMMA"),
   Span(doc17, 46, 47, label ="TARIFF"),
   Span(doc17, 52, 53, label ="COUNTRY"),
   Span(doc17, 55, 56, label ="PR_SURCH"),
   Span(doc17, 57, 58, label ="SURCHARGE"),
   Span(doc17, 60, 61, label ="PR_ESURCH"),
   Span(doc17, 62, 63, label ="ESURCHARGE"),
   Span(doc17, 63, 64, label ="TOTAL")]
docs.append(doc17)
print("doc18, 78, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 2000; AMOUNT 12.800; ARTICLE 1130022187; PRICE 16,01; UNIT 100; SUMMA 2.049; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 233,62; PR_ESURCH 3,50; ESURCHARGE 71,72; TOTAL 2.354; ")
doc18 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 2000 12.800 PC 1130022187 16,01 100 PC 2.049 ,28 LBBU-DP-1 D-M8/U5/16-W3 LBBU-DP 1D M8-U5/16 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 233,62 Energy Surcharge 3,50 % 71,72 2.354 ,62''')
doc18.ents = [
   Span(doc18, 3, 4, label ="NORDER"),
   Span(doc18, 9, 12, label ="CONTRACT"),
   Span(doc18, 12, 13, label ="CONTRACT1"),
   Span(doc18, 15, 16, label ="POS"),
   Span(doc18, 16, 17, label ="AMOUNT"),
   Span(doc18, 18, 19, label ="ARTICLE"),
   Span(doc18, 19, 20, label ="PRICE"),
   Span(doc18, 20, 21, label ="UNIT"),
   Span(doc18, 22, 23, label ="SUMMA"),
   Span(doc18, 59, 60, label ="TARIFF"),
   Span(doc18, 64, 65, label ="COUNTRY"),
   Span(doc18, 67, 68, label ="PR_SURCH"),
   Span(doc18, 69, 70, label ="SURCHARGE"),
   Span(doc18, 72, 73, label ="PR_ESURCH"),
   Span(doc18, 74, 75, label ="ESURCHARGE"),
   Span(doc18, 75, 76, label ="TOTAL")]
docs.append(doc18)
print("doc19, 72, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 2100; AMOUNT 2.647; ARTICLE 1130022183; PRICE 13,82; UNIT 100; SUMMA 365,82; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 41,70; PR_ESURCH 3,50; ESURCHARGE 12,80; TOTAL 420,32; ")
doc19 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 2100 2.647 PC 1130022183 13,82 100 PC 365,82 LBBU-DP-1 -M8/U5/16-W3 LBBU-DP 1 M8-U5/16 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 41,70 Energy Surcharge 3,50 % 12,80 420,32''')
doc19.ents = [
   Span(doc19, 3, 4, label ="NORDER"),
   Span(doc19, 9, 12, label ="CONTRACT"),
   Span(doc19, 12, 13, label ="CONTRACT1"),
   Span(doc19, 15, 16, label ="POS"),
   Span(doc19, 16, 17, label ="AMOUNT"),
   Span(doc19, 18, 19, label ="ARTICLE"),
   Span(doc19, 19, 20, label ="PRICE"),
   Span(doc19, 20, 21, label ="UNIT"),
   Span(doc19, 22, 23, label ="SUMMA"),
   Span(doc19, 55, 56, label ="TARIFF"),
   Span(doc19, 60, 61, label ="COUNTRY"),
   Span(doc19, 63, 64, label ="PR_SURCH"),
   Span(doc19, 65, 66, label ="SURCHARGE"),
   Span(doc19, 68, 69, label ="PR_ESURCH"),
   Span(doc19, 70, 71, label ="ESURCHARGE"),
   Span(doc19, 71, 72, label ="TOTAL")]
docs.append(doc19)
print("doc20, 74, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 2200; AMOUNT 1.000; ARTICLE 1130022185; PRICE 14,54; UNIT 100; SUMMA 145,40; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 16,58; PR_ESURCH 3,50; ESURCHARGE 5,09; TOTAL 167,07; ")
doc20 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 2200 1.000 PC 1130022185 14,54 100 PC 145,40 LBBU-DP-2-M8/U5/16-W3 LBBU-DP 2 M8-U5/16 W3    packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 16,58 Energy Surcharge 3,50 % 5,09 167,07''')
doc20.ents = [
   Span(doc20, 3, 4, label ="NORDER"),
   Span(doc20, 9, 12, label ="CONTRACT"),
   Span(doc20, 12, 13, label ="CONTRACT1"),
   Span(doc20, 15, 16, label ="POS"),
   Span(doc20, 16, 17, label ="AMOUNT"),
   Span(doc20, 18, 19, label ="ARTICLE"),
   Span(doc20, 19, 20, label ="PRICE"),
   Span(doc20, 20, 21, label ="UNIT"),
   Span(doc20, 22, 23, label ="SUMMA"),
   Span(doc20, 57, 58, label ="TARIFF"),
   Span(doc20, 62, 63, label ="COUNTRY"),
   Span(doc20, 65, 66, label ="PR_SURCH"),
   Span(doc20, 67, 68, label ="SURCHARGE"),
   Span(doc20, 70, 71, label ="PR_ESURCH"),
   Span(doc20, 72, 73, label ="ESURCHARGE"),
   Span(doc20, 73, 74, label ="TOTAL")]
docs.append(doc20)
print("doc21, 73, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 2300; AMOUNT 500; ARTICLE 1130024605; PRICE 46,52; UNIT 100; SUMMA 232,60; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 26,52; PR_ESURCH 3,50; ESURCHARGE 8,14; TOTAL 267,26; ")
doc21 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 2300 500 PC 1130024605 46,52 100 PC 232,60 LBBU-DP-3D-M8/U5/16-W3 LBBU-DP 3D M8-U5/16 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 26,52 Energy Surcharge 3,50 % 8,14 267,26''')
doc21.ents = [
   Span(doc21, 3, 4, label ="NORDER"),
   Span(doc21, 9, 12, label ="CONTRACT"),
   Span(doc21, 12, 13, label ="CONTRACT1"),
   Span(doc21, 15, 16, label ="POS"),
   Span(doc21, 16, 17, label ="AMOUNT"),
   Span(doc21, 18, 19, label ="ARTICLE"),
   Span(doc21, 19, 20, label ="PRICE"),
   Span(doc21, 20, 21, label ="UNIT"),
   Span(doc21, 22, 23, label ="SUMMA"),
   Span(doc21, 56, 57, label ="TARIFF"),
   Span(doc21, 61, 62, label ="COUNTRY"),
   Span(doc21, 64, 65, label ="PR_SURCH"),
   Span(doc21, 66, 67, label ="SURCHARGE"),
   Span(doc21, 69, 70, label ="PR_ESURCH"),
   Span(doc21, 71, 72, label ="ESURCHARGE"),
   Span(doc21, 72, 73, label ="TOTAL")]
docs.append(doc21)
print("doc22, 67, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 2400; AMOUNT 50; ARTICLE 1120001286; PRICE 70,88; UNIT 100; SUMMA 35,44; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 4,04; PR_ESURCH 3,50; ESURCHARGE 1,24; TOTAL 40,72; ")
doc22 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 2400 50 PC 1120001286 70,88 100 PC 35,44 DSP-5-75-M-W2 DSP 5/75 M W2 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 4,04 Energy Surcharge 3,50 % 1,24 40,72''')
doc22.ents = [
   Span(doc22, 3, 4, label ="NORDER"),
   Span(doc22, 9, 12, label ="CONTRACT"),
   Span(doc22, 12, 13, label ="CONTRACT1"),
   Span(doc22, 15, 16, label ="POS"),
   Span(doc22, 16, 17, label ="AMOUNT"),
   Span(doc22, 18, 19, label ="ARTICLE"),
   Span(doc22, 19, 20, label ="PRICE"),
   Span(doc22, 20, 21, label ="UNIT"),
   Span(doc22, 22, 23, label ="SUMMA"),
   Span(doc22, 50, 51, label ="TARIFF"),
   Span(doc22, 55, 56, label ="COUNTRY"),
   Span(doc22, 58, 59, label ="PR_SURCH"),
   Span(doc22, 60, 61, label ="SURCHARGE"),
   Span(doc22, 63, 64, label ="PR_ESURCH"),
   Span(doc22, 65, 66, label ="ESURCHARGE"),
   Span(doc22, 66, 67, label ="TOTAL")]
docs.append(doc22)
print("doc23, 69, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 2700; AMOUNT 500; ARTICLE 1120021038; PRICE 26,79; UNIT 100; SUMMA 133,95; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 15,27; PR_ESURCH 3,50; ESURCHARGE 4,69; TOTAL 153,91; ")
doc23 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23**   2700 500 PC 1120021038 26,79 100 PC 133,95 LBBU-SP-2-M8 -W2 LBBU-SP 2 M8 W2 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 15,27 Energy Surcharge 3,50 % 4,69 153,91''')
doc23.ents = [
   Span(doc23, 3, 4, label ="NORDER"),
   Span(doc23, 9, 12, label ="CONTRACT"),
   Span(doc23, 12, 13, label ="CONTRACT1"),
   Span(doc23, 16, 17, label ="POS"),
   Span(doc23, 17, 18, label ="AMOUNT"),
   Span(doc23, 19, 20, label ="ARTICLE"),
   Span(doc23, 20, 21, label ="PRICE"),
   Span(doc23, 21, 22, label ="UNIT"),
   Span(doc23, 23, 24, label ="SUMMA"),
   Span(doc23, 52, 53, label ="TARIFF"),
   Span(doc23, 57, 58, label ="COUNTRY"),
   Span(doc23, 60, 61, label ="PR_SURCH"),
   Span(doc23, 62, 63, label ="SURCHARGE"),
   Span(doc23, 65, 66, label ="PR_ESURCH"),
   Span(doc23, 67, 68, label ="ESURCHARGE"),
   Span(doc23, 68, 69, label ="TOTAL")]
docs.append(doc23)
print("doc24, 69, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 2800; AMOUNT 50; ARTICLE 1120021657; PRICE 48,51; UNIT 100; SUMMA 24,26; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 2,177; PR_ESURCH 3,50; ESURCHARGE 0,85; TOTAL 27,88; ")
doc24 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 2800 50 PC 1120021657 48,51 100 PC 24,26 LBBU-SP-3D-M8-W2 LBBU-SP 3D M8 W2 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 2,177 Energy Surcharge 3,50 % 0,85 27,88''')
doc24.ents = [
   Span(doc24, 3, 4, label ="NORDER"),
   Span(doc24, 9, 12, label ="CONTRACT"),
   Span(doc24, 12, 13, label ="CONTRACT1"),
   Span(doc24, 15, 16, label ="POS"),
   Span(doc24, 16, 17, label ="AMOUNT"),
   Span(doc24, 18, 19, label ="ARTICLE"),
   Span(doc24, 19, 20, label ="PRICE"),
   Span(doc24, 20, 21, label ="UNIT"),
   Span(doc24, 22, 23, label ="SUMMA"),
   Span(doc24, 52, 53, label ="TARIFF"),
   Span(doc24, 57, 58, label ="COUNTRY"),
   Span(doc24, 60, 61, label ="PR_SURCH"),
   Span(doc24, 62, 63, label ="SURCHARGE"),
   Span(doc24, 65, 66, label ="PR_ESURCH"),
   Span(doc24, 67, 68, label ="ESURCHARGE"),
   Span(doc24, 68, 69, label ="TOTAL")]
docs.append(doc24)
print("doc25, 69, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 2900; AMOUNT 200; ARTICLE 1120021686; PRICE 38,85; UNIT 100; SUMMA 77,70; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 8,86; PR_ESURCH 3,50; ESURCHARGE 2,72; TOTAL 89,28; ")
doc25 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 2900 200 PC 1120021686 38,85 100 PC 77,70 LBBU-SP-3-M8 -W2 LBBU-SP 3 M8 W2 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 8,86 Energy Surcharge 3,50 % 2,72 89,28    ''')
doc25.ents = [
   Span(doc25, 3, 4, label ="NORDER"),
   Span(doc25, 9, 12, label ="CONTRACT"),
   Span(doc25, 12, 13, label ="CONTRACT1"),
   Span(doc25, 15, 16, label ="POS"),
   Span(doc25, 16, 17, label ="AMOUNT"),
   Span(doc25, 18, 19, label ="ARTICLE"),
   Span(doc25, 19, 20, label ="PRICE"),
   Span(doc25, 20, 21, label ="UNIT"),
   Span(doc25, 22, 23, label ="SUMMA"),
   Span(doc25, 51, 52, label ="TARIFF"),
   Span(doc25, 56, 57, label ="COUNTRY"),
   Span(doc25, 59, 60, label ="PR_SURCH"),
   Span(doc25, 61, 62, label ="SURCHARGE"),
   Span(doc25, 64, 65, label ="PR_ESURCH"),
   Span(doc25, 66, 67, label ="ESURCHARGE"),
   Span(doc25, 67, 68, label ="TOTAL")]
docs.append(doc25)
print("doc26, 65, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 3000; AMOUNT 75; ARTICLE 1120002537; PRICE 28,25; UNIT 100; SUMMA 21,19; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 2,42; PR_ESURCH 3,50; ESURCHARGE 0,74; TOTAL 24,35; ")
doc26 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 3000 75 PC 1120002537 28,25 100 PC 21,19 SP-2D-M-W2 SP 2 DM W2 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 2,42 Energy Surcharge 3,50 % 0,74 24,35''')
doc26.ents = [
   Span(doc26, 3, 4, label ="NORDER"),
   Span(doc26, 9, 12, label ="CONTRACT"),
   Span(doc26, 12, 13, label ="CONTRACT1"),
   Span(doc26, 15, 16, label ="POS"),
   Span(doc26, 16, 17, label ="AMOUNT"),
   Span(doc26, 18, 19, label ="ARTICLE"),
   Span(doc26, 19, 20, label ="PRICE"),
   Span(doc26, 20, 21, label ="UNIT"),
   Span(doc26, 22, 23, label ="SUMMA"),
   Span(doc26, 48, 49, label ="TARIFF"),
   Span(doc26, 53, 54, label ="COUNTRY"),
   Span(doc26, 56, 57, label ="PR_SURCH"),
   Span(doc26, 58, 59, label ="SURCHARGE"),
   Span(doc26, 61, 62, label ="PR_ESURCH"),
   Span(doc26, 63, 64, label ="ESURCHARGE"),
   Span(doc26, 64, 65, label ="TOTAL")]
docs.append(doc26)
print("doc27, 65, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 3100; AMOUNT 950; ARTICLE 1120002541; PRICE 33,32; UNIT 100; SUMMA 316,54; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 36,09; PR_ESURCH 3,50; ESURCHARGE 11,08; TOTAL 363,71; ")
doc27 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 3100 950 PC 1120002541 33,32 100 PC 316,54 SP-4D-M-W2 SP 4 DM W2 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 36,09 Energy Surcharge 3,50 % 11,08 363,71''')
doc27.ents = [
   Span(doc27, 3, 4, label ="NORDER"),
   Span(doc27, 9, 12, label ="CONTRACT"),
   Span(doc27, 12, 13, label ="CONTRACT1"),
   Span(doc27, 15, 16, label ="POS"),
   Span(doc27, 16, 17, label ="AMOUNT"),
   Span(doc27, 18, 19, label ="ARTICLE"),
   Span(doc27, 19, 20, label ="PRICE"),
   Span(doc27, 20, 21, label ="UNIT"),
   Span(doc27, 22, 23, label ="SUMMA"),
   Span(doc27, 48, 49, label ="TARIFF"),
   Span(doc27, 53, 54, label ="COUNTRY"),
   Span(doc27, 56, 57, label ="PR_SURCH"),
   Span(doc27, 58, 59, label ="SURCHARGE"),
   Span(doc27, 61, 62, label ="PR_ESURCH"),
   Span(doc27, 63, 64, label ="ESURCHARGE"),
   Span(doc27, 64, 65, label ="TOTAL")]
docs.append(doc27)
print("doc28, 66, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 3200; AMOUNT 1.400; ARTICLE 1120001167; PRICE 22,15; UNIT 100; SUMMA 310,10; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 35,35; PR_ESURCH 3,50; ESURCHARGE 10,85; TOTAL 356,30; ")
doc28 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 3200 1.400 PC 1120001167 22,15 100 PC 310,10 SP-4-M-W2 SP 4M W2 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 35,35   Energy Surcharge 3,50 % 10,85 356,30''')
doc28.ents = [
   Span(doc28, 3, 4, label ="NORDER"),
   Span(doc28, 9, 12, label ="CONTRACT"),
   Span(doc28, 12, 13, label ="CONTRACT1"),
   Span(doc28, 15, 16, label ="POS"),
   Span(doc28, 16, 17, label ="AMOUNT"),
   Span(doc28, 18, 19, label ="ARTICLE"),
   Span(doc28, 19, 20, label ="PRICE"),
   Span(doc28, 20, 21, label ="UNIT"),
   Span(doc28, 22, 23, label ="SUMMA"),
   Span(doc28, 48, 49, label ="TARIFF"),
   Span(doc28, 53, 54, label ="COUNTRY"),
   Span(doc28, 56, 57, label ="PR_SURCH"),
   Span(doc28, 58, 59, label ="SURCHARGE"),
   Span(doc28, 62, 63, label ="PR_ESURCH"),
   Span(doc28, 64, 65, label ="ESURCHARGE"),
   Span(doc28, 65, 66, label ="TOTAL")]
docs.append(doc28)
print("doc29, 65, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 3300; AMOUNT 450; ARTICLE 1120002543; PRICE 37,22; UNIT 100; SUMMA 167,49; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 19,09; PR_ESURCH 3,50; ESURCHARGE 5,86; TOTAL 192,44; ")
doc29 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 3300 450 PC 1120002543 37,22 100 PC 167,49 SP-5D-M-W2 SP 5 DM W2 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 19,09 Energy Surcharge 3,50 % 5,86 192,44''')
doc29.ents = [
   Span(doc29, 3, 4, label ="NORDER"),
   Span(doc29, 9, 12, label ="CONTRACT"),
   Span(doc29, 12, 13, label ="CONTRACT1"),
   Span(doc29, 15, 16, label ="POS"),
   Span(doc29, 16, 17, label ="AMOUNT"),
   Span(doc29, 18, 19, label ="ARTICLE"),
   Span(doc29, 19, 20, label ="PRICE"),
   Span(doc29, 20, 21, label ="UNIT"),
   Span(doc29, 22, 23, label ="SUMMA"),
   Span(doc29, 48, 49, label ="TARIFF"),
   Span(doc29, 53, 54, label ="COUNTRY"),
   Span(doc29, 56, 57, label ="PR_SURCH"),
   Span(doc29, 58, 59, label ="SURCHARGE"),
   Span(doc29, 61, 62, label ="PR_ESURCH"),
   Span(doc29, 63, 64, label ="ESURCHARGE"),
   Span(doc29, 64, 65, label ="TOTAL")]
docs.append(doc29)
print("doc30, 65, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 3400; AMOUNT 900; ARTICLE 1120001171; PRICE 23,05; UNIT 100; SUMMA 207,45; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 23,65; PR_ESURCH 3,50; ESURCHARGE 7,26; TOTAL 238,36; ")
doc30 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 3400 900 PC 1120001171 23,05 100 PC 207,45 SP-5-M-W2 SP 5 M W2 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 23,65 Energy Surcharge 3,50 % 7,26 238,36''')
doc30.ents = [
   Span(doc30, 3, 4, label ="NORDER"),
   Span(doc30, 9, 12, label ="CONTRACT"),
   Span(doc30, 12, 13, label ="CONTRACT1"),
   Span(doc30, 15, 16, label ="POS"),
   Span(doc30, 16, 17, label ="AMOUNT"),
   Span(doc30, 18, 19, label ="ARTICLE"),
   Span(doc30, 19, 20, label ="PRICE"),
   Span(doc30, 20, 21, label ="UNIT"),
   Span(doc30, 22, 23, label ="SUMMA"),
   Span(doc30, 48, 49, label ="TARIFF"),
   Span(doc30, 53, 54, label ="COUNTRY"),
   Span(doc30, 56, 57, label ="PR_SURCH"),
   Span(doc30, 58, 59, label ="SURCHARGE"),
   Span(doc30, 61, 62, label ="PR_ESURCH"),
   Span(doc30, 63, 64, label ="ESURCHARGE"),
   Span(doc30, 64, 65, label ="TOTAL")]
docs.append(doc30)
print("doc31, 66, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 3500; AMOUNT 1.000; ARTICLE 1120001175; PRICE 29,27; UNIT 100; SUMMA 292,70; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 33,37; PR_ESURCH 3,50; ESURCHARGE 10,24; TOTAL 336,31; ")
doc31 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 3500 1.000 PC 1120001175 29,27 100 PC 292,70 SP-6-M-W2 SP 6 M W2 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098    Country of origin: Germany Material Surcharge 11,40 % 33,37 Energy Surcharge 3,50 % 10,24 336,31''')
doc31.ents = [
   Span(doc31, 3, 4, label ="NORDER"),
   Span(doc31, 9, 12, label ="CONTRACT"),
   Span(doc31, 12, 13, label ="CONTRACT1"),
   Span(doc31, 15, 16, label ="POS"),
   Span(doc31, 16, 17, label ="AMOUNT"),
   Span(doc31, 18, 19, label ="ARTICLE"),
   Span(doc31, 19, 20, label ="PRICE"),
   Span(doc31, 20, 21, label ="UNIT"),
   Span(doc31, 22, 23, label ="SUMMA"),
   Span(doc31, 48, 49, label ="TARIFF"),
   Span(doc31, 54, 55, label ="COUNTRY"),
   Span(doc31, 57, 58, label ="PR_SURCH"),
   Span(doc31, 59, 60, label ="SURCHARGE"),
   Span(doc31, 62, 63, label ="PR_ESURCH"),
   Span(doc31, 64, 65, label ="ESURCHARGE"),
   Span(doc31, 65, 66, label ="TOTAL")]
docs.append(doc31)
print("doc32, 72, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 3600; AMOUNT 200; ARTICLE 1910000432; PRICE 4,07; UNIT 1; SUMMA 814,00; TARIFF 84213925; COUNTRY Italy; PR_SURCH 11,40; SURCHARGE 92,80; PR_ESURCH 3,50; ESURCHARGE 28,49; TOTAL 935,29; ")
doc32 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 3600 200 PC 1910000432 (*) 4,07 1 PC 814,00 SMBT-47-S-10-O-B04-O packed per each item Product description: filter breather Export - Customs tariff no.: 84213925 Country of origin: Italy Material Surcharge 11,40 % 92,80 Energy Surcharge 3,50 % 28,49 935,29 EAC - Eurasian Conformity''')
doc32.ents = [
   Span(doc32, 3, 4, label ="NORDER"),
   Span(doc32, 9, 12, label ="CONTRACT"),
   Span(doc32, 12, 13, label ="CONTRACT1"),
   Span(doc32, 15, 16, label ="POS"),
   Span(doc32, 16, 17, label ="AMOUNT"),
   Span(doc32, 18, 19, label ="ARTICLE"),
   Span(doc32, 22, 23, label ="PRICE"),
   Span(doc32, 23, 24, label ="UNIT"),
   Span(doc32, 25, 26, label ="SUMMA"),
   Span(doc32, 51, 52, label ="TARIFF"),
   Span(doc32, 56, 57, label ="COUNTRY"),
   Span(doc32, 59, 60, label ="PR_SURCH"),
   Span(doc32, 61, 62, label ="SURCHARGE"),
   Span(doc32, 64, 65, label ="PR_ESURCH"),
   Span(doc32, 66, 67, label ="ESURCHARGE"),
   Span(doc32, 67, 68, label ="TOTAL")]
docs.append(doc32)
print("doc33, 63, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 3700; AMOUNT 200; ARTICLE 1730002924; PRICE 25,96; UNIT 1; SUMMA 5.192,00; TARIFF 73079980; COUNTRY Italy; PR_SURCH 15,50; SURCHARGE 804,76; PR_ESURCH 3,50; ESURCHARGE 181,72; TOTAL 6.178,48; ")
doc33 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 3700 200 PC 1730002924 25,96 1 PC 5.192,00 BF-L-604-W66 BF-L-604 packed per each item Product description: flange Export - Customs tariff no.: 73079980 Country of origin: Italy Material Surcharge 15,50 % 804,76 Energy Surcharge 3,50 % 181,72 6.178,48''')
doc33.ents = [
   Span(doc33, 3, 4, label ="NORDER"),
   Span(doc33, 9, 12, label ="CONTRACT"),
   Span(doc33, 12, 13, label ="CONTRACT1"),
   Span(doc33, 15, 16, label ="POS"),
   Span(doc33, 16, 17, label ="AMOUNT"),
   Span(doc33, 18, 19, label ="ARTICLE"),
   Span(doc33, 19, 20, label ="PRICE"),
   Span(doc33, 20, 21, label ="UNIT"),
   Span(doc33, 22, 23, label ="SUMMA"),
   Span(doc33, 46, 47, label ="TARIFF"),
   Span(doc33, 51, 52, label ="COUNTRY"),
   Span(doc33, 54, 55, label ="PR_SURCH"),
   Span(doc33, 56, 57, label ="SURCHARGE"),
   Span(doc33, 59, 60, label ="PR_ESURCH"),
   Span(doc33, 61, 62, label ="ESURCHARGE"),
   Span(doc33, 62, 63, label ="TOTAL")]
docs.append(doc33)
print("doc34, 64, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 3800; AMOUNT 60; ARTICLE 6100026392; PRICE 18,22; UNIT 1; SUMMA 1.093,20; TARIFF 73079100; COUNTRY Italy; PR_SURCH 15,50; SURCHARGE 169,45; PR_ESURCH 3,50; ESURCHARGE 38,26; TOTAL 1.300,91; ")
doc34 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 3800 60 PC 6100026392 18,22 1 PC 1.093,20 BFX-305-35L-W66 BFX-305-L35    packed per each item Product description: flange Export - Customs tariff no.: 73079100 Country of origin: Italy Material Surcharge 15,50 % 169,45 Energy Surcharge 3,50 % 38,26 1.300,91''')
doc34.ents = [
   Span(doc34, 3, 4, label ="NORDER"),
   Span(doc34, 9, 12, label ="CONTRACT"),
   Span(doc34, 12, 13, label ="CONTRACT1"),
   Span(doc34, 15, 16, label ="POS"),
   Span(doc34, 16, 17, label ="AMOUNT"),
   Span(doc34, 18, 19, label ="ARTICLE"),
   Span(doc34, 19, 20, label ="PRICE"),
   Span(doc34, 20, 21, label ="UNIT"),
   Span(doc34, 22, 23, label ="SUMMA"),
   Span(doc34, 47, 48, label ="TARIFF"),
   Span(doc34, 52, 53, label ="COUNTRY"),
   Span(doc34, 55, 56, label ="PR_SURCH"),
   Span(doc34, 57, 58, label ="SURCHARGE"),
   Span(doc34, 60, 61, label ="PR_ESURCH"),
   Span(doc34, 62, 63, label ="ESURCHARGE"),
   Span(doc34, 63, 64, label ="TOTAL")]
docs.append(doc34)
print("doc35, 63, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 3900; AMOUNT 100; ARTICLE 1730000192; PRICE 7,73; UNIT 1; SUMMA 773,00; TARIFF 73079910; COUNTRY Lithuania; PR_SURCH 15,50; SURCHARGE 119,82; PR_ESURCH 3,50; ESURCHARGE 27,06; TOTAL 919,88; ")
doc35 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 3900 100 PC 1730000192 7,73 1 PC 773,00 CAG-604-30S-W66 CAG-604-S30 packed per each item Product description: flange Export - Customs tariff no.: 73079910 Country of origin: Lithuania Material Surcharge 15,50 % 119,82 Energy Surcharge 3,50 % 27,06 919,88''')
doc35.ents = [
   Span(doc35, 3, 4, label ="NORDER"),
   Span(doc35, 9, 12, label ="CONTRACT"),
   Span(doc35, 12, 13, label ="CONTRACT1"),
   Span(doc35, 15, 16, label ="POS"),
   Span(doc35, 16, 17, label ="AMOUNT"),
   Span(doc35, 18, 19, label ="ARTICLE"),
   Span(doc35, 19, 20, label ="PRICE"),
   Span(doc35, 20, 21, label ="UNIT"),
   Span(doc35, 22, 23, label ="SUMMA"),
   Span(doc35, 46, 47, label ="TARIFF"),
   Span(doc35, 51, 52, label ="COUNTRY"),
   Span(doc35, 54, 55, label ="PR_SURCH"),
   Span(doc35, 56, 57, label ="SURCHARGE"),
   Span(doc35, 59, 60, label ="PR_ESURCH"),
   Span(doc35, 61, 62, label ="ESURCHARGE"),
   Span(doc35, 62, 63, label ="TOTAL")]
docs.append(doc35)
print("doc36, 69, #NORDER 2399732; CONTRACT SR-1-06; CONTRACT1 23; POS 4100; AMOUNT 800; ARTICLE 1730000061; PRICE 2,17; UNIT 1; SUMMA 1.736,00; TARIFF 73079910; COUNTRY China; PR_SURCH 15,50; SURCHARGE 269,08; PR_ESURCH 3,50; ESURCHARGE 60,76; TOTAL 2.065,84; ")
doc36 = nlp('''Order number: 2399732 Purchase order number: N SR-1-06 23** 4100 800 PC 1730000061 2,17 1 PC 1.736,00 DB-603-U-W66 DB-603-U Qty/Unit PC = Pair packed per each item Product description: flange Export - Customs tariff no.: 73079910 Country of origin: China Material Surcharge 15,50 % 269,08 Energy Surcharge 3,50 % 60,76 2.065,84''')
doc36.ents = [
   Span(doc36, 3, 4, label ="NORDER"),
   Span(doc36, 9, 12, label ="CONTRACT"),
   Span(doc36, 12, 13, label ="CONTRACT1"),
   Span(doc36, 15, 16, label ="POS"),
   Span(doc36, 16, 17, label ="AMOUNT"),
   Span(doc36, 18, 19, label ="ARTICLE"),
   Span(doc36, 19, 20, label ="PRICE"),
   Span(doc36, 20, 21, label ="UNIT"),
   Span(doc36, 22, 23, label ="SUMMA"),
   Span(doc36, 52, 53, label ="TARIFF"),
   Span(doc36, 57, 58, label ="COUNTRY"),
   Span(doc36, 60, 61, label ="PR_SURCH"),
   Span(doc36, 62, 63, label ="SURCHARGE"),
   Span(doc36, 65, 66, label ="PR_ESURCH"),
   Span(doc36, 67, 68, label ="ESURCHARGE"),
   Span(doc36, 68, 69, label ="TOTAL")]
docs.append(doc36)
doc_bin = DocBin(docs = docs)
doc_bin.to_disk('./train1.spacy')