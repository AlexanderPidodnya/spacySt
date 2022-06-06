import json 
import spacy 
from spacy.matcher import Matcher 
from spacy.tokens import Span, DocBin 
docs = []
print("doc0, 77, #NORDER 2365434; CONTRACT SR-1-06; CONTRACT1 1637; POS 900; AMOUNT 15; ARTICLE 6020000541; PRICE 670,58; UNIT 100; SUMMA 100,59; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 6,94; PR_ESURCH 3,50; ESURCHARGE 3,52; TOTAL 111,05; ")
doc0 = nlp('''Order number: 2365434 Purchase order number: N SR-1-06 1637 900 15 PC 6020000541 (*) 670,58 100 PC 100,59 FI-GE-28LR1 -1/4-WD-B-W3 FI-GE-28LR1 1/4-WD-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 6,94  Energy Surcharge 3,50 % 3,52 111,05''')
doc0.ents = [
   Span(doc0, 3, 4, label ="NORDER"),
   Span(doc0, 9, 12, label ="CONTRACT"),
   Span(doc0, 12, 13, label ="CONTRACT1"),
   Span(doc0, 13, 14, label ="POS"),
   Span(doc0, 14, 15, label ="AMOUNT"),
   Span(doc0, 16, 17, label ="ARTICLE"),
   Span(doc0, 20, 21, label ="PRICE"),
   Span(doc0, 21, 22, label ="UNIT"),
   Span(doc0, 23, 24, label ="SUMMA"),
   Span(doc0, 59, 60, label ="TARIFF"),
   Span(doc0, 64, 65, label ="COUNTRY"),
   Span(doc0, 67, 68, label ="PR_SURCH"),
   Span(doc0, 69, 70, label ="SURCHARGE"),
   Span(doc0, 73, 74, label ="PR_ESURCH"),
   Span(doc0, 75, 76, label ="ESURCHARGE"),
   Span(doc0, 76, 77, label ="TOTAL")]
docs.append(doc0)
print("doc1, 78, #NORDER 2390558; CONTRACT SR-1-06; CONTRACT1 1910; POS 3100; AMOUNT 510; ARTICLE 6010003921; PRICE 371,39; UNIT 100; SUMMA 1.894,09; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 130,69; PR_ESURCH 3,50; ESURCHARGE 66,29; TOTAL 2.091,07; ")
doc1 = nlp('''Order number: 2390558 Purchase order number: N SR-1-06 1910** 3100 510 PC 6010003921 (*) 371,39 100 PC 1.894,09 FI-REDSD-3 5/28L-V-W3-DKO FI-REDSD-3 5/28L-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 130,69 Energy Surcharge 3,50 % 66,29 2.091,07''')
doc1.ents = [
   Span(doc1, 3, 4, label ="NORDER"),
   Span(doc1, 9, 12, label ="CONTRACT"),
   Span(doc1, 12, 13, label ="CONTRACT1"),
   Span(doc1, 15, 16, label ="POS"),
   Span(doc1, 16, 17, label ="AMOUNT"),
   Span(doc1, 18, 19, label ="ARTICLE"),
   Span(doc1, 22, 23, label ="PRICE"),
   Span(doc1, 23, 24, label ="UNIT"),
   Span(doc1, 25, 26, label ="SUMMA"),
   Span(doc1, 61, 62, label ="TARIFF"),
   Span(doc1, 66, 67, label ="COUNTRY"),
   Span(doc1, 69, 70, label ="PR_SURCH"),
   Span(doc1, 71, 72, label ="SURCHARGE"),
   Span(doc1, 74, 75, label ="PR_ESURCH"),
   Span(doc1, 76, 77, label ="ESURCHARGE"),
   Span(doc1, 77, 78, label ="TOTAL")]
docs.append(doc1)
print("doc2, 69, #NORDER 2390558; CONTRACT SR-1-06; CONTRACT1 1910; POS 6900; AMOUNT 600; ARTICLE 6020000529; PRICE 53,75; UNIT 100; SUMMA 322,50; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 22,25; PR_ESURCH 3,50; ESURCHARGE 11,29; TOTAL 356,04; ")
doc2 = nlp('''Order number: 2390558 Purchase order number: N SR-1-06 1910** 6900 600 PC 6020000529 (*) 53,75 100 PC 322,50 FI-GE-O8LR3/8-WD-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 22,25 Energy Surcharge 3,50 % 11,29 356,04''')
doc2.ents = [
   Span(doc2, 3, 4, label ="NORDER"),
   Span(doc2, 9, 12, label ="CONTRACT"),
   Span(doc2, 12, 13, label ="CONTRACT1"),
   Span(doc2, 15, 16, label ="POS"),
   Span(doc2, 16, 17, label ="AMOUNT"),
   Span(doc2, 18, 19, label ="ARTICLE"),
   Span(doc2, 22, 23, label ="PRICE"),
   Span(doc2, 23, 24, label ="UNIT"),
   Span(doc2, 25, 26, label ="SUMMA"),
   Span(doc2, 52, 53, label ="TARIFF"),
   Span(doc2, 57, 58, label ="COUNTRY"),
   Span(doc2, 60, 61, label ="PR_SURCH"),
   Span(doc2, 62, 63, label ="SURCHARGE"),
   Span(doc2, 65, 66, label ="PR_ESURCH"),
   Span(doc2, 67, 68, label ="ESURCHARGE"),
   Span(doc2, 68, 69, label ="TOTAL")]
docs.append(doc2)
print("doc3, 61, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 7200; AMOUNT 50; ARTICLE 6030003819; PRICE 114,28; UNIT 100; SUMMA 57,14; TARIFF 73079910; COUNTRY Germany   ; PR_SURCH 6,90; SURCHARGE 3,94; PR_ESURCH 3,50; ESURCHARGE 2,00; TOTAL 63,08; ")
doc3 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 7200 50 PC 6030003819 114,28 100 PC 57,14 FI-M-35L-W3 packed per each item Product description: nuts Export - Customs tariff no.: 73079910 Country of origin: Germany   Material Surcharge 6,90 % 3,94 Energy Surcharge 3,50 % 2,00 63,08''')
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
   Span(doc3, 43, 44, label ="TARIFF"),
   Span(doc3, 48, 50, label ="COUNTRY"),
   Span(doc3, 52, 53, label ="PR_SURCH"),
   Span(doc3, 54, 55, label ="SURCHARGE"),
   Span(doc3, 57, 58, label ="PR_ESURCH"),
   Span(doc3, 59, 60, label ="ESURCHARGE"),
   Span(doc3, 60, 61, label ="TOTAL")]
docs.append(doc3)
print("doc4, 63, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 7300; AMOUNT 75; ARTICLE 6030005626; PRICE 157,47; UNIT 100; SUMMA 118,10; TARIFF 73181699; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 8,15; PR_ESURCH 3,50; ESURCHARGE 4,13; TOTAL 130,38; ")
doc4 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 7300 75 PC 6030005626 (*) 157,47 100 PC 118,10 FI-SKM-35L-W3 packed per each item Product description: nuts Export - Customs tariff no.: 73181699 Country of origin: Germany Material Surcharge 6,90 % 8,15 Energy Surcharge 3,50 % 4,13 130,38''')
doc4.ents = [
   Span(doc4, 3, 4, label ="NORDER"),
   Span(doc4, 9, 12, label ="CONTRACT"),
   Span(doc4, 12, 13, label ="CONTRACT1"),
   Span(doc4, 15, 16, label ="POS"),
   Span(doc4, 16, 17, label ="AMOUNT"),
   Span(doc4, 18, 19, label ="ARTICLE"),
   Span(doc4, 22, 23, label ="PRICE"),
   Span(doc4, 23, 24, label ="UNIT"),
   Span(doc4, 25, 26, label ="SUMMA"),
   Span(doc4, 46, 47, label ="TARIFF"),
   Span(doc4, 51, 52, label ="COUNTRY"),
   Span(doc4, 54, 55, label ="PR_SURCH"),
   Span(doc4, 56, 57, label ="SURCHARGE"),
   Span(doc4, 59, 60, label ="PR_ESURCH"),
   Span(doc4, 61, 62, label ="ESURCHARGE"),
   Span(doc4, 62, 63, label ="TOTAL")]
docs.append(doc4)
print("doc5, 76, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 7400; AMOUNT 40; ARTICLE 6010004110; PRICE 39,04; UNIT 100; SUMMA 15,62; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 1,08; PR_ESURCH 3,50; ESURCHARGE 0,55; TOTAL 17,25; ")
doc5 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 7400 40 PC 6010004110 (*) 39,04 100 PC 15,62 FI-VD-12L-V-W3-M FI-VD-12L-B-W3-M packed per each item Product description: Plug Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 1,08 Energy Surcharge 3,50 % 0,55 17,25''')
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
   Span(doc5, 59, 60, label ="TARIFF"),
   Span(doc5, 64, 65, label ="COUNTRY"),
   Span(doc5, 67, 68, label ="PR_SURCH"),
   Span(doc5, 69, 70, label ="SURCHARGE"),
   Span(doc5, 72, 73, label ="PR_ESURCH"),
   Span(doc5, 74, 75, label ="ESURCHARGE"),
   Span(doc5, 75, 76, label ="TOTAL")]
docs.append(doc5)
print("doc6, 81, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 7500; AMOUNT 600; ARTICLE 6010001836; PRICE 15,74; UNIT 100; SUMMA 94,44; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 6,52; PR_ESURCH 3,50; ESURCHARGE 3,31; TOTAL 104,27; ")
doc6 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 7500 600 PC 6010001836 (*) 15,74 100 PC 94,44 FI-VS-M14x1.5-WD-B-W3 FI-VS-M14x1,5-WD-B-W3 packed per each item Product description: Plug Export - Customs tariff no.: 73079910    Country of origin: Germany Material Surcharge 6,90 % 6,52 Energy Surcharge 3,50 % 3,31 104,27''')
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
   Span(doc6, 63, 64, label ="TARIFF"),
   Span(doc6, 69, 70, label ="COUNTRY"),
   Span(doc6, 72, 73, label ="PR_SURCH"),
   Span(doc6, 74, 75, label ="SURCHARGE"),
   Span(doc6, 77, 78, label ="PR_ESURCH"),
   Span(doc6, 79, 80, label ="ESURCHARGE"),
   Span(doc6, 80, 81, label ="TOTAL")]
docs.append(doc6)
print("doc7, 76, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 7600; AMOUNT 400; ARTICLE 6010004241; PRICE 312,86; UNIT 100; SUMMA 1.251,44; TARIFF 84813091; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 86,35; PR_ESURCH 3,50; ESURCHARGE 43,80; TOTAL 1.381,59; ")
doc7 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 7600 400 PC 6010004241 (*) 312,86 100 PC 1.251,44 FI-RV-08L-W3-0.5 FI-RV-08L-W3-0,5 packed per each item Product description: valve Export - Customs tariff no.: 84813091 Country of origin: Germany Material Surcharge 6,90 % 86,35 Energy Surcharge 3,50 % 43,80 1.381,59 EAC - Eurasian Conformity''')
doc7.ents = [
   Span(doc7, 3, 4, label ="NORDER"),
   Span(doc7, 9, 12, label ="CONTRACT"),
   Span(doc7, 12, 13, label ="CONTRACT1"),
   Span(doc7, 15, 16, label ="POS"),
   Span(doc7, 16, 17, label ="AMOUNT"),
   Span(doc7, 18, 19, label ="ARTICLE"),
   Span(doc7, 22, 23, label ="PRICE"),
   Span(doc7, 23, 24, label ="UNIT"),
   Span(doc7, 25, 26, label ="SUMMA"),
   Span(doc7, 55, 56, label ="TARIFF"),
   Span(doc7, 60, 61, label ="COUNTRY"),
   Span(doc7, 63, 64, label ="PR_SURCH"),
   Span(doc7, 65, 66, label ="SURCHARGE"),
   Span(doc7, 68, 69, label ="PR_ESURCH"),
   Span(doc7, 70, 71, label ="ESURCHARGE"),
   Span(doc7, 71, 72, label ="TOTAL")]
docs.append(doc7)
print("doc8, 84, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 7700; AMOUNT 75; ARTICLE 6010004404; PRICE 551,22; UNIT 100; SUMMA 413,42; TARIFF 84813091; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 28,53; PR_ESURCH 3,50; ESURCHARGE 14,47; TOTAL 456,42; ")
doc8 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 7700 75 PC 6010004404 (*) 551,22 100 PC 413,42 FI-RVZ-12LM-WD-B-W3-0.2 FI-RVZ-12LM-WD-B-W3-0,2 packed per each item Product description: valve Export - Customs tariff no.: 84813091 Country of origin: Germany Material Surcharge 6,90 % 28,53 Energy Surcharge 3,50 % 14,47 456,42 EAC - Eurasian Conformity''')
doc8.ents = [
   Span(doc8, 3, 4, label ="NORDER"),
   Span(doc8, 9, 12, label ="CONTRACT"),
   Span(doc8, 12, 13, label ="CONTRACT1"),
   Span(doc8, 15, 16, label ="POS"),
   Span(doc8, 16, 17, label ="AMOUNT"),
   Span(doc8, 18, 19, label ="ARTICLE"),
   Span(doc8, 22, 23, label ="PRICE"),
   Span(doc8, 23, 24, label ="UNIT"),
   Span(doc8, 25, 26, label ="SUMMA"),
   Span(doc8, 63, 64, label ="TARIFF"),
   Span(doc8, 68, 69, label ="COUNTRY"),
   Span(doc8, 71, 72, label ="PR_SURCH"),
   Span(doc8, 73, 74, label ="SURCHARGE"),
   Span(doc8, 76, 77, label ="PR_ESURCH"),
   Span(doc8, 78, 79, label ="ESURCHARGE"),
   Span(doc8, 79, 80, label ="TOTAL")]
docs.append(doc8)
print("doc9, 64, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 7800; AMOUNT 2.500; ARTICLE 6030004271; PRICE 10,93; UNIT 100; SUMMA 273,25; TARIFF 73269098; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 18,85; PR_ESURCH 3,50; ESURCHARGE 9,56; TOTAL 301,66; ")
doc9 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 7800 2.500 PC 6030004271 (*) 10,93 100 PC 273,25    FI-DS-15L-W3 packed per each item Product description: ring Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 6,90 % 18,85 Energy Surcharge 3,50 % 9,56 301,66''')
doc9.ents = [
   Span(doc9, 3, 4, label ="NORDER"),
   Span(doc9, 9, 12, label ="CONTRACT"),
   Span(doc9, 12, 13, label ="CONTRACT1"),
   Span(doc9, 15, 16, label ="POS"),
   Span(doc9, 16, 17, label ="AMOUNT"),
   Span(doc9, 18, 19, label ="ARTICLE"),
   Span(doc9, 22, 23, label ="PRICE"),
   Span(doc9, 23, 24, label ="UNIT"),
   Span(doc9, 25, 26, label ="SUMMA"),
   Span(doc9, 47, 48, label ="TARIFF"),
   Span(doc9, 52, 53, label ="COUNTRY"),
   Span(doc9, 55, 56, label ="PR_SURCH"),
   Span(doc9, 57, 58, label ="SURCHARGE"),
   Span(doc9, 60, 61, label ="PR_ESURCH"),
   Span(doc9, 62, 63, label ="ESURCHARGE"),
   Span(doc9, 63, 64, label ="TOTAL")]
docs.append(doc9)
print("doc10, 64, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 7900; AMOUNT 3.000; ARTICLE 6030004272; PRICE 16,04; UNIT 100; SUMMA 481,20; TARIFF 73269098; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 33,20; PR_ESURCH 3,50; ESURCHARGE 16,84; TOTAL 531,24; ")
doc10 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 7900 3.000 PC 6030004272 (*) 16,04 100 PC 481,20 FI-DS-1 8L-W3 packed per each item Product description: ring Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 6,90 % 33,20 Energy Surcharge 3,50 % 16,84 531,24''')
doc10.ents = [
   Span(doc10, 3, 4, label ="NORDER"),
   Span(doc10, 9, 12, label ="CONTRACT"),
   Span(doc10, 12, 13, label ="CONTRACT1"),
   Span(doc10, 15, 16, label ="POS"),
   Span(doc10, 16, 17, label ="AMOUNT"),
   Span(doc10, 18, 19, label ="ARTICLE"),
   Span(doc10, 22, 23, label ="PRICE"),
   Span(doc10, 23, 24, label ="UNIT"),
   Span(doc10, 25, 26, label ="SUMMA"),
   Span(doc10, 47, 48, label ="TARIFF"),
   Span(doc10, 52, 53, label ="COUNTRY"),
   Span(doc10, 55, 56, label ="PR_SURCH"),
   Span(doc10, 57, 58, label ="SURCHARGE"),
   Span(doc10, 60, 61, label ="PR_ESURCH"),
   Span(doc10, 62, 63, label ="ESURCHARGE"),
   Span(doc10, 63, 64, label ="TOTAL")]
docs.append(doc10)
print("doc11, 63, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 8000; AMOUNT 5.500; ARTICLE 6030004273; PRICE 19,24; UNIT 100; SUMMA 1.058,20; TARIFF 73269098; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 73,02; PR_ESURCH 3,50; ESURCHARGE 37,04; TOTAL 1.168,26; ")
doc11 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 8000 5.500 PC 6030004273 (*) 19,24 100 PC 1.058,20 FI-DS-22L-W3 packed per each item Product description: ring Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 6,90 % 73,02 Energy Surcharge 3,50 % 37,04 1.168,26''')
doc11.ents = [
   Span(doc11, 3, 4, label ="NORDER"),
   Span(doc11, 9, 12, label ="CONTRACT"),
   Span(doc11, 12, 13, label ="CONTRACT1"),
   Span(doc11, 15, 16, label ="POS"),
   Span(doc11, 16, 17, label ="AMOUNT"),
   Span(doc11, 18, 19, label ="ARTICLE"),
   Span(doc11, 22, 23, label ="PRICE"),
   Span(doc11, 23, 24, label ="UNIT"),
   Span(doc11, 25, 26, label ="SUMMA"),
   Span(doc11, 46, 47, label ="TARIFF"),
   Span(doc11, 51, 52, label ="COUNTRY"),
   Span(doc11, 54, 55, label ="PR_SURCH"),
   Span(doc11, 56, 57, label ="SURCHARGE"),
   Span(doc11, 59, 60, label ="PR_ESURCH"),
   Span(doc11, 61, 62, label ="ESURCHARGE"),
   Span(doc11, 62, 63, label ="TOTAL")]
docs.append(doc11)
print("doc12, 64, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 8100; AMOUNT 400; ARTICLE 6030004274; PRICE 22,63; UNIT 100; SUMMA 90,52; TARIFF 73269098; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 6,25; PR_ESURCH 3,50; ESURCHARGE 3,17; TOTAL 99,94; ")
doc12 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 8100 400 PC 6030004274 (*) 22,63 100 PC 90,52    FI-DS-28L-W3 packed per each item Product description: ring Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 6,90 % 6,25 Energy Surcharge 3,50 % 3,17 99,94''')
doc12.ents = [
   Span(doc12, 3, 4, label ="NORDER"),
   Span(doc12, 9, 12, label ="CONTRACT"),
   Span(doc12, 12, 13, label ="CONTRACT1"),
   Span(doc12, 15, 16, label ="POS"),
   Span(doc12, 16, 17, label ="AMOUNT"),
   Span(doc12, 18, 19, label ="ARTICLE"),
   Span(doc12, 22, 23, label ="PRICE"),
   Span(doc12, 23, 24, label ="UNIT"),
   Span(doc12, 25, 26, label ="SUMMA"),
   Span(doc12, 47, 48, label ="TARIFF"),
   Span(doc12, 52, 53, label ="COUNTRY"),
   Span(doc12, 55, 56, label ="PR_SURCH"),
   Span(doc12, 57, 58, label ="SURCHARGE"),
   Span(doc12, 60, 61, label ="PR_ESURCH"),
   Span(doc12, 62, 63, label ="ESURCHARGE"),
   Span(doc12, 63, 64, label ="TOTAL")]
docs.append(doc12)
print("doc13, 78, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 8300; AMOUNT 200; ARTICLE 6010003903; PRICE 102,59; UNIT 100; SUMMA 205,18; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 14,16; PR_ESURCH 3,50; ESURCHARGE 7,18; TOTAL 226,52; ")
doc13 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 8300 200 PC 6010003903 (*) 102,59 100 PC 205,18 FI-REDSD-1 5/08L-V-W3-DKO FI-REDSD-1 5/08L-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 14,16 Energy Surcharge 3,50 % 7,18 226,52''')
doc13.ents = [
   Span(doc13, 3, 4, label ="NORDER"),
   Span(doc13, 9, 12, label ="CONTRACT"),
   Span(doc13, 12, 13, label ="CONTRACT1"),
   Span(doc13, 15, 16, label ="POS"),
   Span(doc13, 16, 17, label ="AMOUNT"),
   Span(doc13, 18, 19, label ="ARTICLE"),
   Span(doc13, 22, 23, label ="PRICE"),
   Span(doc13, 23, 24, label ="UNIT"),
   Span(doc13, 25, 26, label ="SUMMA"),
   Span(doc13, 61, 62, label ="TARIFF"),
   Span(doc13, 66, 67, label ="COUNTRY"),
   Span(doc13, 69, 70, label ="PR_SURCH"),
   Span(doc13, 71, 72, label ="SURCHARGE"),
   Span(doc13, 74, 75, label ="PR_ESURCH"),
   Span(doc13, 76, 77, label ="ESURCHARGE"),
   Span(doc13, 77, 78, label ="TOTAL")]
docs.append(doc13)
print("doc14, 76, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 8500; AMOUNT 100; ARTICLE 6010003969; PRICE 263,25; UNIT 100; SUMMA 263,25; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 18,16; PR_ESURCH 3,50; ESURCHARGE 9,21; TOTAL 290,62; ")
doc14 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 8500 100 PC 6010003969 (*) 263,25 100 PC 263,25 FI-REDSD-22/08L-V-W3-DKO FI-REDSD-22/08L-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 18,16 Energy Surcharge 3,50 % 9,21 290,62''')
doc14.ents = [
   Span(doc14, 3, 4, label ="NORDER"),
   Span(doc14, 9, 12, label ="CONTRACT"),
   Span(doc14, 12, 13, label ="CONTRACT1"),
   Span(doc14, 15, 16, label ="POS"),
   Span(doc14, 16, 17, label ="AMOUNT"),
   Span(doc14, 18, 19, label ="ARTICLE"),
   Span(doc14, 22, 23, label ="PRICE"),
   Span(doc14, 23, 24, label ="UNIT"),
   Span(doc14, 25, 26, label ="SUMMA"),
   Span(doc14, 59, 60, label ="TARIFF"),
   Span(doc14, 64, 65, label ="COUNTRY"),
   Span(doc14, 67, 68, label ="PR_SURCH"),
   Span(doc14, 69, 70, label ="SURCHARGE"),
   Span(doc14, 72, 73, label ="PR_ESURCH"),
   Span(doc14, 74, 75, label ="ESURCHARGE"),
   Span(doc14, 75, 76, label ="TOTAL")]
docs.append(doc14)
print("doc15, 77, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 8700; AMOUNT 600; ARTICLE 6010003913; PRICE 176,70; UNIT 100; SUMMA 1.060,20; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 73,15; PR_ESURCH 3,50; ESURCHARGE 37,11; TOTAL 1.170,46; ")
doc15 = nlp('''Order number: 2390568   Purchase order number: N SR-1-06 1911** 8700 600 PC 6010003913 (*) 176,70 100 PC 1.060,20 FI-REDSD-22/18L-V-W3-DKO FI-REDSD-22/18L-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 73,15 Energy Surcharge 3,50 % 37,11 1.170,46''')
doc15.ents = [
   Span(doc15, 3, 4, label ="NORDER"),
   Span(doc15, 10, 13, label ="CONTRACT"),
   Span(doc15, 13, 14, label ="CONTRACT1"),
   Span(doc15, 16, 17, label ="POS"),
   Span(doc15, 17, 18, label ="AMOUNT"),
   Span(doc15, 19, 20, label ="ARTICLE"),
   Span(doc15, 23, 24, label ="PRICE"),
   Span(doc15, 24, 25, label ="UNIT"),
   Span(doc15, 26, 27, label ="SUMMA"),
   Span(doc15, 60, 61, label ="TARIFF"),
   Span(doc15, 65, 66, label ="COUNTRY"),
   Span(doc15, 68, 69, label ="PR_SURCH"),
   Span(doc15, 70, 71, label ="SURCHARGE"),
   Span(doc15, 73, 74, label ="PR_ESURCH"),
   Span(doc15, 75, 76, label ="ESURCHARGE"),
   Span(doc15, 76, 77, label ="TOTAL")]
docs.append(doc15)
print("doc16, 76, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 8800; AMOUNT 150; ARTICLE 6010003956; PRICE 448,44; UNIT 100; SUMMA 672,66; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 46,41; PR_ESURCH 3,50; ESURCHARGE 23,54; TOTAL 742,61; ")
doc16 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 8800 150 PC 6010003956 (*) 448,44 100 PC 672,66 FI-REDSD-28/08L-V-W3-DKO FI-REDSD-28/08L-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 46,41 Energy Surcharge 3,50 % 23,54 742,61''')
doc16.ents = [
   Span(doc16, 3, 4, label ="NORDER"),
   Span(doc16, 9, 12, label ="CONTRACT"),
   Span(doc16, 12, 13, label ="CONTRACT1"),
   Span(doc16, 15, 16, label ="POS"),
   Span(doc16, 16, 17, label ="AMOUNT"),
   Span(doc16, 18, 19, label ="ARTICLE"),
   Span(doc16, 22, 23, label ="PRICE"),
   Span(doc16, 23, 24, label ="UNIT"),
   Span(doc16, 25, 26, label ="SUMMA"),
   Span(doc16, 59, 60, label ="TARIFF"),
   Span(doc16, 64, 65, label ="COUNTRY"),
   Span(doc16, 67, 68, label ="PR_SURCH"),
   Span(doc16, 69, 70, label ="SURCHARGE"),
   Span(doc16, 72, 73, label ="PR_ESURCH"),
   Span(doc16, 74, 75, label ="ESURCHARGE"),
   Span(doc16, 75, 76, label ="TOTAL")]
docs.append(doc16)
print("doc17, 77, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 8900; AMOUNT 105; ARTICLE 6010003914; PRICE 337,56; UNIT 100; SUMMA 354,44; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 24,46; PR_ESURCH 3,50; ESURCHARGE 12,41; TOTAL 391,31; ")
doc17 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 8900 105 PC 6010003914 (*) 337,56 100 PC 354,44 FI-REDSD-28/12L-V-W3-DKO FI-REDSD-28/12L-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 24,46 Energy Surcharge 3,50 % 12,41   391,31''')
doc17.ents = [
   Span(doc17, 3, 4, label ="NORDER"),
   Span(doc17, 9, 12, label ="CONTRACT"),
   Span(doc17, 12, 13, label ="CONTRACT1"),
   Span(doc17, 15, 16, label ="POS"),
   Span(doc17, 16, 17, label ="AMOUNT"),
   Span(doc17, 18, 19, label ="ARTICLE"),
   Span(doc17, 22, 23, label ="PRICE"),
   Span(doc17, 23, 24, label ="UNIT"),
   Span(doc17, 25, 26, label ="SUMMA"),
   Span(doc17, 59, 60, label ="TARIFF"),
   Span(doc17, 64, 65, label ="COUNTRY"),
   Span(doc17, 67, 68, label ="PR_SURCH"),
   Span(doc17, 69, 70, label ="SURCHARGE"),
   Span(doc17, 72, 73, label ="PR_ESURCH"),
   Span(doc17, 74, 75, label ="ESURCHARGE"),
   Span(doc17, 76, 77, label ="TOTAL")]
docs.append(doc17)
print("doc18, 78, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 9100; AMOUNT 480; ARTICLE 6010003921; PRICE 371,39; UNIT 100; SUMMA 1.782,67; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 123,00; PR_ESURCH 3,50; ESURCHARGE 62,39; TOTAL 1.968,06; ")
doc18 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 9100 480 PC 6010003921 (*) 371,39 100 PC 1.782,67 FI-REDSD-3 5/28L-V-W3-DKO FI-REDSD-3 5/28L-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 123,00 Energy Surcharge 3,50 % 62,39 1.968,06''')
doc18.ents = [
   Span(doc18, 3, 4, label ="NORDER"),
   Span(doc18, 9, 12, label ="CONTRACT"),
   Span(doc18, 12, 13, label ="CONTRACT1"),
   Span(doc18, 15, 16, label ="POS"),
   Span(doc18, 16, 17, label ="AMOUNT"),
   Span(doc18, 18, 19, label ="ARTICLE"),
   Span(doc18, 22, 23, label ="PRICE"),
   Span(doc18, 23, 24, label ="UNIT"),
   Span(doc18, 25, 26, label ="SUMMA"),
   Span(doc18, 61, 62, label ="TARIFF"),
   Span(doc18, 66, 67, label ="COUNTRY"),
   Span(doc18, 69, 70, label ="PR_SURCH"),
   Span(doc18, 71, 72, label ="SURCHARGE"),
   Span(doc18, 74, 75, label ="PR_ESURCH"),
   Span(doc18, 76, 77, label ="ESURCHARGE"),
   Span(doc18, 77, 78, label ="TOTAL")]
docs.append(doc18)
print("doc19, 80, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 9300; AMOUNT 300; ARTICLE 6010013612; PRICE 164,64; UNIT 100; SUMMA 493,92; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 34,08; PR_ESURCH 3,50; ESURCHARGE 17,29; TOTAL 545,29; ")
doc19 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 9300 300 PC 6010013612 (*) 164,64 100 PC 493,92 FI-EGED-08LM-OR-BV-W3-DKO FI-EGED-08LM-OR-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 34,08 Energy Surcharge 3,50 % 17,29 545,29''')
doc19.ents = [
   Span(doc19, 3, 4, label ="NORDER"),
   Span(doc19, 9, 12, label ="CONTRACT"),
   Span(doc19, 12, 13, label ="CONTRACT1"),
   Span(doc19, 15, 16, label ="POS"),
   Span(doc19, 16, 17, label ="AMOUNT"),
   Span(doc19, 18, 19, label ="ARTICLE"),
   Span(doc19, 22, 23, label ="PRICE"),
   Span(doc19, 23, 24, label ="UNIT"),
   Span(doc19, 25, 26, label ="SUMMA"),
   Span(doc19, 63, 64, label ="TARIFF"),
   Span(doc19, 68, 69, label ="COUNTRY"),
   Span(doc19, 71, 72, label ="PR_SURCH"),
   Span(doc19, 73, 74, label ="SURCHARGE"),
   Span(doc19, 76, 77, label ="PR_ESURCH"),
   Span(doc19, 78, 79, label ="ESURCHARGE"),
   Span(doc19, 79, 80, label ="TOTAL")]
docs.append(doc19)
print("doc20, 82, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 9400; AMOUNT 600; ARTICLE 6010003835; PRICE 108,24; UNIT 100; SUMMA 649,44; TARIFF 73079910; COUNTRY Germany   ; PR_SURCH 6,90; SURCHARGE 44,81; PR_ESURCH 3,50; ESURCHARGE 22,73; TOTAL 716,98; ")
doc20 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 9400 600 PC 6010003835 (*) 108,24 100 PC 649,44 FI-EGED-0 8LR-WD-BV-W3-DKO FI-EGED-08LR-WD-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany   Material Surcharge 6,90 % 44,81 Energy Surcharge 3,50 % 22,73 716,98''')
doc20.ents = [
   Span(doc20, 3, 4, label ="NORDER"),
   Span(doc20, 9, 12, label ="CONTRACT"),
   Span(doc20, 12, 13, label ="CONTRACT1"),
   Span(doc20, 15, 16, label ="POS"),
   Span(doc20, 16, 17, label ="AMOUNT"),
   Span(doc20, 18, 19, label ="ARTICLE"),
   Span(doc20, 22, 23, label ="PRICE"),
   Span(doc20, 23, 24, label ="UNIT"),
   Span(doc20, 25, 26, label ="SUMMA"),
   Span(doc20, 64, 65, label ="TARIFF"),
   Span(doc20, 69, 71, label ="COUNTRY"),
   Span(doc20, 73, 74, label ="PR_SURCH"),
   Span(doc20, 75, 76, label ="SURCHARGE"),
   Span(doc20, 78, 79, label ="PR_ESURCH"),
   Span(doc20, 80, 81, label ="ESURCHARGE"),
   Span(doc20, 81, 82, label ="TOTAL")]
docs.append(doc20)
print("doc21, 82, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 9700; AMOUNT 100; ARTICLE 6010003807; PRICE 159,53; UNIT 100; SUMMA 159,53; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 11,01; PR_ESURCH 3,50; ESURCHARGE 5,58; TOTAL 176,12; ")
doc21 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 9700 100 PC 6010003807 (*) 159,53 100 PC 159,53 FI-EGED-1 5LM-WD-BV-W3-DKO FI-EGED-1 5LM-WD-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 11,01 Energy Surcharge 3,50 % 5,58 176,12''')
doc21.ents = [
   Span(doc21, 3, 4, label ="NORDER"),
   Span(doc21, 9, 12, label ="CONTRACT"),
   Span(doc21, 12, 13, label ="CONTRACT1"),
   Span(doc21, 15, 16, label ="POS"),
   Span(doc21, 16, 17, label ="AMOUNT"),
   Span(doc21, 18, 19, label ="ARTICLE"),
   Span(doc21, 22, 23, label ="PRICE"),
   Span(doc21, 23, 24, label ="UNIT"),
   Span(doc21, 25, 26, label ="SUMMA"),
   Span(doc21, 65, 66, label ="TARIFF"),
   Span(doc21, 70, 71, label ="COUNTRY"),
   Span(doc21, 73, 74, label ="PR_SURCH"),
   Span(doc21, 75, 76, label ="SURCHARGE"),
   Span(doc21, 78, 79, label ="PR_ESURCH"),
   Span(doc21, 80, 81, label ="ESURCHARGE"),
   Span(doc21, 81, 82, label ="TOTAL")]
docs.append(doc21)
print("doc22, 81, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 9800; AMOUNT 120; ARTICLE 6010013616; PRICE 229,31; UNIT 100; SUMMA 275,17; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 18,99; PR_ESURCH 3,50; ESURCHARGE 9,63; TOTAL 303,79; ")
doc22 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 9800 120 PC 6010013616 (*) 229,31 100 PC 275,17 FI-EGED-18LM-OR-BV-W3-DKO FI-EGED-1 8LM-OR-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 18,99 Energy Surcharge 3,50 % 9,63 303,79''')
doc22.ents = [
   Span(doc22, 3, 4, label ="NORDER"),
   Span(doc22, 9, 12, label ="CONTRACT"),
   Span(doc22, 12, 13, label ="CONTRACT1"),
   Span(doc22, 15, 16, label ="POS"),
   Span(doc22, 16, 17, label ="AMOUNT"),
   Span(doc22, 18, 19, label ="ARTICLE"),
   Span(doc22, 22, 23, label ="PRICE"),
   Span(doc22, 23, 24, label ="UNIT"),
   Span(doc22, 25, 26, label ="SUMMA"),
   Span(doc22, 64, 65, label ="TARIFF"),
   Span(doc22, 69, 70, label ="COUNTRY"),
   Span(doc22, 72, 73, label ="PR_SURCH"),
   Span(doc22, 74, 75, label ="SURCHARGE"),
   Span(doc22, 77, 78, label ="PR_ESURCH"),
   Span(doc22, 79, 80, label ="ESURCHARGE"),
   Span(doc22, 80, 81, label ="TOTAL")]
docs.append(doc22)
print("doc23, 82, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 9900; AMOUNT 300; ARTICLE 6010003843; PRICE 91,14; UNIT 100; SUMMA 273,42; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 18,87; PR_ESURCH 3,50; ESURCHARGE 9,57; TOTAL 301,86; ")
doc23 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 9900 300 PC 6010003843 (*) 91,14 100 PC 273,42 FI-EGED-1 8LR-WD-BV-W3-DKO FI-EGED-18LR-WD-B-W3-DKO packed per each item Product description: fitting    Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 18,87 Energy Surcharge 3,50 % 9,57 301,86''')
doc23.ents = [
   Span(doc23, 3, 4, label ="NORDER"),
   Span(doc23, 9, 12, label ="CONTRACT"),
   Span(doc23, 12, 13, label ="CONTRACT1"),
   Span(doc23, 15, 16, label ="POS"),
   Span(doc23, 16, 17, label ="AMOUNT"),
   Span(doc23, 18, 19, label ="ARTICLE"),
   Span(doc23, 22, 23, label ="PRICE"),
   Span(doc23, 23, 24, label ="UNIT"),
   Span(doc23, 25, 26, label ="SUMMA"),
   Span(doc23, 65, 66, label ="TARIFF"),
   Span(doc23, 70, 71, label ="COUNTRY"),
   Span(doc23, 73, 74, label ="PR_SURCH"),
   Span(doc23, 75, 76, label ="SURCHARGE"),
   Span(doc23, 78, 79, label ="PR_ESURCH"),
   Span(doc23, 80, 81, label ="ESURCHARGE"),
   Span(doc23, 81, 82, label ="TOTAL")]
docs.append(doc23)
print("doc24, 82, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 10000; AMOUNT 600; ARTICLE 6010003812; PRICE 447,50; UNIT 100; SUMMA 2.685,00; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 185,27; PR_ESURCH 3,50; ESURCHARGE 93,98; TOTAL 2.964; ")
doc24 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 10000 600 PC 6010003812 (*) 447,50 100 PC 2.685,00 FI-EGED-28LM-WD-BV-W3-DKO FI-EGED-28LM-WD-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 185,27 Energy Surcharge 3,50 % 93,98 2.964 ,25''')
doc24.ents = [
   Span(doc24, 3, 4, label ="NORDER"),
   Span(doc24, 9, 12, label ="CONTRACT"),
   Span(doc24, 12, 13, label ="CONTRACT1"),
   Span(doc24, 15, 16, label ="POS"),
   Span(doc24, 16, 17, label ="AMOUNT"),
   Span(doc24, 18, 19, label ="ARTICLE"),
   Span(doc24, 22, 23, label ="PRICE"),
   Span(doc24, 23, 24, label ="UNIT"),
   Span(doc24, 25, 26, label ="SUMMA"),
   Span(doc24, 63, 64, label ="TARIFF"),
   Span(doc24, 68, 69, label ="COUNTRY"),
   Span(doc24, 71, 72, label ="PR_SURCH"),
   Span(doc24, 73, 74, label ="SURCHARGE"),
   Span(doc24, 76, 77, label ="PR_ESURCH"),
   Span(doc24, 78, 79, label ="ESURCHARGE"),
   Span(doc24, 79, 80, label ="TOTAL")]
docs.append(doc24)
print("doc25, 76, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 10100; AMOUNT 1.760; ARTICLE 6010003587; PRICE 175,69; UNIT 100; SUMMA 3.092,14; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 213,36; PR_ESURCH 3,50; ESURCHARGE 108,22; TOTAL 3.413,72; ")
doc25 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 10100 1.760 PC 6010003587 (*) 175,69 100 PC 3.092,14 FI-ETD-12L-V-W3-DKO FI-ETD-12L-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 213,36 Energy Surcharge 3,50 % 108,22 3.413,72''')
doc25.ents = [
   Span(doc25, 3, 4, label ="NORDER"),
   Span(doc25, 9, 12, label ="CONTRACT"),
   Span(doc25, 12, 13, label ="CONTRACT1"),
   Span(doc25, 15, 16, label ="POS"),
   Span(doc25, 16, 17, label ="AMOUNT"),
   Span(doc25, 18, 19, label ="ARTICLE"),
   Span(doc25, 22, 23, label ="PRICE"),
   Span(doc25, 23, 24, label ="UNIT"),
   Span(doc25, 25, 26, label ="SUMMA"),
   Span(doc25, 59, 60, label ="TARIFF"),
   Span(doc25, 64, 65, label ="COUNTRY"),
   Span(doc25, 67, 68, label ="PR_SURCH"),
   Span(doc25, 69, 70, label ="SURCHARGE"),
   Span(doc25, 72, 73, label ="PR_ESURCH"),
   Span(doc25, 74, 75, label ="ESURCHARGE"),
   Span(doc25, 75, 76, label ="TOTAL")]
docs.append(doc25)
print("doc26, 77, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 10200; AMOUNT 40; ARTICLE 6010003593; PRICE 308,52; UNIT 100; SUMMA 123,41; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 8,52; PR_ESURCH 3,50; ESURCHARGE 4,32; TOTAL 136,25; ")
doc26 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 10200 40 PC 6010003593 (*) 308,52 100 PC 123,41 FI-ETD-15L-V-W3-DKO    FI-ETD-15L-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 8,52 Energy Surcharge 3,50 % 4,32 136,25''')
doc26.ents = [
   Span(doc26, 3, 4, label ="NORDER"),
   Span(doc26, 9, 12, label ="CONTRACT"),
   Span(doc26, 12, 13, label ="CONTRACT1"),
   Span(doc26, 15, 16, label ="POS"),
   Span(doc26, 16, 17, label ="AMOUNT"),
   Span(doc26, 18, 19, label ="ARTICLE"),
   Span(doc26, 22, 23, label ="PRICE"),
   Span(doc26, 23, 24, label ="UNIT"),
   Span(doc26, 25, 26, label ="SUMMA"),
   Span(doc26, 60, 61, label ="TARIFF"),
   Span(doc26, 65, 66, label ="COUNTRY"),
   Span(doc26, 68, 69, label ="PR_SURCH"),
   Span(doc26, 70, 71, label ="SURCHARGE"),
   Span(doc26, 73, 74, label ="PR_ESURCH"),
   Span(doc26, 75, 76, label ="ESURCHARGE"),
   Span(doc26, 76, 77, label ="TOTAL")]
docs.append(doc26)
print("doc27, 78, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 10400; AMOUNT 660; ARTICLE 6010003605; PRICE 524,45; UNIT 100; SUMMA 3.461; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 238,83; PR_ESURCH 3,50; ESURCHARGE 121,15; TOTAL 3.821,35; ")
doc27 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 10400 660 PC 6010003605 (*) 524,45 100 PC 3.461 ,37 FI-ETD-22L-V-W3-DKO FI-ETD-22L-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 238,83 Energy Surcharge 3,50 % 121,15 3.821,35''')
doc27.ents = [
   Span(doc27, 3, 4, label ="NORDER"),
   Span(doc27, 9, 12, label ="CONTRACT"),
   Span(doc27, 12, 13, label ="CONTRACT1"),
   Span(doc27, 15, 16, label ="POS"),
   Span(doc27, 16, 17, label ="AMOUNT"),
   Span(doc27, 18, 19, label ="ARTICLE"),
   Span(doc27, 22, 23, label ="PRICE"),
   Span(doc27, 23, 24, label ="UNIT"),
   Span(doc27, 25, 26, label ="SUMMA"),
   Span(doc27, 61, 62, label ="TARIFF"),
   Span(doc27, 66, 67, label ="COUNTRY"),
   Span(doc27, 69, 70, label ="PR_SURCH"),
   Span(doc27, 71, 72, label ="SURCHARGE"),
   Span(doc27, 74, 75, label ="PR_ESURCH"),
   Span(doc27, 76, 77, label ="ESURCHARGE"),
   Span(doc27, 77, 78, label ="TOTAL")]
docs.append(doc27)
print("doc28, 65, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 10700; AMOUNT 140; ARTICLE 6010002010; PRICE 201,60; UNIT 100; SUMMA 282,24; TARIFF 73079290; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 19,47; PR_ESURCH 3,50; ESURCHARGE 9,88; TOTAL 311,59; ")
doc28 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 10700 140 PC 6010002010 (*) 201,60 100 PC 282,24 FI-EW-18L-W3-SV packed per each item Product description: fitting Export - Customs tariff no.: 73079290 Country of origin: Germany Material Surcharge 6,90 % 19,47 Energy Surcharge 3,50 % 9,88 311,59''')
doc28.ents = [
   Span(doc28, 3, 4, label ="NORDER"),
   Span(doc28, 9, 12, label ="CONTRACT"),
   Span(doc28, 12, 13, label ="CONTRACT1"),
   Span(doc28, 15, 16, label ="POS"),
   Span(doc28, 16, 17, label ="AMOUNT"),
   Span(doc28, 18, 19, label ="ARTICLE"),
   Span(doc28, 22, 23, label ="PRICE"),
   Span(doc28, 23, 24, label ="UNIT"),
   Span(doc28, 25, 26, label ="SUMMA"),
   Span(doc28, 48, 49, label ="TARIFF"),
   Span(doc28, 53, 54, label ="COUNTRY"),
   Span(doc28, 56, 57, label ="PR_SURCH"),
   Span(doc28, 58, 59, label ="SURCHARGE"),
   Span(doc28, 61, 62, label ="PR_ESURCH"),
   Span(doc28, 63, 64, label ="ESURCHARGE"),
   Span(doc28, 64, 65, label ="TOTAL")]
docs.append(doc28)
print("doc29, 77, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 10800; AMOUNT 100; ARTICLE 6010003464; PRICE 119,10; UNIT 100; SUMMA 119,10; TARIFF 73079290; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 8,22; PR_ESURCH 3,50; ESURCHARGE 4,17; TOTAL 131,49; ")
doc29 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911**   10800 100 PC 6010003464 (*) 119,10 100 PC 119,10 FI-EWD-10L-V-W3-DKO FI-EWD-10L-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079290 Country of origin: Germany Material Surcharge 6,90 % 8,22 Energy Surcharge 3,50 % 4,17 131,49''')
doc29.ents = [
   Span(doc29, 3, 4, label ="NORDER"),
   Span(doc29, 9, 12, label ="CONTRACT"),
   Span(doc29, 12, 13, label ="CONTRACT1"),
   Span(doc29, 16, 17, label ="POS"),
   Span(doc29, 17, 18, label ="AMOUNT"),
   Span(doc29, 19, 20, label ="ARTICLE"),
   Span(doc29, 23, 24, label ="PRICE"),
   Span(doc29, 24, 25, label ="UNIT"),
   Span(doc29, 26, 27, label ="SUMMA"),
   Span(doc29, 60, 61, label ="TARIFF"),
   Span(doc29, 65, 66, label ="COUNTRY"),
   Span(doc29, 68, 69, label ="PR_SURCH"),
   Span(doc29, 70, 71, label ="SURCHARGE"),
   Span(doc29, 73, 74, label ="PR_ESURCH"),
   Span(doc29, 75, 76, label ="ESURCHARGE"),
   Span(doc29, 76, 77, label ="TOTAL")]
docs.append(doc29)
print("doc30, 76, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 10900; AMOUNT 100; ARTICLE 6010003476; PRICE 196,12; UNIT 100; SUMMA 196,12; TARIFF 73079290; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 13,53; PR_ESURCH 3,50; ESURCHARGE 6,86; TOTAL 216,51; ")
doc30 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 10900 100 PC 6010003476 (*) 196,12 100 PC 196,12 FI-EWD-15L-V-W3-DKO FI-EWD-15L-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079290 Country of origin: Germany Material Surcharge 6,90 % 13,53 Energy Surcharge 3,50 % 6,86 216,51''')
doc30.ents = [
   Span(doc30, 3, 4, label ="NORDER"),
   Span(doc30, 9, 12, label ="CONTRACT"),
   Span(doc30, 12, 13, label ="CONTRACT1"),
   Span(doc30, 15, 16, label ="POS"),
   Span(doc30, 16, 17, label ="AMOUNT"),
   Span(doc30, 18, 19, label ="ARTICLE"),
   Span(doc30, 22, 23, label ="PRICE"),
   Span(doc30, 23, 24, label ="UNIT"),
   Span(doc30, 25, 26, label ="SUMMA"),
   Span(doc30, 59, 60, label ="TARIFF"),
   Span(doc30, 64, 65, label ="COUNTRY"),
   Span(doc30, 67, 68, label ="PR_SURCH"),
   Span(doc30, 69, 70, label ="SURCHARGE"),
   Span(doc30, 72, 73, label ="PR_ESURCH"),
   Span(doc30, 74, 75, label ="ESURCHARGE"),
   Span(doc30, 75, 76, label ="TOTAL")]
docs.append(doc30)
print("doc31, 79, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 11100; AMOUNT 2.505; ARTICLE 6010003494; PRICE 450,46; UNIT 100; SUMMA 11.284,02; TARIFF 73079290; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 778,60; PR_ESURCH 3,50; ESURCHARGE 394,94; TOTAL 12.457; ")
doc31 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 11100 2.505 PC 6010003494 (*) 450,46 100 PC 11.284,02 FI-EWD-28L-V-W3-DKO FI-EWD-28L-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079290 Country of origin: Germany Material Surcharge 6,90 % 778,60 Energy Surcharge 3,50 % 394,94 12.457 ,56   ''')
doc31.ents = [
   Span(doc31, 3, 4, label ="NORDER"),
   Span(doc31, 9, 12, label ="CONTRACT"),
   Span(doc31, 12, 13, label ="CONTRACT1"),
   Span(doc31, 15, 16, label ="POS"),
   Span(doc31, 16, 17, label ="AMOUNT"),
   Span(doc31, 18, 19, label ="ARTICLE"),
   Span(doc31, 22, 23, label ="PRICE"),
   Span(doc31, 23, 24, label ="UNIT"),
   Span(doc31, 25, 26, label ="SUMMA"),
   Span(doc31, 59, 60, label ="TARIFF"),
   Span(doc31, 64, 65, label ="COUNTRY"),
   Span(doc31, 67, 68, label ="PR_SURCH"),
   Span(doc31, 69, 70, label ="SURCHARGE"),
   Span(doc31, 72, 73, label ="PR_ESURCH"),
   Span(doc31, 74, 75, label ="ESURCHARGE"),
   Span(doc31, 75, 76, label ="TOTAL")]
docs.append(doc31)
print("doc32, 63, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 11200; AMOUNT 555; ARTICLE 6030003246; PRICE 21,49; UNIT 100; SUMMA 119,27; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 8,23; PR_ESURCH 3,50; ESURCHARGE 4,17; TOTAL 131,67; ")
doc32 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 11200 555 PC 6030003246 (*) 21,49 100 PC 119,27 FI-G-08L-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 8,23 Energy Surcharge 3,50 % 4,17 131,67''')
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
   Span(doc32, 46, 47, label ="TARIFF"),
   Span(doc32, 51, 52, label ="COUNTRY"),
   Span(doc32, 54, 55, label ="PR_SURCH"),
   Span(doc32, 56, 57, label ="SURCHARGE"),
   Span(doc32, 59, 60, label ="PR_ESURCH"),
   Span(doc32, 61, 62, label ="ESURCHARGE"),
   Span(doc32, 62, 63, label ="TOTAL")]
docs.append(doc32)
print("doc33, 63, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 11300; AMOUNT 700; ARTICLE 6030003272; PRICE 35,43; UNIT 100; SUMMA 248,01; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 17,11; PR_ESURCH 3,50; ESURCHARGE 8,68; TOTAL 273,80; ")
doc33 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 11300 700 PC 6030003272 (*) 35,43 100 PC 248,01 FI-G-12/08L-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 17,11 Energy Surcharge 3,50 % 8,68 273,80''')
doc33.ents = [
   Span(doc33, 3, 4, label ="NORDER"),
   Span(doc33, 9, 12, label ="CONTRACT"),
   Span(doc33, 12, 13, label ="CONTRACT1"),
   Span(doc33, 15, 16, label ="POS"),
   Span(doc33, 16, 17, label ="AMOUNT"),
   Span(doc33, 18, 19, label ="ARTICLE"),
   Span(doc33, 22, 23, label ="PRICE"),
   Span(doc33, 23, 24, label ="UNIT"),
   Span(doc33, 25, 26, label ="SUMMA"),
   Span(doc33, 46, 47, label ="TARIFF"),
   Span(doc33, 51, 52, label ="COUNTRY"),
   Span(doc33, 54, 55, label ="PR_SURCH"),
   Span(doc33, 56, 57, label ="SURCHARGE"),
   Span(doc33, 59, 60, label ="PR_ESURCH"),
   Span(doc33, 61, 62, label ="ESURCHARGE"),
   Span(doc33, 62, 63, label ="TOTAL")]
docs.append(doc33)
print("doc34, 64, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 11500; AMOUNT 150; ARTICLE 6030003251; PRICE 88,25; UNIT 100; SUMMA 132,38; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 9,13; PR_ESURCH 3,50; ESURCHARGE 4,63; TOTAL 146,14; ")
doc34 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 11500 150 PC 6030003251 (*) 88,25 100 PC 132,38 FI-G-22L-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 9,13 Energy Surcharge 3,50 % 4,63 146,14   ''')
doc34.ents = [
   Span(doc34, 3, 4, label ="NORDER"),
   Span(doc34, 9, 12, label ="CONTRACT"),
   Span(doc34, 12, 13, label ="CONTRACT1"),
   Span(doc34, 15, 16, label ="POS"),
   Span(doc34, 16, 17, label ="AMOUNT"),
   Span(doc34, 18, 19, label ="ARTICLE"),
   Span(doc34, 22, 23, label ="PRICE"),
   Span(doc34, 23, 24, label ="UNIT"),
   Span(doc34, 25, 26, label ="SUMMA"),
   Span(doc34, 46, 47, label ="TARIFF"),
   Span(doc34, 51, 52, label ="COUNTRY"),
   Span(doc34, 54, 55, label ="PR_SURCH"),
   Span(doc34, 56, 57, label ="SURCHARGE"),
   Span(doc34, 59, 60, label ="PR_ESURCH"),
   Span(doc34, 61, 62, label ="ESURCHARGE"),
   Span(doc34, 62, 63, label ="TOTAL")]
docs.append(doc34)
print("doc35, 63, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 11600; AMOUNT 35; ARTICLE 6030003252; PRICE 172,93; UNIT 100; SUMMA 60,53; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 4,18; PR_ESURCH 3,50; ESURCHARGE 2,12; TOTAL 66,83; ")
doc35 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 11600 35 PC 6030003252 (*) 172,93 100 PC 60,53 FI-G-28L-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 4,18 Energy Surcharge 3,50 % 2,12 66,83''')
doc35.ents = [
   Span(doc35, 3, 4, label ="NORDER"),
   Span(doc35, 9, 12, label ="CONTRACT"),
   Span(doc35, 12, 13, label ="CONTRACT1"),
   Span(doc35, 15, 16, label ="POS"),
   Span(doc35, 16, 17, label ="AMOUNT"),
   Span(doc35, 18, 19, label ="ARTICLE"),
   Span(doc35, 22, 23, label ="PRICE"),
   Span(doc35, 23, 24, label ="UNIT"),
   Span(doc35, 25, 26, label ="SUMMA"),
   Span(doc35, 46, 47, label ="TARIFF"),
   Span(doc35, 51, 52, label ="COUNTRY"),
   Span(doc35, 54, 55, label ="PR_SURCH"),
   Span(doc35, 56, 57, label ="SURCHARGE"),
   Span(doc35, 59, 60, label ="PR_ESURCH"),
   Span(doc35, 61, 62, label ="ESURCHARGE"),
   Span(doc35, 62, 63, label ="TOTAL")]
docs.append(doc35)
print("doc36, 67, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 11700; AMOUNT 100; ARTICLE 6010000421; PRICE 48,47; UNIT 100; SUMMA 48,47; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 3,34; PR_ESURCH 3,50; ESURCHARGE 1,70; TOTAL 53,51; ")
doc36 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 11700 100 PC 6010000421 (*) 48,47 100 PC 48,47 FI-GE-O6LLM6x1k-W3-MS packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 3,34 Energy Surcharge 3,50 % 1,70 53,51''')
doc36.ents = [
   Span(doc36, 3, 4, label ="NORDER"),
   Span(doc36, 9, 12, label ="CONTRACT"),
   Span(doc36, 12, 13, label ="CONTRACT1"),
   Span(doc36, 15, 16, label ="POS"),
   Span(doc36, 16, 17, label ="AMOUNT"),
   Span(doc36, 18, 19, label ="ARTICLE"),
   Span(doc36, 22, 23, label ="PRICE"),
   Span(doc36, 23, 24, label ="UNIT"),
   Span(doc36, 25, 26, label ="SUMMA"),
   Span(doc36, 50, 51, label ="TARIFF"),
   Span(doc36, 55, 56, label ="COUNTRY"),
   Span(doc36, 58, 59, label ="PR_SURCH"),
   Span(doc36, 60, 61, label ="SURCHARGE"),
   Span(doc36, 63, 64, label ="PR_ESURCH"),
   Span(doc36, 65, 66, label ="ESURCHARGE"),
   Span(doc36, 66, 67, label ="TOTAL")]
docs.append(doc36)
print("doc37, 66, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 11800; AMOUNT 400; ARTICLE 6020000238; PRICE 36,58; UNIT 100; SUMMA 146,32; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 10,10; PR_ESURCH 3,50; ESURCHARGE 5,12; TOTAL 161,54; ")
doc37 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 11800 400 PC 6020000238 (*) 36,58 100 PC 146,32 FI-GE-08L7/16U-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 10,10 Energy Surcharge 3,50 % 5,12 161,54   ''')
doc37.ents = [
   Span(doc37, 3, 4, label ="NORDER"),
   Span(doc37, 9, 12, label ="CONTRACT"),
   Span(doc37, 12, 13, label ="CONTRACT1"),
   Span(doc37, 15, 16, label ="POS"),
   Span(doc37, 16, 17, label ="AMOUNT"),
   Span(doc37, 18, 19, label ="ARTICLE"),
   Span(doc37, 22, 23, label ="PRICE"),
   Span(doc37, 23, 24, label ="UNIT"),
   Span(doc37, 25, 26, label ="SUMMA"),
   Span(doc37, 48, 49, label ="TARIFF"),
   Span(doc37, 53, 54, label ="COUNTRY"),
   Span(doc37, 56, 57, label ="PR_SURCH"),
   Span(doc37, 58, 59, label ="SURCHARGE"),
   Span(doc37, 61, 62, label ="PR_ESURCH"),
   Span(doc37, 63, 64, label ="ESURCHARGE"),
   Span(doc37, 64, 65, label ="TOTAL")]
docs.append(doc37)
print("doc38, 69, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 11900; AMOUNT 4.800; ARTICLE 6020000640; PRICE 33,19; UNIT 100; SUMMA 1.593,12; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 109,93; PR_ESURCH 3,50; ESURCHARGE 55,76; TOTAL 1.758,81; ")
doc38 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 11900 4.800 PC 6020000640 (*) 33,19 100 PC 1.593,12 FI-GE-O8LM-OR-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 109,93 Energy Surcharge 3,50 % 55,76 1.758,81''')
doc38.ents = [
   Span(doc38, 3, 4, label ="NORDER"),
   Span(doc38, 9, 12, label ="CONTRACT"),
   Span(doc38, 12, 13, label ="CONTRACT1"),
   Span(doc38, 15, 16, label ="POS"),
   Span(doc38, 16, 17, label ="AMOUNT"),
   Span(doc38, 18, 19, label ="ARTICLE"),
   Span(doc38, 22, 23, label ="PRICE"),
   Span(doc38, 23, 24, label ="UNIT"),
   Span(doc38, 25, 26, label ="SUMMA"),
   Span(doc38, 52, 53, label ="TARIFF"),
   Span(doc38, 57, 58, label ="COUNTRY"),
   Span(doc38, 60, 61, label ="PR_SURCH"),
   Span(doc38, 62, 63, label ="SURCHARGE"),
   Span(doc38, 65, 66, label ="PR_ESURCH"),
   Span(doc38, 67, 68, label ="ESURCHARGE"),
   Span(doc38, 68, 69, label ="TOTAL")]
docs.append(doc38)
print("doc39, 69, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 12000; AMOUNT 300; ARTICLE 6020000529; PRICE 53,75; UNIT 100; SUMMA 161,25; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 11,13; PR_ESURCH 3,50; ESURCHARGE 5,64; TOTAL 178,02; ")
doc39 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 12000 300 PC 6020000529 (*) 53,75 100 PC 161,25 FI-GE-O8LR3/8-WD-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 11,13 Energy Surcharge 3,50 % 5,64 178,02''')
doc39.ents = [
   Span(doc39, 3, 4, label ="NORDER"),
   Span(doc39, 9, 12, label ="CONTRACT"),
   Span(doc39, 12, 13, label ="CONTRACT1"),
   Span(doc39, 15, 16, label ="POS"),
   Span(doc39, 16, 17, label ="AMOUNT"),
   Span(doc39, 18, 19, label ="ARTICLE"),
   Span(doc39, 22, 23, label ="PRICE"),
   Span(doc39, 23, 24, label ="UNIT"),
   Span(doc39, 25, 26, label ="SUMMA"),
   Span(doc39, 52, 53, label ="TARIFF"),
   Span(doc39, 57, 58, label ="COUNTRY"),
   Span(doc39, 60, 61, label ="PR_SURCH"),
   Span(doc39, 62, 63, label ="SURCHARGE"),
   Span(doc39, 65, 66, label ="PR_ESURCH"),
   Span(doc39, 67, 68, label ="ESURCHARGE"),
   Span(doc39, 68, 69, label ="TOTAL")]
docs.append(doc39)
print("doc40, 72, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 12100; AMOUNT 6.500; ARTICLE 6020000469; PRICE 36,40; UNIT 100; SUMMA 2.366; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 163,25; PR_ESURCH 3,50; ESURCHARGE 82,81; TOTAL 2.612,06; ")
doc40 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 12100 6.500 PC 6020000469 (*) 36,40 100 PC 2.366 ,00 FI-GE-O8LR-WD-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 163,25 Energy Surcharge 3,50 % 82,81 2.612,06   ''')
doc40.ents = [
   Span(doc40, 3, 4, label ="NORDER"),
   Span(doc40, 9, 12, label ="CONTRACT"),
   Span(doc40, 12, 13, label ="CONTRACT1"),
   Span(doc40, 15, 16, label ="POS"),
   Span(doc40, 16, 17, label ="AMOUNT"),
   Span(doc40, 18, 19, label ="ARTICLE"),
   Span(doc40, 22, 23, label ="PRICE"),
   Span(doc40, 23, 24, label ="UNIT"),
   Span(doc40, 25, 26, label ="SUMMA"),
   Span(doc40, 54, 55, label ="TARIFF"),
   Span(doc40, 59, 60, label ="COUNTRY"),
   Span(doc40, 62, 63, label ="PR_SURCH"),
   Span(doc40, 64, 65, label ="SURCHARGE"),
   Span(doc40, 67, 68, label ="PR_ESURCH"),
   Span(doc40, 69, 70, label ="ESURCHARGE"),
   Span(doc40, 70, 71, label ="TOTAL")]
docs.append(doc40)
print("doc41, 63, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 12200; AMOUNT 300; ARTICLE 6030003055; PRICE 37,72; UNIT 100; SUMMA 113,16; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 7,81; PR_ESURCH 3,50; ESURCHARGE 3,96; TOTAL 124,93; ")
doc41 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 12200 300 PC 6030003055 (*) 37,72 100 PC 113,16 FI-GE-12L3/8N-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 7,81 Energy Surcharge 3,50 % 3,96 124,93''')
doc41.ents = [
   Span(doc41, 3, 4, label ="NORDER"),
   Span(doc41, 9, 12, label ="CONTRACT"),
   Span(doc41, 12, 13, label ="CONTRACT1"),
   Span(doc41, 15, 16, label ="POS"),
   Span(doc41, 16, 17, label ="AMOUNT"),
   Span(doc41, 18, 19, label ="ARTICLE"),
   Span(doc41, 22, 23, label ="PRICE"),
   Span(doc41, 23, 24, label ="UNIT"),
   Span(doc41, 25, 26, label ="SUMMA"),
   Span(doc41, 46, 47, label ="TARIFF"),
   Span(doc41, 51, 52, label ="COUNTRY"),
   Span(doc41, 54, 55, label ="PR_SURCH"),
   Span(doc41, 56, 57, label ="SURCHARGE"),
   Span(doc41, 59, 60, label ="PR_ESURCH"),
   Span(doc41, 61, 62, label ="ESURCHARGE"),
   Span(doc41, 62, 63, label ="TOTAL")]
docs.append(doc41)
print("doc42, 65, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 12300; AMOUNT 210; ARTICLE 6020000244; PRICE 356,24; UNIT 100; SUMMA 748,10; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 51,62; PR_ESURCH 3,50; ESURCHARGE 26,18; TOTAL 825,90; ")
doc42 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 12300 210 PC 6020000244 (*) 356,24 100 PC 748,10 FI-GE-12L7/8U-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 51,62 Energy Surcharge 3,50 % 26,18 825,90''')
doc42.ents = [
   Span(doc42, 3, 4, label ="NORDER"),
   Span(doc42, 9, 12, label ="CONTRACT"),
   Span(doc42, 12, 13, label ="CONTRACT1"),
   Span(doc42, 15, 16, label ="POS"),
   Span(doc42, 16, 17, label ="AMOUNT"),
   Span(doc42, 18, 19, label ="ARTICLE"),
   Span(doc42, 22, 23, label ="PRICE"),
   Span(doc42, 23, 24, label ="UNIT"),
   Span(doc42, 25, 26, label ="SUMMA"),
   Span(doc42, 48, 49, label ="TARIFF"),
   Span(doc42, 53, 54, label ="COUNTRY"),
   Span(doc42, 56, 57, label ="PR_SURCH"),
   Span(doc42, 58, 59, label ="SURCHARGE"),
   Span(doc42, 61, 62, label ="PR_ESURCH"),
   Span(doc42, 63, 64, label ="ESURCHARGE"),
   Span(doc42, 64, 65, label ="TOTAL")]
docs.append(doc42)
print("doc43, 77, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 12400; AMOUNT 400; ARTICLE 6020000645; PRICE 105,60; UNIT 100; SUMMA 422,40; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 29,15; PR_ESURCH 3,50; ESURCHARGE 14,78; TOTAL 466,33; ")
doc43 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 12400 400 PC 6020000645 (*) 105,60 100 PC 422,40 FI-GE-12LM12x1.5-OR-B-W3 FI-GE-12LM12x1,5-OR-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 29,15 Energy Surcharge 3,50 % 14,78 466,33   ''')
doc43.ents = [
   Span(doc43, 3, 4, label ="NORDER"),
   Span(doc43, 9, 12, label ="CONTRACT"),
   Span(doc43, 12, 13, label ="CONTRACT1"),
   Span(doc43, 15, 16, label ="POS"),
   Span(doc43, 16, 17, label ="AMOUNT"),
   Span(doc43, 18, 19, label ="ARTICLE"),
   Span(doc43, 22, 23, label ="PRICE"),
   Span(doc43, 23, 24, label ="UNIT"),
   Span(doc43, 25, 26, label ="SUMMA"),
   Span(doc43, 59, 60, label ="TARIFF"),
   Span(doc43, 64, 65, label ="COUNTRY"),
   Span(doc43, 67, 68, label ="PR_SURCH"),
   Span(doc43, 69, 70, label ="SURCHARGE"),
   Span(doc43, 72, 73, label ="PR_ESURCH"),
   Span(doc43, 74, 75, label ="ESURCHARGE"),
   Span(doc43, 75, 76, label ="TOTAL")]
docs.append(doc43)
print("doc44, 80, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 12500; AMOUNT 60; ARTICLE 6010001432; PRICE 206,31; UNIT 100; SUMMA 123,79; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 8,54; PR_ESURCH 3,50; ESURCHARGE 4,33; TOTAL 136,66; ")
doc44 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 12500 60 PC 6010001432 (*) 206,31 100 PC 123,79 FI-GE-12LM12x1.5-WD-B-W3-MS FI-GE-12LM12x1,5-WD-B-W3-MS packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 8,54 Energy Surcharge 3,50 % 4,33 136,66''')
doc44.ents = [
   Span(doc44, 3, 4, label ="NORDER"),
   Span(doc44, 9, 12, label ="CONTRACT"),
   Span(doc44, 12, 13, label ="CONTRACT1"),
   Span(doc44, 15, 16, label ="POS"),
   Span(doc44, 16, 17, label ="AMOUNT"),
   Span(doc44, 18, 19, label ="ARTICLE"),
   Span(doc44, 22, 23, label ="PRICE"),
   Span(doc44, 23, 24, label ="UNIT"),
   Span(doc44, 25, 26, label ="SUMMA"),
   Span(doc44, 63, 64, label ="TARIFF"),
   Span(doc44, 68, 69, label ="COUNTRY"),
   Span(doc44, 71, 72, label ="PR_SURCH"),
   Span(doc44, 73, 74, label ="SURCHARGE"),
   Span(doc44, 76, 77, label ="PR_ESURCH"),
   Span(doc44, 78, 79, label ="ESURCHARGE"),
   Span(doc44, 79, 80, label ="TOTAL")]
docs.append(doc44)
print("doc45, 68, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 12600; AMOUNT 300; ARTICLE 6030003114; PRICE 36,58; UNIT 100; SUMMA 109,74; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 7,57; PR_ESURCH 3,50; ESURCHARGE 3,84; TOTAL 121,15; ")
doc45 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 12600 300 PC 6030003114 (*) 36,58 100 PC 109,74 FI-GE-12LM14x1.5-W3 FI-GE-12LM14x1,5-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 7,57 Energy Surcharge 3,50 % 3,84 121,15''')
doc45.ents = [
   Span(doc45, 3, 4, label ="NORDER"),
   Span(doc45, 9, 12, label ="CONTRACT"),
   Span(doc45, 12, 13, label ="CONTRACT1"),
   Span(doc45, 15, 16, label ="POS"),
   Span(doc45, 16, 17, label ="AMOUNT"),
   Span(doc45, 18, 19, label ="ARTICLE"),
   Span(doc45, 22, 23, label ="PRICE"),
   Span(doc45, 23, 24, label ="UNIT"),
   Span(doc45, 25, 26, label ="SUMMA"),
   Span(doc45, 51, 52, label ="TARIFF"),
   Span(doc45, 56, 57, label ="COUNTRY"),
   Span(doc45, 59, 60, label ="PR_SURCH"),
   Span(doc45, 61, 62, label ="SURCHARGE"),
   Span(doc45, 64, 65, label ="PR_ESURCH"),
   Span(doc45, 66, 67, label ="ESURCHARGE"),
   Span(doc45, 67, 68, label ="TOTAL")]
docs.append(doc45)
print("doc46, 79, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 12800; AMOUNT 5.300; ARTICLE 6020000412; PRICE 67,43; UNIT 100; SUMMA 3.573,79; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 246,59; PR_ESURCH 3,50; ESURCHARGE 125,08; TOTAL 3.945,46; ")
doc46 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 12800 5.300 PC 6020000412 (*) 67,43 100 PC 3.573,79 FI-GE-12LM22x1.5-WD-B-W3 FI-GE-12LM22x1 ,5-WD-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 246,59  Energy Surcharge 3,50 % 125,08 3.945,46''')
doc46.ents = [
   Span(doc46, 3, 4, label ="NORDER"),
   Span(doc46, 9, 12, label ="CONTRACT"),
   Span(doc46, 12, 13, label ="CONTRACT1"),
   Span(doc46, 15, 16, label ="POS"),
   Span(doc46, 16, 17, label ="AMOUNT"),
   Span(doc46, 18, 19, label ="ARTICLE"),
   Span(doc46, 22, 23, label ="PRICE"),
   Span(doc46, 23, 24, label ="UNIT"),
   Span(doc46, 25, 26, label ="SUMMA"),
   Span(doc46, 61, 62, label ="TARIFF"),
   Span(doc46, 66, 67, label ="COUNTRY"),
   Span(doc46, 69, 70, label ="PR_SURCH"),
   Span(doc46, 71, 72, label ="SURCHARGE"),
   Span(doc46, 75, 76, label ="PR_ESURCH"),
   Span(doc46, 77, 78, label ="ESURCHARGE"),
   Span(doc46, 78, 79, label ="TOTAL")]
docs.append(doc46)
print("doc47, 67, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 12900; AMOUNT 150; ARTICLE 6020000370; PRICE 47,72; UNIT 100; SUMMA 71,58; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 4,94; PR_ESURCH 3,50; ESURCHARGE 2,51; TOTAL 79,03; ")
doc47 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 12900 150 PC 6020000370 (*) 47,72 100 PC 71,58 FI-GE-12LM-WD-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 4,94 Energy Surcharge 3,50 % 2,51 79,03''')
doc47.ents = [
   Span(doc47, 3, 4, label ="NORDER"),
   Span(doc47, 9, 12, label ="CONTRACT"),
   Span(doc47, 12, 13, label ="CONTRACT1"),
   Span(doc47, 15, 16, label ="POS"),
   Span(doc47, 16, 17, label ="AMOUNT"),
   Span(doc47, 18, 19, label ="ARTICLE"),
   Span(doc47, 22, 23, label ="PRICE"),
   Span(doc47, 23, 24, label ="UNIT"),
   Span(doc47, 25, 26, label ="SUMMA"),
   Span(doc47, 50, 51, label ="TARIFF"),
   Span(doc47, 55, 56, label ="COUNTRY"),
   Span(doc47, 58, 59, label ="PR_SURCH"),
   Span(doc47, 60, 61, label ="SURCHARGE"),
   Span(doc47, 63, 64, label ="PR_ESURCH"),
   Span(doc47, 65, 66, label ="ESURCHARGE"),
   Span(doc47, 66, 67, label ="TOTAL")]
docs.append(doc47)
print("doc48, 67, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 13000; AMOUNT 6.000; ARTICLE 6020000462; PRICE 72,01; UNIT 100; SUMMA 4.320,60; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 298,12; PR_ESURCH 3,50; ESURCHARGE 151,22; TOTAL 4.769,94; ")
doc48 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 13000 6.000 PC 6020000462 (*) 72,01 100 PC 4.320,60 FI-GE-12LR1/2-WD-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 298,12 Energy Surcharge 3,50 % 151,22 4.769,94''')
doc48.ents = [
   Span(doc48, 3, 4, label ="NORDER"),
   Span(doc48, 9, 12, label ="CONTRACT"),
   Span(doc48, 12, 13, label ="CONTRACT1"),
   Span(doc48, 15, 16, label ="POS"),
   Span(doc48, 16, 17, label ="AMOUNT"),
   Span(doc48, 18, 19, label ="ARTICLE"),
   Span(doc48, 22, 23, label ="PRICE"),
   Span(doc48, 23, 24, label ="UNIT"),
   Span(doc48, 25, 26, label ="SUMMA"),
   Span(doc48, 50, 51, label ="TARIFF"),
   Span(doc48, 55, 56, label ="COUNTRY"),
   Span(doc48, 58, 59, label ="PR_SURCH"),
   Span(doc48, 60, 61, label ="SURCHARGE"),
   Span(doc48, 63, 64, label ="PR_ESURCH"),
   Span(doc48, 65, 66, label ="ESURCHARGE"),
   Span(doc48, 66, 67, label ="TOTAL")]
docs.append(doc48)
print("doc49, 68, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 13100; AMOUNT 500; ARTICLE 6020000460; PRICE 51,67; UNIT 100; SUMMA 258,35; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 17,83; PR_ESURCH 3,50; ESURCHARGE 9,04; TOTAL 285,22; ")
doc49 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 13100 500 PC 6020000460 (*) 51,67 100 PC 258,35 FI-GE-12LR1/4-WD-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 17,83   Energy Surcharge 3,50 % 9,04 285,22''')
doc49.ents = [
   Span(doc49, 3, 4, label ="NORDER"),
   Span(doc49, 9, 12, label ="CONTRACT"),
   Span(doc49, 12, 13, label ="CONTRACT1"),
   Span(doc49, 15, 16, label ="POS"),
   Span(doc49, 16, 17, label ="AMOUNT"),
   Span(doc49, 18, 19, label ="ARTICLE"),
   Span(doc49, 22, 23, label ="PRICE"),
   Span(doc49, 23, 24, label ="UNIT"),
   Span(doc49, 25, 26, label ="SUMMA"),
   Span(doc49, 50, 51, label ="TARIFF"),
   Span(doc49, 55, 56, label ="COUNTRY"),
   Span(doc49, 58, 59, label ="PR_SURCH"),
   Span(doc49, 60, 61, label ="SURCHARGE"),
   Span(doc49, 64, 65, label ="PR_ESURCH"),
   Span(doc49, 66, 67, label ="ESURCHARGE"),
   Span(doc49, 67, 68, label ="TOTAL")]
docs.append(doc49)
print("doc50, 69, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 13200; AMOUNT 3.600; ARTICLE 6020000473; PRICE 41,14; UNIT 100; SUMMA 1.481; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 102,19; PR_ESURCH 3,50; ESURCHARGE 51,84; TOTAL 1.635,07; ")
doc50 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 13200 3.600 PC 6020000473 (*) 41,14 100 PC 1.481 ,04 FI-GE-12LR-WD-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 102,19 Energy Surcharge 3,50 % 51,84 1.635,07''')
doc50.ents = [
   Span(doc50, 3, 4, label ="NORDER"),
   Span(doc50, 9, 12, label ="CONTRACT"),
   Span(doc50, 12, 13, label ="CONTRACT1"),
   Span(doc50, 15, 16, label ="POS"),
   Span(doc50, 16, 17, label ="AMOUNT"),
   Span(doc50, 18, 19, label ="ARTICLE"),
   Span(doc50, 22, 23, label ="PRICE"),
   Span(doc50, 23, 24, label ="UNIT"),
   Span(doc50, 25, 26, label ="SUMMA"),
   Span(doc50, 52, 53, label ="TARIFF"),
   Span(doc50, 57, 58, label ="COUNTRY"),
   Span(doc50, 60, 61, label ="PR_SURCH"),
   Span(doc50, 62, 63, label ="SURCHARGE"),
   Span(doc50, 65, 66, label ="PR_ESURCH"),
   Span(doc50, 67, 68, label ="ESURCHARGE"),
   Span(doc50, 68, 69, label ="TOTAL")]
docs.append(doc50)
print("doc51, 67, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 13300; AMOUNT 500; ARTICLE 6020000651; PRICE 53,17; UNIT 100; SUMMA 265,85; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 18,34; PR_ESURCH 3,50; ESURCHARGE 9,30; TOTAL 293,49; ")
doc51 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 13300 500 PC 6020000651 (*) 53,17 100 PC 265,85 FI-GE-15LM-OR-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 18,34 Energy Surcharge 3,50 % 9,30 293,49''')
doc51.ents = [
   Span(doc51, 3, 4, label ="NORDER"),
   Span(doc51, 9, 12, label ="CONTRACT"),
   Span(doc51, 12, 13, label ="CONTRACT1"),
   Span(doc51, 15, 16, label ="POS"),
   Span(doc51, 16, 17, label ="AMOUNT"),
   Span(doc51, 18, 19, label ="ARTICLE"),
   Span(doc51, 22, 23, label ="PRICE"),
   Span(doc51, 23, 24, label ="UNIT"),
   Span(doc51, 25, 26, label ="SUMMA"),
   Span(doc51, 50, 51, label ="TARIFF"),
   Span(doc51, 55, 56, label ="COUNTRY"),
   Span(doc51, 58, 59, label ="PR_SURCH"),
   Span(doc51, 60, 61, label ="SURCHARGE"),
   Span(doc51, 63, 64, label ="PR_ESURCH"),
   Span(doc51, 65, 66, label ="ESURCHARGE"),
   Span(doc51, 66, 67, label ="TOTAL")]
docs.append(doc51)
print("doc52, 68, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 13400; AMOUNT 125; ARTICLE 6020000372; PRICE 53,56; UNIT 100; SUMMA 66,95; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 4,62; PR_ESURCH 3,50; ESURCHARGE 2,34; TOTAL 73,91; ")
doc52 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 13400 125 PC 6020000372 (*) 53,56 100 PC 66,95 FI-GE-15LM-WD-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 4,62   Energy Surcharge 3,50 % 2,34 73,91''')
doc52.ents = [
   Span(doc52, 3, 4, label ="NORDER"),
   Span(doc52, 9, 12, label ="CONTRACT"),
   Span(doc52, 12, 13, label ="CONTRACT1"),
   Span(doc52, 15, 16, label ="POS"),
   Span(doc52, 16, 17, label ="AMOUNT"),
   Span(doc52, 18, 19, label ="ARTICLE"),
   Span(doc52, 22, 23, label ="PRICE"),
   Span(doc52, 23, 24, label ="UNIT"),
   Span(doc52, 25, 26, label ="SUMMA"),
   Span(doc52, 50, 51, label ="TARIFF"),
   Span(doc52, 55, 56, label ="COUNTRY"),
   Span(doc52, 58, 59, label ="PR_SURCH"),
   Span(doc52, 60, 61, label ="SURCHARGE"),
   Span(doc52, 64, 65, label ="PR_ESURCH"),
   Span(doc52, 66, 67, label ="ESURCHARGE"),
   Span(doc52, 67, 68, label ="TOTAL")]
docs.append(doc52)
print("doc53, 63, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 13500; AMOUNT 300; ARTICLE 6030003059; PRICE 61,85; UNIT 100; SUMMA 185,55; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 12,80; PR_ESURCH 3,50; ESURCHARGE 6,49; TOTAL 204,84; ")
doc53 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 13500 300 PC 6030003059 (*) 61,85 100 PC 185,55 FI-GE-18L1/2N-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 12,80 Energy Surcharge 3,50 % 6,49 204,84''')
doc53.ents = [
   Span(doc53, 3, 4, label ="NORDER"),
   Span(doc53, 9, 12, label ="CONTRACT"),
   Span(doc53, 12, 13, label ="CONTRACT1"),
   Span(doc53, 15, 16, label ="POS"),
   Span(doc53, 16, 17, label ="AMOUNT"),
   Span(doc53, 18, 19, label ="ARTICLE"),
   Span(doc53, 22, 23, label ="PRICE"),
   Span(doc53, 23, 24, label ="UNIT"),
   Span(doc53, 25, 26, label ="SUMMA"),
   Span(doc53, 46, 47, label ="TARIFF"),
   Span(doc53, 51, 52, label ="COUNTRY"),
   Span(doc53, 54, 55, label ="PR_SURCH"),
   Span(doc53, 56, 57, label ="SURCHARGE"),
   Span(doc53, 59, 60, label ="PR_ESURCH"),
   Span(doc53, 61, 62, label ="ESURCHARGE"),
   Span(doc53, 62, 63, label ="TOTAL")]
docs.append(doc53)
print("doc54, 67, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 13600; AMOUNT 525; ARTICLE 6020000653; PRICE 68,46; UNIT 100; SUMMA 359,42; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 24,80; PR_ESURCH 3,50; ESURCHARGE 12,58; TOTAL 396,80; ")
doc54 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 13600 525 PC 6020000653 (*) 68,46 100 PC 359,42 FI-GE-18LM-OR-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 24,80 Energy Surcharge 3,50 % 12,58 396,80''')
doc54.ents = [
   Span(doc54, 3, 4, label ="NORDER"),
   Span(doc54, 9, 12, label ="CONTRACT"),
   Span(doc54, 12, 13, label ="CONTRACT1"),
   Span(doc54, 15, 16, label ="POS"),
   Span(doc54, 16, 17, label ="AMOUNT"),
   Span(doc54, 18, 19, label ="ARTICLE"),
   Span(doc54, 22, 23, label ="PRICE"),
   Span(doc54, 23, 24, label ="UNIT"),
   Span(doc54, 25, 26, label ="SUMMA"),
   Span(doc54, 50, 51, label ="TARIFF"),
   Span(doc54, 55, 56, label ="COUNTRY"),
   Span(doc54, 58, 59, label ="PR_SURCH"),
   Span(doc54, 60, 61, label ="SURCHARGE"),
   Span(doc54, 63, 64, label ="PR_ESURCH"),
   Span(doc54, 65, 66, label ="ESURCHARGE"),
   Span(doc54, 66, 67, label ="TOTAL")]
docs.append(doc54)
print("doc55, 75, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 13900; AMOUNT 150; ARTICLE 6020000253; PRICE 578,00; UNIT 100; SUMMA 867,00; TARIFF 73079910; COUNTRY Germany   ; PR_SURCH 6,90; SURCHARGE 59,82; PR_ESURCH 3,50; ESURCHARGE 30,35; TOTAL 957,17; ")
doc55 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 13900 150 PC 6020000253 (*) 578,00 100 PC 867,00 FI-GE-22L1 -5/16U-B-W3 FI-GE-22L1 5/16U-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany   Material Surcharge 6,90 % 59,82 Energy Surcharge 3,50 % 30,35 957,17''')
doc55.ents = [
   Span(doc55, 3, 4, label ="NORDER"),
   Span(doc55, 9, 12, label ="CONTRACT"),
   Span(doc55, 12, 13, label ="CONTRACT1"),
   Span(doc55, 15, 16, label ="POS"),
   Span(doc55, 16, 17, label ="AMOUNT"),
   Span(doc55, 18, 19, label ="ARTICLE"),
   Span(doc55, 22, 23, label ="PRICE"),
   Span(doc55, 23, 24, label ="UNIT"),
   Span(doc55, 25, 26, label ="SUMMA"),
   Span(doc55, 57, 58, label ="TARIFF"),
   Span(doc55, 62, 64, label ="COUNTRY"),
   Span(doc55, 66, 67, label ="PR_SURCH"),
   Span(doc55, 68, 69, label ="SURCHARGE"),
   Span(doc55, 71, 72, label ="PR_ESURCH"),
   Span(doc55, 73, 74, label ="ESURCHARGE"),
   Span(doc55, 74, 75, label ="TOTAL")]
docs.append(doc55)
print("doc56, 67, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 14000; AMOUNT 500; ARTICLE 6020000251; PRICE 416,01; UNIT 100; SUMMA 2.080,05; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 143,52; PR_ESURCH 3,50; ESURCHARGE 72,80; TOTAL 2.296; ")
doc56 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 14000 500 PC 6020000251 (*) 416,01 100 PC 2.080,05 FI-GE-22L7/8U-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 143,52 Energy Surcharge 3,50 % 72,80 2.296 ,37''')
doc56.ents = [
   Span(doc56, 3, 4, label ="NORDER"),
   Span(doc56, 9, 12, label ="CONTRACT"),
   Span(doc56, 12, 13, label ="CONTRACT1"),
   Span(doc56, 15, 16, label ="POS"),
   Span(doc56, 16, 17, label ="AMOUNT"),
   Span(doc56, 18, 19, label ="ARTICLE"),
   Span(doc56, 22, 23, label ="PRICE"),
   Span(doc56, 23, 24, label ="UNIT"),
   Span(doc56, 25, 26, label ="SUMMA"),
   Span(doc56, 48, 49, label ="TARIFF"),
   Span(doc56, 53, 54, label ="COUNTRY"),
   Span(doc56, 56, 57, label ="PR_SURCH"),
   Span(doc56, 58, 59, label ="SURCHARGE"),
   Span(doc56, 61, 62, label ="PR_ESURCH"),
   Span(doc56, 63, 64, label ="ESURCHARGE"),
   Span(doc56, 64, 65, label ="TOTAL")]
docs.append(doc56)
print("doc57, 80, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 14100; AMOUNT 1.900; ARTICLE 6020000407; PRICE 151,81; UNIT 100; SUMMA 2.884; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 199,02; PR_ESURCH 3,50; ESURCHARGE 100,95; TOTAL 3.184,36; ")
doc57 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 14100 1.900 PC 6020000407 (*) 151,81 100 PC 2.884 ,39 FI-GE-22LM22x1.5-WD-B-W3 FI-GE-22LM22x1 ,5-WD-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 199,02 Energy Surcharge 3,50 % 100,95 3.184,36''')
doc57.ents = [
   Span(doc57, 3, 4, label ="NORDER"),
   Span(doc57, 9, 12, label ="CONTRACT"),
   Span(doc57, 12, 13, label ="CONTRACT1"),
   Span(doc57, 15, 16, label ="POS"),
   Span(doc57, 16, 17, label ="AMOUNT"),
   Span(doc57, 18, 19, label ="ARTICLE"),
   Span(doc57, 22, 23, label ="PRICE"),
   Span(doc57, 23, 24, label ="UNIT"),
   Span(doc57, 25, 26, label ="SUMMA"),
   Span(doc57, 63, 64, label ="TARIFF"),
   Span(doc57, 68, 69, label ="COUNTRY"),
   Span(doc57, 71, 72, label ="PR_SURCH"),
   Span(doc57, 73, 74, label ="SURCHARGE"),
   Span(doc57, 76, 77, label ="PR_ESURCH"),
   Span(doc57, 78, 79, label ="ESURCHARGE"),
   Span(doc57, 79, 80, label ="TOTAL")]
docs.append(doc57)
print("doc58, 64, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 14200; AMOUNT 50; ARTICLE 6030003130; PRICE 89,01; UNIT 100; SUMMA 44,51; TARIFF 73079910; COUNTRY Germany   ; PR_SURCH 6,90; SURCHARGE 3,07; PR_ESURCH 3,50; ESURCHARGE 1,56; TOTAL 49,14; ")
doc58 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 14200 50 PC 6030003130 (*) 89,01 100 PC 44,51 FI-GE-22LM-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany   Material Surcharge 6,90 % 3,07 Energy Surcharge 3,50 % 1,56 49,14''')
doc58.ents = [
   Span(doc58, 3, 4, label ="NORDER"),
   Span(doc58, 9, 12, label ="CONTRACT"),
   Span(doc58, 12, 13, label ="CONTRACT1"),
   Span(doc58, 15, 16, label ="POS"),
   Span(doc58, 16, 17, label ="AMOUNT"),
   Span(doc58, 18, 19, label ="ARTICLE"),
   Span(doc58, 22, 23, label ="PRICE"),
   Span(doc58, 23, 24, label ="UNIT"),
   Span(doc58, 25, 26, label ="SUMMA"),
   Span(doc58, 46, 47, label ="TARIFF"),
   Span(doc58, 51, 53, label ="COUNTRY"),
   Span(doc58, 55, 56, label ="PR_SURCH"),
   Span(doc58, 57, 58, label ="SURCHARGE"),
   Span(doc58, 60, 61, label ="PR_ESURCH"),
   Span(doc58, 62, 63, label ="ESURCHARGE"),
   Span(doc58, 63, 64, label ="TOTAL")]
docs.append(doc58)
print("doc59, 67, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 14300; AMOUNT 100; ARTICLE 6020000376; PRICE 87,33; UNIT 100; SUMMA 87,33; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 6,03; PR_ESURCH 3,50; ESURCHARGE 3,06; TOTAL 96,42; ")
doc59 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 14300 100 PC 6020000376 (*) 87,33 100 PC 87,33 FI-GE-22LM-WD-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 6,03 Energy Surcharge 3,50 % 3,06 96,42''')
doc59.ents = [
   Span(doc59, 3, 4, label ="NORDER"),
   Span(doc59, 9, 12, label ="CONTRACT"),
   Span(doc59, 12, 13, label ="CONTRACT1"),
   Span(doc59, 15, 16, label ="POS"),
   Span(doc59, 16, 17, label ="AMOUNT"),
   Span(doc59, 18, 19, label ="ARTICLE"),
   Span(doc59, 22, 23, label ="PRICE"),
   Span(doc59, 23, 24, label ="UNIT"),
   Span(doc59, 25, 26, label ="SUMMA"),
   Span(doc59, 50, 51, label ="TARIFF"),
   Span(doc59, 55, 56, label ="COUNTRY"),
   Span(doc59, 58, 59, label ="PR_SURCH"),
   Span(doc59, 60, 61, label ="SURCHARGE"),
   Span(doc59, 63, 64, label ="PR_ESURCH"),
   Span(doc59, 65, 66, label ="ESURCHARGE"),
   Span(doc59, 66, 67, label ="TOTAL")]
docs.append(doc59)
print("doc60, 67, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 14600; AMOUNT 175; ARTICLE 6020000656; PRICE 183,12; UNIT 100; SUMMA 320,46; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 22,11; PR_ESURCH 3,50; ESURCHARGE 11,22; TOTAL 353,79; ")
doc60 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 14600 175 PC 6020000656 (*) 183,12 100 PC 320,46 FI-GE-28LM-OR-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 22,11 Energy Surcharge 3,50 % 11,22 353,79''')
doc60.ents = [
   Span(doc60, 3, 4, label ="NORDER"),
   Span(doc60, 9, 12, label ="CONTRACT"),
   Span(doc60, 12, 13, label ="CONTRACT1"),
   Span(doc60, 15, 16, label ="POS"),
   Span(doc60, 16, 17, label ="AMOUNT"),
   Span(doc60, 18, 19, label ="ARTICLE"),
   Span(doc60, 22, 23, label ="PRICE"),
   Span(doc60, 23, 24, label ="UNIT"),
   Span(doc60, 25, 26, label ="SUMMA"),
   Span(doc60, 50, 51, label ="TARIFF"),
   Span(doc60, 55, 56, label ="COUNTRY"),
   Span(doc60, 58, 59, label ="PR_SURCH"),
   Span(doc60, 60, 61, label ="SURCHARGE"),
   Span(doc60, 63, 64, label ="PR_ESURCH"),
   Span(doc60, 65, 66, label ="ESURCHARGE"),
   Span(doc60, 66, 67, label ="TOTAL")]
docs.append(doc60)
print("doc61, 77, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 14700; AMOUNT 500; ARTICLE 6020000277; PRICE 349,72; UNIT 100; SUMMA 1.748,60; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 120,65; PR_ESURCH 3,50; ESURCHARGE 61,20; TOTAL 1.930,45; ")
doc61 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 14700 500 PC 6020000277 (*) 349,72 100 PC 1.748,60 FI-GE-3 5L1 -5/8 U-B-W3 FI-GE-35L1 5/8U-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910    Country of origin: Germany Material Surcharge 6,90 % 120,65 Energy Surcharge 3,50 % 61,20 1.930,45''')
doc61.ents = [
   Span(doc61, 3, 4, label ="NORDER"),
   Span(doc61, 9, 12, label ="CONTRACT"),
   Span(doc61, 12, 13, label ="CONTRACT1"),
   Span(doc61, 15, 16, label ="POS"),
   Span(doc61, 16, 17, label ="AMOUNT"),
   Span(doc61, 18, 19, label ="ARTICLE"),
   Span(doc61, 22, 23, label ="PRICE"),
   Span(doc61, 23, 24, label ="UNIT"),
   Span(doc61, 25, 26, label ="SUMMA"),
   Span(doc61, 59, 60, label ="TARIFF"),
   Span(doc61, 65, 66, label ="COUNTRY"),
   Span(doc61, 68, 69, label ="PR_SURCH"),
   Span(doc61, 70, 71, label ="SURCHARGE"),
   Span(doc61, 73, 74, label ="PR_ESURCH"),
   Span(doc61, 75, 76, label ="ESURCHARGE"),
   Span(doc61, 76, 77, label ="TOTAL")]
docs.append(doc61)
print("doc62, 67, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 14800; AMOUNT 30; ARTICLE 6020000380; PRICE 277,59; UNIT 100; SUMMA 83,28; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 5,75; PR_ESURCH 3,50; ESURCHARGE 2,91; TOTAL 91,94; ")
doc62 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 14800 30 PC 6020000380 (*) 277,59 100 PC 83,28 FI-GE-35LM-WD-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 5,75 Energy Surcharge 3,50 % 2,91 91,94''')
doc62.ents = [
   Span(doc62, 3, 4, label ="NORDER"),
   Span(doc62, 9, 12, label ="CONTRACT"),
   Span(doc62, 12, 13, label ="CONTRACT1"),
   Span(doc62, 15, 16, label ="POS"),
   Span(doc62, 16, 17, label ="AMOUNT"),
   Span(doc62, 18, 19, label ="ARTICLE"),
   Span(doc62, 22, 23, label ="PRICE"),
   Span(doc62, 23, 24, label ="UNIT"),
   Span(doc62, 25, 26, label ="SUMMA"),
   Span(doc62, 50, 51, label ="TARIFF"),
   Span(doc62, 55, 56, label ="COUNTRY"),
   Span(doc62, 58, 59, label ="PR_SURCH"),
   Span(doc62, 60, 61, label ="SURCHARGE"),
   Span(doc62, 63, 64, label ="PR_ESURCH"),
   Span(doc62, 65, 66, label ="ESURCHARGE"),
   Span(doc62, 66, 67, label ="TOTAL")]
docs.append(doc62)
print("doc63, 67, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 14900; AMOUNT 300; ARTICLE 6020000483; PRICE 280,98; UNIT 100; SUMMA 842,94; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 58,16; PR_ESURCH 3,50; ESURCHARGE 29,50; TOTAL 930,60; ")
doc63 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 14900 300 PC 6020000483 (*) 280,98 100 PC 842,94 FI-GE-35LR-WD-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 58,16 Energy Surcharge 3,50 % 29,50 930,60''')
doc63.ents = [
   Span(doc63, 3, 4, label ="NORDER"),
   Span(doc63, 9, 12, label ="CONTRACT"),
   Span(doc63, 12, 13, label ="CONTRACT1"),
   Span(doc63, 15, 16, label ="POS"),
   Span(doc63, 16, 17, label ="AMOUNT"),
   Span(doc63, 18, 19, label ="ARTICLE"),
   Span(doc63, 22, 23, label ="PRICE"),
   Span(doc63, 23, 24, label ="UNIT"),
   Span(doc63, 25, 26, label ="SUMMA"),
   Span(doc63, 50, 51, label ="TARIFF"),
   Span(doc63, 55, 56, label ="COUNTRY"),
   Span(doc63, 58, 59, label ="PR_SURCH"),
   Span(doc63, 60, 61, label ="SURCHARGE"),
   Span(doc63, 63, 64, label ="PR_ESURCH"),
   Span(doc63, 65, 66, label ="ESURCHARGE"),
   Span(doc63, 66, 67, label ="TOTAL")]
docs.append(doc63)
print("doc64, 66, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 15000; AMOUNT 1.080; ARTICLE 6020000199; PRICE 63,56; UNIT 100; SUMMA 686,45; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 47,37; PR_ESURCH 3,50; ESURCHARGE 24,03; TOTAL 757,85; ")
doc64 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 15000 1.080 PC 6020000199 (*) 63,56 100 PC 686,45 FI-GS-08L-W3-SKM packed per each item Product description: fitting Export - Customs tariff no.: 73079910    Country of origin: Germany Material Surcharge 6,90 % 47,37 Energy Surcharge 3,50 % 24,03 757,85''')
doc64.ents = [
   Span(doc64, 3, 4, label ="NORDER"),
   Span(doc64, 9, 12, label ="CONTRACT"),
   Span(doc64, 12, 13, label ="CONTRACT1"),
   Span(doc64, 15, 16, label ="POS"),
   Span(doc64, 16, 17, label ="AMOUNT"),
   Span(doc64, 18, 19, label ="ARTICLE"),
   Span(doc64, 22, 23, label ="PRICE"),
   Span(doc64, 23, 24, label ="UNIT"),
   Span(doc64, 25, 26, label ="SUMMA"),
   Span(doc64, 48, 49, label ="TARIFF"),
   Span(doc64, 54, 55, label ="COUNTRY"),
   Span(doc64, 57, 58, label ="PR_SURCH"),
   Span(doc64, 59, 60, label ="SURCHARGE"),
   Span(doc64, 62, 63, label ="PR_ESURCH"),
   Span(doc64, 64, 65, label ="ESURCHARGE"),
   Span(doc64, 65, 66, label ="TOTAL")]
docs.append(doc64)
print("doc65, 65, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 15100; AMOUNT 570; ARTICLE 6020000203; PRICE 233,65; UNIT 100; SUMMA 1.331,81; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 91,89; PR_ESURCH 3,50; ESURCHARGE 46,61; TOTAL 1.470,31; ")
doc65 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 15100 570 PC 6020000203 (*) 233,65 100 PC 1.331,81 FI-GS-18L-W3-SKM packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 91,89 Energy Surcharge 3,50 % 46,61 1.470,31''')
doc65.ents = [
   Span(doc65, 3, 4, label ="NORDER"),
   Span(doc65, 9, 12, label ="CONTRACT"),
   Span(doc65, 12, 13, label ="CONTRACT1"),
   Span(doc65, 15, 16, label ="POS"),
   Span(doc65, 16, 17, label ="AMOUNT"),
   Span(doc65, 18, 19, label ="ARTICLE"),
   Span(doc65, 22, 23, label ="PRICE"),
   Span(doc65, 23, 24, label ="UNIT"),
   Span(doc65, 25, 26, label ="SUMMA"),
   Span(doc65, 48, 49, label ="TARIFF"),
   Span(doc65, 53, 54, label ="COUNTRY"),
   Span(doc65, 56, 57, label ="PR_SURCH"),
   Span(doc65, 58, 59, label ="SURCHARGE"),
   Span(doc65, 61, 62, label ="PR_ESURCH"),
   Span(doc65, 63, 64, label ="ESURCHARGE"),
   Span(doc65, 64, 65, label ="TOTAL")]
docs.append(doc65)
print("doc66, 65, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 15200; AMOUNT 120; ARTICLE 6020000214; PRICE 368,30; UNIT 100; SUMMA 441,96; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 30,50; PR_ESURCH 3,50; ESURCHARGE 15,47; TOTAL 487,93; ")
doc66 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 15200 120 PC 6020000214 (*) 368,30 100 PC 441,96 FI-GS-20S-W3-SKM packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 30,50 Energy Surcharge 3,50 % 15,47 487,93''')
doc66.ents = [
   Span(doc66, 3, 4, label ="NORDER"),
   Span(doc66, 9, 12, label ="CONTRACT"),
   Span(doc66, 12, 13, label ="CONTRACT1"),
   Span(doc66, 15, 16, label ="POS"),
   Span(doc66, 16, 17, label ="AMOUNT"),
   Span(doc66, 18, 19, label ="ARTICLE"),
   Span(doc66, 22, 23, label ="PRICE"),
   Span(doc66, 23, 24, label ="UNIT"),
   Span(doc66, 25, 26, label ="SUMMA"),
   Span(doc66, 48, 49, label ="TARIFF"),
   Span(doc66, 53, 54, label ="COUNTRY"),
   Span(doc66, 56, 57, label ="PR_SURCH"),
   Span(doc66, 58, 59, label ="SURCHARGE"),
   Span(doc66, 61, 62, label ="PR_ESURCH"),
   Span(doc66, 63, 64, label ="ESURCHARGE"),
   Span(doc66, 64, 65, label ="TOTAL")]
docs.append(doc66)
print("doc67, 68, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 15300; AMOUNT 287; ARTICLE 6020000205; PRICE 424,30; UNIT 100; SUMMA 1.217,74; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 84,02; PR_ESURCH 3,50; ESURCHARGE 42,62; TOTAL 1.344; ")
doc67 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 15300 287 PC 6020000205 (*) 424,30 100 PC 1.217,74 FI-GS-28L-W3-SKM packed per each item Product description: fitting Export - Customs tariff no.: 73079910    Country of origin: Germany Material Surcharge 6,90 % 84,02 Energy Surcharge 3,50 % 42,62 1.344 ,38''')
doc67.ents = [
   Span(doc67, 3, 4, label ="NORDER"),
   Span(doc67, 9, 12, label ="CONTRACT"),
   Span(doc67, 12, 13, label ="CONTRACT1"),
   Span(doc67, 15, 16, label ="POS"),
   Span(doc67, 16, 17, label ="AMOUNT"),
   Span(doc67, 18, 19, label ="ARTICLE"),
   Span(doc67, 22, 23, label ="PRICE"),
   Span(doc67, 23, 24, label ="UNIT"),
   Span(doc67, 25, 26, label ="SUMMA"),
   Span(doc67, 48, 49, label ="TARIFF"),
   Span(doc67, 54, 55, label ="COUNTRY"),
   Span(doc67, 57, 58, label ="PR_SURCH"),
   Span(doc67, 59, 60, label ="SURCHARGE"),
   Span(doc67, 62, 63, label ="PR_ESURCH"),
   Span(doc67, 64, 65, label ="ESURCHARGE"),
   Span(doc67, 65, 66, label ="TOTAL")]
docs.append(doc67)
print("doc68, 65, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 15400; AMOUNT 150; ARTICLE 6020000206; PRICE 697,55; UNIT 100; SUMMA 1.046,33; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 72,20; PR_ESURCH 3,50; ESURCHARGE 36,62; TOTAL 1.155,15; ")
doc68 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 15400 150 PC 6020000206 (*) 697,55 100 PC 1.046,33 FI-GS-35L-W3-SKM packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 72,20 Energy Surcharge 3,50 % 36,62 1.155,15''')
doc68.ents = [
   Span(doc68, 3, 4, label ="NORDER"),
   Span(doc68, 9, 12, label ="CONTRACT"),
   Span(doc68, 12, 13, label ="CONTRACT1"),
   Span(doc68, 15, 16, label ="POS"),
   Span(doc68, 16, 17, label ="AMOUNT"),
   Span(doc68, 18, 19, label ="ARTICLE"),
   Span(doc68, 22, 23, label ="PRICE"),
   Span(doc68, 23, 24, label ="UNIT"),
   Span(doc68, 25, 26, label ="SUMMA"),
   Span(doc68, 48, 49, label ="TARIFF"),
   Span(doc68, 53, 54, label ="COUNTRY"),
   Span(doc68, 56, 57, label ="PR_SURCH"),
   Span(doc68, 58, 59, label ="SURCHARGE"),
   Span(doc68, 61, 62, label ="PR_ESURCH"),
   Span(doc68, 63, 64, label ="ESURCHARGE"),
   Span(doc68, 64, 65, label ="TOTAL")]
docs.append(doc68)
print("doc69, 67, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 15500; AMOUNT 100; ARTICLE 6010000025; PRICE 285,89; UNIT 100; SUMMA 285,89; TARIFF 73079290; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 19,73; PR_ESURCH 3,50; ESURCHARGE 10,01; TOTAL 315,63; ")
doc69 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 15500 100 PC 6010000025 (*) 285,89 100 PC 285,89 FI-RSW-08LM-WD-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079290 Country of origin: Germany Material Surcharge 6,90 % 19,73 Energy Surcharge 3,50 % 10,01 315,63''')
doc69.ents = [
   Span(doc69, 3, 4, label ="NORDER"),
   Span(doc69, 9, 12, label ="CONTRACT"),
   Span(doc69, 12, 13, label ="CONTRACT1"),
   Span(doc69, 15, 16, label ="POS"),
   Span(doc69, 16, 17, label ="AMOUNT"),
   Span(doc69, 18, 19, label ="ARTICLE"),
   Span(doc69, 22, 23, label ="PRICE"),
   Span(doc69, 23, 24, label ="UNIT"),
   Span(doc69, 25, 26, label ="SUMMA"),
   Span(doc69, 50, 51, label ="TARIFF"),
   Span(doc69, 55, 56, label ="COUNTRY"),
   Span(doc69, 58, 59, label ="PR_SURCH"),
   Span(doc69, 60, 61, label ="SURCHARGE"),
   Span(doc69, 63, 64, label ="PR_ESURCH"),
   Span(doc69, 65, 66, label ="ESURCHARGE"),
   Span(doc69, 66, 67, label ="TOTAL")]
docs.append(doc69)
print("doc70, 79, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 15600; AMOUNT 700; ARTICLE 6010003204; PRICE 168,39; UNIT 100; SUMMA 1.178,73; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 81,33; PR_ESURCH 3,50; ESURCHARGE 41,26; TOTAL 1.301; ")
doc70 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 15600 700 PC 6010003204 (*) 168,39 100 PC 1.178,73 FI-SNV-12L-V-W3-DKO FI-SNV-12L-B-W3-DKO packed per each item Product description: fitting    Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 81,33 Energy Surcharge 3,50 % 41,26 1.301 ,32''')
doc70.ents = [
   Span(doc70, 3, 4, label ="NORDER"),
   Span(doc70, 9, 12, label ="CONTRACT"),
   Span(doc70, 12, 13, label ="CONTRACT1"),
   Span(doc70, 15, 16, label ="POS"),
   Span(doc70, 16, 17, label ="AMOUNT"),
   Span(doc70, 18, 19, label ="ARTICLE"),
   Span(doc70, 22, 23, label ="PRICE"),
   Span(doc70, 23, 24, label ="UNIT"),
   Span(doc70, 25, 26, label ="SUMMA"),
   Span(doc70, 60, 61, label ="TARIFF"),
   Span(doc70, 65, 66, label ="COUNTRY"),
   Span(doc70, 68, 69, label ="PR_SURCH"),
   Span(doc70, 70, 71, label ="SURCHARGE"),
   Span(doc70, 73, 74, label ="PR_ESURCH"),
   Span(doc70, 75, 76, label ="ESURCHARGE"),
   Span(doc70, 76, 77, label ="TOTAL")]
docs.append(doc70)
print("doc71, 62, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 15900; AMOUNT 75; ARTICLE 6030003845; PRICE 111,64; UNIT 100; SUMMA 83,73; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 5,78; PR_ESURCH 3,50; ESURCHARGE 2,93; TOTAL 92,44; ")
doc71 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 15900 75 PC 6030003845 111,64 100 PC 83,73 FI-T-O8L-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 5,78 Energy Surcharge 3,50 % 2,93 92,44''')
doc71.ents = [
   Span(doc71, 3, 4, label ="NORDER"),
   Span(doc71, 9, 12, label ="CONTRACT"),
   Span(doc71, 12, 13, label ="CONTRACT1"),
   Span(doc71, 15, 16, label ="POS"),
   Span(doc71, 16, 17, label ="AMOUNT"),
   Span(doc71, 18, 19, label ="ARTICLE"),
   Span(doc71, 19, 20, label ="PRICE"),
   Span(doc71, 20, 21, label ="UNIT"),
   Span(doc71, 22, 23, label ="SUMMA"),
   Span(doc71, 45, 46, label ="TARIFF"),
   Span(doc71, 50, 51, label ="COUNTRY"),
   Span(doc71, 53, 54, label ="PR_SURCH"),
   Span(doc71, 55, 56, label ="SURCHARGE"),
   Span(doc71, 58, 59, label ="PR_ESURCH"),
   Span(doc71, 60, 61, label ="ESURCHARGE"),
   Span(doc71, 61, 62, label ="TOTAL")]
docs.append(doc71)
print("doc72, 60, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 16000; AMOUNT 150; ARTICLE 6030003465; PRICE 467,12; UNIT 100; SUMMA 700,68; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 48,35; PR_ESURCH 3,50; ESURCHARGE 24,52; TOTAL 773,55; ")
doc72 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 16000 150 PC 6030003465 467,12 100 PC 700,68 FI-T-12/08/08L-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 48,35 Energy Surcharge 3,50 % 24,52 773,55''')
doc72.ents = [
   Span(doc72, 3, 4, label ="NORDER"),
   Span(doc72, 9, 12, label ="CONTRACT"),
   Span(doc72, 12, 13, label ="CONTRACT1"),
   Span(doc72, 15, 16, label ="POS"),
   Span(doc72, 16, 17, label ="AMOUNT"),
   Span(doc72, 18, 19, label ="ARTICLE"),
   Span(doc72, 19, 20, label ="PRICE"),
   Span(doc72, 20, 21, label ="UNIT"),
   Span(doc72, 22, 23, label ="SUMMA"),
   Span(doc72, 43, 44, label ="TARIFF"),
   Span(doc72, 48, 49, label ="COUNTRY"),
   Span(doc72, 51, 52, label ="PR_SURCH"),
   Span(doc72, 53, 54, label ="SURCHARGE"),
   Span(doc72, 56, 57, label ="PR_ESURCH"),
   Span(doc72, 58, 59, label ="ESURCHARGE"),
   Span(doc72, 59, 60, label ="TOTAL")]
docs.append(doc72)
print("doc73, 61, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 16100; AMOUNT 100; ARTICLE 6030003463; PRICE 257,10; UNIT 100; SUMMA 257,10; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 17,74; PR_ESURCH 3,50; ESURCHARGE 9,00; TOTAL 283,84; ")
doc73 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 16100 100 PC 6030003463 257,10 100 PC 257,10 FI-T-12/08/12L-W3 packed per each item Product description: fitting    Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 17,74 Energy Surcharge 3,50 % 9,00 283,84''')
doc73.ents = [
   Span(doc73, 3, 4, label ="NORDER"),
   Span(doc73, 9, 12, label ="CONTRACT"),
   Span(doc73, 12, 13, label ="CONTRACT1"),
   Span(doc73, 15, 16, label ="POS"),
   Span(doc73, 16, 17, label ="AMOUNT"),
   Span(doc73, 18, 19, label ="ARTICLE"),
   Span(doc73, 19, 20, label ="PRICE"),
   Span(doc73, 20, 21, label ="UNIT"),
   Span(doc73, 22, 23, label ="SUMMA"),
   Span(doc73, 44, 45, label ="TARIFF"),
   Span(doc73, 49, 50, label ="COUNTRY"),
   Span(doc73, 52, 53, label ="PR_SURCH"),
   Span(doc73, 54, 55, label ="SURCHARGE"),
   Span(doc73, 57, 58, label ="PR_ESURCH"),
   Span(doc73, 59, 60, label ="ESURCHARGE"),
   Span(doc73, 60, 61, label ="TOTAL")]
docs.append(doc73)
print("doc74, 60, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 16200; AMOUNT 30; ARTICLE 6030003849; PRICE 238,93; UNIT 100; SUMMA 71,68; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 4,95; PR_ESURCH 3,50; ESURCHARGE 2,51; TOTAL 79,14; ")
doc74 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 16200 30 PC 6030003849 238,93 100 PC 71,68 FI-T-18L-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 4,95 Energy Surcharge 3,50 % 2,51 79,14''')
doc74.ents = [
   Span(doc74, 3, 4, label ="NORDER"),
   Span(doc74, 9, 12, label ="CONTRACT"),
   Span(doc74, 12, 13, label ="CONTRACT1"),
   Span(doc74, 15, 16, label ="POS"),
   Span(doc74, 16, 17, label ="AMOUNT"),
   Span(doc74, 18, 19, label ="ARTICLE"),
   Span(doc74, 19, 20, label ="PRICE"),
   Span(doc74, 20, 21, label ="UNIT"),
   Span(doc74, 22, 23, label ="SUMMA"),
   Span(doc74, 43, 44, label ="TARIFF"),
   Span(doc74, 48, 49, label ="COUNTRY"),
   Span(doc74, 51, 52, label ="PR_SURCH"),
   Span(doc74, 53, 54, label ="SURCHARGE"),
   Span(doc74, 56, 57, label ="PR_ESURCH"),
   Span(doc74, 58, 59, label ="ESURCHARGE"),
   Span(doc74, 59, 60, label ="TOTAL")]
docs.append(doc74)
print("doc75, 62, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 16300; AMOUNT 740; ARTICLE 6030003850; PRICE 348,87; UNIT 100; SUMMA 2.581; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 178,13; PR_ESURCH 3,50; ESURCHARGE 90,36; TOTAL 2.850,13; ")
doc75 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 16300 740 PC 6030003850 348,87 100 PC 2.581 ,64 FI-T-22L-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 178,13 Energy Surcharge 3,50 % 90,36 2.850,13''')
doc75.ents = [
   Span(doc75, 3, 4, label ="NORDER"),
   Span(doc75, 9, 12, label ="CONTRACT"),
   Span(doc75, 12, 13, label ="CONTRACT1"),
   Span(doc75, 15, 16, label ="POS"),
   Span(doc75, 16, 17, label ="AMOUNT"),
   Span(doc75, 18, 19, label ="ARTICLE"),
   Span(doc75, 19, 20, label ="PRICE"),
   Span(doc75, 20, 21, label ="UNIT"),
   Span(doc75, 22, 23, label ="SUMMA"),
   Span(doc75, 45, 46, label ="TARIFF"),
   Span(doc75, 50, 51, label ="COUNTRY"),
   Span(doc75, 53, 54, label ="PR_SURCH"),
   Span(doc75, 55, 56, label ="SURCHARGE"),
   Span(doc75, 58, 59, label ="PR_ESURCH"),
   Span(doc75, 60, 61, label ="ESURCHARGE"),
   Span(doc75, 61, 62, label ="TOTAL")]
docs.append(doc75)
print("doc76, 61, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 16400; AMOUNT 40; ARTICLE 6030003851; PRICE 550,65; UNIT 100; SUMMA 220,26; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 15,20; PR_ESURCH 3,50; ESURCHARGE 7,71; TOTAL 243,17; ")
doc76 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 16400 40 PC 6030003851 550,65 100 PC 220,26 FI-T-28L-W3 packed per each item Product description: fitting    Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 15,20 Energy Surcharge 3,50 % 7,71 243,17''')
doc76.ents = [
   Span(doc76, 3, 4, label ="NORDER"),
   Span(doc76, 9, 12, label ="CONTRACT"),
   Span(doc76, 12, 13, label ="CONTRACT1"),
   Span(doc76, 15, 16, label ="POS"),
   Span(doc76, 16, 17, label ="AMOUNT"),
   Span(doc76, 18, 19, label ="ARTICLE"),
   Span(doc76, 19, 20, label ="PRICE"),
   Span(doc76, 20, 21, label ="UNIT"),
   Span(doc76, 22, 23, label ="SUMMA"),
   Span(doc76, 44, 45, label ="TARIFF"),
   Span(doc76, 49, 50, label ="COUNTRY"),
   Span(doc76, 52, 53, label ="PR_SURCH"),
   Span(doc76, 54, 55, label ="SURCHARGE"),
   Span(doc76, 57, 58, label ="PR_ESURCH"),
   Span(doc76, 59, 60, label ="ESURCHARGE"),
   Span(doc76, 60, 61, label ="TOTAL")]
docs.append(doc76)
print("doc77, 60, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 16600; AMOUNT 50; ARTICLE 6030003436; PRICE 183,29; UNIT 100; SUMMA 91,65; TARIFF 73079290; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 6,32; PR_ESURCH 3,50; ESURCHARGE 3,21; TOTAL 101,18; ")
doc77 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 16600 50 PC 6030003436 183,29 100 PC 91,65 FI-W-18L-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079290 Country of origin: Germany Material Surcharge 6,90 % 6,32 Energy Surcharge 3,50 % 3,21 101,18''')
doc77.ents = [
   Span(doc77, 3, 4, label ="NORDER"),
   Span(doc77, 9, 12, label ="CONTRACT"),
   Span(doc77, 12, 13, label ="CONTRACT1"),
   Span(doc77, 15, 16, label ="POS"),
   Span(doc77, 16, 17, label ="AMOUNT"),
   Span(doc77, 18, 19, label ="ARTICLE"),
   Span(doc77, 19, 20, label ="PRICE"),
   Span(doc77, 20, 21, label ="UNIT"),
   Span(doc77, 22, 23, label ="SUMMA"),
   Span(doc77, 43, 44, label ="TARIFF"),
   Span(doc77, 48, 49, label ="COUNTRY"),
   Span(doc77, 51, 52, label ="PR_SURCH"),
   Span(doc77, 53, 54, label ="SURCHARGE"),
   Span(doc77, 56, 57, label ="PR_ESURCH"),
   Span(doc77, 58, 59, label ="ESURCHARGE"),
   Span(doc77, 59, 60, label ="TOTAL")]
docs.append(doc77)
print("doc78, 60, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 16700; AMOUNT 30; ARTICLE 6030003438; PRICE 403,37; UNIT 100; SUMMA 121,01; TARIFF 73079290; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 8,35; PR_ESURCH 3,50; ESURCHARGE 4,24; TOTAL 133,60; ")
doc78 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 16700 30 PC 6030003438 403,37 100 PC 121,01 FI-W-28L-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079290 Country of origin: Germany Material Surcharge 6,90 % 8,35 Energy Surcharge 3,50 % 4,24 133,60''')
doc78.ents = [
   Span(doc78, 3, 4, label ="NORDER"),
   Span(doc78, 9, 12, label ="CONTRACT"),
   Span(doc78, 12, 13, label ="CONTRACT1"),
   Span(doc78, 15, 16, label ="POS"),
   Span(doc78, 16, 17, label ="AMOUNT"),
   Span(doc78, 18, 19, label ="ARTICLE"),
   Span(doc78, 19, 20, label ="PRICE"),
   Span(doc78, 20, 21, label ="UNIT"),
   Span(doc78, 22, 23, label ="SUMMA"),
   Span(doc78, 43, 44, label ="TARIFF"),
   Span(doc78, 48, 49, label ="COUNTRY"),
   Span(doc78, 51, 52, label ="PR_SURCH"),
   Span(doc78, 53, 54, label ="SURCHARGE"),
   Span(doc78, 56, 57, label ="PR_ESURCH"),
   Span(doc78, 58, 59, label ="ESURCHARGE"),
   Span(doc78, 59, 60, label ="TOTAL")]
docs.append(doc78)
print("doc79, 61, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 16800; AMOUNT 160; ARTICLE 6030006325; PRICE 382,81; UNIT 100; SUMMA 612,50; TARIFF 73079311; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 42,26; PR_ESURCH 3,50; ESURCHARGE 21,44; TOTAL 676,20; ")
doc79 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 16800 160 PC 6030006325 382,81 100 PC 612,50 FI-WAS-22L-W2 packed per each item Product description: fitting    Export - Customs tariff no.: 73079311 Country of origin: Germany Material Surcharge 6,90 % 42,26 Energy Surcharge 3,50 % 21,44 676,20''')
doc79.ents = [
   Span(doc79, 3, 4, label ="NORDER"),
   Span(doc79, 9, 12, label ="CONTRACT"),
   Span(doc79, 12, 13, label ="CONTRACT1"),
   Span(doc79, 15, 16, label ="POS"),
   Span(doc79, 16, 17, label ="AMOUNT"),
   Span(doc79, 18, 19, label ="ARTICLE"),
   Span(doc79, 19, 20, label ="PRICE"),
   Span(doc79, 20, 21, label ="UNIT"),
   Span(doc79, 22, 23, label ="SUMMA"),
   Span(doc79, 44, 45, label ="TARIFF"),
   Span(doc79, 49, 50, label ="COUNTRY"),
   Span(doc79, 52, 53, label ="PR_SURCH"),
   Span(doc79, 54, 55, label ="SURCHARGE"),
   Span(doc79, 57, 58, label ="PR_ESURCH"),
   Span(doc79, 59, 60, label ="ESURCHARGE"),
   Span(doc79, 60, 61, label ="TOTAL")]
docs.append(doc79)
print("doc80, 69, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 16900; AMOUNT 175; ARTICLE 6010014935; PRICE 110,70; UNIT 100; SUMMA 193,73; TARIFF 73079290; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 13,37; PR_ESURCH 3,50; ESURCHARGE 6,78; TOTAL 213,88; ")
doc80 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 16900 175 PC 6010014935 (*) 110,70 100 PC 193,73 FI-WE-O06LLMk-W3-MS-PR packed per each item Product description: fitting Export - Customs tariff no.: 73079290 Country of origin: Germany Material Surcharge 6,90 % 13,37 Energy Surcharge 3,50 % 6,78 213,88''')
doc80.ents = [
   Span(doc80, 3, 4, label ="NORDER"),
   Span(doc80, 9, 12, label ="CONTRACT"),
   Span(doc80, 12, 13, label ="CONTRACT1"),
   Span(doc80, 15, 16, label ="POS"),
   Span(doc80, 16, 17, label ="AMOUNT"),
   Span(doc80, 18, 19, label ="ARTICLE"),
   Span(doc80, 22, 23, label ="PRICE"),
   Span(doc80, 23, 24, label ="UNIT"),
   Span(doc80, 25, 26, label ="SUMMA"),
   Span(doc80, 52, 53, label ="TARIFF"),
   Span(doc80, 57, 58, label ="COUNTRY"),
   Span(doc80, 60, 61, label ="PR_SURCH"),
   Span(doc80, 62, 63, label ="SURCHARGE"),
   Span(doc80, 65, 66, label ="PR_ESURCH"),
   Span(doc80, 67, 68, label ="ESURCHARGE"),
   Span(doc80, 68, 69, label ="TOTAL")]
docs.append(doc80)
print("doc81, 70, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 17000; AMOUNT 975; ARTICLE 6010008012; PRICE 153,69; UNIT 100; SUMMA 1.498,48; TARIFF 73079290; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 103,40; PR_ESURCH 3,50; ESURCHARGE 52,45; TOTAL 1.654; ")
doc81 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 17000 975 PC 6010008012 (*) 153,69 100 PC 1.498,48 FI-WEE-0 8LM-OR-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079290 Country of origin: Germany Material Surcharge 6,90 % 103,40 Energy Surcharge 3,50 % 52,45 1.654 ,33''')
doc81.ents = [
   Span(doc81, 3, 4, label ="NORDER"),
   Span(doc81, 9, 12, label ="CONTRACT"),
   Span(doc81, 12, 13, label ="CONTRACT1"),
   Span(doc81, 15, 16, label ="POS"),
   Span(doc81, 16, 17, label ="AMOUNT"),
   Span(doc81, 18, 19, label ="ARTICLE"),
   Span(doc81, 22, 23, label ="PRICE"),
   Span(doc81, 23, 24, label ="UNIT"),
   Span(doc81, 25, 26, label ="SUMMA"),
   Span(doc81, 51, 52, label ="TARIFF"),
   Span(doc81, 56, 57, label ="COUNTRY"),
   Span(doc81, 59, 60, label ="PR_SURCH"),
   Span(doc81, 61, 62, label ="SURCHARGE"),
   Span(doc81, 64, 65, label ="PR_ESURCH"),
   Span(doc81, 66, 67, label ="ESURCHARGE"),
   Span(doc81, 67, 68, label ="TOTAL")]
docs.append(doc81)
print("doc82, 69, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 17100; AMOUNT 600; ARTICLE 6010008016; PRICE 272,31; UNIT 100; SUMMA 1.633,86; TARIFF 73079290; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 112,74; PR_ESURCH 3,50; ESURCHARGE 57,19; TOTAL 1.803,79; ")
doc82 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 17100 600 PC 6010008016 (*) 272,31 100 PC 1.633,86 FI-WEE-1 8LM-OR-B-W3 packed per each item Product description: fitting    Export - Customs tariff no.: 73079290 Country of origin: Germany Material Surcharge 6,90 % 112,74 Energy Surcharge 3,50 % 57,19 1.803,79''')
doc82.ents = [
   Span(doc82, 3, 4, label ="NORDER"),
   Span(doc82, 9, 12, label ="CONTRACT"),
   Span(doc82, 12, 13, label ="CONTRACT1"),
   Span(doc82, 15, 16, label ="POS"),
   Span(doc82, 16, 17, label ="AMOUNT"),
   Span(doc82, 18, 19, label ="ARTICLE"),
   Span(doc82, 22, 23, label ="PRICE"),
   Span(doc82, 23, 24, label ="UNIT"),
   Span(doc82, 25, 26, label ="SUMMA"),
   Span(doc82, 52, 53, label ="TARIFF"),
   Span(doc82, 57, 58, label ="COUNTRY"),
   Span(doc82, 60, 61, label ="PR_SURCH"),
   Span(doc82, 62, 63, label ="SURCHARGE"),
   Span(doc82, 65, 66, label ="PR_ESURCH"),
   Span(doc82, 67, 68, label ="ESURCHARGE"),
   Span(doc82, 68, 69, label ="TOTAL")]
docs.append(doc82)
print("doc83, 67, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 17200; AMOUNT 200; ARTICLE 6010013788; PRICE 838,05; UNIT 100; SUMMA 1.676,10; TARIFF 73079290; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 115,65; PR_ESURCH 3,50; ESURCHARGE 58,66; TOTAL 1.850,41; ")
doc83 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 17200 200 PC 6010013788 (*) 838,05 100 PC 1.676,10 FI-WEE-28LM-OK-B-W3 packed per each item Product description: lug Export - Customs tariff no.: 73079290 Country of origin: Germany Material Surcharge 6,90 % 115,65 Energy Surcharge 3,50 % 58,66 1.850,41''')
doc83.ents = [
   Span(doc83, 3, 4, label ="NORDER"),
   Span(doc83, 9, 12, label ="CONTRACT"),
   Span(doc83, 12, 13, label ="CONTRACT1"),
   Span(doc83, 15, 16, label ="POS"),
   Span(doc83, 16, 17, label ="AMOUNT"),
   Span(doc83, 18, 19, label ="ARTICLE"),
   Span(doc83, 22, 23, label ="PRICE"),
   Span(doc83, 23, 24, label ="UNIT"),
   Span(doc83, 25, 26, label ="SUMMA"),
   Span(doc83, 50, 51, label ="TARIFF"),
   Span(doc83, 55, 56, label ="COUNTRY"),
   Span(doc83, 58, 59, label ="PR_SURCH"),
   Span(doc83, 60, 61, label ="SURCHARGE"),
   Span(doc83, 63, 64, label ="PR_ESURCH"),
   Span(doc83, 65, 66, label ="ESURCHARGE"),
   Span(doc83, 66, 67, label ="TOTAL")]
docs.append(doc83)
print("doc84, 67, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 17300; AMOUNT 13; ARTICLE 6020000130; PRICE 251,01; UNIT 100; SUMMA 32,63; TARIFF 73079290; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 2,25; PR_ESURCH 3,50; ESURCHARGE 1,14; TOTAL 36,02; ")
doc84 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 17300 13 PC 6020000130 (*) 251,01 100 PC 32,63 FI-WS-15L-W3-OGR-SKM packed per each item Product description: fitting Export - Customs tariff no.: 73079290 Country of origin: Germany Material Surcharge 6,90 % 2,25 Energy Surcharge 3,50 % 1,14 36,02''')
doc84.ents = [
   Span(doc84, 3, 4, label ="NORDER"),
   Span(doc84, 9, 12, label ="CONTRACT"),
   Span(doc84, 12, 13, label ="CONTRACT1"),
   Span(doc84, 15, 16, label ="POS"),
   Span(doc84, 16, 17, label ="AMOUNT"),
   Span(doc84, 18, 19, label ="ARTICLE"),
   Span(doc84, 22, 23, label ="PRICE"),
   Span(doc84, 23, 24, label ="UNIT"),
   Span(doc84, 25, 26, label ="SUMMA"),
   Span(doc84, 50, 51, label ="TARIFF"),
   Span(doc84, 55, 56, label ="COUNTRY"),
   Span(doc84, 58, 59, label ="PR_SURCH"),
   Span(doc84, 60, 61, label ="SURCHARGE"),
   Span(doc84, 63, 64, label ="PR_ESURCH"),
   Span(doc84, 65, 66, label ="ESURCHARGE"),
   Span(doc84, 66, 67, label ="TOTAL")]
docs.append(doc84)
print("doc85, 68, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 17400; AMOUNT 200; ARTICLE 6020000131; PRICE 343,04; UNIT 100; SUMMA 686,08; TARIFF 73079290; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 47,34; PR_ESURCH 3,50; ESURCHARGE 24,01; TOTAL 757,43; ")
doc85 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 17400 200 PC 6020000131 (*) 343,04 100 PC 686,08 FI-WS-18L-W3-OGR-SKM packed per each item Product description: fitting    Export - Customs tariff no.: 73079290 Country of origin: Germany Material Surcharge 6,90 % 47,34 Energy Surcharge 3,50 % 24,01 757,43''')
doc85.ents = [
   Span(doc85, 3, 4, label ="NORDER"),
   Span(doc85, 9, 12, label ="CONTRACT"),
   Span(doc85, 12, 13, label ="CONTRACT1"),
   Span(doc85, 15, 16, label ="POS"),
   Span(doc85, 16, 17, label ="AMOUNT"),
   Span(doc85, 18, 19, label ="ARTICLE"),
   Span(doc85, 22, 23, label ="PRICE"),
   Span(doc85, 23, 24, label ="UNIT"),
   Span(doc85, 25, 26, label ="SUMMA"),
   Span(doc85, 51, 52, label ="TARIFF"),
   Span(doc85, 56, 57, label ="COUNTRY"),
   Span(doc85, 59, 60, label ="PR_SURCH"),
   Span(doc85, 61, 62, label ="SURCHARGE"),
   Span(doc85, 64, 65, label ="PR_ESURCH"),
   Span(doc85, 66, 67, label ="ESURCHARGE"),
   Span(doc85, 67, 68, label ="TOTAL")]
docs.append(doc85)
print("doc86, 67, #NORDER 2390568; CONTRACT SR-1-06; CONTRACT1 1911; POS 17500; AMOUNT 10; ARTICLE 6020000132; PRICE 559,33; UNIT 100; SUMMA 55,93; TARIFF 73079290; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 3,86; PR_ESURCH 3,50; ESURCHARGE 1,96; TOTAL 61,75; ")
doc86 = nlp('''Order number: 2390568 Purchase order number: N SR-1-06 1911** 17500 10 PC 6020000132 (*) 559,33 100 PC 55,93 FI-WS-22L-W3-OGR-SKM packed per each item Product description: fitting Export - Customs tariff no.: 73079290 Country of origin: Germany Material Surcharge 6,90 % 3,86 Energy Surcharge 3,50 % 1,96 61,75''')
doc86.ents = [
   Span(doc86, 3, 4, label ="NORDER"),
   Span(doc86, 9, 12, label ="CONTRACT"),
   Span(doc86, 12, 13, label ="CONTRACT1"),
   Span(doc86, 15, 16, label ="POS"),
   Span(doc86, 16, 17, label ="AMOUNT"),
   Span(doc86, 18, 19, label ="ARTICLE"),
   Span(doc86, 22, 23, label ="PRICE"),
   Span(doc86, 23, 24, label ="UNIT"),
   Span(doc86, 25, 26, label ="SUMMA"),
   Span(doc86, 50, 51, label ="TARIFF"),
   Span(doc86, 55, 56, label ="COUNTRY"),
   Span(doc86, 58, 59, label ="PR_SURCH"),
   Span(doc86, 60, 61, label ="SURCHARGE"),
   Span(doc86, 63, 64, label ="PR_ESURCH"),
   Span(doc86, 65, 66, label ="ESURCHARGE"),
   Span(doc86, 66, 67, label ="TOTAL")]
docs.append(doc86)
print("doc88, 75, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 17700; AMOUNT 5.000; ARTICLE 1130023863; PRICE 5,47; UNIT 100; SUMMA 273,50; TARIFF 73181588; COUNTRY Origin unknown; PR_SURCH 11,40; SURCHARGE 31,18; PR_ESURCH 3,50; ESURCHARGE 9,57; TOTAL 314,25; ")
doc88 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915** 17700 5.000 PC 1130023863 5,47 100 PC 273,50 AS-M8x28-DIN931/933-8.8-W3 AS-M8X28-DIN931/933-8.8-W3 packed per each item    Product description: screw Export - Customs tariff no.: 73181588 Country of origin: Origin unknown Material Surcharge 11,40 % 31,18 Energy Surcharge 3,50 % 9,57 314,25''')
doc88.ents = [
   Span(doc88, 3, 4, label ="NORDER"),
   Span(doc88, 9, 12, label ="CONTRACT"),
   Span(doc88, 12, 13, label ="CONTRACT1"),
   Span(doc88, 15, 16, label ="POS"),
   Span(doc88, 16, 17, label ="AMOUNT"),
   Span(doc88, 18, 19, label ="ARTICLE"),
   Span(doc88, 19, 20, label ="PRICE"),
   Span(doc88, 20, 21, label ="UNIT"),
   Span(doc88, 22, 23, label ="SUMMA"),
   Span(doc88, 57, 58, label ="TARIFF"),
   Span(doc88, 62, 64, label ="COUNTRY"),
   Span(doc88, 66, 67, label ="PR_SURCH"),
   Span(doc88, 68, 69, label ="SURCHARGE"),
   Span(doc88, 71, 72, label ="PR_ESURCH"),
   Span(doc88, 73, 74, label ="ESURCHARGE"),
   Span(doc88, 74, 75, label ="TOTAL")]
docs.append(doc88)
print("doc89, 73, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 17800; AMOUNT 150; ARTICLE 1130004281; PRICE 4,19; UNIT 100; SUMMA 6,29; TARIFF 73181588; COUNTRY Thailand; PR_SURCH 11,40; SURCHARGE 0,72; PR_ESURCH 3,50; ESURCHARGE 0,22; TOTAL 7,23; ")
doc89 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915** 17800 150 PC 1130004281 4,19 100 PC 6,29 AS-M8x45-DIN931/933-8.8-W3 AS-M8X45-DIN931/933-8.8-W3 packed per each item Product description: screw Export - Customs tariff no.: 73181588 Country of origin: Thailand Material Surcharge 11,40 % 0,72 Energy Surcharge 3,50 % 0,22 7,23''')
doc89.ents = [
   Span(doc89, 3, 4, label ="NORDER"),
   Span(doc89, 9, 12, label ="CONTRACT"),
   Span(doc89, 12, 13, label ="CONTRACT1"),
   Span(doc89, 15, 16, label ="POS"),
   Span(doc89, 16, 17, label ="AMOUNT"),
   Span(doc89, 18, 19, label ="ARTICLE"),
   Span(doc89, 19, 20, label ="PRICE"),
   Span(doc89, 20, 21, label ="UNIT"),
   Span(doc89, 22, 23, label ="SUMMA"),
   Span(doc89, 56, 57, label ="TARIFF"),
   Span(doc89, 61, 62, label ="COUNTRY"),
   Span(doc89, 64, 65, label ="PR_SURCH"),
   Span(doc89, 66, 67, label ="SURCHARGE"),
   Span(doc89, 69, 70, label ="PR_ESURCH"),
   Span(doc89, 71, 72, label ="ESURCHARGE"),
   Span(doc89, 72, 73, label ="TOTAL")]
docs.append(doc89)
print("doc90, 76, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 17900; AMOUNT 600; ARTICLE 1730002340; PRICE 2,24; UNIT 1; SUMMA 1.344,00; TARIFF 73181568; COUNTRY Taiwan; PR_SURCH 15,50; SURCHARGE 208,32; PR_ESURCH 3,50; ESURCHARGE 47,04; TOTAL 1.599,36; ")
doc90 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915** 17900 600 PC 1730002340 2,24 1 PC 1.344,00 IS-1/2-1 3 UNCx3 -3/4-AB18.3-GR8-W1 IS-1/2-13x3#3/4UNC-AB18.3-GR8-W1 packed per each item Product description: screw Export - Customs tariff no.: 73181568 Country of origin: Taiwan Material Surcharge 15,50 % 208,32 Energy Surcharge 3,50 % 47,04 1.599,36''')
doc90.ents = [
   Span(doc90, 3, 4, label ="NORDER"),
   Span(doc90, 9, 12, label ="CONTRACT"),
   Span(doc90, 12, 13, label ="CONTRACT1"),
   Span(doc90, 15, 16, label ="POS"),
   Span(doc90, 16, 17, label ="AMOUNT"),
   Span(doc90, 18, 19, label ="ARTICLE"),
   Span(doc90, 19, 20, label ="PRICE"),
   Span(doc90, 20, 21, label ="UNIT"),
   Span(doc90, 22, 23, label ="SUMMA"),
   Span(doc90, 59, 60, label ="TARIFF"),
   Span(doc90, 64, 65, label ="COUNTRY"),
   Span(doc90, 67, 68, label ="PR_SURCH"),
   Span(doc90, 69, 70, label ="SURCHARGE"),
   Span(doc90, 72, 73, label ="PR_ESURCH"),
   Span(doc90, 74, 75, label ="ESURCHARGE"),
   Span(doc90, 75, 76, label ="TOTAL")]
docs.append(doc90)
print("doc91, 66, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 18000; AMOUNT 100; ARTICLE 1130004134; PRICE 13,46; UNIT 100; SUMMA 13,46; TARIFF 73181568; COUNTRY Origin unknown; PR_SURCH 11,40; SURCHARGE 1,53; PR_ESURCH 3,50; ESURCHARGE 0,47; TOTAL 15,46; ")
doc91 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915** 18000 100 PC 1130004134 13,46 100 PC 13,46    IS-M10X30-ISO4762-8.8-W3 packed per each item Product description: screw Export - Customs tariff no.: 73181568 Country of origin: Origin unknown Material Surcharge 11,40 % 1,53 Energy Surcharge 3,50 % 0,47 15,46''')
doc91.ents = [
   Span(doc91, 3, 4, label ="NORDER"),
   Span(doc91, 9, 12, label ="CONTRACT"),
   Span(doc91, 12, 13, label ="CONTRACT1"),
   Span(doc91, 15, 16, label ="POS"),
   Span(doc91, 16, 17, label ="AMOUNT"),
   Span(doc91, 18, 19, label ="ARTICLE"),
   Span(doc91, 19, 20, label ="PRICE"),
   Span(doc91, 20, 21, label ="UNIT"),
   Span(doc91, 22, 23, label ="SUMMA"),
   Span(doc91, 48, 49, label ="TARIFF"),
   Span(doc91, 53, 55, label ="COUNTRY"),
   Span(doc91, 57, 58, label ="PR_SURCH"),
   Span(doc91, 59, 60, label ="SURCHARGE"),
   Span(doc91, 62, 63, label ="PR_ESURCH"),
   Span(doc91, 64, 65, label ="ESURCHARGE"),
   Span(doc91, 65, 66, label ="TOTAL")]
docs.append(doc91)
print("doc92, 64, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 18100; AMOUNT 700; ARTICLE 1130022370; PRICE 12,30; UNIT 100; SUMMA 86,10; TARIFF 73181568; COUNTRY Philippines; PR_SURCH 11,40; SURCHARGE 9,82; PR_ESURCH 3,50; ESURCHARGE 3,01; TOTAL 98,93; ")
doc92 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915** 18100 700 PC 1130022370 12,30 100 PC 86,10 IS-M10X35-ISO4762-8.8-W3 packed per each item Product description: screw Export - Customs tariff no.: 73181568 Country of origin: Philippines Material Surcharge 11,40 % 9,82 Energy Surcharge 3,50 % 3,01 98,93''')
doc92.ents = [
   Span(doc92, 3, 4, label ="NORDER"),
   Span(doc92, 9, 12, label ="CONTRACT"),
   Span(doc92, 12, 13, label ="CONTRACT1"),
   Span(doc92, 15, 16, label ="POS"),
   Span(doc92, 16, 17, label ="AMOUNT"),
   Span(doc92, 18, 19, label ="ARTICLE"),
   Span(doc92, 19, 20, label ="PRICE"),
   Span(doc92, 20, 21, label ="UNIT"),
   Span(doc92, 22, 23, label ="SUMMA"),
   Span(doc92, 47, 48, label ="TARIFF"),
   Span(doc92, 52, 53, label ="COUNTRY"),
   Span(doc92, 55, 56, label ="PR_SURCH"),
   Span(doc92, 57, 58, label ="SURCHARGE"),
   Span(doc92, 60, 61, label ="PR_ESURCH"),
   Span(doc92, 62, 63, label ="ESURCHARGE"),
   Span(doc92, 63, 64, label ="TOTAL")]
docs.append(doc92)
print("doc93, 74, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 18200; AMOUNT 50; ARTICLE 1210026027; PRICE 3,86; UNIT 1; SUMMA 193,00; TARIFF 84818073; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 22,00; PR_ESURCH 3,50; ESURCHARGE 6,76; TOTAL 221,76; ")
doc93 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915** 18200 50 PC 1210026027 (*) 3,86 1 PC 193,00 SMK-20-08L-B-K-W3 SMK20-08L-PK-C6F packed per each item Product description: coupling Export - Customs tariff no.: 84818073 Country of origin: Germany Material Surcharge 11,40 % 22,00 Energy Surcharge 3,50 % 6,76 221,76''')
doc93.ents = [
   Span(doc93, 3, 4, label ="NORDER"),
   Span(doc93, 9, 12, label ="CONTRACT"),
   Span(doc93, 12, 13, label ="CONTRACT1"),
   Span(doc93, 15, 16, label ="POS"),
   Span(doc93, 16, 17, label ="AMOUNT"),
   Span(doc93, 18, 19, label ="ARTICLE"),
   Span(doc93, 22, 23, label ="PRICE"),
   Span(doc93, 23, 24, label ="UNIT"),
   Span(doc93, 25, 26, label ="SUMMA"),
   Span(doc93, 57, 58, label ="TARIFF"),
   Span(doc93, 62, 63, label ="COUNTRY"),
   Span(doc93, 65, 66, label ="PR_SURCH"),
   Span(doc93, 67, 68, label ="SURCHARGE"),
   Span(doc93, 70, 71, label ="PR_ESURCH"),
   Span(doc93, 72, 73, label ="ESURCHARGE"),
   Span(doc93, 73, 74, label ="TOTAL")]
docs.append(doc93)
print("doc94, 75, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 18300; AMOUNT 1.400; ARTICLE 1210026041; PRICE 4,72; UNIT 1; SUMMA 6.608,00; TARIFF 84818073; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 753,31; PR_ESURCH 3,50; ESURCHARGE 231,28; TOTAL 7.592,59; ")
doc94 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915**   18300 1.400 PC 1210026041 (*) 4,72 1 PC 6.608,00 SMK-20-12L-B-K-W3 SMK20-12L-PK-C6F packed per each item Product description: coupling Export - Customs tariff no.: 84818073 Country of origin: Germany Material Surcharge 11,40 % 753,31 Energy Surcharge 3,50 % 231,28 7.592,59''')
doc94.ents = [
   Span(doc94, 3, 4, label ="NORDER"),
   Span(doc94, 9, 12, label ="CONTRACT"),
   Span(doc94, 12, 13, label ="CONTRACT1"),
   Span(doc94, 16, 17, label ="POS"),
   Span(doc94, 17, 18, label ="AMOUNT"),
   Span(doc94, 19, 20, label ="ARTICLE"),
   Span(doc94, 23, 24, label ="PRICE"),
   Span(doc94, 24, 25, label ="UNIT"),
   Span(doc94, 26, 27, label ="SUMMA"),
   Span(doc94, 58, 59, label ="TARIFF"),
   Span(doc94, 63, 64, label ="COUNTRY"),
   Span(doc94, 66, 67, label ="PR_SURCH"),
   Span(doc94, 68, 69, label ="SURCHARGE"),
   Span(doc94, 71, 72, label ="PR_ESURCH"),
   Span(doc94, 73, 74, label ="ESURCHARGE"),
   Span(doc94, 74, 75, label ="TOTAL")]
docs.append(doc94)
print("doc95, 62, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 18400; AMOUNT 150; ARTICLE 1130000261; PRICE 5,49; UNIT 100; SUMMA 8,24; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,94; PR_ESURCH 3,50; ESURCHARGE 0,29; TOTAL 9,47; ")
doc95 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915** 18400 150 PC 1130000261 5,49 100 PC 8,24 DP-2-W3 DP 2 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 0,94 Energy Surcharge 3,50 % 0,29 9,47''')
doc95.ents = [
   Span(doc95, 3, 4, label ="NORDER"),
   Span(doc95, 9, 12, label ="CONTRACT"),
   Span(doc95, 12, 13, label ="CONTRACT1"),
   Span(doc95, 15, 16, label ="POS"),
   Span(doc95, 16, 17, label ="AMOUNT"),
   Span(doc95, 18, 19, label ="ARTICLE"),
   Span(doc95, 19, 20, label ="PRICE"),
   Span(doc95, 20, 21, label ="UNIT"),
   Span(doc95, 22, 23, label ="SUMMA"),
   Span(doc95, 45, 46, label ="TARIFF"),
   Span(doc95, 50, 51, label ="COUNTRY"),
   Span(doc95, 53, 54, label ="PR_SURCH"),
   Span(doc95, 55, 56, label ="SURCHARGE"),
   Span(doc95, 58, 59, label ="PR_ESURCH"),
   Span(doc95, 60, 61, label ="ESURCHARGE"),
   Span(doc95, 61, 62, label ="TOTAL")]
docs.append(doc95)
print("doc96, 63, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 18500; AMOUNT 2.300; ARTICLE 1130000267; PRICE 7,25; UNIT 100; SUMMA 166,75; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 19,01; PR_ESURCH 3,50; ESURCHARGE 5,84; TOTAL 191,60; ")
doc96 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915** 18500 2.300 PC 1130000267 7,25 100 PC 166,75 DP-4-W3 DP 4 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 19,01 Energy Surcharge 3,50 % 5,84 191,60    ''')
doc96.ents = [
   Span(doc96, 3, 4, label ="NORDER"),
   Span(doc96, 9, 12, label ="CONTRACT"),
   Span(doc96, 12, 13, label ="CONTRACT1"),
   Span(doc96, 15, 16, label ="POS"),
   Span(doc96, 16, 17, label ="AMOUNT"),
   Span(doc96, 18, 19, label ="ARTICLE"),
   Span(doc96, 19, 20, label ="PRICE"),
   Span(doc96, 20, 21, label ="UNIT"),
   Span(doc96, 22, 23, label ="SUMMA"),
   Span(doc96, 45, 46, label ="TARIFF"),
   Span(doc96, 50, 51, label ="COUNTRY"),
   Span(doc96, 53, 54, label ="PR_SURCH"),
   Span(doc96, 55, 56, label ="SURCHARGE"),
   Span(doc96, 58, 59, label ="PR_ESURCH"),
   Span(doc96, 60, 61, label ="ESURCHARGE"),
   Span(doc96, 61, 62, label ="TOTAL")]
docs.append(doc96)
print("doc97, 62, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 18600; AMOUNT 4.800; ARTICLE 1130000269; PRICE 8,76; UNIT 100; SUMMA 420,48; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 47,93; PR_ESURCH 3,50; ESURCHARGE 14,72; TOTAL 483,13; ")
doc97 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915** 18600 4.800 PC 1130000269 8,76 100 PC 420,48 DP-5-W3 DP 5 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 47,93 Energy Surcharge 3,50 % 14,72 483,13''')
doc97.ents = [
   Span(doc97, 3, 4, label ="NORDER"),
   Span(doc97, 9, 12, label ="CONTRACT"),
   Span(doc97, 12, 13, label ="CONTRACT1"),
   Span(doc97, 15, 16, label ="POS"),
   Span(doc97, 16, 17, label ="AMOUNT"),
   Span(doc97, 18, 19, label ="ARTICLE"),
   Span(doc97, 19, 20, label ="PRICE"),
   Span(doc97, 20, 21, label ="UNIT"),
   Span(doc97, 22, 23, label ="SUMMA"),
   Span(doc97, 45, 46, label ="TARIFF"),
   Span(doc97, 50, 51, label ="COUNTRY"),
   Span(doc97, 53, 54, label ="PR_SURCH"),
   Span(doc97, 55, 56, label ="SURCHARGE"),
   Span(doc97, 58, 59, label ="PR_ESURCH"),
   Span(doc97, 60, 61, label ="ESURCHARGE"),
   Span(doc97, 61, 62, label ="TOTAL")]
docs.append(doc97)
print("doc98, 62, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 18700; AMOUNT 900; ARTICLE 1130000273; PRICE 14,05; UNIT 100; SUMMA 126,45; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 14,42; PR_ESURCH 3,50; ESURCHARGE 4,43; TOTAL 145,30; ")
doc98 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915** 18700 900 PC 1130000273 14,05 100 PC 126,45 DP-6-W3 DP 6 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 14,42 Energy Surcharge 3,50 % 4,43 145,30''')
doc98.ents = [
   Span(doc98, 3, 4, label ="NORDER"),
   Span(doc98, 9, 12, label ="CONTRACT"),
   Span(doc98, 12, 13, label ="CONTRACT1"),
   Span(doc98, 15, 16, label ="POS"),
   Span(doc98, 16, 17, label ="AMOUNT"),
   Span(doc98, 18, 19, label ="ARTICLE"),
   Span(doc98, 19, 20, label ="PRICE"),
   Span(doc98, 20, 21, label ="UNIT"),
   Span(doc98, 22, 23, label ="SUMMA"),
   Span(doc98, 45, 46, label ="TARIFF"),
   Span(doc98, 50, 51, label ="COUNTRY"),
   Span(doc98, 53, 54, label ="PR_SURCH"),
   Span(doc98, 55, 56, label ="SURCHARGE"),
   Span(doc98, 58, 59, label ="PR_ESURCH"),
   Span(doc98, 60, 61, label ="ESURCHARGE"),
   Span(doc98, 61, 62, label ="TOTAL")]
docs.append(doc98)
print("doc99, 63, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 18800; AMOUNT 2.000; ARTICLE 1130001959; PRICE 5,12; UNIT 100; SUMMA 102,40; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 11,67; PR_ESURCH 3,50; ESURCHARGE 3,58; TOTAL 117,65; ")
doc99 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915** 18800 2.000 PC 1130001959 5,12 100 PC 102,40 DPL-2-W3 DPL 2 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 11,67   Energy Surcharge 3,50 % 3,58 117,65''')
doc99.ents = [
   Span(doc99, 3, 4, label ="NORDER"),
   Span(doc99, 9, 12, label ="CONTRACT"),
   Span(doc99, 12, 13, label ="CONTRACT1"),
   Span(doc99, 15, 16, label ="POS"),
   Span(doc99, 16, 17, label ="AMOUNT"),
   Span(doc99, 18, 19, label ="ARTICLE"),
   Span(doc99, 19, 20, label ="PRICE"),
   Span(doc99, 20, 21, label ="UNIT"),
   Span(doc99, 22, 23, label ="SUMMA"),
   Span(doc99, 45, 46, label ="TARIFF"),
   Span(doc99, 50, 51, label ="COUNTRY"),
   Span(doc99, 53, 54, label ="PR_SURCH"),
   Span(doc99, 55, 56, label ="SURCHARGE"),
   Span(doc99, 59, 60, label ="PR_ESURCH"),
   Span(doc99, 61, 62, label ="ESURCHARGE"),
   Span(doc99, 62, 63, label ="TOTAL")]
docs.append(doc99)
print("doc100, 62, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 18900; AMOUNT 600; ARTICLE 1130001960; PRICE 5,65; UNIT 100; SUMMA 33,90; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 3,86; PR_ESURCH 3,50; ESURCHARGE 1,19; TOTAL 38,95; ")
doc100 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915** 18900 600 PC 1130001960 5,65 100 PC 33,90 DPL-3-W3 DPL 3 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 3,86 Energy Surcharge 3,50 % 1,19 38,95''')
doc100.ents = [
   Span(doc100, 3, 4, label ="NORDER"),
   Span(doc100, 9, 12, label ="CONTRACT"),
   Span(doc100, 12, 13, label ="CONTRACT1"),
   Span(doc100, 15, 16, label ="POS"),
   Span(doc100, 16, 17, label ="AMOUNT"),
   Span(doc100, 18, 19, label ="ARTICLE"),
   Span(doc100, 19, 20, label ="PRICE"),
   Span(doc100, 20, 21, label ="UNIT"),
   Span(doc100, 22, 23, label ="SUMMA"),
   Span(doc100, 45, 46, label ="TARIFF"),
   Span(doc100, 50, 51, label ="COUNTRY"),
   Span(doc100, 53, 54, label ="PR_SURCH"),
   Span(doc100, 55, 56, label ="SURCHARGE"),
   Span(doc100, 58, 59, label ="PR_ESURCH"),
   Span(doc100, 60, 61, label ="ESURCHARGE"),
   Span(doc100, 61, 62, label ="TOTAL")]
docs.append(doc100)
print("doc101, 62, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 19000; AMOUNT 900; ARTICLE 1130001961; PRICE 6,49; UNIT 100; SUMMA 58,41; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 6,66; PR_ESURCH 3,50; ESURCHARGE 2,04; TOTAL 67,11; ")
doc101 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915** 19000 900 PC 1130001961 6,49 100 PC 58,41 DPL-4-W3 DPL 4 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 6,66 Energy Surcharge 3,50 % 2,04 67,11''')
doc101.ents = [
   Span(doc101, 3, 4, label ="NORDER"),
   Span(doc101, 9, 12, label ="CONTRACT"),
   Span(doc101, 12, 13, label ="CONTRACT1"),
   Span(doc101, 15, 16, label ="POS"),
   Span(doc101, 16, 17, label ="AMOUNT"),
   Span(doc101, 18, 19, label ="ARTICLE"),
   Span(doc101, 19, 20, label ="PRICE"),
   Span(doc101, 20, 21, label ="UNIT"),
   Span(doc101, 22, 23, label ="SUMMA"),
   Span(doc101, 45, 46, label ="TARIFF"),
   Span(doc101, 50, 51, label ="COUNTRY"),
   Span(doc101, 53, 54, label ="PR_SURCH"),
   Span(doc101, 55, 56, label ="SURCHARGE"),
   Span(doc101, 58, 59, label ="PR_ESURCH"),
   Span(doc101, 60, 61, label ="ESURCHARGE"),
   Span(doc101, 61, 62, label ="TOTAL")]
docs.append(doc101)
print("doc102, 77, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 19100; AMOUNT 9.400; ARTICLE 1130022187; PRICE 16,01; UNIT 100; SUMMA 1.504; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 171,56; PR_ESURCH 3,50; ESURCHARGE 52,67; TOTAL 1.729,17; ")
doc102 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915** 19100 9.400 PC 1130022187 16,01 100 PC 1.504 ,94 LBBU-DP-1 D-M8/U5/16-W3 LBBU-DP 1D M8-U5/16 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098    Country of origin: Germany Material Surcharge 11,40 % 171,56 Energy Surcharge 3,50 % 52,67 1.729,17''')
doc102.ents = [
   Span(doc102, 3, 4, label ="NORDER"),
   Span(doc102, 9, 12, label ="CONTRACT"),
   Span(doc102, 12, 13, label ="CONTRACT1"),
   Span(doc102, 15, 16, label ="POS"),
   Span(doc102, 16, 17, label ="AMOUNT"),
   Span(doc102, 18, 19, label ="ARTICLE"),
   Span(doc102, 19, 20, label ="PRICE"),
   Span(doc102, 20, 21, label ="UNIT"),
   Span(doc102, 22, 23, label ="SUMMA"),
   Span(doc102, 59, 60, label ="TARIFF"),
   Span(doc102, 65, 66, label ="COUNTRY"),
   Span(doc102, 68, 69, label ="PR_SURCH"),
   Span(doc102, 70, 71, label ="SURCHARGE"),
   Span(doc102, 73, 74, label ="PR_ESURCH"),
   Span(doc102, 75, 76, label ="ESURCHARGE"),
   Span(doc102, 76, 77, label ="TOTAL")]
docs.append(doc102)
print("doc103, 72, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 19200; AMOUNT 5.700; ARTICLE 1130022183; PRICE 13,82; UNIT 100; SUMMA 787,74; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 89,80; PR_ESURCH 3,50; ESURCHARGE 27,57; TOTAL 905,11; ")
doc103 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915** 19200 5.700 PC 1130022183 13,82 100 PC 787,74 LBBU-DP-1 -M8/U5/16-W3 LBBU-DP 1 M8-U5/16 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 89,80 Energy Surcharge 3,50 % 27,57 905,11''')
doc103.ents = [
   Span(doc103, 3, 4, label ="NORDER"),
   Span(doc103, 9, 12, label ="CONTRACT"),
   Span(doc103, 12, 13, label ="CONTRACT1"),
   Span(doc103, 15, 16, label ="POS"),
   Span(doc103, 16, 17, label ="AMOUNT"),
   Span(doc103, 18, 19, label ="ARTICLE"),
   Span(doc103, 19, 20, label ="PRICE"),
   Span(doc103, 20, 21, label ="UNIT"),
   Span(doc103, 22, 23, label ="SUMMA"),
   Span(doc103, 55, 56, label ="TARIFF"),
   Span(doc103, 60, 61, label ="COUNTRY"),
   Span(doc103, 63, 64, label ="PR_SURCH"),
   Span(doc103, 65, 66, label ="SURCHARGE"),
   Span(doc103, 68, 69, label ="PR_ESURCH"),
   Span(doc103, 70, 71, label ="ESURCHARGE"),
   Span(doc103, 71, 72, label ="TOTAL")]
docs.append(doc103)
print("doc104, 73, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 19300; AMOUNT 11.500; ARTICLE 1130022189; PRICE 17,47; UNIT 100; SUMMA 2.009,05; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 229,03; PR_ESURCH 3,50; ESURCHARGE 70,32; TOTAL 2.308,40; ")
doc104 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915** 19300 11.500 PC 1130022189 17,47 100 PC 2.009,05 LBBU-DP-2D-M8/U5/16-W3 LBBU-DP 2D M8-U5/16 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 229,03 Energy Surcharge 3,50 % 70,32 2.308,40''')
doc104.ents = [
   Span(doc104, 3, 4, label ="NORDER"),
   Span(doc104, 9, 12, label ="CONTRACT"),
   Span(doc104, 12, 13, label ="CONTRACT1"),
   Span(doc104, 15, 16, label ="POS"),
   Span(doc104, 16, 17, label ="AMOUNT"),
   Span(doc104, 18, 19, label ="ARTICLE"),
   Span(doc104, 19, 20, label ="PRICE"),
   Span(doc104, 20, 21, label ="UNIT"),
   Span(doc104, 22, 23, label ="SUMMA"),
   Span(doc104, 56, 57, label ="TARIFF"),
   Span(doc104, 61, 62, label ="COUNTRY"),
   Span(doc104, 64, 65, label ="PR_SURCH"),
   Span(doc104, 66, 67, label ="SURCHARGE"),
   Span(doc104, 69, 70, label ="PR_ESURCH"),
   Span(doc104, 71, 72, label ="ESURCHARGE"),
   Span(doc104, 72, 73, label ="TOTAL")]
docs.append(doc104)
print("doc105, 74, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 19400; AMOUNT 3.900; ARTICLE 1130022185; PRICE 14,54; UNIT 100; SUMMA 567,06; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 64,64; PR_ESURCH 3,50; ESURCHARGE 19,85; TOTAL 651,55; ")
doc105 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915** 19400 3.900 PC 1130022185 14,54 100 PC 567,06 LBBU-DP-2-M8/U5/16-W3 LBBU-DP 2 M8-U5/16 W3    packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 64,64 Energy Surcharge 3,50 % 19,85 651,55''')
doc105.ents = [
   Span(doc105, 3, 4, label ="NORDER"),
   Span(doc105, 9, 12, label ="CONTRACT"),
   Span(doc105, 12, 13, label ="CONTRACT1"),
   Span(doc105, 15, 16, label ="POS"),
   Span(doc105, 16, 17, label ="AMOUNT"),
   Span(doc105, 18, 19, label ="ARTICLE"),
   Span(doc105, 19, 20, label ="PRICE"),
   Span(doc105, 20, 21, label ="UNIT"),
   Span(doc105, 22, 23, label ="SUMMA"),
   Span(doc105, 57, 58, label ="TARIFF"),
   Span(doc105, 62, 63, label ="COUNTRY"),
   Span(doc105, 65, 66, label ="PR_SURCH"),
   Span(doc105, 67, 68, label ="SURCHARGE"),
   Span(doc105, 70, 71, label ="PR_ESURCH"),
   Span(doc105, 72, 73, label ="ESURCHARGE"),
   Span(doc105, 73, 74, label ="TOTAL")]
docs.append(doc105)
print("doc106, 73, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 19500; AMOUNT 1.500; ARTICLE 1130024605; PRICE 46,52; UNIT 100; SUMMA 697,80; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 79,55; PR_ESURCH 3,50; ESURCHARGE 24,42; TOTAL 801,77; ")
doc106 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915** 19500 1.500 PC 1130024605 46,52 100 PC 697,80 LBBU-DP-3D-M8/U5/16-W3 LBBU-DP 3D M8-U5/16 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 79,55 Energy Surcharge 3,50 % 24,42 801,77''')
doc106.ents = [
   Span(doc106, 3, 4, label ="NORDER"),
   Span(doc106, 9, 12, label ="CONTRACT"),
   Span(doc106, 12, 13, label ="CONTRACT1"),
   Span(doc106, 15, 16, label ="POS"),
   Span(doc106, 16, 17, label ="AMOUNT"),
   Span(doc106, 18, 19, label ="ARTICLE"),
   Span(doc106, 19, 20, label ="PRICE"),
   Span(doc106, 20, 21, label ="UNIT"),
   Span(doc106, 22, 23, label ="SUMMA"),
   Span(doc106, 56, 57, label ="TARIFF"),
   Span(doc106, 61, 62, label ="COUNTRY"),
   Span(doc106, 64, 65, label ="PR_SURCH"),
   Span(doc106, 66, 67, label ="SURCHARGE"),
   Span(doc106, 69, 70, label ="PR_ESURCH"),
   Span(doc106, 71, 72, label ="ESURCHARGE"),
   Span(doc106, 72, 73, label ="TOTAL")]
docs.append(doc106)
print("doc107, 73, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 19600; AMOUNT 1.300; ARTICLE 1130024678; PRICE 37,43; UNIT 100; SUMMA 486,59; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 55,47; PR_ESURCH 3,50; ESURCHARGE 17,03; TOTAL 559,09; ")
doc107 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915** 19600 1.300 PC 1130024678 37,43 100 PC 486,59 LBBU-DP-3-M8/U5/16-W3 LBBU-DP 3 M8-U5/16 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 55,47 Energy Surcharge 3,50 % 17,03 559,09''')
doc107.ents = [
   Span(doc107, 3, 4, label ="NORDER"),
   Span(doc107, 9, 12, label ="CONTRACT"),
   Span(doc107, 12, 13, label ="CONTRACT1"),
   Span(doc107, 15, 16, label ="POS"),
   Span(doc107, 16, 17, label ="AMOUNT"),
   Span(doc107, 18, 19, label ="ARTICLE"),
   Span(doc107, 19, 20, label ="PRICE"),
   Span(doc107, 20, 21, label ="UNIT"),
   Span(doc107, 22, 23, label ="SUMMA"),
   Span(doc107, 56, 57, label ="TARIFF"),
   Span(doc107, 61, 62, label ="COUNTRY"),
   Span(doc107, 64, 65, label ="PR_SURCH"),
   Span(doc107, 66, 67, label ="SURCHARGE"),
   Span(doc107, 69, 70, label ="PR_ESURCH"),
   Span(doc107, 71, 72, label ="ESURCHARGE"),
   Span(doc107, 72, 73, label ="TOTAL")]
docs.append(doc107)
print("doc108, 63, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 19700; AMOUNT 25; ARTICLE 1130000441; PRICE 5,67; UNIT 100; SUMMA 1,42; TARIFF 73182100; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,16; PR_ESURCH 3,50; ESURCHARGE 0,05; TOTAL 1,63; ")
doc108 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915**    19700 25 PC 1130000441 5,67 100 PC 1,42 SIG-4-W3 SIG 4 W3 packed per each item Product description: locking plate Export - Customs tariff no.: 73182100 Country of origin: Germany Material Surcharge 11,40 % 0,16 Energy Surcharge 3,50 % 0,05 1,63''')
doc108.ents = [
   Span(doc108, 3, 4, label ="NORDER"),
   Span(doc108, 9, 12, label ="CONTRACT"),
   Span(doc108, 12, 13, label ="CONTRACT1"),
   Span(doc108, 16, 17, label ="POS"),
   Span(doc108, 17, 18, label ="AMOUNT"),
   Span(doc108, 19, 20, label ="ARTICLE"),
   Span(doc108, 20, 21, label ="PRICE"),
   Span(doc108, 21, 22, label ="UNIT"),
   Span(doc108, 23, 24, label ="SUMMA"),
   Span(doc108, 46, 47, label ="TARIFF"),
   Span(doc108, 51, 52, label ="COUNTRY"),
   Span(doc108, 54, 55, label ="PR_SURCH"),
   Span(doc108, 56, 57, label ="SURCHARGE"),
   Span(doc108, 59, 60, label ="PR_ESURCH"),
   Span(doc108, 61, 62, label ="ESURCHARGE"),
   Span(doc108, 62, 63, label ="TOTAL")]
docs.append(doc108)
print("doc109, 67, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 19800; AMOUNT 25; ARTICLE 1120001284; PRICE 66,22; UNIT 100; SUMMA 16,56; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 1,89; PR_ESURCH 3,50; ESURCHARGE 0,58; TOTAL 19,03; ")
doc109 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915** 19800 25 PC 1120001284 66,22 100 PC 16,56 DSP-4-60-M-W2 DSP 4/60 M W2 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 1,89 Energy Surcharge 3,50 % 0,58 19,03''')
doc109.ents = [
   Span(doc109, 3, 4, label ="NORDER"),
   Span(doc109, 9, 12, label ="CONTRACT"),
   Span(doc109, 12, 13, label ="CONTRACT1"),
   Span(doc109, 15, 16, label ="POS"),
   Span(doc109, 16, 17, label ="AMOUNT"),
   Span(doc109, 18, 19, label ="ARTICLE"),
   Span(doc109, 19, 20, label ="PRICE"),
   Span(doc109, 20, 21, label ="UNIT"),
   Span(doc109, 22, 23, label ="SUMMA"),
   Span(doc109, 50, 51, label ="TARIFF"),
   Span(doc109, 55, 56, label ="COUNTRY"),
   Span(doc109, 58, 59, label ="PR_SURCH"),
   Span(doc109, 60, 61, label ="SURCHARGE"),
   Span(doc109, 63, 64, label ="PR_ESURCH"),
   Span(doc109, 65, 66, label ="ESURCHARGE"),
   Span(doc109, 66, 67, label ="TOTAL")]
docs.append(doc109)
print("doc110, 70, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 19900; AMOUNT 3.000; ARTICLE 1120021040; PRICE 29,26; UNIT 100; SUMMA 877,80; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 100,07; PR_ESURCH 3,50; ESURCHARGE 30,72; TOTAL 1.008,59; ")
doc110 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915** 19900 3.000 PC 1120021040 29,26 100 PC 877,80 LBBU-SP-1D-M8-W2 LBBU-SP 1D M8 W2 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 100,07 Energy Surcharge 3,50 % 30,72 1.008,59   ''')
doc110.ents = [
   Span(doc110, 3, 4, label ="NORDER"),
   Span(doc110, 9, 12, label ="CONTRACT"),
   Span(doc110, 12, 13, label ="CONTRACT1"),
   Span(doc110, 15, 16, label ="POS"),
   Span(doc110, 16, 17, label ="AMOUNT"),
   Span(doc110, 18, 19, label ="ARTICLE"),
   Span(doc110, 19, 20, label ="PRICE"),
   Span(doc110, 20, 21, label ="UNIT"),
   Span(doc110, 22, 23, label ="SUMMA"),
   Span(doc110, 52, 53, label ="TARIFF"),
   Span(doc110, 57, 58, label ="COUNTRY"),
   Span(doc110, 60, 61, label ="PR_SURCH"),
   Span(doc110, 62, 63, label ="SURCHARGE"),
   Span(doc110, 65, 66, label ="PR_ESURCH"),
   Span(doc110, 67, 68, label ="ESURCHARGE"),
   Span(doc110, 68, 69, label ="TOTAL")]
docs.append(doc110)
print("doc111, 68, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 20000; AMOUNT 3.300; ARTICLE 1120021036; PRICE 26,19; UNIT 100; SUMMA 864,27; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 98,53; PR_ESURCH 3,50; ESURCHARGE 30,25; TOTAL 993,05; ")
doc111 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915** 20000 3.300 PC 1120021036 26,19 100 PC 864,27 LBBU-SP-1 -M8-W2 LBBU-SP 1 M8 W2 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 98,53 Energy Surcharge 3,50 % 30,25 993,05''')
doc111.ents = [
   Span(doc111, 3, 4, label ="NORDER"),
   Span(doc111, 9, 12, label ="CONTRACT"),
   Span(doc111, 12, 13, label ="CONTRACT1"),
   Span(doc111, 15, 16, label ="POS"),
   Span(doc111, 16, 17, label ="AMOUNT"),
   Span(doc111, 18, 19, label ="ARTICLE"),
   Span(doc111, 19, 20, label ="PRICE"),
   Span(doc111, 20, 21, label ="UNIT"),
   Span(doc111, 22, 23, label ="SUMMA"),
   Span(doc111, 51, 52, label ="TARIFF"),
   Span(doc111, 56, 57, label ="COUNTRY"),
   Span(doc111, 59, 60, label ="PR_SURCH"),
   Span(doc111, 61, 62, label ="SURCHARGE"),
   Span(doc111, 64, 65, label ="PR_ESURCH"),
   Span(doc111, 66, 67, label ="ESURCHARGE"),
   Span(doc111, 67, 68, label ="TOTAL")]
docs.append(doc111)
print("doc112, 71, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 20100; AMOUNT 5.900; ARTICLE 1120021042; PRICE 31,15; UNIT 100; SUMMA 1.837; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 209,51; PR_ESURCH 3,50; ESURCHARGE 64,32; TOTAL 2.111,68; ")
doc112 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915** 20100 5.900 PC 1120021042 31,15 100 PC 1.837 ,85 LBBU-SP-2D-M8-W2 LBBU-SP 2D M8 W2 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 209,51 Energy Surcharge 3,50 % 64,32 2.111,68''')
doc112.ents = [
   Span(doc112, 3, 4, label ="NORDER"),
   Span(doc112, 9, 12, label ="CONTRACT"),
   Span(doc112, 12, 13, label ="CONTRACT1"),
   Span(doc112, 15, 16, label ="POS"),
   Span(doc112, 16, 17, label ="AMOUNT"),
   Span(doc112, 18, 19, label ="ARTICLE"),
   Span(doc112, 19, 20, label ="PRICE"),
   Span(doc112, 20, 21, label ="UNIT"),
   Span(doc112, 22, 23, label ="SUMMA"),
   Span(doc112, 54, 55, label ="TARIFF"),
   Span(doc112, 59, 60, label ="COUNTRY"),
   Span(doc112, 62, 63, label ="PR_SURCH"),
   Span(doc112, 64, 65, label ="SURCHARGE"),
   Span(doc112, 67, 68, label ="PR_ESURCH"),
   Span(doc112, 69, 70, label ="ESURCHARGE"),
   Span(doc112, 70, 71, label ="TOTAL")]
docs.append(doc112)
print("doc113, 69, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 20200; AMOUNT 1.600; ARTICLE 1120021038; PRICE 26,79; UNIT 100; SUMMA 428,64; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 48,86; PR_ESURCH 3,50; ESURCHARGE 15,00; TOTAL 492,50; ")
doc113 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915** 20200 1.600 PC 1120021038 26,79 100 PC 428,64 LBBU-SP-2-M8 -W2 LBBU-SP 2 M8 W2 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 48,86  Energy Surcharge 3,50 % 15,00 492,50''')
doc113.ents = [
   Span(doc113, 3, 4, label ="NORDER"),
   Span(doc113, 9, 12, label ="CONTRACT"),
   Span(doc113, 12, 13, label ="CONTRACT1"),
   Span(doc113, 15, 16, label ="POS"),
   Span(doc113, 16, 17, label ="AMOUNT"),
   Span(doc113, 18, 19, label ="ARTICLE"),
   Span(doc113, 19, 20, label ="PRICE"),
   Span(doc113, 20, 21, label ="UNIT"),
   Span(doc113, 22, 23, label ="SUMMA"),
   Span(doc113, 51, 52, label ="TARIFF"),
   Span(doc113, 56, 57, label ="COUNTRY"),
   Span(doc113, 59, 60, label ="PR_SURCH"),
   Span(doc113, 61, 62, label ="SURCHARGE"),
   Span(doc113, 65, 66, label ="PR_ESURCH"),
   Span(doc113, 67, 68, label ="ESURCHARGE"),
   Span(doc113, 68, 69, label ="TOTAL")]
docs.append(doc113)
print("doc114, 69, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 20300; AMOUNT 400; ARTICLE 1120021657; PRICE 48,51; UNIT 100; SUMMA 194,04; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 22,12; PR_ESURCH 3,50; ESURCHARGE 6,79; TOTAL 222,95; ")
doc114 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915** 20300 400 PC 1120021657 48,51 100 PC 194,04 LBBU-SP-3D-M8-W2 LBBU-SP 3D M8 W2 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 22,12 Energy Surcharge 3,50 % 6,79 222,95''')
doc114.ents = [
   Span(doc114, 3, 4, label ="NORDER"),
   Span(doc114, 9, 12, label ="CONTRACT"),
   Span(doc114, 12, 13, label ="CONTRACT1"),
   Span(doc114, 15, 16, label ="POS"),
   Span(doc114, 16, 17, label ="AMOUNT"),
   Span(doc114, 18, 19, label ="ARTICLE"),
   Span(doc114, 19, 20, label ="PRICE"),
   Span(doc114, 20, 21, label ="UNIT"),
   Span(doc114, 22, 23, label ="SUMMA"),
   Span(doc114, 52, 53, label ="TARIFF"),
   Span(doc114, 57, 58, label ="COUNTRY"),
   Span(doc114, 60, 61, label ="PR_SURCH"),
   Span(doc114, 62, 63, label ="SURCHARGE"),
   Span(doc114, 65, 66, label ="PR_ESURCH"),
   Span(doc114, 67, 68, label ="ESURCHARGE"),
   Span(doc114, 68, 69, label ="TOTAL")]
docs.append(doc114)
print("doc115, 68, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 20400; AMOUNT 800; ARTICLE 1120021686; PRICE 38,85; UNIT 100; SUMMA 310,80; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 35,43; PR_ESURCH 3,50; ESURCHARGE 10,88; TOTAL 357,11; ")
doc115 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915** 20400 800 PC 1120021686 38,85 100 PC 310,80 LBBU-SP-3-M8 -W2 LBBU-SP 3 M8 W2 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 35,43 Energy Surcharge 3,50 % 10,88 357,11''')
doc115.ents = [
   Span(doc115, 3, 4, label ="NORDER"),
   Span(doc115, 9, 12, label ="CONTRACT"),
   Span(doc115, 12, 13, label ="CONTRACT1"),
   Span(doc115, 15, 16, label ="POS"),
   Span(doc115, 16, 17, label ="AMOUNT"),
   Span(doc115, 18, 19, label ="ARTICLE"),
   Span(doc115, 19, 20, label ="PRICE"),
   Span(doc115, 20, 21, label ="UNIT"),
   Span(doc115, 22, 23, label ="SUMMA"),
   Span(doc115, 51, 52, label ="TARIFF"),
   Span(doc115, 56, 57, label ="COUNTRY"),
   Span(doc115, 59, 60, label ="PR_SURCH"),
   Span(doc115, 61, 62, label ="SURCHARGE"),
   Span(doc115, 64, 65, label ="PR_ESURCH"),
   Span(doc115, 66, 67, label ="ESURCHARGE"),
   Span(doc115, 67, 68, label ="TOTAL")]
docs.append(doc115)
print("doc116, 66, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 20500; AMOUNT 150; ARTICLE 1120002537; PRICE 28,25; UNIT 100; SUMMA 42,38; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 4,83; PR_ESURCH 3,50; ESURCHARGE 1,48; TOTAL 48,69; ")
doc116 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915** 20500 150 PC 1120002537 28,25 100 PC 42,38 SP-2D-M-W2 SP 2 DM W2 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098    Country of origin: Germany Material Surcharge 11,40 % 4,83 Energy Surcharge 3,50 % 1,48 48,69''')
doc116.ents = [
   Span(doc116, 3, 4, label ="NORDER"),
   Span(doc116, 9, 12, label ="CONTRACT"),
   Span(doc116, 12, 13, label ="CONTRACT1"),
   Span(doc116, 15, 16, label ="POS"),
   Span(doc116, 16, 17, label ="AMOUNT"),
   Span(doc116, 18, 19, label ="ARTICLE"),
   Span(doc116, 19, 20, label ="PRICE"),
   Span(doc116, 20, 21, label ="UNIT"),
   Span(doc116, 22, 23, label ="SUMMA"),
   Span(doc116, 48, 49, label ="TARIFF"),
   Span(doc116, 54, 55, label ="COUNTRY"),
   Span(doc116, 57, 58, label ="PR_SURCH"),
   Span(doc116, 59, 60, label ="SURCHARGE"),
   Span(doc116, 62, 63, label ="PR_ESURCH"),
   Span(doc116, 64, 65, label ="ESURCHARGE"),
   Span(doc116, 65, 66, label ="TOTAL")]
docs.append(doc116)
print("doc117, 65, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 20600; AMOUNT 50; ARTICLE 1120001156; PRICE 19,70; UNIT 100; SUMMA 9,85; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 1,12; PR_ESURCH 3,50; ESURCHARGE 0,34; TOTAL 11,31; ")
doc117 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915** 20600 50 PC 1120001156 19,70 100 PC 9,85 SP-2-M-W2 SP 2 M W2 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 1,12 Energy Surcharge 3,50 % 0,34 11,31''')
doc117.ents = [
   Span(doc117, 3, 4, label ="NORDER"),
   Span(doc117, 9, 12, label ="CONTRACT"),
   Span(doc117, 12, 13, label ="CONTRACT1"),
   Span(doc117, 15, 16, label ="POS"),
   Span(doc117, 16, 17, label ="AMOUNT"),
   Span(doc117, 18, 19, label ="ARTICLE"),
   Span(doc117, 19, 20, label ="PRICE"),
   Span(doc117, 20, 21, label ="UNIT"),
   Span(doc117, 22, 23, label ="SUMMA"),
   Span(doc117, 48, 49, label ="TARIFF"),
   Span(doc117, 53, 54, label ="COUNTRY"),
   Span(doc117, 56, 57, label ="PR_SURCH"),
   Span(doc117, 58, 59, label ="SURCHARGE"),
   Span(doc117, 61, 62, label ="PR_ESURCH"),
   Span(doc117, 63, 64, label ="ESURCHARGE"),
   Span(doc117, 64, 65, label ="TOTAL")]
docs.append(doc117)
print("doc118, 65, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 20700; AMOUNT 700; ARTICLE 1120001175; PRICE 29,27; UNIT 100; SUMMA 204,89; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 23,36; PR_ESURCH 3,50; ESURCHARGE 7,17; TOTAL 235,42; ")
doc118 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915** 20700 700 PC 1120001175 29,27 100 PC 204,89 SP-6-M-W2 SP 6 M W2 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 23,36 Energy Surcharge 3,50 % 7,17 235,42''')
doc118.ents = [
   Span(doc118, 3, 4, label ="NORDER"),
   Span(doc118, 9, 12, label ="CONTRACT"),
   Span(doc118, 12, 13, label ="CONTRACT1"),
   Span(doc118, 15, 16, label ="POS"),
   Span(doc118, 16, 17, label ="AMOUNT"),
   Span(doc118, 18, 19, label ="ARTICLE"),
   Span(doc118, 19, 20, label ="PRICE"),
   Span(doc118, 20, 21, label ="UNIT"),
   Span(doc118, 22, 23, label ="SUMMA"),
   Span(doc118, 48, 49, label ="TARIFF"),
   Span(doc118, 53, 54, label ="COUNTRY"),
   Span(doc118, 56, 57, label ="PR_SURCH"),
   Span(doc118, 58, 59, label ="SURCHARGE"),
   Span(doc118, 61, 62, label ="PR_ESURCH"),
   Span(doc118, 63, 64, label ="ESURCHARGE"),
   Span(doc118, 64, 65, label ="TOTAL")]
docs.append(doc118)
print("doc119, 75, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 20800; AMOUNT 500; ARTICLE 1910000432; PRICE 4,07; UNIT 1; SUMMA 2.035,00; TARIFF 84213925; COUNTRY Italy; PR_SURCH 11,40; SURCHARGE 231,99; PR_ESURCH 3,50; ESURCHARGE 71,23; TOTAL 2.338; ")
doc119 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915** 20800 500 PC 1910000432 (*) 4,07 1 PC 2.035,00 SMBT-47-S-10-O-B04-O packed per each item    Product description: filter breather Export - Customs tariff no.: 84213925 Country of origin: Italy Material Surcharge 11,40 % 231,99 Energy Surcharge 3,50 % 71,23 2.338 ,22 EAC - Eurasian Conformity''')
doc119.ents = [
   Span(doc119, 3, 4, label ="NORDER"),
   Span(doc119, 9, 12, label ="CONTRACT"),
   Span(doc119, 12, 13, label ="CONTRACT1"),
   Span(doc119, 15, 16, label ="POS"),
   Span(doc119, 16, 17, label ="AMOUNT"),
   Span(doc119, 18, 19, label ="ARTICLE"),
   Span(doc119, 22, 23, label ="PRICE"),
   Span(doc119, 23, 24, label ="UNIT"),
   Span(doc119, 25, 26, label ="SUMMA"),
   Span(doc119, 52, 53, label ="TARIFF"),
   Span(doc119, 57, 58, label ="COUNTRY"),
   Span(doc119, 60, 61, label ="PR_SURCH"),
   Span(doc119, 62, 63, label ="SURCHARGE"),
   Span(doc119, 65, 66, label ="PR_ESURCH"),
   Span(doc119, 67, 68, label ="ESURCHARGE"),
   Span(doc119, 68, 69, label ="TOTAL")]
docs.append(doc119)
print("doc120, 63, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 20900; AMOUNT 120; ARTICLE 1730002924; PRICE 25,96; UNIT 1; SUMMA 3.115,20; TARIFF 73079980; COUNTRY Italy; PR_SURCH 15,50; SURCHARGE 482,86; PR_ESURCH 3,50; ESURCHARGE 109,03; TOTAL 3.707,09; ")
doc120 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915** 20900 120 PC 1730002924 25,96 1 PC 3.115,20 BF-L-604-W66 BF-L-604 packed per each item Product description: flange Export - Customs tariff no.: 73079980 Country of origin: Italy Material Surcharge 15,50 % 482,86 Energy Surcharge 3,50 % 109,03 3.707,09''')
doc120.ents = [
   Span(doc120, 3, 4, label ="NORDER"),
   Span(doc120, 9, 12, label ="CONTRACT"),
   Span(doc120, 12, 13, label ="CONTRACT1"),
   Span(doc120, 15, 16, label ="POS"),
   Span(doc120, 16, 17, label ="AMOUNT"),
   Span(doc120, 18, 19, label ="ARTICLE"),
   Span(doc120, 19, 20, label ="PRICE"),
   Span(doc120, 20, 21, label ="UNIT"),
   Span(doc120, 22, 23, label ="SUMMA"),
   Span(doc120, 46, 47, label ="TARIFF"),
   Span(doc120, 51, 52, label ="COUNTRY"),
   Span(doc120, 54, 55, label ="PR_SURCH"),
   Span(doc120, 56, 57, label ="SURCHARGE"),
   Span(doc120, 59, 60, label ="PR_ESURCH"),
   Span(doc120, 61, 62, label ="ESURCHARGE"),
   Span(doc120, 62, 63, label ="TOTAL")]
docs.append(doc120)
print("doc121, 63, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 21000; AMOUNT 40; ARTICLE 6100026392; PRICE 18,22; UNIT 1; SUMMA 728,80; TARIFF 73079100; COUNTRY Italy; PR_SURCH 15,50; SURCHARGE 112,96; PR_ESURCH 3,50; ESURCHARGE 25,51; TOTAL 867,27; ")
doc121 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915** 21000 40 PC 6100026392 18,22 1 PC 728,80 BFX-305-35L-W66 BFX-305-L35 packed per each item Product description: flange Export - Customs tariff no.: 73079100 Country of origin: Italy Material Surcharge 15,50 % 112,96 Energy Surcharge 3,50 % 25,51 867,27''')
doc121.ents = [
   Span(doc121, 3, 4, label ="NORDER"),
   Span(doc121, 9, 12, label ="CONTRACT"),
   Span(doc121, 12, 13, label ="CONTRACT1"),
   Span(doc121, 15, 16, label ="POS"),
   Span(doc121, 16, 17, label ="AMOUNT"),
   Span(doc121, 18, 19, label ="ARTICLE"),
   Span(doc121, 19, 20, label ="PRICE"),
   Span(doc121, 20, 21, label ="UNIT"),
   Span(doc121, 22, 23, label ="SUMMA"),
   Span(doc121, 46, 47, label ="TARIFF"),
   Span(doc121, 51, 52, label ="COUNTRY"),
   Span(doc121, 54, 55, label ="PR_SURCH"),
   Span(doc121, 56, 57, label ="SURCHARGE"),
   Span(doc121, 59, 60, label ="PR_ESURCH"),
   Span(doc121, 61, 62, label ="ESURCHARGE"),
   Span(doc121, 62, 63, label ="TOTAL")]
docs.append(doc121)
print("doc122, 64, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 21100; AMOUNT 100; ARTICLE 1730000192; PRICE 7,73; UNIT 1; SUMMA 773,00; TARIFF 73079910; COUNTRY Lithuania; PR_SURCH 15,50; SURCHARGE 119,82; PR_ESURCH 3,50; ESURCHARGE 27,06; TOTAL 919,88; ")
doc122 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915**    21100 100 PC 1730000192 7,73 1 PC 773,00 CAG-604-30S-W66 CAG-604-S30 packed per each item Product description: flange Export - Customs tariff no.: 73079910 Country of origin: Lithuania Material Surcharge 15,50 % 119,82 Energy Surcharge 3,50 % 27,06 919,88''')
doc122.ents = [
   Span(doc122, 3, 4, label ="NORDER"),
   Span(doc122, 9, 12, label ="CONTRACT"),
   Span(doc122, 12, 13, label ="CONTRACT1"),
   Span(doc122, 16, 17, label ="POS"),
   Span(doc122, 17, 18, label ="AMOUNT"),
   Span(doc122, 19, 20, label ="ARTICLE"),
   Span(doc122, 20, 21, label ="PRICE"),
   Span(doc122, 21, 22, label ="UNIT"),
   Span(doc122, 23, 24, label ="SUMMA"),
   Span(doc122, 47, 48, label ="TARIFF"),
   Span(doc122, 52, 53, label ="COUNTRY"),
   Span(doc122, 55, 56, label ="PR_SURCH"),
   Span(doc122, 57, 58, label ="SURCHARGE"),
   Span(doc122, 60, 61, label ="PR_ESURCH"),
   Span(doc122, 62, 63, label ="ESURCHARGE"),
   Span(doc122, 63, 64, label ="TOTAL")]
docs.append(doc122)
print("doc123, 72, #NORDER 2390862; CONTRACT SR-1-06; CONTRACT1 1915; POS 21200; AMOUNT 8.000; ARTICLE 1730000523; PRICE 0,08; UNIT 1; SUMMA 640,00; TARIFF 73182100; COUNTRY Origin unknown; PR_SURCH 15,50; SURCHARGE 99,20; PR_ESURCH 3,50; ESURCHARGE 22,40; TOTAL 761,60; ")
doc123 = nlp('''Order number: 2390862 Purchase order number: N SR-1-06 1915** 21200 8.000 PC 1730000523 0,08 1 PC 640,00 Spring-ring-ANSI-B18.21.1-7/16UNC-CS Federring 7/16 UNC ANSI B18.21.1 packed per each item Product description: ring Export - Customs tariff no.: 73182100 Country of origin: Origin unknown Material Surcharge 15,50 % 99,20 Energy Surcharge 3,50 % 22,40 761,60''')
doc123.ents = [
   Span(doc123, 3, 4, label ="NORDER"),
   Span(doc123, 9, 12, label ="CONTRACT"),
   Span(doc123, 12, 13, label ="CONTRACT1"),
   Span(doc123, 15, 16, label ="POS"),
   Span(doc123, 16, 17, label ="AMOUNT"),
   Span(doc123, 18, 19, label ="ARTICLE"),
   Span(doc123, 19, 20, label ="PRICE"),
   Span(doc123, 20, 21, label ="UNIT"),
   Span(doc123, 22, 23, label ="SUMMA"),
   Span(doc123, 54, 55, label ="TARIFF"),
   Span(doc123, 59, 61, label ="COUNTRY"),
   Span(doc123, 63, 64, label ="PR_SURCH"),
   Span(doc123, 65, 66, label ="SURCHARGE"),
   Span(doc123, 68, 69, label ="PR_ESURCH"),
   Span(doc123, 70, 71, label ="ESURCHARGE"),
   Span(doc123, 71, 72, label ="TOTAL")]
docs.append(doc123)
print("doc124, 63, #NORDER 2390890; CONTRACT SR-1-06; CONTRACT1 1918; POS 21300; AMOUNT 150; ARTICLE 6100076275; PRICE 9,92; UNIT 1; SUMMA 1.488,00; TARIFF 90261089; COUNTRY China; PR_SURCH 11,40; SURCHARGE 169,63; PR_ESURCH 3,50; ESURCHARGE 52,08; TOTAL 1.709,71; ")
doc124 = nlp('''Order number: 2390890 Purchase order number: N SR-1-06 1918** 21300 150 PC 6100076275 (*) 9,92 1 PC 1.488,00 SNA-150-B-X-O-12-496915 packed per each item Export - Customs tariff no.: 90261089 Country of origin: China Material Surcharge 11,40 % 169,63 Energy Surcharge 3,50 % 52,08 1.709,71''')
doc124.ents = [
   Span(doc124, 3, 4, label ="NORDER"),
   Span(doc124, 9, 12, label ="CONTRACT"),
   Span(doc124, 12, 13, label ="CONTRACT1"),
   Span(doc124, 15, 16, label ="POS"),
   Span(doc124, 16, 17, label ="AMOUNT"),
   Span(doc124, 18, 19, label ="ARTICLE"),
   Span(doc124, 22, 23, label ="PRICE"),
   Span(doc124, 23, 24, label ="UNIT"),
   Span(doc124, 25, 26, label ="SUMMA"),
   Span(doc124, 46, 47, label ="TARIFF"),
   Span(doc124, 51, 52, label ="COUNTRY"),
   Span(doc124, 54, 55, label ="PR_SURCH"),
   Span(doc124, 56, 57, label ="SURCHARGE"),
   Span(doc124, 59, 60, label ="PR_ESURCH"),
   Span(doc124, 61, 62, label ="ESURCHARGE"),
   Span(doc124, 62, 63, label ="TOTAL")]
docs.append(doc124)
print("doc125, 63, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 21400; AMOUNT 200; ARTICLE 1130017267; PRICE 19,68; UNIT 100; SUMMA 39,36; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 4,49; PR_ESURCH 3,50; ESURCHARGE 1,38; TOTAL 45,23; ")
doc125 = nlp('''Order number: 2390896   Purchase order number: N SR-1-06 1919** 21400 200 PC 1130017267 19,68 100 PC 39,36 LNGF-312.7/12.7-PA LNGF 312,7/12,7 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 4,49 Energy Surcharge 3,50 % 1,38 45,23''')
doc125.ents = [
   Span(doc125, 3, 4, label ="NORDER"),
   Span(doc125, 10, 13, label ="CONTRACT"),
   Span(doc125, 13, 14, label ="CONTRACT1"),
   Span(doc125, 16, 17, label ="POS"),
   Span(doc125, 17, 18, label ="AMOUNT"),
   Span(doc125, 19, 20, label ="ARTICLE"),
   Span(doc125, 20, 21, label ="PRICE"),
   Span(doc125, 21, 22, label ="UNIT"),
   Span(doc125, 23, 24, label ="SUMMA"),
   Span(doc125, 46, 47, label ="TARIFF"),
   Span(doc125, 51, 52, label ="COUNTRY"),
   Span(doc125, 54, 55, label ="PR_SURCH"),
   Span(doc125, 56, 57, label ="SURCHARGE"),
   Span(doc125, 59, 60, label ="PR_ESURCH"),
   Span(doc125, 61, 62, label ="ESURCHARGE"),
   Span(doc125, 62, 63, label ="TOTAL")]
docs.append(doc125)
print("doc126, 62, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 21500; AMOUNT 400; ARTICLE 1130001960; PRICE 5,65; UNIT 100; SUMMA 22,60; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 2,58; PR_ESURCH 3,50; ESURCHARGE 0,79; TOTAL 25,97; ")
doc126 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 21500 400 PC 1130001960 5,65 100 PC 22,60 DPL-3-W3 DPL 3 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 2,58 Energy Surcharge 3,50 % 0,79 25,97''')
doc126.ents = [
   Span(doc126, 3, 4, label ="NORDER"),
   Span(doc126, 9, 12, label ="CONTRACT"),
   Span(doc126, 12, 13, label ="CONTRACT1"),
   Span(doc126, 15, 16, label ="POS"),
   Span(doc126, 16, 17, label ="AMOUNT"),
   Span(doc126, 18, 19, label ="ARTICLE"),
   Span(doc126, 19, 20, label ="PRICE"),
   Span(doc126, 20, 21, label ="UNIT"),
   Span(doc126, 22, 23, label ="SUMMA"),
   Span(doc126, 45, 46, label ="TARIFF"),
   Span(doc126, 50, 51, label ="COUNTRY"),
   Span(doc126, 53, 54, label ="PR_SURCH"),
   Span(doc126, 55, 56, label ="SURCHARGE"),
   Span(doc126, 58, 59, label ="PR_ESURCH"),
   Span(doc126, 60, 61, label ="ESURCHARGE"),
   Span(doc126, 61, 62, label ="TOTAL")]
docs.append(doc126)
print("doc127, 59, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 21600; AMOUNT 800; ARTICLE 6100196638; PRICE 52,37; UNIT 100; SUMMA 418,96; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 47,76; PR_ESURCH 3,50; ESURCHARGE 14,66; TOTAL 481,38; ")
doc127 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 21600 800 PC 6100196638 52,37 100 PC 418,96 LBBU-218/18-SA-M8/U5/16/2 packed per each item Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 47,76 Energy Surcharge 3,50 % 14,66 481,38    ''')
doc127.ents = [
   Span(doc127, 3, 4, label ="NORDER"),
   Span(doc127, 9, 12, label ="CONTRACT"),
   Span(doc127, 12, 13, label ="CONTRACT1"),
   Span(doc127, 15, 16, label ="POS"),
   Span(doc127, 16, 17, label ="AMOUNT"),
   Span(doc127, 18, 19, label ="ARTICLE"),
   Span(doc127, 19, 20, label ="PRICE"),
   Span(doc127, 20, 21, label ="UNIT"),
   Span(doc127, 22, 23, label ="SUMMA"),
   Span(doc127, 41, 42, label ="TARIFF"),
   Span(doc127, 46, 47, label ="COUNTRY"),
   Span(doc127, 49, 50, label ="PR_SURCH"),
   Span(doc127, 51, 52, label ="SURCHARGE"),
   Span(doc127, 54, 55, label ="PR_ESURCH"),
   Span(doc127, 56, 57, label ="ESURCHARGE"),
   Span(doc127, 57, 58, label ="TOTAL")]
docs.append(doc127)
print("doc128, 63, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 21700; AMOUNT 75; ARTICLE 1130005319; PRICE 63,10; UNIT 100; SUMMA 47,33; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 5,40; PR_ESURCH 3,50; ESURCHARGE 1,66; TOTAL 54,39; ")
doc128 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 21700 75 PC 1130005319 63,10 100 PC 47,33 215/15-PA-H 215/15 PAH packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 5,40 Energy Surcharge 3,50 % 1,66 54,39''')
doc128.ents = [
   Span(doc128, 3, 4, label ="NORDER"),
   Span(doc128, 9, 12, label ="CONTRACT"),
   Span(doc128, 12, 13, label ="CONTRACT1"),
   Span(doc128, 15, 16, label ="POS"),
   Span(doc128, 16, 17, label ="AMOUNT"),
   Span(doc128, 18, 19, label ="ARTICLE"),
   Span(doc128, 19, 20, label ="PRICE"),
   Span(doc128, 20, 21, label ="UNIT"),
   Span(doc128, 22, 23, label ="SUMMA"),
   Span(doc128, 46, 47, label ="TARIFF"),
   Span(doc128, 51, 52, label ="COUNTRY"),
   Span(doc128, 54, 55, label ="PR_SURCH"),
   Span(doc128, 56, 57, label ="SURCHARGE"),
   Span(doc128, 59, 60, label ="PR_ESURCH"),
   Span(doc128, 61, 62, label ="ESURCHARGE"),
   Span(doc128, 62, 63, label ="TOTAL")]
docs.append(doc128)
print("doc129, 63, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 21800; AMOUNT 100; ARTICLE 1130005367; PRICE 32,76; UNIT 100; SUMMA 32,76; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 3,73; PR_ESURCH 3,50; ESURCHARGE 1,15; TOTAL 37,64; ")
doc129 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 21800 100 PC 1130005367 32,76 100 PC 32,76 217.2-PA-H 217,2 PAH packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 3,73 Energy Surcharge 3,50 % 1,15 37,64''')
doc129.ents = [
   Span(doc129, 3, 4, label ="NORDER"),
   Span(doc129, 9, 12, label ="CONTRACT"),
   Span(doc129, 12, 13, label ="CONTRACT1"),
   Span(doc129, 15, 16, label ="POS"),
   Span(doc129, 16, 17, label ="AMOUNT"),
   Span(doc129, 18, 19, label ="ARTICLE"),
   Span(doc129, 19, 20, label ="PRICE"),
   Span(doc129, 20, 21, label ="UNIT"),
   Span(doc129, 22, 23, label ="SUMMA"),
   Span(doc129, 46, 47, label ="TARIFF"),
   Span(doc129, 51, 52, label ="COUNTRY"),
   Span(doc129, 54, 55, label ="PR_SURCH"),
   Span(doc129, 56, 57, label ="SURCHARGE"),
   Span(doc129, 59, 60, label ="PR_ESURCH"),
   Span(doc129, 61, 62, label ="ESURCHARGE"),
   Span(doc129, 62, 63, label ="TOTAL")]
docs.append(doc129)
print("doc130, 64, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 21900; AMOUNT 150; ARTICLE 1130005384; PRICE 32,76; UNIT 100; SUMMA 49,14; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 5,60; PR_ESURCH 3,50; ESURCHARGE 1,72; TOTAL 56,46; ")
doc130 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 21900 150 PC 1130005384 32,76 100 PC 49,14 218-PA-H 218 PAH packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 5,60   Energy Surcharge 3,50 % 1,72 56,46''')
doc130.ents = [
   Span(doc130, 3, 4, label ="NORDER"),
   Span(doc130, 9, 12, label ="CONTRACT"),
   Span(doc130, 12, 13, label ="CONTRACT1"),
   Span(doc130, 15, 16, label ="POS"),
   Span(doc130, 16, 17, label ="AMOUNT"),
   Span(doc130, 18, 19, label ="ARTICLE"),
   Span(doc130, 19, 20, label ="PRICE"),
   Span(doc130, 20, 21, label ="UNIT"),
   Span(doc130, 22, 23, label ="SUMMA"),
   Span(doc130, 46, 47, label ="TARIFF"),
   Span(doc130, 51, 52, label ="COUNTRY"),
   Span(doc130, 54, 55, label ="PR_SURCH"),
   Span(doc130, 56, 57, label ="SURCHARGE"),
   Span(doc130, 60, 61, label ="PR_ESURCH"),
   Span(doc130, 62, 63, label ="ESURCHARGE"),
   Span(doc130, 63, 64, label ="TOTAL")]
docs.append(doc130)
print("doc131, 63, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 22000; AMOUNT 125; ARTICLE 1130003214; PRICE 54,78; UNIT 100; SUMMA 68,48; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 7,81; PR_ESURCH 3,50; ESURCHARGE 2,40; TOTAL 78,69; ")
doc131 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 22000 125 PC 1130003214 54,78 100 PC 68,48 322/22-PA-H 322/22 PAH packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 7,81 Energy Surcharge 3,50 % 2,40 78,69''')
doc131.ents = [
   Span(doc131, 3, 4, label ="NORDER"),
   Span(doc131, 9, 12, label ="CONTRACT"),
   Span(doc131, 12, 13, label ="CONTRACT1"),
   Span(doc131, 15, 16, label ="POS"),
   Span(doc131, 16, 17, label ="AMOUNT"),
   Span(doc131, 18, 19, label ="ARTICLE"),
   Span(doc131, 19, 20, label ="PRICE"),
   Span(doc131, 20, 21, label ="UNIT"),
   Span(doc131, 22, 23, label ="SUMMA"),
   Span(doc131, 46, 47, label ="TARIFF"),
   Span(doc131, 51, 52, label ="COUNTRY"),
   Span(doc131, 54, 55, label ="PR_SURCH"),
   Span(doc131, 56, 57, label ="SURCHARGE"),
   Span(doc131, 59, 60, label ="PR_ESURCH"),
   Span(doc131, 61, 62, label ="ESURCHARGE"),
   Span(doc131, 62, 63, label ="TOTAL")]
docs.append(doc131)
print("doc132, 66, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 22100; AMOUNT 50; ARTICLE 1130005582; PRICE 23,90; UNIT 100; SUMMA 11,95; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 1,36; PR_ESURCH 3,50; ESURCHARGE 0,42; TOTAL 13,73; ")
doc132 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 22100 50 PC 1130005582 23,90 100 PC 11,95 322-PP-H-BK 322 PPH black9005 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 1,36 Energy Surcharge 3,50 % 0,42 13,73''')
doc132.ents = [
   Span(doc132, 3, 4, label ="NORDER"),
   Span(doc132, 9, 12, label ="CONTRACT"),
   Span(doc132, 12, 13, label ="CONTRACT1"),
   Span(doc132, 15, 16, label ="POS"),
   Span(doc132, 16, 17, label ="AMOUNT"),
   Span(doc132, 18, 19, label ="ARTICLE"),
   Span(doc132, 19, 20, label ="PRICE"),
   Span(doc132, 20, 21, label ="UNIT"),
   Span(doc132, 22, 23, label ="SUMMA"),
   Span(doc132, 49, 50, label ="TARIFF"),
   Span(doc132, 54, 55, label ="COUNTRY"),
   Span(doc132, 57, 58, label ="PR_SURCH"),
   Span(doc132, 59, 60, label ="SURCHARGE"),
   Span(doc132, 62, 63, label ="PR_ESURCH"),
   Span(doc132, 64, 65, label ="ESURCHARGE"),
   Span(doc132, 65, 66, label ="TOTAL")]
docs.append(doc132)
print("doc133, 67, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 22200; AMOUNT 500; ARTICLE 1130005661; PRICE 33,06; UNIT 100; SUMMA 165,30; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 18,84; PR_ESURCH 3,50; ESURCHARGE 5,79; TOTAL 189,93; ")
doc133 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 22200 500 PC 1130005661 33,06 100 PC 165,30 325/25-PP-H-BK 325/25 PPH black9005 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097    Country of origin: Germany Material Surcharge 11,40 % 18,84 Energy Surcharge 3,50 % 5,79 189,93''')
doc133.ents = [
   Span(doc133, 3, 4, label ="NORDER"),
   Span(doc133, 9, 12, label ="CONTRACT"),
   Span(doc133, 12, 13, label ="CONTRACT1"),
   Span(doc133, 15, 16, label ="POS"),
   Span(doc133, 16, 17, label ="AMOUNT"),
   Span(doc133, 18, 19, label ="ARTICLE"),
   Span(doc133, 19, 20, label ="PRICE"),
   Span(doc133, 20, 21, label ="UNIT"),
   Span(doc133, 22, 23, label ="SUMMA"),
   Span(doc133, 49, 50, label ="TARIFF"),
   Span(doc133, 55, 56, label ="COUNTRY"),
   Span(doc133, 58, 59, label ="PR_SURCH"),
   Span(doc133, 60, 61, label ="SURCHARGE"),
   Span(doc133, 63, 64, label ="PR_ESURCH"),
   Span(doc133, 65, 66, label ="ESURCHARGE"),
   Span(doc133, 66, 67, label ="TOTAL")]
docs.append(doc133)
print("doc134, 61, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 22300; AMOUNT 50; ARTICLE 1130005715; PRICE 81,41; UNIT 100; SUMMA 40,71; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 4,64; PR_ESURCH 3,50; ESURCHARGE 1,42; TOTAL 46,77; ")
doc134 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 22300 50 PC 1130005715 81,41 100 PC 40,71 4025-PA 4025 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 4,64 Energy Surcharge 3,50 % 1,42 46,77''')
doc134.ents = [
   Span(doc134, 3, 4, label ="NORDER"),
   Span(doc134, 9, 12, label ="CONTRACT"),
   Span(doc134, 12, 13, label ="CONTRACT1"),
   Span(doc134, 15, 16, label ="POS"),
   Span(doc134, 16, 17, label ="AMOUNT"),
   Span(doc134, 18, 19, label ="ARTICLE"),
   Span(doc134, 19, 20, label ="PRICE"),
   Span(doc134, 20, 21, label ="UNIT"),
   Span(doc134, 22, 23, label ="SUMMA"),
   Span(doc134, 44, 45, label ="TARIFF"),
   Span(doc134, 49, 50, label ="COUNTRY"),
   Span(doc134, 52, 53, label ="PR_SURCH"),
   Span(doc134, 54, 55, label ="SURCHARGE"),
   Span(doc134, 57, 58, label ="PR_ESURCH"),
   Span(doc134, 59, 60, label ="ESURCHARGE"),
   Span(doc134, 60, 61, label ="TOTAL")]
docs.append(doc134)
print("doc135, 66, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 22400; AMOUNT 600; ARTICLE 1130026834; PRICE 40,89; UNIT 100; SUMMA 245,34; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 27,97; PR_ESURCH 3,50; ESURCHARGE 8,59; TOTAL 281,90; ")
doc135 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 22400 600 PC 1130026834 40,89 100 PC 245,34 426.9/26.9-PP-H-BK 426,9/26,9 PPH black9005 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 27,97 Energy Surcharge 3,50 % 8,59 281,90''')
doc135.ents = [
   Span(doc135, 3, 4, label ="NORDER"),
   Span(doc135, 9, 12, label ="CONTRACT"),
   Span(doc135, 12, 13, label ="CONTRACT1"),
   Span(doc135, 15, 16, label ="POS"),
   Span(doc135, 16, 17, label ="AMOUNT"),
   Span(doc135, 18, 19, label ="ARTICLE"),
   Span(doc135, 19, 20, label ="PRICE"),
   Span(doc135, 20, 21, label ="UNIT"),
   Span(doc135, 22, 23, label ="SUMMA"),
   Span(doc135, 49, 50, label ="TARIFF"),
   Span(doc135, 54, 55, label ="COUNTRY"),
   Span(doc135, 57, 58, label ="PR_SURCH"),
   Span(doc135, 59, 60, label ="SURCHARGE"),
   Span(doc135, 62, 63, label ="PR_ESURCH"),
   Span(doc135, 64, 65, label ="ESURCHARGE"),
   Span(doc135, 65, 66, label ="TOTAL")]
docs.append(doc135)
print("doc136, 67, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 22500; AMOUNT 3.200; ARTICLE 1130026758; PRICE 29,27; UNIT 100; SUMMA 936,64; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 106,78; PR_ESURCH 3,50; ESURCHARGE 32,78; TOTAL 1.076,20; ")
doc136 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 22500 3.200 PC 1130026758 29,27 100 PC 936,64 426.9-PP-H-BK 426,9 PPH black9005    packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 106,78 Energy Surcharge 3,50 % 32,78 1.076,20''')
doc136.ents = [
   Span(doc136, 3, 4, label ="NORDER"),
   Span(doc136, 9, 12, label ="CONTRACT"),
   Span(doc136, 12, 13, label ="CONTRACT1"),
   Span(doc136, 15, 16, label ="POS"),
   Span(doc136, 16, 17, label ="AMOUNT"),
   Span(doc136, 18, 19, label ="ARTICLE"),
   Span(doc136, 19, 20, label ="PRICE"),
   Span(doc136, 20, 21, label ="UNIT"),
   Span(doc136, 22, 23, label ="SUMMA"),
   Span(doc136, 50, 51, label ="TARIFF"),
   Span(doc136, 55, 56, label ="COUNTRY"),
   Span(doc136, 58, 59, label ="PR_SURCH"),
   Span(doc136, 60, 61, label ="SURCHARGE"),
   Span(doc136, 63, 64, label ="PR_ESURCH"),
   Span(doc136, 65, 66, label ="ESURCHARGE"),
   Span(doc136, 66, 67, label ="TOTAL")]
docs.append(doc136)
print("doc137, 63, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 22600; AMOUNT 600; ARTICLE 1130005809; PRICE 85,31; UNIT 100; SUMMA 511,86; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 58,35; PR_ESURCH 3,50; ESURCHARGE 17,92; TOTAL 588,13; ")
doc137 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 22600 600 PC 1130005809 85,31 100 PC 511,86 428/28-PA-H 428/28 PAH packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 58,35 Energy Surcharge 3,50 % 17,92 588,13''')
doc137.ents = [
   Span(doc137, 3, 4, label ="NORDER"),
   Span(doc137, 9, 12, label ="CONTRACT"),
   Span(doc137, 12, 13, label ="CONTRACT1"),
   Span(doc137, 15, 16, label ="POS"),
   Span(doc137, 16, 17, label ="AMOUNT"),
   Span(doc137, 18, 19, label ="ARTICLE"),
   Span(doc137, 19, 20, label ="PRICE"),
   Span(doc137, 20, 21, label ="UNIT"),
   Span(doc137, 22, 23, label ="SUMMA"),
   Span(doc137, 46, 47, label ="TARIFF"),
   Span(doc137, 51, 52, label ="COUNTRY"),
   Span(doc137, 54, 55, label ="PR_SURCH"),
   Span(doc137, 56, 57, label ="SURCHARGE"),
   Span(doc137, 59, 60, label ="PR_ESURCH"),
   Span(doc137, 61, 62, label ="ESURCHARGE"),
   Span(doc137, 62, 63, label ="TOTAL")]
docs.append(doc137)
print("doc138, 65, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 22700; AMOUNT 100; ARTICLE 1130010963; PRICE 29,27; UNIT 100; SUMMA 29,27; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 3,34; PR_ESURCH 3,50; ESURCHARGE 1,02; TOTAL 33,63; ")
doc138 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 22700 100 PC 1130010963 29,27 100 PC 29,27 428 -PP-H-BK 428 PPH black9005 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 3,34 Energy Surcharge 3,50 % 1,02 33,63''')
doc138.ents = [
   Span(doc138, 3, 4, label ="NORDER"),
   Span(doc138, 9, 12, label ="CONTRACT"),
   Span(doc138, 12, 13, label ="CONTRACT1"),
   Span(doc138, 15, 16, label ="POS"),
   Span(doc138, 16, 17, label ="AMOUNT"),
   Span(doc138, 18, 19, label ="ARTICLE"),
   Span(doc138, 19, 20, label ="PRICE"),
   Span(doc138, 20, 21, label ="UNIT"),
   Span(doc138, 22, 23, label ="SUMMA"),
   Span(doc138, 48, 49, label ="TARIFF"),
   Span(doc138, 53, 54, label ="COUNTRY"),
   Span(doc138, 56, 57, label ="PR_SURCH"),
   Span(doc138, 58, 59, label ="SURCHARGE"),
   Span(doc138, 61, 62, label ="PR_ESURCH"),
   Span(doc138, 63, 64, label ="ESURCHARGE"),
   Span(doc138, 64, 65, label ="TOTAL")]
docs.append(doc138)
print("doc139, 67, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 22800; AMOUNT 100; ARTICLE 1130007768; PRICE 65,63; UNIT 100; SUMMA 65,63; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 7,48; PR_ESURCH 3,50; ESURCHARGE 2,30; TOTAL 75,41; ")
doc139 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919**   22800 100 PC 1130007768 65,63 100 PC 65,63 532/32-PP-H-BK 532/32 PPH black9005 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 7,48 Energy Surcharge 3,50 % 2,30 75,41''')
doc139.ents = [
   Span(doc139, 3, 4, label ="NORDER"),
   Span(doc139, 9, 12, label ="CONTRACT"),
   Span(doc139, 12, 13, label ="CONTRACT1"),
   Span(doc139, 16, 17, label ="POS"),
   Span(doc139, 17, 18, label ="AMOUNT"),
   Span(doc139, 19, 20, label ="ARTICLE"),
   Span(doc139, 20, 21, label ="PRICE"),
   Span(doc139, 21, 22, label ="UNIT"),
   Span(doc139, 23, 24, label ="SUMMA"),
   Span(doc139, 50, 51, label ="TARIFF"),
   Span(doc139, 55, 56, label ="COUNTRY"),
   Span(doc139, 58, 59, label ="PR_SURCH"),
   Span(doc139, 60, 61, label ="SURCHARGE"),
   Span(doc139, 63, 64, label ="PR_ESURCH"),
   Span(doc139, 65, 66, label ="ESURCHARGE"),
   Span(doc139, 66, 67, label ="TOTAL")]
docs.append(doc139)
print("doc140, 66, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 22900; AMOUNT 1.350; ARTICLE 1130008136; PRICE 63,01; UNIT 100; SUMMA 850,64; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 96,97; PR_ESURCH 3,50; ESURCHARGE 29,77; TOTAL 977,38; ")
doc140 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 22900 1.350 PC 1130008136 63,01 100 PC 850,64 535/35-PP-H-BK 535/35 PPH black9005 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 96,97 Energy Surcharge 3,50 % 29,77 977,38''')
doc140.ents = [
   Span(doc140, 3, 4, label ="NORDER"),
   Span(doc140, 9, 12, label ="CONTRACT"),
   Span(doc140, 12, 13, label ="CONTRACT1"),
   Span(doc140, 15, 16, label ="POS"),
   Span(doc140, 16, 17, label ="AMOUNT"),
   Span(doc140, 18, 19, label ="ARTICLE"),
   Span(doc140, 19, 20, label ="PRICE"),
   Span(doc140, 20, 21, label ="UNIT"),
   Span(doc140, 22, 23, label ="SUMMA"),
   Span(doc140, 49, 50, label ="TARIFF"),
   Span(doc140, 54, 55, label ="COUNTRY"),
   Span(doc140, 57, 58, label ="PR_SURCH"),
   Span(doc140, 59, 60, label ="SURCHARGE"),
   Span(doc140, 62, 63, label ="PR_ESURCH"),
   Span(doc140, 64, 65, label ="ESURCHARGE"),
   Span(doc140, 65, 66, label ="TOTAL")]
docs.append(doc140)
print("doc141, 67, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 23000; AMOUNT 550; ARTICLE 1130010965; PRICE 45,34; UNIT 100; SUMMA 249,37; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 28,43; PR_ESURCH 3,50; ESURCHARGE 8,73; TOTAL 286,53; ")
doc141 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 23000 550 PC 1130010965 45,34 100 PC 249,37 535-PP-H-BK 535 PPH black9005 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 28,43 Energy Surcharge 3,50 % 8,73 286,53   ''')
doc141.ents = [
   Span(doc141, 3, 4, label ="NORDER"),
   Span(doc141, 9, 12, label ="CONTRACT"),
   Span(doc141, 12, 13, label ="CONTRACT1"),
   Span(doc141, 15, 16, label ="POS"),
   Span(doc141, 16, 17, label ="AMOUNT"),
   Span(doc141, 18, 19, label ="ARTICLE"),
   Span(doc141, 19, 20, label ="PRICE"),
   Span(doc141, 20, 21, label ="UNIT"),
   Span(doc141, 22, 23, label ="SUMMA"),
   Span(doc141, 49, 50, label ="TARIFF"),
   Span(doc141, 54, 55, label ="COUNTRY"),
   Span(doc141, 57, 58, label ="PR_SURCH"),
   Span(doc141, 59, 60, label ="SURCHARGE"),
   Span(doc141, 62, 63, label ="PR_ESURCH"),
   Span(doc141, 64, 65, label ="ESURCHARGE"),
   Span(doc141, 65, 66, label ="TOTAL")]
docs.append(doc141)
print("doc142, 65, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 23100; AMOUNT 650; ARTICLE 1130006044; PRICE 84,96; UNIT 100; SUMMA 552,24; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 62,96; PR_ESURCH 3,50; ESURCHARGE 19,33; TOTAL 634,53; ")
doc142 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 23100 650 PC 1130006044 84,96 100 PC 552,24 538/38 -PP-H-BK 538/38 PPH black9005 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 62,96 Energy Surcharge 3,50 % 19,33 634,53''')
doc142.ents = [
   Span(doc142, 3, 4, label ="NORDER"),
   Span(doc142, 9, 12, label ="CONTRACT"),
   Span(doc142, 12, 13, label ="CONTRACT1"),
   Span(doc142, 15, 16, label ="POS"),
   Span(doc142, 16, 17, label ="AMOUNT"),
   Span(doc142, 18, 19, label ="ARTICLE"),
   Span(doc142, 19, 20, label ="PRICE"),
   Span(doc142, 20, 21, label ="UNIT"),
   Span(doc142, 22, 23, label ="SUMMA"),
   Span(doc142, 48, 49, label ="TARIFF"),
   Span(doc142, 53, 54, label ="COUNTRY"),
   Span(doc142, 56, 57, label ="PR_SURCH"),
   Span(doc142, 58, 59, label ="SURCHARGE"),
   Span(doc142, 61, 62, label ="PR_ESURCH"),
   Span(doc142, 63, 64, label ="ESURCHARGE"),
   Span(doc142, 64, 65, label ="TOTAL")]
docs.append(doc142)
print("doc143, 66, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 23200; AMOUNT 800; ARTICLE 1130006029; PRICE 45,34; UNIT 100; SUMMA 362,72; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 41,35; PR_ESURCH 3,50; ESURCHARGE 12,70; TOTAL 416,77; ")
doc143 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 23200 800 PC 1130006029 45,34 100 PC 362,72 538-PP-H-BK 538 PPH black9005 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 41,35 Energy Surcharge 3,50 % 12,70 416,77''')
doc143.ents = [
   Span(doc143, 3, 4, label ="NORDER"),
   Span(doc143, 9, 12, label ="CONTRACT"),
   Span(doc143, 12, 13, label ="CONTRACT1"),
   Span(doc143, 15, 16, label ="POS"),
   Span(doc143, 16, 17, label ="AMOUNT"),
   Span(doc143, 18, 19, label ="ARTICLE"),
   Span(doc143, 19, 20, label ="PRICE"),
   Span(doc143, 20, 21, label ="UNIT"),
   Span(doc143, 22, 23, label ="SUMMA"),
   Span(doc143, 49, 50, label ="TARIFF"),
   Span(doc143, 54, 55, label ="COUNTRY"),
   Span(doc143, 57, 58, label ="PR_SURCH"),
   Span(doc143, 59, 60, label ="SURCHARGE"),
   Span(doc143, 62, 63, label ="PR_ESURCH"),
   Span(doc143, 64, 65, label ="ESURCHARGE"),
   Span(doc143, 65, 66, label ="TOTAL")]
docs.append(doc143)
print("doc144, 67, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 23300; AMOUNT 700; ARTICLE 1130023599; PRICE 45,34; UNIT 100; SUMMA 317,38; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 36,18; PR_ESURCH 3,50; ESURCHARGE 11,11; TOTAL 364,67; ")
doc144 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 23300 700 PC 1130023599 45,34 100 PC 317,38 542-PP-H-BK 542 PPH BLACK9005 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 36,18  Energy Surcharge 3,50 % 11,11 364,67''')
doc144.ents = [
   Span(doc144, 3, 4, label ="NORDER"),
   Span(doc144, 9, 12, label ="CONTRACT"),
   Span(doc144, 12, 13, label ="CONTRACT1"),
   Span(doc144, 15, 16, label ="POS"),
   Span(doc144, 16, 17, label ="AMOUNT"),
   Span(doc144, 18, 19, label ="ARTICLE"),
   Span(doc144, 19, 20, label ="PRICE"),
   Span(doc144, 20, 21, label ="UNIT"),
   Span(doc144, 22, 23, label ="SUMMA"),
   Span(doc144, 49, 50, label ="TARIFF"),
   Span(doc144, 54, 55, label ="COUNTRY"),
   Span(doc144, 57, 58, label ="PR_SURCH"),
   Span(doc144, 59, 60, label ="SURCHARGE"),
   Span(doc144, 63, 64, label ="PR_ESURCH"),
   Span(doc144, 65, 66, label ="ESURCHARGE"),
   Span(doc144, 66, 67, label ="TOTAL")]
docs.append(doc144)
print("doc145, 63, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 23400; AMOUNT 25; ARTICLE 1130003573; PRICE 136,30; UNIT 100; SUMMA 34,08; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 3,89; PR_ESURCH 3,50; ESURCHARGE 1,19; TOTAL 39,16; ")
doc145 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 23400 25 PC 1130003573 136,30 100 PC 34,08 644.5-PA-H 644,5 PAH packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 3,89 Energy Surcharge 3,50 % 1,19 39,16''')
doc145.ents = [
   Span(doc145, 3, 4, label ="NORDER"),
   Span(doc145, 9, 12, label ="CONTRACT"),
   Span(doc145, 12, 13, label ="CONTRACT1"),
   Span(doc145, 15, 16, label ="POS"),
   Span(doc145, 16, 17, label ="AMOUNT"),
   Span(doc145, 18, 19, label ="ARTICLE"),
   Span(doc145, 19, 20, label ="PRICE"),
   Span(doc145, 20, 21, label ="UNIT"),
   Span(doc145, 22, 23, label ="SUMMA"),
   Span(doc145, 46, 47, label ="TARIFF"),
   Span(doc145, 51, 52, label ="COUNTRY"),
   Span(doc145, 54, 55, label ="PR_SURCH"),
   Span(doc145, 56, 57, label ="SURCHARGE"),
   Span(doc145, 59, 60, label ="PR_ESURCH"),
   Span(doc145, 61, 62, label ="ESURCHARGE"),
   Span(doc145, 62, 63, label ="TOTAL")]
docs.append(doc145)
print("doc146, 63, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 23500; AMOUNT 700; ARTICLE 1130003576; PRICE 183,80; UNIT 100; SUMMA 1.286,60; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 146,67; PR_ESURCH 3,50; ESURCHARGE 45,03; TOTAL 1.478,30; ")
doc146 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 23500 700 PC 1130003576 183,80 100 PC 1.286,60 648.3-PA-H 648,3 PAH packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 146,67 Energy Surcharge 3,50 % 45,03 1.478,30''')
doc146.ents = [
   Span(doc146, 3, 4, label ="NORDER"),
   Span(doc146, 9, 12, label ="CONTRACT"),
   Span(doc146, 12, 13, label ="CONTRACT1"),
   Span(doc146, 15, 16, label ="POS"),
   Span(doc146, 16, 17, label ="AMOUNT"),
   Span(doc146, 18, 19, label ="ARTICLE"),
   Span(doc146, 19, 20, label ="PRICE"),
   Span(doc146, 20, 21, label ="UNIT"),
   Span(doc146, 22, 23, label ="SUMMA"),
   Span(doc146, 46, 47, label ="TARIFF"),
   Span(doc146, 51, 52, label ="COUNTRY"),
   Span(doc146, 54, 55, label ="PR_SURCH"),
   Span(doc146, 56, 57, label ="SURCHARGE"),
   Span(doc146, 59, 60, label ="PR_ESURCH"),
   Span(doc146, 61, 62, label ="ESURCHARGE"),
   Span(doc146, 62, 63, label ="TOTAL")]
docs.append(doc146)
print("doc147, 64, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 23600; AMOUNT 25; ARTICLE 1130003579; PRICE 136,30; UNIT 100; SUMMA 34,08; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 3,89; PR_ESURCH 3,50; ESURCHARGE 1,19; TOTAL 39,16; ")
doc147 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 23600 25 PC 1130003579 136,30 100 PC 34,08 650.8-PA-H 650,8 PAH packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097    Country of origin: Germany Material Surcharge 11,40 % 3,89 Energy Surcharge 3,50 % 1,19 39,16''')
doc147.ents = [
   Span(doc147, 3, 4, label ="NORDER"),
   Span(doc147, 9, 12, label ="CONTRACT"),
   Span(doc147, 12, 13, label ="CONTRACT1"),
   Span(doc147, 15, 16, label ="POS"),
   Span(doc147, 16, 17, label ="AMOUNT"),
   Span(doc147, 18, 19, label ="ARTICLE"),
   Span(doc147, 19, 20, label ="PRICE"),
   Span(doc147, 20, 21, label ="UNIT"),
   Span(doc147, 22, 23, label ="SUMMA"),
   Span(doc147, 46, 47, label ="TARIFF"),
   Span(doc147, 52, 53, label ="COUNTRY"),
   Span(doc147, 55, 56, label ="PR_SURCH"),
   Span(doc147, 57, 58, label ="SURCHARGE"),
   Span(doc147, 60, 61, label ="PR_ESURCH"),
   Span(doc147, 62, 63, label ="ESURCHARGE"),
   Span(doc147, 63, 64, label ="TOTAL")]
docs.append(doc147)
print("doc148, 69, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 23700; AMOUNT 6.200; ARTICLE 1130023498; PRICE 37,84; UNIT 100; SUMMA 2.346,08; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 267,45; PR_ESURCH 3,50; ESURCHARGE 82,11; TOTAL 2.695,64; ")
doc148 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 23700 6.200 PC 1130023498 37,84 100 PC 2.346,08 LBBU-108/08-SA-M8/U5/16 LBBU 108/08 SA M8-U5/16 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 267,45 Energy Surcharge 3,50 % 82,11 2.695,64''')
doc148.ents = [
   Span(doc148, 3, 4, label ="NORDER"),
   Span(doc148, 9, 12, label ="CONTRACT"),
   Span(doc148, 12, 13, label ="CONTRACT1"),
   Span(doc148, 15, 16, label ="POS"),
   Span(doc148, 16, 17, label ="AMOUNT"),
   Span(doc148, 18, 19, label ="ARTICLE"),
   Span(doc148, 19, 20, label ="PRICE"),
   Span(doc148, 20, 21, label ="UNIT"),
   Span(doc148, 22, 23, label ="SUMMA"),
   Span(doc148, 52, 53, label ="TARIFF"),
   Span(doc148, 57, 58, label ="COUNTRY"),
   Span(doc148, 60, 61, label ="PR_SURCH"),
   Span(doc148, 62, 63, label ="SURCHARGE"),
   Span(doc148, 65, 66, label ="PR_ESURCH"),
   Span(doc148, 67, 68, label ="ESURCHARGE"),
   Span(doc148, 68, 69, label ="TOTAL")]
docs.append(doc148)
print("doc149, 69, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 23800; AMOUNT 1.500; ARTICLE 1130023472; PRICE 31,28; UNIT 100; SUMMA 469,20; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 53,49; PR_ESURCH 3,50; ESURCHARGE 16,42; TOTAL 539,11; ")
doc149 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 23800 1.500 PC 1130023472 31,28 100 PC 469,20 LBBU-108-SA-M8/U5/16 LBBU 108 SA M8-U5/16 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 53,49 Energy Surcharge 3,50 % 16,42 539,11''')
doc149.ents = [
   Span(doc149, 3, 4, label ="NORDER"),
   Span(doc149, 9, 12, label ="CONTRACT"),
   Span(doc149, 12, 13, label ="CONTRACT1"),
   Span(doc149, 15, 16, label ="POS"),
   Span(doc149, 16, 17, label ="AMOUNT"),
   Span(doc149, 18, 19, label ="ARTICLE"),
   Span(doc149, 19, 20, label ="PRICE"),
   Span(doc149, 20, 21, label ="UNIT"),
   Span(doc149, 22, 23, label ="SUMMA"),
   Span(doc149, 52, 53, label ="TARIFF"),
   Span(doc149, 57, 58, label ="COUNTRY"),
   Span(doc149, 60, 61, label ="PR_SURCH"),
   Span(doc149, 62, 63, label ="SURCHARGE"),
   Span(doc149, 65, 66, label ="PR_ESURCH"),
   Span(doc149, 67, 68, label ="ESURCHARGE"),
   Span(doc149, 68, 69, label ="TOTAL")]
docs.append(doc149)
print("doc150, 70, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 23900; AMOUNT 600; ARTICLE 1130023553; PRICE 37,84; UNIT 100; SUMMA 227,04; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 25,88; PR_ESURCH 3,50; ESURCHARGE 7,95; TOTAL 260,87; ")
doc150 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 23900 600 PC 1130023553 37,84 100 PC 227,04 LBBU-112.7/12.7-SA-M8/U5/16 LBBU 112,7/12,7 SA M8-U5/16    packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 25,88 Energy Surcharge 3,50 % 7,95 260,87''')
doc150.ents = [
   Span(doc150, 3, 4, label ="NORDER"),
   Span(doc150, 9, 12, label ="CONTRACT"),
   Span(doc150, 12, 13, label ="CONTRACT1"),
   Span(doc150, 15, 16, label ="POS"),
   Span(doc150, 16, 17, label ="AMOUNT"),
   Span(doc150, 18, 19, label ="ARTICLE"),
   Span(doc150, 19, 20, label ="PRICE"),
   Span(doc150, 20, 21, label ="UNIT"),
   Span(doc150, 22, 23, label ="SUMMA"),
   Span(doc150, 53, 54, label ="TARIFF"),
   Span(doc150, 58, 59, label ="COUNTRY"),
   Span(doc150, 61, 62, label ="PR_SURCH"),
   Span(doc150, 63, 64, label ="SURCHARGE"),
   Span(doc150, 66, 67, label ="PR_ESURCH"),
   Span(doc150, 68, 69, label ="ESURCHARGE"),
   Span(doc150, 69, 70, label ="TOTAL")]
docs.append(doc150)
print("doc151, 69, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 24000; AMOUNT 350; ARTICLE 1130023477; PRICE 31,28; UNIT 100; SUMMA 109,48; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 12,48; PR_ESURCH 3,50; ESURCHARGE 3,83; TOTAL 125,79; ")
doc151 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 24000 350 PC 1130023477 31,28 100 PC 109,48 LBBU-112.7-SA-M8/U5/16 LBBU 112,7 SA M8-U5/16 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 12,48 Energy Surcharge 3,50 % 3,83 125,79''')
doc151.ents = [
   Span(doc151, 3, 4, label ="NORDER"),
   Span(doc151, 9, 12, label ="CONTRACT"),
   Span(doc151, 12, 13, label ="CONTRACT1"),
   Span(doc151, 15, 16, label ="POS"),
   Span(doc151, 16, 17, label ="AMOUNT"),
   Span(doc151, 18, 19, label ="ARTICLE"),
   Span(doc151, 19, 20, label ="PRICE"),
   Span(doc151, 20, 21, label ="UNIT"),
   Span(doc151, 22, 23, label ="SUMMA"),
   Span(doc151, 52, 53, label ="TARIFF"),
   Span(doc151, 57, 58, label ="COUNTRY"),
   Span(doc151, 60, 61, label ="PR_SURCH"),
   Span(doc151, 62, 63, label ="SURCHARGE"),
   Span(doc151, 65, 66, label ="PR_ESURCH"),
   Span(doc151, 67, 68, label ="ESURCHARGE"),
   Span(doc151, 68, 69, label ="TOTAL")]
docs.append(doc151)
print("doc152, 69, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 24100; AMOUNT 1.000; ARTICLE 1130029812; PRICE 37,84; UNIT 100; SUMMA 378,40; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 43,14; PR_ESURCH 3,50; ESURCHARGE 13,24; TOTAL 434,78; ")
doc152 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 24100 1.000 PC 1130029812 37,84 100 PC 378,40 LBBU-11 2/08 -SA-M8/U5/16 LBBU 112/08 SA M8-U5/16 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 43,14 Energy Surcharge 3,50 % 13,24 434,78''')
doc152.ents = [
   Span(doc152, 3, 4, label ="NORDER"),
   Span(doc152, 9, 12, label ="CONTRACT"),
   Span(doc152, 12, 13, label ="CONTRACT1"),
   Span(doc152, 15, 16, label ="POS"),
   Span(doc152, 16, 17, label ="AMOUNT"),
   Span(doc152, 18, 19, label ="ARTICLE"),
   Span(doc152, 19, 20, label ="PRICE"),
   Span(doc152, 20, 21, label ="UNIT"),
   Span(doc152, 22, 23, label ="SUMMA"),
   Span(doc152, 52, 53, label ="TARIFF"),
   Span(doc152, 57, 58, label ="COUNTRY"),
   Span(doc152, 60, 61, label ="PR_SURCH"),
   Span(doc152, 62, 63, label ="SURCHARGE"),
   Span(doc152, 65, 66, label ="PR_ESURCH"),
   Span(doc152, 67, 68, label ="ESURCHARGE"),
   Span(doc152, 68, 69, label ="TOTAL")]
docs.append(doc152)
print("doc153, 70, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 24200; AMOUNT 1.500; ARTICLE 1130022741; PRICE 37,84; UNIT 100; SUMMA 567,60; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 64,71; PR_ESURCH 3,50; ESURCHARGE 19,87; TOTAL 652,18; ")
doc153 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919**   24200 1.500 PC 1130022741 37,84 100 PC 567,60 LBBU-112/12-SA-M8/U5/16 LBBU 112/12 SA M8-U5/16 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 64,71 Energy Surcharge 3,50 % 19,87 652,18''')
doc153.ents = [
   Span(doc153, 3, 4, label ="NORDER"),
   Span(doc153, 9, 12, label ="CONTRACT"),
   Span(doc153, 12, 13, label ="CONTRACT1"),
   Span(doc153, 16, 17, label ="POS"),
   Span(doc153, 17, 18, label ="AMOUNT"),
   Span(doc153, 19, 20, label ="ARTICLE"),
   Span(doc153, 20, 21, label ="PRICE"),
   Span(doc153, 21, 22, label ="UNIT"),
   Span(doc153, 23, 24, label ="SUMMA"),
   Span(doc153, 53, 54, label ="TARIFF"),
   Span(doc153, 58, 59, label ="COUNTRY"),
   Span(doc153, 61, 62, label ="PR_SURCH"),
   Span(doc153, 63, 64, label ="SURCHARGE"),
   Span(doc153, 66, 67, label ="PR_ESURCH"),
   Span(doc153, 68, 69, label ="ESURCHARGE"),
   Span(doc153, 69, 70, label ="TOTAL")]
docs.append(doc153)
print("doc154, 71, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 24300; AMOUNT 4.000; ARTICLE 1130023476; PRICE 31,28; UNIT 100; SUMMA 1.251,20; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 142,64; PR_ESURCH 3,50; ESURCHARGE 43,79; TOTAL 1.437; ")
doc154 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 24300 4.000 PC 1130023476 31,28 100 PC 1.251,20 LBBU-112-SA-M8/U5/16 LBBU 112 SA M8-U5/16 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 142,64 Energy Surcharge 3,50 % 43,79 1.437 ,63''')
doc154.ents = [
   Span(doc154, 3, 4, label ="NORDER"),
   Span(doc154, 9, 12, label ="CONTRACT"),
   Span(doc154, 12, 13, label ="CONTRACT1"),
   Span(doc154, 15, 16, label ="POS"),
   Span(doc154, 16, 17, label ="AMOUNT"),
   Span(doc154, 18, 19, label ="ARTICLE"),
   Span(doc154, 19, 20, label ="PRICE"),
   Span(doc154, 20, 21, label ="UNIT"),
   Span(doc154, 22, 23, label ="SUMMA"),
   Span(doc154, 52, 53, label ="TARIFF"),
   Span(doc154, 57, 58, label ="COUNTRY"),
   Span(doc154, 60, 61, label ="PR_SURCH"),
   Span(doc154, 62, 63, label ="SURCHARGE"),
   Span(doc154, 65, 66, label ="PR_ESURCH"),
   Span(doc154, 67, 68, label ="ESURCHARGE"),
   Span(doc154, 68, 69, label ="TOTAL")]
docs.append(doc154)
print("doc155, 58, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 24400; AMOUNT 600; ARTICLE 6100196633; PRICE 52,37; UNIT 100; SUMMA 314,22; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 35,82; PR_ESURCH 3,50; ESURCHARGE 11,00; TOTAL 361,04; ")
doc155 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 24400 600 PC 6100196633 52,37 100 PC 314,22 LBBU-218/12-SA-M8/U5/16/2 packed per each item Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 35,82 Energy Surcharge 3,50 % 11,00 361,04''')
doc155.ents = [
   Span(doc155, 3, 4, label ="NORDER"),
   Span(doc155, 9, 12, label ="CONTRACT"),
   Span(doc155, 12, 13, label ="CONTRACT1"),
   Span(doc155, 15, 16, label ="POS"),
   Span(doc155, 16, 17, label ="AMOUNT"),
   Span(doc155, 18, 19, label ="ARTICLE"),
   Span(doc155, 19, 20, label ="PRICE"),
   Span(doc155, 20, 21, label ="UNIT"),
   Span(doc155, 22, 23, label ="SUMMA"),
   Span(doc155, 41, 42, label ="TARIFF"),
   Span(doc155, 46, 47, label ="COUNTRY"),
   Span(doc155, 49, 50, label ="PR_SURCH"),
   Span(doc155, 51, 52, label ="SURCHARGE"),
   Span(doc155, 54, 55, label ="PR_ESURCH"),
   Span(doc155, 56, 57, label ="ESURCHARGE"),
   Span(doc155, 57, 58, label ="TOTAL")]
docs.append(doc155)
print("doc156, 59, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 24500; AMOUNT 150; ARTICLE 6100196642; PRICE 52,37; UNIT 100; SUMMA 78,56; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 8,96; PR_ESURCH 3,50; ESURCHARGE 2,75; TOTAL 90,27; ")
doc156 = nlp('''Order number: 2390896   Purchase order number: N SR-1-06 1919** 24500 150 PC 6100196642 52,37 100 PC 78,56 LBBU-219/12.7-SA-M8/U5/16/2 packed per each item Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 8,96 Energy Surcharge 3,50 % 2,75 90,27''')
doc156.ents = [
   Span(doc156, 3, 4, label ="NORDER"),
   Span(doc156, 10, 13, label ="CONTRACT"),
   Span(doc156, 13, 14, label ="CONTRACT1"),
   Span(doc156, 16, 17, label ="POS"),
   Span(doc156, 17, 18, label ="AMOUNT"),
   Span(doc156, 19, 20, label ="ARTICLE"),
   Span(doc156, 20, 21, label ="PRICE"),
   Span(doc156, 21, 22, label ="UNIT"),
   Span(doc156, 23, 24, label ="SUMMA"),
   Span(doc156, 42, 43, label ="TARIFF"),
   Span(doc156, 47, 48, label ="COUNTRY"),
   Span(doc156, 50, 51, label ="PR_SURCH"),
   Span(doc156, 52, 53, label ="SURCHARGE"),
   Span(doc156, 55, 56, label ="PR_ESURCH"),
   Span(doc156, 57, 58, label ="ESURCHARGE"),
   Span(doc156, 58, 59, label ="TOTAL")]
docs.append(doc156)
print("doc157, 63, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 24600; AMOUNT 800; ARTICLE 6100196646; PRICE 52,37; UNIT 100; SUMMA 418,96; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 47,76; PR_ESURCH 3,50; ESURCHARGE 14,66; TOTAL 481,38; ")
doc157 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 24600 800 PC 6100196646 52,37 100 PC 418,96 LBBU-219/19-SA-M8/U5/16/2 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 47,76 Energy Surcharge 3,50 % 14,66 481,38''')
doc157.ents = [
   Span(doc157, 3, 4, label ="NORDER"),
   Span(doc157, 9, 12, label ="CONTRACT"),
   Span(doc157, 12, 13, label ="CONTRACT1"),
   Span(doc157, 15, 16, label ="POS"),
   Span(doc157, 16, 17, label ="AMOUNT"),
   Span(doc157, 18, 19, label ="ARTICLE"),
   Span(doc157, 19, 20, label ="PRICE"),
   Span(doc157, 20, 21, label ="UNIT"),
   Span(doc157, 22, 23, label ="SUMMA"),
   Span(doc157, 46, 47, label ="TARIFF"),
   Span(doc157, 51, 52, label ="COUNTRY"),
   Span(doc157, 54, 55, label ="PR_SURCH"),
   Span(doc157, 56, 57, label ="SURCHARGE"),
   Span(doc157, 59, 60, label ="PR_ESURCH"),
   Span(doc157, 61, 62, label ="ESURCHARGE"),
   Span(doc157, 62, 63, label ="TOTAL")]
docs.append(doc157)
print("doc158, 69, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 24700; AMOUNT 1.100; ARTICLE 1130025662; PRICE 94,23; UNIT 100; SUMMA 1.036,53; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 118,16; PR_ESURCH 3,50; ESURCHARGE 36,28; TOTAL 1.190,97; ")
doc158 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 24700 1.100 PC 1130025662 94,23 100 PC 1.036,53 LBBU-322/22-SA-M8/U5/16 LBBU 322/22 SA M8-U5/16 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 118,16 Energy Surcharge 3,50 % 36,28 1.190,97''')
doc158.ents = [
   Span(doc158, 3, 4, label ="NORDER"),
   Span(doc158, 9, 12, label ="CONTRACT"),
   Span(doc158, 12, 13, label ="CONTRACT1"),
   Span(doc158, 15, 16, label ="POS"),
   Span(doc158, 16, 17, label ="AMOUNT"),
   Span(doc158, 18, 19, label ="ARTICLE"),
   Span(doc158, 19, 20, label ="PRICE"),
   Span(doc158, 20, 21, label ="UNIT"),
   Span(doc158, 22, 23, label ="SUMMA"),
   Span(doc158, 52, 53, label ="TARIFF"),
   Span(doc158, 57, 58, label ="COUNTRY"),
   Span(doc158, 60, 61, label ="PR_SURCH"),
   Span(doc158, 62, 63, label ="SURCHARGE"),
   Span(doc158, 65, 66, label ="PR_ESURCH"),
   Span(doc158, 67, 68, label ="ESURCHARGE"),
   Span(doc158, 68, 69, label ="TOTAL")]
docs.append(doc158)
print("doc159, 70, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 24800; AMOUNT 1.000; ARTICLE 1130025898; PRICE 70,37; UNIT 100; SUMMA 703,70; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 80,22; PR_ESURCH 3,50; ESURCHARGE 24,63; TOTAL 808,55; ")
doc159 = nlp('''Order number: 2390896   Purchase order number: N SR-1-06 1919** 24800 1.000 PC 1130025898 70,37 100 PC 703,70 LBBU-322-SA-M8/U5/16 LBBU 322 SA M8-U5/16 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 80,22 Energy Surcharge 3,50 % 24,63 808,55''')
doc159.ents = [
   Span(doc159, 3, 4, label ="NORDER"),
   Span(doc159, 10, 13, label ="CONTRACT"),
   Span(doc159, 13, 14, label ="CONTRACT1"),
   Span(doc159, 16, 17, label ="POS"),
   Span(doc159, 17, 18, label ="AMOUNT"),
   Span(doc159, 19, 20, label ="ARTICLE"),
   Span(doc159, 20, 21, label ="PRICE"),
   Span(doc159, 21, 22, label ="UNIT"),
   Span(doc159, 23, 24, label ="SUMMA"),
   Span(doc159, 53, 54, label ="TARIFF"),
   Span(doc159, 58, 59, label ="COUNTRY"),
   Span(doc159, 61, 62, label ="PR_SURCH"),
   Span(doc159, 63, 64, label ="SURCHARGE"),
   Span(doc159, 66, 67, label ="PR_ESURCH"),
   Span(doc159, 68, 69, label ="ESURCHARGE"),
   Span(doc159, 69, 70, label ="TOTAL")]
docs.append(doc159)
print("doc160, 69, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 24900; AMOUNT 25; ARTICLE 1130025899; PRICE 94,23; UNIT 100; SUMMA 23,56; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 2,69; PR_ESURCH 3,50; ESURCHARGE 0,82; TOTAL 27,07; ")
doc160 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 24900 25 PC 1130025899 94,23 100 PC 23,56 LBBU-323-SA-M8/U5/16 LBBU 323 SA M8-U5/16 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 2,69 Energy Surcharge 3,50 % 0,82 27,07''')
doc160.ents = [
   Span(doc160, 3, 4, label ="NORDER"),
   Span(doc160, 9, 12, label ="CONTRACT"),
   Span(doc160, 12, 13, label ="CONTRACT1"),
   Span(doc160, 15, 16, label ="POS"),
   Span(doc160, 16, 17, label ="AMOUNT"),
   Span(doc160, 18, 19, label ="ARTICLE"),
   Span(doc160, 19, 20, label ="PRICE"),
   Span(doc160, 20, 21, label ="UNIT"),
   Span(doc160, 22, 23, label ="SUMMA"),
   Span(doc160, 52, 53, label ="TARIFF"),
   Span(doc160, 57, 58, label ="COUNTRY"),
   Span(doc160, 60, 61, label ="PR_SURCH"),
   Span(doc160, 62, 63, label ="SURCHARGE"),
   Span(doc160, 65, 66, label ="PR_ESURCH"),
   Span(doc160, 67, 68, label ="ESURCHARGE"),
   Span(doc160, 68, 69, label ="TOTAL")]
docs.append(doc160)
print("doc161, 70, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 25000; AMOUNT 150; ARTICLE 1130025904; PRICE 94,23; UNIT 100; SUMMA 141,35; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 16,11; PR_ESURCH 3,50; ESURCHARGE 4,95; TOTAL 162,41; ")
doc161 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 25000 150 PC 1130025904 94,23 100 PC 141,35 LBBU-325.4/25.4-SA-M8/U5/16 LBBU 325,4/25,4 SA M8-U5/16 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 16,11 Energy Surcharge 3,50 % 4,95   162,41''')
doc161.ents = [
   Span(doc161, 3, 4, label ="NORDER"),
   Span(doc161, 9, 12, label ="CONTRACT"),
   Span(doc161, 12, 13, label ="CONTRACT1"),
   Span(doc161, 15, 16, label ="POS"),
   Span(doc161, 16, 17, label ="AMOUNT"),
   Span(doc161, 18, 19, label ="ARTICLE"),
   Span(doc161, 19, 20, label ="PRICE"),
   Span(doc161, 20, 21, label ="UNIT"),
   Span(doc161, 22, 23, label ="SUMMA"),
   Span(doc161, 52, 53, label ="TARIFF"),
   Span(doc161, 57, 58, label ="COUNTRY"),
   Span(doc161, 60, 61, label ="PR_SURCH"),
   Span(doc161, 62, 63, label ="SURCHARGE"),
   Span(doc161, 65, 66, label ="PR_ESURCH"),
   Span(doc161, 67, 68, label ="ESURCHARGE"),
   Span(doc161, 69, 70, label ="TOTAL")]
docs.append(doc161)
print("doc162, 69, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 25100; AMOUNT 100; ARTICLE 1130025664; PRICE 94,23; UNIT 100; SUMMA 94,23; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 10,74; PR_ESURCH 3,50; ESURCHARGE 3,30; TOTAL 108,27; ")
doc162 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 25100 100 PC 1130025664 94,23 100 PC 94,23 LBBU-325.4-SA-M8/U5/16 LBBU 325,4 SA M8-U5/16 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 10,74 Energy Surcharge 3,50 % 3,30 108,27''')
doc162.ents = [
   Span(doc162, 3, 4, label ="NORDER"),
   Span(doc162, 9, 12, label ="CONTRACT"),
   Span(doc162, 12, 13, label ="CONTRACT1"),
   Span(doc162, 15, 16, label ="POS"),
   Span(doc162, 16, 17, label ="AMOUNT"),
   Span(doc162, 18, 19, label ="ARTICLE"),
   Span(doc162, 19, 20, label ="PRICE"),
   Span(doc162, 20, 21, label ="UNIT"),
   Span(doc162, 22, 23, label ="SUMMA"),
   Span(doc162, 52, 53, label ="TARIFF"),
   Span(doc162, 57, 58, label ="COUNTRY"),
   Span(doc162, 60, 61, label ="PR_SURCH"),
   Span(doc162, 62, 63, label ="SURCHARGE"),
   Span(doc162, 65, 66, label ="PR_ESURCH"),
   Span(doc162, 67, 68, label ="ESURCHARGE"),
   Span(doc162, 68, 69, label ="TOTAL")]
docs.append(doc162)
print("doc163, 68, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 25200; AMOUNT 50; ARTICLE 1130025900; PRICE 70,37; UNIT 100; SUMMA 35,19; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 4,01; PR_ESURCH 3,50; ESURCHARGE 1,23; TOTAL 40,43; ")
doc163 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 25200 50 PC 1130025900 70,37 100 PC 35,19 LBBU-328 -SA-M8/U5/16 LBBU 328 SA M8-U5/16 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 4,01 Energy Surcharge 3,50 % 1,23 40,43''')
doc163.ents = [
   Span(doc163, 3, 4, label ="NORDER"),
   Span(doc163, 9, 12, label ="CONTRACT"),
   Span(doc163, 12, 13, label ="CONTRACT1"),
   Span(doc163, 15, 16, label ="POS"),
   Span(doc163, 16, 17, label ="AMOUNT"),
   Span(doc163, 18, 19, label ="ARTICLE"),
   Span(doc163, 19, 20, label ="PRICE"),
   Span(doc163, 20, 21, label ="UNIT"),
   Span(doc163, 22, 23, label ="SUMMA"),
   Span(doc163, 51, 52, label ="TARIFF"),
   Span(doc163, 56, 57, label ="COUNTRY"),
   Span(doc163, 59, 60, label ="PR_SURCH"),
   Span(doc163, 61, 62, label ="SURCHARGE"),
   Span(doc163, 64, 65, label ="PR_ESURCH"),
   Span(doc163, 66, 67, label ="ESURCHARGE"),
   Span(doc163, 67, 68, label ="TOTAL")]
docs.append(doc163)
print("doc164, 70, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 25300; AMOUNT 200; ARTICLE 1130025901; PRICE 70,37; UNIT 100; SUMMA 140,74; TARIFF 39269097; COUNTRY Germany   ; PR_SURCH 11,40; SURCHARGE 16,04; PR_ESURCH 3,50; ESURCHARGE 4,93; TOTAL 161,71; ")
doc164 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 25300 200 PC 1130025901 70,37 100 PC 140,74 LBBU-330-SA-M8/U5/16 LBBU 330 SA M8-U5/16 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany   Material Surcharge 11,40 % 16,04 Energy Surcharge 3,50 % 4,93 161,71''')
doc164.ents = [
   Span(doc164, 3, 4, label ="NORDER"),
   Span(doc164, 9, 12, label ="CONTRACT"),
   Span(doc164, 12, 13, label ="CONTRACT1"),
   Span(doc164, 15, 16, label ="POS"),
   Span(doc164, 16, 17, label ="AMOUNT"),
   Span(doc164, 18, 19, label ="ARTICLE"),
   Span(doc164, 19, 20, label ="PRICE"),
   Span(doc164, 20, 21, label ="UNIT"),
   Span(doc164, 22, 23, label ="SUMMA"),
   Span(doc164, 52, 53, label ="TARIFF"),
   Span(doc164, 57, 59, label ="COUNTRY"),
   Span(doc164, 61, 62, label ="PR_SURCH"),
   Span(doc164, 63, 64, label ="SURCHARGE"),
   Span(doc164, 66, 67, label ="PR_ESURCH"),
   Span(doc164, 68, 69, label ="ESURCHARGE"),
   Span(doc164, 69, 70, label ="TOTAL")]
docs.append(doc164)
print("doc165, 62, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 25400; AMOUNT 200; ARTICLE 1130004823; PRICE 13,12; UNIT 100; SUMMA 26,24; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 2,99; PR_ESURCH 3,50; ESURCHARGE 0,92; TOTAL 30,15; ")
doc165 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 25400 200 PC 1130004823 13,12 100 PC 26,24 LN-312-PA LN 312 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 2,99 Energy Surcharge 3,50 % 0,92 30,15''')
doc165.ents = [
   Span(doc165, 3, 4, label ="NORDER"),
   Span(doc165, 9, 12, label ="CONTRACT"),
   Span(doc165, 12, 13, label ="CONTRACT1"),
   Span(doc165, 15, 16, label ="POS"),
   Span(doc165, 16, 17, label ="AMOUNT"),
   Span(doc165, 18, 19, label ="ARTICLE"),
   Span(doc165, 19, 20, label ="PRICE"),
   Span(doc165, 20, 21, label ="UNIT"),
   Span(doc165, 22, 23, label ="SUMMA"),
   Span(doc165, 45, 46, label ="TARIFF"),
   Span(doc165, 50, 51, label ="COUNTRY"),
   Span(doc165, 53, 54, label ="PR_SURCH"),
   Span(doc165, 55, 56, label ="SURCHARGE"),
   Span(doc165, 58, 59, label ="PR_ESURCH"),
   Span(doc165, 60, 61, label ="ESURCHARGE"),
   Span(doc165, 61, 62, label ="TOTAL")]
docs.append(doc165)
print("doc166, 62, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 25500; AMOUNT 800; ARTICLE 1130017263; PRICE 16,16; UNIT 100; SUMMA 129,28; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 14,74; PR_ESURCH 3,50; ESURCHARGE 4,52; TOTAL 148,54; ")
doc166 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 25500 800 PC 1130017263 16,16 100 PC 129,28 LNGF-212.7/12.7-PA LNGF 212,7/12,7 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 14,74 Energy Surcharge 3,50 % 4,52 148,54''')
doc166.ents = [
   Span(doc166, 3, 4, label ="NORDER"),
   Span(doc166, 9, 12, label ="CONTRACT"),
   Span(doc166, 12, 13, label ="CONTRACT1"),
   Span(doc166, 15, 16, label ="POS"),
   Span(doc166, 16, 17, label ="AMOUNT"),
   Span(doc166, 18, 19, label ="ARTICLE"),
   Span(doc166, 19, 20, label ="PRICE"),
   Span(doc166, 20, 21, label ="UNIT"),
   Span(doc166, 22, 23, label ="SUMMA"),
   Span(doc166, 45, 46, label ="TARIFF"),
   Span(doc166, 50, 51, label ="COUNTRY"),
   Span(doc166, 53, 54, label ="PR_SURCH"),
   Span(doc166, 55, 56, label ="SURCHARGE"),
   Span(doc166, 58, 59, label ="PR_ESURCH"),
   Span(doc166, 60, 61, label ="ESURCHARGE"),
   Span(doc166, 61, 62, label ="TOTAL")]
docs.append(doc166)
print("doc167, 66, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 25600; AMOUNT 200; ARTICLE 1130029312; PRICE 10,84; UNIT 100; SUMMA 21,68; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 2,47; PR_ESURCH 3,50; ESURCHARGE 0,76; TOTAL 24,91; ")
doc167 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 25600 200 PC 1130029312 10,84 100 PC 21,68 LNUF-212/08-PP-BK LNUF 212/08 PP black9005 packed per each item Product description: Pipe clamp    Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 2,47 Energy Surcharge 3,50 % 0,76 24,91''')
doc167.ents = [
   Span(doc167, 3, 4, label ="NORDER"),
   Span(doc167, 9, 12, label ="CONTRACT"),
   Span(doc167, 12, 13, label ="CONTRACT1"),
   Span(doc167, 15, 16, label ="POS"),
   Span(doc167, 16, 17, label ="AMOUNT"),
   Span(doc167, 18, 19, label ="ARTICLE"),
   Span(doc167, 19, 20, label ="PRICE"),
   Span(doc167, 20, 21, label ="UNIT"),
   Span(doc167, 22, 23, label ="SUMMA"),
   Span(doc167, 49, 50, label ="TARIFF"),
   Span(doc167, 54, 55, label ="COUNTRY"),
   Span(doc167, 57, 58, label ="PR_SURCH"),
   Span(doc167, 59, 60, label ="SURCHARGE"),
   Span(doc167, 62, 63, label ="PR_ESURCH"),
   Span(doc167, 64, 65, label ="ESURCHARGE"),
   Span(doc167, 65, 66, label ="TOTAL")]
docs.append(doc167)
print("doc168, 62, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 25700; AMOUNT 300; ARTICLE 1130017319; PRICE 20,78; UNIT 100; SUMMA 62,34; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 7,11; PR_ESURCH 3,50; ESURCHARGE 2,18; TOTAL 71,63; ")
doc168 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 25700 300 PC 1130017319 20,78 100 PC 62,34 LNUF-315/12-PA LNUF 315/12 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 7,11 Energy Surcharge 3,50 % 2,18 71,63''')
doc168.ents = [
   Span(doc168, 3, 4, label ="NORDER"),
   Span(doc168, 9, 12, label ="CONTRACT"),
   Span(doc168, 12, 13, label ="CONTRACT1"),
   Span(doc168, 15, 16, label ="POS"),
   Span(doc168, 16, 17, label ="AMOUNT"),
   Span(doc168, 18, 19, label ="ARTICLE"),
   Span(doc168, 19, 20, label ="PRICE"),
   Span(doc168, 20, 21, label ="UNIT"),
   Span(doc168, 22, 23, label ="SUMMA"),
   Span(doc168, 45, 46, label ="TARIFF"),
   Span(doc168, 50, 51, label ="COUNTRY"),
   Span(doc168, 53, 54, label ="PR_SURCH"),
   Span(doc168, 55, 56, label ="SURCHARGE"),
   Span(doc168, 58, 59, label ="PR_ESURCH"),
   Span(doc168, 60, 61, label ="ESURCHARGE"),
   Span(doc168, 61, 62, label ="TOTAL")]
docs.append(doc168)
print("doc169, 65, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 25800; AMOUNT 400; ARTICLE 1130029278; PRICE 18,27; UNIT 100; SUMMA 73,08; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 8,33; PR_ESURCH 3,50; ESURCHARGE 2,56; TOTAL 83,97; ")
doc169 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 25800 400 PC 1130029278 18,27 100 PC 73,08 LNUF-422/15-PP-BK LNUF 422/15 PP black9005 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 8,33 Energy Surcharge 3,50 % 2,56 83,97''')
doc169.ents = [
   Span(doc169, 3, 4, label ="NORDER"),
   Span(doc169, 9, 12, label ="CONTRACT"),
   Span(doc169, 12, 13, label ="CONTRACT1"),
   Span(doc169, 15, 16, label ="POS"),
   Span(doc169, 16, 17, label ="AMOUNT"),
   Span(doc169, 18, 19, label ="ARTICLE"),
   Span(doc169, 19, 20, label ="PRICE"),
   Span(doc169, 20, 21, label ="UNIT"),
   Span(doc169, 22, 23, label ="SUMMA"),
   Span(doc169, 48, 49, label ="TARIFF"),
   Span(doc169, 53, 54, label ="COUNTRY"),
   Span(doc169, 56, 57, label ="PR_SURCH"),
   Span(doc169, 58, 59, label ="SURCHARGE"),
   Span(doc169, 61, 62, label ="PR_ESURCH"),
   Span(doc169, 63, 64, label ="ESURCHARGE"),
   Span(doc169, 64, 65, label ="TOTAL")]
docs.append(doc169)
print("doc170, 66, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 25900; AMOUNT 200; ARTICLE 1130029397; PRICE 18,27; UNIT 100; SUMMA 36,54; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 4,17; PR_ESURCH 3,50; ESURCHARGE 1,28; TOTAL 41,99; ")
doc170 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 25900 200 PC 1130029397 18,27 100 PC 36,54 LNUF-422/18-PP-BK    LNUF 422/18 PP black9005 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 4,17 Energy Surcharge 3,50 % 1,28 41,99''')
doc170.ents = [
   Span(doc170, 3, 4, label ="NORDER"),
   Span(doc170, 9, 12, label ="CONTRACT"),
   Span(doc170, 12, 13, label ="CONTRACT1"),
   Span(doc170, 15, 16, label ="POS"),
   Span(doc170, 16, 17, label ="AMOUNT"),
   Span(doc170, 18, 19, label ="ARTICLE"),
   Span(doc170, 19, 20, label ="PRICE"),
   Span(doc170, 20, 21, label ="UNIT"),
   Span(doc170, 22, 23, label ="SUMMA"),
   Span(doc170, 49, 50, label ="TARIFF"),
   Span(doc170, 54, 55, label ="COUNTRY"),
   Span(doc170, 57, 58, label ="PR_SURCH"),
   Span(doc170, 59, 60, label ="SURCHARGE"),
   Span(doc170, 62, 63, label ="PR_ESURCH"),
   Span(doc170, 64, 65, label ="ESURCHARGE"),
   Span(doc170, 65, 66, label ="TOTAL")]
docs.append(doc170)
print("doc171, 73, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 26000; AMOUNT 600; ARTICLE 1910000092; PRICE 6,73; UNIT 1; SUMMA 4.038,00; TARIFF 90261089; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 460,33; PR_ESURCH 3,50; ESURCHARGE 141,33; TOTAL 4.639,66; ")
doc171 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 26000 600 PC 1910000092 (*) 6,73 1 PC 4.038,00 SNA-127-B-S-O-12 SNA 127 B-S-O-12 packed per each item Product description: level gauge Export - Customs tariff no.: 90261089 Country of origin: Germany Material Surcharge 11,40 % 460,33 Energy Surcharge 3,50 % 141,33 4.639,66''')
doc171.ents = [
   Span(doc171, 3, 4, label ="NORDER"),
   Span(doc171, 9, 12, label ="CONTRACT"),
   Span(doc171, 12, 13, label ="CONTRACT1"),
   Span(doc171, 15, 16, label ="POS"),
   Span(doc171, 16, 17, label ="AMOUNT"),
   Span(doc171, 18, 19, label ="ARTICLE"),
   Span(doc171, 22, 23, label ="PRICE"),
   Span(doc171, 23, 24, label ="UNIT"),
   Span(doc171, 25, 26, label ="SUMMA"),
   Span(doc171, 56, 57, label ="TARIFF"),
   Span(doc171, 61, 62, label ="COUNTRY"),
   Span(doc171, 64, 65, label ="PR_SURCH"),
   Span(doc171, 66, 67, label ="SURCHARGE"),
   Span(doc171, 69, 70, label ="PR_ESURCH"),
   Span(doc171, 71, 72, label ="ESURCHARGE"),
   Span(doc171, 72, 73, label ="TOTAL")]
docs.append(doc171)
print("doc172, 69, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 26100; AMOUNT 100; ARTICLE 1130029459; PRICE 82,23; UNIT 100; SUMMA 82,23; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 9,37; PR_ESURCH 3,50; ESURCHARGE 2,88; TOTAL 94,48; ")
doc172 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 26100 100 PC 1130029459 82,23 100 PC 82,23 LBBU-328/22-SA-M8/U5/16 LBBU 328/22 SA M8-U5/16 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 9,37 Energy Surcharge 3,50 % 2,88 94,48''')
doc172.ents = [
   Span(doc172, 3, 4, label ="NORDER"),
   Span(doc172, 9, 12, label ="CONTRACT"),
   Span(doc172, 12, 13, label ="CONTRACT1"),
   Span(doc172, 15, 16, label ="POS"),
   Span(doc172, 16, 17, label ="AMOUNT"),
   Span(doc172, 18, 19, label ="ARTICLE"),
   Span(doc172, 19, 20, label ="PRICE"),
   Span(doc172, 20, 21, label ="UNIT"),
   Span(doc172, 22, 23, label ="SUMMA"),
   Span(doc172, 52, 53, label ="TARIFF"),
   Span(doc172, 57, 58, label ="COUNTRY"),
   Span(doc172, 60, 61, label ="PR_SURCH"),
   Span(doc172, 62, 63, label ="SURCHARGE"),
   Span(doc172, 65, 66, label ="PR_ESURCH"),
   Span(doc172, 67, 68, label ="ESURCHARGE"),
   Span(doc172, 68, 69, label ="TOTAL")]
docs.append(doc172)
print("doc173, 70, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 26200; AMOUNT 100; ARTICLE 1130029458; PRICE 82,23; UNIT 100; SUMMA 82,23; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 9,37; PR_ESURCH 3,50; ESURCHARGE 2,88; TOTAL 94,48; ")
doc173 = nlp('''Order number: 2390896   Purchase order number: N SR-1-06 1919** 26200 100 PC 1130029458 82,23 100 PC 82,23 LBBU-323/22-SA-M8/U5/16 LBBU 323/22 SA M8-U5/16 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 9,37 Energy Surcharge 3,50 % 2,88 94,48''')
doc173.ents = [
   Span(doc173, 3, 4, label ="NORDER"),
   Span(doc173, 10, 13, label ="CONTRACT"),
   Span(doc173, 13, 14, label ="CONTRACT1"),
   Span(doc173, 16, 17, label ="POS"),
   Span(doc173, 17, 18, label ="AMOUNT"),
   Span(doc173, 19, 20, label ="ARTICLE"),
   Span(doc173, 20, 21, label ="PRICE"),
   Span(doc173, 21, 22, label ="UNIT"),
   Span(doc173, 23, 24, label ="SUMMA"),
   Span(doc173, 53, 54, label ="TARIFF"),
   Span(doc173, 58, 59, label ="COUNTRY"),
   Span(doc173, 61, 62, label ="PR_SURCH"),
   Span(doc173, 63, 64, label ="SURCHARGE"),
   Span(doc173, 66, 67, label ="PR_ESURCH"),
   Span(doc173, 68, 69, label ="ESURCHARGE"),
   Span(doc173, 69, 70, label ="TOTAL")]
docs.append(doc173)
print("doc174, 64, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 26300; AMOUNT 1.000; ARTICLE 6100211504; PRICE 52,37; UNIT 100; SUMMA 523,70; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 59,70; PR_ESURCH 3,50; ESURCHARGE 18,33; TOTAL 601,73; ")
doc174 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 26300 1.000 PC 6100211504 52,37 100 PC 523,70 LBBU-2 12/08-SA-M8/U5/16/2 packed per each item Product description: clamp combination Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 59,70 Energy Surcharge 3,50 % 18,33 601,73''')
doc174.ents = [
   Span(doc174, 3, 4, label ="NORDER"),
   Span(doc174, 9, 12, label ="CONTRACT"),
   Span(doc174, 12, 13, label ="CONTRACT1"),
   Span(doc174, 15, 16, label ="POS"),
   Span(doc174, 16, 17, label ="AMOUNT"),
   Span(doc174, 18, 19, label ="ARTICLE"),
   Span(doc174, 19, 20, label ="PRICE"),
   Span(doc174, 20, 21, label ="UNIT"),
   Span(doc174, 22, 23, label ="SUMMA"),
   Span(doc174, 47, 48, label ="TARIFF"),
   Span(doc174, 52, 53, label ="COUNTRY"),
   Span(doc174, 55, 56, label ="PR_SURCH"),
   Span(doc174, 57, 58, label ="SURCHARGE"),
   Span(doc174, 60, 61, label ="PR_ESURCH"),
   Span(doc174, 62, 63, label ="ESURCHARGE"),
   Span(doc174, 63, 64, label ="TOTAL")]
docs.append(doc174)
print("doc175, 67, #NORDER 2390896; CONTRACT SR-1-06; CONTRACT1 1919; POS 26400; AMOUNT 200; ARTICLE 6100223417; PRICE 52,37; UNIT 100; SUMMA 104,74; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 11,94; PR_ESURCH 3,50; ESURCHARGE 3,67; TOTAL 120,35; ")
doc175 = nlp('''Order number: 2390896 Purchase order number: N SR-1-06 1919** 26400 200 PC 6100223417 52,37 100 PC 104,74 LBBU-208/08-SA-M8/U5/16/2 packed per each item Customer ID-No.: 000000001 130023506 Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 11,94 Energy Surcharge 3,50 % 3,67 120,35   ''')
doc175.ents = [
   Span(doc175, 3, 4, label ="NORDER"),
   Span(doc175, 9, 12, label ="CONTRACT"),
   Span(doc175, 12, 13, label ="CONTRACT1"),
   Span(doc175, 15, 16, label ="POS"),
   Span(doc175, 16, 17, label ="AMOUNT"),
   Span(doc175, 18, 19, label ="ARTICLE"),
   Span(doc175, 19, 20, label ="PRICE"),
   Span(doc175, 20, 21, label ="UNIT"),
   Span(doc175, 22, 23, label ="SUMMA"),
   Span(doc175, 49, 50, label ="TARIFF"),
   Span(doc175, 54, 55, label ="COUNTRY"),
   Span(doc175, 57, 58, label ="PR_SURCH"),
   Span(doc175, 59, 60, label ="SURCHARGE"),
   Span(doc175, 62, 63, label ="PR_ESURCH"),
   Span(doc175, 64, 65, label ="ESURCHARGE"),
   Span(doc175, 65, 66, label ="TOTAL")]
docs.append(doc175)
print("doc176, 71, #NORDER 2391982; CONTRACT SR-1-06; CONTRACT1 1914; POS 26500; AMOUNT 1.500; ARTICLE 1130024605; PRICE 46,52; UNIT 100; SUMMA 697,80; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 79,55; PR_ESURCH 3,50; ESURCHARGE 24,42; TOTAL 801,77; ")
doc176 = nlp('''Order number: 2391982 Purchase order number: N SR-1-06 1914 26500 1.500 PC 1130024605 46,52 100 PC 697,80 LBBU-DP-3D-M8/U5/16-W3 LBBU-DP 3D M8-U5/16 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 79,55 Energy Surcharge 3,50 % 24,42 801,77''')
doc176.ents = [
   Span(doc176, 3, 4, label ="NORDER"),
   Span(doc176, 9, 12, label ="CONTRACT"),
   Span(doc176, 12, 13, label ="CONTRACT1"),
   Span(doc176, 13, 14, label ="POS"),
   Span(doc176, 14, 15, label ="AMOUNT"),
   Span(doc176, 16, 17, label ="ARTICLE"),
   Span(doc176, 17, 18, label ="PRICE"),
   Span(doc176, 18, 19, label ="UNIT"),
   Span(doc176, 20, 21, label ="SUMMA"),
   Span(doc176, 54, 55, label ="TARIFF"),
   Span(doc176, 59, 60, label ="COUNTRY"),
   Span(doc176, 62, 63, label ="PR_SURCH"),
   Span(doc176, 64, 65, label ="SURCHARGE"),
   Span(doc176, 67, 68, label ="PR_ESURCH"),
   Span(doc176, 69, 70, label ="ESURCHARGE"),
   Span(doc176, 70, 71, label ="TOTAL")]
docs.append(doc176)
print("doc177, 73, #NORDER 2399580; CONTRACT SR-1-06; CONTRACT1 13; POS 26600; AMOUNT 25.000; ARTICLE 1130022787; PRICE 23,28; UNIT 100; SUMMA 5.820,00; TARIFF 73079980; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 663,48; PR_ESURCH 3,50; ESURCHARGE 203,70; TOTAL 6.687,18; ")
doc177 = nlp('''Order number: 2399580 Purchase order number: N SR-1-06 13 26600 25.000 PC 1130022787 23,28 100 PC 5.820,00 LBBU-HUE-2/2D-PM-M8/U5/16-W3 LBBU-HUE 2/2D PM M8-U5/16 W3 packed per each item Product description: sleeve Export - Customs tariff no.: 73079980 Country of origin: Germany Material Surcharge 11,40 % 663,48 Energy Surcharge 3,50 % 203,70 6.687,18''')
doc177.ents = [
   Span(doc177, 3, 4, label ="NORDER"),
   Span(doc177, 9, 12, label ="CONTRACT"),
   Span(doc177, 12, 13, label ="CONTRACT1"),
   Span(doc177, 13, 14, label ="POS"),
   Span(doc177, 14, 15, label ="AMOUNT"),
   Span(doc177, 16, 17, label ="ARTICLE"),
   Span(doc177, 17, 18, label ="PRICE"),
   Span(doc177, 18, 19, label ="UNIT"),
   Span(doc177, 20, 21, label ="SUMMA"),
   Span(doc177, 56, 57, label ="TARIFF"),
   Span(doc177, 61, 62, label ="COUNTRY"),
   Span(doc177, 64, 65, label ="PR_SURCH"),
   Span(doc177, 66, 67, label ="SURCHARGE"),
   Span(doc177, 69, 70, label ="PR_ESURCH"),
   Span(doc177, 71, 72, label ="ESURCHARGE"),
   Span(doc177, 72, 73, label ="TOTAL")]
docs.append(doc177)
print("doc178, 79, #NORDER 2399586; CONTRACT SR-1-06; CONTRACT1 16; POS 26700; AMOUNT 450; ARTICLE 6020000541; PRICE 670,58; UNIT 100; SUMMA 3.017,61; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 208,22; PR_ESURCH 3,50; ESURCHARGE 105,62; TOTAL 3.331,45; ")
doc178 = nlp('''Order number: 2399586 Purchase order number: N SR-1-06 16** 26700 450 PC 6020000541 (*) 670,58 100 PC 3.017,61 FI-GE-28LR1 -1/4-WD-B-W3 FI-GE-28LR1 1/4-WD-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 208,22   Energy Surcharge 3,50 % 105,62 3.331,45''')
doc178.ents = [
   Span(doc178, 3, 4, label ="NORDER"),
   Span(doc178, 9, 12, label ="CONTRACT"),
   Span(doc178, 12, 13, label ="CONTRACT1"),
   Span(doc178, 15, 16, label ="POS"),
   Span(doc178, 16, 17, label ="AMOUNT"),
   Span(doc178, 18, 19, label ="ARTICLE"),
   Span(doc178, 22, 23, label ="PRICE"),
   Span(doc178, 23, 24, label ="UNIT"),
   Span(doc178, 25, 26, label ="SUMMA"),
   Span(doc178, 61, 62, label ="TARIFF"),
   Span(doc178, 66, 67, label ="COUNTRY"),
   Span(doc178, 69, 70, label ="PR_SURCH"),
   Span(doc178, 71, 72, label ="SURCHARGE"),
   Span(doc178, 75, 76, label ="PR_ESURCH"),
   Span(doc178, 77, 78, label ="ESURCHARGE"),
   Span(doc178, 78, 79, label ="TOTAL")]
docs.append(doc178)
print("doc179, 78, #NORDER 2399591; CONTRACT SR-1-06; CONTRACT1 17; POS 26800; AMOUNT 600; ARTICLE 6020000541; PRICE 670,58; UNIT 100; SUMMA 4.023,48; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 277,62; PR_ESURCH 3,50; ESURCHARGE 140,82; TOTAL 4.441,92; ")
doc179 = nlp('''Order number: 2399591 Purchase order number: N SR-1-06 17** 26800 600 PC 6020000541 (*) 670,58 100 PC 4.023,48 FI-GE-28LR1 -1/4-WD-B-W3 FI-GE-28LR1 1/4-WD-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 277,62 Energy Surcharge 3,50 % 140,82 4.441,92''')
doc179.ents = [
   Span(doc179, 3, 4, label ="NORDER"),
   Span(doc179, 9, 12, label ="CONTRACT"),
   Span(doc179, 12, 13, label ="CONTRACT1"),
   Span(doc179, 15, 16, label ="POS"),
   Span(doc179, 16, 17, label ="AMOUNT"),
   Span(doc179, 18, 19, label ="ARTICLE"),
   Span(doc179, 22, 23, label ="PRICE"),
   Span(doc179, 23, 24, label ="UNIT"),
   Span(doc179, 25, 26, label ="SUMMA"),
   Span(doc179, 61, 62, label ="TARIFF"),
   Span(doc179, 66, 67, label ="COUNTRY"),
   Span(doc179, 69, 70, label ="PR_SURCH"),
   Span(doc179, 71, 72, label ="SURCHARGE"),
   Span(doc179, 74, 75, label ="PR_ESURCH"),
   Span(doc179, 76, 77, label ="ESURCHARGE"),
   Span(doc179, 77, 78, label ="TOTAL")]
docs.append(doc179)
print("doc181, 79, #NORDER 2399641; CONTRACT SR-1-06; CONTRACT1 18; POS 27000; AMOUNT 600; ARTICLE 6020000541; PRICE 670,58; UNIT 100; SUMMA 4.023,48; TARIFF 73079910; COUNTRY Germany   ; PR_SURCH 6,90; SURCHARGE 277,62; PR_ESURCH 3,50; ESURCHARGE 140,82; TOTAL 4.441,92; ")
doc181 = nlp('''Order number: 2399641 Purchase order number: N SR-1-06 18** 27000 600 PC 6020000541 (*) 670,58 100 PC 4.023,48 FI-GE-28LR1 -1/4-WD-B-W3 FI-GE-28LR1 1/4-WD-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany   Material Surcharge 6,90 % 277,62 Energy Surcharge 3,50 % 140,82 4.441,92''')
doc181.ents = [
   Span(doc181, 3, 4, label ="NORDER"),
   Span(doc181, 9, 12, label ="CONTRACT"),
   Span(doc181, 12, 13, label ="CONTRACT1"),
   Span(doc181, 15, 16, label ="POS"),
   Span(doc181, 16, 17, label ="AMOUNT"),
   Span(doc181, 18, 19, label ="ARTICLE"),
   Span(doc181, 22, 23, label ="PRICE"),
   Span(doc181, 23, 24, label ="UNIT"),
   Span(doc181, 25, 26, label ="SUMMA"),
   Span(doc181, 61, 62, label ="TARIFF"),
   Span(doc181, 66, 68, label ="COUNTRY"),
   Span(doc181, 70, 71, label ="PR_SURCH"),
   Span(doc181, 72, 73, label ="SURCHARGE"),
   Span(doc181, 75, 76, label ="PR_ESURCH"),
   Span(doc181, 77, 78, label ="ESURCHARGE"),
   Span(doc181, 78, 79, label ="TOTAL")]
docs.append(doc181)
print("doc182, 60, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 27100; AMOUNT 40.000; ARTICLE 6030003812; PRICE 8,87; UNIT 100; SUMMA 3.548,00; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 244,81; PR_ESURCH 3,50; ESURCHARGE 124,18; TOTAL 3.916,99; ")
doc182 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 27100 40.000 PC 6030003812 8,87 100 PC 3.548,00 FI-M-08L-W3 packed per each item Product description: nuts Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 244,81 Energy Surcharge 3,50 % 124,18 3.916,99''')
doc182.ents = [
   Span(doc182, 3, 4, label ="NORDER"),
   Span(doc182, 9, 12, label ="CONTRACT"),
   Span(doc182, 12, 13, label ="CONTRACT1"),
   Span(doc182, 15, 16, label ="POS"),
   Span(doc182, 16, 17, label ="AMOUNT"),
   Span(doc182, 18, 19, label ="ARTICLE"),
   Span(doc182, 19, 20, label ="PRICE"),
   Span(doc182, 20, 21, label ="UNIT"),
   Span(doc182, 22, 23, label ="SUMMA"),
   Span(doc182, 43, 44, label ="TARIFF"),
   Span(doc182, 48, 49, label ="COUNTRY"),
   Span(doc182, 51, 52, label ="PR_SURCH"),
   Span(doc182, 53, 54, label ="SURCHARGE"),
   Span(doc182, 56, 57, label ="PR_ESURCH"),
   Span(doc182, 58, 59, label ="ESURCHARGE"),
   Span(doc182, 59, 60, label ="TOTAL")]
docs.append(doc182)
print("doc183, 76, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 27400; AMOUNT 20; ARTICLE 6010004110; PRICE 39,04; UNIT 100; SUMMA 7,81; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 0,54; PR_ESURCH 3,50; ESURCHARGE 0,27; TOTAL 8,62; ")
doc183 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 27400 20 PC 6010004110 (*) 39,04 100 PC 7,81 FI-VD-12L-V-W3-M FI-VD-12L-B-W3-M packed per each item Product description: Plug Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 0,54 Energy Surcharge 3,50 % 0,27 8,62''')
doc183.ents = [
   Span(doc183, 3, 4, label ="NORDER"),
   Span(doc183, 9, 12, label ="CONTRACT"),
   Span(doc183, 12, 13, label ="CONTRACT1"),
   Span(doc183, 15, 16, label ="POS"),
   Span(doc183, 16, 17, label ="AMOUNT"),
   Span(doc183, 18, 19, label ="ARTICLE"),
   Span(doc183, 22, 23, label ="PRICE"),
   Span(doc183, 23, 24, label ="UNIT"),
   Span(doc183, 25, 26, label ="SUMMA"),
   Span(doc183, 59, 60, label ="TARIFF"),
   Span(doc183, 64, 65, label ="COUNTRY"),
   Span(doc183, 67, 68, label ="PR_SURCH"),
   Span(doc183, 69, 70, label ="SURCHARGE"),
   Span(doc183, 72, 73, label ="PR_ESURCH"),
   Span(doc183, 74, 75, label ="ESURCHARGE"),
   Span(doc183, 75, 76, label ="TOTAL")]
docs.append(doc183)
print("doc184, 81, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 27500; AMOUNT 100; ARTICLE 6010001836; PRICE 15,74; UNIT 100; SUMMA 15,74; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 1,09; PR_ESURCH 3,50; ESURCHARGE 0,55; TOTAL 17,38; ")
doc184 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 27500 100 PC 6010001836 (*) 15,74 100 PC 15,74 FI-VS-M14x1.5-WD-B-W3 FI-VS-M14x1,5-WD-B-W3 packed per each item Product description: Plug    Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 1,09 Energy Surcharge 3,50 % 0,55 17,38''')
doc184.ents = [
   Span(doc184, 3, 4, label ="NORDER"),
   Span(doc184, 9, 12, label ="CONTRACT"),
   Span(doc184, 12, 13, label ="CONTRACT1"),
   Span(doc184, 15, 16, label ="POS"),
   Span(doc184, 16, 17, label ="AMOUNT"),
   Span(doc184, 18, 19, label ="ARTICLE"),
   Span(doc184, 22, 23, label ="PRICE"),
   Span(doc184, 23, 24, label ="UNIT"),
   Span(doc184, 25, 26, label ="SUMMA"),
   Span(doc184, 64, 65, label ="TARIFF"),
   Span(doc184, 69, 70, label ="COUNTRY"),
   Span(doc184, 72, 73, label ="PR_SURCH"),
   Span(doc184, 74, 75, label ="SURCHARGE"),
   Span(doc184, 77, 78, label ="PR_ESURCH"),
   Span(doc184, 79, 80, label ="ESURCHARGE"),
   Span(doc184, 80, 81, label ="TOTAL")]
docs.append(doc184)
print("doc185, 76, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 27600; AMOUNT 100; ARTICLE 6010004241; PRICE 312,86; UNIT 100; SUMMA 312,86; TARIFF 84813091; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 21,59; PR_ESURCH 3,50; ESURCHARGE 10,95; TOTAL 345,40; ")
doc185 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 27600 100 PC 6010004241 (*) 312,86 100 PC 312,86 FI-RV-08L-W3-0.5 FI-RV-08L-W3-0,5 packed per each item Product description: valve Export - Customs tariff no.: 84813091 Country of origin: Germany Material Surcharge 6,90 % 21,59 Energy Surcharge 3,50 % 10,95 345,40 EAC - Eurasian Conformity''')
doc185.ents = [
   Span(doc185, 3, 4, label ="NORDER"),
   Span(doc185, 9, 12, label ="CONTRACT"),
   Span(doc185, 12, 13, label ="CONTRACT1"),
   Span(doc185, 15, 16, label ="POS"),
   Span(doc185, 16, 17, label ="AMOUNT"),
   Span(doc185, 18, 19, label ="ARTICLE"),
   Span(doc185, 22, 23, label ="PRICE"),
   Span(doc185, 23, 24, label ="UNIT"),
   Span(doc185, 25, 26, label ="SUMMA"),
   Span(doc185, 55, 56, label ="TARIFF"),
   Span(doc185, 60, 61, label ="COUNTRY"),
   Span(doc185, 63, 64, label ="PR_SURCH"),
   Span(doc185, 65, 66, label ="SURCHARGE"),
   Span(doc185, 68, 69, label ="PR_ESURCH"),
   Span(doc185, 70, 71, label ="ESURCHARGE"),
   Span(doc185, 71, 72, label ="TOTAL")]
docs.append(doc185)
print("doc186, 86, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 27700; AMOUNT 30; ARTICLE 6010004949; PRICE 2.294,82; UNIT 100; SUMMA 688,45; TARIFF 84813091; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 47,50; PR_ESURCH 3,50; ESURCHARGE 24,10; TOTAL 760,05; ")
doc186 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 27700 30 PC 6010004949 (*) 2.294,82 100 PC 688,45 FI-RVV-35LR-WD-B-W3-0.2 FI-RVV-35LR-WD-B-W3-0 ,2 packed per each item Product description: valve Export - Customs tariff no.: 84813091 Country of origin: Germany Material Surcharge 6,90 % 47,50 Energy Surcharge 3,50 % 24,10 760,05 EAC - Eurasian Conformity''')
doc186.ents = [
   Span(doc186, 3, 4, label ="NORDER"),
   Span(doc186, 9, 12, label ="CONTRACT"),
   Span(doc186, 12, 13, label ="CONTRACT1"),
   Span(doc186, 15, 16, label ="POS"),
   Span(doc186, 16, 17, label ="AMOUNT"),
   Span(doc186, 18, 19, label ="ARTICLE"),
   Span(doc186, 22, 23, label ="PRICE"),
   Span(doc186, 23, 24, label ="UNIT"),
   Span(doc186, 25, 26, label ="SUMMA"),
   Span(doc186, 65, 66, label ="TARIFF"),
   Span(doc186, 70, 71, label ="COUNTRY"),
   Span(doc186, 73, 74, label ="PR_SURCH"),
   Span(doc186, 75, 76, label ="SURCHARGE"),
   Span(doc186, 78, 79, label ="PR_ESURCH"),
   Span(doc186, 80, 81, label ="ESURCHARGE"),
   Span(doc186, 81, 82, label ="TOTAL")]
docs.append(doc186)
print("doc187, 85, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 27800; AMOUNT 30; ARTICLE 6010004404; PRICE 551,22; UNIT 100; SUMMA 165,37; TARIFF 84813091; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 11,41; PR_ESURCH 3,50; ESURCHARGE 5,79; TOTAL 182,57; ")
doc187 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19**   27800 30 PC 6010004404 (*) 551,22 100 PC 165,37 FI-RVZ-12LM-WD-B-W3-0.2 FI-RVZ-12LM-WD-B-W3-0,2 packed per each item Product description: valve Export - Customs tariff no.: 84813091 Country of origin: Germany Material Surcharge 6,90 % 11,41 Energy Surcharge 3,50 % 5,79 182,57 EAC - Eurasian Conformity''')
doc187.ents = [
   Span(doc187, 3, 4, label ="NORDER"),
   Span(doc187, 9, 12, label ="CONTRACT"),
   Span(doc187, 12, 13, label ="CONTRACT1"),
   Span(doc187, 16, 17, label ="POS"),
   Span(doc187, 17, 18, label ="AMOUNT"),
   Span(doc187, 19, 20, label ="ARTICLE"),
   Span(doc187, 23, 24, label ="PRICE"),
   Span(doc187, 24, 25, label ="UNIT"),
   Span(doc187, 26, 27, label ="SUMMA"),
   Span(doc187, 64, 65, label ="TARIFF"),
   Span(doc187, 69, 70, label ="COUNTRY"),
   Span(doc187, 72, 73, label ="PR_SURCH"),
   Span(doc187, 74, 75, label ="SURCHARGE"),
   Span(doc187, 77, 78, label ="PR_ESURCH"),
   Span(doc187, 79, 80, label ="ESURCHARGE"),
   Span(doc187, 80, 81, label ="TOTAL")]
docs.append(doc187)
print("doc188, 63, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 27900; AMOUNT 2.000; ARTICLE 6030004273; PRICE 19,24; UNIT 100; SUMMA 384,80; TARIFF 73269098; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 26,55; PR_ESURCH 3,50; ESURCHARGE 13,47; TOTAL 424,82; ")
doc188 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 27900 2.000 PC 6030004273 (*) 19,24 100 PC 384,80 FI-DS-22L-W3 packed per each item Product description: ring Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 6,90 % 26,55 Energy Surcharge 3,50 % 13,47 424,82''')
doc188.ents = [
   Span(doc188, 3, 4, label ="NORDER"),
   Span(doc188, 9, 12, label ="CONTRACT"),
   Span(doc188, 12, 13, label ="CONTRACT1"),
   Span(doc188, 15, 16, label ="POS"),
   Span(doc188, 16, 17, label ="AMOUNT"),
   Span(doc188, 18, 19, label ="ARTICLE"),
   Span(doc188, 22, 23, label ="PRICE"),
   Span(doc188, 23, 24, label ="UNIT"),
   Span(doc188, 25, 26, label ="SUMMA"),
   Span(doc188, 46, 47, label ="TARIFF"),
   Span(doc188, 51, 52, label ="COUNTRY"),
   Span(doc188, 54, 55, label ="PR_SURCH"),
   Span(doc188, 56, 57, label ="SURCHARGE"),
   Span(doc188, 59, 60, label ="PR_ESURCH"),
   Span(doc188, 61, 62, label ="ESURCHARGE"),
   Span(doc188, 62, 63, label ="TOTAL")]
docs.append(doc188)
print("doc189, 64, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 28000; AMOUNT 400; ARTICLE 6030004274; PRICE 22,63; UNIT 100; SUMMA 90,52; TARIFF 73269098; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 6,25; PR_ESURCH 3,50; ESURCHARGE 3,17; TOTAL 99,94; ")
doc189 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 28000 400 PC 6030004274 (*) 22,63 100 PC 90,52 FI-DS-28L-W3 packed per each item Product description: ring Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 6,90 % 6,25 Energy Surcharge 3,50 % 3,17 99,94   ''')
doc189.ents = [
   Span(doc189, 3, 4, label ="NORDER"),
   Span(doc189, 9, 12, label ="CONTRACT"),
   Span(doc189, 12, 13, label ="CONTRACT1"),
   Span(doc189, 15, 16, label ="POS"),
   Span(doc189, 16, 17, label ="AMOUNT"),
   Span(doc189, 18, 19, label ="ARTICLE"),
   Span(doc189, 22, 23, label ="PRICE"),
   Span(doc189, 23, 24, label ="UNIT"),
   Span(doc189, 25, 26, label ="SUMMA"),
   Span(doc189, 46, 47, label ="TARIFF"),
   Span(doc189, 51, 52, label ="COUNTRY"),
   Span(doc189, 54, 55, label ="PR_SURCH"),
   Span(doc189, 56, 57, label ="SURCHARGE"),
   Span(doc189, 59, 60, label ="PR_ESURCH"),
   Span(doc189, 61, 62, label ="ESURCHARGE"),
   Span(doc189, 62, 63, label ="TOTAL")]
docs.append(doc189)
print("doc190, 78, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 28100; AMOUNT 200; ARTICLE 6010003900; PRICE 43,84; UNIT 100; SUMMA 87,68; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 6,05; PR_ESURCH 3,50; ESURCHARGE 3,07; TOTAL 96,80; ")
doc190 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 28100 200 PC 6010003900 (*) 43,84 100 PC 87,68 FI-REDSD-1 2/08L-V-W3-DKO FI-REDSD-1 2/08L-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 6,05 Energy Surcharge 3,50 % 3,07 96,80''')
doc190.ents = [
   Span(doc190, 3, 4, label ="NORDER"),
   Span(doc190, 9, 12, label ="CONTRACT"),
   Span(doc190, 12, 13, label ="CONTRACT1"),
   Span(doc190, 15, 16, label ="POS"),
   Span(doc190, 16, 17, label ="AMOUNT"),
   Span(doc190, 18, 19, label ="ARTICLE"),
   Span(doc190, 22, 23, label ="PRICE"),
   Span(doc190, 23, 24, label ="UNIT"),
   Span(doc190, 25, 26, label ="SUMMA"),
   Span(doc190, 61, 62, label ="TARIFF"),
   Span(doc190, 66, 67, label ="COUNTRY"),
   Span(doc190, 69, 70, label ="PR_SURCH"),
   Span(doc190, 71, 72, label ="SURCHARGE"),
   Span(doc190, 74, 75, label ="PR_ESURCH"),
   Span(doc190, 76, 77, label ="ESURCHARGE"),
   Span(doc190, 77, 78, label ="TOTAL")]
docs.append(doc190)
print("doc191, 78, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 28200; AMOUNT 100; ARTICLE 6010003903; PRICE 102,59; UNIT 100; SUMMA 102,59; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 7,08; PR_ESURCH 3,50; ESURCHARGE 3,59; TOTAL 113,26; ")
doc191 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 28200 100 PC 6010003903 (*) 102,59 100 PC 102,59 FI-REDSD-1 5/08L-V-W3-DKO FI-REDSD-1 5/08L-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 7,08 Energy Surcharge 3,50 % 3,59 113,26''')
doc191.ents = [
   Span(doc191, 3, 4, label ="NORDER"),
   Span(doc191, 9, 12, label ="CONTRACT"),
   Span(doc191, 12, 13, label ="CONTRACT1"),
   Span(doc191, 15, 16, label ="POS"),
   Span(doc191, 16, 17, label ="AMOUNT"),
   Span(doc191, 18, 19, label ="ARTICLE"),
   Span(doc191, 22, 23, label ="PRICE"),
   Span(doc191, 23, 24, label ="UNIT"),
   Span(doc191, 25, 26, label ="SUMMA"),
   Span(doc191, 61, 62, label ="TARIFF"),
   Span(doc191, 66, 67, label ="COUNTRY"),
   Span(doc191, 69, 70, label ="PR_SURCH"),
   Span(doc191, 71, 72, label ="SURCHARGE"),
   Span(doc191, 74, 75, label ="PR_ESURCH"),
   Span(doc191, 76, 77, label ="ESURCHARGE"),
   Span(doc191, 77, 78, label ="TOTAL")]
docs.append(doc191)
print("doc192, 77, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 28400; AMOUNT 100; ARTICLE 6010003969; PRICE 263,25; UNIT 100; SUMMA 263,25; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 18,16; PR_ESURCH 3,50; ESURCHARGE 9,21; TOTAL 290,62; ")
doc192 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 28400 100 PC 6010003969 (*) 263,25 100 PC 263,25 FI-REDSD-22/08L-V-W3-DKO FI-REDSD-22/08L-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 18,16   Energy Surcharge 3,50 % 9,21 290,62''')
doc192.ents = [
   Span(doc192, 3, 4, label ="NORDER"),
   Span(doc192, 9, 12, label ="CONTRACT"),
   Span(doc192, 12, 13, label ="CONTRACT1"),
   Span(doc192, 15, 16, label ="POS"),
   Span(doc192, 16, 17, label ="AMOUNT"),
   Span(doc192, 18, 19, label ="ARTICLE"),
   Span(doc192, 22, 23, label ="PRICE"),
   Span(doc192, 23, 24, label ="UNIT"),
   Span(doc192, 25, 26, label ="SUMMA"),
   Span(doc192, 59, 60, label ="TARIFF"),
   Span(doc192, 64, 65, label ="COUNTRY"),
   Span(doc192, 67, 68, label ="PR_SURCH"),
   Span(doc192, 69, 70, label ="SURCHARGE"),
   Span(doc192, 73, 74, label ="PR_ESURCH"),
   Span(doc192, 75, 76, label ="ESURCHARGE"),
   Span(doc192, 76, 77, label ="TOTAL")]
docs.append(doc192)
print("doc193, 76, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 28500; AMOUNT 300; ARTICLE 6010003913; PRICE 176,70; UNIT 100; SUMMA 530,10; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 36,58; PR_ESURCH 3,50; ESURCHARGE 18,55; TOTAL 585,23; ")
doc193 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 28500 300 PC 6010003913 (*) 176,70 100 PC 530,10 FI-REDSD-22/18L-V-W3-DKO FI-REDSD-22/18L-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 36,58 Energy Surcharge 3,50 % 18,55 585,23''')
doc193.ents = [
   Span(doc193, 3, 4, label ="NORDER"),
   Span(doc193, 9, 12, label ="CONTRACT"),
   Span(doc193, 12, 13, label ="CONTRACT1"),
   Span(doc193, 15, 16, label ="POS"),
   Span(doc193, 16, 17, label ="AMOUNT"),
   Span(doc193, 18, 19, label ="ARTICLE"),
   Span(doc193, 22, 23, label ="PRICE"),
   Span(doc193, 23, 24, label ="UNIT"),
   Span(doc193, 25, 26, label ="SUMMA"),
   Span(doc193, 59, 60, label ="TARIFF"),
   Span(doc193, 64, 65, label ="COUNTRY"),
   Span(doc193, 67, 68, label ="PR_SURCH"),
   Span(doc193, 69, 70, label ="SURCHARGE"),
   Span(doc193, 72, 73, label ="PR_ESURCH"),
   Span(doc193, 74, 75, label ="ESURCHARGE"),
   Span(doc193, 75, 76, label ="TOTAL")]
docs.append(doc193)
print("doc194, 76, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 28600; AMOUNT 90; ARTICLE 6010014115; PRICE 550,85; UNIT 100; SUMMA 495,77; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 34,21; PR_ESURCH 3,50; ESURCHARGE 17,35; TOTAL 547,33; ")
doc194 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 28600 90 PC 6010014115 (*) 550,85 100 PC 495,77 FI-REDSD-22L-V-W3-DKO FI-REDSD-22L-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 34,21 Energy Surcharge 3,50 % 17,35 547,33''')
doc194.ents = [
   Span(doc194, 3, 4, label ="NORDER"),
   Span(doc194, 9, 12, label ="CONTRACT"),
   Span(doc194, 12, 13, label ="CONTRACT1"),
   Span(doc194, 15, 16, label ="POS"),
   Span(doc194, 16, 17, label ="AMOUNT"),
   Span(doc194, 18, 19, label ="ARTICLE"),
   Span(doc194, 22, 23, label ="PRICE"),
   Span(doc194, 23, 24, label ="UNIT"),
   Span(doc194, 25, 26, label ="SUMMA"),
   Span(doc194, 59, 60, label ="TARIFF"),
   Span(doc194, 64, 65, label ="COUNTRY"),
   Span(doc194, 67, 68, label ="PR_SURCH"),
   Span(doc194, 69, 70, label ="SURCHARGE"),
   Span(doc194, 72, 73, label ="PR_ESURCH"),
   Span(doc194, 74, 75, label ="ESURCHARGE"),
   Span(doc194, 75, 76, label ="TOTAL")]
docs.append(doc194)
print("doc195, 78, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 28700; AMOUNT 300; ARTICLE 6010003921; PRICE 371,39; UNIT 100; SUMMA 1.114,17; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 76,88; PR_ESURCH 3,50; ESURCHARGE 39,00; TOTAL 1.230,05; ")
doc195 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 28700 300 PC 6010003921 (*) 371,39 100 PC 1.114,17 FI-REDSD-3 5/28L-V-W3-DKO FI-REDSD-35/28L-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079910    Country of origin: Germany Material Surcharge 6,90 % 76,88 Energy Surcharge 3,50 % 39,00 1.230,05''')
doc195.ents = [
   Span(doc195, 3, 4, label ="NORDER"),
   Span(doc195, 9, 12, label ="CONTRACT"),
   Span(doc195, 12, 13, label ="CONTRACT1"),
   Span(doc195, 15, 16, label ="POS"),
   Span(doc195, 16, 17, label ="AMOUNT"),
   Span(doc195, 18, 19, label ="ARTICLE"),
   Span(doc195, 22, 23, label ="PRICE"),
   Span(doc195, 23, 24, label ="UNIT"),
   Span(doc195, 25, 26, label ="SUMMA"),
   Span(doc195, 60, 61, label ="TARIFF"),
   Span(doc195, 66, 67, label ="COUNTRY"),
   Span(doc195, 69, 70, label ="PR_SURCH"),
   Span(doc195, 71, 72, label ="SURCHARGE"),
   Span(doc195, 74, 75, label ="PR_ESURCH"),
   Span(doc195, 76, 77, label ="ESURCHARGE"),
   Span(doc195, 77, 78, label ="TOTAL")]
docs.append(doc195)
print("doc196, 80, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 28900; AMOUNT 200; ARTICLE 6010013612; PRICE 164,64; UNIT 100; SUMMA 329,28; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 22,72; PR_ESURCH 3,50; ESURCHARGE 11,52; TOTAL 363,52; ")
doc196 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 28900 200 PC 6010013612 (*) 164,64 100 PC 329,28 FI-EGED-08LM-OR-BV-W3-DKO FI-EGED-08LM-OR-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 22,72 Energy Surcharge 3,50 % 11,52 363,52''')
doc196.ents = [
   Span(doc196, 3, 4, label ="NORDER"),
   Span(doc196, 9, 12, label ="CONTRACT"),
   Span(doc196, 12, 13, label ="CONTRACT1"),
   Span(doc196, 15, 16, label ="POS"),
   Span(doc196, 16, 17, label ="AMOUNT"),
   Span(doc196, 18, 19, label ="ARTICLE"),
   Span(doc196, 22, 23, label ="PRICE"),
   Span(doc196, 23, 24, label ="UNIT"),
   Span(doc196, 25, 26, label ="SUMMA"),
   Span(doc196, 63, 64, label ="TARIFF"),
   Span(doc196, 68, 69, label ="COUNTRY"),
   Span(doc196, 71, 72, label ="PR_SURCH"),
   Span(doc196, 73, 74, label ="SURCHARGE"),
   Span(doc196, 76, 77, label ="PR_ESURCH"),
   Span(doc196, 78, 79, label ="ESURCHARGE"),
   Span(doc196, 79, 80, label ="TOTAL")]
docs.append(doc196)
print("doc197, 81, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 29000; AMOUNT 100; ARTICLE 6010003835; PRICE 108,24; UNIT 100; SUMMA 108,24; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 7,47; PR_ESURCH 3,50; ESURCHARGE 3,79; TOTAL 119,50; ")
doc197 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 29000 100 PC 6010003835 (*) 108,24 100 PC 108,24 FI-EGED-0 8LR-WD-BV-W3-DKO FI-EGED-08LR-WD-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 7,47 Energy Surcharge 3,50 % 3,79 119,50''')
doc197.ents = [
   Span(doc197, 3, 4, label ="NORDER"),
   Span(doc197, 9, 12, label ="CONTRACT"),
   Span(doc197, 12, 13, label ="CONTRACT1"),
   Span(doc197, 15, 16, label ="POS"),
   Span(doc197, 16, 17, label ="AMOUNT"),
   Span(doc197, 18, 19, label ="ARTICLE"),
   Span(doc197, 22, 23, label ="PRICE"),
   Span(doc197, 23, 24, label ="UNIT"),
   Span(doc197, 25, 26, label ="SUMMA"),
   Span(doc197, 64, 65, label ="TARIFF"),
   Span(doc197, 69, 70, label ="COUNTRY"),
   Span(doc197, 72, 73, label ="PR_SURCH"),
   Span(doc197, 74, 75, label ="SURCHARGE"),
   Span(doc197, 77, 78, label ="PR_ESURCH"),
   Span(doc197, 79, 80, label ="ESURCHARGE"),
   Span(doc197, 80, 81, label ="TOTAL")]
docs.append(doc197)
print("doc198, 82, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 29100; AMOUNT 100; ARTICLE 6010003806; PRICE 134,84; UNIT 100; SUMMA 134,84; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 9,30; PR_ESURCH 3,50; ESURCHARGE 4,72; TOTAL 148,86; ")
doc198 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 29100 100 PC 6010003806 (*) 134,84 100 PC 134,84 FI-EGED-12LM-WD-BV-W3-DKO FI-EGED-1 2LM-WD-B-W3-DKO    packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 9,30 Energy Surcharge 3,50 % 4,72 148,86''')
doc198.ents = [
   Span(doc198, 3, 4, label ="NORDER"),
   Span(doc198, 9, 12, label ="CONTRACT"),
   Span(doc198, 12, 13, label ="CONTRACT1"),
   Span(doc198, 15, 16, label ="POS"),
   Span(doc198, 16, 17, label ="AMOUNT"),
   Span(doc198, 18, 19, label ="ARTICLE"),
   Span(doc198, 22, 23, label ="PRICE"),
   Span(doc198, 23, 24, label ="UNIT"),
   Span(doc198, 25, 26, label ="SUMMA"),
   Span(doc198, 65, 66, label ="TARIFF"),
   Span(doc198, 70, 71, label ="COUNTRY"),
   Span(doc198, 73, 74, label ="PR_SURCH"),
   Span(doc198, 75, 76, label ="SURCHARGE"),
   Span(doc198, 78, 79, label ="PR_ESURCH"),
   Span(doc198, 80, 81, label ="ESURCHARGE"),
   Span(doc198, 81, 82, label ="TOTAL")]
docs.append(doc198)
print("doc199, 82, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 29200; AMOUNT 100; ARTICLE 6010003841; PRICE 154,64; UNIT 100; SUMMA 154,64; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 10,67; PR_ESURCH 3,50; ESURCHARGE 5,41; TOTAL 170,72; ")
doc199 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 29200 100 PC 6010003841 (*) 154,64 100 PC 154,64 FI-EGED-1 5LR-WD-BV-W3-DKO FI-EGED-1 5LR-WD-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 10,67 Energy Surcharge 3,50 % 5,41 170,72''')
doc199.ents = [
   Span(doc199, 3, 4, label ="NORDER"),
   Span(doc199, 9, 12, label ="CONTRACT"),
   Span(doc199, 12, 13, label ="CONTRACT1"),
   Span(doc199, 15, 16, label ="POS"),
   Span(doc199, 16, 17, label ="AMOUNT"),
   Span(doc199, 18, 19, label ="ARTICLE"),
   Span(doc199, 22, 23, label ="PRICE"),
   Span(doc199, 23, 24, label ="UNIT"),
   Span(doc199, 25, 26, label ="SUMMA"),
   Span(doc199, 65, 66, label ="TARIFF"),
   Span(doc199, 70, 71, label ="COUNTRY"),
   Span(doc199, 73, 74, label ="PR_SURCH"),
   Span(doc199, 75, 76, label ="SURCHARGE"),
   Span(doc199, 78, 79, label ="PR_ESURCH"),
   Span(doc199, 80, 81, label ="ESURCHARGE"),
   Span(doc199, 81, 82, label ="TOTAL")]
docs.append(doc199)
print("doc200, 82, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 29300; AMOUNT 40; ARTICLE 6010003843; PRICE 91,14; UNIT 100; SUMMA 36,46; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 2,52; PR_ESURCH 3,50; ESURCHARGE 1,28; TOTAL 40,26; ")
doc200 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 29300 40 PC 6010003843 (*) 91,14 100 PC 36,46 FI-EGED-1 8LR-WD-BV-W3-DKO FI-EGED-1 8LR-WD-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 2,52 Energy Surcharge 3,50 % 1,28 40,26''')
doc200.ents = [
   Span(doc200, 3, 4, label ="NORDER"),
   Span(doc200, 9, 12, label ="CONTRACT"),
   Span(doc200, 12, 13, label ="CONTRACT1"),
   Span(doc200, 15, 16, label ="POS"),
   Span(doc200, 16, 17, label ="AMOUNT"),
   Span(doc200, 18, 19, label ="ARTICLE"),
   Span(doc200, 22, 23, label ="PRICE"),
   Span(doc200, 23, 24, label ="UNIT"),
   Span(doc200, 25, 26, label ="SUMMA"),
   Span(doc200, 65, 66, label ="TARIFF"),
   Span(doc200, 70, 71, label ="COUNTRY"),
   Span(doc200, 73, 74, label ="PR_SURCH"),
   Span(doc200, 75, 76, label ="SURCHARGE"),
   Span(doc200, 78, 79, label ="PR_ESURCH"),
   Span(doc200, 80, 81, label ="ESURCHARGE"),
   Span(doc200, 81, 82, label ="TOTAL")]
docs.append(doc200)
print("doc201, 77, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 29400; AMOUNT 1.550; ARTICLE 6010003728; PRICE 741,82; UNIT 100; SUMMA 11.498,21; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 793,38; PR_ESURCH 3,50; ESURCHARGE 402,44; TOTAL 12.694,03; ")
doc201 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19**   29400 1.550 PC 6010003728 (*) 741,82 100 PC 11.498,21 FI-ELD-28L-V-W3-DKO FI-ELD-28L-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 793,38 Energy Surcharge 3,50 % 402,44 12.694,03''')
doc201.ents = [
   Span(doc201, 3, 4, label ="NORDER"),
   Span(doc201, 9, 12, label ="CONTRACT"),
   Span(doc201, 12, 13, label ="CONTRACT1"),
   Span(doc201, 16, 17, label ="POS"),
   Span(doc201, 17, 18, label ="AMOUNT"),
   Span(doc201, 19, 20, label ="ARTICLE"),
   Span(doc201, 23, 24, label ="PRICE"),
   Span(doc201, 24, 25, label ="UNIT"),
   Span(doc201, 26, 27, label ="SUMMA"),
   Span(doc201, 60, 61, label ="TARIFF"),
   Span(doc201, 65, 66, label ="COUNTRY"),
   Span(doc201, 68, 69, label ="PR_SURCH"),
   Span(doc201, 70, 71, label ="SURCHARGE"),
   Span(doc201, 73, 74, label ="PR_ESURCH"),
   Span(doc201, 75, 76, label ="ESURCHARGE"),
   Span(doc201, 76, 77, label ="TOTAL")]
docs.append(doc201)
print("doc202, 80, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 29500; AMOUNT 50; ARTICLE 6010007591; PRICE 591,20; UNIT 100; SUMMA 295,60; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 20,40; PR_ESURCH 3,50; ESURCHARGE 10,35; TOTAL 326,35; ")
doc202 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 29500 50 PC 6010007591 (*) 591,20 100 PC 295,60 FI-EMAD-06SR1/4-V-W3-DKI-DKO FI-EMAD-06SR1/4-B-W3-DKI-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 20,40 Energy Surcharge 3,50 % 10,35 326,35''')
doc202.ents = [
   Span(doc202, 3, 4, label ="NORDER"),
   Span(doc202, 9, 12, label ="CONTRACT"),
   Span(doc202, 12, 13, label ="CONTRACT1"),
   Span(doc202, 15, 16, label ="POS"),
   Span(doc202, 16, 17, label ="AMOUNT"),
   Span(doc202, 18, 19, label ="ARTICLE"),
   Span(doc202, 22, 23, label ="PRICE"),
   Span(doc202, 23, 24, label ="UNIT"),
   Span(doc202, 25, 26, label ="SUMMA"),
   Span(doc202, 63, 64, label ="TARIFF"),
   Span(doc202, 68, 69, label ="COUNTRY"),
   Span(doc202, 71, 72, label ="PR_SURCH"),
   Span(doc202, 73, 74, label ="SURCHARGE"),
   Span(doc202, 76, 77, label ="PR_ESURCH"),
   Span(doc202, 78, 79, label ="ESURCHARGE"),
   Span(doc202, 79, 80, label ="TOTAL")]
docs.append(doc202)
print("doc203, 79, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 29600; AMOUNT 720; ARTICLE 6010003587; PRICE 175,69; UNIT 100; SUMMA 1.264; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 87,28; PR_ESURCH 3,50; ESURCHARGE 44,27; TOTAL 1.396,52; ")
doc203 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 29600 720 PC 6010003587 (*) 175,69 100 PC 1.264 ,97 FI-ETD-12L-V-W3-DKO FI-ETD-12L-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 87,28 Energy Surcharge 3,50 % 44,27 1.396,52   ''')
doc203.ents = [
   Span(doc203, 3, 4, label ="NORDER"),
   Span(doc203, 9, 12, label ="CONTRACT"),
   Span(doc203, 12, 13, label ="CONTRACT1"),
   Span(doc203, 15, 16, label ="POS"),
   Span(doc203, 16, 17, label ="AMOUNT"),
   Span(doc203, 18, 19, label ="ARTICLE"),
   Span(doc203, 22, 23, label ="PRICE"),
   Span(doc203, 23, 24, label ="UNIT"),
   Span(doc203, 25, 26, label ="SUMMA"),
   Span(doc203, 61, 62, label ="TARIFF"),
   Span(doc203, 66, 67, label ="COUNTRY"),
   Span(doc203, 69, 70, label ="PR_SURCH"),
   Span(doc203, 71, 72, label ="SURCHARGE"),
   Span(doc203, 74, 75, label ="PR_ESURCH"),
   Span(doc203, 76, 77, label ="ESURCHARGE"),
   Span(doc203, 77, 78, label ="TOTAL")]
docs.append(doc203)
print("doc204, 76, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 29800; AMOUNT 1.250; ARTICLE 6010003611; PRICE 740,61; UNIT 100; SUMMA 9.257,63; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 638,78; PR_ESURCH 3,50; ESURCHARGE 324,02; TOTAL 10.220,43; ")
doc204 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 29800 1.250 PC 6010003611 (*) 740,61 100 PC 9.257,63 FI-ETD-28L-V-W3-DKO FI-ETD-28L-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 638,78 Energy Surcharge 3,50 % 324,02 10.220,43''')
doc204.ents = [
   Span(doc204, 3, 4, label ="NORDER"),
   Span(doc204, 9, 12, label ="CONTRACT"),
   Span(doc204, 12, 13, label ="CONTRACT1"),
   Span(doc204, 15, 16, label ="POS"),
   Span(doc204, 16, 17, label ="AMOUNT"),
   Span(doc204, 18, 19, label ="ARTICLE"),
   Span(doc204, 22, 23, label ="PRICE"),
   Span(doc204, 23, 24, label ="UNIT"),
   Span(doc204, 25, 26, label ="SUMMA"),
   Span(doc204, 59, 60, label ="TARIFF"),
   Span(doc204, 64, 65, label ="COUNTRY"),
   Span(doc204, 67, 68, label ="PR_SURCH"),
   Span(doc204, 69, 70, label ="SURCHARGE"),
   Span(doc204, 72, 73, label ="PR_ESURCH"),
   Span(doc204, 74, 75, label ="ESURCHARGE"),
   Span(doc204, 75, 76, label ="TOTAL")]
docs.append(doc204)
print("doc205, 76, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 30000; AMOUNT 7.300; ARTICLE 6010003470; PRICE 144,57; UNIT 100; SUMMA 10.553,61; TARIFF 73079290; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 728,20; PR_ESURCH 3,50; ESURCHARGE 369,38; TOTAL 11.651,19; ")
doc205 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 30000 7.300 PC 6010003470 (*) 144,57 100 PC 10.553,61 FI-EWD-12L-V-W3-DKO FI-EWD-12L-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079290 Country of origin: Germany Material Surcharge 6,90 % 728,20 Energy Surcharge 3,50 % 369,38 11.651,19''')
doc205.ents = [
   Span(doc205, 3, 4, label ="NORDER"),
   Span(doc205, 9, 12, label ="CONTRACT"),
   Span(doc205, 12, 13, label ="CONTRACT1"),
   Span(doc205, 15, 16, label ="POS"),
   Span(doc205, 16, 17, label ="AMOUNT"),
   Span(doc205, 18, 19, label ="ARTICLE"),
   Span(doc205, 22, 23, label ="PRICE"),
   Span(doc205, 23, 24, label ="UNIT"),
   Span(doc205, 25, 26, label ="SUMMA"),
   Span(doc205, 59, 60, label ="TARIFF"),
   Span(doc205, 64, 65, label ="COUNTRY"),
   Span(doc205, 67, 68, label ="PR_SURCH"),
   Span(doc205, 69, 70, label ="SURCHARGE"),
   Span(doc205, 72, 73, label ="PR_ESURCH"),
   Span(doc205, 74, 75, label ="ESURCHARGE"),
   Span(doc205, 75, 76, label ="TOTAL")]
docs.append(doc205)
print("doc206, 77, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 30200; AMOUNT 750; ARTICLE 6010003494; PRICE 450,46; UNIT 100; SUMMA 3.378,45; TARIFF 73079290; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 233,11; PR_ESURCH 3,50; ESURCHARGE 118,25; TOTAL 3.729,81; ")
doc206 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 30200 750 PC 6010003494 (*) 450,46 100 PC 3.378,45 FI-EWD-28L-V-W3-DKO FI-EWD-28L-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079290 Country of origin: Germany Material Surcharge 6,90 % 233,11  Energy Surcharge 3,50 % 118,25 3.729,81''')
doc206.ents = [
   Span(doc206, 3, 4, label ="NORDER"),
   Span(doc206, 9, 12, label ="CONTRACT"),
   Span(doc206, 12, 13, label ="CONTRACT1"),
   Span(doc206, 15, 16, label ="POS"),
   Span(doc206, 16, 17, label ="AMOUNT"),
   Span(doc206, 18, 19, label ="ARTICLE"),
   Span(doc206, 22, 23, label ="PRICE"),
   Span(doc206, 23, 24, label ="UNIT"),
   Span(doc206, 25, 26, label ="SUMMA"),
   Span(doc206, 59, 60, label ="TARIFF"),
   Span(doc206, 64, 65, label ="COUNTRY"),
   Span(doc206, 67, 68, label ="PR_SURCH"),
   Span(doc206, 69, 70, label ="SURCHARGE"),
   Span(doc206, 73, 74, label ="PR_ESURCH"),
   Span(doc206, 75, 76, label ="ESURCHARGE"),
   Span(doc206, 76, 77, label ="TOTAL")]
docs.append(doc206)
print("doc207, 63, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 30300; AMOUNT 100; ARTICLE 6030003250; PRICE 62,43; UNIT 100; SUMMA 62,43; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 4,31; PR_ESURCH 3,50; ESURCHARGE 2,19; TOTAL 68,93; ")
doc207 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 30300 100 PC 6030003250 (*) 62,43 100 PC 62,43 FI-G-18L-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 4,31 Energy Surcharge 3,50 % 2,19 68,93''')
doc207.ents = [
   Span(doc207, 3, 4, label ="NORDER"),
   Span(doc207, 9, 12, label ="CONTRACT"),
   Span(doc207, 12, 13, label ="CONTRACT1"),
   Span(doc207, 15, 16, label ="POS"),
   Span(doc207, 16, 17, label ="AMOUNT"),
   Span(doc207, 18, 19, label ="ARTICLE"),
   Span(doc207, 22, 23, label ="PRICE"),
   Span(doc207, 23, 24, label ="UNIT"),
   Span(doc207, 25, 26, label ="SUMMA"),
   Span(doc207, 46, 47, label ="TARIFF"),
   Span(doc207, 51, 52, label ="COUNTRY"),
   Span(doc207, 54, 55, label ="PR_SURCH"),
   Span(doc207, 56, 57, label ="SURCHARGE"),
   Span(doc207, 59, 60, label ="PR_ESURCH"),
   Span(doc207, 61, 62, label ="ESURCHARGE"),
   Span(doc207, 62, 63, label ="TOTAL")]
docs.append(doc207)
print("doc208, 63, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 30500; AMOUNT 75; ARTICLE 6030003545; PRICE 45,83; UNIT 100; SUMMA 34,37; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 2,37; PR_ESURCH 3,50; ESURCHARGE 1,20; TOTAL 37,94; ")
doc208 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 30500 75 PC 6030003545 (*) 45,83 100 PC 34,37 FI-GA-10LR-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 2,37 Energy Surcharge 3,50 % 1,20 37,94''')
doc208.ents = [
   Span(doc208, 3, 4, label ="NORDER"),
   Span(doc208, 9, 12, label ="CONTRACT"),
   Span(doc208, 12, 13, label ="CONTRACT1"),
   Span(doc208, 15, 16, label ="POS"),
   Span(doc208, 16, 17, label ="AMOUNT"),
   Span(doc208, 18, 19, label ="ARTICLE"),
   Span(doc208, 22, 23, label ="PRICE"),
   Span(doc208, 23, 24, label ="UNIT"),
   Span(doc208, 25, 26, label ="SUMMA"),
   Span(doc208, 46, 47, label ="TARIFF"),
   Span(doc208, 51, 52, label ="COUNTRY"),
   Span(doc208, 54, 55, label ="PR_SURCH"),
   Span(doc208, 56, 57, label ="SURCHARGE"),
   Span(doc208, 59, 60, label ="PR_ESURCH"),
   Span(doc208, 61, 62, label ="ESURCHARGE"),
   Span(doc208, 62, 63, label ="TOTAL")]
docs.append(doc208)
print("doc209, 64, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 30600; AMOUNT 150; ARTICLE 6030003046; PRICE 269,70; UNIT 100; SUMMA 404,55; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 27,91; PR_ESURCH 3,50; ESURCHARGE 14,16; TOTAL 446,62; ")
doc209 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 30600 150 PC 6030003046 (*) 269,70 100 PC 404,55 FI-GE-08L1/8N-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 27,91   Energy Surcharge 3,50 % 14,16 446,62''')
doc209.ents = [
   Span(doc209, 3, 4, label ="NORDER"),
   Span(doc209, 9, 12, label ="CONTRACT"),
   Span(doc209, 12, 13, label ="CONTRACT1"),
   Span(doc209, 15, 16, label ="POS"),
   Span(doc209, 16, 17, label ="AMOUNT"),
   Span(doc209, 18, 19, label ="ARTICLE"),
   Span(doc209, 22, 23, label ="PRICE"),
   Span(doc209, 23, 24, label ="UNIT"),
   Span(doc209, 25, 26, label ="SUMMA"),
   Span(doc209, 46, 47, label ="TARIFF"),
   Span(doc209, 51, 52, label ="COUNTRY"),
   Span(doc209, 54, 55, label ="PR_SURCH"),
   Span(doc209, 56, 57, label ="SURCHARGE"),
   Span(doc209, 60, 61, label ="PR_ESURCH"),
   Span(doc209, 62, 63, label ="ESURCHARGE"),
   Span(doc209, 63, 64, label ="TOTAL")]
docs.append(doc209)
print("doc210, 69, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 30800; AMOUNT 600; ARTICLE 6020000640; PRICE 33,19; UNIT 100; SUMMA 199,14; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 13,74; PR_ESURCH 3,50; ESURCHARGE 6,97; TOTAL 219,85; ")
doc210 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 30800 600 PC 6020000640 (*) 33,19 100 PC 199,14 FI-GE-O8LM-OR-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 13,74 Energy Surcharge 3,50 % 6,97 219,85''')
doc210.ents = [
   Span(doc210, 3, 4, label ="NORDER"),
   Span(doc210, 9, 12, label ="CONTRACT"),
   Span(doc210, 12, 13, label ="CONTRACT1"),
   Span(doc210, 15, 16, label ="POS"),
   Span(doc210, 16, 17, label ="AMOUNT"),
   Span(doc210, 18, 19, label ="ARTICLE"),
   Span(doc210, 22, 23, label ="PRICE"),
   Span(doc210, 23, 24, label ="UNIT"),
   Span(doc210, 25, 26, label ="SUMMA"),
   Span(doc210, 52, 53, label ="TARIFF"),
   Span(doc210, 57, 58, label ="COUNTRY"),
   Span(doc210, 60, 61, label ="PR_SURCH"),
   Span(doc210, 62, 63, label ="SURCHARGE"),
   Span(doc210, 65, 66, label ="PR_ESURCH"),
   Span(doc210, 67, 68, label ="ESURCHARGE"),
   Span(doc210, 68, 69, label ="TOTAL")]
docs.append(doc210)
print("doc211, 69, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 30900; AMOUNT 150; ARTICLE 6020000529; PRICE 53,75; UNIT 100; SUMMA 80,63; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 5,56; PR_ESURCH 3,50; ESURCHARGE 2,82; TOTAL 89,01; ")
doc211 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 30900 150 PC 6020000529 (*) 53,75 100 PC 80,63 FI-GE-O8LR3/8-WD-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 5,56 Energy Surcharge 3,50 % 2,82 89,01''')
doc211.ents = [
   Span(doc211, 3, 4, label ="NORDER"),
   Span(doc211, 9, 12, label ="CONTRACT"),
   Span(doc211, 12, 13, label ="CONTRACT1"),
   Span(doc211, 15, 16, label ="POS"),
   Span(doc211, 16, 17, label ="AMOUNT"),
   Span(doc211, 18, 19, label ="ARTICLE"),
   Span(doc211, 22, 23, label ="PRICE"),
   Span(doc211, 23, 24, label ="UNIT"),
   Span(doc211, 25, 26, label ="SUMMA"),
   Span(doc211, 52, 53, label ="TARIFF"),
   Span(doc211, 57, 58, label ="COUNTRY"),
   Span(doc211, 60, 61, label ="PR_SURCH"),
   Span(doc211, 62, 63, label ="SURCHARGE"),
   Span(doc211, 65, 66, label ="PR_ESURCH"),
   Span(doc211, 67, 68, label ="ESURCHARGE"),
   Span(doc211, 68, 69, label ="TOTAL")]
docs.append(doc211)
print("doc212, 64, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 31100; AMOUNT 450; ARTICLE 6030003055; PRICE 37,72; UNIT 100; SUMMA 169,74; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 11,71; PR_ESURCH 3,50; ESURCHARGE 5,94; TOTAL 187,39; ")
doc212 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 31100 450 PC 6030003055 (*) 37,72 100 PC 169,74 FI-GE-12L3/8N-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 11,71   Energy Surcharge 3,50 % 5,94 187,39''')
doc212.ents = [
   Span(doc212, 3, 4, label ="NORDER"),
   Span(doc212, 9, 12, label ="CONTRACT"),
   Span(doc212, 12, 13, label ="CONTRACT1"),
   Span(doc212, 15, 16, label ="POS"),
   Span(doc212, 16, 17, label ="AMOUNT"),
   Span(doc212, 18, 19, label ="ARTICLE"),
   Span(doc212, 22, 23, label ="PRICE"),
   Span(doc212, 23, 24, label ="UNIT"),
   Span(doc212, 25, 26, label ="SUMMA"),
   Span(doc212, 46, 47, label ="TARIFF"),
   Span(doc212, 51, 52, label ="COUNTRY"),
   Span(doc212, 54, 55, label ="PR_SURCH"),
   Span(doc212, 56, 57, label ="SURCHARGE"),
   Span(doc212, 60, 61, label ="PR_ESURCH"),
   Span(doc212, 62, 63, label ="ESURCHARGE"),
   Span(doc212, 63, 64, label ="TOTAL")]
docs.append(doc212)
print("doc213, 76, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 31200; AMOUNT 600; ARTICLE 6020000645; PRICE 105,60; UNIT 100; SUMMA 633,60; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 43,72; PR_ESURCH 3,50; ESURCHARGE 22,18; TOTAL 699,50; ")
doc213 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 31200 600 PC 6020000645 (*) 105,60 100 PC 633,60 FI-GE-12LM12x1.5-OR-B-W3 FI-GE-12LM12x1,5-OR-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 43,72 Energy Surcharge 3,50 % 22,18 699,50''')
doc213.ents = [
   Span(doc213, 3, 4, label ="NORDER"),
   Span(doc213, 9, 12, label ="CONTRACT"),
   Span(doc213, 12, 13, label ="CONTRACT1"),
   Span(doc213, 15, 16, label ="POS"),
   Span(doc213, 16, 17, label ="AMOUNT"),
   Span(doc213, 18, 19, label ="ARTICLE"),
   Span(doc213, 22, 23, label ="PRICE"),
   Span(doc213, 23, 24, label ="UNIT"),
   Span(doc213, 25, 26, label ="SUMMA"),
   Span(doc213, 59, 60, label ="TARIFF"),
   Span(doc213, 64, 65, label ="COUNTRY"),
   Span(doc213, 67, 68, label ="PR_SURCH"),
   Span(doc213, 69, 70, label ="SURCHARGE"),
   Span(doc213, 72, 73, label ="PR_ESURCH"),
   Span(doc213, 74, 75, label ="ESURCHARGE"),
   Span(doc213, 75, 76, label ="TOTAL")]
docs.append(doc213)
print("doc214, 80, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 31300; AMOUNT 60; ARTICLE 6010001432; PRICE 206,31; UNIT 100; SUMMA 123,79; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 8,54; PR_ESURCH 3,50; ESURCHARGE 4,33; TOTAL 136,66; ")
doc214 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 31300 60 PC 6010001432 (*) 206,31 100 PC 123,79 FI-GE-12LM12x1.5-WD-B-W3-MS FI-GE-12LM12x1,5-WD-B-W3-MS packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 8,54 Energy Surcharge 3,50 % 4,33 136,66''')
doc214.ents = [
   Span(doc214, 3, 4, label ="NORDER"),
   Span(doc214, 9, 12, label ="CONTRACT"),
   Span(doc214, 12, 13, label ="CONTRACT1"),
   Span(doc214, 15, 16, label ="POS"),
   Span(doc214, 16, 17, label ="AMOUNT"),
   Span(doc214, 18, 19, label ="ARTICLE"),
   Span(doc214, 22, 23, label ="PRICE"),
   Span(doc214, 23, 24, label ="UNIT"),
   Span(doc214, 25, 26, label ="SUMMA"),
   Span(doc214, 63, 64, label ="TARIFF"),
   Span(doc214, 68, 69, label ="COUNTRY"),
   Span(doc214, 71, 72, label ="PR_SURCH"),
   Span(doc214, 73, 74, label ="SURCHARGE"),
   Span(doc214, 76, 77, label ="PR_ESURCH"),
   Span(doc214, 78, 79, label ="ESURCHARGE"),
   Span(doc214, 79, 80, label ="TOTAL")]
docs.append(doc214)
print("doc215, 68, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 31600; AMOUNT 2.400; ARTICLE 6020000647; PRICE 47,52; UNIT 100; SUMMA 1.140,48; TARIFF 73079910; COUNTRY Germany   ; PR_SURCH 6,90; SURCHARGE 78,69; PR_ESURCH 3,50; ESURCHARGE 39,92; TOTAL 1.259,09; ")
doc215 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 31600 2.400 PC 6020000647 (*) 47,52 100 PC 1.140,48 FI-GE-12LM-OR-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany   Material Surcharge 6,90 % 78,69 Energy Surcharge 3,50 % 39,92 1.259,09''')
doc215.ents = [
   Span(doc215, 3, 4, label ="NORDER"),
   Span(doc215, 9, 12, label ="CONTRACT"),
   Span(doc215, 12, 13, label ="CONTRACT1"),
   Span(doc215, 15, 16, label ="POS"),
   Span(doc215, 16, 17, label ="AMOUNT"),
   Span(doc215, 18, 19, label ="ARTICLE"),
   Span(doc215, 22, 23, label ="PRICE"),
   Span(doc215, 23, 24, label ="UNIT"),
   Span(doc215, 25, 26, label ="SUMMA"),
   Span(doc215, 50, 51, label ="TARIFF"),
   Span(doc215, 55, 57, label ="COUNTRY"),
   Span(doc215, 59, 60, label ="PR_SURCH"),
   Span(doc215, 61, 62, label ="SURCHARGE"),
   Span(doc215, 64, 65, label ="PR_ESURCH"),
   Span(doc215, 66, 67, label ="ESURCHARGE"),
   Span(doc215, 67, 68, label ="TOTAL")]
docs.append(doc215)
print("doc216, 67, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 31700; AMOUNT 2.600; ARTICLE 6020000462; PRICE 72,01; UNIT 100; SUMMA 1.872,26; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 129,19; PR_ESURCH 3,50; ESURCHARGE 65,53; TOTAL 2.066,98; ")
doc216 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 31700 2.600 PC 6020000462 (*) 72,01 100 PC 1.872,26 FI-GE-12LR1/2-WD-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 129,19 Energy Surcharge 3,50 % 65,53 2.066,98''')
doc216.ents = [
   Span(doc216, 3, 4, label ="NORDER"),
   Span(doc216, 9, 12, label ="CONTRACT"),
   Span(doc216, 12, 13, label ="CONTRACT1"),
   Span(doc216, 15, 16, label ="POS"),
   Span(doc216, 16, 17, label ="AMOUNT"),
   Span(doc216, 18, 19, label ="ARTICLE"),
   Span(doc216, 22, 23, label ="PRICE"),
   Span(doc216, 23, 24, label ="UNIT"),
   Span(doc216, 25, 26, label ="SUMMA"),
   Span(doc216, 50, 51, label ="TARIFF"),
   Span(doc216, 55, 56, label ="COUNTRY"),
   Span(doc216, 58, 59, label ="PR_SURCH"),
   Span(doc216, 60, 61, label ="SURCHARGE"),
   Span(doc216, 63, 64, label ="PR_ESURCH"),
   Span(doc216, 65, 66, label ="ESURCHARGE"),
   Span(doc216, 66, 67, label ="TOTAL")]
docs.append(doc216)
print("doc217, 67, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 31800; AMOUNT 600; ARTICLE 6020000473; PRICE 41,14; UNIT 100; SUMMA 246,84; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 17,03; PR_ESURCH 3,50; ESURCHARGE 8,64; TOTAL 272,51; ")
doc217 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 31800 600 PC 6020000473 (*) 41,14 100 PC 246,84 FI-GE-12LR-WD-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 17,03 Energy Surcharge 3,50 % 8,64 272,51''')
doc217.ents = [
   Span(doc217, 3, 4, label ="NORDER"),
   Span(doc217, 9, 12, label ="CONTRACT"),
   Span(doc217, 12, 13, label ="CONTRACT1"),
   Span(doc217, 15, 16, label ="POS"),
   Span(doc217, 16, 17, label ="AMOUNT"),
   Span(doc217, 18, 19, label ="ARTICLE"),
   Span(doc217, 22, 23, label ="PRICE"),
   Span(doc217, 23, 24, label ="UNIT"),
   Span(doc217, 25, 26, label ="SUMMA"),
   Span(doc217, 50, 51, label ="TARIFF"),
   Span(doc217, 55, 56, label ="COUNTRY"),
   Span(doc217, 58, 59, label ="PR_SURCH"),
   Span(doc217, 60, 61, label ="SURCHARGE"),
   Span(doc217, 63, 64, label ="PR_ESURCH"),
   Span(doc217, 65, 66, label ="ESURCHARGE"),
   Span(doc217, 66, 67, label ="TOTAL")]
docs.append(doc217)
print("doc218, 68, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 31900; AMOUNT 225; ARTICLE 6020000653; PRICE 68,46; UNIT 100; SUMMA 154,04; TARIFF 73079910; COUNTRY Germany   ; PR_SURCH 6,90; SURCHARGE 10,63; PR_ESURCH 3,50; ESURCHARGE 5,39; TOTAL 170,06; ")
doc218 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 31900 225 PC 6020000653 (*) 68,46 100 PC 154,04 FI-GE-18LM-OR-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany   Material Surcharge 6,90 % 10,63 Energy Surcharge 3,50 % 5,39 170,06''')
doc218.ents = [
   Span(doc218, 3, 4, label ="NORDER"),
   Span(doc218, 9, 12, label ="CONTRACT"),
   Span(doc218, 12, 13, label ="CONTRACT1"),
   Span(doc218, 15, 16, label ="POS"),
   Span(doc218, 16, 17, label ="AMOUNT"),
   Span(doc218, 18, 19, label ="ARTICLE"),
   Span(doc218, 22, 23, label ="PRICE"),
   Span(doc218, 23, 24, label ="UNIT"),
   Span(doc218, 25, 26, label ="SUMMA"),
   Span(doc218, 50, 51, label ="TARIFF"),
   Span(doc218, 55, 57, label ="COUNTRY"),
   Span(doc218, 59, 60, label ="PR_SURCH"),
   Span(doc218, 61, 62, label ="SURCHARGE"),
   Span(doc218, 64, 65, label ="PR_ESURCH"),
   Span(doc218, 66, 67, label ="ESURCHARGE"),
   Span(doc218, 67, 68, label ="TOTAL")]
docs.append(doc218)
print("doc219, 69, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 32000; AMOUNT 1.500; ARTICLE 6020000534; PRICE 156,52; UNIT 100; SUMMA 2.347; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 162,00; PR_ESURCH 3,50; ESURCHARGE 82,17; TOTAL 2.591,97; ")
doc219 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 32000 1.500 PC 6020000534 (*) 156,52 100 PC 2.347 ,80 FI-GE-18LR3/4-WD-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 162,00 Energy Surcharge 3,50 % 82,17 2.591,97''')
doc219.ents = [
   Span(doc219, 3, 4, label ="NORDER"),
   Span(doc219, 9, 12, label ="CONTRACT"),
   Span(doc219, 12, 13, label ="CONTRACT1"),
   Span(doc219, 15, 16, label ="POS"),
   Span(doc219, 16, 17, label ="AMOUNT"),
   Span(doc219, 18, 19, label ="ARTICLE"),
   Span(doc219, 22, 23, label ="PRICE"),
   Span(doc219, 23, 24, label ="UNIT"),
   Span(doc219, 25, 26, label ="SUMMA"),
   Span(doc219, 52, 53, label ="TARIFF"),
   Span(doc219, 57, 58, label ="COUNTRY"),
   Span(doc219, 60, 61, label ="PR_SURCH"),
   Span(doc219, 62, 63, label ="SURCHARGE"),
   Span(doc219, 65, 66, label ="PR_ESURCH"),
   Span(doc219, 67, 68, label ="ESURCHARGE"),
   Span(doc219, 68, 69, label ="TOTAL")]
docs.append(doc219)
print("doc220, 74, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 32300; AMOUNT 50; ARTICLE 6020000253; PRICE 578,00; UNIT 100; SUMMA 289,00; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 19,94; PR_ESURCH 3,50; ESURCHARGE 10,12; TOTAL 319,06; ")
doc220 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 32300 50 PC 6020000253 (*) 578,00 100 PC 289,00 FI-GE-22L1 -5/16U-B-W3 FI-GE-22L1 5/16U-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 19,94 Energy Surcharge 3,50 % 10,12 319,06''')
doc220.ents = [
   Span(doc220, 3, 4, label ="NORDER"),
   Span(doc220, 9, 12, label ="CONTRACT"),
   Span(doc220, 12, 13, label ="CONTRACT1"),
   Span(doc220, 15, 16, label ="POS"),
   Span(doc220, 16, 17, label ="AMOUNT"),
   Span(doc220, 18, 19, label ="ARTICLE"),
   Span(doc220, 22, 23, label ="PRICE"),
   Span(doc220, 23, 24, label ="UNIT"),
   Span(doc220, 25, 26, label ="SUMMA"),
   Span(doc220, 57, 58, label ="TARIFF"),
   Span(doc220, 62, 63, label ="COUNTRY"),
   Span(doc220, 65, 66, label ="PR_SURCH"),
   Span(doc220, 67, 68, label ="SURCHARGE"),
   Span(doc220, 70, 71, label ="PR_ESURCH"),
   Span(doc220, 72, 73, label ="ESURCHARGE"),
   Span(doc220, 73, 74, label ="TOTAL")]
docs.append(doc220)
print("doc221, 66, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 32400; AMOUNT 100; ARTICLE 6020000251; PRICE 416,01; UNIT 100; SUMMA 416,01; TARIFF 73079910; COUNTRY Germany   ; PR_SURCH 6,90; SURCHARGE 28,70; PR_ESURCH 3,50; ESURCHARGE 14,56; TOTAL 459,27; ")
doc221 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 32400 100 PC 6020000251 (*) 416,01 100 PC 416,01 FI-GE-22L7/8U-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany   Material Surcharge 6,90 % 28,70 Energy Surcharge 3,50 % 14,56 459,27''')
doc221.ents = [
   Span(doc221, 3, 4, label ="NORDER"),
   Span(doc221, 9, 12, label ="CONTRACT"),
   Span(doc221, 12, 13, label ="CONTRACT1"),
   Span(doc221, 15, 16, label ="POS"),
   Span(doc221, 16, 17, label ="AMOUNT"),
   Span(doc221, 18, 19, label ="ARTICLE"),
   Span(doc221, 22, 23, label ="PRICE"),
   Span(doc221, 23, 24, label ="UNIT"),
   Span(doc221, 25, 26, label ="SUMMA"),
   Span(doc221, 48, 49, label ="TARIFF"),
   Span(doc221, 53, 55, label ="COUNTRY"),
   Span(doc221, 57, 58, label ="PR_SURCH"),
   Span(doc221, 59, 60, label ="SURCHARGE"),
   Span(doc221, 62, 63, label ="PR_ESURCH"),
   Span(doc221, 64, 65, label ="ESURCHARGE"),
   Span(doc221, 65, 66, label ="TOTAL")]
docs.append(doc221)
print("doc222, 78, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 32500; AMOUNT 300; ARTICLE 6020000407; PRICE 151,81; UNIT 100; SUMMA 455,43; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 31,42; PR_ESURCH 3,50; ESURCHARGE 15,94; TOTAL 502,79; ")
doc222 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 32500 300 PC 6020000407 (*) 151,81 100 PC 455,43 FI-GE-22LM22x1.5-WD-B-W3 FI-GE-22LM22x1 ,5-WD-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 31,42 Energy Surcharge 3,50 % 15,94 502,79''')
doc222.ents = [
   Span(doc222, 3, 4, label ="NORDER"),
   Span(doc222, 9, 12, label ="CONTRACT"),
   Span(doc222, 12, 13, label ="CONTRACT1"),
   Span(doc222, 15, 16, label ="POS"),
   Span(doc222, 16, 17, label ="AMOUNT"),
   Span(doc222, 18, 19, label ="ARTICLE"),
   Span(doc222, 22, 23, label ="PRICE"),
   Span(doc222, 23, 24, label ="UNIT"),
   Span(doc222, 25, 26, label ="SUMMA"),
   Span(doc222, 61, 62, label ="TARIFF"),
   Span(doc222, 66, 67, label ="COUNTRY"),
   Span(doc222, 69, 70, label ="PR_SURCH"),
   Span(doc222, 71, 72, label ="SURCHARGE"),
   Span(doc222, 74, 75, label ="PR_ESURCH"),
   Span(doc222, 76, 77, label ="ESURCHARGE"),
   Span(doc222, 77, 78, label ="TOTAL")]
docs.append(doc222)
print("doc223, 63, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 32600; AMOUNT 50; ARTICLE 6030003130; PRICE 89,01; UNIT 100; SUMMA 44,51; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 3,07; PR_ESURCH 3,50; ESURCHARGE 1,56; TOTAL 49,14; ")
doc223 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 32600 50 PC 6030003130 (*) 89,01 100 PC 44,51 FI-GE-22LM-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 3,07 Energy Surcharge 3,50 % 1,56 49,14''')
doc223.ents = [
   Span(doc223, 3, 4, label ="NORDER"),
   Span(doc223, 9, 12, label ="CONTRACT"),
   Span(doc223, 12, 13, label ="CONTRACT1"),
   Span(doc223, 15, 16, label ="POS"),
   Span(doc223, 16, 17, label ="AMOUNT"),
   Span(doc223, 18, 19, label ="ARTICLE"),
   Span(doc223, 22, 23, label ="PRICE"),
   Span(doc223, 23, 24, label ="UNIT"),
   Span(doc223, 25, 26, label ="SUMMA"),
   Span(doc223, 46, 47, label ="TARIFF"),
   Span(doc223, 51, 52, label ="COUNTRY"),
   Span(doc223, 54, 55, label ="PR_SURCH"),
   Span(doc223, 56, 57, label ="SURCHARGE"),
   Span(doc223, 59, 60, label ="PR_ESURCH"),
   Span(doc223, 61, 62, label ="ESURCHARGE"),
   Span(doc223, 62, 63, label ="TOTAL")]
docs.append(doc223)
print("doc224, 69, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 32800; AMOUNT 40; ARTICLE 6020000396; PRICE 199,33; UNIT 100; SUMMA 79,73; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 5,50; PR_ESURCH 3,50; ESURCHARGE 2,79; TOTAL 88,02; ")
doc224 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 32800 40 PC 6020000396 (* ) 199,33 100 PC 79,73 FI-GE-25 SM-WD-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910    Country of origin: Germany Material Surcharge 6,90 % 5,50 Energy Surcharge 3,50 % 2,79 88,02''')
doc224.ents = [
   Span(doc224, 3, 4, label ="NORDER"),
   Span(doc224, 9, 12, label ="CONTRACT"),
   Span(doc224, 12, 13, label ="CONTRACT1"),
   Span(doc224, 15, 16, label ="POS"),
   Span(doc224, 16, 17, label ="AMOUNT"),
   Span(doc224, 18, 19, label ="ARTICLE"),
   Span(doc224, 22, 23, label ="PRICE"),
   Span(doc224, 23, 24, label ="UNIT"),
   Span(doc224, 25, 26, label ="SUMMA"),
   Span(doc224, 51, 52, label ="TARIFF"),
   Span(doc224, 57, 58, label ="COUNTRY"),
   Span(doc224, 60, 61, label ="PR_SURCH"),
   Span(doc224, 62, 63, label ="SURCHARGE"),
   Span(doc224, 65, 66, label ="PR_ESURCH"),
   Span(doc224, 67, 68, label ="ESURCHARGE"),
   Span(doc224, 68, 69, label ="TOTAL")]
docs.append(doc224)
print("doc225, 77, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 32900; AMOUNT 3.030; ARTICLE 6020000255; PRICE 600,25; UNIT 100; SUMMA 18.187; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 1.254,94; PR_ESURCH 3,50; ESURCHARGE 636,57; TOTAL 20.079,09; ")
doc225 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 32900 3.030 PC 6020000255 (*) 600,25 100 PC 18.187 ,58 FI-GE-28 L1 -5/16U-B-W3 FI-GE-28L1 5/16U-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 1.254,94 Energy Surcharge 3,50 % 636,57 20.079,09''')
doc225.ents = [
   Span(doc225, 3, 4, label ="NORDER"),
   Span(doc225, 9, 12, label ="CONTRACT"),
   Span(doc225, 12, 13, label ="CONTRACT1"),
   Span(doc225, 15, 16, label ="POS"),
   Span(doc225, 16, 17, label ="AMOUNT"),
   Span(doc225, 18, 19, label ="ARTICLE"),
   Span(doc225, 22, 23, label ="PRICE"),
   Span(doc225, 23, 24, label ="UNIT"),
   Span(doc225, 25, 26, label ="SUMMA"),
   Span(doc225, 60, 61, label ="TARIFF"),
   Span(doc225, 65, 66, label ="COUNTRY"),
   Span(doc225, 68, 69, label ="PR_SURCH"),
   Span(doc225, 70, 71, label ="SURCHARGE"),
   Span(doc225, 73, 74, label ="PR_ESURCH"),
   Span(doc225, 75, 76, label ="ESURCHARGE"),
   Span(doc225, 76, 77, label ="TOTAL")]
docs.append(doc225)
print("doc226, 67, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 33000; AMOUNT 175; ARTICLE 6020000656; PRICE 183,12; UNIT 100; SUMMA 320,46; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 22,11; PR_ESURCH 3,50; ESURCHARGE 11,22; TOTAL 353,79; ")
doc226 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 33000 175 PC 6020000656 (*) 183,12 100 PC 320,46 FI-GE-28LM-OR-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 22,11 Energy Surcharge 3,50 % 11,22 353,79''')
doc226.ents = [
   Span(doc226, 3, 4, label ="NORDER"),
   Span(doc226, 9, 12, label ="CONTRACT"),
   Span(doc226, 12, 13, label ="CONTRACT1"),
   Span(doc226, 15, 16, label ="POS"),
   Span(doc226, 16, 17, label ="AMOUNT"),
   Span(doc226, 18, 19, label ="ARTICLE"),
   Span(doc226, 22, 23, label ="PRICE"),
   Span(doc226, 23, 24, label ="UNIT"),
   Span(doc226, 25, 26, label ="SUMMA"),
   Span(doc226, 50, 51, label ="TARIFF"),
   Span(doc226, 55, 56, label ="COUNTRY"),
   Span(doc226, 58, 59, label ="PR_SURCH"),
   Span(doc226, 60, 61, label ="SURCHARGE"),
   Span(doc226, 63, 64, label ="PR_ESURCH"),
   Span(doc226, 65, 66, label ="ESURCHARGE"),
   Span(doc226, 66, 67, label ="TOTAL")]
docs.append(doc226)
print("doc227, 79, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 33100; AMOUNT 750; ARTICLE 6020000541; PRICE 670,58; UNIT 100; SUMMA 5.029,35; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 347,03; PR_ESURCH 3,50; ESURCHARGE 176,03; TOTAL 5.552,41; ")
doc227 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 33100 750 PC 6020000541 (*) 670,58 100 PC 5.029,35 FI-GE-28LR1 -1/4-WD-B-W3 FI-GE-28LR1 1/4-WD-B-W3 packed per each item    Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 347,03 Energy Surcharge 3,50 % 176,03 5.552,41''')
doc227.ents = [
   Span(doc227, 3, 4, label ="NORDER"),
   Span(doc227, 9, 12, label ="CONTRACT"),
   Span(doc227, 12, 13, label ="CONTRACT1"),
   Span(doc227, 15, 16, label ="POS"),
   Span(doc227, 16, 17, label ="AMOUNT"),
   Span(doc227, 18, 19, label ="ARTICLE"),
   Span(doc227, 22, 23, label ="PRICE"),
   Span(doc227, 23, 24, label ="UNIT"),
   Span(doc227, 25, 26, label ="SUMMA"),
   Span(doc227, 62, 63, label ="TARIFF"),
   Span(doc227, 67, 68, label ="COUNTRY"),
   Span(doc227, 70, 71, label ="PR_SURCH"),
   Span(doc227, 72, 73, label ="SURCHARGE"),
   Span(doc227, 75, 76, label ="PR_ESURCH"),
   Span(doc227, 77, 78, label ="ESURCHARGE"),
   Span(doc227, 78, 79, label ="TOTAL")]
docs.append(doc227)
print("doc228, 67, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 33200; AMOUNT 200; ARTICLE 6020000481; PRICE 162,78; UNIT 100; SUMMA 325,56; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 22,46; PR_ESURCH 3,50; ESURCHARGE 11,39; TOTAL 359,41; ")
doc228 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 33200 200 PC 6020000481 (*) 162,78 100 PC 325,56 FI-GE-28LR-WD-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 22,46 Energy Surcharge 3,50 % 11,39 359,41''')
doc228.ents = [
   Span(doc228, 3, 4, label ="NORDER"),
   Span(doc228, 9, 12, label ="CONTRACT"),
   Span(doc228, 12, 13, label ="CONTRACT1"),
   Span(doc228, 15, 16, label ="POS"),
   Span(doc228, 16, 17, label ="AMOUNT"),
   Span(doc228, 18, 19, label ="ARTICLE"),
   Span(doc228, 22, 23, label ="PRICE"),
   Span(doc228, 23, 24, label ="UNIT"),
   Span(doc228, 25, 26, label ="SUMMA"),
   Span(doc228, 50, 51, label ="TARIFF"),
   Span(doc228, 55, 56, label ="COUNTRY"),
   Span(doc228, 58, 59, label ="PR_SURCH"),
   Span(doc228, 60, 61, label ="SURCHARGE"),
   Span(doc228, 63, 64, label ="PR_ESURCH"),
   Span(doc228, 65, 66, label ="ESURCHARGE"),
   Span(doc228, 66, 67, label ="TOTAL")]
docs.append(doc228)
print("doc229, 75, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 33300; AMOUNT 60; ARTICLE 6020000277; PRICE 349,72; UNIT 100; SUMMA 209,83; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 14,48; PR_ESURCH 3,50; ESURCHARGE 7,34; TOTAL 231,65; ")
doc229 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 33300 60 PC 6020000277 (*) 349,72 100 PC 209,83 FI-GE-3 5L1 -5/8U-B-W3 FI-GE-35L1 5/8U-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 14,48 Energy Surcharge 3,50 % 7,34 231,65''')
doc229.ents = [
   Span(doc229, 3, 4, label ="NORDER"),
   Span(doc229, 9, 12, label ="CONTRACT"),
   Span(doc229, 12, 13, label ="CONTRACT1"),
   Span(doc229, 15, 16, label ="POS"),
   Span(doc229, 16, 17, label ="AMOUNT"),
   Span(doc229, 18, 19, label ="ARTICLE"),
   Span(doc229, 22, 23, label ="PRICE"),
   Span(doc229, 23, 24, label ="UNIT"),
   Span(doc229, 25, 26, label ="SUMMA"),
   Span(doc229, 58, 59, label ="TARIFF"),
   Span(doc229, 63, 64, label ="COUNTRY"),
   Span(doc229, 66, 67, label ="PR_SURCH"),
   Span(doc229, 68, 69, label ="SURCHARGE"),
   Span(doc229, 71, 72, label ="PR_ESURCH"),
   Span(doc229, 73, 74, label ="ESURCHARGE"),
   Span(doc229, 74, 75, label ="TOTAL")]
docs.append(doc229)
print("doc230, 68, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 33400; AMOUNT 30; ARTICLE 6020000380; PRICE 277,59; UNIT 100; SUMMA 83,28; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 5,75; PR_ESURCH 3,50; ESURCHARGE 2,91; TOTAL 91,94; ")
doc230 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 33400 30 PC 6020000380 (*) 277,59 100 PC 83,28 FI-GE-35LM-WD-B-W3    packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 5,75 Energy Surcharge 3,50 % 2,91 91,94''')
doc230.ents = [
   Span(doc230, 3, 4, label ="NORDER"),
   Span(doc230, 9, 12, label ="CONTRACT"),
   Span(doc230, 12, 13, label ="CONTRACT1"),
   Span(doc230, 15, 16, label ="POS"),
   Span(doc230, 16, 17, label ="AMOUNT"),
   Span(doc230, 18, 19, label ="ARTICLE"),
   Span(doc230, 22, 23, label ="PRICE"),
   Span(doc230, 23, 24, label ="UNIT"),
   Span(doc230, 25, 26, label ="SUMMA"),
   Span(doc230, 51, 52, label ="TARIFF"),
   Span(doc230, 56, 57, label ="COUNTRY"),
   Span(doc230, 59, 60, label ="PR_SURCH"),
   Span(doc230, 61, 62, label ="SURCHARGE"),
   Span(doc230, 64, 65, label ="PR_ESURCH"),
   Span(doc230, 66, 67, label ="ESURCHARGE"),
   Span(doc230, 67, 68, label ="TOTAL")]
docs.append(doc230)
print("doc231, 65, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 33500; AMOUNT 75; ARTICLE 6020000198; PRICE 64,12; UNIT 100; SUMMA 48,09; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 3,32; PR_ESURCH 3,50; ESURCHARGE 1,68; TOTAL 53,09; ")
doc231 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 33500 75 PC 6020000198 (*) 64,12 100 PC 48,09 FI-GS-06L-W3-SKM packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 3,32 Energy Surcharge 3,50 % 1,68 53,09''')
doc231.ents = [
   Span(doc231, 3, 4, label ="NORDER"),
   Span(doc231, 9, 12, label ="CONTRACT"),
   Span(doc231, 12, 13, label ="CONTRACT1"),
   Span(doc231, 15, 16, label ="POS"),
   Span(doc231, 16, 17, label ="AMOUNT"),
   Span(doc231, 18, 19, label ="ARTICLE"),
   Span(doc231, 22, 23, label ="PRICE"),
   Span(doc231, 23, 24, label ="UNIT"),
   Span(doc231, 25, 26, label ="SUMMA"),
   Span(doc231, 48, 49, label ="TARIFF"),
   Span(doc231, 53, 54, label ="COUNTRY"),
   Span(doc231, 56, 57, label ="PR_SURCH"),
   Span(doc231, 58, 59, label ="SURCHARGE"),
   Span(doc231, 61, 62, label ="PR_ESURCH"),
   Span(doc231, 63, 64, label ="ESURCHARGE"),
   Span(doc231, 64, 65, label ="TOTAL")]
docs.append(doc231)
print("doc232, 67, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 33600; AMOUNT 1.680; ARTICLE 6020000199; PRICE 63,56; UNIT 100; SUMMA 1.067; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 73,68; PR_ESURCH 3,50; ESURCHARGE 37,37; TOTAL 1.178,86; ")
doc232 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 33600 1.680 PC 6020000199 (*) 63,56 100 PC 1.067 ,81 FI-GS-08L-W3-SKM packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 73,68 Energy Surcharge 3,50 % 37,37 1.178,86''')
doc232.ents = [
   Span(doc232, 3, 4, label ="NORDER"),
   Span(doc232, 9, 12, label ="CONTRACT"),
   Span(doc232, 12, 13, label ="CONTRACT1"),
   Span(doc232, 15, 16, label ="POS"),
   Span(doc232, 16, 17, label ="AMOUNT"),
   Span(doc232, 18, 19, label ="ARTICLE"),
   Span(doc232, 22, 23, label ="PRICE"),
   Span(doc232, 23, 24, label ="UNIT"),
   Span(doc232, 25, 26, label ="SUMMA"),
   Span(doc232, 50, 51, label ="TARIFF"),
   Span(doc232, 55, 56, label ="COUNTRY"),
   Span(doc232, 58, 59, label ="PR_SURCH"),
   Span(doc232, 60, 61, label ="SURCHARGE"),
   Span(doc232, 63, 64, label ="PR_ESURCH"),
   Span(doc232, 65, 66, label ="ESURCHARGE"),
   Span(doc232, 66, 67, label ="TOTAL")]
docs.append(doc232)
print("doc233, 66, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 33700; AMOUNT 60; ARTICLE 6020000203; PRICE 233,65; UNIT 100; SUMMA 140,19; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 9,67; PR_ESURCH 3,50; ESURCHARGE 4,91; TOTAL 154,77; ")
doc233 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 33700 60 PC 6020000203 (*) 233,65 100 PC 140,19 FI-GS-18L-W3-SKM    packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 9,67 Energy Surcharge 3,50 % 4,91 154,77''')
doc233.ents = [
   Span(doc233, 3, 4, label ="NORDER"),
   Span(doc233, 9, 12, label ="CONTRACT"),
   Span(doc233, 12, 13, label ="CONTRACT1"),
   Span(doc233, 15, 16, label ="POS"),
   Span(doc233, 16, 17, label ="AMOUNT"),
   Span(doc233, 18, 19, label ="ARTICLE"),
   Span(doc233, 22, 23, label ="PRICE"),
   Span(doc233, 23, 24, label ="UNIT"),
   Span(doc233, 25, 26, label ="SUMMA"),
   Span(doc233, 49, 50, label ="TARIFF"),
   Span(doc233, 54, 55, label ="COUNTRY"),
   Span(doc233, 57, 58, label ="PR_SURCH"),
   Span(doc233, 59, 60, label ="SURCHARGE"),
   Span(doc233, 62, 63, label ="PR_ESURCH"),
   Span(doc233, 64, 65, label ="ESURCHARGE"),
   Span(doc233, 65, 66, label ="TOTAL")]
docs.append(doc233)
print("doc234, 65, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 33800; AMOUNT 120; ARTICLE 6020000206; PRICE 697,55; UNIT 100; SUMMA 837,06; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 57,76; PR_ESURCH 3,50; ESURCHARGE 29,30; TOTAL 924,12; ")
doc234 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 33800 120 PC 6020000206 (*) 697,55 100 PC 837,06 FI-GS-35L-W3-SKM packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 57,76 Energy Surcharge 3,50 % 29,30 924,12''')
doc234.ents = [
   Span(doc234, 3, 4, label ="NORDER"),
   Span(doc234, 9, 12, label ="CONTRACT"),
   Span(doc234, 12, 13, label ="CONTRACT1"),
   Span(doc234, 15, 16, label ="POS"),
   Span(doc234, 16, 17, label ="AMOUNT"),
   Span(doc234, 18, 19, label ="ARTICLE"),
   Span(doc234, 22, 23, label ="PRICE"),
   Span(doc234, 23, 24, label ="UNIT"),
   Span(doc234, 25, 26, label ="SUMMA"),
   Span(doc234, 48, 49, label ="TARIFF"),
   Span(doc234, 53, 54, label ="COUNTRY"),
   Span(doc234, 56, 57, label ="PR_SURCH"),
   Span(doc234, 58, 59, label ="SURCHARGE"),
   Span(doc234, 61, 62, label ="PR_ESURCH"),
   Span(doc234, 63, 64, label ="ESURCHARGE"),
   Span(doc234, 64, 65, label ="TOTAL")]
docs.append(doc234)
print("doc235, 60, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 34000; AMOUNT 100; ARTICLE 6030003465; PRICE 467,12; UNIT 100; SUMMA 467,12; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 32,23; PR_ESURCH 3,50; ESURCHARGE 16,35; TOTAL 515,70; ")
doc235 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 34000 100 PC 6030003465 467,12 100 PC 467,12 FI-T-12/08/08L-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 32,23 Energy Surcharge 3,50 % 16,35 515,70''')
doc235.ents = [
   Span(doc235, 3, 4, label ="NORDER"),
   Span(doc235, 9, 12, label ="CONTRACT"),
   Span(doc235, 12, 13, label ="CONTRACT1"),
   Span(doc235, 15, 16, label ="POS"),
   Span(doc235, 16, 17, label ="AMOUNT"),
   Span(doc235, 18, 19, label ="ARTICLE"),
   Span(doc235, 19, 20, label ="PRICE"),
   Span(doc235, 20, 21, label ="UNIT"),
   Span(doc235, 22, 23, label ="SUMMA"),
   Span(doc235, 43, 44, label ="TARIFF"),
   Span(doc235, 48, 49, label ="COUNTRY"),
   Span(doc235, 51, 52, label ="PR_SURCH"),
   Span(doc235, 53, 54, label ="SURCHARGE"),
   Span(doc235, 56, 57, label ="PR_ESURCH"),
   Span(doc235, 58, 59, label ="ESURCHARGE"),
   Span(doc235, 59, 60, label ="TOTAL")]
docs.append(doc235)
print("doc236, 61, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 34100; AMOUNT 100; ARTICLE 6030003463; PRICE 257,10; UNIT 100; SUMMA 257,10; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 17,74; PR_ESURCH 3,50; ESURCHARGE 9,00; TOTAL 283,84; ")
doc236 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 34100 100 PC 6030003463 257,10 100 PC 257,10 FI-T-12/08/12L-W3    packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 17,74 Energy Surcharge 3,50 % 9,00 283,84''')
doc236.ents = [
   Span(doc236, 3, 4, label ="NORDER"),
   Span(doc236, 9, 12, label ="CONTRACT"),
   Span(doc236, 12, 13, label ="CONTRACT1"),
   Span(doc236, 15, 16, label ="POS"),
   Span(doc236, 16, 17, label ="AMOUNT"),
   Span(doc236, 18, 19, label ="ARTICLE"),
   Span(doc236, 19, 20, label ="PRICE"),
   Span(doc236, 20, 21, label ="UNIT"),
   Span(doc236, 22, 23, label ="SUMMA"),
   Span(doc236, 44, 45, label ="TARIFF"),
   Span(doc236, 49, 50, label ="COUNTRY"),
   Span(doc236, 52, 53, label ="PR_SURCH"),
   Span(doc236, 54, 55, label ="SURCHARGE"),
   Span(doc236, 57, 58, label ="PR_ESURCH"),
   Span(doc236, 59, 60, label ="ESURCHARGE"),
   Span(doc236, 60, 61, label ="TOTAL")]
docs.append(doc236)
print("doc237, 60, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 34200; AMOUNT 220; ARTICLE 6030003850; PRICE 348,87; UNIT 100; SUMMA 767,51; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 52,96; PR_ESURCH 3,50; ESURCHARGE 26,86; TOTAL 847,33; ")
doc237 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 34200 220 PC 6030003850 348,87 100 PC 767,51 FI-T-22L-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 52,96 Energy Surcharge 3,50 % 26,86 847,33''')
doc237.ents = [
   Span(doc237, 3, 4, label ="NORDER"),
   Span(doc237, 9, 12, label ="CONTRACT"),
   Span(doc237, 12, 13, label ="CONTRACT1"),
   Span(doc237, 15, 16, label ="POS"),
   Span(doc237, 16, 17, label ="AMOUNT"),
   Span(doc237, 18, 19, label ="ARTICLE"),
   Span(doc237, 19, 20, label ="PRICE"),
   Span(doc237, 20, 21, label ="UNIT"),
   Span(doc237, 22, 23, label ="SUMMA"),
   Span(doc237, 43, 44, label ="TARIFF"),
   Span(doc237, 48, 49, label ="COUNTRY"),
   Span(doc237, 51, 52, label ="PR_SURCH"),
   Span(doc237, 53, 54, label ="SURCHARGE"),
   Span(doc237, 56, 57, label ="PR_ESURCH"),
   Span(doc237, 58, 59, label ="ESURCHARGE"),
   Span(doc237, 59, 60, label ="TOTAL")]
docs.append(doc237)
print("doc238, 60, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 34300; AMOUNT 20; ARTICLE 6030003851; PRICE 550,65; UNIT 100; SUMMA 110,13; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 7,60; PR_ESURCH 3,50; ESURCHARGE 3,85; TOTAL 121,58; ")
doc238 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 34300 20 PC 6030003851 550,65 100 PC 110,13 FI-T-28L-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 7,60 Energy Surcharge 3,50 % 3,85 121,58''')
doc238.ents = [
   Span(doc238, 3, 4, label ="NORDER"),
   Span(doc238, 9, 12, label ="CONTRACT"),
   Span(doc238, 12, 13, label ="CONTRACT1"),
   Span(doc238, 15, 16, label ="POS"),
   Span(doc238, 16, 17, label ="AMOUNT"),
   Span(doc238, 18, 19, label ="ARTICLE"),
   Span(doc238, 19, 20, label ="PRICE"),
   Span(doc238, 20, 21, label ="UNIT"),
   Span(doc238, 22, 23, label ="SUMMA"),
   Span(doc238, 43, 44, label ="TARIFF"),
   Span(doc238, 48, 49, label ="COUNTRY"),
   Span(doc238, 51, 52, label ="PR_SURCH"),
   Span(doc238, 53, 54, label ="SURCHARGE"),
   Span(doc238, 56, 57, label ="PR_ESURCH"),
   Span(doc238, 58, 59, label ="ESURCHARGE"),
   Span(doc238, 59, 60, label ="TOTAL")]
docs.append(doc238)
print("doc239, 61, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 34400; AMOUNT 10; ARTICLE 6030003530; PRICE 2.656,70; UNIT 100; SUMMA 265,67; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 18,33; PR_ESURCH 3,50; ESURCHARGE 9,30; TOTAL 293,30; ")
doc239 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 34400 10 PC 6030003530 2.656,70 100 PC 265,67 FI-T-30/20/30S-W3    packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 18,33 Energy Surcharge 3,50 % 9,30 293,30''')
doc239.ents = [
   Span(doc239, 3, 4, label ="NORDER"),
   Span(doc239, 9, 12, label ="CONTRACT"),
   Span(doc239, 12, 13, label ="CONTRACT1"),
   Span(doc239, 15, 16, label ="POS"),
   Span(doc239, 16, 17, label ="AMOUNT"),
   Span(doc239, 18, 19, label ="ARTICLE"),
   Span(doc239, 19, 20, label ="PRICE"),
   Span(doc239, 20, 21, label ="UNIT"),
   Span(doc239, 22, 23, label ="SUMMA"),
   Span(doc239, 44, 45, label ="TARIFF"),
   Span(doc239, 49, 50, label ="COUNTRY"),
   Span(doc239, 52, 53, label ="PR_SURCH"),
   Span(doc239, 54, 55, label ="SURCHARGE"),
   Span(doc239, 57, 58, label ="PR_ESURCH"),
   Span(doc239, 59, 60, label ="ESURCHARGE"),
   Span(doc239, 60, 61, label ="TOTAL")]
docs.append(doc239)
print("doc240, 60, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 34500; AMOUNT 100; ARTICLE 6030003432; PRICE 89,01; UNIT 100; SUMMA 89,01; TARIFF 73079290; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 6,14; PR_ESURCH 3,50; ESURCHARGE 3,12; TOTAL 98,27; ")
doc240 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 34500 100 PC 6030003432 89,01 100 PC 89,01 FI-W-08L-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079290 Country of origin: Germany Material Surcharge 6,90 % 6,14 Energy Surcharge 3,50 % 3,12 98,27''')
doc240.ents = [
   Span(doc240, 3, 4, label ="NORDER"),
   Span(doc240, 9, 12, label ="CONTRACT"),
   Span(doc240, 12, 13, label ="CONTRACT1"),
   Span(doc240, 15, 16, label ="POS"),
   Span(doc240, 16, 17, label ="AMOUNT"),
   Span(doc240, 18, 19, label ="ARTICLE"),
   Span(doc240, 19, 20, label ="PRICE"),
   Span(doc240, 20, 21, label ="UNIT"),
   Span(doc240, 22, 23, label ="SUMMA"),
   Span(doc240, 43, 44, label ="TARIFF"),
   Span(doc240, 48, 49, label ="COUNTRY"),
   Span(doc240, 51, 52, label ="PR_SURCH"),
   Span(doc240, 53, 54, label ="SURCHARGE"),
   Span(doc240, 56, 57, label ="PR_ESURCH"),
   Span(doc240, 58, 59, label ="ESURCHARGE"),
   Span(doc240, 59, 60, label ="TOTAL")]
docs.append(doc240)
print("doc241, 60, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 34600; AMOUNT 35; ARTICLE 6030003435; PRICE 148,97; UNIT 100; SUMMA 52,14; TARIFF 73079290; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 3,60; PR_ESURCH 3,50; ESURCHARGE 1,82; TOTAL 57,56; ")
doc241 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 34600 35 PC 6030003435 148,97 100 PC 52,14 FI-W-15L-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079290 Country of origin: Germany Material Surcharge 6,90 % 3,60 Energy Surcharge 3,50 % 1,82 57,56''')
doc241.ents = [
   Span(doc241, 3, 4, label ="NORDER"),
   Span(doc241, 9, 12, label ="CONTRACT"),
   Span(doc241, 12, 13, label ="CONTRACT1"),
   Span(doc241, 15, 16, label ="POS"),
   Span(doc241, 16, 17, label ="AMOUNT"),
   Span(doc241, 18, 19, label ="ARTICLE"),
   Span(doc241, 19, 20, label ="PRICE"),
   Span(doc241, 20, 21, label ="UNIT"),
   Span(doc241, 22, 23, label ="SUMMA"),
   Span(doc241, 43, 44, label ="TARIFF"),
   Span(doc241, 48, 49, label ="COUNTRY"),
   Span(doc241, 51, 52, label ="PR_SURCH"),
   Span(doc241, 53, 54, label ="SURCHARGE"),
   Span(doc241, 56, 57, label ="PR_ESURCH"),
   Span(doc241, 58, 59, label ="ESURCHARGE"),
   Span(doc241, 59, 60, label ="TOTAL")]
docs.append(doc241)
print("doc242, 69, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 34700; AMOUNT 225; ARTICLE 6010008012; PRICE 153,69; UNIT 100; SUMMA 345,80; TARIFF 73079290; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 23,86; PR_ESURCH 3,50; ESURCHARGE 12,10; TOTAL 381,76; ")
doc242 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 34700 225 PC 6010008012 (*) 153,69 100 PC 345,80 FI-WEE-0 8LM-OR-B-W3    packed per each item Product description: fitting Export - Customs tariff no.: 73079290 Country of origin: Germany Material Surcharge 6,90 % 23,86 Energy Surcharge 3,50 % 12,10 381,76''')
doc242.ents = [
   Span(doc242, 3, 4, label ="NORDER"),
   Span(doc242, 9, 12, label ="CONTRACT"),
   Span(doc242, 12, 13, label ="CONTRACT1"),
   Span(doc242, 15, 16, label ="POS"),
   Span(doc242, 16, 17, label ="AMOUNT"),
   Span(doc242, 18, 19, label ="ARTICLE"),
   Span(doc242, 22, 23, label ="PRICE"),
   Span(doc242, 23, 24, label ="UNIT"),
   Span(doc242, 25, 26, label ="SUMMA"),
   Span(doc242, 52, 53, label ="TARIFF"),
   Span(doc242, 57, 58, label ="COUNTRY"),
   Span(doc242, 60, 61, label ="PR_SURCH"),
   Span(doc242, 62, 63, label ="SURCHARGE"),
   Span(doc242, 65, 66, label ="PR_ESURCH"),
   Span(doc242, 67, 68, label ="ESURCHARGE"),
   Span(doc242, 68, 69, label ="TOTAL")]
docs.append(doc242)
print("doc243, 65, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 34800; AMOUNT 90; ARTICLE 6020003354; PRICE 251,01; UNIT 100; SUMMA 225,91; TARIFF 73079290; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 15,59; PR_ESURCH 3,50; ESURCHARGE 7,91; TOTAL 249,41; ")
doc243 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 34800 90 PC 6020003354 (*) 251,01 100 PC 225,91 FI-WS-15L-W3-SKM packed per each item Product description: fitting Export - Customs tariff no.: 73079290 Country of origin: Germany Material Surcharge 6,90 % 15,59 Energy Surcharge 3,50 % 7,91 249,41''')
doc243.ents = [
   Span(doc243, 3, 4, label ="NORDER"),
   Span(doc243, 9, 12, label ="CONTRACT"),
   Span(doc243, 12, 13, label ="CONTRACT1"),
   Span(doc243, 15, 16, label ="POS"),
   Span(doc243, 16, 17, label ="AMOUNT"),
   Span(doc243, 18, 19, label ="ARTICLE"),
   Span(doc243, 22, 23, label ="PRICE"),
   Span(doc243, 23, 24, label ="UNIT"),
   Span(doc243, 25, 26, label ="SUMMA"),
   Span(doc243, 48, 49, label ="TARIFF"),
   Span(doc243, 53, 54, label ="COUNTRY"),
   Span(doc243, 56, 57, label ="PR_SURCH"),
   Span(doc243, 58, 59, label ="SURCHARGE"),
   Span(doc243, 61, 62, label ="PR_ESURCH"),
   Span(doc243, 63, 64, label ="ESURCHARGE"),
   Span(doc243, 64, 65, label ="TOTAL")]
docs.append(doc243)
print("doc244, 67, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 34900; AMOUNT 100; ARTICLE 6020000131; PRICE 343,04; UNIT 100; SUMMA 343,04; TARIFF 73079290; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 23,67; PR_ESURCH 3,50; ESURCHARGE 12,01; TOTAL 378,72; ")
doc244 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 34900 100 PC 6020000131 (*) 343,04 100 PC 343,04 FI-WS-18L-W3-OGR-SKM packed per each item Product description: fitting Export - Customs tariff no.: 73079290 Country of origin: Germany Material Surcharge 6,90 % 23,67 Energy Surcharge 3,50 % 12,01 378,72''')
doc244.ents = [
   Span(doc244, 3, 4, label ="NORDER"),
   Span(doc244, 9, 12, label ="CONTRACT"),
   Span(doc244, 12, 13, label ="CONTRACT1"),
   Span(doc244, 15, 16, label ="POS"),
   Span(doc244, 16, 17, label ="AMOUNT"),
   Span(doc244, 18, 19, label ="ARTICLE"),
   Span(doc244, 22, 23, label ="PRICE"),
   Span(doc244, 23, 24, label ="UNIT"),
   Span(doc244, 25, 26, label ="SUMMA"),
   Span(doc244, 50, 51, label ="TARIFF"),
   Span(doc244, 55, 56, label ="COUNTRY"),
   Span(doc244, 58, 59, label ="PR_SURCH"),
   Span(doc244, 60, 61, label ="SURCHARGE"),
   Span(doc244, 63, 64, label ="PR_ESURCH"),
   Span(doc244, 65, 66, label ="ESURCHARGE"),
   Span(doc244, 66, 67, label ="TOTAL")]
docs.append(doc244)
print("doc245, 68, #NORDER 2399653; CONTRACT SR-1-06; CONTRACT1 19; POS 35000; AMOUNT 30; ARTICLE 6020000132; PRICE 559,33; UNIT 100; SUMMA 167,80; TARIFF 73079290; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 11,58; PR_ESURCH 3,50; ESURCHARGE 5,87; TOTAL 185,25; ")
doc245 = nlp('''Order number: 2399653 Purchase order number: N SR-1-06 19** 35000 30 PC 6020000132 (*) 559,33 100 PC 167,80 FI-WS-22L-W3-OGR-SKM    packed per each item Product description: fitting Export - Customs tariff no.: 73079290 Country of origin: Germany Material Surcharge 6,90 % 11,58 Energy Surcharge 3,50 % 5,87 185,25''')
doc245.ents = [
   Span(doc245, 3, 4, label ="NORDER"),
   Span(doc245, 9, 12, label ="CONTRACT"),
   Span(doc245, 12, 13, label ="CONTRACT1"),
   Span(doc245, 15, 16, label ="POS"),
   Span(doc245, 16, 17, label ="AMOUNT"),
   Span(doc245, 18, 19, label ="ARTICLE"),
   Span(doc245, 22, 23, label ="PRICE"),
   Span(doc245, 23, 24, label ="UNIT"),
   Span(doc245, 25, 26, label ="SUMMA"),
   Span(doc245, 51, 52, label ="TARIFF"),
   Span(doc245, 56, 57, label ="COUNTRY"),
   Span(doc245, 59, 60, label ="PR_SURCH"),
   Span(doc245, 61, 62, label ="SURCHARGE"),
   Span(doc245, 64, 65, label ="PR_ESURCH"),
   Span(doc245, 66, 67, label ="ESURCHARGE"),
   Span(doc245, 67, 68, label ="TOTAL")]
docs.append(doc245)
print("doc246, 59, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 35100; AMOUNT 300; ARTICLE 6100196603; PRICE 32,75; UNIT 100; SUMMA 98,25; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 11,20; PR_ESURCH 3,50; ESURCHARGE 3,44; TOTAL 112,89; ")
doc246 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 35100 300 PC 6100196603 32,75 100 PC 98,25 LBBU-212-SA-M8/U5/1 6/2 packed per each item Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 11,20 Energy Surcharge 3,50 % 3,44 112,89''')
doc246.ents = [
   Span(doc246, 3, 4, label ="NORDER"),
   Span(doc246, 9, 12, label ="CONTRACT"),
   Span(doc246, 12, 13, label ="CONTRACT1"),
   Span(doc246, 15, 16, label ="POS"),
   Span(doc246, 16, 17, label ="AMOUNT"),
   Span(doc246, 18, 19, label ="ARTICLE"),
   Span(doc246, 19, 20, label ="PRICE"),
   Span(doc246, 20, 21, label ="UNIT"),
   Span(doc246, 22, 23, label ="SUMMA"),
   Span(doc246, 42, 43, label ="TARIFF"),
   Span(doc246, 47, 48, label ="COUNTRY"),
   Span(doc246, 50, 51, label ="PR_SURCH"),
   Span(doc246, 52, 53, label ="SURCHARGE"),
   Span(doc246, 55, 56, label ="PR_ESURCH"),
   Span(doc246, 57, 58, label ="ESURCHARGE"),
   Span(doc246, 58, 59, label ="TOTAL")]
docs.append(doc246)
print("doc247, 59, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 35200; AMOUNT 1.500; ARTICLE 6100196618; PRICE 52,37; UNIT 100; SUMMA 785,55; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 89,55; PR_ESURCH 3,50; ESURCHARGE 27,49; TOTAL 902,59; ")
doc247 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 35200 1.500 PC 6100196618 52,37 100 PC 785,55 LBBU-2 15/12-SA-M8/U5/16/2 packed per each item Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 89,55 Energy Surcharge 3,50 % 27,49 902,59''')
doc247.ents = [
   Span(doc247, 3, 4, label ="NORDER"),
   Span(doc247, 9, 12, label ="CONTRACT"),
   Span(doc247, 12, 13, label ="CONTRACT1"),
   Span(doc247, 15, 16, label ="POS"),
   Span(doc247, 16, 17, label ="AMOUNT"),
   Span(doc247, 18, 19, label ="ARTICLE"),
   Span(doc247, 19, 20, label ="PRICE"),
   Span(doc247, 20, 21, label ="UNIT"),
   Span(doc247, 22, 23, label ="SUMMA"),
   Span(doc247, 42, 43, label ="TARIFF"),
   Span(doc247, 47, 48, label ="COUNTRY"),
   Span(doc247, 50, 51, label ="PR_SURCH"),
   Span(doc247, 52, 53, label ="SURCHARGE"),
   Span(doc247, 55, 56, label ="PR_ESURCH"),
   Span(doc247, 57, 58, label ="ESURCHARGE"),
   Span(doc247, 58, 59, label ="TOTAL")]
docs.append(doc247)
print("doc248, 60, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 35300; AMOUNT 200; ARTICLE 6100196619; PRICE 52,37; UNIT 100; SUMMA 104,74; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 11,94; PR_ESURCH 3,50; ESURCHARGE 3,67; TOTAL 120,35; ")
doc248 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 35300 200 PC 6100196619 52,37 100 PC 104,74 LBBU-2 15/15-SA-M8/U5/16/2 packed per each item Export - Customs tariff no.: 39269097    Country of origin: Germany Material Surcharge 11,40 % 11,94 Energy Surcharge 3,50 % 3,67 120,35''')
doc248.ents = [
   Span(doc248, 3, 4, label ="NORDER"),
   Span(doc248, 9, 12, label ="CONTRACT"),
   Span(doc248, 12, 13, label ="CONTRACT1"),
   Span(doc248, 15, 16, label ="POS"),
   Span(doc248, 16, 17, label ="AMOUNT"),
   Span(doc248, 18, 19, label ="ARTICLE"),
   Span(doc248, 19, 20, label ="PRICE"),
   Span(doc248, 20, 21, label ="UNIT"),
   Span(doc248, 22, 23, label ="SUMMA"),
   Span(doc248, 42, 43, label ="TARIFF"),
   Span(doc248, 48, 49, label ="COUNTRY"),
   Span(doc248, 51, 52, label ="PR_SURCH"),
   Span(doc248, 53, 54, label ="SURCHARGE"),
   Span(doc248, 56, 57, label ="PR_ESURCH"),
   Span(doc248, 58, 59, label ="ESURCHARGE"),
   Span(doc248, 59, 60, label ="TOTAL")]
docs.append(doc248)
print("doc249, 59, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 35400; AMOUNT 500; ARTICLE 6100196617; PRICE 32,75; UNIT 100; SUMMA 163,75; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 18,67; PR_ESURCH 3,50; ESURCHARGE 5,73; TOTAL 188,15; ")
doc249 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 35400 500 PC 6100196617 32,75 100 PC 163,75 LBBU-2 15-SA-M8/U5/16/2 packed per each item Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 18,67 Energy Surcharge 3,50 % 5,73 188,15''')
doc249.ents = [
   Span(doc249, 3, 4, label ="NORDER"),
   Span(doc249, 9, 12, label ="CONTRACT"),
   Span(doc249, 12, 13, label ="CONTRACT1"),
   Span(doc249, 15, 16, label ="POS"),
   Span(doc249, 16, 17, label ="AMOUNT"),
   Span(doc249, 18, 19, label ="ARTICLE"),
   Span(doc249, 19, 20, label ="PRICE"),
   Span(doc249, 20, 21, label ="UNIT"),
   Span(doc249, 22, 23, label ="SUMMA"),
   Span(doc249, 42, 43, label ="TARIFF"),
   Span(doc249, 47, 48, label ="COUNTRY"),
   Span(doc249, 50, 51, label ="PR_SURCH"),
   Span(doc249, 52, 53, label ="SURCHARGE"),
   Span(doc249, 55, 56, label ="PR_ESURCH"),
   Span(doc249, 57, 58, label ="ESURCHARGE"),
   Span(doc249, 58, 59, label ="TOTAL")]
docs.append(doc249)
print("doc250, 59, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 35500; AMOUNT 150; ARTICLE 6100196628; PRICE 52,37; UNIT 100; SUMMA 78,56; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 8,96; PR_ESURCH 3,50; ESURCHARGE 2,75; TOTAL 90,27; ")
doc250 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 35500 150 PC 6100196628 52,37 100 PC 78,56 LBBU-2 16/16-SA-M8/U5/16/2 packed per each item Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 8,96 Energy Surcharge 3,50 % 2,75 90,27''')
doc250.ents = [
   Span(doc250, 3, 4, label ="NORDER"),
   Span(doc250, 9, 12, label ="CONTRACT"),
   Span(doc250, 12, 13, label ="CONTRACT1"),
   Span(doc250, 15, 16, label ="POS"),
   Span(doc250, 16, 17, label ="AMOUNT"),
   Span(doc250, 18, 19, label ="ARTICLE"),
   Span(doc250, 19, 20, label ="PRICE"),
   Span(doc250, 20, 21, label ="UNIT"),
   Span(doc250, 22, 23, label ="SUMMA"),
   Span(doc250, 42, 43, label ="TARIFF"),
   Span(doc250, 47, 48, label ="COUNTRY"),
   Span(doc250, 50, 51, label ="PR_SURCH"),
   Span(doc250, 52, 53, label ="SURCHARGE"),
   Span(doc250, 55, 56, label ="PR_ESURCH"),
   Span(doc250, 57, 58, label ="ESURCHARGE"),
   Span(doc250, 58, 59, label ="TOTAL")]
docs.append(doc250)
print("doc251, 59, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 35600; AMOUNT 200; ARTICLE 6100196636; PRICE 52,37; UNIT 100; SUMMA 104,74; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 11,94; PR_ESURCH 3,50; ESURCHARGE 3,67; TOTAL 120,35; ")
doc251 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 35600 200 PC 6100196636 52,37 100 PC 104,74 LBBU-218/15-SA-M8/U5/16/2 packed per each item Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 11,94 Energy Surcharge 3,50 % 3,67   120,35''')
doc251.ents = [
   Span(doc251, 3, 4, label ="NORDER"),
   Span(doc251, 9, 12, label ="CONTRACT"),
   Span(doc251, 12, 13, label ="CONTRACT1"),
   Span(doc251, 15, 16, label ="POS"),
   Span(doc251, 16, 17, label ="AMOUNT"),
   Span(doc251, 18, 19, label ="ARTICLE"),
   Span(doc251, 19, 20, label ="PRICE"),
   Span(doc251, 20, 21, label ="UNIT"),
   Span(doc251, 22, 23, label ="SUMMA"),
   Span(doc251, 41, 42, label ="TARIFF"),
   Span(doc251, 46, 47, label ="COUNTRY"),
   Span(doc251, 49, 50, label ="PR_SURCH"),
   Span(doc251, 51, 52, label ="SURCHARGE"),
   Span(doc251, 54, 55, label ="PR_ESURCH"),
   Span(doc251, 56, 57, label ="ESURCHARGE"),
   Span(doc251, 58, 59, label ="TOTAL")]
docs.append(doc251)
print("doc252, 58, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 35700; AMOUNT 100; ARTICLE 6100196640; PRICE 32,75; UNIT 100; SUMMA 32,75; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 3,73; PR_ESURCH 3,50; ESURCHARGE 1,15; TOTAL 37,63; ")
doc252 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 35700 100 PC 6100196640 32,75 100 PC 32,75 LBBU-219-SA-M8/U5/16/2 packed per each item Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 3,73 Energy Surcharge 3,50 % 1,15 37,63''')
doc252.ents = [
   Span(doc252, 3, 4, label ="NORDER"),
   Span(doc252, 9, 12, label ="CONTRACT"),
   Span(doc252, 12, 13, label ="CONTRACT1"),
   Span(doc252, 15, 16, label ="POS"),
   Span(doc252, 16, 17, label ="AMOUNT"),
   Span(doc252, 18, 19, label ="ARTICLE"),
   Span(doc252, 19, 20, label ="PRICE"),
   Span(doc252, 20, 21, label ="UNIT"),
   Span(doc252, 22, 23, label ="SUMMA"),
   Span(doc252, 41, 42, label ="TARIFF"),
   Span(doc252, 46, 47, label ="COUNTRY"),
   Span(doc252, 49, 50, label ="PR_SURCH"),
   Span(doc252, 51, 52, label ="SURCHARGE"),
   Span(doc252, 54, 55, label ="PR_ESURCH"),
   Span(doc252, 56, 57, label ="ESURCHARGE"),
   Span(doc252, 57, 58, label ="TOTAL")]
docs.append(doc252)
print("doc253, 63, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 35800; AMOUNT 50; ARTICLE 1130005409; PRICE 46,81; UNIT 100; SUMMA 23,41; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 2,67; PR_ESURCH 3,50; ESURCHARGE 0,82; TOTAL 26,90; ")
doc253 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 35800 50 PC 1130005409 46,81 100 PC 23,41 218/18-PA-H 218/18 PAH packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 2,67 Energy Surcharge 3,50 % 0,82 26,90''')
doc253.ents = [
   Span(doc253, 3, 4, label ="NORDER"),
   Span(doc253, 9, 12, label ="CONTRACT"),
   Span(doc253, 12, 13, label ="CONTRACT1"),
   Span(doc253, 15, 16, label ="POS"),
   Span(doc253, 16, 17, label ="AMOUNT"),
   Span(doc253, 18, 19, label ="ARTICLE"),
   Span(doc253, 19, 20, label ="PRICE"),
   Span(doc253, 20, 21, label ="UNIT"),
   Span(doc253, 22, 23, label ="SUMMA"),
   Span(doc253, 46, 47, label ="TARIFF"),
   Span(doc253, 51, 52, label ="COUNTRY"),
   Span(doc253, 54, 55, label ="PR_SURCH"),
   Span(doc253, 56, 57, label ="SURCHARGE"),
   Span(doc253, 59, 60, label ="PR_ESURCH"),
   Span(doc253, 61, 62, label ="ESURCHARGE"),
   Span(doc253, 62, 63, label ="TOTAL")]
docs.append(doc253)
print("doc254, 64, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 35900; AMOUNT 25; ARTICLE 1130005384; PRICE 32,76; UNIT 100; SUMMA 8,19; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,93; PR_ESURCH 3,50; ESURCHARGE 0,29; TOTAL 9,41; ")
doc254 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 35900 25 PC 1130005384 32,76 100 PC 8,19 218-PA-H 218 PAH packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 0,93   Energy Surcharge 3,50 % 0,29 9,41''')
doc254.ents = [
   Span(doc254, 3, 4, label ="NORDER"),
   Span(doc254, 9, 12, label ="CONTRACT"),
   Span(doc254, 12, 13, label ="CONTRACT1"),
   Span(doc254, 15, 16, label ="POS"),
   Span(doc254, 16, 17, label ="AMOUNT"),
   Span(doc254, 18, 19, label ="ARTICLE"),
   Span(doc254, 19, 20, label ="PRICE"),
   Span(doc254, 20, 21, label ="UNIT"),
   Span(doc254, 22, 23, label ="SUMMA"),
   Span(doc254, 46, 47, label ="TARIFF"),
   Span(doc254, 51, 52, label ="COUNTRY"),
   Span(doc254, 54, 55, label ="PR_SURCH"),
   Span(doc254, 56, 57, label ="SURCHARGE"),
   Span(doc254, 60, 61, label ="PR_ESURCH"),
   Span(doc254, 62, 63, label ="ESURCHARGE"),
   Span(doc254, 63, 64, label ="TOTAL")]
docs.append(doc254)
print("doc255, 63, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 36000; AMOUNT 50; ARTICLE 1130003214; PRICE 54,78; UNIT 100; SUMMA 27,39; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 3,12; PR_ESURCH 3,50; ESURCHARGE 0,96; TOTAL 31,47; ")
doc255 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 36000 50 PC 1130003214 54,78 100 PC 27,39 322/22-PA-H 322/22 PAH packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 3,12 Energy Surcharge 3,50 % 0,96 31,47''')
doc255.ents = [
   Span(doc255, 3, 4, label ="NORDER"),
   Span(doc255, 9, 12, label ="CONTRACT"),
   Span(doc255, 12, 13, label ="CONTRACT1"),
   Span(doc255, 15, 16, label ="POS"),
   Span(doc255, 16, 17, label ="AMOUNT"),
   Span(doc255, 18, 19, label ="ARTICLE"),
   Span(doc255, 19, 20, label ="PRICE"),
   Span(doc255, 20, 21, label ="UNIT"),
   Span(doc255, 22, 23, label ="SUMMA"),
   Span(doc255, 46, 47, label ="TARIFF"),
   Span(doc255, 51, 52, label ="COUNTRY"),
   Span(doc255, 54, 55, label ="PR_SURCH"),
   Span(doc255, 56, 57, label ="SURCHARGE"),
   Span(doc255, 59, 60, label ="PR_ESURCH"),
   Span(doc255, 61, 62, label ="ESURCHARGE"),
   Span(doc255, 62, 63, label ="TOTAL")]
docs.append(doc255)
print("doc256, 66, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 36100; AMOUNT 50; ARTICLE 1130005582; PRICE 23,90; UNIT 100; SUMMA 11,95; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 1,36; PR_ESURCH 3,50; ESURCHARGE 0,42; TOTAL 13,73; ")
doc256 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 36100 50 PC 1130005582 23,90 100 PC 11,95 322-PP-H-BK 322 PPH black9005 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 1,36 Energy Surcharge 3,50 % 0,42 13,73''')
doc256.ents = [
   Span(doc256, 3, 4, label ="NORDER"),
   Span(doc256, 9, 12, label ="CONTRACT"),
   Span(doc256, 12, 13, label ="CONTRACT1"),
   Span(doc256, 15, 16, label ="POS"),
   Span(doc256, 16, 17, label ="AMOUNT"),
   Span(doc256, 18, 19, label ="ARTICLE"),
   Span(doc256, 19, 20, label ="PRICE"),
   Span(doc256, 20, 21, label ="UNIT"),
   Span(doc256, 22, 23, label ="SUMMA"),
   Span(doc256, 49, 50, label ="TARIFF"),
   Span(doc256, 54, 55, label ="COUNTRY"),
   Span(doc256, 57, 58, label ="PR_SURCH"),
   Span(doc256, 59, 60, label ="SURCHARGE"),
   Span(doc256, 62, 63, label ="PR_ESURCH"),
   Span(doc256, 64, 65, label ="ESURCHARGE"),
   Span(doc256, 65, 66, label ="TOTAL")]
docs.append(doc256)
print("doc257, 64, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 36200; AMOUNT 25; ARTICLE 1130003286; PRICE 50,00; UNIT 100; SUMMA 12,50; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 1,43; PR_ESURCH 3,50; ESURCHARGE 0,44; TOTAL 14,37; ")
doc257 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 36200 25 PC 1130003286 50,00 100 PC 12,50 325-PA-H 325 PAH packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097    Country of origin: Germany Material Surcharge 11,40 % 1,43 Energy Surcharge 3,50 % 0,44 14,37''')
doc257.ents = [
   Span(doc257, 3, 4, label ="NORDER"),
   Span(doc257, 9, 12, label ="CONTRACT"),
   Span(doc257, 12, 13, label ="CONTRACT1"),
   Span(doc257, 15, 16, label ="POS"),
   Span(doc257, 16, 17, label ="AMOUNT"),
   Span(doc257, 18, 19, label ="ARTICLE"),
   Span(doc257, 19, 20, label ="PRICE"),
   Span(doc257, 20, 21, label ="UNIT"),
   Span(doc257, 22, 23, label ="SUMMA"),
   Span(doc257, 46, 47, label ="TARIFF"),
   Span(doc257, 52, 53, label ="COUNTRY"),
   Span(doc257, 55, 56, label ="PR_SURCH"),
   Span(doc257, 57, 58, label ="SURCHARGE"),
   Span(doc257, 60, 61, label ="PR_ESURCH"),
   Span(doc257, 62, 63, label ="ESURCHARGE"),
   Span(doc257, 63, 64, label ="TOTAL")]
docs.append(doc257)
print("doc258, 61, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 36300; AMOUNT 200; ARTICLE 1130005715; PRICE 81,41; UNIT 100; SUMMA 162,82; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 18,56; PR_ESURCH 3,50; ESURCHARGE 5,70; TOTAL 187,08; ")
doc258 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 36300 200 PC 1130005715 81,41 100 PC 162,82 4025-PA 4025 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 18,56 Energy Surcharge 3,50 % 5,70 187,08''')
doc258.ents = [
   Span(doc258, 3, 4, label ="NORDER"),
   Span(doc258, 9, 12, label ="CONTRACT"),
   Span(doc258, 12, 13, label ="CONTRACT1"),
   Span(doc258, 15, 16, label ="POS"),
   Span(doc258, 16, 17, label ="AMOUNT"),
   Span(doc258, 18, 19, label ="ARTICLE"),
   Span(doc258, 19, 20, label ="PRICE"),
   Span(doc258, 20, 21, label ="UNIT"),
   Span(doc258, 22, 23, label ="SUMMA"),
   Span(doc258, 44, 45, label ="TARIFF"),
   Span(doc258, 49, 50, label ="COUNTRY"),
   Span(doc258, 52, 53, label ="PR_SURCH"),
   Span(doc258, 54, 55, label ="SURCHARGE"),
   Span(doc258, 57, 58, label ="PR_ESURCH"),
   Span(doc258, 59, 60, label ="ESURCHARGE"),
   Span(doc258, 60, 61, label ="TOTAL")]
docs.append(doc258)
print("doc259, 66, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 36400; AMOUNT 200; ARTICLE 1130026834; PRICE 40,89; UNIT 100; SUMMA 81,78; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 9,32; PR_ESURCH 3,50; ESURCHARGE 2,86; TOTAL 93,96; ")
doc259 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 36400 200 PC 1130026834 40,89 100 PC 81,78 426.9/26.9-PP-H-BK 426,9/26,9 PPH black9005 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 9,32 Energy Surcharge 3,50 % 2,86 93,96''')
doc259.ents = [
   Span(doc259, 3, 4, label ="NORDER"),
   Span(doc259, 9, 12, label ="CONTRACT"),
   Span(doc259, 12, 13, label ="CONTRACT1"),
   Span(doc259, 15, 16, label ="POS"),
   Span(doc259, 16, 17, label ="AMOUNT"),
   Span(doc259, 18, 19, label ="ARTICLE"),
   Span(doc259, 19, 20, label ="PRICE"),
   Span(doc259, 20, 21, label ="UNIT"),
   Span(doc259, 22, 23, label ="SUMMA"),
   Span(doc259, 49, 50, label ="TARIFF"),
   Span(doc259, 54, 55, label ="COUNTRY"),
   Span(doc259, 57, 58, label ="PR_SURCH"),
   Span(doc259, 59, 60, label ="SURCHARGE"),
   Span(doc259, 62, 63, label ="PR_ESURCH"),
   Span(doc259, 64, 65, label ="ESURCHARGE"),
   Span(doc259, 65, 66, label ="TOTAL")]
docs.append(doc259)
print("doc260, 67, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 36500; AMOUNT 1.400; ARTICLE 1130026758; PRICE 29,27; UNIT 100; SUMMA 409,78; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 46,71; PR_ESURCH 3,50; ESURCHARGE 14,34; TOTAL 470,83; ")
doc260 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 36500 1.400 PC 1130026758 29,27 100 PC 409,78 426.9-PP-H-BK 426,9 PPH black9005    packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 46,71 Energy Surcharge 3,50 % 14,34 470,83''')
doc260.ents = [
   Span(doc260, 3, 4, label ="NORDER"),
   Span(doc260, 9, 12, label ="CONTRACT"),
   Span(doc260, 12, 13, label ="CONTRACT1"),
   Span(doc260, 15, 16, label ="POS"),
   Span(doc260, 16, 17, label ="AMOUNT"),
   Span(doc260, 18, 19, label ="ARTICLE"),
   Span(doc260, 19, 20, label ="PRICE"),
   Span(doc260, 20, 21, label ="UNIT"),
   Span(doc260, 22, 23, label ="SUMMA"),
   Span(doc260, 50, 51, label ="TARIFF"),
   Span(doc260, 55, 56, label ="COUNTRY"),
   Span(doc260, 58, 59, label ="PR_SURCH"),
   Span(doc260, 60, 61, label ="SURCHARGE"),
   Span(doc260, 63, 64, label ="PR_ESURCH"),
   Span(doc260, 65, 66, label ="ESURCHARGE"),
   Span(doc260, 66, 67, label ="TOTAL")]
docs.append(doc260)
print("doc261, 63, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 36600; AMOUNT 200; ARTICLE 1130005809; PRICE 85,31; UNIT 100; SUMMA 170,62; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 19,45; PR_ESURCH 3,50; ESURCHARGE 5,97; TOTAL 196,04; ")
doc261 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 36600 200 PC 1130005809 85,31 100 PC 170,62 428/28-PA-H 428/28 PAH packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 19,45 Energy Surcharge 3,50 % 5,97 196,04''')
doc261.ents = [
   Span(doc261, 3, 4, label ="NORDER"),
   Span(doc261, 9, 12, label ="CONTRACT"),
   Span(doc261, 12, 13, label ="CONTRACT1"),
   Span(doc261, 15, 16, label ="POS"),
   Span(doc261, 16, 17, label ="AMOUNT"),
   Span(doc261, 18, 19, label ="ARTICLE"),
   Span(doc261, 19, 20, label ="PRICE"),
   Span(doc261, 20, 21, label ="UNIT"),
   Span(doc261, 22, 23, label ="SUMMA"),
   Span(doc261, 46, 47, label ="TARIFF"),
   Span(doc261, 51, 52, label ="COUNTRY"),
   Span(doc261, 54, 55, label ="PR_SURCH"),
   Span(doc261, 56, 57, label ="SURCHARGE"),
   Span(doc261, 59, 60, label ="PR_ESURCH"),
   Span(doc261, 61, 62, label ="ESURCHARGE"),
   Span(doc261, 62, 63, label ="TOTAL")]
docs.append(doc261)
print("doc262, 65, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 36700; AMOUNT 50; ARTICLE 1130010963; PRICE 29,27; UNIT 100; SUMMA 14,64; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 1,67; PR_ESURCH 3,50; ESURCHARGE 0,51; TOTAL 16,82; ")
doc262 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 36700 50 PC 1130010963 29,27 100 PC 14,64 428 -PP-H-BK 428 PPH black9005 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 1,67 Energy Surcharge 3,50 % 0,51 16,82''')
doc262.ents = [
   Span(doc262, 3, 4, label ="NORDER"),
   Span(doc262, 9, 12, label ="CONTRACT"),
   Span(doc262, 12, 13, label ="CONTRACT1"),
   Span(doc262, 15, 16, label ="POS"),
   Span(doc262, 16, 17, label ="AMOUNT"),
   Span(doc262, 18, 19, label ="ARTICLE"),
   Span(doc262, 19, 20, label ="PRICE"),
   Span(doc262, 20, 21, label ="UNIT"),
   Span(doc262, 22, 23, label ="SUMMA"),
   Span(doc262, 48, 49, label ="TARIFF"),
   Span(doc262, 53, 54, label ="COUNTRY"),
   Span(doc262, 56, 57, label ="PR_SURCH"),
   Span(doc262, 58, 59, label ="SURCHARGE"),
   Span(doc262, 61, 62, label ="PR_ESURCH"),
   Span(doc262, 63, 64, label ="ESURCHARGE"),
   Span(doc262, 64, 65, label ="TOTAL")]
docs.append(doc262)
print("doc263, 67, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 36800; AMOUNT 100; ARTICLE 1130007768; PRICE 65,63; UNIT 100; SUMMA 65,63; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 7,48; PR_ESURCH 3,50; ESURCHARGE 2,30; TOTAL 75,41; ")
doc263 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27**   36800 100 PC 1130007768 65,63 100 PC 65,63 532/32-PP-H-BK 532/32 PPH black9005 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 7,48 Energy Surcharge 3,50 % 2,30 75,41''')
doc263.ents = [
   Span(doc263, 3, 4, label ="NORDER"),
   Span(doc263, 9, 12, label ="CONTRACT"),
   Span(doc263, 12, 13, label ="CONTRACT1"),
   Span(doc263, 16, 17, label ="POS"),
   Span(doc263, 17, 18, label ="AMOUNT"),
   Span(doc263, 19, 20, label ="ARTICLE"),
   Span(doc263, 20, 21, label ="PRICE"),
   Span(doc263, 21, 22, label ="UNIT"),
   Span(doc263, 23, 24, label ="SUMMA"),
   Span(doc263, 50, 51, label ="TARIFF"),
   Span(doc263, 55, 56, label ="COUNTRY"),
   Span(doc263, 58, 59, label ="PR_SURCH"),
   Span(doc263, 60, 61, label ="SURCHARGE"),
   Span(doc263, 63, 64, label ="PR_ESURCH"),
   Span(doc263, 65, 66, label ="ESURCHARGE"),
   Span(doc263, 66, 67, label ="TOTAL")]
docs.append(doc263)
print("doc264, 66, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 36900; AMOUNT 800; ARTICLE 1130008136; PRICE 63,01; UNIT 100; SUMMA 504,08; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 57,47; PR_ESURCH 3,50; ESURCHARGE 17,64; TOTAL 579,19; ")
doc264 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 36900 800 PC 1130008136 63,01 100 PC 504,08 535/35-PP-H-BK 535/35 PPH black9005 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 57,47 Energy Surcharge 3,50 % 17,64 579,19''')
doc264.ents = [
   Span(doc264, 3, 4, label ="NORDER"),
   Span(doc264, 9, 12, label ="CONTRACT"),
   Span(doc264, 12, 13, label ="CONTRACT1"),
   Span(doc264, 15, 16, label ="POS"),
   Span(doc264, 16, 17, label ="AMOUNT"),
   Span(doc264, 18, 19, label ="ARTICLE"),
   Span(doc264, 19, 20, label ="PRICE"),
   Span(doc264, 20, 21, label ="UNIT"),
   Span(doc264, 22, 23, label ="SUMMA"),
   Span(doc264, 49, 50, label ="TARIFF"),
   Span(doc264, 54, 55, label ="COUNTRY"),
   Span(doc264, 57, 58, label ="PR_SURCH"),
   Span(doc264, 59, 60, label ="SURCHARGE"),
   Span(doc264, 62, 63, label ="PR_ESURCH"),
   Span(doc264, 64, 65, label ="ESURCHARGE"),
   Span(doc264, 65, 66, label ="TOTAL")]
docs.append(doc264)
print("doc265, 66, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 37000; AMOUNT 50; ARTICLE 1130006044; PRICE 84,96; UNIT 100; SUMMA 42,48; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 4,84; PR_ESURCH 3,50; ESURCHARGE 1,49; TOTAL 48,81; ")
doc265 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 37000 50 PC 1130006044 84,96 100 PC 42,48 538/38 -PP-H-BK 538/38 PPH black9005 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 4,84 Energy Surcharge 3,50 % 1,49 48,81   ''')
doc265.ents = [
   Span(doc265, 3, 4, label ="NORDER"),
   Span(doc265, 9, 12, label ="CONTRACT"),
   Span(doc265, 12, 13, label ="CONTRACT1"),
   Span(doc265, 15, 16, label ="POS"),
   Span(doc265, 16, 17, label ="AMOUNT"),
   Span(doc265, 18, 19, label ="ARTICLE"),
   Span(doc265, 19, 20, label ="PRICE"),
   Span(doc265, 20, 21, label ="UNIT"),
   Span(doc265, 22, 23, label ="SUMMA"),
   Span(doc265, 48, 49, label ="TARIFF"),
   Span(doc265, 53, 54, label ="COUNTRY"),
   Span(doc265, 56, 57, label ="PR_SURCH"),
   Span(doc265, 58, 59, label ="SURCHARGE"),
   Span(doc265, 61, 62, label ="PR_ESURCH"),
   Span(doc265, 63, 64, label ="ESURCHARGE"),
   Span(doc265, 64, 65, label ="TOTAL")]
docs.append(doc265)
print("doc266, 63, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 37100; AMOUNT 50; ARTICLE 1130003573; PRICE 136,30; UNIT 100; SUMMA 68,15; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 7,77; PR_ESURCH 3,50; ESURCHARGE 2,39; TOTAL 78,31; ")
doc266 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 37100 50 PC 1130003573 136,30 100 PC 68,15 644.5-PA-H 644,5 PAH packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 7,77 Energy Surcharge 3,50 % 2,39 78,31''')
doc266.ents = [
   Span(doc266, 3, 4, label ="NORDER"),
   Span(doc266, 9, 12, label ="CONTRACT"),
   Span(doc266, 12, 13, label ="CONTRACT1"),
   Span(doc266, 15, 16, label ="POS"),
   Span(doc266, 16, 17, label ="AMOUNT"),
   Span(doc266, 18, 19, label ="ARTICLE"),
   Span(doc266, 19, 20, label ="PRICE"),
   Span(doc266, 20, 21, label ="UNIT"),
   Span(doc266, 22, 23, label ="SUMMA"),
   Span(doc266, 46, 47, label ="TARIFF"),
   Span(doc266, 51, 52, label ="COUNTRY"),
   Span(doc266, 54, 55, label ="PR_SURCH"),
   Span(doc266, 56, 57, label ="SURCHARGE"),
   Span(doc266, 59, 60, label ="PR_ESURCH"),
   Span(doc266, 61, 62, label ="ESURCHARGE"),
   Span(doc266, 62, 63, label ="TOTAL")]
docs.append(doc266)
print("doc267, 63, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 37200; AMOUNT 900; ARTICLE 1130003576; PRICE 183,80; UNIT 100; SUMMA 1.654,20; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 188,58; PR_ESURCH 3,50; ESURCHARGE 57,90; TOTAL 1.900,68; ")
doc267 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 37200 900 PC 1130003576 183,80 100 PC 1.654,20 648.3-PA-H 648,3 PAH packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 188,58 Energy Surcharge 3,50 % 57,90 1.900,68''')
doc267.ents = [
   Span(doc267, 3, 4, label ="NORDER"),
   Span(doc267, 9, 12, label ="CONTRACT"),
   Span(doc267, 12, 13, label ="CONTRACT1"),
   Span(doc267, 15, 16, label ="POS"),
   Span(doc267, 16, 17, label ="AMOUNT"),
   Span(doc267, 18, 19, label ="ARTICLE"),
   Span(doc267, 19, 20, label ="PRICE"),
   Span(doc267, 20, 21, label ="UNIT"),
   Span(doc267, 22, 23, label ="SUMMA"),
   Span(doc267, 46, 47, label ="TARIFF"),
   Span(doc267, 51, 52, label ="COUNTRY"),
   Span(doc267, 54, 55, label ="PR_SURCH"),
   Span(doc267, 56, 57, label ="SURCHARGE"),
   Span(doc267, 59, 60, label ="PR_ESURCH"),
   Span(doc267, 61, 62, label ="ESURCHARGE"),
   Span(doc267, 62, 63, label ="TOTAL")]
docs.append(doc267)
print("doc268, 64, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 37300; AMOUNT 25; ARTICLE 1130003579; PRICE 136,30; UNIT 100; SUMMA 34,08; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 3,89; PR_ESURCH 3,50; ESURCHARGE 1,19; TOTAL 39,16; ")
doc268 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 37300 25 PC 1130003579 136,30 100 PC 34,08 650.8-PA-H 650,8 PAH packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 3,89   Energy Surcharge 3,50 % 1,19 39,16''')
doc268.ents = [
   Span(doc268, 3, 4, label ="NORDER"),
   Span(doc268, 9, 12, label ="CONTRACT"),
   Span(doc268, 12, 13, label ="CONTRACT1"),
   Span(doc268, 15, 16, label ="POS"),
   Span(doc268, 16, 17, label ="AMOUNT"),
   Span(doc268, 18, 19, label ="ARTICLE"),
   Span(doc268, 19, 20, label ="PRICE"),
   Span(doc268, 20, 21, label ="UNIT"),
   Span(doc268, 22, 23, label ="SUMMA"),
   Span(doc268, 46, 47, label ="TARIFF"),
   Span(doc268, 51, 52, label ="COUNTRY"),
   Span(doc268, 54, 55, label ="PR_SURCH"),
   Span(doc268, 56, 57, label ="SURCHARGE"),
   Span(doc268, 60, 61, label ="PR_ESURCH"),
   Span(doc268, 62, 63, label ="ESURCHARGE"),
   Span(doc268, 63, 64, label ="TOTAL")]
docs.append(doc268)
print("doc269, 71, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 37400; AMOUNT 9.375; ARTICLE 1130023498; PRICE 37,84; UNIT 100; SUMMA 3.547; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 404,42; PR_ESURCH 3,50; ESURCHARGE 124,16; TOTAL 4.076,08; ")
doc269 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 37400 9.375 PC 1130023498 37,84 100 PC 3.547 ,50 LBBU-108/08-SA-M8/U5/16 LBBU 108/08 SA M8-U5/16 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 404,42 Energy Surcharge 3,50 % 124,16 4.076,08''')
doc269.ents = [
   Span(doc269, 3, 4, label ="NORDER"),
   Span(doc269, 9, 12, label ="CONTRACT"),
   Span(doc269, 12, 13, label ="CONTRACT1"),
   Span(doc269, 15, 16, label ="POS"),
   Span(doc269, 16, 17, label ="AMOUNT"),
   Span(doc269, 18, 19, label ="ARTICLE"),
   Span(doc269, 19, 20, label ="PRICE"),
   Span(doc269, 20, 21, label ="UNIT"),
   Span(doc269, 22, 23, label ="SUMMA"),
   Span(doc269, 54, 55, label ="TARIFF"),
   Span(doc269, 59, 60, label ="COUNTRY"),
   Span(doc269, 62, 63, label ="PR_SURCH"),
   Span(doc269, 64, 65, label ="SURCHARGE"),
   Span(doc269, 67, 68, label ="PR_ESURCH"),
   Span(doc269, 69, 70, label ="ESURCHARGE"),
   Span(doc269, 70, 71, label ="TOTAL")]
docs.append(doc269)
print("doc270, 69, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 37500; AMOUNT 2.500; ARTICLE 1130023472; PRICE 31,28; UNIT 100; SUMMA 782,00; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 89,15; PR_ESURCH 3,50; ESURCHARGE 27,37; TOTAL 898,52; ")
doc270 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 37500 2.500 PC 1130023472 31,28 100 PC 782,00 LBBU-108-SA-M8/U5/16 LBBU 108 SA M8-U5/16 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 89,15 Energy Surcharge 3,50 % 27,37 898,52''')
doc270.ents = [
   Span(doc270, 3, 4, label ="NORDER"),
   Span(doc270, 9, 12, label ="CONTRACT"),
   Span(doc270, 12, 13, label ="CONTRACT1"),
   Span(doc270, 15, 16, label ="POS"),
   Span(doc270, 16, 17, label ="AMOUNT"),
   Span(doc270, 18, 19, label ="ARTICLE"),
   Span(doc270, 19, 20, label ="PRICE"),
   Span(doc270, 20, 21, label ="UNIT"),
   Span(doc270, 22, 23, label ="SUMMA"),
   Span(doc270, 52, 53, label ="TARIFF"),
   Span(doc270, 57, 58, label ="COUNTRY"),
   Span(doc270, 60, 61, label ="PR_SURCH"),
   Span(doc270, 62, 63, label ="SURCHARGE"),
   Span(doc270, 65, 66, label ="PR_ESURCH"),
   Span(doc270, 67, 68, label ="ESURCHARGE"),
   Span(doc270, 68, 69, label ="TOTAL")]
docs.append(doc270)
print("doc271, 70, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 37600; AMOUNT 200; ARTICLE 1130023477; PRICE 31,28; UNIT 100; SUMMA 62,56; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 7,13; PR_ESURCH 3,50; ESURCHARGE 2,19; TOTAL 71,88; ")
doc271 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 37600 200 PC 1130023477 31,28 100 PC 62,56 LBBU-112.7-SA-M8/U5/16 LBBU 112,7 SA M8-U5/16 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097    Country of origin: Germany Material Surcharge 11,40 % 7,13 Energy Surcharge 3,50 % 2,19 71,88''')
doc271.ents = [
   Span(doc271, 3, 4, label ="NORDER"),
   Span(doc271, 9, 12, label ="CONTRACT"),
   Span(doc271, 12, 13, label ="CONTRACT1"),
   Span(doc271, 15, 16, label ="POS"),
   Span(doc271, 16, 17, label ="AMOUNT"),
   Span(doc271, 18, 19, label ="ARTICLE"),
   Span(doc271, 19, 20, label ="PRICE"),
   Span(doc271, 20, 21, label ="UNIT"),
   Span(doc271, 22, 23, label ="SUMMA"),
   Span(doc271, 52, 53, label ="TARIFF"),
   Span(doc271, 58, 59, label ="COUNTRY"),
   Span(doc271, 61, 62, label ="PR_SURCH"),
   Span(doc271, 63, 64, label ="SURCHARGE"),
   Span(doc271, 66, 67, label ="PR_ESURCH"),
   Span(doc271, 68, 69, label ="ESURCHARGE"),
   Span(doc271, 69, 70, label ="TOTAL")]
docs.append(doc271)
print("doc272, 69, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 37700; AMOUNT 600; ARTICLE 1130029812; PRICE 37,84; UNIT 100; SUMMA 227,04; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 25,88; PR_ESURCH 3,50; ESURCHARGE 7,95; TOTAL 260,87; ")
doc272 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 37700 600 PC 1130029812 37,84 100 PC 227,04 LBBU-11 2/08 -SA-M8/U5/16 LBBU 112/08 SA M8-U5/16 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 25,88 Energy Surcharge 3,50 % 7,95 260,87''')
doc272.ents = [
   Span(doc272, 3, 4, label ="NORDER"),
   Span(doc272, 9, 12, label ="CONTRACT"),
   Span(doc272, 12, 13, label ="CONTRACT1"),
   Span(doc272, 15, 16, label ="POS"),
   Span(doc272, 16, 17, label ="AMOUNT"),
   Span(doc272, 18, 19, label ="ARTICLE"),
   Span(doc272, 19, 20, label ="PRICE"),
   Span(doc272, 20, 21, label ="UNIT"),
   Span(doc272, 22, 23, label ="SUMMA"),
   Span(doc272, 52, 53, label ="TARIFF"),
   Span(doc272, 57, 58, label ="COUNTRY"),
   Span(doc272, 60, 61, label ="PR_SURCH"),
   Span(doc272, 62, 63, label ="SURCHARGE"),
   Span(doc272, 65, 66, label ="PR_ESURCH"),
   Span(doc272, 67, 68, label ="ESURCHARGE"),
   Span(doc272, 68, 69, label ="TOTAL")]
docs.append(doc272)
print("doc273, 69, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 37800; AMOUNT 2.300; ARTICLE 1130022741; PRICE 37,84; UNIT 100; SUMMA 870,32; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 99,22; PR_ESURCH 3,50; ESURCHARGE 30,46; TOTAL 1.000,00; ")
doc273 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 37800 2.300 PC 1130022741 37,84 100 PC 870,32 LBBU-112/12-SA-M8/U5/16 LBBU 112/12 SA M8-U5/16 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 99,22 Energy Surcharge 3,50 % 30,46 1.000,00''')
doc273.ents = [
   Span(doc273, 3, 4, label ="NORDER"),
   Span(doc273, 9, 12, label ="CONTRACT"),
   Span(doc273, 12, 13, label ="CONTRACT1"),
   Span(doc273, 15, 16, label ="POS"),
   Span(doc273, 16, 17, label ="AMOUNT"),
   Span(doc273, 18, 19, label ="ARTICLE"),
   Span(doc273, 19, 20, label ="PRICE"),
   Span(doc273, 20, 21, label ="UNIT"),
   Span(doc273, 22, 23, label ="SUMMA"),
   Span(doc273, 52, 53, label ="TARIFF"),
   Span(doc273, 57, 58, label ="COUNTRY"),
   Span(doc273, 60, 61, label ="PR_SURCH"),
   Span(doc273, 62, 63, label ="SURCHARGE"),
   Span(doc273, 65, 66, label ="PR_ESURCH"),
   Span(doc273, 67, 68, label ="ESURCHARGE"),
   Span(doc273, 68, 69, label ="TOTAL")]
docs.append(doc273)
print("doc274, 70, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 37900; AMOUNT 700; ARTICLE 1130023476; PRICE 31,28; UNIT 100; SUMMA 218,96; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 24,96; PR_ESURCH 3,50; ESURCHARGE 7,66; TOTAL 251,58; ")
doc274 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 37900 700 PC 1130023476 31,28 100 PC 218,96 LBBU-112-SA-M8/U5/16 LBBU 112 SA M8-U5/16    packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 24,96 Energy Surcharge 3,50 % 7,66 251,58''')
doc274.ents = [
   Span(doc274, 3, 4, label ="NORDER"),
   Span(doc274, 9, 12, label ="CONTRACT"),
   Span(doc274, 12, 13, label ="CONTRACT1"),
   Span(doc274, 15, 16, label ="POS"),
   Span(doc274, 16, 17, label ="AMOUNT"),
   Span(doc274, 18, 19, label ="ARTICLE"),
   Span(doc274, 19, 20, label ="PRICE"),
   Span(doc274, 20, 21, label ="UNIT"),
   Span(doc274, 22, 23, label ="SUMMA"),
   Span(doc274, 53, 54, label ="TARIFF"),
   Span(doc274, 58, 59, label ="COUNTRY"),
   Span(doc274, 61, 62, label ="PR_SURCH"),
   Span(doc274, 63, 64, label ="SURCHARGE"),
   Span(doc274, 66, 67, label ="PR_ESURCH"),
   Span(doc274, 68, 69, label ="ESURCHARGE"),
   Span(doc274, 69, 70, label ="TOTAL")]
docs.append(doc274)
print("doc275, 69, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 38000; AMOUNT 400; ARTICLE 1130025898; PRICE 70,37; UNIT 100; SUMMA 281,48; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 32,09; PR_ESURCH 3,50; ESURCHARGE 9,85; TOTAL 323,42; ")
doc275 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 38000 400 PC 1130025898 70,37 100 PC 281,48 LBBU-322-SA-M8/U5/16 LBBU 322 SA M8-U5/16 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 32,09 Energy Surcharge 3,50 % 9,85 323,42''')
doc275.ents = [
   Span(doc275, 3, 4, label ="NORDER"),
   Span(doc275, 9, 12, label ="CONTRACT"),
   Span(doc275, 12, 13, label ="CONTRACT1"),
   Span(doc275, 15, 16, label ="POS"),
   Span(doc275, 16, 17, label ="AMOUNT"),
   Span(doc275, 18, 19, label ="ARTICLE"),
   Span(doc275, 19, 20, label ="PRICE"),
   Span(doc275, 20, 21, label ="UNIT"),
   Span(doc275, 22, 23, label ="SUMMA"),
   Span(doc275, 52, 53, label ="TARIFF"),
   Span(doc275, 57, 58, label ="COUNTRY"),
   Span(doc275, 60, 61, label ="PR_SURCH"),
   Span(doc275, 62, 63, label ="SURCHARGE"),
   Span(doc275, 65, 66, label ="PR_ESURCH"),
   Span(doc275, 67, 68, label ="ESURCHARGE"),
   Span(doc275, 68, 69, label ="TOTAL")]
docs.append(doc275)
print("doc276, 69, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 38100; AMOUNT 100; ARTICLE 1130024637; PRICE 94,23; UNIT 100; SUMMA 94,23; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 10,74; PR_ESURCH 3,50; ESURCHARGE 3,30; TOTAL 108,27; ")
doc276 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 38100 100 PC 1130024637 94,23 100 PC 94,23 LBBU-328/28-SA-M8/U5/16 LBBU 328/28 SA M8-U5/16 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 10,74 Energy Surcharge 3,50 % 3,30 108,27''')
doc276.ents = [
   Span(doc276, 3, 4, label ="NORDER"),
   Span(doc276, 9, 12, label ="CONTRACT"),
   Span(doc276, 12, 13, label ="CONTRACT1"),
   Span(doc276, 15, 16, label ="POS"),
   Span(doc276, 16, 17, label ="AMOUNT"),
   Span(doc276, 18, 19, label ="ARTICLE"),
   Span(doc276, 19, 20, label ="PRICE"),
   Span(doc276, 20, 21, label ="UNIT"),
   Span(doc276, 22, 23, label ="SUMMA"),
   Span(doc276, 52, 53, label ="TARIFF"),
   Span(doc276, 57, 58, label ="COUNTRY"),
   Span(doc276, 60, 61, label ="PR_SURCH"),
   Span(doc276, 62, 63, label ="SURCHARGE"),
   Span(doc276, 65, 66, label ="PR_ESURCH"),
   Span(doc276, 67, 68, label ="ESURCHARGE"),
   Span(doc276, 68, 69, label ="TOTAL")]
docs.append(doc276)
print("doc277, 69, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 38200; AMOUNT 100; ARTICLE 1130025900; PRICE 70,37; UNIT 100; SUMMA 70,37; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 8,02; PR_ESURCH 3,50; ESURCHARGE 2,46; TOTAL 80,85; ")
doc277 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27**   38200 100 PC 1130025900 70,37 100 PC 70,37 LBBU-328 -SA-M8/U5/16 LBBU 328 SA M8-U5/16 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 8,02 Energy Surcharge 3,50 % 2,46 80,85''')
doc277.ents = [
   Span(doc277, 3, 4, label ="NORDER"),
   Span(doc277, 9, 12, label ="CONTRACT"),
   Span(doc277, 12, 13, label ="CONTRACT1"),
   Span(doc277, 16, 17, label ="POS"),
   Span(doc277, 17, 18, label ="AMOUNT"),
   Span(doc277, 19, 20, label ="ARTICLE"),
   Span(doc277, 20, 21, label ="PRICE"),
   Span(doc277, 21, 22, label ="UNIT"),
   Span(doc277, 23, 24, label ="SUMMA"),
   Span(doc277, 52, 53, label ="TARIFF"),
   Span(doc277, 57, 58, label ="COUNTRY"),
   Span(doc277, 60, 61, label ="PR_SURCH"),
   Span(doc277, 62, 63, label ="SURCHARGE"),
   Span(doc277, 65, 66, label ="PR_ESURCH"),
   Span(doc277, 67, 68, label ="ESURCHARGE"),
   Span(doc277, 68, 69, label ="TOTAL")]
docs.append(doc277)
print("doc278, 62, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 38300; AMOUNT 900; ARTICLE 1130017263; PRICE 16,16; UNIT 100; SUMMA 145,44; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 16,58; PR_ESURCH 3,50; ESURCHARGE 5,09; TOTAL 167,11; ")
doc278 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 38300 900 PC 1130017263 16,16 100 PC 145,44 LNGF-212.7/12.7-PA LNGF 212,7/12,7 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 16,58 Energy Surcharge 3,50 % 5,09 167,11''')
doc278.ents = [
   Span(doc278, 3, 4, label ="NORDER"),
   Span(doc278, 9, 12, label ="CONTRACT"),
   Span(doc278, 12, 13, label ="CONTRACT1"),
   Span(doc278, 15, 16, label ="POS"),
   Span(doc278, 16, 17, label ="AMOUNT"),
   Span(doc278, 18, 19, label ="ARTICLE"),
   Span(doc278, 19, 20, label ="PRICE"),
   Span(doc278, 20, 21, label ="UNIT"),
   Span(doc278, 22, 23, label ="SUMMA"),
   Span(doc278, 45, 46, label ="TARIFF"),
   Span(doc278, 50, 51, label ="COUNTRY"),
   Span(doc278, 53, 54, label ="PR_SURCH"),
   Span(doc278, 55, 56, label ="SURCHARGE"),
   Span(doc278, 58, 59, label ="PR_ESURCH"),
   Span(doc278, 60, 61, label ="ESURCHARGE"),
   Span(doc278, 61, 62, label ="TOTAL")]
docs.append(doc278)
print("doc279, 63, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 38400; AMOUNT 25; ARTICLE 1130017266; PRICE 25,15; UNIT 100; SUMMA 6,29; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,72; PR_ESURCH 3,50; ESURCHARGE 0,22; TOTAL 7,23; ")
doc279 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 38400 25 PC 1130017266 25,15 100 PC 6,29 LNGF-312/12-PA LNGF 312/12 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 0,72 Energy Surcharge 3,50 % 0,22 7,23   ''')
doc279.ents = [
   Span(doc279, 3, 4, label ="NORDER"),
   Span(doc279, 9, 12, label ="CONTRACT"),
   Span(doc279, 12, 13, label ="CONTRACT1"),
   Span(doc279, 15, 16, label ="POS"),
   Span(doc279, 16, 17, label ="AMOUNT"),
   Span(doc279, 18, 19, label ="ARTICLE"),
   Span(doc279, 19, 20, label ="PRICE"),
   Span(doc279, 20, 21, label ="UNIT"),
   Span(doc279, 22, 23, label ="SUMMA"),
   Span(doc279, 45, 46, label ="TARIFF"),
   Span(doc279, 50, 51, label ="COUNTRY"),
   Span(doc279, 53, 54, label ="PR_SURCH"),
   Span(doc279, 55, 56, label ="SURCHARGE"),
   Span(doc279, 58, 59, label ="PR_ESURCH"),
   Span(doc279, 60, 61, label ="ESURCHARGE"),
   Span(doc279, 61, 62, label ="TOTAL")]
docs.append(doc279)
print("doc280, 65, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 38500; AMOUNT 200; ARTICLE 1130029312; PRICE 10,84; UNIT 100; SUMMA 21,68; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 2,47; PR_ESURCH 3,50; ESURCHARGE 0,76; TOTAL 24,91; ")
doc280 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 38500 200 PC 1130029312 10,84 100 PC 21,68 LNUF-212/08-PP-BK LNUF 212/08 PP black9005 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 2,47 Energy Surcharge 3,50 % 0,76 24,91''')
doc280.ents = [
   Span(doc280, 3, 4, label ="NORDER"),
   Span(doc280, 9, 12, label ="CONTRACT"),
   Span(doc280, 12, 13, label ="CONTRACT1"),
   Span(doc280, 15, 16, label ="POS"),
   Span(doc280, 16, 17, label ="AMOUNT"),
   Span(doc280, 18, 19, label ="ARTICLE"),
   Span(doc280, 19, 20, label ="PRICE"),
   Span(doc280, 20, 21, label ="UNIT"),
   Span(doc280, 22, 23, label ="SUMMA"),
   Span(doc280, 48, 49, label ="TARIFF"),
   Span(doc280, 53, 54, label ="COUNTRY"),
   Span(doc280, 56, 57, label ="PR_SURCH"),
   Span(doc280, 58, 59, label ="SURCHARGE"),
   Span(doc280, 61, 62, label ="PR_ESURCH"),
   Span(doc280, 63, 64, label ="ESURCHARGE"),
   Span(doc280, 64, 65, label ="TOTAL")]
docs.append(doc280)
print("doc281, 62, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 38600; AMOUNT 100; ARTICLE 1130017319; PRICE 20,78; UNIT 100; SUMMA 20,78; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 2,37; PR_ESURCH 3,50; ESURCHARGE 0,73; TOTAL 23,88; ")
doc281 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 38600 100 PC 1130017319 20,78 100 PC 20,78 LNUF-315/12-PA LNUF 315/12 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 2,37 Energy Surcharge 3,50 % 0,73 23,88''')
doc281.ents = [
   Span(doc281, 3, 4, label ="NORDER"),
   Span(doc281, 9, 12, label ="CONTRACT"),
   Span(doc281, 12, 13, label ="CONTRACT1"),
   Span(doc281, 15, 16, label ="POS"),
   Span(doc281, 16, 17, label ="AMOUNT"),
   Span(doc281, 18, 19, label ="ARTICLE"),
   Span(doc281, 19, 20, label ="PRICE"),
   Span(doc281, 20, 21, label ="UNIT"),
   Span(doc281, 22, 23, label ="SUMMA"),
   Span(doc281, 45, 46, label ="TARIFF"),
   Span(doc281, 50, 51, label ="COUNTRY"),
   Span(doc281, 53, 54, label ="PR_SURCH"),
   Span(doc281, 55, 56, label ="SURCHARGE"),
   Span(doc281, 58, 59, label ="PR_ESURCH"),
   Span(doc281, 60, 61, label ="ESURCHARGE"),
   Span(doc281, 61, 62, label ="TOTAL")]
docs.append(doc281)
print("doc282, 63, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 38700; AMOUNT 50; ARTICLE 1130025844; PRICE 51,73; UNIT 100; SUMMA 25,87; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 2,95; PR_ESURCH 3,50; ESURCHARGE 0,91; TOTAL 29,73; ")
doc282 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 38700 50 PC 1130025844 51,73 100 PC 25,87 LNUF-421.3/18-PA LNUF 421,3/18 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 2,95  Energy Surcharge 3,50 % 0,91 29,73''')
doc282.ents = [
   Span(doc282, 3, 4, label ="NORDER"),
   Span(doc282, 9, 12, label ="CONTRACT"),
   Span(doc282, 12, 13, label ="CONTRACT1"),
   Span(doc282, 15, 16, label ="POS"),
   Span(doc282, 16, 17, label ="AMOUNT"),
   Span(doc282, 18, 19, label ="ARTICLE"),
   Span(doc282, 19, 20, label ="PRICE"),
   Span(doc282, 20, 21, label ="UNIT"),
   Span(doc282, 22, 23, label ="SUMMA"),
   Span(doc282, 45, 46, label ="TARIFF"),
   Span(doc282, 50, 51, label ="COUNTRY"),
   Span(doc282, 53, 54, label ="PR_SURCH"),
   Span(doc282, 55, 56, label ="SURCHARGE"),
   Span(doc282, 59, 60, label ="PR_ESURCH"),
   Span(doc282, 61, 62, label ="ESURCHARGE"),
   Span(doc282, 62, 63, label ="TOTAL")]
docs.append(doc282)
print("doc283, 65, #NORDER 2399874; CONTRACT SR-1-06; CONTRACT1 27; POS 38800; AMOUNT 250; ARTICLE 1130029278; PRICE 18,27; UNIT 100; SUMMA 45,68; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 5,21; PR_ESURCH 3,50; ESURCHARGE 1,60; TOTAL 52,49; ")
doc283 = nlp('''Order number: 2399874 Purchase order number: N SR-1-06 27** 38800 250 PC 1130029278 18,27 100 PC 45,68 LNUF-422/15-PP-BK LNUF 422/15 PP black9005 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 5,21 Energy Surcharge 3,50 % 1,60 52,49''')
doc283.ents = [
   Span(doc283, 3, 4, label ="NORDER"),
   Span(doc283, 9, 12, label ="CONTRACT"),
   Span(doc283, 12, 13, label ="CONTRACT1"),
   Span(doc283, 15, 16, label ="POS"),
   Span(doc283, 16, 17, label ="AMOUNT"),
   Span(doc283, 18, 19, label ="ARTICLE"),
   Span(doc283, 19, 20, label ="PRICE"),
   Span(doc283, 20, 21, label ="UNIT"),
   Span(doc283, 22, 23, label ="SUMMA"),
   Span(doc283, 48, 49, label ="TARIFF"),
   Span(doc283, 53, 54, label ="COUNTRY"),
   Span(doc283, 56, 57, label ="PR_SURCH"),
   Span(doc283, 58, 59, label ="SURCHARGE"),
   Span(doc283, 61, 62, label ="PR_ESURCH"),
   Span(doc283, 63, 64, label ="ESURCHARGE"),
   Span(doc283, 64, 65, label ="TOTAL")]
docs.append(doc283)
doc_bin = DocBin(docs = docs)
doc_bin.to_disk('./train1.spacy')