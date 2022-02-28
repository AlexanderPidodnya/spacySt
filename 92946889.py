import json 
import spacy 
from spacy.matcher import Matcher 
from spacy.tokens import Span, DocBin 
import random
nlp = spacy.blank("en")

docs = []
print("doc0, 72, #NORDER 2332617; CONTRACT SR-1-06; CONTRACT1 1231; POS 2000; AMOUNT 2; ARTICLE 6010003898; PRICE 102,90; UNIT 100; SUMMA 2,06; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 0,14; TOTAL 2,20; ")
doc0 = nlp('''Order number: 2332617 Purchase order number: N SR-1-06 1231 2000 2 PC 6010003898 (* ) 102,90 100 PC 2,06 FI-REDSD-1 0/08L-V-W3-DKO FI-REDSD-1 0/08L-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 0,14    2,20''')
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
   Span(doc0, 71, 72, label ="TOTAL")]
docs.append(doc0)
print("doc1, 70, #NORDER 2356615; CONTRACT SR-1-06; CONTRACT1 1526; POS 2100; AMOUNT 4; ARTICLE 1910000214; PRICE 80,49; UNIT 1; SUMMA 321,96; TARIFF 84812010; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 36,70; TOTAL 358,66; ")
doc1 = nlp('''Order number: 2356615 Purchase order number: N SR-1-06 1526 2100 4 PC 1910000214 80,49 1 PC 321,96 DV-25-B-G DV-25-P-B Throttle valve (in-line mounting) packed per each item Product description: valve Export - Customs tariff no.: 84812010 Country of origin: Germany Material Surcharge 11,40 % 36,70 358,66 EAC - Eurasian Conformity''')
doc1.ents = [
   Span(doc1, 3, 4, label ="NORDER"),
   Span(doc1, 9, 12, label ="CONTRACT"),
   Span(doc1, 12, 13, label ="CONTRACT1"),
   Span(doc1, 13, 14, label ="POS"),
   Span(doc1, 14, 15, label ="AMOUNT"),
   Span(doc1, 16, 17, label ="ARTICLE"),
   Span(doc1, 17, 18, label ="PRICE"),
   Span(doc1, 18, 19, label ="UNIT"),
   Span(doc1, 20, 21, label ="SUMMA"),
   Span(doc1, 54, 55, label ="TARIFF"),
   Span(doc1, 59, 60, label ="COUNTRY"),
   Span(doc1, 62, 63, label ="PR_SURCH"),
   Span(doc1, 64, 65, label ="SURCHARGE"),
   Span(doc1, 65, 66, label ="TOTAL")]
docs.append(doc1)
print("doc2, 58, #NORDER 2376447; CONTRACT SR-1-06; CONTRACT1 1725; POS 2200; AMOUNT 200; ARTICLE 1120002537; PRICE 38,09; UNIT 100; SUMMA 76,18; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 8,68; TOTAL 84,86; ")
doc2 = nlp('''Order number: 2376447 Purchase order number: N SR-1-06 1725 2200 200 PC 1120002537 38,09 100 PC 76,18 SP-2D-M-W2 SP 2 DM W2 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 8,68 84,86''')
doc2.ents = [
   Span(doc2, 3, 4, label ="NORDER"),
   Span(doc2, 9, 12, label ="CONTRACT"),
   Span(doc2, 12, 13, label ="CONTRACT1"),
   Span(doc2, 13, 14, label ="POS"),
   Span(doc2, 14, 15, label ="AMOUNT"),
   Span(doc2, 16, 17, label ="ARTICLE"),
   Span(doc2, 17, 18, label ="PRICE"),
   Span(doc2, 18, 19, label ="UNIT"),
   Span(doc2, 20, 21, label ="SUMMA"),
   Span(doc2, 46, 47, label ="TARIFF"),
   Span(doc2, 51, 52, label ="COUNTRY"),
   Span(doc2, 54, 55, label ="PR_SURCH"),
   Span(doc2, 56, 57, label ="SURCHARGE"),
   Span(doc2, 57, 58, label ="TOTAL")]
docs.append(doc2)
print("doc3, 59, #NORDER 2377510; CONTRACT SR-1-06; CONTRACT1 1767; POS 2300; AMOUNT 300; ARTICLE 1120001188; PRICE 31,83; UNIT 100; SUMMA 95,49; TARIFF 73269098; COUNTRY Germany   ; PR_SURCH 11,40; SURCHARGE 10,89; TOTAL 106,38; ")
doc3 = nlp('''Order number: 2377510 Purchase order number: N SR-1-06 1767 2300 300 PC 1120001188 31,83 100 PC 95,49 SP-3-M-W3 SP 3 M W3 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany   Material Surcharge 11,40 % 10,89 106,38''')
doc3.ents = [
   Span(doc3, 3, 4, label ="NORDER"),
   Span(doc3, 9, 12, label ="CONTRACT"),
   Span(doc3, 12, 13, label ="CONTRACT1"),
   Span(doc3, 13, 14, label ="POS"),
   Span(doc3, 14, 15, label ="AMOUNT"),
   Span(doc3, 16, 17, label ="ARTICLE"),
   Span(doc3, 17, 18, label ="PRICE"),
   Span(doc3, 18, 19, label ="UNIT"),
   Span(doc3, 20, 21, label ="SUMMA"),
   Span(doc3, 46, 47, label ="TARIFF"),
   Span(doc3, 51, 53, label ="COUNTRY"),
   Span(doc3, 55, 56, label ="PR_SURCH"),
   Span(doc3, 57, 58, label ="SURCHARGE"),
   Span(doc3, 58, 59, label ="TOTAL")]
docs.append(doc3)
print("doc4, 58, #NORDER 2378632; CONTRACT SR-1-06; CONTRACT1 1772; POS 2400; AMOUNT 25; ARTICLE 1120002537; PRICE 38,09; UNIT 100; SUMMA 9,52; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 1,09; TOTAL 10,61; ")
doc4 = nlp('''Order number: 2378632 Purchase order number: N SR-1-06 1772 2400 25 PC 1120002537 38,09 100 PC 9,52 SP-2D-M-W2 SP 2 DM W2 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 1,09 10,61''')
doc4.ents = [
   Span(doc4, 3, 4, label ="NORDER"),
   Span(doc4, 9, 12, label ="CONTRACT"),
   Span(doc4, 12, 13, label ="CONTRACT1"),
   Span(doc4, 13, 14, label ="POS"),
   Span(doc4, 14, 15, label ="AMOUNT"),
   Span(doc4, 16, 17, label ="ARTICLE"),
   Span(doc4, 17, 18, label ="PRICE"),
   Span(doc4, 18, 19, label ="UNIT"),
   Span(doc4, 20, 21, label ="SUMMA"),
   Span(doc4, 46, 47, label ="TARIFF"),
   Span(doc4, 51, 52, label ="COUNTRY"),
   Span(doc4, 54, 55, label ="PR_SURCH"),
   Span(doc4, 56, 57, label ="SURCHARGE"),
   Span(doc4, 57, 58, label ="TOTAL")]
docs.append(doc4)
print("doc5, 61, #NORDER 2380831; CONTRACT SR-1-06; CONTRACT1 1808; POS 2500; AMOUNT 150; ARTICLE 1020023990; PRICE 42,38; UNIT 1; SUMMA 6.357; TARIFF 84219990; COUNTRY Germany; PR_SURCH 8,90; SURCHARGE 565,77; TOTAL 6.922,77; ")
doc5 = nlp('''Order number: 2380831 Purchase order number: N SR-1-06 1808 2500 150 PC 1020023990 42,38 1 PC 6.357 ,00 SN-045-E-20-B/4 SN-045E20B/4 packed per each item Product description: filter element Export - Customs tariff no.: 84219990 Country of origin: Germany Material Surcharge 8,90 % 565,77 6.922,77 EAC - Eurasian Conformity''')
doc5.ents = [
   Span(doc5, 3, 4, label ="NORDER"),
   Span(doc5, 9, 12, label ="CONTRACT"),
   Span(doc5, 12, 13, label ="CONTRACT1"),
   Span(doc5, 13, 14, label ="POS"),
   Span(doc5, 14, 15, label ="AMOUNT"),
   Span(doc5, 16, 17, label ="ARTICLE"),
   Span(doc5, 17, 18, label ="PRICE"),
   Span(doc5, 18, 19, label ="UNIT"),
   Span(doc5, 20, 21, label ="SUMMA"),
   Span(doc5, 45, 46, label ="TARIFF"),
   Span(doc5, 50, 51, label ="COUNTRY"),
   Span(doc5, 53, 54, label ="PR_SURCH"),
   Span(doc5, 55, 56, label ="SURCHARGE"),
   Span(doc5, 56, 57, label ="TOTAL")]
docs.append(doc5)
print("doc6, 54, #NORDER 2382763; CONTRACT SR-1-06; CONTRACT1 1824; POS 2600; AMOUNT 1.500; ARTICLE 6030003815; PRICE 24,92; UNIT 100; SUMMA 373,80; TARIFF 73079910; COUNTRY Germany   ; PR_SURCH 6,90; SURCHARGE 25,79; TOTAL 399,59; ")
doc6 = nlp('''Order number: 2382763 Purchase order number: N SR-1-06 1824 2600 1.500 PC 6030003815 24,92 100 PC 373,80 FI-M-15L-W3 packed per each item Product description: nuts Export - Customs tariff no.: 73079910 Country of origin: Germany   Material Surcharge 6,90 % 25,79 399,59''')
doc6.ents = [
   Span(doc6, 3, 4, label ="NORDER"),
   Span(doc6, 9, 12, label ="CONTRACT"),
   Span(doc6, 12, 13, label ="CONTRACT1"),
   Span(doc6, 13, 14, label ="POS"),
   Span(doc6, 14, 15, label ="AMOUNT"),
   Span(doc6, 16, 17, label ="ARTICLE"),
   Span(doc6, 17, 18, label ="PRICE"),
   Span(doc6, 18, 19, label ="UNIT"),
   Span(doc6, 20, 21, label ="SUMMA"),
   Span(doc6, 41, 42, label ="TARIFF"),
   Span(doc6, 46, 48, label ="COUNTRY"),
   Span(doc6, 50, 51, label ="PR_SURCH"),
   Span(doc6, 52, 53, label ="SURCHARGE"),
   Span(doc6, 53, 54, label ="TOTAL")]
docs.append(doc6)
print("doc7, 53, #NORDER 2384639; CONTRACT SR-1-06; CONTRACT1 1828; POS 2700; AMOUNT 3.000; ARTICLE 6030003815; PRICE 24,92; UNIT 100; SUMMA 747,60; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 51,58; TOTAL 799,18; ")
doc7 = nlp('''Order number: 2384639 Purchase order number: N SR-1-06 1828 2700 3.000 PC 6030003815 24,92 100 PC 747,60 FI-M-15L-W3 packed per each item Product description: nuts Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 51,58 799,18''')
doc7.ents = [
   Span(doc7, 3, 4, label ="NORDER"),
   Span(doc7, 9, 12, label ="CONTRACT"),
   Span(doc7, 12, 13, label ="CONTRACT1"),
   Span(doc7, 13, 14, label ="POS"),
   Span(doc7, 14, 15, label ="AMOUNT"),
   Span(doc7, 16, 17, label ="ARTICLE"),
   Span(doc7, 17, 18, label ="PRICE"),
   Span(doc7, 18, 19, label ="UNIT"),
   Span(doc7, 20, 21, label ="SUMMA"),
   Span(doc7, 41, 42, label ="TARIFF"),
   Span(doc7, 46, 47, label ="COUNTRY"),
   Span(doc7, 49, 50, label ="PR_SURCH"),
   Span(doc7, 51, 52, label ="SURCHARGE"),
   Span(doc7, 52, 53, label ="TOTAL")]
docs.append(doc7)
print("doc8, 78, #NORDER 2384650; CONTRACT SR-1-06; CONTRACT1 1843; POS 2800; AMOUNT 6; ARTICLE 6100031624; PRICE 169,97; UNIT 1; SUMMA 1.019,82; TARIFF 84219990; COUNTRY Czech Republic; PR_SURCH 8,90; SURCHARGE 90,76; TOTAL 1.110,58; ")
doc8 = nlp('''Order number: 2384650 Purchase order number: N SR-1-06 1843 2800 6 PC 6100031624 169,97 1 PC 1.019,82 SP-204-E-06-V/4 SP-204E06B/4 new delivery standard at Stauff "extended filter area" --> new Diameter 154,5 Sealing standard Viton packed per each item Product description: filter element Export - Customs tariff no.: 84219990 Country of origin: Czech Republic Material Surcharge 8,90 % 90,76 1.110,58 EAC - Eurasian Conformity''')
doc8.ents = [
   Span(doc8, 3, 4, label ="NORDER"),
   Span(doc8, 9, 12, label ="CONTRACT"),
   Span(doc8, 12, 13, label ="CONTRACT1"),
   Span(doc8, 13, 14, label ="POS"),
   Span(doc8, 14, 15, label ="AMOUNT"),
   Span(doc8, 16, 17, label ="ARTICLE"),
   Span(doc8, 17, 18, label ="PRICE"),
   Span(doc8, 18, 19, label ="UNIT"),
   Span(doc8, 20, 21, label ="SUMMA"),
   Span(doc8, 61, 62, label ="TARIFF"),
   Span(doc8, 66, 68, label ="COUNTRY"),
   Span(doc8, 70, 71, label ="PR_SURCH"),
   Span(doc8, 72, 73, label ="SURCHARGE"),
   Span(doc8, 73, 74, label ="TOTAL")]
docs.append(doc8)
print("doc9, 67, #NORDER 2386798; CONTRACT SR-1-06; CONTRACT1 1863; POS 2900; AMOUNT 14; ARTICLE 1910000835; PRICE 8,62; UNIT 1; SUMMA 120,68; TARIFF 84213925; COUNTRY Italy; PR_SURCH 11,40; SURCHARGE 13,76; TOTAL 134,44; ")
doc9 = nlp('''Order number: 2386798 Purchase order number: N SR-1-06 1863 2900 14 PC 1910000835 8,62 1 PC 120,68 SMBB-80-S-L-10-O-C-S150-O packed per each item Product description: filter breather Export - Customs tariff no.: 84213925    Country of origin: Italy Material Surcharge 11,40 % 13,76 134,44 EAC - Eurasian Conformity''')
doc9.ents = [
   Span(doc9, 3, 4, label ="NORDER"),
   Span(doc9, 9, 12, label ="CONTRACT"),
   Span(doc9, 12, 13, label ="CONTRACT1"),
   Span(doc9, 13, 14, label ="POS"),
   Span(doc9, 14, 15, label ="AMOUNT"),
   Span(doc9, 16, 17, label ="ARTICLE"),
   Span(doc9, 17, 18, label ="PRICE"),
   Span(doc9, 18, 19, label ="UNIT"),
   Span(doc9, 20, 21, label ="SUMMA"),
   Span(doc9, 50, 51, label ="TARIFF"),
   Span(doc9, 56, 57, label ="COUNTRY"),
   Span(doc9, 59, 60, label ="PR_SURCH"),
   Span(doc9, 61, 62, label ="SURCHARGE"),
   Span(doc9, 62, 63, label ="TOTAL")]
docs.append(doc9)
print("doc10, 79, #NORDER 2386854; CONTRACT SR-1-06; CONTRACT1 1870; POS 3000; AMOUNT 4; ARTICLE 1010002404; PRICE 28,37; UNIT 1; SUMMA 113,48; TARIFF 84212980; COUNTRY China; PR_SURCH 8,90; SURCHARGE 10,10; TOTAL 123,58; ")
doc10 = nlp('''Order number: 2386854 Purchase order number: N SR-1-06 1870 3000 4 PC 1010002404 28,37 1 PC 113,48 RFB-022-0-O0-B-G16-O-G16-L10 RFBO22...B/B/O/G/L10 packed per each item Product description: filter housing Export - Customs tariff no.: 84212980 Country of origin: China Material Surcharge 8,90 % 10,10 123,58 EAC - Eurasian Conformity''')
doc10.ents = [
   Span(doc10, 3, 4, label ="NORDER"),
   Span(doc10, 9, 12, label ="CONTRACT"),
   Span(doc10, 12, 13, label ="CONTRACT1"),
   Span(doc10, 13, 14, label ="POS"),
   Span(doc10, 14, 15, label ="AMOUNT"),
   Span(doc10, 16, 17, label ="ARTICLE"),
   Span(doc10, 17, 18, label ="PRICE"),
   Span(doc10, 18, 19, label ="UNIT"),
   Span(doc10, 20, 21, label ="SUMMA"),
   Span(doc10, 63, 64, label ="TARIFF"),
   Span(doc10, 68, 69, label ="COUNTRY"),
   Span(doc10, 71, 72, label ="PR_SURCH"),
   Span(doc10, 73, 74, label ="SURCHARGE"),
   Span(doc10, 74, 75, label ="TOTAL")]
docs.append(doc10)
print("doc11, 69, #NORDER 2388151; CONTRACT SR-1-06; CONTRACT1 1894; POS 3100; AMOUNT 10; ARTICLE 6010003210; PRICE 1.010,19; UNIT 100; SUMMA 101,02; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 6,97; TOTAL 107,99; ")
doc11 = nlp('''Order number: 2388151 Purchase order number: N SR-1-06 1894 3100 10 PC 6010003210 (*) 1.010,19 100 PC 101,02 FI-SNV-42L-V-W3-DKO FI-SNV-42L-B-W3-DKO packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 6,97 107,99''')
doc11.ents = [
   Span(doc11, 3, 4, label ="NORDER"),
   Span(doc11, 9, 12, label ="CONTRACT"),
   Span(doc11, 12, 13, label ="CONTRACT1"),
   Span(doc11, 13, 14, label ="POS"),
   Span(doc11, 14, 15, label ="AMOUNT"),
   Span(doc11, 16, 17, label ="ARTICLE"),
   Span(doc11, 20, 21, label ="PRICE"),
   Span(doc11, 21, 22, label ="UNIT"),
   Span(doc11, 23, 24, label ="SUMMA"),
   Span(doc11, 57, 58, label ="TARIFF"),
   Span(doc11, 62, 63, label ="COUNTRY"),
   Span(doc11, 65, 66, label ="PR_SURCH"),
   Span(doc11, 67, 68, label ="SURCHARGE"),
   Span(doc11, 68, 69, label ="TOTAL")]
docs.append(doc11)
print("doc12, 57, #NORDER 2390985; CONTRACT SR-1-06; CONTRACT1 1921; POS 3200; AMOUNT 2; ARTICLE 1730001175; PRICE 5,84; UNIT 1; SUMMA 11,68; TARIFF 73079100; COUNTRY Italy; PR_SURCH 15,50; SURCHARGE 1,81; TOTAL 13,49; ")
doc12 = nlp('''Order number: 2390985 Purchase order number: N SR-1-06 1921 3200 2 PC 1730001175 5,84 1 PC 11,68 BAS-302-SRE-25/19-W1 BAS-302-SRE-25/19 packed per each item    Product description: flange Export - Customs tariff no.: 73079100 Country of origin: Italy Material Surcharge 15,50 % 1,81 13,49''')
doc12.ents = [
   Span(doc12, 3, 4, label ="NORDER"),
   Span(doc12, 9, 12, label ="CONTRACT"),
   Span(doc12, 12, 13, label ="CONTRACT1"),
   Span(doc12, 13, 14, label ="POS"),
   Span(doc12, 14, 15, label ="AMOUNT"),
   Span(doc12, 16, 17, label ="ARTICLE"),
   Span(doc12, 17, 18, label ="PRICE"),
   Span(doc12, 18, 19, label ="UNIT"),
   Span(doc12, 20, 21, label ="SUMMA"),
   Span(doc12, 45, 46, label ="TARIFF"),
   Span(doc12, 50, 51, label ="COUNTRY"),
   Span(doc12, 53, 54, label ="PR_SURCH"),
   Span(doc12, 55, 56, label ="SURCHARGE"),
   Span(doc12, 56, 57, label ="TOTAL")]
docs.append(doc12)
print("doc13, 69, #NORDER 2391171; CONTRACT SR-1-06; CONTRACT1 1926; POS 3300; AMOUNT 20; ARTICLE 6100069717; PRICE 16,38; UNIT 1; SUMMA 327,60; TARIFF 84812010; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 22,60; TOTAL 350,20; ")
doc13 = nlp('''Order number: 2391171 Purchase order number: N SR-1-06 1926 3300 20 PC 6100069717 (*) 16,38 1 PC 327,60 QRC-RH-10-M-12S-BT-W3 RH08-2-S1220 packed per each item Product description: coupling Export - Customs tariff no.: 84812010 Country of origin: Germany Material Surcharge 6,90 % 22,60 350,20 EAC - Eurasian Conformity''')
doc13.ents = [
   Span(doc13, 3, 4, label ="NORDER"),
   Span(doc13, 9, 12, label ="CONTRACT"),
   Span(doc13, 12, 13, label ="CONTRACT1"),
   Span(doc13, 13, 14, label ="POS"),
   Span(doc13, 14, 15, label ="AMOUNT"),
   Span(doc13, 16, 17, label ="ARTICLE"),
   Span(doc13, 20, 21, label ="PRICE"),
   Span(doc13, 21, 22, label ="UNIT"),
   Span(doc13, 23, 24, label ="SUMMA"),
   Span(doc13, 53, 54, label ="TARIFF"),
   Span(doc13, 58, 59, label ="COUNTRY"),
   Span(doc13, 61, 62, label ="PR_SURCH"),
   Span(doc13, 63, 64, label ="SURCHARGE"),
   Span(doc13, 64, 65, label ="TOTAL")]
docs.append(doc13)
print("doc14, 53, #NORDER 2391175; CONTRACT SR-1-06; CONTRACT1 1930; POS 3400; AMOUNT 2; ARTICLE 1730002233; PRICE 23,55; UNIT 1; SUMMA 47,10; TARIFF 73072100; COUNTRY Italy; PR_SURCH 15,50; SURCHARGE 7,30; TOTAL 54,40; ")
doc14 = nlp('''Order number: 2391175 Purchase order number: N SR-1-06 1930 3400 2 PC 1730002233 23,55 1 PC 47,10 BFX-305-G-W5 packed per each item Product description: flange Export - Customs tariff no.: 73072100 Country of origin: Italy Material Surcharge 15,50 % 7,30 54,40''')
doc14.ents = [
   Span(doc14, 3, 4, label ="NORDER"),
   Span(doc14, 9, 12, label ="CONTRACT"),
   Span(doc14, 12, 13, label ="CONTRACT1"),
   Span(doc14, 13, 14, label ="POS"),
   Span(doc14, 14, 15, label ="AMOUNT"),
   Span(doc14, 16, 17, label ="ARTICLE"),
   Span(doc14, 17, 18, label ="PRICE"),
   Span(doc14, 18, 19, label ="UNIT"),
   Span(doc14, 20, 21, label ="SUMMA"),
   Span(doc14, 41, 42, label ="TARIFF"),
   Span(doc14, 46, 47, label ="COUNTRY"),
   Span(doc14, 49, 50, label ="PR_SURCH"),
   Span(doc14, 51, 52, label ="SURCHARGE"),
   Span(doc14, 52, 53, label ="TOTAL")]
docs.append(doc14)
print("doc15, 61, #NORDER 2391175; CONTRACT SR-1-06; CONTRACT1 1930; POS 3500; AMOUNT 4; ARTICLE 1710000563; PRICE 38,62; UNIT 1; SUMMA 154,48; TARIFF 73072100; COUNTRY Italy; PR_SURCH 15,50; SURCHARGE 23,94; TOTAL 178,42; ")
doc15 = nlp('''Order number: 2391175 Purchase order number: N SR-1-06 1930 3500 4 PC 1710000563 38,62 1 PC 154,48 BFX-303-G-W5-K BFX-303-G-W5#K packed per each item    Product description: flange Export - Customs tariff no.: 73072100 Country of origin: Italy Material Surcharge 15,50 % 23,94 178,42''')
doc15.ents = [
   Span(doc15, 3, 4, label ="NORDER"),
   Span(doc15, 9, 12, label ="CONTRACT"),
   Span(doc15, 12, 13, label ="CONTRACT1"),
   Span(doc15, 13, 14, label ="POS"),
   Span(doc15, 14, 15, label ="AMOUNT"),
   Span(doc15, 16, 17, label ="ARTICLE"),
   Span(doc15, 17, 18, label ="PRICE"),
   Span(doc15, 18, 19, label ="UNIT"),
   Span(doc15, 20, 21, label ="SUMMA"),
   Span(doc15, 49, 50, label ="TARIFF"),
   Span(doc15, 54, 55, label ="COUNTRY"),
   Span(doc15, 57, 58, label ="PR_SURCH"),
   Span(doc15, 59, 60, label ="SURCHARGE"),
   Span(doc15, 60, 61, label ="TOTAL")]
docs.append(doc15)
print("doc16, 66, #NORDER 2391178; CONTRACT SR-1-06; CONTRACT1 1933; POS 3600; AMOUNT 1; ARTICLE 1130004189; PRICE 561,56; UNIT 100; SUMMA 5,62; TARIFF 73181588; COUNTRY Italy; PR_SURCH 11,40; SURCHARGE 0,64; TOTAL 6,26; ")
doc16 = nlp('''Order number: 2391178 Purchase order number: N SR-1-06 1933 3600 1 PC 1130004189 561,56 100 PC 5,62 AS-M30x300-DIN931/933-8.8-W1 AS-M30X300-DIN931/933-8.8-W1 packed per each item Product description: screw Export - Customs tariff no.: 73181588 Country of origin: Italy Material Surcharge 11,40 % 0,64 6,26''')
doc16.ents = [
   Span(doc16, 3, 4, label ="NORDER"),
   Span(doc16, 9, 12, label ="CONTRACT"),
   Span(doc16, 12, 13, label ="CONTRACT1"),
   Span(doc16, 13, 14, label ="POS"),
   Span(doc16, 14, 15, label ="AMOUNT"),
   Span(doc16, 16, 17, label ="ARTICLE"),
   Span(doc16, 17, 18, label ="PRICE"),
   Span(doc16, 18, 19, label ="UNIT"),
   Span(doc16, 20, 21, label ="SUMMA"),
   Span(doc16, 54, 55, label ="TARIFF"),
   Span(doc16, 59, 60, label ="COUNTRY"),
   Span(doc16, 62, 63, label ="PR_SURCH"),
   Span(doc16, 64, 65, label ="SURCHARGE"),
   Span(doc16, 65, 66, label ="TOTAL")]
docs.append(doc16)
print("doc17, 57, #NORDER 2391477; CONTRACT SR-1-06; CONTRACT1 1956; POS 3700; AMOUNT 1.500; ARTICLE 6020002495; PRICE 47,50; UNIT 100; SUMMA 712,50; TARIFF 73269098; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 49,16; TOTAL 761,66; ")
doc17 = nlp('''Order number: 2391477 Purchase order number: N SR-1-06 1956 3700 1.500 PC 6020002495 47,50 100 PC 712,50 FI-WDDS-08L/S-V-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 6,90 % 49,16 761,66''')
doc17.ents = [
   Span(doc17, 3, 4, label ="NORDER"),
   Span(doc17, 9, 12, label ="CONTRACT"),
   Span(doc17, 12, 13, label ="CONTRACT1"),
   Span(doc17, 13, 14, label ="POS"),
   Span(doc17, 14, 15, label ="AMOUNT"),
   Span(doc17, 16, 17, label ="ARTICLE"),
   Span(doc17, 17, 18, label ="PRICE"),
   Span(doc17, 18, 19, label ="UNIT"),
   Span(doc17, 20, 21, label ="SUMMA"),
   Span(doc17, 45, 46, label ="TARIFF"),
   Span(doc17, 50, 51, label ="COUNTRY"),
   Span(doc17, 53, 54, label ="PR_SURCH"),
   Span(doc17, 55, 56, label ="SURCHARGE"),
   Span(doc17, 56, 57, label ="TOTAL")]
docs.append(doc17)
print("doc18, 58, #NORDER 2391477; CONTRACT SR-1-06; CONTRACT1 1956; POS 3800; AMOUNT 1.500; ARTICLE 6020002497; PRICE 63,73; UNIT 100; SUMMA 955,95; TARIFF 73269098; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 65,96; TOTAL 1.021,91; ")
doc18 = nlp('''Order number: 2391477 Purchase order number: N SR-1-06 1956 3800 1.500 PC 6020002497 63,73 100 PC 955,95 FI-WDDS-12L/S-V-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73269098    Country of origin: Germany Material Surcharge 6,90 % 65,96 1.021,91''')
doc18.ents = [
   Span(doc18, 3, 4, label ="NORDER"),
   Span(doc18, 9, 12, label ="CONTRACT"),
   Span(doc18, 12, 13, label ="CONTRACT1"),
   Span(doc18, 13, 14, label ="POS"),
   Span(doc18, 14, 15, label ="AMOUNT"),
   Span(doc18, 16, 17, label ="ARTICLE"),
   Span(doc18, 17, 18, label ="PRICE"),
   Span(doc18, 18, 19, label ="UNIT"),
   Span(doc18, 20, 21, label ="SUMMA"),
   Span(doc18, 45, 46, label ="TARIFF"),
   Span(doc18, 51, 52, label ="COUNTRY"),
   Span(doc18, 54, 55, label ="PR_SURCH"),
   Span(doc18, 56, 57, label ="SURCHARGE"),
   Span(doc18, 57, 58, label ="TOTAL")]
docs.append(doc18)
print("doc19, 71, #NORDER 2393463; CONTRACT SR-1-06; CONTRACT1 1972; POS 3900; AMOUNT 10; ARTICLE 1110030608; PRICE 280,27; UNIT 100; SUMMA 28,03; TARIFF 39269097; COUNTRY Germany; PR_SURCH 10,40; SURCHARGE 2,92; TOTAL 30,95; ")
doc19 = nlp('''Order number: 2393463 Purchase order number: N SR-1-06 1972 3900 10 PC 1110030608 280,27 100 PC 28,03 SPV-112a-PP-DP-AS-M-W5-A SPV 112A PP-DP-AS M W5#A packed per each item Product description: clamp combination Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 10,40 % 2,92 30,95''')
doc19.ents = [
   Span(doc19, 3, 4, label ="NORDER"),
   Span(doc19, 9, 12, label ="CONTRACT"),
   Span(doc19, 12, 13, label ="CONTRACT1"),
   Span(doc19, 13, 14, label ="POS"),
   Span(doc19, 14, 15, label ="AMOUNT"),
   Span(doc19, 16, 17, label ="ARTICLE"),
   Span(doc19, 17, 18, label ="PRICE"),
   Span(doc19, 18, 19, label ="UNIT"),
   Span(doc19, 20, 21, label ="SUMMA"),
   Span(doc19, 59, 60, label ="TARIFF"),
   Span(doc19, 64, 65, label ="COUNTRY"),
   Span(doc19, 67, 68, label ="PR_SURCH"),
   Span(doc19, 69, 70, label ="SURCHARGE"),
   Span(doc19, 70, 71, label ="TOTAL")]
docs.append(doc19)
print("doc20, 53, #NORDER 2393470; CONTRACT SR-1-06; CONTRACT1 1979; POS 4000; AMOUNT 2; ARTICLE 6100004078; PRICE 31,32; UNIT 1; SUMMA 62,64; TARIFF 73072100; COUNTRY Italy; PR_SURCH 15,50; SURCHARGE 9,71; TOTAL 72,35; ")
doc20 = nlp('''Order number: 2393470 Purchase order number: N SR-1-06 1979 4000 2 PC 6100004078 31,32 1 PC 62,64 BAS-303-SRE-35/27-W5 packed per each item Product description: flange Export - Customs tariff no.: 73072100 Country of origin: Italy Material Surcharge 15,50 % 9,71 72,35''')
doc20.ents = [
   Span(doc20, 3, 4, label ="NORDER"),
   Span(doc20, 9, 12, label ="CONTRACT"),
   Span(doc20, 12, 13, label ="CONTRACT1"),
   Span(doc20, 13, 14, label ="POS"),
   Span(doc20, 14, 15, label ="AMOUNT"),
   Span(doc20, 16, 17, label ="ARTICLE"),
   Span(doc20, 17, 18, label ="PRICE"),
   Span(doc20, 18, 19, label ="UNIT"),
   Span(doc20, 20, 21, label ="SUMMA"),
   Span(doc20, 41, 42, label ="TARIFF"),
   Span(doc20, 46, 47, label ="COUNTRY"),
   Span(doc20, 49, 50, label ="PR_SURCH"),
   Span(doc20, 51, 52, label ="SURCHARGE"),
   Span(doc20, 52, 53, label ="TOTAL")]
docs.append(doc20)
print("doc21, 50, #NORDER 2393470; CONTRACT SR-1-06; CONTRACT1 1979; POS 4100; AMOUNT 4; ARTICLE 6100179013; PRICE 55,21; UNIT 1; SUMMA 220,84; TARIFF 73072100; COUNTRY Italy; PR_SURCH 15,50; SURCHARGE 34,23; TOTAL 255,07; ")
doc21 = nlp('''Order number: 2393470 Purchase order number: N SR-1-06 1979 4100 4 PC 6100179013 55,21 1 PC 220,84 BAS-603-SRE-25/17-W5 packed per each item Export - Customs tariff no.: 73072100 Country of origin: Italy Material Surcharge 15,50 % 34,23   255,07''')
doc21.ents = [
   Span(doc21, 3, 4, label ="NORDER"),
   Span(doc21, 9, 12, label ="CONTRACT"),
   Span(doc21, 12, 13, label ="CONTRACT1"),
   Span(doc21, 13, 14, label ="POS"),
   Span(doc21, 14, 15, label ="AMOUNT"),
   Span(doc21, 16, 17, label ="ARTICLE"),
   Span(doc21, 17, 18, label ="PRICE"),
   Span(doc21, 18, 19, label ="UNIT"),
   Span(doc21, 20, 21, label ="SUMMA"),
   Span(doc21, 37, 38, label ="TARIFF"),
   Span(doc21, 42, 43, label ="COUNTRY"),
   Span(doc21, 45, 46, label ="PR_SURCH"),
   Span(doc21, 47, 48, label ="SURCHARGE"),
   Span(doc21, 49, 50, label ="TOTAL")]
docs.append(doc21)
print("doc22, 55, #NORDER 2393487; CONTRACT SR-1-06; CONTRACT1 1969; POS 4200; AMOUNT 7; ARTICLE 6100240708; PRICE 11,92; UNIT 1; SUMMA 83,44; TARIFF 73079100; COUNTRY Italy; PR_SURCH 15,50; SURCHARGE 12,93; TOTAL 96,37; ")
doc22 = nlp('''Order number: 2393487 Purchase order number: N SR-1-06 1969 4200 7 PC 6100240708 11,92 1 PC 83,44 BFX-605-CP-W11-C3 packed per each item Product description: flange Export - Customs tariff no.: 73079100 Country of origin: Italy Material Surcharge 15,50 % 12,93 96,37''')
doc22.ents = [
   Span(doc22, 3, 4, label ="NORDER"),
   Span(doc22, 9, 12, label ="CONTRACT"),
   Span(doc22, 12, 13, label ="CONTRACT1"),
   Span(doc22, 13, 14, label ="POS"),
   Span(doc22, 14, 15, label ="AMOUNT"),
   Span(doc22, 16, 17, label ="ARTICLE"),
   Span(doc22, 17, 18, label ="PRICE"),
   Span(doc22, 18, 19, label ="UNIT"),
   Span(doc22, 20, 21, label ="SUMMA"),
   Span(doc22, 43, 44, label ="TARIFF"),
   Span(doc22, 48, 49, label ="COUNTRY"),
   Span(doc22, 51, 52, label ="PR_SURCH"),
   Span(doc22, 53, 54, label ="SURCHARGE"),
   Span(doc22, 54, 55, label ="TOTAL")]
docs.append(doc22)
print("doc23, 56, #NORDER 2393487; CONTRACT SR-1-06; CONTRACT1 1969; POS 4300; AMOUNT 6; ARTICLE 6100133267; PRICE 10,13; UNIT 1; SUMMA 60,78; TARIFF 73079100; COUNTRY Italy; PR_SURCH 15,50; SURCHARGE 9,42; TOTAL 70,20; ")
doc23 = nlp('''Order number: 2393487 Purchase order number: N SR-1-06 1969 4300 6 PC 6100133267 10,13 1 PC 60,78 BAS-307-CP-W 1-C3 packed per each item Product description: flange Export - Customs tariff no.: 73079100 Country of origin: Italy Material Surcharge 15,50 % 9,42 70,20''')
doc23.ents = [
   Span(doc23, 3, 4, label ="NORDER"),
   Span(doc23, 9, 12, label ="CONTRACT"),
   Span(doc23, 12, 13, label ="CONTRACT1"),
   Span(doc23, 13, 14, label ="POS"),
   Span(doc23, 14, 15, label ="AMOUNT"),
   Span(doc23, 16, 17, label ="ARTICLE"),
   Span(doc23, 17, 18, label ="PRICE"),
   Span(doc23, 18, 19, label ="UNIT"),
   Span(doc23, 20, 21, label ="SUMMA"),
   Span(doc23, 44, 45, label ="TARIFF"),
   Span(doc23, 49, 50, label ="COUNTRY"),
   Span(doc23, 52, 53, label ="PR_SURCH"),
   Span(doc23, 54, 55, label ="SURCHARGE"),
   Span(doc23, 55, 56, label ="TOTAL")]
docs.append(doc23)
print("doc24, 49, #NORDER 2393664; CONTRACT SR-1-06; CONTRACT1 1991; POS 4400; AMOUNT 2; ARTICLE 6100008161; PRICE 98,75; UNIT 1; SUMMA 197,50; TARIFF 73072100; COUNTRY Italy; PR_SURCH 15,50; SURCHARGE 30,61; TOTAL 228,11; ")
doc24 = nlp('''Order number: 2393664 Purchase order number: N SR-1-06 1991 4400 2 PC 6100008161 98,75 1 PC 197,50 BAS-606-ST-61/43-W5 packed per each item Export - Customs tariff no.: 73072100 Country of origin: Italy Material Surcharge 15,50 % 30,61 228,11''')
doc24.ents = [
   Span(doc24, 3, 4, label ="NORDER"),
   Span(doc24, 9, 12, label ="CONTRACT"),
   Span(doc24, 12, 13, label ="CONTRACT1"),
   Span(doc24, 13, 14, label ="POS"),
   Span(doc24, 14, 15, label ="AMOUNT"),
   Span(doc24, 16, 17, label ="ARTICLE"),
   Span(doc24, 17, 18, label ="PRICE"),
   Span(doc24, 18, 19, label ="UNIT"),
   Span(doc24, 20, 21, label ="SUMMA"),
   Span(doc24, 37, 38, label ="TARIFF"),
   Span(doc24, 42, 43, label ="COUNTRY"),
   Span(doc24, 45, 46, label ="PR_SURCH"),
   Span(doc24, 47, 48, label ="SURCHARGE"),
   Span(doc24, 48, 49, label ="TOTAL")]
docs.append(doc24)
print("doc25, 54, #NORDER 2393664; CONTRACT SR-1-06; CONTRACT1 1991; POS 4500; AMOUNT 2; ARTICLE 6100088211; PRICE 202,27; UNIT 1; SUMMA 404,54; TARIFF 73072100; COUNTRY Italy; PR_SURCH 15,50; SURCHARGE 62,70; TOTAL 467,24; ")
doc25 = nlp('''Order number: 2393664 Purchase order number: N SR-1-06 1991 4500 2 PC 6100088211 202,27 1 PC 404,54    BAS-310-STRE-90/82-W5 packed per each item Product description: flange Export - Customs tariff no.: 73072100 Country of origin: Italy Material Surcharge 15,50 % 62,70 467,24''')
doc25.ents = [
   Span(doc25, 3, 4, label ="NORDER"),
   Span(doc25, 9, 12, label ="CONTRACT"),
   Span(doc25, 12, 13, label ="CONTRACT1"),
   Span(doc25, 13, 14, label ="POS"),
   Span(doc25, 14, 15, label ="AMOUNT"),
   Span(doc25, 16, 17, label ="ARTICLE"),
   Span(doc25, 17, 18, label ="PRICE"),
   Span(doc25, 18, 19, label ="UNIT"),
   Span(doc25, 20, 21, label ="SUMMA"),
   Span(doc25, 42, 43, label ="TARIFF"),
   Span(doc25, 47, 48, label ="COUNTRY"),
   Span(doc25, 50, 51, label ="PR_SURCH"),
   Span(doc25, 52, 53, label ="SURCHARGE"),
   Span(doc25, 53, 54, label ="TOTAL")]
docs.append(doc25)
print("doc26, 60, #NORDER 2393664; CONTRACT SR-1-06; CONTRACT1 1991; POS 4600; AMOUNT 9; ARTICLE 1710000977; PRICE 82,11; UNIT 1; SUMMA 738,99; TARIFF 73072100; COUNTRY Italy; PR_SURCH 15,50; SURCHARGE 114,54; TOTAL 853,53; ")
doc26 = nlp('''Order number: 2393664 Purchase order number: N SR-1-06 1991 4600 9 PC 1710000977 82,11 1 PC 738,99 BFX-307 -STRE-77/70-W5-K BFX-307-STRE-7 7/70-W5#K packed per each item Product description: flange Export - Customs tariff no.: 73072100 Country of origin: Italy Material Surcharge 15,50 % 114,54 853,53''')
doc26.ents = [
   Span(doc26, 3, 4, label ="NORDER"),
   Span(doc26, 9, 12, label ="CONTRACT"),
   Span(doc26, 12, 13, label ="CONTRACT1"),
   Span(doc26, 13, 14, label ="POS"),
   Span(doc26, 14, 15, label ="AMOUNT"),
   Span(doc26, 16, 17, label ="ARTICLE"),
   Span(doc26, 17, 18, label ="PRICE"),
   Span(doc26, 18, 19, label ="UNIT"),
   Span(doc26, 20, 21, label ="SUMMA"),
   Span(doc26, 48, 49, label ="TARIFF"),
   Span(doc26, 53, 54, label ="COUNTRY"),
   Span(doc26, 56, 57, label ="PR_SURCH"),
   Span(doc26, 58, 59, label ="SURCHARGE"),
   Span(doc26, 59, 60, label ="TOTAL")]
docs.append(doc26)
print("doc27, 67, #NORDER 2393669; CONTRACT SR-1-06; CONTRACT1 1995; POS 4700; AMOUNT 25; ARTICLE 1210026116; PRICE 4,51; UNIT 1; SUMMA 112,75; TARIFF 84818073; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 12,85; TOTAL 125,60; ")
doc27 = nlp('''Order number: 2393669 Purchase order number: N SR-1-06 1995 4700 25 PC 1210026116 (*) 4,51 1 PC 112,75 SMK-20-G1/4-B-C-W3 SMK20-G1/4-PC-C6F packed per each item Product description: coupling Export - Customs tariff no.: 84818073 Country of origin: Germany Material Surcharge 11,40 % 12,85 125,60''')
doc27.ents = [
   Span(doc27, 3, 4, label ="NORDER"),
   Span(doc27, 9, 12, label ="CONTRACT"),
   Span(doc27, 12, 13, label ="CONTRACT1"),
   Span(doc27, 13, 14, label ="POS"),
   Span(doc27, 14, 15, label ="AMOUNT"),
   Span(doc27, 16, 17, label ="ARTICLE"),
   Span(doc27, 20, 21, label ="PRICE"),
   Span(doc27, 21, 22, label ="UNIT"),
   Span(doc27, 23, 24, label ="SUMMA"),
   Span(doc27, 55, 56, label ="TARIFF"),
   Span(doc27, 60, 61, label ="COUNTRY"),
   Span(doc27, 63, 64, label ="PR_SURCH"),
   Span(doc27, 65, 66, label ="SURCHARGE"),
   Span(doc27, 66, 67, label ="TOTAL")]
docs.append(doc27)
print("doc28, 61, #NORDER 2393669; CONTRACT SR-1-06; CONTRACT1 1995; POS 4800; AMOUNT 1; ARTICLE 3404000165; PRICE 207,02; UNIT 1; SUMMA 207,02; TARIFF 84812010; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 14,28; TOTAL 221,30; ")
doc28 = nlp('''Order number: 2393669 Purchase order number: N SR-1-06 1995 4800 1 PC 3404000165 207,02 1 PC 207,02 BBV -2-G20R-1101-M   BBV2G20R1101M packed per each item Product description: valve Export - Customs tariff no.: 84812010 Country of origin: Germany Material Surcharge 6,90 % 14,28 221,30 EAC - Eurasian Conformity''')
doc28.ents = [
   Span(doc28, 3, 4, label ="NORDER"),
   Span(doc28, 9, 12, label ="CONTRACT"),
   Span(doc28, 12, 13, label ="CONTRACT1"),
   Span(doc28, 13, 14, label ="POS"),
   Span(doc28, 14, 15, label ="AMOUNT"),
   Span(doc28, 16, 17, label ="ARTICLE"),
   Span(doc28, 17, 18, label ="PRICE"),
   Span(doc28, 18, 19, label ="UNIT"),
   Span(doc28, 20, 21, label ="SUMMA"),
   Span(doc28, 45, 46, label ="TARIFF"),
   Span(doc28, 50, 51, label ="COUNTRY"),
   Span(doc28, 53, 54, label ="PR_SURCH"),
   Span(doc28, 55, 56, label ="SURCHARGE"),
   Span(doc28, 56, 57, label ="TOTAL")]
docs.append(doc28)
print("doc29, 59, #NORDER 2393715; CONTRACT SR-1-06; CONTRACT1 2013; POS 4900; AMOUNT 10; ARTICLE 1020023700; PRICE 74,91; UNIT 1; SUMMA 749,10; TARIFF 84219990; COUNTRY Germany; PR_SURCH 8,90; SURCHARGE 66,67; TOTAL 815,77; ")
doc29 = nlp('''Order number: 2393715 Purchase order number: N SR-1-06 2013 4900 10 PC 1020023700 74,91 1 PC 749,10 SE-160-G-10-B/4 SE-160G10B/4 packed per each item Product description: filter element Export - Customs tariff no.: 84219990 Country of origin: Germany Material Surcharge 8,90 % 66,67 815,77 EAC - Eurasian Conformity''')
doc29.ents = [
   Span(doc29, 3, 4, label ="NORDER"),
   Span(doc29, 9, 12, label ="CONTRACT"),
   Span(doc29, 12, 13, label ="CONTRACT1"),
   Span(doc29, 13, 14, label ="POS"),
   Span(doc29, 14, 15, label ="AMOUNT"),
   Span(doc29, 16, 17, label ="ARTICLE"),
   Span(doc29, 17, 18, label ="PRICE"),
   Span(doc29, 18, 19, label ="UNIT"),
   Span(doc29, 20, 21, label ="SUMMA"),
   Span(doc29, 43, 44, label ="TARIFF"),
   Span(doc29, 48, 49, label ="COUNTRY"),
   Span(doc29, 51, 52, label ="PR_SURCH"),
   Span(doc29, 53, 54, label ="SURCHARGE"),
   Span(doc29, 54, 55, label ="TOTAL")]
docs.append(doc29)
print("doc30, 71, #NORDER 2399576; CONTRACT SR-1-06; CONTRACT1 12; POS 5000; AMOUNT 60; ARTICLE 1110024275; PRICE 417,86; UNIT 100; SUMMA 250,72; TARIFF 39269097; COUNTRY Germany; PR_SURCH 10,40; SURCHARGE 26,07; TOTAL 276,79; ")
doc30 = nlp('''Order number: 2399576 Purchase order number: N SR-1-06 12 5000 60 PC 1110024275 417,86 100 PC 250,72 SPV-538-PP-DP-AS-M-W5-A SPV 538 PP-DP-AS M W5#A packed per each item Product description: clamp combination Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 10,40 % 26,07 276,79''')
doc30.ents = [
   Span(doc30, 3, 4, label ="NORDER"),
   Span(doc30, 9, 12, label ="CONTRACT"),
   Span(doc30, 12, 13, label ="CONTRACT1"),
   Span(doc30, 13, 14, label ="POS"),
   Span(doc30, 14, 15, label ="AMOUNT"),
   Span(doc30, 16, 17, label ="ARTICLE"),
   Span(doc30, 17, 18, label ="PRICE"),
   Span(doc30, 18, 19, label ="UNIT"),
   Span(doc30, 20, 21, label ="SUMMA"),
   Span(doc30, 59, 60, label ="TARIFF"),
   Span(doc30, 64, 65, label ="COUNTRY"),
   Span(doc30, 67, 68, label ="PR_SURCH"),
   Span(doc30, 69, 70, label ="SURCHARGE"),
   Span(doc30, 70, 71, label ="TOTAL")]
docs.append(doc30)
print("doc31, 63, #NORDER 2399576; CONTRACT SR-1-06; CONTRACT1 12; POS 5100; AMOUNT 20; ARTICLE 6100113990; PRICE 767,53; UNIT 100; SUMMA 153,51; TARIFF 39269097; COUNTRY Germany; PR_SURCH 10,40; SURCHARGE 15,97; TOTAL 169,48; ")
doc31 = nlp('''Order number: 2399576   Purchase order number: N SR-1-06 12 5100 20 PC 6100113990 767,53 100 PC 153,51 SPV-770-PP-DP-AS-M-W5-A packed per each item Product description: clamp combination Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 10,40 % 15,97 169,48''')
doc31.ents = [
   Span(doc31, 3, 4, label ="NORDER"),
   Span(doc31, 10, 13, label ="CONTRACT"),
   Span(doc31, 13, 14, label ="CONTRACT1"),
   Span(doc31, 14, 15, label ="POS"),
   Span(doc31, 15, 16, label ="AMOUNT"),
   Span(doc31, 17, 18, label ="ARTICLE"),
   Span(doc31, 18, 19, label ="PRICE"),
   Span(doc31, 19, 20, label ="UNIT"),
   Span(doc31, 21, 22, label ="SUMMA"),
   Span(doc31, 51, 52, label ="TARIFF"),
   Span(doc31, 56, 57, label ="COUNTRY"),
   Span(doc31, 59, 60, label ="PR_SURCH"),
   Span(doc31, 61, 62, label ="SURCHARGE"),
   Span(doc31, 62, 63, label ="TOTAL")]
docs.append(doc31)
print("doc32, 58, #NORDER 2399894; CONTRACT SR-1-06; CONTRACT1 32; POS 5200; AMOUNT 25; ARTICLE 1120001188; PRICE 31,83; UNIT 100; SUMMA 7,96; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,91; TOTAL 8,87; ")
doc32 = nlp('''Order number: 2399894 Purchase order number: N SR-1-06 32 5200 25 PC 1120001188 31,83 100 PC 7,96 SP-3-M-W3 SP 3 M W3 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 0,91 8,87''')
doc32.ents = [
   Span(doc32, 3, 4, label ="NORDER"),
   Span(doc32, 9, 12, label ="CONTRACT"),
   Span(doc32, 12, 13, label ="CONTRACT1"),
   Span(doc32, 13, 14, label ="POS"),
   Span(doc32, 14, 15, label ="AMOUNT"),
   Span(doc32, 16, 17, label ="ARTICLE"),
   Span(doc32, 17, 18, label ="PRICE"),
   Span(doc32, 18, 19, label ="UNIT"),
   Span(doc32, 20, 21, label ="SUMMA"),
   Span(doc32, 46, 47, label ="TARIFF"),
   Span(doc32, 51, 52, label ="COUNTRY"),
   Span(doc32, 54, 55, label ="PR_SURCH"),
   Span(doc32, 56, 57, label ="SURCHARGE"),
   Span(doc32, 57, 58, label ="TOTAL")]
docs.append(doc32)
print("doc33, 58, #NORDER 2399900; CONTRACT SR-1-06; CONTRACT1 33; POS 5300; AMOUNT 25; ARTICLE 1120001188; PRICE 31,83; UNIT 100; SUMMA 7,96; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,91; TOTAL 8,87; ")
doc33 = nlp('''Order number: 2399900 Purchase order number: N SR-1-06 33 5300 25 PC 1120001188 31,83 100 PC 7,96 SP-3-M-W3 SP 3 M W3 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 0,91 8,87''')
doc33.ents = [
   Span(doc33, 3, 4, label ="NORDER"),
   Span(doc33, 9, 12, label ="CONTRACT"),
   Span(doc33, 12, 13, label ="CONTRACT1"),
   Span(doc33, 13, 14, label ="POS"),
   Span(doc33, 14, 15, label ="AMOUNT"),
   Span(doc33, 16, 17, label ="ARTICLE"),
   Span(doc33, 17, 18, label ="PRICE"),
   Span(doc33, 18, 19, label ="UNIT"),
   Span(doc33, 20, 21, label ="SUMMA"),
   Span(doc33, 46, 47, label ="TARIFF"),
   Span(doc33, 51, 52, label ="COUNTRY"),
   Span(doc33, 54, 55, label ="PR_SURCH"),
   Span(doc33, 56, 57, label ="SURCHARGE"),
   Span(doc33, 57, 58, label ="TOTAL")]
docs.append(doc33)
print("doc34, 67, #NORDER 2400283; CONTRACT SR-1-06; CONTRACT1 43; POS 5400; AMOUNT 168; ARTICLE 1130004041; PRICE 40,63; UNIT 100; SUMMA 68,26; TARIFF 73181575; COUNTRY Thailand; PR_SURCH 10,40; SURCHARGE 7,10; TOTAL 75,36; ")
doc34 = nlp('''Order number: 2400283 Purchase order number: N SR-1-06 43   5400 168 PC 1130004041 40,63 100 PC 68,26 AS-M6x100-DIN931/933-70-W5 AS-M6X100-DIN931/933-70-W5 packed per each item Product description: screw Export - Customs tariff no.: 73181575 Country of origin: Thailand Material Surcharge 10,40 % 7,10 75,36''')
doc34.ents = [
   Span(doc34, 3, 4, label ="NORDER"),
   Span(doc34, 9, 12, label ="CONTRACT"),
   Span(doc34, 12, 13, label ="CONTRACT1"),
   Span(doc34, 14, 15, label ="POS"),
   Span(doc34, 15, 16, label ="AMOUNT"),
   Span(doc34, 17, 18, label ="ARTICLE"),
   Span(doc34, 18, 19, label ="PRICE"),
   Span(doc34, 19, 20, label ="UNIT"),
   Span(doc34, 21, 22, label ="SUMMA"),
   Span(doc34, 55, 56, label ="TARIFF"),
   Span(doc34, 60, 61, label ="COUNTRY"),
   Span(doc34, 63, 64, label ="PR_SURCH"),
   Span(doc34, 65, 66, label ="SURCHARGE"),
   Span(doc34, 66, 67, label ="TOTAL")]
docs.append(doc34)
print("doc35, 59, #NORDER 2403214; CONTRACT SR-1-06; CONTRACT1 69; POS 5500; AMOUNT 4; ARTICLE 1020022807; PRICE 180,76; UNIT 1; SUMMA 723,04; TARIFF 84219990; COUNTRY Germany; PR_SURCH 8,90; SURCHARGE 64,35; TOTAL 787,39; ")
doc35 = nlp('''Order number: 2403214 Purchase order number: N SR-1-06 69 5500 4 PC 1020022807 180,76 1 PC 723,04 RE-600-G-20-B/5 RE-600G20B/5 packed per each item Product description: filter element Export - Customs tariff no.: 84219990 Country of origin: Germany Material Surcharge 8,90 % 64,35 787,39 EAC - Eurasian Conformity''')
doc35.ents = [
   Span(doc35, 3, 4, label ="NORDER"),
   Span(doc35, 9, 12, label ="CONTRACT"),
   Span(doc35, 12, 13, label ="CONTRACT1"),
   Span(doc35, 13, 14, label ="POS"),
   Span(doc35, 14, 15, label ="AMOUNT"),
   Span(doc35, 16, 17, label ="ARTICLE"),
   Span(doc35, 17, 18, label ="PRICE"),
   Span(doc35, 18, 19, label ="UNIT"),
   Span(doc35, 20, 21, label ="SUMMA"),
   Span(doc35, 43, 44, label ="TARIFF"),
   Span(doc35, 48, 49, label ="COUNTRY"),
   Span(doc35, 51, 52, label ="PR_SURCH"),
   Span(doc35, 53, 54, label ="SURCHARGE"),
   Span(doc35, 54, 55, label ="TOTAL")]
docs.append(doc35)
print("doc36, 73, #NORDER 2403216; CONTRACT SR-1-06; CONTRACT1 71; POS 5600; AMOUNT 16; ARTICLE 1110009552; PRICE 310,19; UNIT 100; SUMMA 49,63; TARIFF 76169910; COUNTRY Poland; PR_SURCH 11,40; SURCHARGE 5,66; TOTAL 55,29; ")
doc36 = nlp('''Order number: 2403216 Purchase order number: N SR-1-06 71 5600 16 PC 1110009552 (*) 310,19 100 PC 49,63 SPAL-4022-AL-DPAL-AS-M -W12-A SPAL 4022 AL-DPAL-AS M W12#A packed per each item Product description: clamp combination Export - Customs tariff no.: 76169910 Country of origin: Poland Material Surcharge 11,40 % 5,66 55,29''')
doc36.ents = [
   Span(doc36, 3, 4, label ="NORDER"),
   Span(doc36, 9, 12, label ="CONTRACT"),
   Span(doc36, 12, 13, label ="CONTRACT1"),
   Span(doc36, 13, 14, label ="POS"),
   Span(doc36, 14, 15, label ="AMOUNT"),
   Span(doc36, 16, 17, label ="ARTICLE"),
   Span(doc36, 20, 21, label ="PRICE"),
   Span(doc36, 21, 22, label ="UNIT"),
   Span(doc36, 23, 24, label ="SUMMA"),
   Span(doc36, 61, 62, label ="TARIFF"),
   Span(doc36, 66, 67, label ="COUNTRY"),
   Span(doc36, 69, 70, label ="PR_SURCH"),
   Span(doc36, 71, 72, label ="SURCHARGE"),
   Span(doc36, 72, 73, label ="TOTAL")]
docs.append(doc36)
print("doc37, 75, #NORDER 2403216; CONTRACT SR-1-06; CONTRACT1 71; POS 5700; AMOUNT 21; ARTICLE 1110009568; PRICE 978,02; UNIT 100; SUMMA 205,38; TARIFF 76169910; COUNTRY Lithuania; PR_SURCH 11,40; SURCHARGE 23,41; TOTAL 228,79; ")
doc37 = nlp('''Order number: 2403216   Purchase order number: N SR-1-06 71 5700 21 PC 1110009568 (*) 978,02 100 PC 205,38 SPAL-6060.3-AL-DPAL-AS-M-W12-A SPAL 6060,3 AL-DPAL-AS M W12#A packed per each item Product description: clamp combination Export - Customs tariff no.: 76169910 Country of origin: Lithuania Material Surcharge 11,40 % 23,41 228,79''')
doc37.ents = [
   Span(doc37, 3, 4, label ="NORDER"),
   Span(doc37, 10, 13, label ="CONTRACT"),
   Span(doc37, 13, 14, label ="CONTRACT1"),
   Span(doc37, 14, 15, label ="POS"),
   Span(doc37, 15, 16, label ="AMOUNT"),
   Span(doc37, 17, 18, label ="ARTICLE"),
   Span(doc37, 21, 22, label ="PRICE"),
   Span(doc37, 22, 23, label ="UNIT"),
   Span(doc37, 24, 25, label ="SUMMA"),
   Span(doc37, 63, 64, label ="TARIFF"),
   Span(doc37, 68, 69, label ="COUNTRY"),
   Span(doc37, 71, 72, label ="PR_SURCH"),
   Span(doc37, 73, 74, label ="SURCHARGE"),
   Span(doc37, 74, 75, label ="TOTAL")]
docs.append(doc37)
print("doc38, 55, #NORDER 2403217; CONTRACT SR-1-06; CONTRACT1 72; POS 5800; AMOUNT 1; ARTICLE 6100177987; PRICE 42,34; UNIT 1; SUMMA 42,34; TARIFF 73072100; COUNTRY Italy; PR_SURCH 15,50; SURCHARGE 6,56; TOTAL 48,90; ")
doc38 = nlp('''Order number: 2403217 Purchase order number: N SR-1-06 72 5800 1 PC 6100177987 42,34 1 PC 42,34 BFX-305-SRE-42/36-W5-K packed per each item Product description: flange Export - Customs tariff no.: 73072100 Country of origin: Italy Material Surcharge 15,50 % 6,56 48,90''')
doc38.ents = [
   Span(doc38, 3, 4, label ="NORDER"),
   Span(doc38, 9, 12, label ="CONTRACT"),
   Span(doc38, 12, 13, label ="CONTRACT1"),
   Span(doc38, 13, 14, label ="POS"),
   Span(doc38, 14, 15, label ="AMOUNT"),
   Span(doc38, 16, 17, label ="ARTICLE"),
   Span(doc38, 17, 18, label ="PRICE"),
   Span(doc38, 18, 19, label ="UNIT"),
   Span(doc38, 20, 21, label ="SUMMA"),
   Span(doc38, 43, 44, label ="TARIFF"),
   Span(doc38, 48, 49, label ="COUNTRY"),
   Span(doc38, 51, 52, label ="PR_SURCH"),
   Span(doc38, 53, 54, label ="SURCHARGE"),
   Span(doc38, 54, 55, label ="TOTAL")]
docs.append(doc38)
print("doc39, 63, #NORDER 2403217; CONTRACT SR-1-06; CONTRACT1 72; POS 5900; AMOUNT 6; ARTICLE 1710000294; PRICE 45,00; UNIT 1; SUMMA 270,00; TARIFF 73072100; COUNTRY Europ.; PR_SURCH 15,50; SURCHARGE 41,85; TOTAL 311,85; ")
doc39 = nlp('''Order number: 2403217 Purchase order number: N SR-1-06 72 5900 6 PC 1710000294 45,00 1 PC 270,00 BFX-304-ST-42.8/32-W5-K BFX-304-ST-42,8/32-W5#K packed per each item Product description: flange Export - Customs tariff no.: 73072100 Country of origin: Europ. Comm. Material Surcharge 15,50 % 41,85 311,85''')
doc39.ents = [
   Span(doc39, 3, 4, label ="NORDER"),
   Span(doc39, 9, 12, label ="CONTRACT"),
   Span(doc39, 12, 13, label ="CONTRACT1"),
   Span(doc39, 13, 14, label ="POS"),
   Span(doc39, 14, 15, label ="AMOUNT"),
   Span(doc39, 16, 17, label ="ARTICLE"),
   Span(doc39, 17, 18, label ="PRICE"),
   Span(doc39, 18, 19, label ="UNIT"),
   Span(doc39, 20, 21, label ="SUMMA"),
   Span(doc39, 48, 49, label ="TARIFF"),
   Span(doc39, 53, 55, label ="COUNTRY"),
   Span(doc39, 59, 60, label ="PR_SURCH"),
   Span(doc39, 61, 62, label ="SURCHARGE"),
   Span(doc39, 62, 63, label ="TOTAL")]
docs.append(doc39)
print("doc40, 56, #NORDER 2403220; CONTRACT SR-1-06; CONTRACT1 75; POS 6000; AMOUNT 4; ARTICLE 1710001561; PRICE 4,65; UNIT 1; SUMMA 18,60; TARIFF 73079100; COUNTRY China; PR_SURCH 15,50; SURCHARGE 2,88; TOTAL 21,48; ")
doc40 = nlp('''Order number: 2403220 Purchase order number: N SR-1-06 75   6000 4 PC 1710001561 4,65 1 PC 18,60 DB-FL-304-M-B-W66-K packed per each item Export - Customs tariff no.: 73079100 Country of origin: China Material Surcharge 15,50 % 2,88 21,48''')
doc40.ents = [
   Span(doc40, 3, 4, label ="NORDER"),
   Span(doc40, 9, 12, label ="CONTRACT"),
   Span(doc40, 12, 13, label ="CONTRACT1"),
   Span(doc40, 14, 15, label ="POS"),
   Span(doc40, 15, 16, label ="AMOUNT"),
   Span(doc40, 17, 18, label ="ARTICLE"),
   Span(doc40, 18, 19, label ="PRICE"),
   Span(doc40, 19, 20, label ="UNIT"),
   Span(doc40, 21, 22, label ="SUMMA"),
   Span(doc40, 44, 45, label ="TARIFF"),
   Span(doc40, 49, 50, label ="COUNTRY"),
   Span(doc40, 52, 53, label ="PR_SURCH"),
   Span(doc40, 54, 55, label ="SURCHARGE"),
   Span(doc40, 55, 56, label ="TOTAL")]
docs.append(doc40)
print("doc41, 54, #NORDER 2405196; CONTRACT SR-1-06; CONTRACT1 85; POS 6100; AMOUNT 175; ARTICLE 1130005391; PRICE 36,71; UNIT 100; SUMMA 64,24; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 7,32; TOTAL 71,56; ")
doc41 = nlp('''Order number: 2405196 Purchase order number: N SR-1-06 85 6100 175 PC 1130005391 36,71 100 PC 64,24 218-SA 218 SA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 7,32 71,56''')
doc41.ents = [
   Span(doc41, 3, 4, label ="NORDER"),
   Span(doc41, 9, 12, label ="CONTRACT"),
   Span(doc41, 12, 13, label ="CONTRACT1"),
   Span(doc41, 13, 14, label ="POS"),
   Span(doc41, 14, 15, label ="AMOUNT"),
   Span(doc41, 16, 17, label ="ARTICLE"),
   Span(doc41, 17, 18, label ="PRICE"),
   Span(doc41, 18, 19, label ="UNIT"),
   Span(doc41, 20, 21, label ="SUMMA"),
   Span(doc41, 42, 43, label ="TARIFF"),
   Span(doc41, 47, 48, label ="COUNTRY"),
   Span(doc41, 50, 51, label ="PR_SURCH"),
   Span(doc41, 52, 53, label ="SURCHARGE"),
   Span(doc41, 53, 54, label ="TOTAL")]
docs.append(doc41)
print("doc42, 54, #NORDER 2405196; CONTRACT SR-1-06; CONTRACT1 85; POS 6200; AMOUNT 4; ARTICLE 1130003125; PRICE 368,39; UNIT 100; SUMMA 14,74; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 1,68; TOTAL 16,42; ")
doc42 = nlp('''Order number: 2405196 Purchase order number: N SR-1-06 85 6200 4 PC 1130003125 368,39 100 PC 14,74 6048.3-PA 6048,3 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 1,68 16,42''')
doc42.ents = [
   Span(doc42, 3, 4, label ="NORDER"),
   Span(doc42, 9, 12, label ="CONTRACT"),
   Span(doc42, 12, 13, label ="CONTRACT1"),
   Span(doc42, 13, 14, label ="POS"),
   Span(doc42, 14, 15, label ="AMOUNT"),
   Span(doc42, 16, 17, label ="ARTICLE"),
   Span(doc42, 17, 18, label ="PRICE"),
   Span(doc42, 18, 19, label ="UNIT"),
   Span(doc42, 20, 21, label ="SUMMA"),
   Span(doc42, 42, 43, label ="TARIFF"),
   Span(doc42, 47, 48, label ="COUNTRY"),
   Span(doc42, 50, 51, label ="PR_SURCH"),
   Span(doc42, 52, 53, label ="SURCHARGE"),
   Span(doc42, 53, 54, label ="TOTAL")]
docs.append(doc42)
print("doc43, 55, #NORDER 2405196; CONTRACT SR-1-06; CONTRACT1 85; POS 6300; AMOUNT 4; ARTICLE 1130003135; PRICE 368,39; UNIT 100; SUMMA 14,74; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 1,68; TOTAL 16,42; ")
doc43 = nlp('''Order number: 2405196 Purchase order number: N SR-1-06 85 6300 4 PC 1130003135 368,39 100 PC 14,74 6060.3-PA    6060,3 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 1,68 16,42''')
doc43.ents = [
   Span(doc43, 3, 4, label ="NORDER"),
   Span(doc43, 9, 12, label ="CONTRACT"),
   Span(doc43, 12, 13, label ="CONTRACT1"),
   Span(doc43, 13, 14, label ="POS"),
   Span(doc43, 14, 15, label ="AMOUNT"),
   Span(doc43, 16, 17, label ="ARTICLE"),
   Span(doc43, 17, 18, label ="PRICE"),
   Span(doc43, 18, 19, label ="UNIT"),
   Span(doc43, 20, 21, label ="SUMMA"),
   Span(doc43, 43, 44, label ="TARIFF"),
   Span(doc43, 48, 49, label ="COUNTRY"),
   Span(doc43, 51, 52, label ="PR_SURCH"),
   Span(doc43, 53, 54, label ="SURCHARGE"),
   Span(doc43, 54, 55, label ="TOTAL")]
docs.append(doc43)
print("doc44, 54, #NORDER 2405196; CONTRACT SR-1-06; CONTRACT1 85; POS 6400; AMOUNT 25; ARTICLE 1130005583; PRICE 41,59; UNIT 100; SUMMA 10,40; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 1,19; TOTAL 11,59; ")
doc44 = nlp('''Order number: 2405196 Purchase order number: N SR-1-06 85 6400 25 PC 1130005583 41,59 100 PC 10,40 322-SA 322 SA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 1,19 11,59''')
doc44.ents = [
   Span(doc44, 3, 4, label ="NORDER"),
   Span(doc44, 9, 12, label ="CONTRACT"),
   Span(doc44, 12, 13, label ="CONTRACT1"),
   Span(doc44, 13, 14, label ="POS"),
   Span(doc44, 14, 15, label ="AMOUNT"),
   Span(doc44, 16, 17, label ="ARTICLE"),
   Span(doc44, 17, 18, label ="PRICE"),
   Span(doc44, 18, 19, label ="UNIT"),
   Span(doc44, 20, 21, label ="SUMMA"),
   Span(doc44, 42, 43, label ="TARIFF"),
   Span(doc44, 47, 48, label ="COUNTRY"),
   Span(doc44, 50, 51, label ="PR_SURCH"),
   Span(doc44, 52, 53, label ="SURCHARGE"),
   Span(doc44, 53, 54, label ="TOTAL")]
docs.append(doc44)
print("doc45, 56, #NORDER 2405196; CONTRACT SR-1-06; CONTRACT1 85; POS 6500; AMOUNT 725; ARTICLE 1130005358; PRICE 63,10; UNIT 100; SUMMA 457,48; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 52,15; TOTAL 509,63; ")
doc45 = nlp('''Order number: 2405196 Purchase order number: N SR-1-06 85 6500 725 PC 1130005358 63,10 100 PC 457,48 216/16-PA-H 216/16 PAH packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 52,15 509,63''')
doc45.ents = [
   Span(doc45, 3, 4, label ="NORDER"),
   Span(doc45, 9, 12, label ="CONTRACT"),
   Span(doc45, 12, 13, label ="CONTRACT1"),
   Span(doc45, 13, 14, label ="POS"),
   Span(doc45, 14, 15, label ="AMOUNT"),
   Span(doc45, 16, 17, label ="ARTICLE"),
   Span(doc45, 17, 18, label ="PRICE"),
   Span(doc45, 18, 19, label ="UNIT"),
   Span(doc45, 20, 21, label ="SUMMA"),
   Span(doc45, 44, 45, label ="TARIFF"),
   Span(doc45, 49, 50, label ="COUNTRY"),
   Span(doc45, 52, 53, label ="PR_SURCH"),
   Span(doc45, 54, 55, label ="SURCHARGE"),
   Span(doc45, 55, 56, label ="TOTAL")]
docs.append(doc45)
print("doc46, 54, #NORDER 2405196; CONTRACT SR-1-06; CONTRACT1 85; POS 6600; AMOUNT 2.400; ARTICLE 6030003814; PRICE 15,60; UNIT 100; SUMMA 374,40; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 25,83; TOTAL 400,23; ")
doc46 = nlp('''Order number: 2405196 Purchase order number: N SR-1-06 85 6600 2.400 PC 6030003814 15,60 100 PC 374,40 FI-M-12L-W3    packed per each item Product description: nuts Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 25,83 400,23''')
doc46.ents = [
   Span(doc46, 3, 4, label ="NORDER"),
   Span(doc46, 9, 12, label ="CONTRACT"),
   Span(doc46, 12, 13, label ="CONTRACT1"),
   Span(doc46, 13, 14, label ="POS"),
   Span(doc46, 14, 15, label ="AMOUNT"),
   Span(doc46, 16, 17, label ="ARTICLE"),
   Span(doc46, 17, 18, label ="PRICE"),
   Span(doc46, 18, 19, label ="UNIT"),
   Span(doc46, 20, 21, label ="SUMMA"),
   Span(doc46, 42, 43, label ="TARIFF"),
   Span(doc46, 47, 48, label ="COUNTRY"),
   Span(doc46, 50, 51, label ="PR_SURCH"),
   Span(doc46, 52, 53, label ="SURCHARGE"),
   Span(doc46, 53, 54, label ="TOTAL")]
docs.append(doc46)
print("doc47, 73, #NORDER 2405196; CONTRACT SR-1-06; CONTRACT1 85; POS 6700; AMOUNT 4; ARTICLE 1910000239; PRICE 6,13; UNIT 1; SUMMA 24,52; TARIFF 84213925; COUNTRY Italy; PR_SURCH 11,40; SURCHARGE 2,80; TOTAL 27,32; ")
doc47 = nlp('''Order number: 2405196 Purchase order number: N SR-1-06 85 6700 4 PC 1910000239 6,13 1 PC 24,52 SMBB-47-N-10-O0-C-S065 SMBB-47-N-10-O-C-S065-O packed per each item Product description: filter breather Export - Customs tariff no.: 84213925 Country of origin: Italy Material Surcharge 11,40 % 2,80 27,32 EAC - Eurasian Conformity''')
doc47.ents = [
   Span(doc47, 3, 4, label ="NORDER"),
   Span(doc47, 9, 12, label ="CONTRACT"),
   Span(doc47, 12, 13, label ="CONTRACT1"),
   Span(doc47, 13, 14, label ="POS"),
   Span(doc47, 14, 15, label ="AMOUNT"),
   Span(doc47, 16, 17, label ="ARTICLE"),
   Span(doc47, 17, 18, label ="PRICE"),
   Span(doc47, 18, 19, label ="UNIT"),
   Span(doc47, 20, 21, label ="SUMMA"),
   Span(doc47, 57, 58, label ="TARIFF"),
   Span(doc47, 62, 63, label ="COUNTRY"),
   Span(doc47, 65, 66, label ="PR_SURCH"),
   Span(doc47, 67, 68, label ="SURCHARGE"),
   Span(doc47, 68, 69, label ="TOTAL")]
docs.append(doc47)
print("doc48, 76, #NORDER 2405196; CONTRACT SR-1-06; CONTRACT1 85; POS 6800; AMOUNT 1; ARTICLE 6100075962; PRICE 20,65; UNIT 1; SUMMA 20,65; TARIFF 84812010; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 1,42; TOTAL 22,07; ")
doc48 = nlp('''Order number: 2405196 Purchase order number: N SR-1-06 85 6800 1 PC 6100075962 20,65 1 PC 20,65 BBV -2-G16-8001-M 2/2-Way Block Ball Valve DN25 G1-PN350, POM, FPM, ZiNi packed per each item Product description: valve Export - Customs tariff no.: 84812010 Country of origin: Germany Material Surcharge 6,90 % 1,42 22,07 EAC - Eurasian Conformity''')
doc48.ents = [
   Span(doc48, 3, 4, label ="NORDER"),
   Span(doc48, 9, 12, label ="CONTRACT"),
   Span(doc48, 12, 13, label ="CONTRACT1"),
   Span(doc48, 13, 14, label ="POS"),
   Span(doc48, 14, 15, label ="AMOUNT"),
   Span(doc48, 16, 17, label ="ARTICLE"),
   Span(doc48, 17, 18, label ="PRICE"),
   Span(doc48, 18, 19, label ="UNIT"),
   Span(doc48, 20, 21, label ="SUMMA"),
   Span(doc48, 60, 61, label ="TARIFF"),
   Span(doc48, 65, 66, label ="COUNTRY"),
   Span(doc48, 68, 69, label ="PR_SURCH"),
   Span(doc48, 70, 71, label ="SURCHARGE"),
   Span(doc48, 71, 72, label ="TOTAL")]
docs.append(doc48)
print("doc49, 67, #NORDER 2405196; CONTRACT SR-1-06; CONTRACT1 85; POS 6900; AMOUNT 4; ARTICLE 1910000427; PRICE 7,18; UNIT 1; SUMMA 28,72; TARIFF 84213925; COUNTRY Italy; PR_SURCH 11,40; SURCHARGE 3,27; TOTAL 31,99; ")
doc49 = nlp('''Order number: 2405196 Purchase order number: N SR-1-06 85   6900 4 PC 1910000427 7,18 1 PC 28,72 SMBB-80-S-O-40-O-C-S080-O packed per each item Product description: filter breather Export - Customs tariff no.: 84213925 Country of origin: Italy Material Surcharge 11,40 % 3,27 31,99 EAC - Eurasian Conformity''')
doc49.ents = [
   Span(doc49, 3, 4, label ="NORDER"),
   Span(doc49, 9, 12, label ="CONTRACT"),
   Span(doc49, 12, 13, label ="CONTRACT1"),
   Span(doc49, 14, 15, label ="POS"),
   Span(doc49, 15, 16, label ="AMOUNT"),
   Span(doc49, 17, 18, label ="ARTICLE"),
   Span(doc49, 18, 19, label ="PRICE"),
   Span(doc49, 19, 20, label ="UNIT"),
   Span(doc49, 21, 22, label ="SUMMA"),
   Span(doc49, 51, 52, label ="TARIFF"),
   Span(doc49, 56, 57, label ="COUNTRY"),
   Span(doc49, 59, 60, label ="PR_SURCH"),
   Span(doc49, 61, 62, label ="SURCHARGE"),
   Span(doc49, 62, 63, label ="TOTAL")]
docs.append(doc49)
print("doc50, 54, #NORDER 2405196; CONTRACT SR-1-06; CONTRACT1 85; POS 7000; AMOUNT 4; ARTICLE 1130005052; PRICE 2.383,00; UNIT 100; SUMMA 95,32; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 10,87; TOTAL 106,19; ")
doc50 = nlp('''Order number: 2405196 Purchase order number: N SR-1-06 85 7000 4 PC 1130005052 2.383,00 100 PC 95,32 10219-PP 10219 PP packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 10,87 106,19''')
doc50.ents = [
   Span(doc50, 3, 4, label ="NORDER"),
   Span(doc50, 9, 12, label ="CONTRACT"),
   Span(doc50, 12, 13, label ="CONTRACT1"),
   Span(doc50, 13, 14, label ="POS"),
   Span(doc50, 14, 15, label ="AMOUNT"),
   Span(doc50, 16, 17, label ="ARTICLE"),
   Span(doc50, 17, 18, label ="PRICE"),
   Span(doc50, 18, 19, label ="UNIT"),
   Span(doc50, 20, 21, label ="SUMMA"),
   Span(doc50, 42, 43, label ="TARIFF"),
   Span(doc50, 47, 48, label ="COUNTRY"),
   Span(doc50, 50, 51, label ="PR_SURCH"),
   Span(doc50, 52, 53, label ="SURCHARGE"),
   Span(doc50, 53, 54, label ="TOTAL")]
docs.append(doc50)
print("doc51, 53, #NORDER 2405198; CONTRACT SR-1-06; CONTRACT1 86; POS 7100; AMOUNT 250; ARTICLE 6030003815; PRICE 24,92; UNIT 100; SUMMA 62,30; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 4,30; TOTAL 66,60; ")
doc51 = nlp('''Order number: 2405198 Purchase order number: N SR-1-06 86 7100 250 PC 6030003815 24,92 100 PC 62,30 FI-M-15L-W3 packed per each item Product description: nuts Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 4,30 66,60''')
doc51.ents = [
   Span(doc51, 3, 4, label ="NORDER"),
   Span(doc51, 9, 12, label ="CONTRACT"),
   Span(doc51, 12, 13, label ="CONTRACT1"),
   Span(doc51, 13, 14, label ="POS"),
   Span(doc51, 14, 15, label ="AMOUNT"),
   Span(doc51, 16, 17, label ="ARTICLE"),
   Span(doc51, 17, 18, label ="PRICE"),
   Span(doc51, 18, 19, label ="UNIT"),
   Span(doc51, 20, 21, label ="SUMMA"),
   Span(doc51, 41, 42, label ="TARIFF"),
   Span(doc51, 46, 47, label ="COUNTRY"),
   Span(doc51, 49, 50, label ="PR_SURCH"),
   Span(doc51, 51, 52, label ="SURCHARGE"),
   Span(doc51, 52, 53, label ="TOTAL")]
docs.append(doc51)
print("doc52, 57, #NORDER 2405198; CONTRACT SR-1-06; CONTRACT1 86; POS 7200; AMOUNT 100; ARTICLE 6030005623; PRICE 69,19; UNIT 100; SUMMA 69,19; TARIFF 73181699; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 4,77; TOTAL 73,96; ")
doc52 = nlp('''Order number: 2405198 Purchase order number: N SR-1-06 86 7200 100 PC 6030005623 (*) 69,19 100 PC 69,19    FI-SKM-18L-W3 packed per each item Product description: nuts Export - Customs tariff no.: 73181699 Country of origin: Germany Material Surcharge 6,90 % 4,77 73,96''')
doc52.ents = [
   Span(doc52, 3, 4, label ="NORDER"),
   Span(doc52, 9, 12, label ="CONTRACT"),
   Span(doc52, 12, 13, label ="CONTRACT1"),
   Span(doc52, 13, 14, label ="POS"),
   Span(doc52, 14, 15, label ="AMOUNT"),
   Span(doc52, 16, 17, label ="ARTICLE"),
   Span(doc52, 20, 21, label ="PRICE"),
   Span(doc52, 21, 22, label ="UNIT"),
   Span(doc52, 23, 24, label ="SUMMA"),
   Span(doc52, 45, 46, label ="TARIFF"),
   Span(doc52, 50, 51, label ="COUNTRY"),
   Span(doc52, 53, 54, label ="PR_SURCH"),
   Span(doc52, 55, 56, label ="SURCHARGE"),
   Span(doc52, 56, 57, label ="TOTAL")]
docs.append(doc52)
print("doc53, 58, #NORDER 2405198; CONTRACT SR-1-06; CONTRACT1 86; POS 7300; AMOUNT 5.000; ARTICLE 6030004267; PRICE 9,31; UNIT 100; SUMMA 465,50; TARIFF 73269098; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 32,12; TOTAL 497,62; ")
doc53 = nlp('''Order number: 2405198 Purchase order number: N SR-1-06 86 7300 5.000 PC 6030004267 (*) 9,31 100 PC 465,50 FI-DS-06L/S-W3 packed per each item Product description: ring Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 6,90 % 32,12 497,62''')
doc53.ents = [
   Span(doc53, 3, 4, label ="NORDER"),
   Span(doc53, 9, 12, label ="CONTRACT"),
   Span(doc53, 12, 13, label ="CONTRACT1"),
   Span(doc53, 13, 14, label ="POS"),
   Span(doc53, 14, 15, label ="AMOUNT"),
   Span(doc53, 16, 17, label ="ARTICLE"),
   Span(doc53, 20, 21, label ="PRICE"),
   Span(doc53, 21, 22, label ="UNIT"),
   Span(doc53, 23, 24, label ="SUMMA"),
   Span(doc53, 46, 47, label ="TARIFF"),
   Span(doc53, 51, 52, label ="COUNTRY"),
   Span(doc53, 54, 55, label ="PR_SURCH"),
   Span(doc53, 56, 57, label ="SURCHARGE"),
   Span(doc53, 57, 58, label ="TOTAL")]
docs.append(doc53)
print("doc54, 55, #NORDER 2405198; CONTRACT SR-1-06; CONTRACT1 86; POS 7400; AMOUNT 120; ARTICLE 1230000376; PRICE 18,37; UNIT 100; SUMMA 22,04; TARIFF 40169300; COUNTRY China; PR_SURCH 6,90; SURCHARGE 1,52; TOTAL 23,56; ")
doc54 = nlp('''Order number: 2405198 Purchase order number: N SR-1-06 86 7400 120 PC 1230000376 18,37 100 PC 22,04 WDG-14.7x18.9x1.5-B90 WDG NBR-14,7x18,9x1,5-SH90 packed per each item Product description: seal Export - Customs tariff no.: 40169300 Country of origin: China Material Surcharge 6,90 % 1,52 23,56''')
doc54.ents = [
   Span(doc54, 3, 4, label ="NORDER"),
   Span(doc54, 9, 12, label ="CONTRACT"),
   Span(doc54, 12, 13, label ="CONTRACT1"),
   Span(doc54, 13, 14, label ="POS"),
   Span(doc54, 14, 15, label ="AMOUNT"),
   Span(doc54, 16, 17, label ="ARTICLE"),
   Span(doc54, 17, 18, label ="PRICE"),
   Span(doc54, 18, 19, label ="UNIT"),
   Span(doc54, 20, 21, label ="SUMMA"),
   Span(doc54, 43, 44, label ="TARIFF"),
   Span(doc54, 48, 49, label ="COUNTRY"),
   Span(doc54, 51, 52, label ="PR_SURCH"),
   Span(doc54, 53, 54, label ="SURCHARGE"),
   Span(doc54, 54, 55, label ="TOTAL")]
docs.append(doc54)
print("doc55, 60, #NORDER 2405198; CONTRACT SR-1-06; CONTRACT1 86; POS 7500; AMOUNT 35; ARTICLE 6010007172; PRICE 286,75; UNIT 100; SUMMA 100,36; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 6,92; TOTAL 107,28; ")
doc55 = nlp('''Order number: 2405198 Purchase order number: N SR-1-06 86 7500 35 PC 6010007172 (*) 286,75 100 PC 100,36 FI-REDS-1 8/06L-W3-SV packed per each item    Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 6,92 107,28''')
doc55.ents = [
   Span(doc55, 3, 4, label ="NORDER"),
   Span(doc55, 9, 12, label ="CONTRACT"),
   Span(doc55, 12, 13, label ="CONTRACT1"),
   Span(doc55, 13, 14, label ="POS"),
   Span(doc55, 14, 15, label ="AMOUNT"),
   Span(doc55, 16, 17, label ="ARTICLE"),
   Span(doc55, 20, 21, label ="PRICE"),
   Span(doc55, 21, 22, label ="UNIT"),
   Span(doc55, 23, 24, label ="SUMMA"),
   Span(doc55, 48, 49, label ="TARIFF"),
   Span(doc55, 53, 54, label ="COUNTRY"),
   Span(doc55, 56, 57, label ="PR_SURCH"),
   Span(doc55, 58, 59, label ="SURCHARGE"),
   Span(doc55, 59, 60, label ="TOTAL")]
docs.append(doc55)
print("doc56, 60, #NORDER 2405198; CONTRACT SR-1-06; CONTRACT1 86; POS 7600; AMOUNT 50; ARTICLE 6020000462; PRICE 104,39; UNIT 100; SUMMA 52,20; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 3,60; TOTAL 55,80; ")
doc56 = nlp('''Order number: 2405198 Purchase order number: N SR-1-06 86 7600 50 PC 6020000462 (*) 104,39 100 PC 52,20 FI-GE-12LR1/2-WD-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 3,60 55,80''')
doc56.ents = [
   Span(doc56, 3, 4, label ="NORDER"),
   Span(doc56, 9, 12, label ="CONTRACT"),
   Span(doc56, 12, 13, label ="CONTRACT1"),
   Span(doc56, 13, 14, label ="POS"),
   Span(doc56, 14, 15, label ="AMOUNT"),
   Span(doc56, 16, 17, label ="ARTICLE"),
   Span(doc56, 20, 21, label ="PRICE"),
   Span(doc56, 21, 22, label ="UNIT"),
   Span(doc56, 23, 24, label ="SUMMA"),
   Span(doc56, 48, 49, label ="TARIFF"),
   Span(doc56, 53, 54, label ="COUNTRY"),
   Span(doc56, 56, 57, label ="PR_SURCH"),
   Span(doc56, 58, 59, label ="SURCHARGE"),
   Span(doc56, 59, 60, label ="TOTAL")]
docs.append(doc56)
print("doc57, 60, #NORDER 2405198; CONTRACT SR-1-06; CONTRACT1 86; POS 7700; AMOUNT 150; ARTICLE 6020000509; PRICE 107,16; UNIT 100; SUMMA 160,74; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 11,09; TOTAL 171,83; ")
doc57 = nlp('''Order number: 2405198 Purchase order number: N SR-1-06 86 7700 150 PC 6020000509 (*) 107,16 100 PC 160,74 FI-GE-15LR3/8-WD-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 11,09 171,83''')
doc57.ents = [
   Span(doc57, 3, 4, label ="NORDER"),
   Span(doc57, 9, 12, label ="CONTRACT"),
   Span(doc57, 12, 13, label ="CONTRACT1"),
   Span(doc57, 13, 14, label ="POS"),
   Span(doc57, 14, 15, label ="AMOUNT"),
   Span(doc57, 16, 17, label ="ARTICLE"),
   Span(doc57, 20, 21, label ="PRICE"),
   Span(doc57, 21, 22, label ="UNIT"),
   Span(doc57, 23, 24, label ="SUMMA"),
   Span(doc57, 48, 49, label ="TARIFF"),
   Span(doc57, 53, 54, label ="COUNTRY"),
   Span(doc57, 56, 57, label ="PR_SURCH"),
   Span(doc57, 58, 59, label ="SURCHARGE"),
   Span(doc57, 59, 60, label ="TOTAL")]
docs.append(doc57)
print("doc58, 54, #NORDER 2405198; CONTRACT SR-1-06; CONTRACT1 86; POS 7800; AMOUNT 50; ARTICLE 6030003848; PRICE 256,32; UNIT 100; SUMMA 128,16; TARIFF 73079290; COUNTRY Germany   ; PR_SURCH 6,90; SURCHARGE 8,84; TOTAL 137,00; ")
doc58 = nlp('''Order number: 2405198 Purchase order number: N SR-1-06 86 7800 50 PC 6030003848 256,32 100 PC 128,16 FI-T-15L-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079290 Country of origin: Germany   Material Surcharge 6,90 % 8,84 137,00''')
doc58.ents = [
   Span(doc58, 3, 4, label ="NORDER"),
   Span(doc58, 9, 12, label ="CONTRACT"),
   Span(doc58, 12, 13, label ="CONTRACT1"),
   Span(doc58, 13, 14, label ="POS"),
   Span(doc58, 14, 15, label ="AMOUNT"),
   Span(doc58, 16, 17, label ="ARTICLE"),
   Span(doc58, 17, 18, label ="PRICE"),
   Span(doc58, 18, 19, label ="UNIT"),
   Span(doc58, 20, 21, label ="SUMMA"),
   Span(doc58, 41, 42, label ="TARIFF"),
   Span(doc58, 46, 48, label ="COUNTRY"),
   Span(doc58, 50, 51, label ="PR_SURCH"),
   Span(doc58, 52, 53, label ="SURCHARGE"),
   Span(doc58, 53, 54, label ="TOTAL")]
docs.append(doc58)
print("doc59, 59, #NORDER 2405206; CONTRACT SR-1-06; CONTRACT1 87; POS 7900; AMOUNT 20; ARTICLE 1130003971; PRICE 4,51; UNIT 100; SUMMA 0,90; TARIFF 73181568; COUNTRY Taiwan; PR_SURCH 11,40; SURCHARGE 0,10; TOTAL 1,00; ")
doc59 = nlp('''Order number: 2405206 Purchase order number: N SR-1-06 87 7900 20 PC 1130003971 4,51 100 PC 0,90 IS-M6X25-ISO4 762-8 .8-W3 packed per each item Product description: screw Export - Customs tariff no.: 73181568 Country of origin: Taiwan Material Surcharge 11,40 % 0,10 1,00''')
doc59.ents = [
   Span(doc59, 3, 4, label ="NORDER"),
   Span(doc59, 9, 12, label ="CONTRACT"),
   Span(doc59, 12, 13, label ="CONTRACT1"),
   Span(doc59, 13, 14, label ="POS"),
   Span(doc59, 14, 15, label ="AMOUNT"),
   Span(doc59, 16, 17, label ="ARTICLE"),
   Span(doc59, 17, 18, label ="PRICE"),
   Span(doc59, 18, 19, label ="UNIT"),
   Span(doc59, 20, 21, label ="SUMMA"),
   Span(doc59, 47, 48, label ="TARIFF"),
   Span(doc59, 52, 53, label ="COUNTRY"),
   Span(doc59, 55, 56, label ="PR_SURCH"),
   Span(doc59, 57, 58, label ="SURCHARGE"),
   Span(doc59, 58, 59, label ="TOTAL")]
docs.append(doc59)
print("doc60, 65, #NORDER 2405206; CONTRACT SR-1-06; CONTRACT1 87; POS 8000; AMOUNT 20; ARTICLE 6100152347; PRICE 12,73; UNIT 100; SUMMA 2,55; TARIFF 73181692; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,29; TOTAL 2,84; ")
doc60 = nlp('''Order number: 2405206 Purchase order number: N SR-1-06 87 8000 20 PC 6100152347 12,73, 100 PC 2,55 SM-1-8/1 D-M-W3/2 packed per each item Customer ID-No.: 000000001 120001932 Product description: nuts Export - Customs tariff no.: 73181692 Country of origin: Germany Material Surcharge 11,40 % 0,29 2,84''')
doc60.ents = [
   Span(doc60, 3, 4, label ="NORDER"),
   Span(doc60, 9, 12, label ="CONTRACT"),
   Span(doc60, 12, 13, label ="CONTRACT1"),
   Span(doc60, 13, 14, label ="POS"),
   Span(doc60, 14, 15, label ="AMOUNT"),
   Span(doc60, 16, 17, label ="ARTICLE"),
   Span(doc60, 17, 18, label ="PRICE"),
   Span(doc60, 19, 20, label ="UNIT"),
   Span(doc60, 21, 22, label ="SUMMA"),
   Span(doc60, 53, 54, label ="TARIFF"),
   Span(doc60, 58, 59, label ="COUNTRY"),
   Span(doc60, 61, 62, label ="PR_SURCH"),
   Span(doc60, 63, 64, label ="SURCHARGE"),
   Span(doc60, 64, 65, label ="TOTAL")]
docs.append(doc60)
print("doc61, 74, #NORDER 2405206; CONTRACT SR-1-06; CONTRACT1 87; POS 8100; AMOUNT 100; ARTICLE 6010001838; PRICE 94,35; UNIT 100; SUMMA 94,35; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 6,51; TOTAL 100,86; ")
doc61 = nlp('''Order number: 2405206 Purchase order number: N SR-1-06 87 8100 100 PC 6010001838 (*) 94,35 100 PC 94,35 FI-VS-M16x1.5-WD-B-W3 FI-VS-M16x1,5-WD-B-W3 packed per each item Product description: Plug Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 6,51    100,86''')
doc61.ents = [
   Span(doc61, 3, 4, label ="NORDER"),
   Span(doc61, 9, 12, label ="CONTRACT"),
   Span(doc61, 12, 13, label ="CONTRACT1"),
   Span(doc61, 13, 14, label ="POS"),
   Span(doc61, 14, 15, label ="AMOUNT"),
   Span(doc61, 16, 17, label ="ARTICLE"),
   Span(doc61, 20, 21, label ="PRICE"),
   Span(doc61, 21, 22, label ="UNIT"),
   Span(doc61, 23, 24, label ="SUMMA"),
   Span(doc61, 61, 62, label ="TARIFF"),
   Span(doc61, 66, 67, label ="COUNTRY"),
   Span(doc61, 69, 70, label ="PR_SURCH"),
   Span(doc61, 71, 72, label ="SURCHARGE"),
   Span(doc61, 73, 74, label ="TOTAL")]
docs.append(doc61)
print("doc62, 54, #NORDER 2405206; CONTRACT SR-1-06; CONTRACT1 87; POS 8200; AMOUNT 25; ARTICLE 1130003000; PRICE 18,37; UNIT 100; SUMMA 4,59; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,52; TOTAL 5,11; ")
doc62 = nlp('''Order number: 2405206 Purchase order number: N SR-1-06 87 8200 25 PC 1130003000 18,37 100 PC 4,59 112-PP 112 PP packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 0,52 5,11''')
doc62.ents = [
   Span(doc62, 3, 4, label ="NORDER"),
   Span(doc62, 9, 12, label ="CONTRACT"),
   Span(doc62, 12, 13, label ="CONTRACT1"),
   Span(doc62, 13, 14, label ="POS"),
   Span(doc62, 14, 15, label ="AMOUNT"),
   Span(doc62, 16, 17, label ="ARTICLE"),
   Span(doc62, 17, 18, label ="PRICE"),
   Span(doc62, 18, 19, label ="UNIT"),
   Span(doc62, 20, 21, label ="SUMMA"),
   Span(doc62, 42, 43, label ="TARIFF"),
   Span(doc62, 47, 48, label ="COUNTRY"),
   Span(doc62, 50, 51, label ="PR_SURCH"),
   Span(doc62, 52, 53, label ="SURCHARGE"),
   Span(doc62, 53, 54, label ="TOTAL")]
docs.append(doc62)
print("doc63, 71, #NORDER 2405206; CONTRACT SR-1-06; CONTRACT1 87; POS 8300; AMOUNT 100; ARTICLE 6020000403; PRICE 204,26; UNIT 100; SUMMA 204,26; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 14,09; TOTAL 218,35; ")
doc63 = nlp('''Order number: 2405206 Purchase order number: N SR-1-06 87 8300 100 PC 6020000403 (*) 204,26 100 PC 204,26 FI-GE-12LM14x1.5-WD-B-W3 FI-GE-12LM14x1 ,5-WD-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 14,09 218,35''')
doc63.ents = [
   Span(doc63, 3, 4, label ="NORDER"),
   Span(doc63, 9, 12, label ="CONTRACT"),
   Span(doc63, 12, 13, label ="CONTRACT1"),
   Span(doc63, 13, 14, label ="POS"),
   Span(doc63, 14, 15, label ="AMOUNT"),
   Span(doc63, 16, 17, label ="ARTICLE"),
   Span(doc63, 20, 21, label ="PRICE"),
   Span(doc63, 21, 22, label ="UNIT"),
   Span(doc63, 23, 24, label ="SUMMA"),
   Span(doc63, 59, 60, label ="TARIFF"),
   Span(doc63, 64, 65, label ="COUNTRY"),
   Span(doc63, 67, 68, label ="PR_SURCH"),
   Span(doc63, 69, 70, label ="SURCHARGE"),
   Span(doc63, 70, 71, label ="TOTAL")]
docs.append(doc63)
print("doc64, 54, #NORDER 2405206; CONTRACT SR-1-06; CONTRACT1 87; POS 8400; AMOUNT 100; ARTICLE 1130002821; PRICE 1,56; UNIT 100; SUMMA 1,56; TARIFF 73182200; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,18; TOTAL 1,74; ")
doc64 = nlp('''Order number: 2405206 Purchase order number: N SR-1-06 87 8400 100 PC 1130002821 1,56 100 PC 1,56 US-W3 US W3 packed per each item Product description: washer Export - Customs tariff no.: 73182200 Country of origin: Germany Material Surcharge 11,40 % 0,18   1,74''')
doc64.ents = [
   Span(doc64, 3, 4, label ="NORDER"),
   Span(doc64, 9, 12, label ="CONTRACT"),
   Span(doc64, 12, 13, label ="CONTRACT1"),
   Span(doc64, 13, 14, label ="POS"),
   Span(doc64, 14, 15, label ="AMOUNT"),
   Span(doc64, 16, 17, label ="ARTICLE"),
   Span(doc64, 17, 18, label ="PRICE"),
   Span(doc64, 18, 19, label ="UNIT"),
   Span(doc64, 20, 21, label ="SUMMA"),
   Span(doc64, 41, 42, label ="TARIFF"),
   Span(doc64, 46, 47, label ="COUNTRY"),
   Span(doc64, 49, 50, label ="PR_SURCH"),
   Span(doc64, 51, 52, label ="SURCHARGE"),
   Span(doc64, 53, 54, label ="TOTAL")]
docs.append(doc64)
print("doc65, 59, #NORDER 2406835; CONTRACT SR-1-06; CONTRACT1 88; POS 8500; AMOUNT 2; ARTICLE 1020024123; PRICE 47,93; UNIT 1; SUMMA 95,86; TARIFF 84219990; COUNTRY Germany; PR_SURCH 8,90; SURCHARGE 8,53; TOTAL 104,39; ")
doc65 = nlp('''Order number: 2406835 Purchase order number: N SR-1-06 88 8500 2 PC 1020024123 47,93 1 PC 95,86 SP-030-E-03-B/4 SP-030E03B/4 packed per each item Product description: filter element Export - Customs tariff no.: 84219990 Country of origin: Germany Material Surcharge 8,90 % 8,53 104,39 EAC - Eurasian Conformity''')
doc65.ents = [
   Span(doc65, 3, 4, label ="NORDER"),
   Span(doc65, 9, 12, label ="CONTRACT"),
   Span(doc65, 12, 13, label ="CONTRACT1"),
   Span(doc65, 13, 14, label ="POS"),
   Span(doc65, 14, 15, label ="AMOUNT"),
   Span(doc65, 16, 17, label ="ARTICLE"),
   Span(doc65, 17, 18, label ="PRICE"),
   Span(doc65, 18, 19, label ="UNIT"),
   Span(doc65, 20, 21, label ="SUMMA"),
   Span(doc65, 43, 44, label ="TARIFF"),
   Span(doc65, 48, 49, label ="COUNTRY"),
   Span(doc65, 51, 52, label ="PR_SURCH"),
   Span(doc65, 53, 54, label ="SURCHARGE"),
   Span(doc65, 54, 55, label ="TOTAL")]
docs.append(doc65)
print("doc66, 76, #NORDER 2406845; CONTRACT SR-1-06; CONTRACT1 89; POS 8600; AMOUNT 4; ARTICLE 6100075962; PRICE 20,65; UNIT 1; SUMMA 82,60; TARIFF 84812010; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 5,70; TOTAL 88,30; ")
doc66 = nlp('''Order number: 2406845 Purchase order number: N SR-1-06 89 8600 4 PC 6100075962 20,65 1 PC 82,60 BBV -2-G16-8001-M 2/2-Way Block Ball Valve DN25 G1-PN350, POM, FPM, ZiNi packed per each item Product description: valve Export - Customs tariff no.: 84812010 Country of origin: Germany Material Surcharge 6,90 % 5,70 88,30 EAC - Eurasian Conformity''')
doc66.ents = [
   Span(doc66, 3, 4, label ="NORDER"),
   Span(doc66, 9, 12, label ="CONTRACT"),
   Span(doc66, 12, 13, label ="CONTRACT1"),
   Span(doc66, 13, 14, label ="POS"),
   Span(doc66, 14, 15, label ="AMOUNT"),
   Span(doc66, 16, 17, label ="ARTICLE"),
   Span(doc66, 17, 18, label ="PRICE"),
   Span(doc66, 18, 19, label ="UNIT"),
   Span(doc66, 20, 21, label ="SUMMA"),
   Span(doc66, 60, 61, label ="TARIFF"),
   Span(doc66, 65, 66, label ="COUNTRY"),
   Span(doc66, 68, 69, label ="PR_SURCH"),
   Span(doc66, 70, 71, label ="SURCHARGE"),
   Span(doc66, 71, 72, label ="TOTAL")]
docs.append(doc66)
print("doc67, 62, #NORDER 2406879; CONTRACT SR-1-06; CONTRACT1 91; POS 8700; AMOUNT 100; ARTICLE 1120003536; PRICE 15,03; UNIT 100; SUMMA 15,03; TARIFF 73181588; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 1,71; TOTAL 16,74; ")
doc67 = nlp('''Order number: 2406879 Purchase order number: N SR-1-06 91 8700 100 PC 1120003536 (*) 15,03 100 PC 15,03 AF-2-M-W3 AF 2 M W3 M6x25 packed per each item Product description: screw Export - Customs tariff no.: 73181588    Country of origin: Germany Material Surcharge 11,40 % 1,71 16,74''')
doc67.ents = [
   Span(doc67, 3, 4, label ="NORDER"),
   Span(doc67, 9, 12, label ="CONTRACT"),
   Span(doc67, 12, 13, label ="CONTRACT1"),
   Span(doc67, 13, 14, label ="POS"),
   Span(doc67, 14, 15, label ="AMOUNT"),
   Span(doc67, 16, 17, label ="ARTICLE"),
   Span(doc67, 20, 21, label ="PRICE"),
   Span(doc67, 21, 22, label ="UNIT"),
   Span(doc67, 23, 24, label ="SUMMA"),
   Span(doc67, 49, 50, label ="TARIFF"),
   Span(doc67, 55, 56, label ="COUNTRY"),
   Span(doc67, 58, 59, label ="PR_SURCH"),
   Span(doc67, 60, 61, label ="SURCHARGE"),
   Span(doc67, 61, 62, label ="TOTAL")]
docs.append(doc67)
print("doc68, 67, #NORDER 2406879; CONTRACT SR-1-06; CONTRACT1 91; POS 8800; AMOUNT 450; ARTICLE 1130004021; PRICE 4,09; UNIT 100; SUMMA 18,41; TARIFF 73181588; COUNTRY Origin unknown; PR_SURCH 11,40; SURCHARGE 2,10; TOTAL 20,51; ")
doc68 = nlp('''Order number: 2406879 Purchase order number: N SR-1-06 91 8800 450 PC 1130004021 4,09 100 PC 18,41 AS-M6x35-DIN931/933-8.8-W3 AS-M6X35-DIN931/933-8.8-W3 packed per each item Product description: screw Export - Customs tariff no.: 73181588 Country of origin: Origin unknown Material Surcharge 11,40 % 2,10 20,51''')
doc68.ents = [
   Span(doc68, 3, 4, label ="NORDER"),
   Span(doc68, 9, 12, label ="CONTRACT"),
   Span(doc68, 12, 13, label ="CONTRACT1"),
   Span(doc68, 13, 14, label ="POS"),
   Span(doc68, 14, 15, label ="AMOUNT"),
   Span(doc68, 16, 17, label ="ARTICLE"),
   Span(doc68, 17, 18, label ="PRICE"),
   Span(doc68, 18, 19, label ="UNIT"),
   Span(doc68, 20, 21, label ="SUMMA"),
   Span(doc68, 54, 55, label ="TARIFF"),
   Span(doc68, 59, 61, label ="COUNTRY"),
   Span(doc68, 63, 64, label ="PR_SURCH"),
   Span(doc68, 65, 66, label ="SURCHARGE"),
   Span(doc68, 66, 67, label ="TOTAL")]
docs.append(doc68)
print("doc69, 67, #NORDER 2406879; CONTRACT SR-1-06; CONTRACT1 91; POS 8900; AMOUNT 50; ARTICLE 1130004023; PRICE 4,51; UNIT 100; SUMMA 2,26; TARIFF 73181588; COUNTRY Origin unknown; PR_SURCH 11,40; SURCHARGE 0,26; TOTAL 2,52; ")
doc69 = nlp('''Order number: 2406879 Purchase order number: N SR-1-06 91 8900 50 PC 1130004023 4,51 100 PC 2,26 AS-M6x45-DIN931/933-8.8-W3 AS-M6X45-DIN931/933-8.8-W3 packed per each item Product description: screw Export - Customs tariff no.: 73181588 Country of origin: Origin unknown Material Surcharge 11,40 % 0,26 2,52''')
doc69.ents = [
   Span(doc69, 3, 4, label ="NORDER"),
   Span(doc69, 9, 12, label ="CONTRACT"),
   Span(doc69, 12, 13, label ="CONTRACT1"),
   Span(doc69, 13, 14, label ="POS"),
   Span(doc69, 14, 15, label ="AMOUNT"),
   Span(doc69, 16, 17, label ="ARTICLE"),
   Span(doc69, 17, 18, label ="PRICE"),
   Span(doc69, 18, 19, label ="UNIT"),
   Span(doc69, 20, 21, label ="SUMMA"),
   Span(doc69, 54, 55, label ="TARIFF"),
   Span(doc69, 59, 61, label ="COUNTRY"),
   Span(doc69, 63, 64, label ="PR_SURCH"),
   Span(doc69, 65, 66, label ="SURCHARGE"),
   Span(doc69, 66, 67, label ="TOTAL")]
docs.append(doc69)
print("doc70, 68, #NORDER 2406879; CONTRACT SR-1-06; CONTRACT1 91; POS 9000; AMOUNT 50; ARTICLE 1130004024; PRICE 5,48; UNIT 100; SUMMA 2,74; TARIFF 73181588; COUNTRY Origin unknown; PR_SURCH 11,40; SURCHARGE 0,31; TOTAL 3,05; ")
doc70 = nlp('''Order number: 2406879 Purchase order number: N SR-1-06 91 9000 50 PC 1130004024 5,48 100 PC 2,74 AS-M6x60-DIN931/933-8.8-W3 AS-M6X60-DIN931/933-8.8-W3 packed per each item Product description: screw Export - Customs tariff no.: 73181588    Country of origin: Origin unknown Material Surcharge 11,40 % 0,31 3,05''')
doc70.ents = [
   Span(doc70, 3, 4, label ="NORDER"),
   Span(doc70, 9, 12, label ="CONTRACT"),
   Span(doc70, 12, 13, label ="CONTRACT1"),
   Span(doc70, 13, 14, label ="POS"),
   Span(doc70, 14, 15, label ="AMOUNT"),
   Span(doc70, 16, 17, label ="ARTICLE"),
   Span(doc70, 17, 18, label ="PRICE"),
   Span(doc70, 18, 19, label ="UNIT"),
   Span(doc70, 20, 21, label ="SUMMA"),
   Span(doc70, 54, 55, label ="TARIFF"),
   Span(doc70, 60, 62, label ="COUNTRY"),
   Span(doc70, 64, 65, label ="PR_SURCH"),
   Span(doc70, 66, 67, label ="SURCHARGE"),
   Span(doc70, 67, 68, label ="TOTAL")]
docs.append(doc70)
print("doc71, 54, #NORDER 2406879; CONTRACT SR-1-06; CONTRACT1 91; POS 9100; AMOUNT 275; ARTICLE 1130005272; PRICE 36,71; UNIT 100; SUMMA 100,95; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 11,51; TOTAL 112,46; ")
doc71 = nlp('''Order number: 2406879 Purchase order number: N SR-1-06 91 9100 275 PC 1130005272 36,71 100 PC 100,95 214-PA 214 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 11,51 112,46''')
doc71.ents = [
   Span(doc71, 3, 4, label ="NORDER"),
   Span(doc71, 9, 12, label ="CONTRACT"),
   Span(doc71, 12, 13, label ="CONTRACT1"),
   Span(doc71, 13, 14, label ="POS"),
   Span(doc71, 14, 15, label ="AMOUNT"),
   Span(doc71, 16, 17, label ="ARTICLE"),
   Span(doc71, 17, 18, label ="PRICE"),
   Span(doc71, 18, 19, label ="UNIT"),
   Span(doc71, 20, 21, label ="SUMMA"),
   Span(doc71, 42, 43, label ="TARIFF"),
   Span(doc71, 47, 48, label ="COUNTRY"),
   Span(doc71, 50, 51, label ="PR_SURCH"),
   Span(doc71, 52, 53, label ="SURCHARGE"),
   Span(doc71, 53, 54, label ="TOTAL")]
docs.append(doc71)
print("doc72, 54, #NORDER 2406879; CONTRACT SR-1-06; CONTRACT1 91; POS 9200; AMOUNT 25; ARTICLE 1130003772; PRICE 55,26; UNIT 100; SUMMA 13,82; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 1,58; TOTAL 15,40; ")
doc72 = nlp('''Order number: 2406879 Purchase order number: N SR-1-06 91 9200 25 PC 1130003772 55,26 100 PC 13,82 430-PA 430 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 1,58 15,40''')
doc72.ents = [
   Span(doc72, 3, 4, label ="NORDER"),
   Span(doc72, 9, 12, label ="CONTRACT"),
   Span(doc72, 12, 13, label ="CONTRACT1"),
   Span(doc72, 13, 14, label ="POS"),
   Span(doc72, 14, 15, label ="AMOUNT"),
   Span(doc72, 16, 17, label ="ARTICLE"),
   Span(doc72, 17, 18, label ="PRICE"),
   Span(doc72, 18, 19, label ="UNIT"),
   Span(doc72, 20, 21, label ="SUMMA"),
   Span(doc72, 42, 43, label ="TARIFF"),
   Span(doc72, 47, 48, label ="COUNTRY"),
   Span(doc72, 50, 51, label ="PR_SURCH"),
   Span(doc72, 52, 53, label ="SURCHARGE"),
   Span(doc72, 53, 54, label ="TOTAL")]
docs.append(doc72)
print("doc73, 55, #NORDER 2406879; CONTRACT SR-1-06; CONTRACT1 91; POS 9300; AMOUNT 25; ARTICLE 1130006023; PRICE 85,35; UNIT 100; SUMMA 21,34; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 2,43; TOTAL 23,77; ")
doc73 = nlp('''Order number: 2406879 Purchase order number: N SR-1-06 91 9300 25 PC 1130006023 85,35 100 PC 21,34 538-PA 538 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097    Country of origin: Germany Material Surcharge 11,40 % 2,43 23,77''')
doc73.ents = [
   Span(doc73, 3, 4, label ="NORDER"),
   Span(doc73, 9, 12, label ="CONTRACT"),
   Span(doc73, 12, 13, label ="CONTRACT1"),
   Span(doc73, 13, 14, label ="POS"),
   Span(doc73, 14, 15, label ="AMOUNT"),
   Span(doc73, 16, 17, label ="ARTICLE"),
   Span(doc73, 17, 18, label ="PRICE"),
   Span(doc73, 18, 19, label ="UNIT"),
   Span(doc73, 20, 21, label ="SUMMA"),
   Span(doc73, 42, 43, label ="TARIFF"),
   Span(doc73, 48, 49, label ="COUNTRY"),
   Span(doc73, 51, 52, label ="PR_SURCH"),
   Span(doc73, 53, 54, label ="SURCHARGE"),
   Span(doc73, 54, 55, label ="TOTAL")]
docs.append(doc73)
print("doc74, 55, #NORDER 2406879; CONTRACT SR-1-06; CONTRACT1 91; POS 9400; AMOUNT 125; ARTICLE 1130000261; PRICE 7,39; UNIT 100; SUMMA 9,24; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 1,05; TOTAL 10,29; ")
doc74 = nlp('''Order number: 2406879 Purchase order number: N SR-1-06 91 9400 125 PC 1130000261 7,39 100 PC 9,24 DP-2-W3 DP 2 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 1,05 10,29''')
doc74.ents = [
   Span(doc74, 3, 4, label ="NORDER"),
   Span(doc74, 9, 12, label ="CONTRACT"),
   Span(doc74, 12, 13, label ="CONTRACT1"),
   Span(doc74, 13, 14, label ="POS"),
   Span(doc74, 14, 15, label ="AMOUNT"),
   Span(doc74, 16, 17, label ="ARTICLE"),
   Span(doc74, 17, 18, label ="PRICE"),
   Span(doc74, 18, 19, label ="UNIT"),
   Span(doc74, 20, 21, label ="SUMMA"),
   Span(doc74, 43, 44, label ="TARIFF"),
   Span(doc74, 48, 49, label ="COUNTRY"),
   Span(doc74, 51, 52, label ="PR_SURCH"),
   Span(doc74, 53, 54, label ="SURCHARGE"),
   Span(doc74, 54, 55, label ="TOTAL")]
docs.append(doc74)
print("doc75, 58, #NORDER 2406879; CONTRACT SR-1-06; CONTRACT1 91; POS 9500; AMOUNT 250; ARTICLE 1120001156; PRICE 26,58; UNIT 100; SUMMA 66,45; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 7,58; TOTAL 74,03; ")
doc75 = nlp('''Order number: 2406879 Purchase order number: N SR-1-06 91 9500 250 PC 1120001156 26,58 100 PC 66,45 SP-2-M-W2 SP 2 M W2 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 7,58 74,03''')
doc75.ents = [
   Span(doc75, 3, 4, label ="NORDER"),
   Span(doc75, 9, 12, label ="CONTRACT"),
   Span(doc75, 12, 13, label ="CONTRACT1"),
   Span(doc75, 13, 14, label ="POS"),
   Span(doc75, 14, 15, label ="AMOUNT"),
   Span(doc75, 16, 17, label ="ARTICLE"),
   Span(doc75, 17, 18, label ="PRICE"),
   Span(doc75, 18, 19, label ="UNIT"),
   Span(doc75, 20, 21, label ="SUMMA"),
   Span(doc75, 46, 47, label ="TARIFF"),
   Span(doc75, 51, 52, label ="COUNTRY"),
   Span(doc75, 54, 55, label ="PR_SURCH"),
   Span(doc75, 56, 57, label ="SURCHARGE"),
   Span(doc75, 57, 58, label ="TOTAL")]
docs.append(doc75)
print("doc76, 61, #NORDER 2406882; CONTRACT SR-1-06; CONTRACT1 92; POS 9600; AMOUNT 115; ARTICLE 1910000225; PRICE 4,40; UNIT 1; SUMMA 506,00; TARIFF 84213925; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 57,68; TOTAL 563,68; ")
doc76 = nlp('''Order number: 2406882 Purchase order number: N SR-1-06 92 9600 115 PC 1910000225 (*) 4,40 1 PC 506,00 SES-2-O SES 2 packed per each item Product description: lug Export - Customs tariff no.: 84213925    Country of origin: Germany Material Surcharge 11,40 % 57,68 563,68 EAC - Eurasian Conformity''')
doc76.ents = [
   Span(doc76, 3, 4, label ="NORDER"),
   Span(doc76, 9, 12, label ="CONTRACT"),
   Span(doc76, 12, 13, label ="CONTRACT1"),
   Span(doc76, 13, 14, label ="POS"),
   Span(doc76, 14, 15, label ="AMOUNT"),
   Span(doc76, 16, 17, label ="ARTICLE"),
   Span(doc76, 20, 21, label ="PRICE"),
   Span(doc76, 21, 22, label ="UNIT"),
   Span(doc76, 23, 24, label ="SUMMA"),
   Span(doc76, 44, 45, label ="TARIFF"),
   Span(doc76, 50, 51, label ="COUNTRY"),
   Span(doc76, 53, 54, label ="PR_SURCH"),
   Span(doc76, 55, 56, label ="SURCHARGE"),
   Span(doc76, 56, 57, label ="TOTAL")]
docs.append(doc76)
print("doc77, 68, #NORDER 2406890; CONTRACT SR-1-06; CONTRACT1 93; POS 9700; AMOUNT 6; ARTICLE 1130004020; PRICE 3,93; UNIT 100; SUMMA 0,24; TARIFF 73181588; COUNTRY Origin unknown; PR_SURCH 11,40; SURCHARGE 0,03; TOTAL 0,27; ")
doc77 = nlp('''Order number: 2406890 Purchase order number: N SR-1-06 93 9700 6 PC 1130004020 3,93. 100 PC 0,24 AS-M6x30-DIN931/933-8.8-W3 AS-M6X30-DIN931/933-8.8-W3 packed per each item Product description: screw Export - Customs tariff no.: 73181588 Country of origin: Origin unknown Material Surcharge 11,40 % 0,03 0,27''')
doc77.ents = [
   Span(doc77, 3, 4, label ="NORDER"),
   Span(doc77, 9, 12, label ="CONTRACT"),
   Span(doc77, 12, 13, label ="CONTRACT1"),
   Span(doc77, 13, 14, label ="POS"),
   Span(doc77, 14, 15, label ="AMOUNT"),
   Span(doc77, 16, 17, label ="ARTICLE"),
   Span(doc77, 17, 18, label ="PRICE"),
   Span(doc77, 19, 20, label ="UNIT"),
   Span(doc77, 21, 22, label ="SUMMA"),
   Span(doc77, 55, 56, label ="TARIFF"),
   Span(doc77, 60, 62, label ="COUNTRY"),
   Span(doc77, 64, 65, label ="PR_SURCH"),
   Span(doc77, 66, 67, label ="SURCHARGE"),
   Span(doc77, 67, 68, label ="TOTAL")]
docs.append(doc77)
print("doc78, 68, #NORDER 2406891; CONTRACT SR-1-06; CONTRACT1 94; POS 9800; AMOUNT 12; ARTICLE 1210026005; PRICE 5,29; UNIT 1; SUMMA 63,48; TARIFF 84812010; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 7,24; TOTAL 70,72; ")
doc78 = nlp('''Order number: 2406891 Purchase order number: N SR-1-06 94 9800 12 PC 1210026005 (*) 5,29 1 PC 63,48 SKK-1 2-G1/4-B-C-W3 SKK12-G1/4-PC-C6F packed per each item Product description: coupling Export - Customs tariff no.: 84812010 Country of origin: Germany Material Surcharge 11,40 % 7,24 70,72''')
doc78.ents = [
   Span(doc78, 3, 4, label ="NORDER"),
   Span(doc78, 9, 12, label ="CONTRACT"),
   Span(doc78, 12, 13, label ="CONTRACT1"),
   Span(doc78, 13, 14, label ="POS"),
   Span(doc78, 14, 15, label ="AMOUNT"),
   Span(doc78, 16, 17, label ="ARTICLE"),
   Span(doc78, 20, 21, label ="PRICE"),
   Span(doc78, 21, 22, label ="UNIT"),
   Span(doc78, 23, 24, label ="SUMMA"),
   Span(doc78, 56, 57, label ="TARIFF"),
   Span(doc78, 61, 62, label ="COUNTRY"),
   Span(doc78, 64, 65, label ="PR_SURCH"),
   Span(doc78, 66, 67, label ="SURCHARGE"),
   Span(doc78, 67, 68, label ="TOTAL")]
docs.append(doc78)
print("doc79, 65, #NORDER 2406895; CONTRACT SR-1-06; CONTRACT1 95; POS 9900; AMOUNT 1; ARTICLE 2012031323; PRICE 0,51; UNIT 1; SUMMA 0,51; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 0,04; TOTAL 0,55; ")
doc79 = nlp('''Order number: 2406895 Purchase order number: N SR-1-06 95 9900 1 PC 2012031323 (*) 0,51 1 PC 0,51 HCS-10-DKR-06-S-M-W3 11501N10-DKR-DN10-3/8# packed per each item Export - Customs tariff no.: 73079910    Country of origin: Germany Material Surcharge 6,90 % 0,04 0,55''')
doc79.ents = [
   Span(doc79, 3, 4, label ="NORDER"),
   Span(doc79, 9, 12, label ="CONTRACT"),
   Span(doc79, 12, 13, label ="CONTRACT1"),
   Span(doc79, 13, 14, label ="POS"),
   Span(doc79, 14, 15, label ="AMOUNT"),
   Span(doc79, 16, 17, label ="ARTICLE"),
   Span(doc79, 20, 21, label ="PRICE"),
   Span(doc79, 21, 22, label ="UNIT"),
   Span(doc79, 23, 24, label ="SUMMA"),
   Span(doc79, 52, 53, label ="TARIFF"),
   Span(doc79, 58, 59, label ="COUNTRY"),
   Span(doc79, 61, 62, label ="PR_SURCH"),
   Span(doc79, 63, 64, label ="SURCHARGE"),
   Span(doc79, 64, 65, label ="TOTAL")]
docs.append(doc79)
print("doc80, 66, #NORDER 2407326; CONTRACT SR-1-06; CONTRACT1 97; POS 10000; AMOUNT 12; ARTICLE 1130004180; PRICE 8,38; UNIT 100; SUMMA 1,01; TARIFF 73181588; COUNTRY Thailand; PR_SURCH 11,40; SURCHARGE 0,12; TOTAL 1,13; ")
doc80 = nlp('''Order number: 2407326 Purchase order number: N SR-1-06 97 10000 12 PC 1130004180 8,38 100 PC 1,01 AS-M10x45-DIN931/933-8.8-W1 AS-M10X45-DIN931/933-8.8-W1 packed per each item Product description: screw Export - Customs tariff no.: 73181588 Country of origin: Thailand Material Surcharge 11,40 % 0,12 1,13''')
doc80.ents = [
   Span(doc80, 3, 4, label ="NORDER"),
   Span(doc80, 9, 12, label ="CONTRACT"),
   Span(doc80, 12, 13, label ="CONTRACT1"),
   Span(doc80, 13, 14, label ="POS"),
   Span(doc80, 14, 15, label ="AMOUNT"),
   Span(doc80, 16, 17, label ="ARTICLE"),
   Span(doc80, 17, 18, label ="PRICE"),
   Span(doc80, 18, 19, label ="UNIT"),
   Span(doc80, 20, 21, label ="SUMMA"),
   Span(doc80, 54, 55, label ="TARIFF"),
   Span(doc80, 59, 60, label ="COUNTRY"),
   Span(doc80, 62, 63, label ="PR_SURCH"),
   Span(doc80, 64, 65, label ="SURCHARGE"),
   Span(doc80, 65, 66, label ="TOTAL")]
docs.append(doc80)
print("doc81, 54, #NORDER 2407326; CONTRACT SR-1-06; CONTRACT1 97; POS 10100; AMOUNT 20; ARTICLE 1130005471; PRICE 45,12; UNIT 100; SUMMA 9,02; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 1,03; TOTAL 10,05; ")
doc81 = nlp('''Order number: 2407326 Purchase order number: N SR-1-06 97 10100 20 PC 1130005471 45,12 100 PC 9,02 3015-PP 3015 PP packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 1,03 10,05''')
doc81.ents = [
   Span(doc81, 3, 4, label ="NORDER"),
   Span(doc81, 9, 12, label ="CONTRACT"),
   Span(doc81, 12, 13, label ="CONTRACT1"),
   Span(doc81, 13, 14, label ="POS"),
   Span(doc81, 14, 15, label ="AMOUNT"),
   Span(doc81, 16, 17, label ="ARTICLE"),
   Span(doc81, 17, 18, label ="PRICE"),
   Span(doc81, 18, 19, label ="UNIT"),
   Span(doc81, 20, 21, label ="SUMMA"),
   Span(doc81, 42, 43, label ="TARIFF"),
   Span(doc81, 47, 48, label ="COUNTRY"),
   Span(doc81, 50, 51, label ="PR_SURCH"),
   Span(doc81, 52, 53, label ="SURCHARGE"),
   Span(doc81, 53, 54, label ="TOTAL")]
docs.append(doc81)
print("doc82, 60, #NORDER 2407328; CONTRACT SR-1-06; CONTRACT1 99; POS 10200; AMOUNT 20; ARTICLE 6100201500; PRICE 2,23; UNIT 1; SUMMA 44,60; TARIFF 84812010; COUNTRY China; PR_SURCH 6,90; SURCHARGE 3,08; TOTAL 47,68; ")
doc82 = nlp('''Order number: 2407328 Purchase order number: N SR-1-06 99 10200 20 PC 6100201500 2,23 1 PC 44,60 QRC-IA-06-F-G04-BT-W3AA packed per each item Export - Customs tariff no.: 84812010 Country of origin: China Material Surcharge 6,90 % 3,08  47,68 EAC - Eurasian Conformity''')
doc82.ents = [
   Span(doc82, 3, 4, label ="NORDER"),
   Span(doc82, 9, 12, label ="CONTRACT"),
   Span(doc82, 12, 13, label ="CONTRACT1"),
   Span(doc82, 13, 14, label ="POS"),
   Span(doc82, 14, 15, label ="AMOUNT"),
   Span(doc82, 16, 17, label ="ARTICLE"),
   Span(doc82, 17, 18, label ="PRICE"),
   Span(doc82, 18, 19, label ="UNIT"),
   Span(doc82, 20, 21, label ="SUMMA"),
   Span(doc82, 43, 44, label ="TARIFF"),
   Span(doc82, 48, 49, label ="COUNTRY"),
   Span(doc82, 51, 52, label ="PR_SURCH"),
   Span(doc82, 53, 54, label ="SURCHARGE"),
   Span(doc82, 55, 56, label ="TOTAL")]
docs.append(doc82)
print("doc83, 63, #NORDER 2407328; CONTRACT SR-1-06; CONTRACT1 99; POS 10300; AMOUNT 20; ARTICLE 6100201501; PRICE 0,98; UNIT 1; SUMMA 19,60; TARIFF 84812010; COUNTRY China; PR_SURCH 6,90; SURCHARGE 1,35; TOTAL 20,95; ")
doc83 = nlp('''Order number: 2407328 Purchase order number: N SR-1-06 99 10300 20 PC 6100201501 0,98 1 PC 19,60 QRC-IA-06-M-G04-B-W3AA packed per each item Product description: coupling Export - Customs tariff no.: 84812010 Country of origin: China Material Surcharge 6,90 % 1,35 20,95 EAC - Eurasian Conformity''')
doc83.ents = [
   Span(doc83, 3, 4, label ="NORDER"),
   Span(doc83, 9, 12, label ="CONTRACT"),
   Span(doc83, 12, 13, label ="CONTRACT1"),
   Span(doc83, 13, 14, label ="POS"),
   Span(doc83, 14, 15, label ="AMOUNT"),
   Span(doc83, 16, 17, label ="ARTICLE"),
   Span(doc83, 17, 18, label ="PRICE"),
   Span(doc83, 18, 19, label ="UNIT"),
   Span(doc83, 20, 21, label ="SUMMA"),
   Span(doc83, 47, 48, label ="TARIFF"),
   Span(doc83, 52, 53, label ="COUNTRY"),
   Span(doc83, 55, 56, label ="PR_SURCH"),
   Span(doc83, 57, 58, label ="SURCHARGE"),
   Span(doc83, 58, 59, label ="TOTAL")]
docs.append(doc83)
print("doc84, 69, #NORDER 2407329; CONTRACT SR-1-06; CONTRACT1 100; POS 10400; AMOUNT 6; ARTICLE 1210001522; PRICE 5,07; UNIT 1; SUMMA 30,42; TARIFF 90269000; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 3,47; TOTAL 33,89; ")
doc84 = nlp('''Order number: 2407329 Purchase order number: N SR-1-06 100 10400 6 PC 1210001522 (*) 5,07 1 PC 30,42 SMA-15-G1/2-B-OR-W3 SMA15-G1/2-P-OR-C6F packed per each item Product description: connector Export - Customs tariff no.: 90269000 Country of origin: Germany Material Surcharge 11,40 % 3,47 33,89''')
doc84.ents = [
   Span(doc84, 3, 4, label ="NORDER"),
   Span(doc84, 9, 12, label ="CONTRACT"),
   Span(doc84, 12, 13, label ="CONTRACT1"),
   Span(doc84, 13, 14, label ="POS"),
   Span(doc84, 14, 15, label ="AMOUNT"),
   Span(doc84, 16, 17, label ="ARTICLE"),
   Span(doc84, 20, 21, label ="PRICE"),
   Span(doc84, 21, 22, label ="UNIT"),
   Span(doc84, 23, 24, label ="SUMMA"),
   Span(doc84, 57, 58, label ="TARIFF"),
   Span(doc84, 62, 63, label ="COUNTRY"),
   Span(doc84, 65, 66, label ="PR_SURCH"),
   Span(doc84, 67, 68, label ="SURCHARGE"),
   Span(doc84, 68, 69, label ="TOTAL")]
docs.append(doc84)
print("doc85, 59, #NORDER 2407329; CONTRACT SR-1-06; CONTRACT1 100; POS 10500; AMOUNT 20; ARTICLE 6010000771; PRICE 349,15; UNIT 100; SUMMA 69,83; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 4,82; TOTAL 74,65; ")
doc85 = nlp('''Order number: 2407329 Purchase order number: N SR-1-06 100 10500 20 PC 6010000771 (*) 349,15 100 PC 69,83 FI-G-20S-W3-MS packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 4,82   74,65''')
doc85.ents = [
   Span(doc85, 3, 4, label ="NORDER"),
   Span(doc85, 9, 12, label ="CONTRACT"),
   Span(doc85, 12, 13, label ="CONTRACT1"),
   Span(doc85, 13, 14, label ="POS"),
   Span(doc85, 14, 15, label ="AMOUNT"),
   Span(doc85, 16, 17, label ="ARTICLE"),
   Span(doc85, 20, 21, label ="PRICE"),
   Span(doc85, 21, 22, label ="UNIT"),
   Span(doc85, 23, 24, label ="SUMMA"),
   Span(doc85, 46, 47, label ="TARIFF"),
   Span(doc85, 51, 52, label ="COUNTRY"),
   Span(doc85, 54, 55, label ="PR_SURCH"),
   Span(doc85, 56, 57, label ="SURCHARGE"),
   Span(doc85, 58, 59, label ="TOTAL")]
docs.append(doc85)
print("doc86, 71, #NORDER 2407329; CONTRACT SR-1-06; CONTRACT1 100; POS 10600; AMOUNT 50; ARTICLE 6020000359; PRICE 146,91; UNIT 100; SUMMA 73,46; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 5,07; TOTAL 78,53; ")
doc86 = nlp('''Order number: 2407329 Purchase order number: N SR-1-06 100 10600 50 PC 6020000359 (*) 146,91 100 PC 73,46 FI-GE-10LM18x1.5-WD-B-W3 FI-GE-10LM18x1 ,5-WD-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 5,07 78,53''')
doc86.ents = [
   Span(doc86, 3, 4, label ="NORDER"),
   Span(doc86, 9, 12, label ="CONTRACT"),
   Span(doc86, 12, 13, label ="CONTRACT1"),
   Span(doc86, 13, 14, label ="POS"),
   Span(doc86, 14, 15, label ="AMOUNT"),
   Span(doc86, 16, 17, label ="ARTICLE"),
   Span(doc86, 20, 21, label ="PRICE"),
   Span(doc86, 21, 22, label ="UNIT"),
   Span(doc86, 23, 24, label ="SUMMA"),
   Span(doc86, 59, 60, label ="TARIFF"),
   Span(doc86, 64, 65, label ="COUNTRY"),
   Span(doc86, 67, 68, label ="PR_SURCH"),
   Span(doc86, 69, 70, label ="SURCHARGE"),
   Span(doc86, 70, 71, label ="TOTAL")]
docs.append(doc86)
print("doc87, 61, #NORDER 2407329; CONTRACT SR-1-06; CONTRACT1 100; POS 10700; AMOUNT 40; ARTICLE 6020000504; PRICE 531,26; UNIT 100; SUMMA 212,50; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 14,66; TOTAL 227,16; ")
doc87 = nlp('''Order number: 2407329 Purchase order number: N SR-1-06 100 10700 40 PC 6020000504 (*) 531,26 100 PC 212,50 FI-GE-38 SR-WD-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 14,66 227,16''')
doc87.ents = [
   Span(doc87, 3, 4, label ="NORDER"),
   Span(doc87, 9, 12, label ="CONTRACT"),
   Span(doc87, 12, 13, label ="CONTRACT1"),
   Span(doc87, 13, 14, label ="POS"),
   Span(doc87, 14, 15, label ="AMOUNT"),
   Span(doc87, 16, 17, label ="ARTICLE"),
   Span(doc87, 20, 21, label ="PRICE"),
   Span(doc87, 21, 22, label ="UNIT"),
   Span(doc87, 23, 24, label ="SUMMA"),
   Span(doc87, 49, 50, label ="TARIFF"),
   Span(doc87, 54, 55, label ="COUNTRY"),
   Span(doc87, 57, 58, label ="PR_SURCH"),
   Span(doc87, 59, 60, label ="SURCHARGE"),
   Span(doc87, 60, 61, label ="TOTAL")]
docs.append(doc87)
print("doc88, 67, #NORDER 2407332; CONTRACT SR-1-06; CONTRACT1 103; POS 10800; AMOUNT 120; ARTICLE 1130004022; PRICE 4,30; UNIT 100; SUMMA 5,16; TARIFF 73181588; COUNTRY Taiwan; PR_SURCH 11,40; SURCHARGE 0,59; TOTAL 5,75; ")
doc88 = nlp('''Order number: 2407332 Purchase order number: N SR-1-06 103 10800 120 PC 1130004022 4,30 100 PC 5,16 AS-M6x40-DIN931/933-8.8-W3 AS-M6X40-DIN931/933-8.8-W3 packed per each item Product description: screw Export - Customs tariff no.: 73181588 Country of origin: Taiwan Material Surcharge 11,40 % 0,59 5,75   ''')
doc88.ents = [
   Span(doc88, 3, 4, label ="NORDER"),
   Span(doc88, 9, 12, label ="CONTRACT"),
   Span(doc88, 12, 13, label ="CONTRACT1"),
   Span(doc88, 13, 14, label ="POS"),
   Span(doc88, 14, 15, label ="AMOUNT"),
   Span(doc88, 16, 17, label ="ARTICLE"),
   Span(doc88, 17, 18, label ="PRICE"),
   Span(doc88, 18, 19, label ="UNIT"),
   Span(doc88, 20, 21, label ="SUMMA"),
   Span(doc88, 54, 55, label ="TARIFF"),
   Span(doc88, 59, 60, label ="COUNTRY"),
   Span(doc88, 62, 63, label ="PR_SURCH"),
   Span(doc88, 64, 65, label ="SURCHARGE"),
   Span(doc88, 65, 66, label ="TOTAL")]
docs.append(doc88)
print("doc89, 67, #NORDER 2407332; CONTRACT SR-1-06; CONTRACT1 103; POS 10900; AMOUNT 120; ARTICLE 1130004023; PRICE 4,51; UNIT 100; SUMMA 5,41; TARIFF 73181588; COUNTRY Origin unknown; PR_SURCH 11,40; SURCHARGE 0,62; TOTAL 6,03; ")
doc89 = nlp('''Order number: 2407332 Purchase order number: N SR-1-06 103 10900 120 PC 1130004023 4,51 100 PC 5,41 AS-M6x45-DIN931/933-8.8-W3 AS-M6X45-DIN931/933-8.8-W3 packed per each item Product description: screw Export - Customs tariff no.: 73181588 Country of origin: Origin unknown Material Surcharge 11,40 % 0,62 6,03''')
doc89.ents = [
   Span(doc89, 3, 4, label ="NORDER"),
   Span(doc89, 9, 12, label ="CONTRACT"),
   Span(doc89, 12, 13, label ="CONTRACT1"),
   Span(doc89, 13, 14, label ="POS"),
   Span(doc89, 14, 15, label ="AMOUNT"),
   Span(doc89, 16, 17, label ="ARTICLE"),
   Span(doc89, 17, 18, label ="PRICE"),
   Span(doc89, 18, 19, label ="UNIT"),
   Span(doc89, 20, 21, label ="SUMMA"),
   Span(doc89, 54, 55, label ="TARIFF"),
   Span(doc89, 59, 61, label ="COUNTRY"),
   Span(doc89, 63, 64, label ="PR_SURCH"),
   Span(doc89, 65, 66, label ="SURCHARGE"),
   Span(doc89, 66, 67, label ="TOTAL")]
docs.append(doc89)
print("doc90, 67, #NORDER 2407332; CONTRACT SR-1-06; CONTRACT1 103; POS 11000; AMOUNT 240; ARTICLE 1130004024; PRICE 5,48; UNIT 100; SUMMA 13,15; TARIFF 73181588; COUNTRY Origin unknown; PR_SURCH 11,40; SURCHARGE 1,50; TOTAL 14,65; ")
doc90 = nlp('''Order number: 2407332 Purchase order number: N SR-1-06 103 11000 240 PC 1130004024 5,48 100 PC 13,15 AS-M6x60-DIN931/933-8.8-W3 AS-M6X60-DIN931/933-8.8-W3 packed per each item Product description: screw Export - Customs tariff no.: 73181588 Country of origin: Origin unknown Material Surcharge 11,40 % 1,50 14,65''')
doc90.ents = [
   Span(doc90, 3, 4, label ="NORDER"),
   Span(doc90, 9, 12, label ="CONTRACT"),
   Span(doc90, 12, 13, label ="CONTRACT1"),
   Span(doc90, 13, 14, label ="POS"),
   Span(doc90, 14, 15, label ="AMOUNT"),
   Span(doc90, 16, 17, label ="ARTICLE"),
   Span(doc90, 17, 18, label ="PRICE"),
   Span(doc90, 18, 19, label ="UNIT"),
   Span(doc90, 20, 21, label ="SUMMA"),
   Span(doc90, 54, 55, label ="TARIFF"),
   Span(doc90, 59, 61, label ="COUNTRY"),
   Span(doc90, 63, 64, label ="PR_SURCH"),
   Span(doc90, 65, 66, label ="SURCHARGE"),
   Span(doc90, 66, 67, label ="TOTAL")]
docs.append(doc90)
print("doc91, 55, #NORDER 2407332; CONTRACT SR-1-06; CONTRACT1 103; POS 11100; AMOUNT 75; ARTICLE 1130003768; PRICE 32,99; UNIT 100; SUMMA 24,74; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 2,82; TOTAL 27,56; ")
doc91 = nlp('''Order number: 2407332 Purchase order number: N SR-1-06 103 11100 75 PC 1130003768 32,99 100 PC 24,74 428-PP 428 PP packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 2,82 27,56    ''')
doc91.ents = [
   Span(doc91, 3, 4, label ="NORDER"),
   Span(doc91, 9, 12, label ="CONTRACT"),
   Span(doc91, 12, 13, label ="CONTRACT1"),
   Span(doc91, 13, 14, label ="POS"),
   Span(doc91, 14, 15, label ="AMOUNT"),
   Span(doc91, 16, 17, label ="ARTICLE"),
   Span(doc91, 17, 18, label ="PRICE"),
   Span(doc91, 18, 19, label ="UNIT"),
   Span(doc91, 20, 21, label ="SUMMA"),
   Span(doc91, 42, 43, label ="TARIFF"),
   Span(doc91, 47, 48, label ="COUNTRY"),
   Span(doc91, 50, 51, label ="PR_SURCH"),
   Span(doc91, 52, 53, label ="SURCHARGE"),
   Span(doc91, 53, 54, label ="TOTAL")]
docs.append(doc91)
print("doc92, 54, #NORDER 2407332; CONTRACT SR-1-06; CONTRACT1 103; POS 11200; AMOUNT 75; ARTICLE 1130005997; PRICE 51,18; UNIT 100; SUMMA 38,39; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 4,38; TOTAL 42,77; ")
doc92 = nlp('''Order number: 2407332 Purchase order number: N SR-1-06 103 11200 75 PC 1130005997 51,18 100 PC 38,39 535-PP 535 PP packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 4,38 42,77''')
doc92.ents = [
   Span(doc92, 3, 4, label ="NORDER"),
   Span(doc92, 9, 12, label ="CONTRACT"),
   Span(doc92, 12, 13, label ="CONTRACT1"),
   Span(doc92, 13, 14, label ="POS"),
   Span(doc92, 14, 15, label ="AMOUNT"),
   Span(doc92, 16, 17, label ="ARTICLE"),
   Span(doc92, 17, 18, label ="PRICE"),
   Span(doc92, 18, 19, label ="UNIT"),
   Span(doc92, 20, 21, label ="SUMMA"),
   Span(doc92, 42, 43, label ="TARIFF"),
   Span(doc92, 47, 48, label ="COUNTRY"),
   Span(doc92, 50, 51, label ="PR_SURCH"),
   Span(doc92, 52, 53, label ="SURCHARGE"),
   Span(doc92, 53, 54, label ="TOTAL")]
docs.append(doc92)
print("doc93, 55, #NORDER 2407332; CONTRACT SR-1-06; CONTRACT1 103; POS 11300; AMOUNT 75; ARTICLE 1130000264; PRICE 8,38; UNIT 100; SUMMA 6,29; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,72; TOTAL 7,01; ")
doc93 = nlp('''Order number: 2407332 Purchase order number: N SR-1-06 103 11300 75 PC 1130000264 8,38 100 PC 6,29 DP-3-W3 DP 3 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 0,72 7,01''')
doc93.ents = [
   Span(doc93, 3, 4, label ="NORDER"),
   Span(doc93, 9, 12, label ="CONTRACT"),
   Span(doc93, 12, 13, label ="CONTRACT1"),
   Span(doc93, 13, 14, label ="POS"),
   Span(doc93, 14, 15, label ="AMOUNT"),
   Span(doc93, 16, 17, label ="ARTICLE"),
   Span(doc93, 17, 18, label ="PRICE"),
   Span(doc93, 18, 19, label ="UNIT"),
   Span(doc93, 20, 21, label ="SUMMA"),
   Span(doc93, 43, 44, label ="TARIFF"),
   Span(doc93, 48, 49, label ="COUNTRY"),
   Span(doc93, 51, 52, label ="PR_SURCH"),
   Span(doc93, 53, 54, label ="SURCHARGE"),
   Span(doc93, 54, 55, label ="TOTAL")]
docs.append(doc93)
print("doc94, 56, #NORDER 2407332; CONTRACT SR-1-06; CONTRACT1 103; POS 11400; AMOUNT 125; ARTICLE 1130000269; PRICE 11,33; UNIT 100; SUMMA 14,16; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 1,61; TOTAL 15,77; ")
doc94 = nlp('''Order number: 2407332 Purchase order number: N SR-1-06 103 11400 125 PC 1130000269 11,33 100 PC 14,16 DP-5-W3 DP 5 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 1,61 15,77    ''')
doc94.ents = [
   Span(doc94, 3, 4, label ="NORDER"),
   Span(doc94, 9, 12, label ="CONTRACT"),
   Span(doc94, 12, 13, label ="CONTRACT1"),
   Span(doc94, 13, 14, label ="POS"),
   Span(doc94, 14, 15, label ="AMOUNT"),
   Span(doc94, 16, 17, label ="ARTICLE"),
   Span(doc94, 17, 18, label ="PRICE"),
   Span(doc94, 18, 19, label ="UNIT"),
   Span(doc94, 20, 21, label ="SUMMA"),
   Span(doc94, 43, 44, label ="TARIFF"),
   Span(doc94, 48, 49, label ="COUNTRY"),
   Span(doc94, 51, 52, label ="PR_SURCH"),
   Span(doc94, 53, 54, label ="SURCHARGE"),
   Span(doc94, 54, 55, label ="TOTAL")]
docs.append(doc94)
print("doc95, 58, #NORDER 2407332; CONTRACT SR-1-06; CONTRACT1 103; POS 11500; AMOUNT 75; ARTICLE 1120001161; PRICE 27,74; UNIT 100; SUMMA 20,81; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 2,37; TOTAL 23,18; ")
doc95 = nlp('''Order number: 2407332 Purchase order number: N SR-1-06 103 11500 75 PC 1120001161 27,74 100 PC 20,81 SP-3-M-W2 SP 3 M W2 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 2,37 23,18''')
doc95.ents = [
   Span(doc95, 3, 4, label ="NORDER"),
   Span(doc95, 9, 12, label ="CONTRACT"),
   Span(doc95, 12, 13, label ="CONTRACT1"),
   Span(doc95, 13, 14, label ="POS"),
   Span(doc95, 14, 15, label ="AMOUNT"),
   Span(doc95, 16, 17, label ="ARTICLE"),
   Span(doc95, 17, 18, label ="PRICE"),
   Span(doc95, 18, 19, label ="UNIT"),
   Span(doc95, 20, 21, label ="SUMMA"),
   Span(doc95, 46, 47, label ="TARIFF"),
   Span(doc95, 51, 52, label ="COUNTRY"),
   Span(doc95, 54, 55, label ="PR_SURCH"),
   Span(doc95, 56, 57, label ="SURCHARGE"),
   Span(doc95, 57, 58, label ="TOTAL")]
docs.append(doc95)
print("doc96, 58, #NORDER 2407332; CONTRACT SR-1-06; CONTRACT1 103; POS 11600; AMOUNT 100; ARTICLE 1120001171; PRICE 31,04; UNIT 100; SUMMA 31,04; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 3,54; TOTAL 34,58; ")
doc96 = nlp('''Order number: 2407332 Purchase order number: N SR-1-06 103 11600 100 PC 1120001171 31,04 100 PC 31,04 SP-5-M-W2 SP 5 M W2 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 3,54 34,58''')
doc96.ents = [
   Span(doc96, 3, 4, label ="NORDER"),
   Span(doc96, 9, 12, label ="CONTRACT"),
   Span(doc96, 12, 13, label ="CONTRACT1"),
   Span(doc96, 13, 14, label ="POS"),
   Span(doc96, 14, 15, label ="AMOUNT"),
   Span(doc96, 16, 17, label ="ARTICLE"),
   Span(doc96, 17, 18, label ="PRICE"),
   Span(doc96, 18, 19, label ="UNIT"),
   Span(doc96, 20, 21, label ="SUMMA"),
   Span(doc96, 46, 47, label ="TARIFF"),
   Span(doc96, 51, 52, label ="COUNTRY"),
   Span(doc96, 54, 55, label ="PR_SURCH"),
   Span(doc96, 56, 57, label ="SURCHARGE"),
   Span(doc96, 57, 58, label ="TOTAL")]
docs.append(doc96)
print("doc97, 68, #NORDER 2407333; CONTRACT SR-1-06; CONTRACT1 104; POS 11700; AMOUNT 200; ARTICLE 1130004021; PRICE 4,09; UNIT 100; SUMMA 8,18; TARIFF 73181588; COUNTRY Origin unknown; PR_SURCH 11,40; SURCHARGE 0,93; TOTAL 9,11; ")
doc97 = nlp('''Order number: 2407333 Purchase order number: N SR-1-06 104 11700 200 PC 1130004021 4,09 100 PC 8,18 AS-M6x35-DIN931/933-8.8-W3 AS-M6X35-DIN931/933-8.8-W3 packed per each item Product description: screw Export - Customs tariff no.: 73181588 Country of origin: Origin unknown Material Surcharge 11,40 % 0,93 9,11    ''')
doc97.ents = [
   Span(doc97, 3, 4, label ="NORDER"),
   Span(doc97, 9, 12, label ="CONTRACT"),
   Span(doc97, 12, 13, label ="CONTRACT1"),
   Span(doc97, 13, 14, label ="POS"),
   Span(doc97, 14, 15, label ="AMOUNT"),
   Span(doc97, 16, 17, label ="ARTICLE"),
   Span(doc97, 17, 18, label ="PRICE"),
   Span(doc97, 18, 19, label ="UNIT"),
   Span(doc97, 20, 21, label ="SUMMA"),
   Span(doc97, 54, 55, label ="TARIFF"),
   Span(doc97, 59, 61, label ="COUNTRY"),
   Span(doc97, 63, 64, label ="PR_SURCH"),
   Span(doc97, 65, 66, label ="SURCHARGE"),
   Span(doc97, 66, 67, label ="TOTAL")]
docs.append(doc97)
print("doc98, 55, #NORDER 2407333; CONTRACT SR-1-06; CONTRACT1 104; POS 11800; AMOUNT 100; ARTICLE 1130000261; PRICE 7,39; UNIT 100; SUMMA 7,39; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,84; TOTAL 8,23; ")
doc98 = nlp('''Order number: 2407333 Purchase order number: N SR-1-06 104 11800 100 PC 1130000261 7,39 100 PC 7,39 DP-2-W3 DP 2 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 0,84 8,23''')
doc98.ents = [
   Span(doc98, 3, 4, label ="NORDER"),
   Span(doc98, 9, 12, label ="CONTRACT"),
   Span(doc98, 12, 13, label ="CONTRACT1"),
   Span(doc98, 13, 14, label ="POS"),
   Span(doc98, 14, 15, label ="AMOUNT"),
   Span(doc98, 16, 17, label ="ARTICLE"),
   Span(doc98, 17, 18, label ="PRICE"),
   Span(doc98, 18, 19, label ="UNIT"),
   Span(doc98, 20, 21, label ="SUMMA"),
   Span(doc98, 43, 44, label ="TARIFF"),
   Span(doc98, 48, 49, label ="COUNTRY"),
   Span(doc98, 51, 52, label ="PR_SURCH"),
   Span(doc98, 53, 54, label ="SURCHARGE"),
   Span(doc98, 54, 55, label ="TOTAL")]
docs.append(doc98)
print("doc99, 58, #NORDER 2407333; CONTRACT SR-1-06; CONTRACT1 104; POS 11900; AMOUNT 100; ARTICLE 1120001249; PRICE 35,37; UNIT 100; SUMMA 35,37; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 4,03; TOTAL 39,40; ")
doc99 = nlp('''Order number: 2407333 Purchase order number: N SR-1-06 104 11900 100 PC 1120001249 35,37 100 PC 35,37 SPV-2-M-W3 SPV 2 M W3 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 4,03 39,40''')
doc99.ents = [
   Span(doc99, 3, 4, label ="NORDER"),
   Span(doc99, 9, 12, label ="CONTRACT"),
   Span(doc99, 12, 13, label ="CONTRACT1"),
   Span(doc99, 13, 14, label ="POS"),
   Span(doc99, 14, 15, label ="AMOUNT"),
   Span(doc99, 16, 17, label ="ARTICLE"),
   Span(doc99, 17, 18, label ="PRICE"),
   Span(doc99, 18, 19, label ="UNIT"),
   Span(doc99, 20, 21, label ="SUMMA"),
   Span(doc99, 46, 47, label ="TARIFF"),
   Span(doc99, 51, 52, label ="COUNTRY"),
   Span(doc99, 54, 55, label ="PR_SURCH"),
   Span(doc99, 56, 57, label ="SURCHARGE"),
   Span(doc99, 57, 58, label ="TOTAL")]
docs.append(doc99)
print("doc100, 69, #NORDER 2407339; CONTRACT SR-1-06; CONTRACT1 105; POS 12000; AMOUNT 96; ARTICLE 1130004020; PRICE 3,93; UNIT 100; SUMMA 3,77; TARIFF 73181588; COUNTRY Origin unknown; PR_SURCH 11,40; SURCHARGE 0,43; TOTAL 4,20; ")
doc100 = nlp('''Order number: 2407339 Purchase order number: N SR-1-06 105 12000 96 PC 1130004020 3,93. 100 PC 3,77 AS-M6x30-DIN931/933-8.8-W3 AS-M6X30-DIN931/933-8.8-W3 packed per each item Product description: screw Export - Customs tariff no.: 73181588 Country of origin: Origin unknown Material Surcharge 11,40 % 0,43 4,20   ''')
doc100.ents = [
   Span(doc100, 3, 4, label ="NORDER"),
   Span(doc100, 9, 12, label ="CONTRACT"),
   Span(doc100, 12, 13, label ="CONTRACT1"),
   Span(doc100, 13, 14, label ="POS"),
   Span(doc100, 14, 15, label ="AMOUNT"),
   Span(doc100, 16, 17, label ="ARTICLE"),
   Span(doc100, 17, 18, label ="PRICE"),
   Span(doc100, 19, 20, label ="UNIT"),
   Span(doc100, 21, 22, label ="SUMMA"),
   Span(doc100, 55, 56, label ="TARIFF"),
   Span(doc100, 60, 62, label ="COUNTRY"),
   Span(doc100, 64, 65, label ="PR_SURCH"),
   Span(doc100, 66, 67, label ="SURCHARGE"),
   Span(doc100, 67, 68, label ="TOTAL")]
docs.append(doc100)
print("doc101, 67, #NORDER 2407339; CONTRACT SR-1-06; CONTRACT1 105; POS 12100; AMOUNT 28; ARTICLE 1130004021; PRICE 4,09; UNIT 100; SUMMA 1,15; TARIFF 73181588; COUNTRY Origin unknown; PR_SURCH 11,40; SURCHARGE 0,13; TOTAL 1,28; ")
doc101 = nlp('''Order number: 2407339 Purchase order number: N SR-1-06 105 12100 28 PC 1130004021 4,09 100 PC 1,15 AS-M6x35-DIN931/933-8.8-W3 AS-M6X35-DIN931/933-8.8-W3 packed per each item Product description: screw Export - Customs tariff no.: 73181588 Country of origin: Origin unknown Material Surcharge 11,40 % 0,13 1,28''')
doc101.ents = [
   Span(doc101, 3, 4, label ="NORDER"),
   Span(doc101, 9, 12, label ="CONTRACT"),
   Span(doc101, 12, 13, label ="CONTRACT1"),
   Span(doc101, 13, 14, label ="POS"),
   Span(doc101, 14, 15, label ="AMOUNT"),
   Span(doc101, 16, 17, label ="ARTICLE"),
   Span(doc101, 17, 18, label ="PRICE"),
   Span(doc101, 18, 19, label ="UNIT"),
   Span(doc101, 20, 21, label ="SUMMA"),
   Span(doc101, 54, 55, label ="TARIFF"),
   Span(doc101, 59, 61, label ="COUNTRY"),
   Span(doc101, 63, 64, label ="PR_SURCH"),
   Span(doc101, 65, 66, label ="SURCHARGE"),
   Span(doc101, 66, 67, label ="TOTAL")]
docs.append(doc101)
print("doc102, 67, #NORDER 2407339; CONTRACT SR-1-06; CONTRACT1 105; POS 12200; AMOUNT 2; ARTICLE 1130004024; PRICE 5,48; UNIT 100; SUMMA 0,11; TARIFF 73181588; COUNTRY Origin unknown; PR_SURCH 11,40; SURCHARGE 0,01; TOTAL 0,12; ")
doc102 = nlp('''Order number: 2407339 Purchase order number: N SR-1-06 105 12200 2 PC 1130004024 5,48 100 PC 0,11 AS-M6x60-DIN931/933-8.8-W3 AS-M6X60-DIN931/933-8.8-W3 packed per each item Product description: screw Export - Customs tariff no.: 73181588 Country of origin: Origin unknown Material Surcharge 11,40 % 0,01 0,12''')
doc102.ents = [
   Span(doc102, 3, 4, label ="NORDER"),
   Span(doc102, 9, 12, label ="CONTRACT"),
   Span(doc102, 12, 13, label ="CONTRACT1"),
   Span(doc102, 13, 14, label ="POS"),
   Span(doc102, 14, 15, label ="AMOUNT"),
   Span(doc102, 16, 17, label ="ARTICLE"),
   Span(doc102, 17, 18, label ="PRICE"),
   Span(doc102, 18, 19, label ="UNIT"),
   Span(doc102, 20, 21, label ="SUMMA"),
   Span(doc102, 54, 55, label ="TARIFF"),
   Span(doc102, 59, 61, label ="COUNTRY"),
   Span(doc102, 63, 64, label ="PR_SURCH"),
   Span(doc102, 65, 66, label ="SURCHARGE"),
   Span(doc102, 66, 67, label ="TOTAL")]
docs.append(doc102)
print("doc103, 61, #NORDER 2407339; CONTRACT SR-1-06; CONTRACT1 105; POS 12300; AMOUNT 4; ARTICLE 1730000052; PRICE 0,23; UNIT 1; SUMMA 0,92; TARIFF 40169300; COUNTRY China; PR_SURCH 15,50; SURCHARGE 0,14; TOTAL 1,06; ")
doc103 = nlp('''Order number: 2407339 Purchase order number: N SR-1-06 105 12300 4 PC 1730000052 0,23 1 PC 0,92 O-Ring-47 .22x3.53-B90 O-Ring NBR-47,22x3,53-SH90 packed per each item Product description: seal Export - Customs tariff no.: 40169300 Country of origin: China Material Surcharge 15,50 % 0,14 1,06   ''')
doc103.ents = [
   Span(doc103, 3, 4, label ="NORDER"),
   Span(doc103, 9, 12, label ="CONTRACT"),
   Span(doc103, 12, 13, label ="CONTRACT1"),
   Span(doc103, 13, 14, label ="POS"),
   Span(doc103, 14, 15, label ="AMOUNT"),
   Span(doc103, 16, 17, label ="ARTICLE"),
   Span(doc103, 17, 18, label ="PRICE"),
   Span(doc103, 18, 19, label ="UNIT"),
   Span(doc103, 20, 21, label ="SUMMA"),
   Span(doc103, 48, 49, label ="TARIFF"),
   Span(doc103, 53, 54, label ="COUNTRY"),
   Span(doc103, 56, 57, label ="PR_SURCH"),
   Span(doc103, 58, 59, label ="SURCHARGE"),
   Span(doc103, 59, 60, label ="TOTAL")]
docs.append(doc103)
print("doc104, 75, #NORDER 2407339; CONTRACT SR-1-06; CONTRACT1 105; POS 12400; AMOUNT 4; ARTICLE 1720000008; PRICE 1,53; UNIT 1; SUMMA 6,12; TARIFF 73181568; COUNTRY Origin unknown; PR_SURCH 15,50; SURCHARGE 0,95; TOTAL 7,07; ")
doc104 = nlp('''Order number: 2407339 Purchase order number: N SR-1-06 105 12400 4 PC 1720000008 1,53 1 PC 6,12 Kit-BFX-IS-M12X45-ISO4762-8.8-W66 SET-BFX-IS-M12X45-8.8-ISO4762-W66 packed per each item Product description: screw Export - Customs tariff no.: 73181568 Country of origin: Origin unknown Material Surcharge 15,50 % 0,95 7,07''')
doc104.ents = [
   Span(doc104, 3, 4, label ="NORDER"),
   Span(doc104, 9, 12, label ="CONTRACT"),
   Span(doc104, 12, 13, label ="CONTRACT1"),
   Span(doc104, 13, 14, label ="POS"),
   Span(doc104, 14, 15, label ="AMOUNT"),
   Span(doc104, 16, 17, label ="ARTICLE"),
   Span(doc104, 17, 18, label ="PRICE"),
   Span(doc104, 18, 19, label ="UNIT"),
   Span(doc104, 20, 21, label ="SUMMA"),
   Span(doc104, 62, 63, label ="TARIFF"),
   Span(doc104, 67, 69, label ="COUNTRY"),
   Span(doc104, 71, 72, label ="PR_SURCH"),
   Span(doc104, 73, 74, label ="SURCHARGE"),
   Span(doc104, 74, 75, label ="TOTAL")]
docs.append(doc104)
print("doc105, 55, #NORDER 2407339; CONTRACT SR-1-06; CONTRACT1 105; POS 12500; AMOUNT 50; ARTICLE 1130000258; PRICE 6,83; UNIT 100; SUMMA 3,42; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,39; TOTAL 3,81; ")
doc105 = nlp('''Order number: 2407339 Purchase order number: N SR-1-06 105 12500 50 PC 1130000258 6,83 100 PC 3,42 DP-1a-W3 DP 1a W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 0,39 3,81''')
doc105.ents = [
   Span(doc105, 3, 4, label ="NORDER"),
   Span(doc105, 9, 12, label ="CONTRACT"),
   Span(doc105, 12, 13, label ="CONTRACT1"),
   Span(doc105, 13, 14, label ="POS"),
   Span(doc105, 14, 15, label ="AMOUNT"),
   Span(doc105, 16, 17, label ="ARTICLE"),
   Span(doc105, 17, 18, label ="PRICE"),
   Span(doc105, 18, 19, label ="UNIT"),
   Span(doc105, 20, 21, label ="SUMMA"),
   Span(doc105, 43, 44, label ="TARIFF"),
   Span(doc105, 48, 49, label ="COUNTRY"),
   Span(doc105, 51, 52, label ="PR_SURCH"),
   Span(doc105, 53, 54, label ="SURCHARGE"),
   Span(doc105, 54, 55, label ="TOTAL")]
docs.append(doc105)
print("doc106, 56, #NORDER 2407339; CONTRACT SR-1-06; CONTRACT1 105; POS 12600; AMOUNT 25; ARTICLE 1130000261; PRICE 7,39; UNIT 100; SUMMA 1,85; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,21; TOTAL 2,06; ")
doc106 = nlp('''Order number: 2407339 Purchase order number: N SR-1-06 105 12600 25 PC 1130000261 7,39 100 PC 1,85 DP-2-W3 DP 2 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 0,21 2,06    ''')
doc106.ents = [
   Span(doc106, 3, 4, label ="NORDER"),
   Span(doc106, 9, 12, label ="CONTRACT"),
   Span(doc106, 12, 13, label ="CONTRACT1"),
   Span(doc106, 13, 14, label ="POS"),
   Span(doc106, 14, 15, label ="AMOUNT"),
   Span(doc106, 16, 17, label ="ARTICLE"),
   Span(doc106, 17, 18, label ="PRICE"),
   Span(doc106, 18, 19, label ="UNIT"),
   Span(doc106, 20, 21, label ="SUMMA"),
   Span(doc106, 43, 44, label ="TARIFF"),
   Span(doc106, 48, 49, label ="COUNTRY"),
   Span(doc106, 51, 52, label ="PR_SURCH"),
   Span(doc106, 53, 54, label ="SURCHARGE"),
   Span(doc106, 54, 55, label ="TOTAL")]
docs.append(doc106)
print("doc107, 55, #NORDER 2407339; CONTRACT SR-1-06; CONTRACT1 105; POS 12700; AMOUNT 25; ARTICLE 1130000269; PRICE 11,33; UNIT 100; SUMMA 2,83; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,32; TOTAL 3,15; ")
doc107 = nlp('''Order number: 2407339 Purchase order number: N SR-1-06 105 12700 25 PC 1130000269 11,33 100 PC 2,83 DP-5-W3 DP 5 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 0,32 3,15''')
doc107.ents = [
   Span(doc107, 3, 4, label ="NORDER"),
   Span(doc107, 9, 12, label ="CONTRACT"),
   Span(doc107, 12, 13, label ="CONTRACT1"),
   Span(doc107, 13, 14, label ="POS"),
   Span(doc107, 14, 15, label ="AMOUNT"),
   Span(doc107, 16, 17, label ="ARTICLE"),
   Span(doc107, 17, 18, label ="PRICE"),
   Span(doc107, 18, 19, label ="UNIT"),
   Span(doc107, 20, 21, label ="SUMMA"),
   Span(doc107, 43, 44, label ="TARIFF"),
   Span(doc107, 48, 49, label ="COUNTRY"),
   Span(doc107, 51, 52, label ="PR_SURCH"),
   Span(doc107, 53, 54, label ="SURCHARGE"),
   Span(doc107, 54, 55, label ="TOTAL")]
docs.append(doc107)
print("doc108, 58, #NORDER 2407339; CONTRACT SR-1-06; CONTRACT1 105; POS 12800; AMOUNT 50; ARTICLE 1120001184; PRICE 27,92; UNIT 100; SUMMA 13,96; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 1,59; TOTAL 15,55; ")
doc108 = nlp('''Order number: 2407339 Purchase order number: N SR-1-06 105 12800 50 PC 1120001184 27,92 100 PC 13,96 SP-1A-M-W3 SP 1a M W3 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 1,59 15,55''')
doc108.ents = [
   Span(doc108, 3, 4, label ="NORDER"),
   Span(doc108, 9, 12, label ="CONTRACT"),
   Span(doc108, 12, 13, label ="CONTRACT1"),
   Span(doc108, 13, 14, label ="POS"),
   Span(doc108, 14, 15, label ="AMOUNT"),
   Span(doc108, 16, 17, label ="ARTICLE"),
   Span(doc108, 17, 18, label ="PRICE"),
   Span(doc108, 18, 19, label ="UNIT"),
   Span(doc108, 20, 21, label ="SUMMA"),
   Span(doc108, 46, 47, label ="TARIFF"),
   Span(doc108, 51, 52, label ="COUNTRY"),
   Span(doc108, 54, 55, label ="PR_SURCH"),
   Span(doc108, 56, 57, label ="SURCHARGE"),
   Span(doc108, 57, 58, label ="TOTAL")]
docs.append(doc108)
print("doc109, 59, #NORDER 2407339; CONTRACT SR-1-06; CONTRACT1 105; POS 12900; AMOUNT 25; ARTICLE 1120001156; PRICE 26,58; UNIT 100; SUMMA 6,65; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,76; TOTAL 7,41; ")
doc109 = nlp('''Order number: 2407339 Purchase order number: N SR-1-06 105 12900 25 PC 1120001156 26,58 100 PC 6,65 SP-2-M-W2 SP 2 M W2 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 0,76 7,41   ''')
doc109.ents = [
   Span(doc109, 3, 4, label ="NORDER"),
   Span(doc109, 9, 12, label ="CONTRACT"),
   Span(doc109, 12, 13, label ="CONTRACT1"),
   Span(doc109, 13, 14, label ="POS"),
   Span(doc109, 14, 15, label ="AMOUNT"),
   Span(doc109, 16, 17, label ="ARTICLE"),
   Span(doc109, 17, 18, label ="PRICE"),
   Span(doc109, 18, 19, label ="UNIT"),
   Span(doc109, 20, 21, label ="SUMMA"),
   Span(doc109, 46, 47, label ="TARIFF"),
   Span(doc109, 51, 52, label ="COUNTRY"),
   Span(doc109, 54, 55, label ="PR_SURCH"),
   Span(doc109, 56, 57, label ="SURCHARGE"),
   Span(doc109, 57, 58, label ="TOTAL")]
docs.append(doc109)
print("doc110, 73, #NORDER 2407339; CONTRACT SR-1-06; CONTRACT1 105; POS 13000; AMOUNT 2; ARTICLE 1910000239; PRICE 6,13; UNIT 1; SUMMA 12,26; TARIFF 84213925; COUNTRY Italy; PR_SURCH 11,40; SURCHARGE 1,40; TOTAL 13,66; ")
doc110 = nlp('''Order number: 2407339 Purchase order number: N SR-1-06 105 13000 2 PC 1910000239 6,13 1 PC 12,26 SMBB-47-N-10-O0-C-S065 SMBB-47-N-10-O-C-S065-O packed per each item Product description: filter breather Export - Customs tariff no.: 84213925 Country of origin: Italy Material Surcharge 11,40 % 1,40 13,66 EAC - Eurasian Conformity''')
doc110.ents = [
   Span(doc110, 3, 4, label ="NORDER"),
   Span(doc110, 9, 12, label ="CONTRACT"),
   Span(doc110, 12, 13, label ="CONTRACT1"),
   Span(doc110, 13, 14, label ="POS"),
   Span(doc110, 14, 15, label ="AMOUNT"),
   Span(doc110, 16, 17, label ="ARTICLE"),
   Span(doc110, 17, 18, label ="PRICE"),
   Span(doc110, 18, 19, label ="UNIT"),
   Span(doc110, 20, 21, label ="SUMMA"),
   Span(doc110, 57, 58, label ="TARIFF"),
   Span(doc110, 62, 63, label ="COUNTRY"),
   Span(doc110, 65, 66, label ="PR_SURCH"),
   Span(doc110, 67, 68, label ="SURCHARGE"),
   Span(doc110, 68, 69, label ="TOTAL")]
docs.append(doc110)
print("doc111, 60, #NORDER 2407339; CONTRACT SR-1-06; CONTRACT1 105; POS 13100; AMOUNT 4; ARTICLE 1730001519; PRICE 30,91; UNIT 1; SUMMA 123,64; TARIFF 73079100; COUNTRY Italy; PR_SURCH 15,50; SURCHARGE 19,16; TOTAL 142,80; ")
doc111 = nlp('''Order number: 2407339 Purchase order number: N SR-1-06 105 13100 4 PC 1730001519 30,91 1 PC 123,64 BFX90-305-42L-W66 BFX90-305-L42 packed per each item Product description: flange Export - Customs tariff no.: 73079100 Country of origin: Italy Material Surcharge 15,50 % 19,16 142,80''')
doc111.ents = [
   Span(doc111, 3, 4, label ="NORDER"),
   Span(doc111, 9, 12, label ="CONTRACT"),
   Span(doc111, 12, 13, label ="CONTRACT1"),
   Span(doc111, 13, 14, label ="POS"),
   Span(doc111, 14, 15, label ="AMOUNT"),
   Span(doc111, 16, 17, label ="ARTICLE"),
   Span(doc111, 17, 18, label ="PRICE"),
   Span(doc111, 18, 19, label ="UNIT"),
   Span(doc111, 20, 21, label ="SUMMA"),
   Span(doc111, 48, 49, label ="TARIFF"),
   Span(doc111, 53, 54, label ="COUNTRY"),
   Span(doc111, 56, 57, label ="PR_SURCH"),
   Span(doc111, 58, 59, label ="SURCHARGE"),
   Span(doc111, 59, 60, label ="TOTAL")]
docs.append(doc111)
print("doc112, 61, #NORDER 2407342; CONTRACT SR-1-06; CONTRACT1 106; POS 13200; AMOUNT 24; ARTICLE 1730000099; PRICE 0,57; UNIT 1; SUMMA 13,68; TARIFF 40169300; COUNTRY Origin unknown; PR_SURCH 15,50; SURCHARGE 2,12; TOTAL 15,80; ")
doc112 = nlp('''Order number: 2407342 Purchase order number: N SR-1-06 106 13200 24 PC 1730000099 0,57 1 PC 13,68 O-Ring-24.99x3.53-V90 O-Ring FPM-24,99x3,53-SH90 packed per each item Product description: seal Export - Customs tariff no.: 40169300 Country of origin: Origin unknown Material Surcharge 15,50 % 2,12 15,80  ''')
doc112.ents = [
   Span(doc112, 3, 4, label ="NORDER"),
   Span(doc112, 9, 12, label ="CONTRACT"),
   Span(doc112, 12, 13, label ="CONTRACT1"),
   Span(doc112, 13, 14, label ="POS"),
   Span(doc112, 14, 15, label ="AMOUNT"),
   Span(doc112, 16, 17, label ="ARTICLE"),
   Span(doc112, 17, 18, label ="PRICE"),
   Span(doc112, 18, 19, label ="UNIT"),
   Span(doc112, 20, 21, label ="SUMMA"),
   Span(doc112, 47, 48, label ="TARIFF"),
   Span(doc112, 52, 54, label ="COUNTRY"),
   Span(doc112, 56, 57, label ="PR_SURCH"),
   Span(doc112, 58, 59, label ="SURCHARGE"),
   Span(doc112, 59, 60, label ="TOTAL")]
docs.append(doc112)
print("doc113, 75, #NORDER 2407342; CONTRACT SR-1-06; CONTRACT1 106; POS 13300; AMOUNT 24; ARTICLE 1720000112; PRICE 2,99; UNIT 1; SUMMA 71,76; TARIFF 73181562; COUNTRY Origin unknown; PR_SURCH 15,50; SURCHARGE 11,12; TOTAL 82,88; ")
doc113 = nlp('''Order number: 2407342 Purchase order number: N SR-1-06 106 13300 24 PC 1720000112 2,99 1 PC 71,76 Kit-BFX-IS-M10X35-ISO4762-80-W5 SET-BFX-IS-M10X35-IS0O4762-80-W5 packed per each item Product description: screw Export - Customs tariff no.: 73181562 Country of origin: Origin unknown Material Surcharge 15,50 % 11,12 82,88''')
doc113.ents = [
   Span(doc113, 3, 4, label ="NORDER"),
   Span(doc113, 9, 12, label ="CONTRACT"),
   Span(doc113, 12, 13, label ="CONTRACT1"),
   Span(doc113, 13, 14, label ="POS"),
   Span(doc113, 14, 15, label ="AMOUNT"),
   Span(doc113, 16, 17, label ="ARTICLE"),
   Span(doc113, 17, 18, label ="PRICE"),
   Span(doc113, 18, 19, label ="UNIT"),
   Span(doc113, 20, 21, label ="SUMMA"),
   Span(doc113, 62, 63, label ="TARIFF"),
   Span(doc113, 67, 69, label ="COUNTRY"),
   Span(doc113, 71, 72, label ="PR_SURCH"),
   Span(doc113, 73, 74, label ="SURCHARGE"),
   Span(doc113, 74, 75, label ="TOTAL")]
docs.append(doc113)
print("doc114, 53, #NORDER 2407342; CONTRACT SR-1-06; CONTRACT1 106; POS 13400; AMOUNT 3; ARTICLE 1730002365; PRICE 47,29; UNIT 1; SUMMA 141,87; TARIFF 73072100; COUNTRY Italy; PR_SURCH 15,50; SURCHARGE 21,99; TOTAL 163,86; ")
doc114 = nlp('''Order number: 2407342 Purchase order number: N SR-1-06 106 13400 3 PC 1730002365 47,29 1 PC 141,87 BAS-306-CP-W5 packed per each item Product description: flange Export - Customs tariff no.: 73072100 Country of origin: Italy Material Surcharge 15,50 % 21,99 163,86''')
doc114.ents = [
   Span(doc114, 3, 4, label ="NORDER"),
   Span(doc114, 9, 12, label ="CONTRACT"),
   Span(doc114, 12, 13, label ="CONTRACT1"),
   Span(doc114, 13, 14, label ="POS"),
   Span(doc114, 14, 15, label ="AMOUNT"),
   Span(doc114, 16, 17, label ="ARTICLE"),
   Span(doc114, 17, 18, label ="PRICE"),
   Span(doc114, 18, 19, label ="UNIT"),
   Span(doc114, 20, 21, label ="SUMMA"),
   Span(doc114, 41, 42, label ="TARIFF"),
   Span(doc114, 46, 47, label ="COUNTRY"),
   Span(doc114, 49, 50, label ="PR_SURCH"),
   Span(doc114, 51, 52, label ="SURCHARGE"),
   Span(doc114, 52, 53, label ="TOTAL")]
docs.append(doc114)
print("doc115, 59, #NORDER 2407348; CONTRACT SR-1-06; CONTRACT1 108; POS 13500; AMOUNT 20; ARTICLE 1120001955; PRICE 202,17; UNIT 100; SUMMA 40,43; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 4,61; TOTAL 45,04; ")
doc115 = nlp('''Order number: 2407348 Purchase order number: N SR-1-06 108 13500 20 PC 1120001955 202,17 100 PC 40,43 SPAL-6S-M-W2 SPAL 6 S M W2 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 4,61 45,04''')
doc115.ents = [
   Span(doc115, 3, 4, label ="NORDER"),
   Span(doc115, 9, 12, label ="CONTRACT"),
   Span(doc115, 12, 13, label ="CONTRACT1"),
   Span(doc115, 13, 14, label ="POS"),
   Span(doc115, 14, 15, label ="AMOUNT"),
   Span(doc115, 16, 17, label ="ARTICLE"),
   Span(doc115, 17, 18, label ="PRICE"),
   Span(doc115, 18, 19, label ="UNIT"),
   Span(doc115, 20, 21, label ="SUMMA"),
   Span(doc115, 47, 48, label ="TARIFF"),
   Span(doc115, 52, 53, label ="COUNTRY"),
   Span(doc115, 55, 56, label ="PR_SURCH"),
   Span(doc115, 57, 58, label ="SURCHARGE"),
   Span(doc115, 58, 59, label ="TOTAL")]
docs.append(doc115)
print("doc116, 56, #NORDER 2407349; CONTRACT SR-1-06; CONTRACT1 109; POS 13600; AMOUNT 20; ARTICLE 1730001578; PRICE 3,99; UNIT 1; SUMMA 79,80; TARIFF 73079100; COUNTRY China; PR_SURCH 15,50; SURCHARGE 12,37; TOTAL 92,17; ")
doc116 = nlp('''Order number: 2407349  Purchase order number: N SR-1-06 109 13600 20 PC 1730001578 3,99 1 PC 79,80 BM -G-306-W66 BM-G-306 packed per each item Product description: flange Export - Customs tariff no.: 73079100 Country of origin: China Material Surcharge 15,50 % 12,37 92,17''')
doc116.ents = [
   Span(doc116, 3, 4, label ="NORDER"),
   Span(doc116, 10, 13, label ="CONTRACT"),
   Span(doc116, 13, 14, label ="CONTRACT1"),
   Span(doc116, 14, 15, label ="POS"),
   Span(doc116, 15, 16, label ="AMOUNT"),
   Span(doc116, 17, 18, label ="ARTICLE"),
   Span(doc116, 18, 19, label ="PRICE"),
   Span(doc116, 19, 20, label ="UNIT"),
   Span(doc116, 21, 22, label ="SUMMA"),
   Span(doc116, 44, 45, label ="TARIFF"),
   Span(doc116, 49, 50, label ="COUNTRY"),
   Span(doc116, 52, 53, label ="PR_SURCH"),
   Span(doc116, 54, 55, label ="SURCHARGE"),
   Span(doc116, 55, 56, label ="TOTAL")]
docs.append(doc116)
print("doc117, 66, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 13700; AMOUNT 7; ARTICLE 1130004014; PRICE 4,30; UNIT 100; SUMMA 0,30; TARIFF 73181588; COUNTRY Poland; PR_SURCH 11,40; SURCHARGE 0,03; TOTAL 0,33; ")
doc117 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 13700 7 PC 1130004014 4,30 100 PC 0,30 AS-M6x27-DIN931/933-8.8-W3 AS-M6X27-DIN931/933-8.8-W3 packed per each item Product description: screw Export - Customs tariff no.: 73181588 Country of origin: Poland Material Surcharge 11,40 % 0,03 0,33''')
doc117.ents = [
   Span(doc117, 3, 4, label ="NORDER"),
   Span(doc117, 9, 12, label ="CONTRACT"),
   Span(doc117, 12, 13, label ="CONTRACT1"),
   Span(doc117, 13, 14, label ="POS"),
   Span(doc117, 14, 15, label ="AMOUNT"),
   Span(doc117, 16, 17, label ="ARTICLE"),
   Span(doc117, 17, 18, label ="PRICE"),
   Span(doc117, 18, 19, label ="UNIT"),
   Span(doc117, 20, 21, label ="SUMMA"),
   Span(doc117, 54, 55, label ="TARIFF"),
   Span(doc117, 59, 60, label ="COUNTRY"),
   Span(doc117, 62, 63, label ="PR_SURCH"),
   Span(doc117, 64, 65, label ="SURCHARGE"),
   Span(doc117, 65, 66, label ="TOTAL")]
docs.append(doc117)
print("doc118, 68, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 13800; AMOUNT 62; ARTICLE 1130004020; PRICE 3,93; UNIT 100; SUMMA 2,44; TARIFF 73181588; COUNTRY Origin unknown; PR_SURCH 11,40; SURCHARGE 0,28; TOTAL 2,72; ")
doc118 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 13800 62 PC 1130004020 3,93. 100 PC 2,44 AS-M6x30-DIN931/933-8.8-W3 AS-M6X30-DIN931/933-8.8-W3 packed per each item Product description: screw Export - Customs tariff no.: 73181588 Country of origin: Origin unknown Material Surcharge 11,40 % 0,28 2,72''')
doc118.ents = [
   Span(doc118, 3, 4, label ="NORDER"),
   Span(doc118, 9, 12, label ="CONTRACT"),
   Span(doc118, 12, 13, label ="CONTRACT1"),
   Span(doc118, 13, 14, label ="POS"),
   Span(doc118, 14, 15, label ="AMOUNT"),
   Span(doc118, 16, 17, label ="ARTICLE"),
   Span(doc118, 17, 18, label ="PRICE"),
   Span(doc118, 19, 20, label ="UNIT"),
   Span(doc118, 21, 22, label ="SUMMA"),
   Span(doc118, 55, 56, label ="TARIFF"),
   Span(doc118, 60, 62, label ="COUNTRY"),
   Span(doc118, 64, 65, label ="PR_SURCH"),
   Span(doc118, 66, 67, label ="SURCHARGE"),
   Span(doc118, 67, 68, label ="TOTAL")]
docs.append(doc118)
print("doc119, 68, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 13900; AMOUNT 86; ARTICLE 1130004021; PRICE 4,09; UNIT 100; SUMMA 3,52; TARIFF 73181588; COUNTRY Origin unknown; PR_SURCH 11,40; SURCHARGE 0,40; TOTAL 3,92; ")
doc119 = nlp('''Order number: 2407352   Purchase order number: N SR-1-06 110 13900 86 PC 1130004021 4,09 100 PC 3,52 AS-M6x35-DIN931/933-8.8-W3 AS-M6X35-DIN931/933-8.8-W3 packed per each item Product description: screw Export - Customs tariff no.: 73181588 Country of origin: Origin unknown Material Surcharge 11,40 % 0,40 3,92''')
doc119.ents = [
   Span(doc119, 3, 4, label ="NORDER"),
   Span(doc119, 10, 13, label ="CONTRACT"),
   Span(doc119, 13, 14, label ="CONTRACT1"),
   Span(doc119, 14, 15, label ="POS"),
   Span(doc119, 15, 16, label ="AMOUNT"),
   Span(doc119, 17, 18, label ="ARTICLE"),
   Span(doc119, 18, 19, label ="PRICE"),
   Span(doc119, 19, 20, label ="UNIT"),
   Span(doc119, 21, 22, label ="SUMMA"),
   Span(doc119, 55, 56, label ="TARIFF"),
   Span(doc119, 60, 62, label ="COUNTRY"),
   Span(doc119, 64, 65, label ="PR_SURCH"),
   Span(doc119, 66, 67, label ="SURCHARGE"),
   Span(doc119, 67, 68, label ="TOTAL")]
docs.append(doc119)
print("doc120, 66, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 14000; AMOUNT 4; ARTICLE 1130004022; PRICE 4,30; UNIT 100; SUMMA 0,17; TARIFF 73181588; COUNTRY Taiwan; PR_SURCH 11,40; SURCHARGE 0,02; TOTAL 0,19; ")
doc120 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 14000 4 PC 1130004022 4,30 100 PC 0,17 AS-M6x40-DIN931/933-8.8-W3 AS-M6X40-DIN931/933-8.8-W3 packed per each item Product description: screw Export - Customs tariff no.: 73181588 Country of origin: Taiwan Material Surcharge 11,40 % 0,02 0,19''')
doc120.ents = [
   Span(doc120, 3, 4, label ="NORDER"),
   Span(doc120, 9, 12, label ="CONTRACT"),
   Span(doc120, 12, 13, label ="CONTRACT1"),
   Span(doc120, 13, 14, label ="POS"),
   Span(doc120, 14, 15, label ="AMOUNT"),
   Span(doc120, 16, 17, label ="ARTICLE"),
   Span(doc120, 17, 18, label ="PRICE"),
   Span(doc120, 18, 19, label ="UNIT"),
   Span(doc120, 20, 21, label ="SUMMA"),
   Span(doc120, 54, 55, label ="TARIFF"),
   Span(doc120, 59, 60, label ="COUNTRY"),
   Span(doc120, 62, 63, label ="PR_SURCH"),
   Span(doc120, 64, 65, label ="SURCHARGE"),
   Span(doc120, 65, 66, label ="TOTAL")]
docs.append(doc120)
print("doc121, 67, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 14100; AMOUNT 4; ARTICLE 1130004017; PRICE 5,08; UNIT 100; SUMMA 0,20; TARIFF 73181588; COUNTRY Origin unknown; PR_SURCH 11,40; SURCHARGE 0,02; TOTAL 0,22; ")
doc121 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 14100 4 PC 1130004017 5,08 100 PC 0,20 AS-M6x42-DIN931/933-8.8-W3 AS-M6X42-DIN931/933-8.8-W3 packed per each item Product description: screw Export - Customs tariff no.: 73181588 Country of origin: Origin unknown Material Surcharge 11,40 % 0,02 0,22''')
doc121.ents = [
   Span(doc121, 3, 4, label ="NORDER"),
   Span(doc121, 9, 12, label ="CONTRACT"),
   Span(doc121, 12, 13, label ="CONTRACT1"),
   Span(doc121, 13, 14, label ="POS"),
   Span(doc121, 14, 15, label ="AMOUNT"),
   Span(doc121, 16, 17, label ="ARTICLE"),
   Span(doc121, 17, 18, label ="PRICE"),
   Span(doc121, 18, 19, label ="UNIT"),
   Span(doc121, 20, 21, label ="SUMMA"),
   Span(doc121, 54, 55, label ="TARIFF"),
   Span(doc121, 59, 61, label ="COUNTRY"),
   Span(doc121, 63, 64, label ="PR_SURCH"),
   Span(doc121, 65, 66, label ="SURCHARGE"),
   Span(doc121, 66, 67, label ="TOTAL")]
docs.append(doc121)
print("doc122, 68, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 14200; AMOUNT 34; ARTICLE 1130004023; PRICE 4,51; UNIT 100; SUMMA 1,53; TARIFF 73181588; COUNTRY Origin unknown; PR_SURCH 11,40; SURCHARGE 0,17; TOTAL 1,70; ")
doc122 = nlp('''Order number: 2407352   Purchase order number: N SR-1-06 110 14200 34 PC 1130004023 4,51 100 PC 1,53 AS-M6x45-DIN931/933-8.8-W3 AS-M6X45-DIN931/933-8.8-W3 packed per each item Product description: screw Export - Customs tariff no.: 73181588 Country of origin: Origin unknown Material Surcharge 11,40 % 0,17 1,70''')
doc122.ents = [
   Span(doc122, 3, 4, label ="NORDER"),
   Span(doc122, 10, 13, label ="CONTRACT"),
   Span(doc122, 13, 14, label ="CONTRACT1"),
   Span(doc122, 14, 15, label ="POS"),
   Span(doc122, 15, 16, label ="AMOUNT"),
   Span(doc122, 17, 18, label ="ARTICLE"),
   Span(doc122, 18, 19, label ="PRICE"),
   Span(doc122, 19, 20, label ="UNIT"),
   Span(doc122, 21, 22, label ="SUMMA"),
   Span(doc122, 55, 56, label ="TARIFF"),
   Span(doc122, 60, 62, label ="COUNTRY"),
   Span(doc122, 64, 65, label ="PR_SURCH"),
   Span(doc122, 66, 67, label ="SURCHARGE"),
   Span(doc122, 67, 68, label ="TOTAL")]
docs.append(doc122)
print("doc123, 67, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 14300; AMOUNT 52; ARTICLE 1130004018; PRICE 6,24; UNIT 100; SUMMA 3,24; TARIFF 73181588; COUNTRY Origin unknown; PR_SURCH 11,40; SURCHARGE 0,37; TOTAL 3,61; ")
doc123 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 14300 52 PC 1130004018 6,24 100 PC 3,24 AS-M6x57-DIN931/933-8.8-W3 AS-M6X57-DIN931/933-8.8-W3 packed per each item Product description: screw Export - Customs tariff no.: 73181588 Country of origin: Origin unknown Material Surcharge 11,40 % 0,37 3,61''')
doc123.ents = [
   Span(doc123, 3, 4, label ="NORDER"),
   Span(doc123, 9, 12, label ="CONTRACT"),
   Span(doc123, 12, 13, label ="CONTRACT1"),
   Span(doc123, 13, 14, label ="POS"),
   Span(doc123, 14, 15, label ="AMOUNT"),
   Span(doc123, 16, 17, label ="ARTICLE"),
   Span(doc123, 17, 18, label ="PRICE"),
   Span(doc123, 18, 19, label ="UNIT"),
   Span(doc123, 20, 21, label ="SUMMA"),
   Span(doc123, 54, 55, label ="TARIFF"),
   Span(doc123, 59, 61, label ="COUNTRY"),
   Span(doc123, 63, 64, label ="PR_SURCH"),
   Span(doc123, 65, 66, label ="SURCHARGE"),
   Span(doc123, 66, 67, label ="TOTAL")]
docs.append(doc123)
print("doc124, 67, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 14400; AMOUNT 2; ARTICLE 1130004024; PRICE 5,48; UNIT 100; SUMMA 0,11; TARIFF 73181588; COUNTRY Origin unknown; PR_SURCH 11,40; SURCHARGE 0,01; TOTAL 0,12; ")
doc124 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 14400 2 PC 1130004024 5,48 100 PC 0,11 AS-M6x60-DIN931/933-8.8-W3 AS-M6X60-DIN931/933-8.8-W3 packed per each item Product description: screw Export - Customs tariff no.: 73181588 Country of origin: Origin unknown Material Surcharge 11,40 % 0,01 0,12''')
doc124.ents = [
   Span(doc124, 3, 4, label ="NORDER"),
   Span(doc124, 9, 12, label ="CONTRACT"),
   Span(doc124, 12, 13, label ="CONTRACT1"),
   Span(doc124, 13, 14, label ="POS"),
   Span(doc124, 14, 15, label ="AMOUNT"),
   Span(doc124, 16, 17, label ="ARTICLE"),
   Span(doc124, 17, 18, label ="PRICE"),
   Span(doc124, 18, 19, label ="UNIT"),
   Span(doc124, 20, 21, label ="SUMMA"),
   Span(doc124, 54, 55, label ="TARIFF"),
   Span(doc124, 59, 61, label ="COUNTRY"),
   Span(doc124, 63, 64, label ="PR_SURCH"),
   Span(doc124, 65, 66, label ="SURCHARGE"),
   Span(doc124, 66, 67, label ="TOTAL")]
docs.append(doc124)
print("doc125, 68, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 14500; AMOUNT 1; ARTICLE 1130004280; PRICE 5,08; UNIT 100; SUMMA 0,05; TARIFF 73181588; COUNTRY Origin unknown; PR_SURCH 11,40; SURCHARGE 0,01; TOTAL 0,06; ")
doc125 = nlp('''Order number: 2407352   Purchase order number: N SR-1-06 110 14500 1 PC 1130004280 5,08 100 PC 0,05 AS-M8x35-DIN931/933-8.8-W3 AS-M8X35-DIN931/933-8.8-W3 packed per each item Product description: screw Export - Customs tariff no.: 73181588 Country of origin: Origin unknown Material Surcharge 11,40 % 0,01 0,06''')
doc125.ents = [
   Span(doc125, 3, 4, label ="NORDER"),
   Span(doc125, 10, 13, label ="CONTRACT"),
   Span(doc125, 13, 14, label ="CONTRACT1"),
   Span(doc125, 14, 15, label ="POS"),
   Span(doc125, 15, 16, label ="AMOUNT"),
   Span(doc125, 17, 18, label ="ARTICLE"),
   Span(doc125, 18, 19, label ="PRICE"),
   Span(doc125, 19, 20, label ="UNIT"),
   Span(doc125, 21, 22, label ="SUMMA"),
   Span(doc125, 55, 56, label ="TARIFF"),
   Span(doc125, 60, 62, label ="COUNTRY"),
   Span(doc125, 64, 65, label ="PR_SURCH"),
   Span(doc125, 66, 67, label ="SURCHARGE"),
   Span(doc125, 67, 68, label ="TOTAL")]
docs.append(doc125)
print("doc126, 66, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 14600; AMOUNT 10; ARTICLE 1130004283; PRICE 9,19; UNIT 100; SUMMA 0,92; TARIFF 73181588; COUNTRY Taiwan; PR_SURCH 11,40; SURCHARGE 0,10; TOTAL 1,02; ")
doc126 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 14600 10 PC 1130004283 9,19 100 PC 0,92 AS-M8x60-DIN931/933-8.8-W3 AS-M8X60-DIN931/933-8.8-W3 packed per each item Product description: screw Export - Customs tariff no.: 73181588 Country of origin: Taiwan Material Surcharge 11,40 % 0,10 1,02''')
doc126.ents = [
   Span(doc126, 3, 4, label ="NORDER"),
   Span(doc126, 9, 12, label ="CONTRACT"),
   Span(doc126, 12, 13, label ="CONTRACT1"),
   Span(doc126, 13, 14, label ="POS"),
   Span(doc126, 14, 15, label ="AMOUNT"),
   Span(doc126, 16, 17, label ="ARTICLE"),
   Span(doc126, 17, 18, label ="PRICE"),
   Span(doc126, 18, 19, label ="UNIT"),
   Span(doc126, 20, 21, label ="SUMMA"),
   Span(doc126, 54, 55, label ="TARIFF"),
   Span(doc126, 59, 60, label ="COUNTRY"),
   Span(doc126, 62, 63, label ="PR_SURCH"),
   Span(doc126, 64, 65, label ="SURCHARGE"),
   Span(doc126, 65, 66, label ="TOTAL")]
docs.append(doc126)
print("doc127, 62, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 14700; AMOUNT 16; ARTICLE 1130004570; PRICE 5,76; UNIT 100; SUMMA 0,92; TARIFF 73181692; COUNTRY China; PR_SURCH 11,40; SURCHARGE 0,10; TOTAL 1,02; ")
doc127 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 14700 16 PC 1130004570 5,76 100 PC 0,92 MUS-M12-DINENISO4032-W3 MUS M12 DIN EN ISO 4032 W3 packed per each item Product description: nuts Export - Customs tariff no.: 73181692 Country of origin: China Material Surcharge 11,40 % 0,10 1,02''')
doc127.ents = [
   Span(doc127, 3, 4, label ="NORDER"),
   Span(doc127, 9, 12, label ="CONTRACT"),
   Span(doc127, 12, 13, label ="CONTRACT1"),
   Span(doc127, 13, 14, label ="POS"),
   Span(doc127, 14, 15, label ="AMOUNT"),
   Span(doc127, 16, 17, label ="ARTICLE"),
   Span(doc127, 17, 18, label ="PRICE"),
   Span(doc127, 18, 19, label ="UNIT"),
   Span(doc127, 20, 21, label ="SUMMA"),
   Span(doc127, 50, 51, label ="TARIFF"),
   Span(doc127, 55, 56, label ="COUNTRY"),
   Span(doc127, 58, 59, label ="PR_SURCH"),
   Span(doc127, 60, 61, label ="SURCHARGE"),
   Span(doc127, 61, 62, label ="TOTAL")]
docs.append(doc127)
print("doc128, 64, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 14800; AMOUNT 344; ARTICLE 1130004571; PRICE 8,10; UNIT 100; SUMMA 27,86; TARIFF 73181699; COUNTRY Origin unknown; PR_SURCH 11,40; SURCHARGE 3,18; TOTAL 31,04; ")
doc128 = nlp('''Order number: 2407352   Purchase order number: N SR-1-06 110 14800 344 PC 1130004571 8,10 100 PC 27,86 MUS-M16-DINENISO4032-W3 MUS M16 DIN EN ISO 4032 W3 packed per each item Product description: nuts Export - Customs tariff no.: 73181699 Country of origin: Origin unknown Material Surcharge 11,40 % 3,18 31,04''')
doc128.ents = [
   Span(doc128, 3, 4, label ="NORDER"),
   Span(doc128, 10, 13, label ="CONTRACT"),
   Span(doc128, 13, 14, label ="CONTRACT1"),
   Span(doc128, 14, 15, label ="POS"),
   Span(doc128, 15, 16, label ="AMOUNT"),
   Span(doc128, 17, 18, label ="ARTICLE"),
   Span(doc128, 18, 19, label ="PRICE"),
   Span(doc128, 19, 20, label ="UNIT"),
   Span(doc128, 21, 22, label ="SUMMA"),
   Span(doc128, 51, 52, label ="TARIFF"),
   Span(doc128, 56, 58, label ="COUNTRY"),
   Span(doc128, 60, 61, label ="PR_SURCH"),
   Span(doc128, 62, 63, label ="SURCHARGE"),
   Span(doc128, 63, 64, label ="TOTAL")]
docs.append(doc128)
print("doc129, 62, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 14900; AMOUNT 100; ARTICLE 1130004572; PRICE 16,16; UNIT 100; SUMMA 16,16; TARIFF 73181699; COUNTRY China; PR_SURCH 11,40; SURCHARGE 1,84; TOTAL 18,00; ")
doc129 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 14900 100 PC 1130004572 16,16 100 PC 16,16 MUS-M20-DINENISO4032-W3 MUS M20 DIN EN ISO 4032 W3 packed per each item Product description: nuts Export - Customs tariff no.: 73181699 Country of origin: China Material Surcharge 11,40 % 1,84 18,00''')
doc129.ents = [
   Span(doc129, 3, 4, label ="NORDER"),
   Span(doc129, 9, 12, label ="CONTRACT"),
   Span(doc129, 12, 13, label ="CONTRACT1"),
   Span(doc129, 13, 14, label ="POS"),
   Span(doc129, 14, 15, label ="AMOUNT"),
   Span(doc129, 16, 17, label ="ARTICLE"),
   Span(doc129, 17, 18, label ="PRICE"),
   Span(doc129, 18, 19, label ="UNIT"),
   Span(doc129, 20, 21, label ="SUMMA"),
   Span(doc129, 50, 51, label ="TARIFF"),
   Span(doc129, 55, 56, label ="COUNTRY"),
   Span(doc129, 58, 59, label ="PR_SURCH"),
   Span(doc129, 60, 61, label ="SURCHARGE"),
   Span(doc129, 61, 62, label ="TOTAL")]
docs.append(doc129)
print("doc130, 55, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 15000; AMOUNT 1; ARTICLE 6100088655; PRICE 300,21; UNIT 100; SUMMA 3,00; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,34; TOTAL 3,34; ")
doc130 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 15000 1 PC 6100088655 300,21 100 PC 3,00 RB+ RUL-38-PA-W32 packed per each item Product description: clamp combination Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 0,34 3,34''')
doc130.ents = [
   Span(doc130, 3, 4, label ="NORDER"),
   Span(doc130, 9, 12, label ="CONTRACT"),
   Span(doc130, 12, 13, label ="CONTRACT1"),
   Span(doc130, 13, 14, label ="POS"),
   Span(doc130, 14, 15, label ="AMOUNT"),
   Span(doc130, 16, 17, label ="ARTICLE"),
   Span(doc130, 17, 18, label ="PRICE"),
   Span(doc130, 18, 19, label ="UNIT"),
   Span(doc130, 20, 21, label ="SUMMA"),
   Span(doc130, 43, 44, label ="TARIFF"),
   Span(doc130, 48, 49, label ="COUNTRY"),
   Span(doc130, 51, 52, label ="PR_SURCH"),
   Span(doc130, 53, 54, label ="SURCHARGE"),
   Span(doc130, 54, 55, label ="TOTAL")]
docs.append(doc130)
print("doc131, 55, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 15400; AMOUNT 25; ARTICLE 1130003001; PRICE 26,38; UNIT 100; SUMMA 6,60; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,75; TOTAL 7,35; ")
doc131 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110    15400 25 PC 1130003001 26,38 100 PC 6,60 112-PA 112 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 0,75 7,35''')
doc131.ents = [
   Span(doc131, 3, 4, label ="NORDER"),
   Span(doc131, 9, 12, label ="CONTRACT"),
   Span(doc131, 12, 13, label ="CONTRACT1"),
   Span(doc131, 14, 15, label ="POS"),
   Span(doc131, 15, 16, label ="AMOUNT"),
   Span(doc131, 17, 18, label ="ARTICLE"),
   Span(doc131, 18, 19, label ="PRICE"),
   Span(doc131, 19, 20, label ="UNIT"),
   Span(doc131, 21, 22, label ="SUMMA"),
   Span(doc131, 43, 44, label ="TARIFF"),
   Span(doc131, 48, 49, label ="COUNTRY"),
   Span(doc131, 51, 52, label ="PR_SURCH"),
   Span(doc131, 53, 54, label ="SURCHARGE"),
   Span(doc131, 54, 55, label ="TOTAL")]
docs.append(doc131)
print("doc132, 54, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 15500; AMOUNT 25; ARTICLE 1130005366; PRICE 36,71; UNIT 100; SUMMA 9,18; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 1,05; TOTAL 10,23; ")
doc132 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 15500 25 PC 1130005366 36,71 100 PC 9,18 217.2-PA 217,2 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 1,05 10,23''')
doc132.ents = [
   Span(doc132, 3, 4, label ="NORDER"),
   Span(doc132, 9, 12, label ="CONTRACT"),
   Span(doc132, 12, 13, label ="CONTRACT1"),
   Span(doc132, 13, 14, label ="POS"),
   Span(doc132, 14, 15, label ="AMOUNT"),
   Span(doc132, 16, 17, label ="ARTICLE"),
   Span(doc132, 17, 18, label ="PRICE"),
   Span(doc132, 18, 19, label ="UNIT"),
   Span(doc132, 20, 21, label ="SUMMA"),
   Span(doc132, 42, 43, label ="TARIFF"),
   Span(doc132, 47, 48, label ="COUNTRY"),
   Span(doc132, 50, 51, label ="PR_SURCH"),
   Span(doc132, 52, 53, label ="SURCHARGE"),
   Span(doc132, 53, 54, label ="TOTAL")]
docs.append(doc132)
print("doc133, 54, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 15600; AMOUNT 25; ARTICLE 1130005630; PRICE 26,77; UNIT 100; SUMMA 6,69; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,76; TOTAL 7,45; ")
doc133 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 15600 25 PC 1130005630 26,77 100 PC 6,69 325-PP 325 PP packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 0,76 7,45''')
doc133.ents = [
   Span(doc133, 3, 4, label ="NORDER"),
   Span(doc133, 9, 12, label ="CONTRACT"),
   Span(doc133, 12, 13, label ="CONTRACT1"),
   Span(doc133, 13, 14, label ="POS"),
   Span(doc133, 14, 15, label ="AMOUNT"),
   Span(doc133, 16, 17, label ="ARTICLE"),
   Span(doc133, 17, 18, label ="PRICE"),
   Span(doc133, 18, 19, label ="UNIT"),
   Span(doc133, 20, 21, label ="SUMMA"),
   Span(doc133, 42, 43, label ="TARIFF"),
   Span(doc133, 47, 48, label ="COUNTRY"),
   Span(doc133, 50, 51, label ="PR_SURCH"),
   Span(doc133, 52, 53, label ="SURCHARGE"),
   Span(doc133, 53, 54, label ="TOTAL")]
docs.append(doc133)
print("doc134, 55, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 15700; AMOUNT 25; ARTICLE 1130003772; PRICE 55,26; UNIT 100; SUMMA 13,82; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 1,58; TOTAL 15,40; ")
doc134 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110    15700 25 PC 1130003772 55,26 100 PC 13,82 430-PA 430 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 1,58 15,40''')
doc134.ents = [
   Span(doc134, 3, 4, label ="NORDER"),
   Span(doc134, 9, 12, label ="CONTRACT"),
   Span(doc134, 12, 13, label ="CONTRACT1"),
   Span(doc134, 14, 15, label ="POS"),
   Span(doc134, 15, 16, label ="AMOUNT"),
   Span(doc134, 17, 18, label ="ARTICLE"),
   Span(doc134, 18, 19, label ="PRICE"),
   Span(doc134, 19, 20, label ="UNIT"),
   Span(doc134, 21, 22, label ="SUMMA"),
   Span(doc134, 43, 44, label ="TARIFF"),
   Span(doc134, 48, 49, label ="COUNTRY"),
   Span(doc134, 51, 52, label ="PR_SURCH"),
   Span(doc134, 53, 54, label ="SURCHARGE"),
   Span(doc134, 54, 55, label ="TOTAL")]
docs.append(doc134)
print("doc135, 54, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 15800; AMOUNT 25; ARTICLE 1130006023; PRICE 85,35; UNIT 100; SUMMA 21,34; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 2,43; TOTAL 23,77; ")
doc135 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 15800 25 PC 1130006023 85,35 100 PC 21,34 538-PA 538 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 2,43 23,77''')
doc135.ents = [
   Span(doc135, 3, 4, label ="NORDER"),
   Span(doc135, 9, 12, label ="CONTRACT"),
   Span(doc135, 12, 13, label ="CONTRACT1"),
   Span(doc135, 13, 14, label ="POS"),
   Span(doc135, 14, 15, label ="AMOUNT"),
   Span(doc135, 16, 17, label ="ARTICLE"),
   Span(doc135, 17, 18, label ="PRICE"),
   Span(doc135, 18, 19, label ="UNIT"),
   Span(doc135, 20, 21, label ="SUMMA"),
   Span(doc135, 42, 43, label ="TARIFF"),
   Span(doc135, 47, 48, label ="COUNTRY"),
   Span(doc135, 50, 51, label ="PR_SURCH"),
   Span(doc135, 52, 53, label ="SURCHARGE"),
   Span(doc135, 53, 54, label ="TOTAL")]
docs.append(doc135)
print("doc136, 54, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 15900; AMOUNT 10; ARTICLE 1130006040; PRICE 131,47; UNIT 100; SUMMA 13,15; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 1,50; TOTAL 14,65; ")
doc136 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 15900 10 PC 1130006040 131,47 100 PC 13,15 538/38-PA 538/38 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 1,50 14,65''')
doc136.ents = [
   Span(doc136, 3, 4, label ="NORDER"),
   Span(doc136, 9, 12, label ="CONTRACT"),
   Span(doc136, 12, 13, label ="CONTRACT1"),
   Span(doc136, 13, 14, label ="POS"),
   Span(doc136, 14, 15, label ="AMOUNT"),
   Span(doc136, 16, 17, label ="ARTICLE"),
   Span(doc136, 17, 18, label ="PRICE"),
   Span(doc136, 18, 19, label ="UNIT"),
   Span(doc136, 20, 21, label ="SUMMA"),
   Span(doc136, 42, 43, label ="TARIFF"),
   Span(doc136, 47, 48, label ="COUNTRY"),
   Span(doc136, 50, 51, label ="PR_SURCH"),
   Span(doc136, 52, 53, label ="SURCHARGE"),
   Span(doc136, 53, 54, label ="TOTAL")]
docs.append(doc136)
print("doc137, 55, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 16000; AMOUNT 20; ARTICLE 1130006214; PRICE 231,10; UNIT 100; SUMMA 46,22; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 5,27; TOTAL 51,49; ")
doc137 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110    16000 20 PC 1130006214 231,10 100 PC 46,22 757.2-PA 757,2 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 5,27 51,49''')
doc137.ents = [
   Span(doc137, 3, 4, label ="NORDER"),
   Span(doc137, 9, 12, label ="CONTRACT"),
   Span(doc137, 12, 13, label ="CONTRACT1"),
   Span(doc137, 14, 15, label ="POS"),
   Span(doc137, 15, 16, label ="AMOUNT"),
   Span(doc137, 17, 18, label ="ARTICLE"),
   Span(doc137, 18, 19, label ="PRICE"),
   Span(doc137, 19, 20, label ="UNIT"),
   Span(doc137, 21, 22, label ="SUMMA"),
   Span(doc137, 43, 44, label ="TARIFF"),
   Span(doc137, 48, 49, label ="COUNTRY"),
   Span(doc137, 51, 52, label ="PR_SURCH"),
   Span(doc137, 53, 54, label ="SURCHARGE"),
   Span(doc137, 54, 55, label ="TOTAL")]
docs.append(doc137)
print("doc138, 54, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 16100; AMOUNT 10; ARTICLE 1130006216; PRICE 110,54; UNIT 100; SUMMA 11,05; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 1,26; TOTAL 12,31; ")
doc138 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 16100 10 PC 1130006216 110,54 100 PC 11,05 757.2-PP 757,2 PP packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 1,26 12,31''')
doc138.ents = [
   Span(doc138, 3, 4, label ="NORDER"),
   Span(doc138, 9, 12, label ="CONTRACT"),
   Span(doc138, 12, 13, label ="CONTRACT1"),
   Span(doc138, 13, 14, label ="POS"),
   Span(doc138, 14, 15, label ="AMOUNT"),
   Span(doc138, 16, 17, label ="ARTICLE"),
   Span(doc138, 17, 18, label ="PRICE"),
   Span(doc138, 18, 19, label ="UNIT"),
   Span(doc138, 20, 21, label ="SUMMA"),
   Span(doc138, 42, 43, label ="TARIFF"),
   Span(doc138, 47, 48, label ="COUNTRY"),
   Span(doc138, 50, 51, label ="PR_SURCH"),
   Span(doc138, 52, 53, label ="SURCHARGE"),
   Span(doc138, 53, 54, label ="TOTAL")]
docs.append(doc138)
print("doc139, 55, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 16200; AMOUNT 100; ARTICLE 1130004846; PRICE 5,30; UNIT 100; SUMMA 5,30; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,60; TOTAL 5,90; ")
doc139 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 16200 100 PC 1130004846 5,30 100 PC 5,30 LB-209.5-PP LB 209,5 PP packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 0,60 5,90''')
doc139.ents = [
   Span(doc139, 3, 4, label ="NORDER"),
   Span(doc139, 9, 12, label ="CONTRACT"),
   Span(doc139, 12, 13, label ="CONTRACT1"),
   Span(doc139, 13, 14, label ="POS"),
   Span(doc139, 14, 15, label ="AMOUNT"),
   Span(doc139, 16, 17, label ="ARTICLE"),
   Span(doc139, 17, 18, label ="PRICE"),
   Span(doc139, 18, 19, label ="UNIT"),
   Span(doc139, 20, 21, label ="SUMMA"),
   Span(doc139, 43, 44, label ="TARIFF"),
   Span(doc139, 48, 49, label ="COUNTRY"),
   Span(doc139, 51, 52, label ="PR_SURCH"),
   Span(doc139, 53, 54, label ="SURCHARGE"),
   Span(doc139, 54, 55, label ="TOTAL")]
docs.append(doc139)
print("doc140, 74, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 16300; AMOUNT 4; ARTICLE 6100084956; PRICE 17,07; UNIT 1; SUMMA 68,28; TARIFF 84812010; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 4,71; TOTAL 72,99; ")
doc140 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110   16300 4 PC 6100084956 17,07 1 PC 68,28 BBV-2-25S-8001-M 2/2-Way Block Ball Valve DN20 25S-PN420, POM, FPM, ZiNi packed per each item Product description: valve Export - Customs tariff no.: 84812010 Country of origin: Germany Material Surcharge 6,90 % 4,71 72,99 EAC - Eurasian Conformity''')
doc140.ents = [
   Span(doc140, 3, 4, label ="NORDER"),
   Span(doc140, 9, 12, label ="CONTRACT"),
   Span(doc140, 12, 13, label ="CONTRACT1"),
   Span(doc140, 14, 15, label ="POS"),
   Span(doc140, 15, 16, label ="AMOUNT"),
   Span(doc140, 17, 18, label ="ARTICLE"),
   Span(doc140, 18, 19, label ="PRICE"),
   Span(doc140, 19, 20, label ="UNIT"),
   Span(doc140, 21, 22, label ="SUMMA"),
   Span(doc140, 58, 59, label ="TARIFF"),
   Span(doc140, 63, 64, label ="COUNTRY"),
   Span(doc140, 66, 67, label ="PR_SURCH"),
   Span(doc140, 68, 69, label ="SURCHARGE"),
   Span(doc140, 69, 70, label ="TOTAL")]
docs.append(doc140)
print("doc141, 73, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 16400; AMOUNT 6; ARTICLE 6100084958; PRICE 21,57; UNIT 1; SUMMA 129,42; TARIFF 84812010; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 8,93; TOTAL 138,35; ")
doc141 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 16400 6 PC 6100084958 21,57 1 PC 129,42 BBV-2-30S-8001-M 2/2-Way Block Ball Valve DN25 30S-PN350, POM, FPM, ZiNi packed per each item Product description: valve Export - Customs tariff no.: 84812010 Country of origin: Germany Material Surcharge 6,90 % 8,93 138,35 EAC - Eurasian Conformity''')
doc141.ents = [
   Span(doc141, 3, 4, label ="NORDER"),
   Span(doc141, 9, 12, label ="CONTRACT"),
   Span(doc141, 12, 13, label ="CONTRACT1"),
   Span(doc141, 13, 14, label ="POS"),
   Span(doc141, 14, 15, label ="AMOUNT"),
   Span(doc141, 16, 17, label ="ARTICLE"),
   Span(doc141, 17, 18, label ="PRICE"),
   Span(doc141, 18, 19, label ="UNIT"),
   Span(doc141, 20, 21, label ="SUMMA"),
   Span(doc141, 57, 58, label ="TARIFF"),
   Span(doc141, 62, 63, label ="COUNTRY"),
   Span(doc141, 65, 66, label ="PR_SURCH"),
   Span(doc141, 67, 68, label ="SURCHARGE"),
   Span(doc141, 68, 69, label ="TOTAL")]
docs.append(doc141)
print("doc142, 76, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 16500; AMOUNT 2; ARTICLE 6100084960; PRICE 28,59; UNIT 1; SUMMA 57,18; TARIFF 84812010; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 3,95; TOTAL 61,13; ")
doc142 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 16500 2 PC 6100084960 28,59 1 PC 57,18 BBV-2-38SDN25-8001-M 2/2-Way Block Ball Valve DN25 38S-PN315, POM, FPM, ZiNi packed per each item Product description: valve Export - Customs tariff no.: 84812010 Country of origin: Germany Material Surcharge 6,90 % 3,95 61,13   EAC - Eurasian Conformity''')
doc142.ents = [
   Span(doc142, 3, 4, label ="NORDER"),
   Span(doc142, 9, 12, label ="CONTRACT"),
   Span(doc142, 12, 13, label ="CONTRACT1"),
   Span(doc142, 13, 14, label ="POS"),
   Span(doc142, 14, 15, label ="AMOUNT"),
   Span(doc142, 16, 17, label ="ARTICLE"),
   Span(doc142, 17, 18, label ="PRICE"),
   Span(doc142, 18, 19, label ="UNIT"),
   Span(doc142, 20, 21, label ="SUMMA"),
   Span(doc142, 59, 60, label ="TARIFF"),
   Span(doc142, 64, 65, label ="COUNTRY"),
   Span(doc142, 67, 68, label ="PR_SURCH"),
   Span(doc142, 69, 70, label ="SURCHARGE"),
   Span(doc142, 70, 71, label ="TOTAL")]
docs.append(doc142)
print("doc143, 56, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 16600; AMOUNT 50; ARTICLE 1130000258; PRICE 6,83; UNIT 100; SUMMA 3,42; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,39; TOTAL 3,81; ")
doc143 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 16600 50 PC 1130000258 6,83 100 PC 3,42 DP-1 a-W3 DP 1a W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 0,39 3,81''')
doc143.ents = [
   Span(doc143, 3, 4, label ="NORDER"),
   Span(doc143, 9, 12, label ="CONTRACT"),
   Span(doc143, 12, 13, label ="CONTRACT1"),
   Span(doc143, 13, 14, label ="POS"),
   Span(doc143, 14, 15, label ="AMOUNT"),
   Span(doc143, 16, 17, label ="ARTICLE"),
   Span(doc143, 17, 18, label ="PRICE"),
   Span(doc143, 18, 19, label ="UNIT"),
   Span(doc143, 20, 21, label ="SUMMA"),
   Span(doc143, 44, 45, label ="TARIFF"),
   Span(doc143, 49, 50, label ="COUNTRY"),
   Span(doc143, 52, 53, label ="PR_SURCH"),
   Span(doc143, 54, 55, label ="SURCHARGE"),
   Span(doc143, 55, 56, label ="TOTAL")]
docs.append(doc143)
print("doc144, 55, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 16700; AMOUNT 50; ARTICLE 1130000261; PRICE 7,39; UNIT 100; SUMMA 3,70; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,42; TOTAL 4,12; ")
doc144 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 16700 50 PC 1130000261 7,39 100 PC 3,70 DP-2-W3 DP 2 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 0,42 4,12''')
doc144.ents = [
   Span(doc144, 3, 4, label ="NORDER"),
   Span(doc144, 9, 12, label ="CONTRACT"),
   Span(doc144, 12, 13, label ="CONTRACT1"),
   Span(doc144, 13, 14, label ="POS"),
   Span(doc144, 14, 15, label ="AMOUNT"),
   Span(doc144, 16, 17, label ="ARTICLE"),
   Span(doc144, 17, 18, label ="PRICE"),
   Span(doc144, 18, 19, label ="UNIT"),
   Span(doc144, 20, 21, label ="SUMMA"),
   Span(doc144, 43, 44, label ="TARIFF"),
   Span(doc144, 48, 49, label ="COUNTRY"),
   Span(doc144, 51, 52, label ="PR_SURCH"),
   Span(doc144, 53, 54, label ="SURCHARGE"),
   Span(doc144, 54, 55, label ="TOTAL")]
docs.append(doc144)
print("doc145, 56, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 16800; AMOUNT 25; ARTICLE 1130000264; PRICE 8,38; UNIT 100; SUMMA 2,10; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,24; TOTAL 2,34; ")
doc145 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 16800 25 PC 1130000264 8,38 100 PC 2,10 DP-3-W3 DP 3 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 0,24    2,34''')
doc145.ents = [
   Span(doc145, 3, 4, label ="NORDER"),
   Span(doc145, 9, 12, label ="CONTRACT"),
   Span(doc145, 12, 13, label ="CONTRACT1"),
   Span(doc145, 13, 14, label ="POS"),
   Span(doc145, 14, 15, label ="AMOUNT"),
   Span(doc145, 16, 17, label ="ARTICLE"),
   Span(doc145, 17, 18, label ="PRICE"),
   Span(doc145, 18, 19, label ="UNIT"),
   Span(doc145, 20, 21, label ="SUMMA"),
   Span(doc145, 43, 44, label ="TARIFF"),
   Span(doc145, 48, 49, label ="COUNTRY"),
   Span(doc145, 51, 52, label ="PR_SURCH"),
   Span(doc145, 53, 54, label ="SURCHARGE"),
   Span(doc145, 55, 56, label ="TOTAL")]
docs.append(doc145)
print("doc146, 55, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 16900; AMOUNT 50; ARTICLE 1130000269; PRICE 11,33; UNIT 100; SUMMA 5,67; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,65; TOTAL 6,32; ")
doc146 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 16900 50 PC 1130000269 11,33 100 PC 5,67 DP-5-W3 DP 5 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 0,65 6,32''')
doc146.ents = [
   Span(doc146, 3, 4, label ="NORDER"),
   Span(doc146, 9, 12, label ="CONTRACT"),
   Span(doc146, 12, 13, label ="CONTRACT1"),
   Span(doc146, 13, 14, label ="POS"),
   Span(doc146, 14, 15, label ="AMOUNT"),
   Span(doc146, 16, 17, label ="ARTICLE"),
   Span(doc146, 17, 18, label ="PRICE"),
   Span(doc146, 18, 19, label ="UNIT"),
   Span(doc146, 20, 21, label ="SUMMA"),
   Span(doc146, 43, 44, label ="TARIFF"),
   Span(doc146, 48, 49, label ="COUNTRY"),
   Span(doc146, 51, 52, label ="PR_SURCH"),
   Span(doc146, 53, 54, label ="SURCHARGE"),
   Span(doc146, 54, 55, label ="TOTAL")]
docs.append(doc146)
print("doc147, 54, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 17000; AMOUNT 20; ARTICLE 1130001501; PRICE 42,57; UNIT 100; SUMMA 8,51; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,97; TOTAL 9,48; ")
doc147 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 17000 20 PC 1130001501 42,57 100 PC 8,51 DP-7 -W3 DP 7 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 0,97 9,48''')
doc147.ents = [
   Span(doc147, 3, 4, label ="NORDER"),
   Span(doc147, 9, 12, label ="CONTRACT"),
   Span(doc147, 12, 13, label ="CONTRACT1"),
   Span(doc147, 13, 14, label ="POS"),
   Span(doc147, 14, 15, label ="AMOUNT"),
   Span(doc147, 16, 17, label ="ARTICLE"),
   Span(doc147, 17, 18, label ="PRICE"),
   Span(doc147, 18, 19, label ="UNIT"),
   Span(doc147, 20, 21, label ="SUMMA"),
   Span(doc147, 42, 43, label ="TARIFF"),
   Span(doc147, 47, 48, label ="COUNTRY"),
   Span(doc147, 50, 51, label ="PR_SURCH"),
   Span(doc147, 52, 53, label ="SURCHARGE"),
   Span(doc147, 53, 54, label ="TOTAL")]
docs.append(doc147)
print("doc148, 55, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 17100; AMOUNT 86; ARTICLE 1130002248; PRICE 379,72; UNIT 100; SUMMA 326,56; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 37,23; TOTAL 363,79; ")
doc148 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 17100 86 PC 1130002248 379,72 100 PC 326,56 RUL-133-PA RUL 133 PA packed per each item Product description: Handle Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 37,23   363,79''')
doc148.ents = [
   Span(doc148, 3, 4, label ="NORDER"),
   Span(doc148, 9, 12, label ="CONTRACT"),
   Span(doc148, 12, 13, label ="CONTRACT1"),
   Span(doc148, 13, 14, label ="POS"),
   Span(doc148, 14, 15, label ="AMOUNT"),
   Span(doc148, 16, 17, label ="ARTICLE"),
   Span(doc148, 17, 18, label ="PRICE"),
   Span(doc148, 18, 19, label ="UNIT"),
   Span(doc148, 20, 21, label ="SUMMA"),
   Span(doc148, 42, 43, label ="TARIFF"),
   Span(doc148, 47, 48, label ="COUNTRY"),
   Span(doc148, 50, 51, label ="PR_SURCH"),
   Span(doc148, 52, 53, label ="SURCHARGE"),
   Span(doc148, 54, 55, label ="TOTAL")]
docs.append(doc148)
print("doc149, 54, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 17200; AMOUNT 4; ARTICLE 1130002244; PRICE 277,00; UNIT 100; SUMMA 11,08; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 1,26; TOTAL 12,34; ")
doc149 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 17200 4 PC 1130002244 277,00 100 PC 11,08 RUL-76.1-PA RUL 76,1 PA packed per each item Product description: Handle Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 1,26 12,34''')
doc149.ents = [
   Span(doc149, 3, 4, label ="NORDER"),
   Span(doc149, 9, 12, label ="CONTRACT"),
   Span(doc149, 12, 13, label ="CONTRACT1"),
   Span(doc149, 13, 14, label ="POS"),
   Span(doc149, 14, 15, label ="AMOUNT"),
   Span(doc149, 16, 17, label ="ARTICLE"),
   Span(doc149, 17, 18, label ="PRICE"),
   Span(doc149, 18, 19, label ="UNIT"),
   Span(doc149, 20, 21, label ="SUMMA"),
   Span(doc149, 42, 43, label ="TARIFF"),
   Span(doc149, 47, 48, label ="COUNTRY"),
   Span(doc149, 50, 51, label ="PR_SURCH"),
   Span(doc149, 52, 53, label ="SURCHARGE"),
   Span(doc149, 53, 54, label ="TOTAL")]
docs.append(doc149)
print("doc150, 58, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 17300; AMOUNT 25; ARTICLE 1120001184; PRICE 27,92; UNIT 100; SUMMA 6,98; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,80; TOTAL 7,78; ")
doc150 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 17300 25 PC 1120001184 27,92 100 PC 6,98 SP-1A-M-W3 SP 1a M W3 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 0,80 7,78''')
doc150.ents = [
   Span(doc150, 3, 4, label ="NORDER"),
   Span(doc150, 9, 12, label ="CONTRACT"),
   Span(doc150, 12, 13, label ="CONTRACT1"),
   Span(doc150, 13, 14, label ="POS"),
   Span(doc150, 14, 15, label ="AMOUNT"),
   Span(doc150, 16, 17, label ="ARTICLE"),
   Span(doc150, 17, 18, label ="PRICE"),
   Span(doc150, 18, 19, label ="UNIT"),
   Span(doc150, 20, 21, label ="SUMMA"),
   Span(doc150, 46, 47, label ="TARIFF"),
   Span(doc150, 51, 52, label ="COUNTRY"),
   Span(doc150, 54, 55, label ="PR_SURCH"),
   Span(doc150, 56, 57, label ="SURCHARGE"),
   Span(doc150, 57, 58, label ="TOTAL")]
docs.append(doc150)
print("doc151, 59, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 17400; AMOUNT 50; ARTICLE 1120001156; PRICE 26,58; UNIT 100; SUMMA 13,29; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 1,52; TOTAL 14,81; ")
doc151 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 17400 50 PC 1120001156 26,58 100 PC 13,29 SP-2-M-W2 SP 2 M W2 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 1,52    14,81''')
doc151.ents = [
   Span(doc151, 3, 4, label ="NORDER"),
   Span(doc151, 9, 12, label ="CONTRACT"),
   Span(doc151, 12, 13, label ="CONTRACT1"),
   Span(doc151, 13, 14, label ="POS"),
   Span(doc151, 14, 15, label ="AMOUNT"),
   Span(doc151, 16, 17, label ="ARTICLE"),
   Span(doc151, 17, 18, label ="PRICE"),
   Span(doc151, 18, 19, label ="UNIT"),
   Span(doc151, 20, 21, label ="SUMMA"),
   Span(doc151, 46, 47, label ="TARIFF"),
   Span(doc151, 51, 52, label ="COUNTRY"),
   Span(doc151, 54, 55, label ="PR_SURCH"),
   Span(doc151, 56, 57, label ="SURCHARGE"),
   Span(doc151, 58, 59, label ="TOTAL")]
docs.append(doc151)
print("doc152, 58, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 17500; AMOUNT 25; ARTICLE 1120001192; PRICE 35,95; UNIT 100; SUMMA 8,99; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 1,02; TOTAL 10,01; ")
doc152 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 17500 25 PC 1120001192 35,95 100 PC 8,99 SP-5-M-W3 SP 5 M W3 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 1,02 10,01''')
doc152.ents = [
   Span(doc152, 3, 4, label ="NORDER"),
   Span(doc152, 9, 12, label ="CONTRACT"),
   Span(doc152, 12, 13, label ="CONTRACT1"),
   Span(doc152, 13, 14, label ="POS"),
   Span(doc152, 14, 15, label ="AMOUNT"),
   Span(doc152, 16, 17, label ="ARTICLE"),
   Span(doc152, 17, 18, label ="PRICE"),
   Span(doc152, 18, 19, label ="UNIT"),
   Span(doc152, 20, 21, label ="SUMMA"),
   Span(doc152, 46, 47, label ="TARIFF"),
   Span(doc152, 51, 52, label ="COUNTRY"),
   Span(doc152, 54, 55, label ="PR_SURCH"),
   Span(doc152, 56, 57, label ="SURCHARGE"),
   Span(doc152, 57, 58, label ="TOTAL")]
docs.append(doc152)
print("doc153, 59, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 17600; AMOUNT 10; ARTICLE 1120002550; PRICE 61,13; UNIT 100; SUMMA 6,11; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,70; TOTAL 6,81; ")
doc153 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 17600 10 PC 1120002550 61,13. 100 PC 6,11 SP-5D-M-W3 SP 5 DM W3 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 0,70 6,81''')
doc153.ents = [
   Span(doc153, 3, 4, label ="NORDER"),
   Span(doc153, 9, 12, label ="CONTRACT"),
   Span(doc153, 12, 13, label ="CONTRACT1"),
   Span(doc153, 13, 14, label ="POS"),
   Span(doc153, 14, 15, label ="AMOUNT"),
   Span(doc153, 16, 17, label ="ARTICLE"),
   Span(doc153, 17, 18, label ="PRICE"),
   Span(doc153, 19, 20, label ="UNIT"),
   Span(doc153, 21, 22, label ="SUMMA"),
   Span(doc153, 47, 48, label ="TARIFF"),
   Span(doc153, 52, 53, label ="COUNTRY"),
   Span(doc153, 55, 56, label ="PR_SURCH"),
   Span(doc153, 57, 58, label ="SURCHARGE"),
   Span(doc153, 58, 59, label ="TOTAL")]
docs.append(doc153)
print("doc154, 59, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 17700; AMOUNT 10; ARTICLE 1120001180; PRICE 49,63; UNIT 100; SUMMA 4,96; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,57; TOTAL 5,53; ")
doc154 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 17700 10 PC 1120001180 49,63 100 PC 4,96 SP-7-M-W2 SP 7M W2 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 0,57    5,53''')
doc154.ents = [
   Span(doc154, 3, 4, label ="NORDER"),
   Span(doc154, 9, 12, label ="CONTRACT"),
   Span(doc154, 12, 13, label ="CONTRACT1"),
   Span(doc154, 13, 14, label ="POS"),
   Span(doc154, 14, 15, label ="AMOUNT"),
   Span(doc154, 16, 17, label ="ARTICLE"),
   Span(doc154, 17, 18, label ="PRICE"),
   Span(doc154, 18, 19, label ="UNIT"),
   Span(doc154, 20, 21, label ="SUMMA"),
   Span(doc154, 46, 47, label ="TARIFF"),
   Span(doc154, 51, 52, label ="COUNTRY"),
   Span(doc154, 54, 55, label ="PR_SURCH"),
   Span(doc154, 56, 57, label ="SURCHARGE"),
   Span(doc154, 58, 59, label ="TOTAL")]
docs.append(doc154)
print("doc155, 58, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 17800; AMOUNT 25; ARTICLE 1120001232; PRICE 31,44; UNIT 100; SUMMA 7,86; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,90; TOTAL 8,76; ")
doc155 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 17800 25 PC 1120001232 31,44 100 PC 7,86 SPV-3-M-W2 SPV 3 M W2 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 0,90 8,76''')
doc155.ents = [
   Span(doc155, 3, 4, label ="NORDER"),
   Span(doc155, 9, 12, label ="CONTRACT"),
   Span(doc155, 12, 13, label ="CONTRACT1"),
   Span(doc155, 13, 14, label ="POS"),
   Span(doc155, 14, 15, label ="AMOUNT"),
   Span(doc155, 16, 17, label ="ARTICLE"),
   Span(doc155, 17, 18, label ="PRICE"),
   Span(doc155, 18, 19, label ="UNIT"),
   Span(doc155, 20, 21, label ="SUMMA"),
   Span(doc155, 46, 47, label ="TARIFF"),
   Span(doc155, 51, 52, label ="COUNTRY"),
   Span(doc155, 54, 55, label ="PR_SURCH"),
   Span(doc155, 56, 57, label ="SURCHARGE"),
   Span(doc155, 57, 58, label ="TOTAL")]
docs.append(doc155)
print("doc156, 58, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 17900; AMOUNT 10; ARTICLE 1120001243; PRICE 63,86; UNIT 100; SUMMA 6,39; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,73; TOTAL 7,12; ")
doc156 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 17900 10 PC 1120001243 63,86 100 PC 6,39 SPV-7-M-W2 SPV 7M W2 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 0,73 7,12''')
doc156.ents = [
   Span(doc156, 3, 4, label ="NORDER"),
   Span(doc156, 9, 12, label ="CONTRACT"),
   Span(doc156, 12, 13, label ="CONTRACT1"),
   Span(doc156, 13, 14, label ="POS"),
   Span(doc156, 14, 15, label ="AMOUNT"),
   Span(doc156, 16, 17, label ="ARTICLE"),
   Span(doc156, 17, 18, label ="PRICE"),
   Span(doc156, 18, 19, label ="UNIT"),
   Span(doc156, 20, 21, label ="SUMMA"),
   Span(doc156, 46, 47, label ="TARIFF"),
   Span(doc156, 51, 52, label ="COUNTRY"),
   Span(doc156, 54, 55, label ="PR_SURCH"),
   Span(doc156, 56, 57, label ="SURCHARGE"),
   Span(doc156, 57, 58, label ="TOTAL")]
docs.append(doc156)
print("doc157, 61, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 18000; AMOUNT 86; ARTICLE 1130004343; PRICE 263,16; UNIT 100; SUMMA 226,32; TARIFF 73269098; COUNTRY Europ.; PR_SURCH 11,40; SURCHARGE 25,80; TOTAL 252,12; ")
doc157 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 18000 86 PC 1130004343 263,16 100 PC 226,32 RB-A-148-W32 RB W32 A= 148 packed per each item Product description: Handle Export - Customs tariff no.: 73269098 Country of origin: Europ. Comm. Material Surcharge 11,40 % 25,80   252,12''')
doc157.ents = [
   Span(doc157, 3, 4, label ="NORDER"),
   Span(doc157, 9, 12, label ="CONTRACT"),
   Span(doc157, 12, 13, label ="CONTRACT1"),
   Span(doc157, 13, 14, label ="POS"),
   Span(doc157, 14, 15, label ="AMOUNT"),
   Span(doc157, 16, 17, label ="ARTICLE"),
   Span(doc157, 17, 18, label ="PRICE"),
   Span(doc157, 18, 19, label ="UNIT"),
   Span(doc157, 20, 21, label ="SUMMA"),
   Span(doc157, 45, 46, label ="TARIFF"),
   Span(doc157, 50, 52, label ="COUNTRY"),
   Span(doc157, 56, 57, label ="PR_SURCH"),
   Span(doc157, 58, 59, label ="SURCHARGE"),
   Span(doc157, 60, 61, label ="TOTAL")]
docs.append(doc157)
print("doc158, 57, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 18100; AMOUNT 9; ARTICLE 1130004349; PRICE 543,61; UNIT 100; SUMMA 48,92; TARIFF 73269098; COUNTRY Italy; PR_SURCH 11,40; SURCHARGE 5,58; TOTAL 54,50; ")
doc158 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 18100 9 PC 1130004349 543,61 100 PC 48,92 RB-A-228-W32 RB W32 A= 228 packed per each item Product description: Handle Export - Customs tariff no.: 73269098 Country of origin: Italy Material Surcharge 11,40 % 5,58 54,50''')
doc158.ents = [
   Span(doc158, 3, 4, label ="NORDER"),
   Span(doc158, 9, 12, label ="CONTRACT"),
   Span(doc158, 12, 13, label ="CONTRACT1"),
   Span(doc158, 13, 14, label ="POS"),
   Span(doc158, 14, 15, label ="AMOUNT"),
   Span(doc158, 16, 17, label ="ARTICLE"),
   Span(doc158, 17, 18, label ="PRICE"),
   Span(doc158, 18, 19, label ="UNIT"),
   Span(doc158, 20, 21, label ="SUMMA"),
   Span(doc158, 45, 46, label ="TARIFF"),
   Span(doc158, 50, 51, label ="COUNTRY"),
   Span(doc158, 53, 54, label ="PR_SURCH"),
   Span(doc158, 55, 56, label ="SURCHARGE"),
   Span(doc158, 56, 57, label ="TOTAL")]
docs.append(doc158)
print("doc159, 60, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 18200; AMOUNT 4; ARTICLE 1130004337; PRICE 110,80; UNIT 100; SUMMA 4,43; TARIFF 73269098; COUNTRY Europ.; PR_SURCH 11,40; SURCHARGE 0,51; TOTAL 4,94; ")
doc159 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 18200 4 PC 1130004337 110,80 100 PC 4,43 RB-A-82-W32 RB W32 A= 82 packed per each item Product description: Handle Export - Customs tariff no.: 73269098 Country of origin: Europ. Comm. Material Surcharge 11,40 % 0,51 4,94''')
doc159.ents = [
   Span(doc159, 3, 4, label ="NORDER"),
   Span(doc159, 9, 12, label ="CONTRACT"),
   Span(doc159, 12, 13, label ="CONTRACT1"),
   Span(doc159, 13, 14, label ="POS"),
   Span(doc159, 14, 15, label ="AMOUNT"),
   Span(doc159, 16, 17, label ="ARTICLE"),
   Span(doc159, 17, 18, label ="PRICE"),
   Span(doc159, 18, 19, label ="UNIT"),
   Span(doc159, 20, 21, label ="SUMMA"),
   Span(doc159, 45, 46, label ="TARIFF"),
   Span(doc159, 50, 52, label ="COUNTRY"),
   Span(doc159, 56, 57, label ="PR_SURCH"),
   Span(doc159, 58, 59, label ="SURCHARGE"),
   Span(doc159, 59, 60, label ="TOTAL")]
docs.append(doc159)
print("doc160, 56, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 18300; AMOUNT 2; ARTICLE 1110031092; PRICE 491,20; UNIT 100; SUMMA 9,82; TARIFF 73269098; COUNTRY Germany; PR_SURCH 10,40; SURCHARGE 1,02; TOTAL 10,84; ")
doc160 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 18300 2 PC 1110031092 491,20 100 PC 9,82 RBD-A-38 -W5-compl RBD W5 A 38 KOMPL packed per each item Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 10,40 % 1,02 10,84   ''')
doc160.ents = [
   Span(doc160, 3, 4, label ="NORDER"),
   Span(doc160, 9, 12, label ="CONTRACT"),
   Span(doc160, 12, 13, label ="CONTRACT1"),
   Span(doc160, 13, 14, label ="POS"),
   Span(doc160, 14, 15, label ="AMOUNT"),
   Span(doc160, 16, 17, label ="ARTICLE"),
   Span(doc160, 17, 18, label ="PRICE"),
   Span(doc160, 18, 19, label ="UNIT"),
   Span(doc160, 20, 21, label ="SUMMA"),
   Span(doc160, 43, 44, label ="TARIFF"),
   Span(doc160, 48, 49, label ="COUNTRY"),
   Span(doc160, 51, 52, label ="PR_SURCH"),
   Span(doc160, 53, 54, label ="SURCHARGE"),
   Span(doc160, 54, 55, label ="TOTAL")]
docs.append(doc160)
print("doc161, 59, #NORDER 2407352; CONTRACT SR-1-06; CONTRACT1 110; POS 18600; AMOUNT 6; ARTICLE 1130021984; PRICE 485,32; UNIT 100; SUMMA 29,12; TARIFF 73269098; COUNTRY Germany; PR_SURCH 10,40; SURCHARGE 3,03; TOTAL 32,15; ")
doc161 = nlp('''Order number: 2407352 Purchase order number: N SR-1-06 110 18600 6 PC 1130021984 485,32 100 PC 29,12 DIN1593-43-W5 DIN 1593-43 W5 packed per each item Product description: Pipe clamp Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 10,40 % 3,03 32,15''')
doc161.ents = [
   Span(doc161, 3, 4, label ="NORDER"),
   Span(doc161, 9, 12, label ="CONTRACT"),
   Span(doc161, 12, 13, label ="CONTRACT1"),
   Span(doc161, 13, 14, label ="POS"),
   Span(doc161, 14, 15, label ="AMOUNT"),
   Span(doc161, 16, 17, label ="ARTICLE"),
   Span(doc161, 17, 18, label ="PRICE"),
   Span(doc161, 18, 19, label ="UNIT"),
   Span(doc161, 20, 21, label ="SUMMA"),
   Span(doc161, 47, 48, label ="TARIFF"),
   Span(doc161, 52, 53, label ="COUNTRY"),
   Span(doc161, 55, 56, label ="PR_SURCH"),
   Span(doc161, 57, 58, label ="SURCHARGE"),
   Span(doc161, 58, 59, label ="TOTAL")]
docs.append(doc161)
print("doc162, 66, #NORDER 2407354; CONTRACT SR-1-06; CONTRACT1 111; POS 18700; AMOUNT 4; ARTICLE 6100073857; PRICE 17,18; UNIT 1; SUMMA 68,72; TARIFF 84812010; COUNTRY Italy; PR_SURCH 6,90; SURCHARGE 4,74; TOTAL 73,46; ")
doc162 = nlp('''Order number: 2407354 Purchase order number: N SR-1-06 111 18700 4 PC 6100073857 17,18 1 PC 68,72 QRC-IA-12-M-G08-V-W5I IA12-2-IGFO8-VA packed per each item Export - Customs tariff no.: 84812010 Country of origin: Italy Material Surcharge 6,90 % 4,74 73,46 EAC - Eurasian Conformity''')
doc162.ents = [
   Span(doc162, 3, 4, label ="NORDER"),
   Span(doc162, 9, 12, label ="CONTRACT"),
   Span(doc162, 12, 13, label ="CONTRACT1"),
   Span(doc162, 13, 14, label ="POS"),
   Span(doc162, 14, 15, label ="AMOUNT"),
   Span(doc162, 16, 17, label ="ARTICLE"),
   Span(doc162, 17, 18, label ="PRICE"),
   Span(doc162, 18, 19, label ="UNIT"),
   Span(doc162, 20, 21, label ="SUMMA"),
   Span(doc162, 50, 51, label ="TARIFF"),
   Span(doc162, 55, 56, label ="COUNTRY"),
   Span(doc162, 58, 59, label ="PR_SURCH"),
   Span(doc162, 60, 61, label ="SURCHARGE"),
   Span(doc162, 61, 62, label ="TOTAL")]
docs.append(doc162)
print("doc163, 67, #NORDER 2407354; CONTRACT SR-1-06; CONTRACT1 111; POS 18800; AMOUNT 4; ARTICLE 6100068861; PRICE 4,24; UNIT 1; SUMMA 16,96; TARIFF 84812010; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 1,17; TOTAL 18,13; ")
doc163 = nlp('''Order number: 2407354 Purchase order number: N SR-1-06 111 18800 4 PC 6100068861 (*) 4,24 1 PC 16,96 QRC-HP-1 2 -F-1 5L-B-W3 HP10-1-L1522N packed per each item Export - Customs tariff no.: 84812010 Country of origin: Germany Material Surcharge 6,90 % 1,17 18,13 EAC - Eurasian Conformity   ''')
doc163.ents = [
   Span(doc163, 3, 4, label ="NORDER"),
   Span(doc163, 9, 12, label ="CONTRACT"),
   Span(doc163, 12, 13, label ="CONTRACT1"),
   Span(doc163, 13, 14, label ="POS"),
   Span(doc163, 14, 15, label ="AMOUNT"),
   Span(doc163, 16, 17, label ="ARTICLE"),
   Span(doc163, 20, 21, label ="PRICE"),
   Span(doc163, 21, 22, label ="UNIT"),
   Span(doc163, 23, 24, label ="SUMMA"),
   Span(doc163, 50, 51, label ="TARIFF"),
   Span(doc163, 55, 56, label ="COUNTRY"),
   Span(doc163, 58, 59, label ="PR_SURCH"),
   Span(doc163, 60, 61, label ="SURCHARGE"),
   Span(doc163, 61, 62, label ="TOTAL")]
docs.append(doc163)
print("doc164, 70, #NORDER 2407354; CONTRACT SR-1-06; CONTRACT1 111; POS 18900; AMOUNT 8; ARTICLE 6100111045; PRICE 4,38; UNIT 1; SUMMA 35,04; TARIFF 84812010; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 2,42; TOTAL 37,46; ")
doc164 = nlp('''Order number: 2407354 Purchase order number: N SR-1-06 111 18900 8 PC 6100111045 (*) 4,38 1 PC 35,04 QRC-HP-1 2 -F-1 5LB-B-W3 HP10-1-N1522N packed per each item Product description: coupling Export - Customs tariff no.: 84812010 Country of origin: Germany Material Surcharge 6,90 % 2,42 37,46 EAC - Eurasian Conformity''')
doc164.ents = [
   Span(doc164, 3, 4, label ="NORDER"),
   Span(doc164, 9, 12, label ="CONTRACT"),
   Span(doc164, 12, 13, label ="CONTRACT1"),
   Span(doc164, 13, 14, label ="POS"),
   Span(doc164, 14, 15, label ="AMOUNT"),
   Span(doc164, 16, 17, label ="ARTICLE"),
   Span(doc164, 20, 21, label ="PRICE"),
   Span(doc164, 21, 22, label ="UNIT"),
   Span(doc164, 23, 24, label ="SUMMA"),
   Span(doc164, 54, 55, label ="TARIFF"),
   Span(doc164, 59, 60, label ="COUNTRY"),
   Span(doc164, 62, 63, label ="PR_SURCH"),
   Span(doc164, 64, 65, label ="SURCHARGE"),
   Span(doc164, 65, 66, label ="TOTAL")]
docs.append(doc164)
print("doc165, 70, #NORDER 2407354; CONTRACT SR-1-06; CONTRACT1 111; POS 19000; AMOUNT 4; ARTICLE 6100111093; PRICE 1,93; UNIT 1; SUMMA 7,72; TARIFF 84812010; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 0,53; TOTAL 8,25; ")
doc165 = nlp('''Order number: 2407354 Purchase order number: N SR-1-06 111 19000 4 PC 6100111093 (*) 1,93 1 PC 7,72 QRC-HP-1 2-M-15LB-B-W3 HP10-2-N1522N packed per each item Product description: coupling Export - Customs tariff no.: 84812010 Country of origin: Germany Material Surcharge 6,90 % 0,53 8,25 EAC - Eurasian Conformity''')
doc165.ents = [
   Span(doc165, 3, 4, label ="NORDER"),
   Span(doc165, 9, 12, label ="CONTRACT"),
   Span(doc165, 12, 13, label ="CONTRACT1"),
   Span(doc165, 13, 14, label ="POS"),
   Span(doc165, 14, 15, label ="AMOUNT"),
   Span(doc165, 16, 17, label ="ARTICLE"),
   Span(doc165, 20, 21, label ="PRICE"),
   Span(doc165, 21, 22, label ="UNIT"),
   Span(doc165, 23, 24, label ="SUMMA"),
   Span(doc165, 54, 55, label ="TARIFF"),
   Span(doc165, 59, 60, label ="COUNTRY"),
   Span(doc165, 62, 63, label ="PR_SURCH"),
   Span(doc165, 64, 65, label ="SURCHARGE"),
   Span(doc165, 65, 66, label ="TOTAL")]
docs.append(doc165)
print("doc166, 66, #NORDER 2407354; CONTRACT SR-1-06; CONTRACT1 111; POS 19100; AMOUNT 12; ARTICLE 6100069025; PRICE 12,11; UNIT 1; SUMMA 145,32; TARIFF 84812010; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 10,03; TOTAL 155,35; ")
doc166 = nlp('''Order number: 2407354 Purchase order number: N SR-1-06 111 19100 12 PC 6100069025 (*) 12,11 1 PC 145,32 QRC-HP-1 9 -F-20SB-BT-W66 HP12-1-T2030 packed per each item Export - Customs tariff no.: 84812010 Country of origin: Germany Material Surcharge 6,90 % 10,03 155,35   EAC - Eurasian Conformity''')
doc166.ents = [
   Span(doc166, 3, 4, label ="NORDER"),
   Span(doc166, 9, 12, label ="CONTRACT"),
   Span(doc166, 12, 13, label ="CONTRACT1"),
   Span(doc166, 13, 14, label ="POS"),
   Span(doc166, 14, 15, label ="AMOUNT"),
   Span(doc166, 16, 17, label ="ARTICLE"),
   Span(doc166, 20, 21, label ="PRICE"),
   Span(doc166, 21, 22, label ="UNIT"),
   Span(doc166, 23, 24, label ="SUMMA"),
   Span(doc166, 49, 50, label ="TARIFF"),
   Span(doc166, 54, 55, label ="COUNTRY"),
   Span(doc166, 57, 58, label ="PR_SURCH"),
   Span(doc166, 59, 60, label ="SURCHARGE"),
   Span(doc166, 60, 61, label ="TOTAL")]
docs.append(doc166)
print("doc167, 65, #NORDER 2407354; CONTRACT SR-1-06; CONTRACT1 111; POS 19200; AMOUNT 8; ARTICLE 6100069049; PRICE 6,09; UNIT 1; SUMMA 48,72; TARIFF 84812010; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 3,36; TOTAL 52,08; ")
doc167 = nlp('''Order number: 2407354 Purchase order number: N SR-1-06 111 19200 8 PC 6100069049 (*) 6,09 1 PC 48,72 QRC-HP-19-M-20SB-B-W66 HP12-2-T2030 packed per each item Export - Customs tariff no.: 84812010 Country of origin: Germany Material Surcharge 6,90 % 3,36 52,08 EAC - Eurasian Conformity''')
doc167.ents = [
   Span(doc167, 3, 4, label ="NORDER"),
   Span(doc167, 9, 12, label ="CONTRACT"),
   Span(doc167, 12, 13, label ="CONTRACT1"),
   Span(doc167, 13, 14, label ="POS"),
   Span(doc167, 14, 15, label ="AMOUNT"),
   Span(doc167, 16, 17, label ="ARTICLE"),
   Span(doc167, 20, 21, label ="PRICE"),
   Span(doc167, 21, 22, label ="UNIT"),
   Span(doc167, 23, 24, label ="SUMMA"),
   Span(doc167, 49, 50, label ="TARIFF"),
   Span(doc167, 54, 55, label ="COUNTRY"),
   Span(doc167, 57, 58, label ="PR_SURCH"),
   Span(doc167, 59, 60, label ="SURCHARGE"),
   Span(doc167, 60, 61, label ="TOTAL")]
docs.append(doc167)
print("doc168, 65, #NORDER 2407354; CONTRACT SR-1-06; CONTRACT1 111; POS 19300; AMOUNT 4; ARTICLE 6100068787; PRICE 3,98; UNIT 1; SUMMA 15,92; TARIFF 84812010; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 1,10; TOTAL 17,02; ")
doc168 = nlp('''Order number: 2407354 Purchase order number: N SR-1-06 111 19300 4 PC 6100068787 (*) 3,98 1 PC 15,92 QRC-HP-10-M-12LB-B-W66 HP08-2-N1218 packed per each item Export - Customs tariff no.: 84812010 Country of origin: Germany Material Surcharge 6,90 % 1,10 17,02 EAC - Eurasian Conformity''')
doc168.ents = [
   Span(doc168, 3, 4, label ="NORDER"),
   Span(doc168, 9, 12, label ="CONTRACT"),
   Span(doc168, 12, 13, label ="CONTRACT1"),
   Span(doc168, 13, 14, label ="POS"),
   Span(doc168, 14, 15, label ="AMOUNT"),
   Span(doc168, 16, 17, label ="ARTICLE"),
   Span(doc168, 20, 21, label ="PRICE"),
   Span(doc168, 21, 22, label ="UNIT"),
   Span(doc168, 23, 24, label ="SUMMA"),
   Span(doc168, 49, 50, label ="TARIFF"),
   Span(doc168, 54, 55, label ="COUNTRY"),
   Span(doc168, 57, 58, label ="PR_SURCH"),
   Span(doc168, 59, 60, label ="SURCHARGE"),
   Span(doc168, 60, 61, label ="TOTAL")]
docs.append(doc168)
print("doc169, 57, #NORDER 2407355; CONTRACT SR-1-06; CONTRACT1 112; POS 19400; AMOUNT 2; ARTICLE 6030003799; PRICE 232,43; UNIT 100; SUMMA 4,65; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 0,32; TOTAL 4,97; ")
doc169 = nlp('''Order number: 2407355 Purchase order number: N SR-1-06 112 19400 2 PC 6030003799 (*) 232,43 100 PC 4,65 FI-VSK-16S-W3 packed per each item Product description: Plug Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 0,32 4,97   ''')
doc169.ents = [
   Span(doc169, 3, 4, label ="NORDER"),
   Span(doc169, 9, 12, label ="CONTRACT"),
   Span(doc169, 12, 13, label ="CONTRACT1"),
   Span(doc169, 13, 14, label ="POS"),
   Span(doc169, 14, 15, label ="AMOUNT"),
   Span(doc169, 16, 17, label ="ARTICLE"),
   Span(doc169, 20, 21, label ="PRICE"),
   Span(doc169, 21, 22, label ="UNIT"),
   Span(doc169, 23, 24, label ="SUMMA"),
   Span(doc169, 44, 45, label ="TARIFF"),
   Span(doc169, 49, 50, label ="COUNTRY"),
   Span(doc169, 52, 53, label ="PR_SURCH"),
   Span(doc169, 54, 55, label ="SURCHARGE"),
   Span(doc169, 55, 56, label ="TOTAL")]
docs.append(doc169)
print("doc170, 71, #NORDER 2407355; CONTRACT SR-1-06; CONTRACT1 112; POS 19500; AMOUNT 2; ARTICLE 1210026048; PRICE 8,80; UNIT 1; SUMMA 17,60; TARIFF 84818073; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 2,01; TOTAL 19,61; ")
doc170 = nlp('''Order number: 2407355 Purchase order number: N SR-1-06 112 19500 2 PC 1210026048 (*) 8,80 1 PC 17,60 SMK-20-16S-G-W3-MS SMK-20-16S-B-G-W3-MS packed per each item Product description: coupling Export - Customs tariff no.: 84818073 Country of origin: Germany Material Surcharge 11,40 % 2,01 19,61''')
doc170.ents = [
   Span(doc170, 3, 4, label ="NORDER"),
   Span(doc170, 9, 12, label ="CONTRACT"),
   Span(doc170, 12, 13, label ="CONTRACT1"),
   Span(doc170, 13, 14, label ="POS"),
   Span(doc170, 14, 15, label ="AMOUNT"),
   Span(doc170, 16, 17, label ="ARTICLE"),
   Span(doc170, 20, 21, label ="PRICE"),
   Span(doc170, 21, 22, label ="UNIT"),
   Span(doc170, 23, 24, label ="SUMMA"),
   Span(doc170, 59, 60, label ="TARIFF"),
   Span(doc170, 64, 65, label ="COUNTRY"),
   Span(doc170, 67, 68, label ="PR_SURCH"),
   Span(doc170, 69, 70, label ="SURCHARGE"),
   Span(doc170, 70, 71, label ="TOTAL")]
docs.append(doc170)
print("doc171, 57, #NORDER 2407356; CONTRACT SR-1-06; CONTRACT1 113; POS 19600; AMOUNT 200; ARTICLE 1130005326; PRICE 87,51; UNIT 100; SUMMA 175,02; TARIFF 76169910; COUNTRY Lithuania; PR_SURCH 11,40; SURCHARGE 19,95; TOTAL 194,97; ")
doc171 = nlp('''Order number: 2407356 Purchase order number: N SR-1-06 113 19600 200 PC 1130005326 (*) 87,51 100 PC 175,02 216-AL 216 AL packed per each item Product description: Pipe clamp Export - Customs tariff no.: 76169910 Country of origin: Lithuania Material Surcharge 11,40 % 19,95 194,97''')
doc171.ents = [
   Span(doc171, 3, 4, label ="NORDER"),
   Span(doc171, 9, 12, label ="CONTRACT"),
   Span(doc171, 12, 13, label ="CONTRACT1"),
   Span(doc171, 13, 14, label ="POS"),
   Span(doc171, 14, 15, label ="AMOUNT"),
   Span(doc171, 16, 17, label ="ARTICLE"),
   Span(doc171, 20, 21, label ="PRICE"),
   Span(doc171, 21, 22, label ="UNIT"),
   Span(doc171, 23, 24, label ="SUMMA"),
   Span(doc171, 45, 46, label ="TARIFF"),
   Span(doc171, 50, 51, label ="COUNTRY"),
   Span(doc171, 53, 54, label ="PR_SURCH"),
   Span(doc171, 55, 56, label ="SURCHARGE"),
   Span(doc171, 56, 57, label ="TOTAL")]
docs.append(doc171)
print("doc172, 58, #NORDER 2407356; CONTRACT SR-1-06; CONTRACT1 113; POS 19700; AMOUNT 50; ARTICLE 1130005624; PRICE 95,52; UNIT 100; SUMMA 47,76; TARIFF 76169910; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 5,44; TOTAL 53,20; ")
doc172 = nlp('''Order number: 2407356 Purchase order number: N SR-1-06 113 19700 50 PC 1130005624 (*) 95,52 100 PC 47,76 325-AL 325 AL packed per each item Product description: Pipe clamp Export - Customs tariff no.: 76169910 Country of origin: Germany Material Surcharge 11,40 % 5,44 53,20   ''')
doc172.ents = [
   Span(doc172, 3, 4, label ="NORDER"),
   Span(doc172, 9, 12, label ="CONTRACT"),
   Span(doc172, 12, 13, label ="CONTRACT1"),
   Span(doc172, 13, 14, label ="POS"),
   Span(doc172, 14, 15, label ="AMOUNT"),
   Span(doc172, 16, 17, label ="ARTICLE"),
   Span(doc172, 20, 21, label ="PRICE"),
   Span(doc172, 21, 22, label ="UNIT"),
   Span(doc172, 23, 24, label ="SUMMA"),
   Span(doc172, 45, 46, label ="TARIFF"),
   Span(doc172, 50, 51, label ="COUNTRY"),
   Span(doc172, 53, 54, label ="PR_SURCH"),
   Span(doc172, 55, 56, label ="SURCHARGE"),
   Span(doc172, 56, 57, label ="TOTAL")]
docs.append(doc172)
print("doc173, 57, #NORDER 2407356; CONTRACT SR-1-06; CONTRACT1 113; POS 19800; AMOUNT 200; ARTICLE 1130005761; PRICE 105,08; UNIT 100; SUMMA 210,16; TARIFF 76169910; COUNTRY Lithuania; PR_SURCH 11,40; SURCHARGE 23,96; TOTAL 234,12; ")
doc173 = nlp('''Order number: 2407356 Purchase order number: N SR-1-06 113 19800 200 PC 1130005761 (*) 105,08 100 PC 210,16 426.9-AL 426,9 AL packed per each item Product description: Pipe clamp Export - Customs tariff no.: 76169910 Country of origin: Lithuania Material Surcharge 11,40 % 23,96 234,12''')
doc173.ents = [
   Span(doc173, 3, 4, label ="NORDER"),
   Span(doc173, 9, 12, label ="CONTRACT"),
   Span(doc173, 12, 13, label ="CONTRACT1"),
   Span(doc173, 13, 14, label ="POS"),
   Span(doc173, 14, 15, label ="AMOUNT"),
   Span(doc173, 16, 17, label ="ARTICLE"),
   Span(doc173, 20, 21, label ="PRICE"),
   Span(doc173, 21, 22, label ="UNIT"),
   Span(doc173, 23, 24, label ="SUMMA"),
   Span(doc173, 45, 46, label ="TARIFF"),
   Span(doc173, 50, 51, label ="COUNTRY"),
   Span(doc173, 53, 54, label ="PR_SURCH"),
   Span(doc173, 55, 56, label ="SURCHARGE"),
   Span(doc173, 56, 57, label ="TOTAL")]
docs.append(doc173)
print("doc174, 57, #NORDER 2407356; CONTRACT SR-1-06; CONTRACT1 113; POS 19900; AMOUNT 150; ARTICLE 1130005948; PRICE 164,86; UNIT 100; SUMMA 247,29; TARIFF 76169910; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 28,19; TOTAL 275,48; ")
doc174 = nlp('''Order number: 2407356 Purchase order number: N SR-1-06 113 19900 150 PC 1130005948 (*) 164,86 100 PC 247,29 532-AL 532 AL packed per each item Product description: Pipe clamp Export - Customs tariff no.: 76169910 Country of origin: Germany Material Surcharge 11,40 % 28,19 275,48''')
doc174.ents = [
   Span(doc174, 3, 4, label ="NORDER"),
   Span(doc174, 9, 12, label ="CONTRACT"),
   Span(doc174, 12, 13, label ="CONTRACT1"),
   Span(doc174, 13, 14, label ="POS"),
   Span(doc174, 14, 15, label ="AMOUNT"),
   Span(doc174, 16, 17, label ="ARTICLE"),
   Span(doc174, 20, 21, label ="PRICE"),
   Span(doc174, 21, 22, label ="UNIT"),
   Span(doc174, 23, 24, label ="SUMMA"),
   Span(doc174, 45, 46, label ="TARIFF"),
   Span(doc174, 50, 51, label ="COUNTRY"),
   Span(doc174, 53, 54, label ="PR_SURCH"),
   Span(doc174, 55, 56, label ="SURCHARGE"),
   Span(doc174, 56, 57, label ="TOTAL")]
docs.append(doc174)
print("doc175, 56, #NORDER 2407356; CONTRACT SR-1-06; CONTRACT1 113; POS 20000; AMOUNT 200; ARTICLE 1130000263; PRICE 28,30; UNIT 100; SUMMA 56,60; TARIFF 73269098; COUNTRY Germany; PR_SURCH 10,40; SURCHARGE 5,89; TOTAL 62,49; ")
doc175 = nlp('''Order number: 2407356 Purchase order number: N SR-1-06 113 20000 200 PC 1130000263 28,30 100 PC 56,60 DP-2-W4 DP 2 W4 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 10,40 % 5,89 62,49    ''')
doc175.ents = [
   Span(doc175, 3, 4, label ="NORDER"),
   Span(doc175, 9, 12, label ="CONTRACT"),
   Span(doc175, 12, 13, label ="CONTRACT1"),
   Span(doc175, 13, 14, label ="POS"),
   Span(doc175, 14, 15, label ="AMOUNT"),
   Span(doc175, 16, 17, label ="ARTICLE"),
   Span(doc175, 17, 18, label ="PRICE"),
   Span(doc175, 18, 19, label ="UNIT"),
   Span(doc175, 20, 21, label ="SUMMA"),
   Span(doc175, 43, 44, label ="TARIFF"),
   Span(doc175, 48, 49, label ="COUNTRY"),
   Span(doc175, 51, 52, label ="PR_SURCH"),
   Span(doc175, 53, 54, label ="SURCHARGE"),
   Span(doc175, 54, 55, label ="TOTAL")]
docs.append(doc175)
print("doc176, 55, #NORDER 2407356; CONTRACT SR-1-06; CONTRACT1 113; POS 20100; AMOUNT 50; ARTICLE 1130000266; PRICE 33,23; UNIT 100; SUMMA 16,62; TARIFF 73269098; COUNTRY Germany; PR_SURCH 10,40; SURCHARGE 1,73; TOTAL 18,35; ")
doc176 = nlp('''Order number: 2407356 Purchase order number: N SR-1-06 113 20100 50 PC 1130000266 33,23 100 PC 16,62 DP-3-W4 DP 3 W4 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 10,40 % 1,73 18,35''')
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
   Span(doc176, 43, 44, label ="TARIFF"),
   Span(doc176, 48, 49, label ="COUNTRY"),
   Span(doc176, 51, 52, label ="PR_SURCH"),
   Span(doc176, 53, 54, label ="SURCHARGE"),
   Span(doc176, 54, 55, label ="TOTAL")]
docs.append(doc176)
print("doc177, 55, #NORDER 2407356; CONTRACT SR-1-06; CONTRACT1 113; POS 20200; AMOUNT 200; ARTICLE 1130000270; PRICE 39,05; UNIT 100; SUMMA 78,10; TARIFF 73269098; COUNTRY Germany; PR_SURCH 10,40; SURCHARGE 8,12; TOTAL 86,22; ")
doc177 = nlp('''Order number: 2407356 Purchase order number: N SR-1-06 113 20200 200 PC 1130000270 39,05 100 PC 78,10 DP-4-W4 DP 4 W4 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 10,40 % 8,12 86,22''')
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
   Span(doc177, 43, 44, label ="TARIFF"),
   Span(doc177, 48, 49, label ="COUNTRY"),
   Span(doc177, 51, 52, label ="PR_SURCH"),
   Span(doc177, 53, 54, label ="SURCHARGE"),
   Span(doc177, 54, 55, label ="TOTAL")]
docs.append(doc177)
print("doc178, 59, #NORDER 2407356; CONTRACT SR-1-06; CONTRACT1 113; POS 20300; AMOUNT 200; ARTICLE 1120001200; PRICE 165,06; UNIT 100; SUMMA 330,12; TARIFF 73269098; COUNTRY Germany; PR_SURCH 10,40; SURCHARGE 34,33; TOTAL 364,45; ")
doc178 = nlp('''Order number: 2407356 Purchase order number: N SR-1-06 113 20300 200 PC 1120001200 165,06 100 PC 330,12 SP-2-M-W4 SP 2M W4 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 10,40 % 34,33 364,45   ''')
doc178.ents = [
   Span(doc178, 3, 4, label ="NORDER"),
   Span(doc178, 9, 12, label ="CONTRACT"),
   Span(doc178, 12, 13, label ="CONTRACT1"),
   Span(doc178, 13, 14, label ="POS"),
   Span(doc178, 14, 15, label ="AMOUNT"),
   Span(doc178, 16, 17, label ="ARTICLE"),
   Span(doc178, 17, 18, label ="PRICE"),
   Span(doc178, 18, 19, label ="UNIT"),
   Span(doc178, 20, 21, label ="SUMMA"),
   Span(doc178, 46, 47, label ="TARIFF"),
   Span(doc178, 51, 52, label ="COUNTRY"),
   Span(doc178, 54, 55, label ="PR_SURCH"),
   Span(doc178, 56, 57, label ="SURCHARGE"),
   Span(doc178, 57, 58, label ="TOTAL")]
docs.append(doc178)
print("doc179, 58, #NORDER 2407356; CONTRACT SR-1-06; CONTRACT1 113; POS 20400; AMOUNT 50; ARTICLE 1120000301; PRICE 168,97; UNIT 100; SUMMA 84,49; TARIFF 73269098; COUNTRY Germany; PR_SURCH 10,40; SURCHARGE 8,79; TOTAL 93,28; ")
doc179 = nlp('''Order number: 2407356 Purchase order number: N SR-1-06 113 20400 50 PC 1120000301 168,97 100 PC 84,49 SP-3-M-W4 SP 3 M W4 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 10,40 % 8,79 93,28''')
doc179.ents = [
   Span(doc179, 3, 4, label ="NORDER"),
   Span(doc179, 9, 12, label ="CONTRACT"),
   Span(doc179, 12, 13, label ="CONTRACT1"),
   Span(doc179, 13, 14, label ="POS"),
   Span(doc179, 14, 15, label ="AMOUNT"),
   Span(doc179, 16, 17, label ="ARTICLE"),
   Span(doc179, 17, 18, label ="PRICE"),
   Span(doc179, 18, 19, label ="UNIT"),
   Span(doc179, 20, 21, label ="SUMMA"),
   Span(doc179, 46, 47, label ="TARIFF"),
   Span(doc179, 51, 52, label ="COUNTRY"),
   Span(doc179, 54, 55, label ="PR_SURCH"),
   Span(doc179, 56, 57, label ="SURCHARGE"),
   Span(doc179, 57, 58, label ="TOTAL")]
docs.append(doc179)
print("doc180, 58, #NORDER 2407356; CONTRACT SR-1-06; CONTRACT1 113; POS 20500; AMOUNT 100; ARTICLE 1120001202; PRICE 183,60; UNIT 100; SUMMA 183,60; TARIFF 73269098; COUNTRY Germany; PR_SURCH 10,40; SURCHARGE 19,09; TOTAL 202,69; ")
doc180 = nlp('''Order number: 2407356 Purchase order number: N SR-1-06 113 20500 100 PC 1120001202 183,60 100 PC 183,60 SP-4-M-W4 SP 4M W4 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 10,40 % 19,09 202,69''')
doc180.ents = [
   Span(doc180, 3, 4, label ="NORDER"),
   Span(doc180, 9, 12, label ="CONTRACT"),
   Span(doc180, 12, 13, label ="CONTRACT1"),
   Span(doc180, 13, 14, label ="POS"),
   Span(doc180, 14, 15, label ="AMOUNT"),
   Span(doc180, 16, 17, label ="ARTICLE"),
   Span(doc180, 17, 18, label ="PRICE"),
   Span(doc180, 18, 19, label ="UNIT"),
   Span(doc180, 20, 21, label ="SUMMA"),
   Span(doc180, 46, 47, label ="TARIFF"),
   Span(doc180, 51, 52, label ="COUNTRY"),
   Span(doc180, 54, 55, label ="PR_SURCH"),
   Span(doc180, 56, 57, label ="SURCHARGE"),
   Span(doc180, 57, 58, label ="TOTAL")]
docs.append(doc180)
print("doc181, 62, #NORDER 2407359; CONTRACT SR-1-06; CONTRACT1 115; POS 20600; AMOUNT 10; ARTICLE 1130000597; PRICE 85,35; UNIT 100; SUMMA 8,54; TARIFF 40169997; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,97; TOTAL 9,51; ")
doc181 = nlp('''Order number: 2407359 Purchase order number: N SR-1-06 115 20600 10 PC 1130000597 85,35 100 PC 8,54 RI-32-6/5S RI-EINSATZ 32 (6+ 5 S) packed per each item Product description: insert Export - Customs tariff no.: 40169997 Country of origin: Germany Material Surcharge 11,40 % 0,97 9,51   ''')
doc181.ents = [
   Span(doc181, 3, 4, label ="NORDER"),
   Span(doc181, 9, 12, label ="CONTRACT"),
   Span(doc181, 12, 13, label ="CONTRACT1"),
   Span(doc181, 13, 14, label ="POS"),
   Span(doc181, 14, 15, label ="AMOUNT"),
   Span(doc181, 16, 17, label ="ARTICLE"),
   Span(doc181, 17, 18, label ="PRICE"),
   Span(doc181, 18, 19, label ="UNIT"),
   Span(doc181, 20, 21, label ="SUMMA"),
   Span(doc181, 49, 50, label ="TARIFF"),
   Span(doc181, 54, 55, label ="COUNTRY"),
   Span(doc181, 57, 58, label ="PR_SURCH"),
   Span(doc181, 59, 60, label ="SURCHARGE"),
   Span(doc181, 60, 61, label ="TOTAL")]
docs.append(doc181)
print("doc182, 56, #NORDER 2407359; CONTRACT SR-1-06; CONTRACT1 115; POS 20700; AMOUNT 160; ARTICLE 1130004576; PRICE 26,57; UNIT 100; SUMMA 42,51; TARIFF 73181639; COUNTRY Origin unknown; PR_SURCH 10,40; SURCHARGE 4,42; TOTAL 46,93; ")
doc182 = nlp('''Order number: 2407359 Purchase order number: N SR-1-06 115 20700 160 PC 1130004576 26,57 100 PC 42,51 MUS-M12-DINENISO4032-W5 packed per each item Product description: nuts Export - Customs tariff no.: 73181639 Country of origin: Origin unknown Material Surcharge 10,40 % 4,42 46,93''')
doc182.ents = [
   Span(doc182, 3, 4, label ="NORDER"),
   Span(doc182, 9, 12, label ="CONTRACT"),
   Span(doc182, 12, 13, label ="CONTRACT1"),
   Span(doc182, 13, 14, label ="POS"),
   Span(doc182, 14, 15, label ="AMOUNT"),
   Span(doc182, 16, 17, label ="ARTICLE"),
   Span(doc182, 17, 18, label ="PRICE"),
   Span(doc182, 18, 19, label ="UNIT"),
   Span(doc182, 20, 21, label ="SUMMA"),
   Span(doc182, 43, 44, label ="TARIFF"),
   Span(doc182, 48, 50, label ="COUNTRY"),
   Span(doc182, 52, 53, label ="PR_SURCH"),
   Span(doc182, 54, 55, label ="SURCHARGE"),
   Span(doc182, 55, 56, label ="TOTAL")]
docs.append(doc182)
print("doc183, 54, #NORDER 2407359; CONTRACT SR-1-06; CONTRACT1 115; POS 20800; AMOUNT 75; ARTICLE 1130003001; PRICE 26,38; UNIT 100; SUMMA 19,79; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 2,26; TOTAL 22,05; ")
doc183 = nlp('''Order number: 2407359 Purchase order number: N SR-1-06 115 20800 75 PC 1130003001 26,38 100 PC 19,79 112-PA 112 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 2,26 22,05''')
doc183.ents = [
   Span(doc183, 3, 4, label ="NORDER"),
   Span(doc183, 9, 12, label ="CONTRACT"),
   Span(doc183, 12, 13, label ="CONTRACT1"),
   Span(doc183, 13, 14, label ="POS"),
   Span(doc183, 14, 15, label ="AMOUNT"),
   Span(doc183, 16, 17, label ="ARTICLE"),
   Span(doc183, 17, 18, label ="PRICE"),
   Span(doc183, 18, 19, label ="UNIT"),
   Span(doc183, 20, 21, label ="SUMMA"),
   Span(doc183, 42, 43, label ="TARIFF"),
   Span(doc183, 47, 48, label ="COUNTRY"),
   Span(doc183, 50, 51, label ="PR_SURCH"),
   Span(doc183, 52, 53, label ="SURCHARGE"),
   Span(doc183, 53, 54, label ="TOTAL")]
docs.append(doc183)
print("doc184, 54, #NORDER 2407359; CONTRACT SR-1-06; CONTRACT1 115; POS 20900; AMOUNT 50; ARTICLE 1130005170; PRICE 44,15; UNIT 100; SUMMA 22,08; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 2,52; TOTAL 24,60; ")
doc184 = nlp('''Order number: 2407359 Purchase order number: N SR-1-06 115 20900 50 PC 1130005170 44,15 100 PC 22,08 112/12-PA 112/12 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 2,52 24,60''')
doc184.ents = [
   Span(doc184, 3, 4, label ="NORDER"),
   Span(doc184, 9, 12, label ="CONTRACT"),
   Span(doc184, 12, 13, label ="CONTRACT1"),
   Span(doc184, 13, 14, label ="POS"),
   Span(doc184, 14, 15, label ="AMOUNT"),
   Span(doc184, 16, 17, label ="ARTICLE"),
   Span(doc184, 17, 18, label ="PRICE"),
   Span(doc184, 18, 19, label ="UNIT"),
   Span(doc184, 20, 21, label ="SUMMA"),
   Span(doc184, 42, 43, label ="TARIFF"),
   Span(doc184, 47, 48, label ="COUNTRY"),
   Span(doc184, 50, 51, label ="PR_SURCH"),
   Span(doc184, 52, 53, label ="SURCHARGE"),
   Span(doc184, 53, 54, label ="TOTAL")]
docs.append(doc184)
print("doc185, 55, #NORDER 2407359; CONTRACT SR-1-06; CONTRACT1 115; POS 21000; AMOUNT 50; ARTICLE 1130005577; PRICE 41,59; UNIT 100; SUMMA 20,80; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 2,37; TOTAL 23,17; ")
doc185 = nlp('''Order number: 2407359   Purchase order number: N SR-1-06 115 21000 50 PC 1130005577 41,59 100 PC 20,80 322-PA 322 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 2,37 23,17''')
doc185.ents = [
   Span(doc185, 3, 4, label ="NORDER"),
   Span(doc185, 10, 13, label ="CONTRACT"),
   Span(doc185, 13, 14, label ="CONTRACT1"),
   Span(doc185, 14, 15, label ="POS"),
   Span(doc185, 15, 16, label ="AMOUNT"),
   Span(doc185, 17, 18, label ="ARTICLE"),
   Span(doc185, 18, 19, label ="PRICE"),
   Span(doc185, 19, 20, label ="UNIT"),
   Span(doc185, 21, 22, label ="SUMMA"),
   Span(doc185, 43, 44, label ="TARIFF"),
   Span(doc185, 48, 49, label ="COUNTRY"),
   Span(doc185, 51, 52, label ="PR_SURCH"),
   Span(doc185, 53, 54, label ="SURCHARGE"),
   Span(doc185, 54, 55, label ="TOTAL")]
docs.append(doc185)
print("doc186, 55, #NORDER 2407359; CONTRACT SR-1-06; CONTRACT1 115; POS 21100; AMOUNT 50; ARTICLE 1130005602; PRICE 61,13; UNIT 100; SUMMA 30,57; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 3,48; TOTAL 34,05; ")
doc186 = nlp('''Order number: 2407359 Purchase order number: N SR-1-06 115 21100 50 PC 1130005602 61,13. 100 PC 30,57 322/22-PA 322/22 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 3,48 34,05''')
doc186.ents = [
   Span(doc186, 3, 4, label ="NORDER"),
   Span(doc186, 9, 12, label ="CONTRACT"),
   Span(doc186, 12, 13, label ="CONTRACT1"),
   Span(doc186, 13, 14, label ="POS"),
   Span(doc186, 14, 15, label ="AMOUNT"),
   Span(doc186, 16, 17, label ="ARTICLE"),
   Span(doc186, 17, 18, label ="PRICE"),
   Span(doc186, 19, 20, label ="UNIT"),
   Span(doc186, 21, 22, label ="SUMMA"),
   Span(doc186, 43, 44, label ="TARIFF"),
   Span(doc186, 48, 49, label ="COUNTRY"),
   Span(doc186, 51, 52, label ="PR_SURCH"),
   Span(doc186, 53, 54, label ="SURCHARGE"),
   Span(doc186, 54, 55, label ="TOTAL")]
docs.append(doc186)
print("doc187, 54, #NORDER 2407359; CONTRACT SR-1-06; CONTRACT1 115; POS 21200; AMOUNT 100; ARTICLE 1130005628; PRICE 41,59; UNIT 100; SUMMA 41,59; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 4,74; TOTAL 46,33; ")
doc187 = nlp('''Order number: 2407359 Purchase order number: N SR-1-06 115 21200 100 PC 1130005628 41,59 100 PC 41,59 325-PA 325 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 4,74 46,33''')
doc187.ents = [
   Span(doc187, 3, 4, label ="NORDER"),
   Span(doc187, 9, 12, label ="CONTRACT"),
   Span(doc187, 12, 13, label ="CONTRACT1"),
   Span(doc187, 13, 14, label ="POS"),
   Span(doc187, 14, 15, label ="AMOUNT"),
   Span(doc187, 16, 17, label ="ARTICLE"),
   Span(doc187, 17, 18, label ="PRICE"),
   Span(doc187, 18, 19, label ="UNIT"),
   Span(doc187, 20, 21, label ="SUMMA"),
   Span(doc187, 42, 43, label ="TARIFF"),
   Span(doc187, 47, 48, label ="COUNTRY"),
   Span(doc187, 50, 51, label ="PR_SURCH"),
   Span(doc187, 52, 53, label ="SURCHARGE"),
   Span(doc187, 53, 54, label ="TOTAL")]
docs.append(doc187)
print("doc188, 55, #NORDER 2407359; CONTRACT SR-1-06; CONTRACT1 115; POS 21300; AMOUNT 25; ARTICLE 1130005630; PRICE 26,77; UNIT 100; SUMMA 6,69; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,76; TOTAL 7,45; ")
doc188 = nlp('''Order number: 2407359   Purchase order number: N SR-1-06 115 21300 25 PC 1130005630 26,77 100 PC 6,69 325-PP 325 PP packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 0,76 7,45''')
doc188.ents = [
   Span(doc188, 3, 4, label ="NORDER"),
   Span(doc188, 10, 13, label ="CONTRACT"),
   Span(doc188, 13, 14, label ="CONTRACT1"),
   Span(doc188, 14, 15, label ="POS"),
   Span(doc188, 15, 16, label ="AMOUNT"),
   Span(doc188, 17, 18, label ="ARTICLE"),
   Span(doc188, 18, 19, label ="PRICE"),
   Span(doc188, 19, 20, label ="UNIT"),
   Span(doc188, 21, 22, label ="SUMMA"),
   Span(doc188, 43, 44, label ="TARIFF"),
   Span(doc188, 48, 49, label ="COUNTRY"),
   Span(doc188, 51, 52, label ="PR_SURCH"),
   Span(doc188, 53, 54, label ="SURCHARGE"),
   Span(doc188, 54, 55, label ="TOTAL")]
docs.append(doc188)
print("doc189, 55, #NORDER 2407359; CONTRACT SR-1-06; CONTRACT1 115; POS 21400; AMOUNT 50; ARTICLE 1130005658; PRICE 61,13; UNIT 100; SUMMA 30,57; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 3,48; TOTAL 34,05; ")
doc189 = nlp('''Order number: 2407359 Purchase order number: N SR-1-06 115 21400 50 PC 1130005658 61,13. 100 PC 30,57 325/25-PA 325/25 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 3,48 34,05''')
doc189.ents = [
   Span(doc189, 3, 4, label ="NORDER"),
   Span(doc189, 9, 12, label ="CONTRACT"),
   Span(doc189, 12, 13, label ="CONTRACT1"),
   Span(doc189, 13, 14, label ="POS"),
   Span(doc189, 14, 15, label ="AMOUNT"),
   Span(doc189, 16, 17, label ="ARTICLE"),
   Span(doc189, 17, 18, label ="PRICE"),
   Span(doc189, 19, 20, label ="UNIT"),
   Span(doc189, 21, 22, label ="SUMMA"),
   Span(doc189, 43, 44, label ="TARIFF"),
   Span(doc189, 48, 49, label ="COUNTRY"),
   Span(doc189, 51, 52, label ="PR_SURCH"),
   Span(doc189, 53, 54, label ="SURCHARGE"),
   Span(doc189, 54, 55, label ="TOTAL")]
docs.append(doc189)
print("doc190, 54, #NORDER 2407359; CONTRACT SR-1-06; CONTRACT1 115; POS 21500; AMOUNT 25; ARTICLE 1130003769; PRICE 55,26; UNIT 100; SUMMA 13,82; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 1,58; TOTAL 15,40; ")
doc190 = nlp('''Order number: 2407359 Purchase order number: N SR-1-06 115 21500 25 PC 1130003769 55,26 100 PC 13,82 428-PA 428 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 1,58 15,40''')
doc190.ents = [
   Span(doc190, 3, 4, label ="NORDER"),
   Span(doc190, 9, 12, label ="CONTRACT"),
   Span(doc190, 12, 13, label ="CONTRACT1"),
   Span(doc190, 13, 14, label ="POS"),
   Span(doc190, 14, 15, label ="AMOUNT"),
   Span(doc190, 16, 17, label ="ARTICLE"),
   Span(doc190, 17, 18, label ="PRICE"),
   Span(doc190, 18, 19, label ="UNIT"),
   Span(doc190, 20, 21, label ="SUMMA"),
   Span(doc190, 42, 43, label ="TARIFF"),
   Span(doc190, 47, 48, label ="COUNTRY"),
   Span(doc190, 50, 51, label ="PR_SURCH"),
   Span(doc190, 52, 53, label ="SURCHARGE"),
   Span(doc190, 53, 54, label ="TOTAL")]
docs.append(doc190)
print("doc191, 57, #NORDER 2407359; CONTRACT SR-1-06; CONTRACT1 115; POS 21600; AMOUNT 10; ARTICLE 1130003570; PRICE 153,31; UNIT 100; SUMMA 15,33; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 1,75; TOTAL 17,08; ")
doc191 = nlp('''Order number: 2407359   Purchase order number: N SR-1-06 115 21600 10 PC 1130003570 153,31 100 PC 15,33 6-PA-R 6 PAR packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 1,75 17,08''')
doc191.ents = [
   Span(doc191, 3, 4, label ="NORDER"),
   Span(doc191, 10, 13, label ="CONTRACT"),
   Span(doc191, 13, 14, label ="CONTRACT1"),
   Span(doc191, 14, 15, label ="POS"),
   Span(doc191, 15, 16, label ="AMOUNT"),
   Span(doc191, 17, 18, label ="ARTICLE"),
   Span(doc191, 18, 19, label ="PRICE"),
   Span(doc191, 19, 20, label ="UNIT"),
   Span(doc191, 21, 22, label ="SUMMA"),
   Span(doc191, 45, 46, label ="TARIFF"),
   Span(doc191, 50, 51, label ="COUNTRY"),
   Span(doc191, 53, 54, label ="PR_SURCH"),
   Span(doc191, 55, 56, label ="SURCHARGE"),
   Span(doc191, 56, 57, label ="TOTAL")]
docs.append(doc191)
print("doc192, 54, #NORDER 2407359; CONTRACT SR-1-06; CONTRACT1 115; POS 21700; AMOUNT 40; ARTICLE 1130002245; PRICE 312,80; UNIT 100; SUMMA 125,12; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 14,26; TOTAL 139,38; ")
doc192 = nlp('''Order number: 2407359 Purchase order number: N SR-1-06 115 21700 40 PC 1130002245 312,80 100 PC 125,12 RUL-88.9-PA RUL 88,9 PA packed per each item Product description: Handle Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 14,26 139,38''')
doc192.ents = [
   Span(doc192, 3, 4, label ="NORDER"),
   Span(doc192, 9, 12, label ="CONTRACT"),
   Span(doc192, 12, 13, label ="CONTRACT1"),
   Span(doc192, 13, 14, label ="POS"),
   Span(doc192, 14, 15, label ="AMOUNT"),
   Span(doc192, 16, 17, label ="ARTICLE"),
   Span(doc192, 17, 18, label ="PRICE"),
   Span(doc192, 18, 19, label ="UNIT"),
   Span(doc192, 20, 21, label ="SUMMA"),
   Span(doc192, 42, 43, label ="TARIFF"),
   Span(doc192, 47, 48, label ="COUNTRY"),
   Span(doc192, 50, 51, label ="PR_SURCH"),
   Span(doc192, 52, 53, label ="SURCHARGE"),
   Span(doc192, 53, 54, label ="TOTAL")]
docs.append(doc192)
print("doc193, 60, #NORDER 2407359; CONTRACT SR-1-06; CONTRACT1 115; POS 21800; AMOUNT 40; ARTICLE 1130004368; PRICE 507,85; UNIT 100; SUMMA 203,14; TARIFF 73269098; COUNTRY Europ.; PR_SURCH 10,40; SURCHARGE 21,13; TOTAL 224,27; ")
doc193 = nlp('''Order number: 2407359 Purchase order number: N SR-1-06 115 21800 40 PC 1130004368 507,85 100 PC 203,14 RB-A-94-W5 RB W5 A= 94 packed per each item Product description: Handle Export - Customs tariff no.: 73269098 Country of origin: Europ. Comm. Material Surcharge 10,40 % 21,13 224,27''')
doc193.ents = [
   Span(doc193, 3, 4, label ="NORDER"),
   Span(doc193, 9, 12, label ="CONTRACT"),
   Span(doc193, 12, 13, label ="CONTRACT1"),
   Span(doc193, 13, 14, label ="POS"),
   Span(doc193, 14, 15, label ="AMOUNT"),
   Span(doc193, 16, 17, label ="ARTICLE"),
   Span(doc193, 17, 18, label ="PRICE"),
   Span(doc193, 18, 19, label ="UNIT"),
   Span(doc193, 20, 21, label ="SUMMA"),
   Span(doc193, 45, 46, label ="TARIFF"),
   Span(doc193, 50, 52, label ="COUNTRY"),
   Span(doc193, 56, 57, label ="PR_SURCH"),
   Span(doc193, 58, 59, label ="SURCHARGE"),
   Span(doc193, 59, 60, label ="TOTAL")]
docs.append(doc193)
print("doc194, 55, #NORDER 2407370; CONTRACT SR-1-06; CONTRACT1 117; POS 21900; AMOUNT 300; ARTICLE 1130005100; PRICE 32,99; UNIT 100; SUMMA 98,97; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 11,28; TOTAL 110,25; ")
doc194 = nlp('''Order number: 2407370   Purchase order number: N SR-1-06 117 21900 300 PC 1130005100 32,99 100 PC 98,97 108a-PA 108a PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 11,28 110,25''')
doc194.ents = [
   Span(doc194, 3, 4, label ="NORDER"),
   Span(doc194, 10, 13, label ="CONTRACT"),
   Span(doc194, 13, 14, label ="CONTRACT1"),
   Span(doc194, 14, 15, label ="POS"),
   Span(doc194, 15, 16, label ="AMOUNT"),
   Span(doc194, 17, 18, label ="ARTICLE"),
   Span(doc194, 18, 19, label ="PRICE"),
   Span(doc194, 19, 20, label ="UNIT"),
   Span(doc194, 21, 22, label ="SUMMA"),
   Span(doc194, 43, 44, label ="TARIFF"),
   Span(doc194, 48, 49, label ="COUNTRY"),
   Span(doc194, 51, 52, label ="PR_SURCH"),
   Span(doc194, 53, 54, label ="SURCHARGE"),
   Span(doc194, 54, 55, label ="TOTAL")]
docs.append(doc194)
print("doc195, 54, #NORDER 2407370; CONTRACT SR-1-06; CONTRACT1 117; POS 22000; AMOUNT 300; ARTICLE 1130005754; PRICE 32,99; UNIT 100; SUMMA 98,97; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 11,28; TOTAL 110,25; ")
doc195 = nlp('''Order number: 2407370 Purchase order number: N SR-1-06 117 22000 300 PC 1130005754 32,99 100 PC 98,97 422-PP 422 PP packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 11,28 110,25''')
doc195.ents = [
   Span(doc195, 3, 4, label ="NORDER"),
   Span(doc195, 9, 12, label ="CONTRACT"),
   Span(doc195, 12, 13, label ="CONTRACT1"),
   Span(doc195, 13, 14, label ="POS"),
   Span(doc195, 14, 15, label ="AMOUNT"),
   Span(doc195, 16, 17, label ="ARTICLE"),
   Span(doc195, 17, 18, label ="PRICE"),
   Span(doc195, 18, 19, label ="UNIT"),
   Span(doc195, 20, 21, label ="SUMMA"),
   Span(doc195, 42, 43, label ="TARIFF"),
   Span(doc195, 47, 48, label ="COUNTRY"),
   Span(doc195, 50, 51, label ="PR_SURCH"),
   Span(doc195, 52, 53, label ="SURCHARGE"),
   Span(doc195, 53, 54, label ="TOTAL")]
docs.append(doc195)
print("doc196, 54, #NORDER 2407370; CONTRACT SR-1-06; CONTRACT1 117; POS 22100; AMOUNT 275; ARTICLE 1130006066; PRICE 85,35; UNIT 100; SUMMA 234,71; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 26,76; TOTAL 261,47; ")
doc196 = nlp('''Order number: 2407370 Purchase order number: N SR-1-06 117 22100 275 PC 1130006066 85,35 100 PC 234,71 542-PA 542 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 26,76 261,47''')
doc196.ents = [
   Span(doc196, 3, 4, label ="NORDER"),
   Span(doc196, 9, 12, label ="CONTRACT"),
   Span(doc196, 12, 13, label ="CONTRACT1"),
   Span(doc196, 13, 14, label ="POS"),
   Span(doc196, 14, 15, label ="AMOUNT"),
   Span(doc196, 16, 17, label ="ARTICLE"),
   Span(doc196, 17, 18, label ="PRICE"),
   Span(doc196, 18, 19, label ="UNIT"),
   Span(doc196, 20, 21, label ="SUMMA"),
   Span(doc196, 42, 43, label ="TARIFF"),
   Span(doc196, 47, 48, label ="COUNTRY"),
   Span(doc196, 50, 51, label ="PR_SURCH"),
   Span(doc196, 52, 53, label ="SURCHARGE"),
   Span(doc196, 53, 54, label ="TOTAL")]
docs.append(doc196)
print("doc197, 55, #NORDER 2407370; CONTRACT SR-1-06; CONTRACT1 117; POS 22200; AMOUNT 200; ARTICLE 1130006216; PRICE 110,54; UNIT 100; SUMMA 221,08; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 25,20; TOTAL 246,28; ")
doc197 = nlp('''Order number: 2407370   Purchase order number: N SR-1-06 117 22200 200 PC 1130006216 110,54 100 PC 221,08 757.2-PP 757,2 PP packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 25,20 246,28''')
doc197.ents = [
   Span(doc197, 3, 4, label ="NORDER"),
   Span(doc197, 10, 13, label ="CONTRACT"),
   Span(doc197, 13, 14, label ="CONTRACT1"),
   Span(doc197, 14, 15, label ="POS"),
   Span(doc197, 15, 16, label ="AMOUNT"),
   Span(doc197, 17, 18, label ="ARTICLE"),
   Span(doc197, 18, 19, label ="PRICE"),
   Span(doc197, 19, 20, label ="UNIT"),
   Span(doc197, 21, 22, label ="SUMMA"),
   Span(doc197, 43, 44, label ="TARIFF"),
   Span(doc197, 48, 49, label ="COUNTRY"),
   Span(doc197, 51, 52, label ="PR_SURCH"),
   Span(doc197, 53, 54, label ="SURCHARGE"),
   Span(doc197, 54, 55, label ="TOTAL")]
docs.append(doc197)
print("doc198, 67, #NORDER 2407372; CONTRACT SR-1-06; CONTRACT1 118; POS 22300; AMOUNT 2; ARTICLE 1130004286; PRICE 15,43; UNIT 100; SUMMA 0,31; TARIFF 73181575; COUNTRY India; PR_SURCH 10,40; SURCHARGE 0,03; TOTAL 0,34; ")
doc198 = nlp('''Order number: 2407372 Purchase order number: N SR-1-06 118 22300 2 PC 1130004286 15,43. 100 PC 0,31 AS-M8x45-DIN931/933-70-W4 AS-M8X45-DIN931/933-70-W4 packed per each item Product description: screw Export - Customs tariff no.: 73181575 Country of origin: India Material Surcharge 10,40 % 0,03 0,34''')
doc198.ents = [
   Span(doc198, 3, 4, label ="NORDER"),
   Span(doc198, 9, 12, label ="CONTRACT"),
   Span(doc198, 12, 13, label ="CONTRACT1"),
   Span(doc198, 13, 14, label ="POS"),
   Span(doc198, 14, 15, label ="AMOUNT"),
   Span(doc198, 16, 17, label ="ARTICLE"),
   Span(doc198, 17, 18, label ="PRICE"),
   Span(doc198, 19, 20, label ="UNIT"),
   Span(doc198, 21, 22, label ="SUMMA"),
   Span(doc198, 55, 56, label ="TARIFF"),
   Span(doc198, 60, 61, label ="COUNTRY"),
   Span(doc198, 63, 64, label ="PR_SURCH"),
   Span(doc198, 65, 66, label ="SURCHARGE"),
   Span(doc198, 66, 67, label ="TOTAL")]
docs.append(doc198)
print("doc199, 54, #NORDER 2407372; CONTRACT SR-1-06; CONTRACT1 118; POS 22400; AMOUNT 25; ARTICLE 1130005518; PRICE 26,77; UNIT 100; SUMMA 6,69; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,76; TOTAL 7,45; ")
doc199 = nlp('''Order number: 2407372 Purchase order number: N SR-1-06 118 22400 25 PC 1130005518 26,77 100 PC 6,69 319-PP 319 PP packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 0,76 7,45''')
doc199.ents = [
   Span(doc199, 3, 4, label ="NORDER"),
   Span(doc199, 9, 12, label ="CONTRACT"),
   Span(doc199, 12, 13, label ="CONTRACT1"),
   Span(doc199, 13, 14, label ="POS"),
   Span(doc199, 14, 15, label ="AMOUNT"),
   Span(doc199, 16, 17, label ="ARTICLE"),
   Span(doc199, 17, 18, label ="PRICE"),
   Span(doc199, 18, 19, label ="UNIT"),
   Span(doc199, 20, 21, label ="SUMMA"),
   Span(doc199, 42, 43, label ="TARIFF"),
   Span(doc199, 47, 48, label ="COUNTRY"),
   Span(doc199, 50, 51, label ="PR_SURCH"),
   Span(doc199, 52, 53, label ="SURCHARGE"),
   Span(doc199, 53, 54, label ="TOTAL")]
docs.append(doc199)
print("doc200, 57, #NORDER 2407372; CONTRACT SR-1-06; CONTRACT1 118; POS 22500; AMOUNT 2; ARTICLE 1130000156; PRICE 50,20; UNIT 100; SUMMA 1,00; TARIFF 73269098; COUNTRY Germany; PR_SURCH 10,40; SURCHARGE 0,10; TOTAL 1,10; ")
doc200 = nlp('''Order number: 2407372   Purchase order number: N SR-1-06 118 22500 2 PC 1130000156 50,20 100 PC 1,00 GD-3D-W4 GD 3 D W4 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 10,40 % 0,10 1,10''')
doc200.ents = [
   Span(doc200, 3, 4, label ="NORDER"),
   Span(doc200, 10, 13, label ="CONTRACT"),
   Span(doc200, 13, 14, label ="CONTRACT1"),
   Span(doc200, 14, 15, label ="POS"),
   Span(doc200, 15, 16, label ="AMOUNT"),
   Span(doc200, 17, 18, label ="ARTICLE"),
   Span(doc200, 18, 19, label ="PRICE"),
   Span(doc200, 19, 20, label ="UNIT"),
   Span(doc200, 21, 22, label ="SUMMA"),
   Span(doc200, 45, 46, label ="TARIFF"),
   Span(doc200, 50, 51, label ="COUNTRY"),
   Span(doc200, 53, 54, label ="PR_SURCH"),
   Span(doc200, 55, 56, label ="SURCHARGE"),
   Span(doc200, 56, 57, label ="TOTAL")]
docs.append(doc200)
print("doc201, 58, #NORDER 2407372; CONTRACT SR-1-06; CONTRACT1 118; POS 22600; AMOUNT 2; ARTICLE 1120002555; PRICE 194,34; UNIT 100; SUMMA 3,89; TARIFF 73269098; COUNTRY Germany; PR_SURCH 10,40; SURCHARGE 0,40; TOTAL 4,29; ")
doc201 = nlp('''Order number: 2407372 Purchase order number: N SR-1-06 118 22600 2 PC 1120002555 194,34 100 PC 3,89 SP-3D-M-W4 SP 3 DM W4 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 10,40 % 0,40 4,29''')
doc201.ents = [
   Span(doc201, 3, 4, label ="NORDER"),
   Span(doc201, 9, 12, label ="CONTRACT"),
   Span(doc201, 12, 13, label ="CONTRACT1"),
   Span(doc201, 13, 14, label ="POS"),
   Span(doc201, 14, 15, label ="AMOUNT"),
   Span(doc201, 16, 17, label ="ARTICLE"),
   Span(doc201, 17, 18, label ="PRICE"),
   Span(doc201, 18, 19, label ="UNIT"),
   Span(doc201, 20, 21, label ="SUMMA"),
   Span(doc201, 46, 47, label ="TARIFF"),
   Span(doc201, 51, 52, label ="COUNTRY"),
   Span(doc201, 54, 55, label ="PR_SURCH"),
   Span(doc201, 56, 57, label ="SURCHARGE"),
   Span(doc201, 57, 58, label ="TOTAL")]
docs.append(doc201)
print("doc202, 54, #NORDER 2407378; CONTRACT SR-1-06; CONTRACT1 119; POS 22700; AMOUNT 30; ARTICLE 1130006214; PRICE 231,10; UNIT 100; SUMMA 69,33; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 7,90; TOTAL 77,23; ")
doc202 = nlp('''Order number: 2407378 Purchase order number: N SR-1-06 119 22700 30 PC 1130006214 231,10 100 PC 69,33 757.2-PA 757,2 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 7,90 77,23''')
doc202.ents = [
   Span(doc202, 3, 4, label ="NORDER"),
   Span(doc202, 9, 12, label ="CONTRACT"),
   Span(doc202, 12, 13, label ="CONTRACT1"),
   Span(doc202, 13, 14, label ="POS"),
   Span(doc202, 14, 15, label ="AMOUNT"),
   Span(doc202, 16, 17, label ="ARTICLE"),
   Span(doc202, 17, 18, label ="PRICE"),
   Span(doc202, 18, 19, label ="UNIT"),
   Span(doc202, 20, 21, label ="SUMMA"),
   Span(doc202, 42, 43, label ="TARIFF"),
   Span(doc202, 47, 48, label ="COUNTRY"),
   Span(doc202, 50, 51, label ="PR_SURCH"),
   Span(doc202, 52, 53, label ="SURCHARGE"),
   Span(doc202, 53, 54, label ="TOTAL")]
docs.append(doc202)
print("doc203, 55, #NORDER 2407379; CONTRACT SR-1-06; CONTRACT1 120; POS 22800; AMOUNT 50; ARTICLE 1130006214; PRICE 231,10; UNIT 100; SUMMA 115,55; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 13,17; TOTAL 128,72; ")
doc203 = nlp('''Order number: 2407379   Purchase order number: N SR-1-06 120 22800 50 PC 1130006214 231,10 100 PC 115,55 757.2-PA 757,2 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 13,17 128,72''')
doc203.ents = [
   Span(doc203, 3, 4, label ="NORDER"),
   Span(doc203, 10, 13, label ="CONTRACT"),
   Span(doc203, 13, 14, label ="CONTRACT1"),
   Span(doc203, 14, 15, label ="POS"),
   Span(doc203, 15, 16, label ="AMOUNT"),
   Span(doc203, 17, 18, label ="ARTICLE"),
   Span(doc203, 18, 19, label ="PRICE"),
   Span(doc203, 19, 20, label ="UNIT"),
   Span(doc203, 21, 22, label ="SUMMA"),
   Span(doc203, 43, 44, label ="TARIFF"),
   Span(doc203, 48, 49, label ="COUNTRY"),
   Span(doc203, 51, 52, label ="PR_SURCH"),
   Span(doc203, 53, 54, label ="SURCHARGE"),
   Span(doc203, 54, 55, label ="TOTAL")]
docs.append(doc203)
print("doc204, 59, #NORDER 2407390; CONTRACT SR-1-06; CONTRACT1 122; POS 22900; AMOUNT 5; ARTICLE 1020022306; PRICE 59,96; UNIT 1; SUMMA 299,80; TARIFF 84219990; COUNTRY Germany; PR_SURCH 8,90; SURCHARGE 26,68; TOTAL 326,48; ")
doc204 = nlp('''Order number: 2407390 Purchase order number: N SR-1-06 122 22900 5 PC 1020022306 59,96 1 PC 299,80 NR-250-E-06-B/4 NR-250E06B/4 packed per each item Product description: filter element Export - Customs tariff no.: 84219990 Country of origin: Germany Material Surcharge 8,90 % 26,68 326,48 EAC - Eurasian Conformity''')
doc204.ents = [
   Span(doc204, 3, 4, label ="NORDER"),
   Span(doc204, 9, 12, label ="CONTRACT"),
   Span(doc204, 12, 13, label ="CONTRACT1"),
   Span(doc204, 13, 14, label ="POS"),
   Span(doc204, 14, 15, label ="AMOUNT"),
   Span(doc204, 16, 17, label ="ARTICLE"),
   Span(doc204, 17, 18, label ="PRICE"),
   Span(doc204, 18, 19, label ="UNIT"),
   Span(doc204, 20, 21, label ="SUMMA"),
   Span(doc204, 43, 44, label ="TARIFF"),
   Span(doc204, 48, 49, label ="COUNTRY"),
   Span(doc204, 51, 52, label ="PR_SURCH"),
   Span(doc204, 53, 54, label ="SURCHARGE"),
   Span(doc204, 54, 55, label ="TOTAL")]
docs.append(doc204)
print("doc205, 69, #NORDER 2407397; CONTRACT SR-1-06; CONTRACT1 123; POS 23000; AMOUNT 2.340; ARTICLE 1130004020; PRICE 3,93; UNIT 100; SUMMA 91,96; TARIFF 73181588; COUNTRY Origin unknown; PR_SURCH 11,40; SURCHARGE 10,48; TOTAL 102,44; ")
doc205 = nlp('''Order number: 2407397 Purchase order number: N SR-1-06 123 23000 2.340 PC 1130004020 3,93. 100 PC 91,96 AS-M6x30-DIN931/933-8.8-W3 AS-M6X30-DIN931/933-8.8-W3 packed per each item Product description: screw Export - Customs tariff no.: 73181588 Country of origin: Origin unknown Material Surcharge 11,40 % 10,48 102,44   ''')
doc205.ents = [
   Span(doc205, 3, 4, label ="NORDER"),
   Span(doc205, 9, 12, label ="CONTRACT"),
   Span(doc205, 12, 13, label ="CONTRACT1"),
   Span(doc205, 13, 14, label ="POS"),
   Span(doc205, 14, 15, label ="AMOUNT"),
   Span(doc205, 16, 17, label ="ARTICLE"),
   Span(doc205, 17, 18, label ="PRICE"),
   Span(doc205, 19, 20, label ="UNIT"),
   Span(doc205, 21, 22, label ="SUMMA"),
   Span(doc205, 55, 56, label ="TARIFF"),
   Span(doc205, 60, 62, label ="COUNTRY"),
   Span(doc205, 64, 65, label ="PR_SURCH"),
   Span(doc205, 66, 67, label ="SURCHARGE"),
   Span(doc205, 67, 68, label ="TOTAL")]
docs.append(doc205)
print("doc206, 67, #NORDER 2407397; CONTRACT SR-1-06; CONTRACT1 123; POS 23100; AMOUNT 520; ARTICLE 1130004021; PRICE 4,09; UNIT 100; SUMMA 21,27; TARIFF 73181588; COUNTRY Origin unknown; PR_SURCH 11,40; SURCHARGE 2,42; TOTAL 23,69; ")
doc206 = nlp('''Order number: 2407397 Purchase order number: N SR-1-06 123 23100 520 PC 1130004021 4,09 100 PC 21,27 AS-M6x35-DIN931/933-8.8-W3 AS-M6X35-DIN931/933-8.8-W3 packed per each item Product description: screw Export - Customs tariff no.: 73181588 Country of origin: Origin unknown Material Surcharge 11,40 % 2,42 23,69''')
doc206.ents = [
   Span(doc206, 3, 4, label ="NORDER"),
   Span(doc206, 9, 12, label ="CONTRACT"),
   Span(doc206, 12, 13, label ="CONTRACT1"),
   Span(doc206, 13, 14, label ="POS"),
   Span(doc206, 14, 15, label ="AMOUNT"),
   Span(doc206, 16, 17, label ="ARTICLE"),
   Span(doc206, 17, 18, label ="PRICE"),
   Span(doc206, 18, 19, label ="UNIT"),
   Span(doc206, 20, 21, label ="SUMMA"),
   Span(doc206, 54, 55, label ="TARIFF"),
   Span(doc206, 59, 61, label ="COUNTRY"),
   Span(doc206, 63, 64, label ="PR_SURCH"),
   Span(doc206, 65, 66, label ="SURCHARGE"),
   Span(doc206, 66, 67, label ="TOTAL")]
docs.append(doc206)
print("doc207, 66, #NORDER 2407397; CONTRACT SR-1-06; CONTRACT1 123; POS 23200; AMOUNT 600; ARTICLE 1130004022; PRICE 4,30; UNIT 100; SUMMA 25,80; TARIFF 73181588; COUNTRY Taiwan; PR_SURCH 11,40; SURCHARGE 2,94; TOTAL 28,74; ")
doc207 = nlp('''Order number: 2407397 Purchase order number: N SR-1-06 123 23200 600 PC 1130004022 4,30 100 PC 25,80 AS-M6x40-DIN931/933-8.8-W3 AS-M6X40-DIN931/933-8.8-W3 packed per each item Product description: screw Export - Customs tariff no.: 73181588 Country of origin: Taiwan Material Surcharge 11,40 % 2,94 28,74''')
doc207.ents = [
   Span(doc207, 3, 4, label ="NORDER"),
   Span(doc207, 9, 12, label ="CONTRACT"),
   Span(doc207, 12, 13, label ="CONTRACT1"),
   Span(doc207, 13, 14, label ="POS"),
   Span(doc207, 14, 15, label ="AMOUNT"),
   Span(doc207, 16, 17, label ="ARTICLE"),
   Span(doc207, 17, 18, label ="PRICE"),
   Span(doc207, 18, 19, label ="UNIT"),
   Span(doc207, 20, 21, label ="SUMMA"),
   Span(doc207, 54, 55, label ="TARIFF"),
   Span(doc207, 59, 60, label ="COUNTRY"),
   Span(doc207, 62, 63, label ="PR_SURCH"),
   Span(doc207, 64, 65, label ="SURCHARGE"),
   Span(doc207, 65, 66, label ="TOTAL")]
docs.append(doc207)
print("doc208, 68, #NORDER 2407397; CONTRACT SR-1-06; CONTRACT1 123; POS 23300; AMOUNT 300; ARTICLE 1130004024; PRICE 5,48; UNIT 100; SUMMA 16,44; TARIFF 73181588; COUNTRY Origin unknown; PR_SURCH 11,40; SURCHARGE 1,87; TOTAL 18,31; ")
doc208 = nlp('''Order number: 2407397 Purchase order number: N SR-1-06 123 23300 300 PC 1130004024 5,48 100 PC 16,44 AS-M6x60-DIN931/933-8.8-W3 AS-M6X60-DIN931/933-8.8-W3 packed per each item Product description: screw Export - Customs tariff no.: 73181588 Country of origin: Origin unknown Material Surcharge 11,40 % 1,87 18,31   ''')
doc208.ents = [
   Span(doc208, 3, 4, label ="NORDER"),
   Span(doc208, 9, 12, label ="CONTRACT"),
   Span(doc208, 12, 13, label ="CONTRACT1"),
   Span(doc208, 13, 14, label ="POS"),
   Span(doc208, 14, 15, label ="AMOUNT"),
   Span(doc208, 16, 17, label ="ARTICLE"),
   Span(doc208, 17, 18, label ="PRICE"),
   Span(doc208, 18, 19, label ="UNIT"),
   Span(doc208, 20, 21, label ="SUMMA"),
   Span(doc208, 54, 55, label ="TARIFF"),
   Span(doc208, 59, 61, label ="COUNTRY"),
   Span(doc208, 63, 64, label ="PR_SURCH"),
   Span(doc208, 65, 66, label ="SURCHARGE"),
   Span(doc208, 66, 67, label ="TOTAL")]
docs.append(doc208)
print("doc209, 66, #NORDER 2407397; CONTRACT SR-1-06; CONTRACT1 123; POS 23400; AMOUNT 25; ARTICLE 1130004283; PRICE 9,19; UNIT 100; SUMMA 2,30; TARIFF 73181588; COUNTRY Taiwan; PR_SURCH 11,40; SURCHARGE 0,26; TOTAL 2,56; ")
doc209 = nlp('''Order number: 2407397 Purchase order number: N SR-1-06 123 23400 25 PC 1130004283 9,19 100 PC 2,30 AS-M8x60-DIN931/933-8.8-W3 AS-M8X60-DIN931/933-8.8-W3 packed per each item Product description: screw Export - Customs tariff no.: 73181588 Country of origin: Taiwan Material Surcharge 11,40 % 0,26 2,56''')
doc209.ents = [
   Span(doc209, 3, 4, label ="NORDER"),
   Span(doc209, 9, 12, label ="CONTRACT"),
   Span(doc209, 12, 13, label ="CONTRACT1"),
   Span(doc209, 13, 14, label ="POS"),
   Span(doc209, 14, 15, label ="AMOUNT"),
   Span(doc209, 16, 17, label ="ARTICLE"),
   Span(doc209, 17, 18, label ="PRICE"),
   Span(doc209, 18, 19, label ="UNIT"),
   Span(doc209, 20, 21, label ="SUMMA"),
   Span(doc209, 54, 55, label ="TARIFF"),
   Span(doc209, 59, 60, label ="COUNTRY"),
   Span(doc209, 62, 63, label ="PR_SURCH"),
   Span(doc209, 64, 65, label ="SURCHARGE"),
   Span(doc209, 65, 66, label ="TOTAL")]
docs.append(doc209)
print("doc210, 59, #NORDER 2407397; CONTRACT SR-1-06; CONTRACT1 123; POS 23500; AMOUNT 180; ARTICLE 1130003971; PRICE 4,51; UNIT 100; SUMMA 8,12; TARIFF 73181568; COUNTRY Taiwan; PR_SURCH 11,40; SURCHARGE 0,93; TOTAL 9,05; ")
doc210 = nlp('''Order number: 2407397 Purchase order number: N SR-1-06 123 23500 180 PC 1130003971 4,51 100 PC 8,12 IS-M6X25-ISO4 762-8 .8-W3 packed per each item Product description: screw Export - Customs tariff no.: 73181568 Country of origin: Taiwan Material Surcharge 11,40 % 0,93 9,05''')
doc210.ents = [
   Span(doc210, 3, 4, label ="NORDER"),
   Span(doc210, 9, 12, label ="CONTRACT"),
   Span(doc210, 12, 13, label ="CONTRACT1"),
   Span(doc210, 13, 14, label ="POS"),
   Span(doc210, 14, 15, label ="AMOUNT"),
   Span(doc210, 16, 17, label ="ARTICLE"),
   Span(doc210, 17, 18, label ="PRICE"),
   Span(doc210, 18, 19, label ="UNIT"),
   Span(doc210, 20, 21, label ="SUMMA"),
   Span(doc210, 47, 48, label ="TARIFF"),
   Span(doc210, 52, 53, label ="COUNTRY"),
   Span(doc210, 55, 56, label ="PR_SURCH"),
   Span(doc210, 57, 58, label ="SURCHARGE"),
   Span(doc210, 58, 59, label ="TOTAL")]
docs.append(doc210)
print("doc211, 65, #NORDER 2407397; CONTRACT SR-1-06; CONTRACT1 123; POS 23600; AMOUNT 4.900; ARTICLE 6100152347; PRICE 12,73; UNIT 100; SUMMA 623,77; TARIFF 73181692; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 71,11; TOTAL 694,88; ")
doc211 = nlp('''Order number: 2407397 Purchase order number: N SR-1-06 123 23600 4.900 PC 6100152347 12,73, 100 PC 623,77 SM-1-8/1 D-M-W3/2 packed per each item Customer ID-No.: 000000001 120001932 Product description: nuts Export - Customs tariff no.: 73181692 Country of origin: Germany Material Surcharge 11,40 % 71,11 694,88''')
doc211.ents = [
   Span(doc211, 3, 4, label ="NORDER"),
   Span(doc211, 9, 12, label ="CONTRACT"),
   Span(doc211, 12, 13, label ="CONTRACT1"),
   Span(doc211, 13, 14, label ="POS"),
   Span(doc211, 14, 15, label ="AMOUNT"),
   Span(doc211, 16, 17, label ="ARTICLE"),
   Span(doc211, 17, 18, label ="PRICE"),
   Span(doc211, 19, 20, label ="UNIT"),
   Span(doc211, 21, 22, label ="SUMMA"),
   Span(doc211, 53, 54, label ="TARIFF"),
   Span(doc211, 58, 59, label ="COUNTRY"),
   Span(doc211, 61, 62, label ="PR_SURCH"),
   Span(doc211, 63, 64, label ="SURCHARGE"),
   Span(doc211, 64, 65, label ="TOTAL")]
docs.append(doc211)
print("doc212, 55, #NORDER 2407397; CONTRACT SR-1-06; CONTRACT1 123; POS 23700; AMOUNT 25; ARTICLE 1130005088; PRICE 44,15; UNIT 100; SUMMA 11,04; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 1,26; TOTAL 12,30; ")
doc212 = nlp('''Order number: 2407397   Purchase order number: N SR-1-06 123 23700 25 PC 1130005088 44,15 100 PC 11,04 108/08-PA 108/08 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 1,26 12,30''')
doc212.ents = [
   Span(doc212, 3, 4, label ="NORDER"),
   Span(doc212, 10, 13, label ="CONTRACT"),
   Span(doc212, 13, 14, label ="CONTRACT1"),
   Span(doc212, 14, 15, label ="POS"),
   Span(doc212, 15, 16, label ="AMOUNT"),
   Span(doc212, 17, 18, label ="ARTICLE"),
   Span(doc212, 18, 19, label ="PRICE"),
   Span(doc212, 19, 20, label ="UNIT"),
   Span(doc212, 21, 22, label ="SUMMA"),
   Span(doc212, 43, 44, label ="TARIFF"),
   Span(doc212, 48, 49, label ="COUNTRY"),
   Span(doc212, 51, 52, label ="PR_SURCH"),
   Span(doc212, 53, 54, label ="SURCHARGE"),
   Span(doc212, 54, 55, label ="TOTAL")]
docs.append(doc212)
print("doc213, 54, #NORDER 2407397; CONTRACT SR-1-06; CONTRACT1 123; POS 23800; AMOUNT 125; ARTICLE 1130005100; PRICE 32,99; UNIT 100; SUMMA 41,24; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 4,70; TOTAL 45,94; ")
doc213 = nlp('''Order number: 2407397 Purchase order number: N SR-1-06 123 23800 125 PC 1130005100 32,99 100 PC 41,24 108a-PA 108a PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 4,70 45,94''')
doc213.ents = [
   Span(doc213, 3, 4, label ="NORDER"),
   Span(doc213, 9, 12, label ="CONTRACT"),
   Span(doc213, 12, 13, label ="CONTRACT1"),
   Span(doc213, 13, 14, label ="POS"),
   Span(doc213, 14, 15, label ="AMOUNT"),
   Span(doc213, 16, 17, label ="ARTICLE"),
   Span(doc213, 17, 18, label ="PRICE"),
   Span(doc213, 18, 19, label ="UNIT"),
   Span(doc213, 20, 21, label ="SUMMA"),
   Span(doc213, 42, 43, label ="TARIFF"),
   Span(doc213, 47, 48, label ="COUNTRY"),
   Span(doc213, 50, 51, label ="PR_SURCH"),
   Span(doc213, 52, 53, label ="SURCHARGE"),
   Span(doc213, 53, 54, label ="TOTAL")]
docs.append(doc213)
print("doc214, 54, #NORDER 2407397; CONTRACT SR-1-06; CONTRACT1 123; POS 23900; AMOUNT 50; ARTICLE 1130005170; PRICE 44,15; UNIT 100; SUMMA 22,08; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 2,52; TOTAL 24,60; ")
doc214 = nlp('''Order number: 2407397 Purchase order number: N SR-1-06 123 23900 50 PC 1130005170 44,15 100 PC 22,08 112/12-PA 112/12 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 2,52 24,60''')
doc214.ents = [
   Span(doc214, 3, 4, label ="NORDER"),
   Span(doc214, 9, 12, label ="CONTRACT"),
   Span(doc214, 12, 13, label ="CONTRACT1"),
   Span(doc214, 13, 14, label ="POS"),
   Span(doc214, 14, 15, label ="AMOUNT"),
   Span(doc214, 16, 17, label ="ARTICLE"),
   Span(doc214, 17, 18, label ="PRICE"),
   Span(doc214, 18, 19, label ="UNIT"),
   Span(doc214, 20, 21, label ="SUMMA"),
   Span(doc214, 42, 43, label ="TARIFF"),
   Span(doc214, 47, 48, label ="COUNTRY"),
   Span(doc214, 50, 51, label ="PR_SURCH"),
   Span(doc214, 52, 53, label ="SURCHARGE"),
   Span(doc214, 53, 54, label ="TOTAL")]
docs.append(doc214)
print("doc215, 55, #NORDER 2407397; CONTRACT SR-1-06; CONTRACT1 123; POS 24000; AMOUNT 300; ARTICLE 1130005383; PRICE 36,71; UNIT 100; SUMMA 110,13; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 12,55; TOTAL 122,68; ")
doc215 = nlp('''Order number: 2407397   Purchase order number: N SR-1-06 123 24000 300 PC 1130005383 36,71 100 PC 110,13 218-PA 218 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 12,55 122,68''')
doc215.ents = [
   Span(doc215, 3, 4, label ="NORDER"),
   Span(doc215, 10, 13, label ="CONTRACT"),
   Span(doc215, 13, 14, label ="CONTRACT1"),
   Span(doc215, 14, 15, label ="POS"),
   Span(doc215, 15, 16, label ="AMOUNT"),
   Span(doc215, 17, 18, label ="ARTICLE"),
   Span(doc215, 18, 19, label ="PRICE"),
   Span(doc215, 19, 20, label ="UNIT"),
   Span(doc215, 21, 22, label ="SUMMA"),
   Span(doc215, 43, 44, label ="TARIFF"),
   Span(doc215, 48, 49, label ="COUNTRY"),
   Span(doc215, 51, 52, label ="PR_SURCH"),
   Span(doc215, 53, 54, label ="SURCHARGE"),
   Span(doc215, 54, 55, label ="TOTAL")]
docs.append(doc215)
print("doc216, 54, #NORDER 2407397; CONTRACT SR-1-06; CONTRACT1 123; POS 24100; AMOUNT 400; ARTICLE 1130005577; PRICE 41,59; UNIT 100; SUMMA 166,36; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 18,97; TOTAL 185,33; ")
doc216 = nlp('''Order number: 2407397 Purchase order number: N SR-1-06 123 24100 400 PC 1130005577 41,59 100 PC 166,36 322-PA 322 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 18,97 185,33''')
doc216.ents = [
   Span(doc216, 3, 4, label ="NORDER"),
   Span(doc216, 9, 12, label ="CONTRACT"),
   Span(doc216, 12, 13, label ="CONTRACT1"),
   Span(doc216, 13, 14, label ="POS"),
   Span(doc216, 14, 15, label ="AMOUNT"),
   Span(doc216, 16, 17, label ="ARTICLE"),
   Span(doc216, 17, 18, label ="PRICE"),
   Span(doc216, 18, 19, label ="UNIT"),
   Span(doc216, 20, 21, label ="SUMMA"),
   Span(doc216, 42, 43, label ="TARIFF"),
   Span(doc216, 47, 48, label ="COUNTRY"),
   Span(doc216, 50, 51, label ="PR_SURCH"),
   Span(doc216, 52, 53, label ="SURCHARGE"),
   Span(doc216, 53, 54, label ="TOTAL")]
docs.append(doc216)
print("doc217, 54, #NORDER 2407397; CONTRACT SR-1-06; CONTRACT1 123; POS 24200; AMOUNT 250; ARTICLE 1130006023; PRICE 85,35; UNIT 100; SUMMA 213,38; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 24,33; TOTAL 237,71; ")
doc217 = nlp('''Order number: 2407397 Purchase order number: N SR-1-06 123 24200 250 PC 1130006023 85,35 100 PC 213,38 538-PA 538 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 24,33 237,71''')
doc217.ents = [
   Span(doc217, 3, 4, label ="NORDER"),
   Span(doc217, 9, 12, label ="CONTRACT"),
   Span(doc217, 12, 13, label ="CONTRACT1"),
   Span(doc217, 13, 14, label ="POS"),
   Span(doc217, 14, 15, label ="AMOUNT"),
   Span(doc217, 16, 17, label ="ARTICLE"),
   Span(doc217, 17, 18, label ="PRICE"),
   Span(doc217, 18, 19, label ="UNIT"),
   Span(doc217, 20, 21, label ="SUMMA"),
   Span(doc217, 42, 43, label ="TARIFF"),
   Span(doc217, 47, 48, label ="COUNTRY"),
   Span(doc217, 50, 51, label ="PR_SURCH"),
   Span(doc217, 52, 53, label ="SURCHARGE"),
   Span(doc217, 53, 54, label ="TOTAL")]
docs.append(doc217)
print("doc218, 55, #NORDER 2407397; CONTRACT SR-1-06; CONTRACT1 123; POS 24300; AMOUNT 30; ARTICLE 1130006040; PRICE 131,47; UNIT 100; SUMMA 39,44; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 4,50; TOTAL 43,94; ")
doc218 = nlp('''Order number: 2407397   Purchase order number: N SR-1-06 123 24300 30 PC 1130006040 131,47 100 PC 39,44 538/38-PA 538/38 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 4,50 43,94''')
doc218.ents = [
   Span(doc218, 3, 4, label ="NORDER"),
   Span(doc218, 10, 13, label ="CONTRACT"),
   Span(doc218, 13, 14, label ="CONTRACT1"),
   Span(doc218, 14, 15, label ="POS"),
   Span(doc218, 15, 16, label ="AMOUNT"),
   Span(doc218, 17, 18, label ="ARTICLE"),
   Span(doc218, 18, 19, label ="PRICE"),
   Span(doc218, 19, 20, label ="UNIT"),
   Span(doc218, 21, 22, label ="SUMMA"),
   Span(doc218, 43, 44, label ="TARIFF"),
   Span(doc218, 48, 49, label ="COUNTRY"),
   Span(doc218, 51, 52, label ="PR_SURCH"),
   Span(doc218, 53, 54, label ="SURCHARGE"),
   Span(doc218, 54, 55, label ="TOTAL")]
docs.append(doc218)
print("doc219, 55, #NORDER 2407397; CONTRACT SR-1-06; CONTRACT1 123; POS 24400; AMOUNT 100; ARTICLE 1130017258; PRICE 16,16; UNIT 100; SUMMA 16,16; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 1,84; TOTAL 18,00; ")
doc219 = nlp('''Order number: 2407397 Purchase order number: N SR-1-06 123 24400 100 PC 1130017258 16,16 100 PC 16,16 LNGF-208/08-PA LNGF 208/08 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 1,84 18,00''')
doc219.ents = [
   Span(doc219, 3, 4, label ="NORDER"),
   Span(doc219, 9, 12, label ="CONTRACT"),
   Span(doc219, 12, 13, label ="CONTRACT1"),
   Span(doc219, 13, 14, label ="POS"),
   Span(doc219, 14, 15, label ="AMOUNT"),
   Span(doc219, 16, 17, label ="ARTICLE"),
   Span(doc219, 17, 18, label ="PRICE"),
   Span(doc219, 18, 19, label ="UNIT"),
   Span(doc219, 20, 21, label ="SUMMA"),
   Span(doc219, 43, 44, label ="TARIFF"),
   Span(doc219, 48, 49, label ="COUNTRY"),
   Span(doc219, 51, 52, label ="PR_SURCH"),
   Span(doc219, 53, 54, label ="SURCHARGE"),
   Span(doc219, 54, 55, label ="TOTAL")]
docs.append(doc219)
print("doc220, 55, #NORDER 2407397; CONTRACT SR-1-06; CONTRACT1 123; POS 24500; AMOUNT 100; ARTICLE 1130017261; PRICE 16,16; UNIT 100; SUMMA 16,16; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 1,84; TOTAL 18,00; ")
doc220 = nlp('''Order number: 2407397 Purchase order number: N SR-1-06 123 24500 100 PC 1130017261 16,16 100 PC 16,16 LNGF-210/10-PA LNGF 210/10 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 1,84 18,00''')
doc220.ents = [
   Span(doc220, 3, 4, label ="NORDER"),
   Span(doc220, 9, 12, label ="CONTRACT"),
   Span(doc220, 12, 13, label ="CONTRACT1"),
   Span(doc220, 13, 14, label ="POS"),
   Span(doc220, 14, 15, label ="AMOUNT"),
   Span(doc220, 16, 17, label ="ARTICLE"),
   Span(doc220, 17, 18, label ="PRICE"),
   Span(doc220, 18, 19, label ="UNIT"),
   Span(doc220, 20, 21, label ="SUMMA"),
   Span(doc220, 43, 44, label ="TARIFF"),
   Span(doc220, 48, 49, label ="COUNTRY"),
   Span(doc220, 51, 52, label ="PR_SURCH"),
   Span(doc220, 53, 54, label ="SURCHARGE"),
   Span(doc220, 54, 55, label ="TOTAL")]
docs.append(doc220)
print("doc221, 56, #NORDER 2407397; CONTRACT SR-1-06; CONTRACT1 123; POS 24600; AMOUNT 200; ARTICLE 1130017262; PRICE 16,16; UNIT 100; SUMMA 32,32; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 3,68; TOTAL 36,00; ")
doc221 = nlp('''Order number: 2407397   Purchase order number: N SR-1-06 123 24600 200 PC 1130017262 16,16 100 PC 32,32 LNGF-212/12-PA LNGF 212/12 PA packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 3,68 36,00''')
doc221.ents = [
   Span(doc221, 3, 4, label ="NORDER"),
   Span(doc221, 10, 13, label ="CONTRACT"),
   Span(doc221, 13, 14, label ="CONTRACT1"),
   Span(doc221, 14, 15, label ="POS"),
   Span(doc221, 15, 16, label ="AMOUNT"),
   Span(doc221, 17, 18, label ="ARTICLE"),
   Span(doc221, 18, 19, label ="PRICE"),
   Span(doc221, 19, 20, label ="UNIT"),
   Span(doc221, 21, 22, label ="SUMMA"),
   Span(doc221, 44, 45, label ="TARIFF"),
   Span(doc221, 49, 50, label ="COUNTRY"),
   Span(doc221, 52, 53, label ="PR_SURCH"),
   Span(doc221, 54, 55, label ="SURCHARGE"),
   Span(doc221, 55, 56, label ="TOTAL")]
docs.append(doc221)
print("doc222, 55, #NORDER 2407397; CONTRACT SR-1-06; CONTRACT1 123; POS 24700; AMOUNT 1.175; ARTICLE 1130000258; PRICE 6,83; UNIT 100; SUMMA 80,25; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 9,15; TOTAL 89,40; ")
doc222 = nlp('''Order number: 2407397 Purchase order number: N SR-1-06 123 24700 1.175 PC 1130000258 6,83 100 PC 80,25 DP-1a-W3 DP 1a W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 9,15 89,40''')
doc222.ents = [
   Span(doc222, 3, 4, label ="NORDER"),
   Span(doc222, 9, 12, label ="CONTRACT"),
   Span(doc222, 12, 13, label ="CONTRACT1"),
   Span(doc222, 13, 14, label ="POS"),
   Span(doc222, 14, 15, label ="AMOUNT"),
   Span(doc222, 16, 17, label ="ARTICLE"),
   Span(doc222, 17, 18, label ="PRICE"),
   Span(doc222, 18, 19, label ="UNIT"),
   Span(doc222, 20, 21, label ="SUMMA"),
   Span(doc222, 43, 44, label ="TARIFF"),
   Span(doc222, 48, 49, label ="COUNTRY"),
   Span(doc222, 51, 52, label ="PR_SURCH"),
   Span(doc222, 53, 54, label ="SURCHARGE"),
   Span(doc222, 54, 55, label ="TOTAL")]
docs.append(doc222)
print("doc223, 55, #NORDER 2407397; CONTRACT SR-1-06; CONTRACT1 123; POS 24800; AMOUNT 250; ARTICLE 1130000261; PRICE 7,39; UNIT 100; SUMMA 18,48; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 2,11; TOTAL 20,59; ")
doc223 = nlp('''Order number: 2407397 Purchase order number: N SR-1-06 123 24800 250 PC 1130000261 7,39 100 PC 18,48 DP-2-W3 DP 2 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 2,11 20,59''')
doc223.ents = [
   Span(doc223, 3, 4, label ="NORDER"),
   Span(doc223, 9, 12, label ="CONTRACT"),
   Span(doc223, 12, 13, label ="CONTRACT1"),
   Span(doc223, 13, 14, label ="POS"),
   Span(doc223, 14, 15, label ="AMOUNT"),
   Span(doc223, 16, 17, label ="ARTICLE"),
   Span(doc223, 17, 18, label ="PRICE"),
   Span(doc223, 18, 19, label ="UNIT"),
   Span(doc223, 20, 21, label ="SUMMA"),
   Span(doc223, 43, 44, label ="TARIFF"),
   Span(doc223, 48, 49, label ="COUNTRY"),
   Span(doc223, 51, 52, label ="PR_SURCH"),
   Span(doc223, 53, 54, label ="SURCHARGE"),
   Span(doc223, 54, 55, label ="TOTAL")]
docs.append(doc223)
print("doc224, 56, #NORDER 2407397; CONTRACT SR-1-06; CONTRACT1 123; POS 24900; AMOUNT 300; ARTICLE 1130000264; PRICE 8,38; UNIT 100; SUMMA 25,14; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 2,87; TOTAL 28,01; ")
doc224 = nlp('''Order number: 2407397   Purchase order number: N SR-1-06 123 24900 300 PC 1130000264 8,38 100 PC 25,14 DP-3-W3 DP 3 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 2,87 28,01''')
doc224.ents = [
   Span(doc224, 3, 4, label ="NORDER"),
   Span(doc224, 10, 13, label ="CONTRACT"),
   Span(doc224, 13, 14, label ="CONTRACT1"),
   Span(doc224, 14, 15, label ="POS"),
   Span(doc224, 15, 16, label ="AMOUNT"),
   Span(doc224, 17, 18, label ="ARTICLE"),
   Span(doc224, 18, 19, label ="PRICE"),
   Span(doc224, 19, 20, label ="UNIT"),
   Span(doc224, 21, 22, label ="SUMMA"),
   Span(doc224, 44, 45, label ="TARIFF"),
   Span(doc224, 49, 50, label ="COUNTRY"),
   Span(doc224, 52, 53, label ="PR_SURCH"),
   Span(doc224, 54, 55, label ="SURCHARGE"),
   Span(doc224, 55, 56, label ="TOTAL")]
docs.append(doc224)
print("doc225, 55, #NORDER 2407397; CONTRACT SR-1-06; CONTRACT1 123; POS 25000; AMOUNT 150; ARTICLE 1130000269; PRICE 11,33; UNIT 100; SUMMA 17,00; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 1,94; TOTAL 18,94; ")
doc225 = nlp('''Order number: 2407397 Purchase order number: N SR-1-06 123 25000 150 PC 1130000269 11,33 100 PC 17,00 DP-5-W3 DP 5 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 1,94 18,94''')
doc225.ents = [
   Span(doc225, 3, 4, label ="NORDER"),
   Span(doc225, 9, 12, label ="CONTRACT"),
   Span(doc225, 12, 13, label ="CONTRACT1"),
   Span(doc225, 13, 14, label ="POS"),
   Span(doc225, 14, 15, label ="AMOUNT"),
   Span(doc225, 16, 17, label ="ARTICLE"),
   Span(doc225, 17, 18, label ="PRICE"),
   Span(doc225, 18, 19, label ="UNIT"),
   Span(doc225, 20, 21, label ="SUMMA"),
   Span(doc225, 43, 44, label ="TARIFF"),
   Span(doc225, 48, 49, label ="COUNTRY"),
   Span(doc225, 51, 52, label ="PR_SURCH"),
   Span(doc225, 53, 54, label ="SURCHARGE"),
   Span(doc225, 54, 55, label ="TOTAL")]
docs.append(doc225)
print("doc226, 55, #NORDER 2407397; CONTRACT SR-1-06; CONTRACT1 123; POS 25100; AMOUNT 625; ARTICLE 1130001959; PRICE 6,91; UNIT 100; SUMMA 43,19; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 4,92; TOTAL 48,11; ")
doc226 = nlp('''Order number: 2407397 Purchase order number: N SR-1-06 123 25100 625 PC 1130001959 6,91 100 PC 43,19 DPL-2-W3 DPL 2 W3 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 4,92 48,11''')
doc226.ents = [
   Span(doc226, 3, 4, label ="NORDER"),
   Span(doc226, 9, 12, label ="CONTRACT"),
   Span(doc226, 12, 13, label ="CONTRACT1"),
   Span(doc226, 13, 14, label ="POS"),
   Span(doc226, 14, 15, label ="AMOUNT"),
   Span(doc226, 16, 17, label ="ARTICLE"),
   Span(doc226, 17, 18, label ="PRICE"),
   Span(doc226, 18, 19, label ="UNIT"),
   Span(doc226, 20, 21, label ="SUMMA"),
   Span(doc226, 43, 44, label ="TARIFF"),
   Span(doc226, 48, 49, label ="COUNTRY"),
   Span(doc226, 51, 52, label ="PR_SURCH"),
   Span(doc226, 53, 54, label ="SURCHARGE"),
   Span(doc226, 54, 55, label ="TOTAL")]
docs.append(doc226)
print("doc227, 59, #NORDER 2407397; CONTRACT SR-1-06; CONTRACT1 123; POS 25200; AMOUNT 25; ARTICLE 1120001161; PRICE 27,74; UNIT 100; SUMMA 6,94; TARIFF 73269098; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 0,79; TOTAL 7,73; ")
doc227 = nlp('''Order number: 2407397   Purchase order number: N SR-1-06 123 25200 25 PC 1120001161 27,74 100 PC 6,94 SP-3-M-W2 SP 3 M W2 packed per each item Product description: weld plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 11,40 % 0,79 7,73''')
doc227.ents = [
   Span(doc227, 3, 4, label ="NORDER"),
   Span(doc227, 10, 13, label ="CONTRACT"),
   Span(doc227, 13, 14, label ="CONTRACT1"),
   Span(doc227, 14, 15, label ="POS"),
   Span(doc227, 15, 16, label ="AMOUNT"),
   Span(doc227, 17, 18, label ="ARTICLE"),
   Span(doc227, 18, 19, label ="PRICE"),
   Span(doc227, 19, 20, label ="UNIT"),
   Span(doc227, 21, 22, label ="SUMMA"),
   Span(doc227, 47, 48, label ="TARIFF"),
   Span(doc227, 52, 53, label ="COUNTRY"),
   Span(doc227, 55, 56, label ="PR_SURCH"),
   Span(doc227, 57, 58, label ="SURCHARGE"),
   Span(doc227, 58, 59, label ="TOTAL")]
docs.append(doc227)
print("doc228, 53, #NORDER 2407397; CONTRACT SR-1-06; CONTRACT1 123; POS 25300; AMOUNT 1.400; ARTICLE 1130002821; PRICE 1,56; UNIT 100; SUMMA 21,84; TARIFF 73182200; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 2,49; TOTAL 24,33; ")
doc228 = nlp('''Order number: 2407397 Purchase order number: N SR-1-06 123 25300 1.400 PC 1130002821 1,56 100 PC 21,84 US-W3 US W3 packed per each item Product description: washer Export - Customs tariff no.: 73182200 Country of origin: Germany Material Surcharge 11,40 % 2,49 24,33''')
doc228.ents = [
   Span(doc228, 3, 4, label ="NORDER"),
   Span(doc228, 9, 12, label ="CONTRACT"),
   Span(doc228, 12, 13, label ="CONTRACT1"),
   Span(doc228, 13, 14, label ="POS"),
   Span(doc228, 14, 15, label ="AMOUNT"),
   Span(doc228, 16, 17, label ="ARTICLE"),
   Span(doc228, 17, 18, label ="PRICE"),
   Span(doc228, 18, 19, label ="UNIT"),
   Span(doc228, 20, 21, label ="SUMMA"),
   Span(doc228, 41, 42, label ="TARIFF"),
   Span(doc228, 46, 47, label ="COUNTRY"),
   Span(doc228, 49, 50, label ="PR_SURCH"),
   Span(doc228, 51, 52, label ="SURCHARGE"),
   Span(doc228, 52, 53, label ="TOTAL")]
docs.append(doc228)
print("doc229, 67, #NORDER 2407400; CONTRACT SR-1-06; CONTRACT1 124; POS 25400; AMOUNT 100; ARTICLE 1130004280; PRICE 5,08; UNIT 100; SUMMA 5,08; TARIFF 73181588; COUNTRY Origin unknown; PR_SURCH 11,40; SURCHARGE 0,58; TOTAL 5,66; ")
doc229 = nlp('''Order number: 2407400 Purchase order number: N SR-1-06 124 25400 100 PC 1130004280 5,08 100 PC 5,08 AS-M8x35-DIN931/933-8.8-W3 AS-M8X35-DIN931/933-8.8-W3 packed per each item Product description: screw Export - Customs tariff no.: 73181588 Country of origin: Origin unknown Material Surcharge 11,40 % 0,58 5,66''')
doc229.ents = [
   Span(doc229, 3, 4, label ="NORDER"),
   Span(doc229, 9, 12, label ="CONTRACT"),
   Span(doc229, 12, 13, label ="CONTRACT1"),
   Span(doc229, 13, 14, label ="POS"),
   Span(doc229, 14, 15, label ="AMOUNT"),
   Span(doc229, 16, 17, label ="ARTICLE"),
   Span(doc229, 17, 18, label ="PRICE"),
   Span(doc229, 18, 19, label ="UNIT"),
   Span(doc229, 20, 21, label ="SUMMA"),
   Span(doc229, 54, 55, label ="TARIFF"),
   Span(doc229, 59, 61, label ="COUNTRY"),
   Span(doc229, 63, 64, label ="PR_SURCH"),
   Span(doc229, 65, 66, label ="SURCHARGE"),
   Span(doc229, 66, 67, label ="TOTAL")]
docs.append(doc229)
print("doc230, 55, #NORDER 2407400; CONTRACT SR-1-06; CONTRACT1 124; POS 25500; AMOUNT 100; ARTICLE 1130005243; PRICE 28,91; UNIT 100; SUMMA 28,91; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 3,30; TOTAL 32,21; ")
doc230 = nlp('''Order number: 2407400   Purchase order number: N SR-1-06 124 25500 100 PC 1130005243 28,91 100 PC 28,91 212.7/12.7-PP 212,7/12,7 PP packed per each item Product description: Pipe clamp Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 3,30 32,21''')
doc230.ents = [
   Span(doc230, 3, 4, label ="NORDER"),
   Span(doc230, 10, 13, label ="CONTRACT"),
   Span(doc230, 13, 14, label ="CONTRACT1"),
   Span(doc230, 14, 15, label ="POS"),
   Span(doc230, 15, 16, label ="AMOUNT"),
   Span(doc230, 17, 18, label ="ARTICLE"),
   Span(doc230, 18, 19, label ="PRICE"),
   Span(doc230, 19, 20, label ="UNIT"),
   Span(doc230, 21, 22, label ="SUMMA"),
   Span(doc230, 43, 44, label ="TARIFF"),
   Span(doc230, 48, 49, label ="COUNTRY"),
   Span(doc230, 51, 52, label ="PR_SURCH"),
   Span(doc230, 53, 54, label ="SURCHARGE"),
   Span(doc230, 54, 55, label ="TOTAL")]
docs.append(doc230)
print("doc231, 56, #NORDER 2407408; CONTRACT SR-1-06; CONTRACT1 127; POS 25600; AMOUNT 48; ARTICLE 1130004576; PRICE 26,57; UNIT 100; SUMMA 12,75; TARIFF 73181639; COUNTRY Origin unknown; PR_SURCH 10,40; SURCHARGE 1,33; TOTAL 14,08; ")
doc231 = nlp('''Order number: 2407408 Purchase order number: N SR-1-06 127 25600 48 PC 1130004576 26,57 100 PC 12,75 MUS-M12-DINENISO4032-W5 packed per each item Product description: nuts Export - Customs tariff no.: 73181639 Country of origin: Origin unknown Material Surcharge 10,40 % 1,33 14,08''')
doc231.ents = [
   Span(doc231, 3, 4, label ="NORDER"),
   Span(doc231, 9, 12, label ="CONTRACT"),
   Span(doc231, 12, 13, label ="CONTRACT1"),
   Span(doc231, 13, 14, label ="POS"),
   Span(doc231, 14, 15, label ="AMOUNT"),
   Span(doc231, 16, 17, label ="ARTICLE"),
   Span(doc231, 17, 18, label ="PRICE"),
   Span(doc231, 18, 19, label ="UNIT"),
   Span(doc231, 20, 21, label ="SUMMA"),
   Span(doc231, 43, 44, label ="TARIFF"),
   Span(doc231, 48, 50, label ="COUNTRY"),
   Span(doc231, 52, 53, label ="PR_SURCH"),
   Span(doc231, 54, 55, label ="SURCHARGE"),
   Span(doc231, 55, 56, label ="TOTAL")]
docs.append(doc231)
print("doc232, 54, #NORDER 2407408; CONTRACT SR-1-06; CONTRACT1 127; POS 25700; AMOUNT 12; ARTICLE 1130002244; PRICE 277,00; UNIT 100; SUMMA 33,24; TARIFF 39269097; COUNTRY Germany; PR_SURCH 11,40; SURCHARGE 3,79; TOTAL 37,03; ")
doc232 = nlp('''Order number: 2407408 Purchase order number: N SR-1-06 127 25700 12 PC 1130002244 277,00 100 PC 33,24 RUL-76.1-PA RUL 76,1 PA packed per each item Product description: Handle Export - Customs tariff no.: 39269097 Country of origin: Germany Material Surcharge 11,40 % 3,79 37,03''')
doc232.ents = [
   Span(doc232, 3, 4, label ="NORDER"),
   Span(doc232, 9, 12, label ="CONTRACT"),
   Span(doc232, 12, 13, label ="CONTRACT1"),
   Span(doc232, 13, 14, label ="POS"),
   Span(doc232, 14, 15, label ="AMOUNT"),
   Span(doc232, 16, 17, label ="ARTICLE"),
   Span(doc232, 17, 18, label ="PRICE"),
   Span(doc232, 18, 19, label ="UNIT"),
   Span(doc232, 20, 21, label ="SUMMA"),
   Span(doc232, 42, 43, label ="TARIFF"),
   Span(doc232, 47, 48, label ="COUNTRY"),
   Span(doc232, 50, 51, label ="PR_SURCH"),
   Span(doc232, 52, 53, label ="SURCHARGE"),
   Span(doc232, 53, 54, label ="TOTAL")]
docs.append(doc232)
print("doc233, 58, #NORDER 2407408; CONTRACT SR-1-06; CONTRACT1 127; POS 25800; AMOUNT 12; ARTICLE 1130004367; PRICE 463,97; UNIT 100; SUMMA 55,68; TARIFF 73269098; COUNTRY Germany; PR_SURCH 10,40; SURCHARGE 5,79; TOTAL 61,47; ")
doc233 = nlp('''Order number: 2407408 Purchase order number: N SR-1-06 127    25800 12 PC 1130004367 463,97 100 PC 55,68 RB-A-8 2 -W5 RB W5 A= 82 packed per each item Product description: Handle Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 10,40 % 5,79 61,47''')
doc233.ents = [
   Span(doc233, 3, 4, label ="NORDER"),
   Span(doc233, 9, 12, label ="CONTRACT"),
   Span(doc233, 12, 13, label ="CONTRACT1"),
   Span(doc233, 14, 15, label ="POS"),
   Span(doc233, 15, 16, label ="AMOUNT"),
   Span(doc233, 17, 18, label ="ARTICLE"),
   Span(doc233, 18, 19, label ="PRICE"),
   Span(doc233, 19, 20, label ="UNIT"),
   Span(doc233, 21, 22, label ="SUMMA"),
   Span(doc233, 46, 47, label ="TARIFF"),
   Span(doc233, 51, 52, label ="COUNTRY"),
   Span(doc233, 54, 55, label ="PR_SURCH"),
   Span(doc233, 56, 57, label ="SURCHARGE"),
   Span(doc233, 57, 58, label ="TOTAL")]
docs.append(doc233)
print("doc234, 66, #NORDER 2407411; CONTRACT SR-1-06; CONTRACT1 128; POS 25900; AMOUNT 320; ARTICLE 6100076732; PRICE 1,66; UNIT 1; SUMMA 531,20; TARIFF 84812010; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 36,65; TOTAL 567,85; ")
doc234 = nlp('''Order number: 2407411 Purchase order number: N SR-1-06 128 25900 320 PC 6100076732 (*) 1,66 1 PC 531,20 QRC-HP-1 2 -M-NF08 -B-W3 HP10-2-INFO8N packed per each item Export - Customs tariff no.: 84812010 Country of origin: Germany Material Surcharge 6,90 % 36,65 567,85 EAC - Eurasian Conformity''')
doc234.ents = [
   Span(doc234, 3, 4, label ="NORDER"),
   Span(doc234, 9, 12, label ="CONTRACT"),
   Span(doc234, 12, 13, label ="CONTRACT1"),
   Span(doc234, 13, 14, label ="POS"),
   Span(doc234, 14, 15, label ="AMOUNT"),
   Span(doc234, 16, 17, label ="ARTICLE"),
   Span(doc234, 20, 21, label ="PRICE"),
   Span(doc234, 21, 22, label ="UNIT"),
   Span(doc234, 23, 24, label ="SUMMA"),
   Span(doc234, 50, 51, label ="TARIFF"),
   Span(doc234, 55, 56, label ="COUNTRY"),
   Span(doc234, 58, 59, label ="PR_SURCH"),
   Span(doc234, 60, 61, label ="SURCHARGE"),
   Span(doc234, 61, 62, label ="TOTAL")]
docs.append(doc234)
print("doc235, 53, #NORDER 2407420; CONTRACT SR-1-06; CONTRACT1 130; POS 26000; AMOUNT 250; ARTICLE 6030003815; PRICE 24,92; UNIT 100; SUMMA 62,30; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 4,30; TOTAL 66,60; ")
doc235 = nlp('''Order number: 2407420 Purchase order number: N SR-1-06 130 26000 250 PC 6030003815 24,92 100 PC 62,30 FI-M-15L-W3 packed per each item Product description: nuts Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 4,30 66,60''')
doc235.ents = [
   Span(doc235, 3, 4, label ="NORDER"),
   Span(doc235, 9, 12, label ="CONTRACT"),
   Span(doc235, 12, 13, label ="CONTRACT1"),
   Span(doc235, 13, 14, label ="POS"),
   Span(doc235, 14, 15, label ="AMOUNT"),
   Span(doc235, 16, 17, label ="ARTICLE"),
   Span(doc235, 17, 18, label ="PRICE"),
   Span(doc235, 18, 19, label ="UNIT"),
   Span(doc235, 20, 21, label ="SUMMA"),
   Span(doc235, 41, 42, label ="TARIFF"),
   Span(doc235, 46, 47, label ="COUNTRY"),
   Span(doc235, 49, 50, label ="PR_SURCH"),
   Span(doc235, 51, 52, label ="SURCHARGE"),
   Span(doc235, 52, 53, label ="TOTAL")]
docs.append(doc235)
print("doc236, 54, #NORDER 2407420; CONTRACT SR-1-06; CONTRACT1 130; POS 26100; AMOUNT 120; ARTICLE 6030003817; PRICE 63,90; UNIT 100; SUMMA 76,68; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 5,29; TOTAL 81,97; ")
doc236 = nlp('''Order number: 2407420 Purchase order number: N SR-1-06 130 26100 120 PC 6030003817 63,90 100 PC 76,68    FI-M-22L-W3 packed per each item Product description: nuts Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 5,29 81,97''')
doc236.ents = [
   Span(doc236, 3, 4, label ="NORDER"),
   Span(doc236, 9, 12, label ="CONTRACT"),
   Span(doc236, 12, 13, label ="CONTRACT1"),
   Span(doc236, 13, 14, label ="POS"),
   Span(doc236, 14, 15, label ="AMOUNT"),
   Span(doc236, 16, 17, label ="ARTICLE"),
   Span(doc236, 17, 18, label ="PRICE"),
   Span(doc236, 18, 19, label ="UNIT"),
   Span(doc236, 20, 21, label ="SUMMA"),
   Span(doc236, 42, 43, label ="TARIFF"),
   Span(doc236, 47, 48, label ="COUNTRY"),
   Span(doc236, 50, 51, label ="PR_SURCH"),
   Span(doc236, 52, 53, label ="SURCHARGE"),
   Span(doc236, 53, 54, label ="TOTAL")]
docs.append(doc236)
print("doc237, 53, #NORDER 2407420; CONTRACT SR-1-06; CONTRACT1 130; POS 26200; AMOUNT 50; ARTICLE 6030003819; PRICE 152,44; UNIT 100; SUMMA 76,22; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 5,26; TOTAL 81,48; ")
doc237 = nlp('''Order number: 2407420 Purchase order number: N SR-1-06 130 26200 50 PC 6030003819 152,44 100 PC 76,22 FI-M-35L-W3 packed per each item Product description: nuts Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 5,26 81,48''')
doc237.ents = [
   Span(doc237, 3, 4, label ="NORDER"),
   Span(doc237, 9, 12, label ="CONTRACT"),
   Span(doc237, 12, 13, label ="CONTRACT1"),
   Span(doc237, 13, 14, label ="POS"),
   Span(doc237, 14, 15, label ="AMOUNT"),
   Span(doc237, 16, 17, label ="ARTICLE"),
   Span(doc237, 17, 18, label ="PRICE"),
   Span(doc237, 18, 19, label ="UNIT"),
   Span(doc237, 20, 21, label ="SUMMA"),
   Span(doc237, 41, 42, label ="TARIFF"),
   Span(doc237, 46, 47, label ="COUNTRY"),
   Span(doc237, 49, 50, label ="PR_SURCH"),
   Span(doc237, 51, 52, label ="SURCHARGE"),
   Span(doc237, 52, 53, label ="TOTAL")]
docs.append(doc237)
print("doc238, 60, #NORDER 2407420; CONTRACT SR-1-06; CONTRACT1 130; POS 26300; AMOUNT 16; ARTICLE 1730000052; PRICE 0,23; UNIT 1; SUMMA 3,68; TARIFF 40169300; COUNTRY China; PR_SURCH 15,50; SURCHARGE 0,57; TOTAL 4,25; ")
doc238 = nlp('''Order number: 2407420 Purchase order number: N SR-1-06 130 26300 16 PC 1730000052 0,23 1 PC 3,68 O-Ring-47 .22x3.53-B90 O-Ring NBR-47,22x3,53-SH90 packed per each item Product description: seal Export - Customs tariff no.: 40169300 Country of origin: China Material Surcharge 15,50 % 0,57 4,25''')
doc238.ents = [
   Span(doc238, 3, 4, label ="NORDER"),
   Span(doc238, 9, 12, label ="CONTRACT"),
   Span(doc238, 12, 13, label ="CONTRACT1"),
   Span(doc238, 13, 14, label ="POS"),
   Span(doc238, 14, 15, label ="AMOUNT"),
   Span(doc238, 16, 17, label ="ARTICLE"),
   Span(doc238, 17, 18, label ="PRICE"),
   Span(doc238, 18, 19, label ="UNIT"),
   Span(doc238, 20, 21, label ="SUMMA"),
   Span(doc238, 48, 49, label ="TARIFF"),
   Span(doc238, 53, 54, label ="COUNTRY"),
   Span(doc238, 56, 57, label ="PR_SURCH"),
   Span(doc238, 58, 59, label ="SURCHARGE"),
   Span(doc238, 59, 60, label ="TOTAL")]
docs.append(doc238)
print("doc239, 62, #NORDER 2407420; CONTRACT SR-1-06; CONTRACT1 130; POS 26400; AMOUNT 2; ARTICLE 1730000055; PRICE 0,44; UNIT 1; SUMMA 0,88; TARIFF 40169300; COUNTRY Origin unknown; PR_SURCH 15,50; SURCHARGE 0,14; TOTAL 1,02; ")
doc239 = nlp('''Order number: 2407420 Purchase order number: N SR-1-06 130 26400 2 PC 1730000055 0,44 1 PC 0,88 O-Ring-8 5.32x3.53-B90 O-Ring NBR-85,32x3,53-SH90    packed per each item Product description: seal Export - Customs tariff no.: 40169300 Country of origin: Origin unknown Material Surcharge 15,50 % 0,14 1,02''')
doc239.ents = [
   Span(doc239, 3, 4, label ="NORDER"),
   Span(doc239, 9, 12, label ="CONTRACT"),
   Span(doc239, 12, 13, label ="CONTRACT1"),
   Span(doc239, 13, 14, label ="POS"),
   Span(doc239, 14, 15, label ="AMOUNT"),
   Span(doc239, 16, 17, label ="ARTICLE"),
   Span(doc239, 17, 18, label ="PRICE"),
   Span(doc239, 18, 19, label ="UNIT"),
   Span(doc239, 20, 21, label ="SUMMA"),
   Span(doc239, 49, 50, label ="TARIFF"),
   Span(doc239, 54, 56, label ="COUNTRY"),
   Span(doc239, 58, 59, label ="PR_SURCH"),
   Span(doc239, 60, 61, label ="SURCHARGE"),
   Span(doc239, 61, 62, label ="TOTAL")]
docs.append(doc239)
print("doc240, 75, #NORDER 2407420; CONTRACT SR-1-06; CONTRACT1 130; POS 26500; AMOUNT 16; ARTICLE 1720000008; PRICE 1,53; UNIT 1; SUMMA 24,48; TARIFF 73181568; COUNTRY Origin unknown; PR_SURCH 15,50; SURCHARGE 3,79; TOTAL 28,27; ")
doc240 = nlp('''Order number: 2407420 Purchase order number: N SR-1-06 130 26500 16 PC 1720000008 1,53 1 PC 24,48 Kit-BFX-IS-M12X45-ISO4762-8.8-W66 SET-BFX-IS-M12X45-8.8-ISO4762-W66 packed per each item Product description: screw Export - Customs tariff no.: 73181568 Country of origin: Origin unknown Material Surcharge 15,50 % 3,79 28,27''')
doc240.ents = [
   Span(doc240, 3, 4, label ="NORDER"),
   Span(doc240, 9, 12, label ="CONTRACT"),
   Span(doc240, 12, 13, label ="CONTRACT1"),
   Span(doc240, 13, 14, label ="POS"),
   Span(doc240, 14, 15, label ="AMOUNT"),
   Span(doc240, 16, 17, label ="ARTICLE"),
   Span(doc240, 17, 18, label ="PRICE"),
   Span(doc240, 18, 19, label ="UNIT"),
   Span(doc240, 20, 21, label ="SUMMA"),
   Span(doc240, 62, 63, label ="TARIFF"),
   Span(doc240, 67, 69, label ="COUNTRY"),
   Span(doc240, 71, 72, label ="PR_SURCH"),
   Span(doc240, 73, 74, label ="SURCHARGE"),
   Span(doc240, 74, 75, label ="TOTAL")]
docs.append(doc240)
print("doc241, 73, #NORDER 2407420; CONTRACT SR-1-06; CONTRACT1 130; POS 26600; AMOUNT 4; ARTICLE 6100084956; PRICE 17,07; UNIT 1; SUMMA 68,28; TARIFF 84812010; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 4,71; TOTAL 72,99; ")
doc241 = nlp('''Order number: 2407420 Purchase order number: N SR-1-06 130 26600 4 PC 6100084956 17,07 1 PC 68,28 BBV-2-25S-8001-M 2/2-Way Block Ball Valve DN20 25S-PN420, POM, FPM, ZiNi packed per each item Product description: valve Export - Customs tariff no.: 84812010 Country of origin: Germany Material Surcharge 6,90 % 4,71 72,99 EAC - Eurasian Conformity''')
doc241.ents = [
   Span(doc241, 3, 4, label ="NORDER"),
   Span(doc241, 9, 12, label ="CONTRACT"),
   Span(doc241, 12, 13, label ="CONTRACT1"),
   Span(doc241, 13, 14, label ="POS"),
   Span(doc241, 14, 15, label ="AMOUNT"),
   Span(doc241, 16, 17, label ="ARTICLE"),
   Span(doc241, 17, 18, label ="PRICE"),
   Span(doc241, 18, 19, label ="UNIT"),
   Span(doc241, 20, 21, label ="SUMMA"),
   Span(doc241, 57, 58, label ="TARIFF"),
   Span(doc241, 62, 63, label ="COUNTRY"),
   Span(doc241, 65, 66, label ="PR_SURCH"),
   Span(doc241, 67, 68, label ="SURCHARGE"),
   Span(doc241, 68, 69, label ="TOTAL")]
docs.append(doc241)
print("doc242, 76, #NORDER 2407420; CONTRACT SR-1-06; CONTRACT1 130; POS 26700; AMOUNT 2; ARTICLE 6100084960; PRICE 28,59; UNIT 1; SUMMA 57,18; TARIFF 84812010; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 3,95; TOTAL 61,13; ")
doc242 = nlp('''Order number: 2407420 Purchase order number: N SR-1-06 130 26700 2 PC 6100084960 28,59 1 PC 57,18 BBV-2-38SDN25-8001-M    2/2-Way Block Ball Valve DN25 38S-PN315, POM, FPM, ZiNi packed per each item Product description: valve Export - Customs tariff no.: 84812010 Country of origin: Germany Material Surcharge 6,90 % 3,95 61,13 EAC - Eurasian Conformity''')
doc242.ents = [
   Span(doc242, 3, 4, label ="NORDER"),
   Span(doc242, 9, 12, label ="CONTRACT"),
   Span(doc242, 12, 13, label ="CONTRACT1"),
   Span(doc242, 13, 14, label ="POS"),
   Span(doc242, 14, 15, label ="AMOUNT"),
   Span(doc242, 16, 17, label ="ARTICLE"),
   Span(doc242, 17, 18, label ="PRICE"),
   Span(doc242, 18, 19, label ="UNIT"),
   Span(doc242, 20, 21, label ="SUMMA"),
   Span(doc242, 60, 61, label ="TARIFF"),
   Span(doc242, 65, 66, label ="COUNTRY"),
   Span(doc242, 68, 69, label ="PR_SURCH"),
   Span(doc242, 70, 71, label ="SURCHARGE"),
   Span(doc242, 71, 72, label ="TOTAL")]
docs.append(doc242)
print("doc243, 56, #NORDER 2407420; CONTRACT SR-1-06; CONTRACT1 130; POS 26800; AMOUNT 24; ARTICLE 6030003227; PRICE 84,77; UNIT 100; SUMMA 20,34; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 1,40; TOTAL 21,74; ")
doc243 = nlp('''Order number: 2407420 Purchase order number: N SR-1-06 130 26800 24 PC 6030003227 (*) 84,77 100 PC 20,34 FI-GE-16SR-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 1,40 21,74''')
doc243.ents = [
   Span(doc243, 3, 4, label ="NORDER"),
   Span(doc243, 9, 12, label ="CONTRACT"),
   Span(doc243, 12, 13, label ="CONTRACT1"),
   Span(doc243, 13, 14, label ="POS"),
   Span(doc243, 14, 15, label ="AMOUNT"),
   Span(doc243, 16, 17, label ="ARTICLE"),
   Span(doc243, 20, 21, label ="PRICE"),
   Span(doc243, 21, 22, label ="UNIT"),
   Span(doc243, 23, 24, label ="SUMMA"),
   Span(doc243, 44, 45, label ="TARIFF"),
   Span(doc243, 49, 50, label ="COUNTRY"),
   Span(doc243, 52, 53, label ="PR_SURCH"),
   Span(doc243, 54, 55, label ="SURCHARGE"),
   Span(doc243, 55, 56, label ="TOTAL")]
docs.append(doc243)
print("doc244, 60, #NORDER 2407420; CONTRACT SR-1-06; CONTRACT1 130; POS 26900; AMOUNT 8; ARTICLE 6020000956; PRICE 1.426,24; UNIT 100; SUMMA 114,10; TARIFF 73079910; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 7,87; TOTAL 121,97; ")
doc244 = nlp('''Order number: 2407420 Purchase order number: N SR-1-06 130 26900 8 PC 6020000956 (*) 1.426,24 100 PC 114,10 FI-GE-35LR3/4-WD-B-W3 packed per each item Product description: fitting Export - Customs tariff no.: 73079910 Country of origin: Germany Material Surcharge 6,90 % 7,87 121,97''')
doc244.ents = [
   Span(doc244, 3, 4, label ="NORDER"),
   Span(doc244, 9, 12, label ="CONTRACT"),
   Span(doc244, 12, 13, label ="CONTRACT1"),
   Span(doc244, 13, 14, label ="POS"),
   Span(doc244, 14, 15, label ="AMOUNT"),
   Span(doc244, 16, 17, label ="ARTICLE"),
   Span(doc244, 20, 21, label ="PRICE"),
   Span(doc244, 21, 22, label ="UNIT"),
   Span(doc244, 23, 24, label ="SUMMA"),
   Span(doc244, 48, 49, label ="TARIFF"),
   Span(doc244, 53, 54, label ="COUNTRY"),
   Span(doc244, 56, 57, label ="PR_SURCH"),
   Span(doc244, 58, 59, label ="SURCHARGE"),
   Span(doc244, 59, 60, label ="TOTAL")]
docs.append(doc244)
print("doc245, 58, #NORDER 2407420; CONTRACT SR-1-06; CONTRACT1 130; POS 27000; AMOUNT 48; ARTICLE 6020000165; PRICE 122,01; UNIT 100; SUMMA 58,56; TARIFF 73079319; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 4,04; TOTAL 62,60; ")
doc245 = nlp('''Order number: 2407420 Purchase order number: N SR-1-06 130 27000 48 PC 6020000165 122,01 100 PC 58,56 FI-SN-16x2-B-W2 packed per each item    Product description: welded socket reduction Export - Customs tariff no.: 73079319 Country of origin: Germany Material Surcharge 6,90 % 4,04 62,60''')
doc245.ents = [
   Span(doc245, 3, 4, label ="NORDER"),
   Span(doc245, 9, 12, label ="CONTRACT"),
   Span(doc245, 12, 13, label ="CONTRACT1"),
   Span(doc245, 13, 14, label ="POS"),
   Span(doc245, 14, 15, label ="AMOUNT"),
   Span(doc245, 16, 17, label ="ARTICLE"),
   Span(doc245, 17, 18, label ="PRICE"),
   Span(doc245, 18, 19, label ="UNIT"),
   Span(doc245, 20, 21, label ="SUMMA"),
   Span(doc245, 46, 47, label ="TARIFF"),
   Span(doc245, 51, 52, label ="COUNTRY"),
   Span(doc245, 54, 55, label ="PR_SURCH"),
   Span(doc245, 56, 57, label ="SURCHARGE"),
   Span(doc245, 57, 58, label ="TOTAL")]
docs.append(doc245)
print("doc246, 57, #NORDER 2407420; CONTRACT SR-1-06; CONTRACT1 130; POS 27100; AMOUNT 50; ARTICLE 6020000181; PRICE 196,21; UNIT 100; SUMMA 98,11; TARIFF 73079319; COUNTRY Germany; PR_SURCH 6,90; SURCHARGE 6,77; TOTAL 104,88; ")
doc246 = nlp('''Order number: 2407420 Purchase order number: N SR-1-06 130 27100 50 PC 6020000181 196,21 100 PC 98,11 FI-SN-25x3-B-W2 packed per each item Product description: welded socket reduction Export - Customs tariff no.: 73079319 Country of origin: Germany Material Surcharge 6,90 % 6,77 104,88''')
doc246.ents = [
   Span(doc246, 3, 4, label ="NORDER"),
   Span(doc246, 9, 12, label ="CONTRACT"),
   Span(doc246, 12, 13, label ="CONTRACT1"),
   Span(doc246, 13, 14, label ="POS"),
   Span(doc246, 14, 15, label ="AMOUNT"),
   Span(doc246, 16, 17, label ="ARTICLE"),
   Span(doc246, 17, 18, label ="PRICE"),
   Span(doc246, 18, 19, label ="UNIT"),
   Span(doc246, 20, 21, label ="SUMMA"),
   Span(doc246, 45, 46, label ="TARIFF"),
   Span(doc246, 50, 51, label ="COUNTRY"),
   Span(doc246, 53, 54, label ="PR_SURCH"),
   Span(doc246, 55, 56, label ="SURCHARGE"),
   Span(doc246, 56, 57, label ="TOTAL")]
docs.append(doc246)
print("doc247, 56, #NORDER 2407420; CONTRACT SR-1-06; CONTRACT1 130; POS 27200; AMOUNT 2; ARTICLE 1730001085; PRICE 6,82; UNIT 1; SUMMA 13,64; TARIFF 73079100; COUNTRY Italy; PR_SURCH 15,50; SURCHARGE 2,11; TOTAL 15,75; ")
doc247 = nlp('''Order number: 2407420 Purchase order number: N SR-1-06 130 27200 2 PC 1730001085 6,82 1 PC 13,64 BAS-303-STRE-3 5/27 -W1 BAS-303-STRE-35/27 packed per each item Product description: flange Export - Customs tariff no.: 73079100 Country of origin: Italy Material Surcharge 15,50 % 2,11 15,75''')
doc247.ents = [
   Span(doc247, 3, 4, label ="NORDER"),
   Span(doc247, 9, 12, label ="CONTRACT"),
   Span(doc247, 12, 13, label ="CONTRACT1"),
   Span(doc247, 13, 14, label ="POS"),
   Span(doc247, 14, 15, label ="AMOUNT"),
   Span(doc247, 16, 17, label ="ARTICLE"),
   Span(doc247, 17, 18, label ="PRICE"),
   Span(doc247, 18, 19, label ="UNIT"),
   Span(doc247, 20, 21, label ="SUMMA"),
   Span(doc247, 44, 45, label ="TARIFF"),
   Span(doc247, 49, 50, label ="COUNTRY"),
   Span(doc247, 52, 53, label ="PR_SURCH"),
   Span(doc247, 54, 55, label ="SURCHARGE"),
   Span(doc247, 55, 56, label ="TOTAL")]
docs.append(doc247)
print("doc248, 57, #NORDER 2407420; CONTRACT SR-1-06; CONTRACT1 130; POS 27300; AMOUNT 1; ARTICLE 1730001182; PRICE 9,98; UNIT 1; SUMMA 9,98; TARIFF 73079100; COUNTRY Italy; PR_SURCH 15,50; SURCHARGE 1,55; TOTAL 11,53; ")
doc248 = nlp('''Order number: 2407420 Purchase order number: N SR-1-06 130 27300 1 PC 1730001182 9,98 1 PC 9,98 BAS-305-SRE-49/38-W1 BAS-305-SRE-49/38 packed per each item Product description: flange    Export - Customs tariff no.: 73079100 Country of origin: Italy Material Surcharge 15,50 % 1,55 11,53''')
doc248.ents = [
   Span(doc248, 3, 4, label ="NORDER"),
   Span(doc248, 9, 12, label ="CONTRACT"),
   Span(doc248, 12, 13, label ="CONTRACT1"),
   Span(doc248, 13, 14, label ="POS"),
   Span(doc248, 14, 15, label ="AMOUNT"),
   Span(doc248, 16, 17, label ="ARTICLE"),
   Span(doc248, 17, 18, label ="PRICE"),
   Span(doc248, 18, 19, label ="UNIT"),
   Span(doc248, 20, 21, label ="SUMMA"),
   Span(doc248, 45, 46, label ="TARIFF"),
   Span(doc248, 50, 51, label ="COUNTRY"),
   Span(doc248, 53, 54, label ="PR_SURCH"),
   Span(doc248, 55, 56, label ="SURCHARGE"),
   Span(doc248, 56, 57, label ="TOTAL")]
docs.append(doc248)
print("doc249, 57, #NORDER 2407420; CONTRACT SR-1-06; CONTRACT1 130; POS 27400; AMOUNT 3; ARTICLE 1730000127; PRICE 11,94; UNIT 1; SUMMA 35,82; TARIFF 73079100; COUNTRY Italy; PR_SURCH 15,50; SURCHARGE 5,55; TOTAL 41,37; ")
doc249 = nlp('''Order number: 2407420 Purchase order number: N SR-1-06 130 27400 3 PC 1730000127 11,94 1 PC 35,82 BAS-306-STRE-61/53-W1 BAS-306-STRE-6 1/53 packed per each item Product description: flange Export - Customs tariff no.: 73079100 Country of origin: Italy Material Surcharge 15,50 % 5,55 41,37''')
doc249.ents = [
   Span(doc249, 3, 4, label ="NORDER"),
   Span(doc249, 9, 12, label ="CONTRACT"),
   Span(doc249, 12, 13, label ="CONTRACT1"),
   Span(doc249, 13, 14, label ="POS"),
   Span(doc249, 14, 15, label ="AMOUNT"),
   Span(doc249, 16, 17, label ="ARTICLE"),
   Span(doc249, 17, 18, label ="PRICE"),
   Span(doc249, 18, 19, label ="UNIT"),
   Span(doc249, 20, 21, label ="SUMMA"),
   Span(doc249, 45, 46, label ="TARIFF"),
   Span(doc249, 50, 51, label ="COUNTRY"),
   Span(doc249, 53, 54, label ="PR_SURCH"),
   Span(doc249, 55, 56, label ="SURCHARGE"),
   Span(doc249, 56, 57, label ="TOTAL")]
docs.append(doc249)
print("doc250, 55, #NORDER 2407420; CONTRACT SR-1-06; CONTRACT1 130; POS 27500; AMOUNT 5; ARTICLE 1730000115; PRICE 16,95; UNIT 1; SUMMA 84,75; TARIFF 73079100; COUNTRY Italy; PR_SURCH 15,50; SURCHARGE 13,14; TOTAL 97,89; ")
doc250 = nlp('''Order number: 2407420 Purchase order number: N SR-1-06 130 27500 5 PC 1730000115 16,95 1 PC 84,75 BAS-308 -STRE-90/82-W1 BAS-308-STRE-90/82 packed per each item Product description: flange Export - Customs tariff no.: 73079100 Country of origin: Italy Material Surcharge 15,50 % 13,14 97,89''')
doc250.ents = [
   Span(doc250, 3, 4, label ="NORDER"),
   Span(doc250, 9, 12, label ="CONTRACT"),
   Span(doc250, 12, 13, label ="CONTRACT1"),
   Span(doc250, 13, 14, label ="POS"),
   Span(doc250, 14, 15, label ="AMOUNT"),
   Span(doc250, 16, 17, label ="ARTICLE"),
   Span(doc250, 17, 18, label ="PRICE"),
   Span(doc250, 18, 19, label ="UNIT"),
   Span(doc250, 20, 21, label ="SUMMA"),
   Span(doc250, 43, 44, label ="TARIFF"),
   Span(doc250, 48, 49, label ="COUNTRY"),
   Span(doc250, 51, 52, label ="PR_SURCH"),
   Span(doc250, 53, 54, label ="SURCHARGE"),
   Span(doc250, 54, 55, label ="TOTAL")]
docs.append(doc250)
print("doc251, 59, #NORDER 2407420; CONTRACT SR-1-06; CONTRACT1 130; POS 27600; AMOUNT 2; ARTICLE 1730000277; PRICE 9,98; UNIT 1; SUMMA 19,96; TARIFF 73079100; COUNTRY Italy; PR_SURCH 15,50; SURCHARGE 3,09; TOTAL 23,05; ")
doc251 = nlp('''Order number: 2407420 Purchase order number: N SR-1-06 130 27600 2 PC 1730000277 9,98 1 PC 19,96 BFX-305-ST-48.6/38-W1 BFX-305-ST-48, 6/38 packed per each item Product description: flange    Export - Customs tariff no.: 73079100 Country of origin: Italy Material Surcharge 15,50 % 3,09 23,05''')
doc251.ents = [
   Span(doc251, 3, 4, label ="NORDER"),
   Span(doc251, 9, 12, label ="CONTRACT"),
   Span(doc251, 12, 13, label ="CONTRACT1"),
   Span(doc251, 13, 14, label ="POS"),
   Span(doc251, 14, 15, label ="AMOUNT"),
   Span(doc251, 16, 17, label ="ARTICLE"),
   Span(doc251, 17, 18, label ="PRICE"),
   Span(doc251, 18, 19, label ="UNIT"),
   Span(doc251, 20, 21, label ="SUMMA"),
   Span(doc251, 47, 48, label ="TARIFF"),
   Span(doc251, 52, 53, label ="COUNTRY"),
   Span(doc251, 55, 56, label ="PR_SURCH"),
   Span(doc251, 57, 58, label ="SURCHARGE"),
   Span(doc251, 58, 59, label ="TOTAL")]
docs.append(doc251)
print("doc252, 56, #NORDER 2407420; CONTRACT SR-1-06; CONTRACT1 130; POS 27700; AMOUNT 16; ARTICLE 1730000120; PRICE 9,98; UNIT 1; SUMMA 159,68; TARIFF 73079100; COUNTRY Italy; PR_SURCH 15,50; SURCHARGE 24,75; TOTAL 184,43; ")
doc252 = nlp('''Order number: 2407420 Purchase order number: N SR-1-06 130 27700 16 PC 1730000120 9,98 1 PC 159,68 BFX-305-STRE-49/42-W1 BFX-305-STRE-49/42 packed per each item Product description: flange Export - Customs tariff no.: 73079100 Country of origin: Italy Material Surcharge 15,50 % 24,75 184,43''')
doc252.ents = [
   Span(doc252, 3, 4, label ="NORDER"),
   Span(doc252, 9, 12, label ="CONTRACT"),
   Span(doc252, 12, 13, label ="CONTRACT1"),
   Span(doc252, 13, 14, label ="POS"),
   Span(doc252, 14, 15, label ="AMOUNT"),
   Span(doc252, 16, 17, label ="ARTICLE"),
   Span(doc252, 17, 18, label ="PRICE"),
   Span(doc252, 18, 19, label ="UNIT"),
   Span(doc252, 20, 21, label ="SUMMA"),
   Span(doc252, 44, 45, label ="TARIFF"),
   Span(doc252, 49, 50, label ="COUNTRY"),
   Span(doc252, 52, 53, label ="PR_SURCH"),
   Span(doc252, 54, 55, label ="SURCHARGE"),
   Span(doc252, 55, 56, label ="TOTAL")]
docs.append(doc252)
print("doc253, 61, #NORDER 2407619; CONTRACT SR-1-06; CONTRACT1 132; POS 27800; AMOUNT 2; ARTICLE 1020013419; PRICE 9,12; UNIT 1; SUMMA 18,24; TARIFF 84212980; COUNTRY Italy; PR_SURCH 8,90; SURCHARGE 1,62; TOTAL 19,86; ")
doc253 = nlp('''Order number: 2407619 Purchase order number: N SR-1-06 132 27800 2 PC 1020013419 9,12 1 PC 18,24 RTE-15-D-10-B RTE-25D10B/S1 packed per each item Product description: filter element Export - Customs tariff no.: 84212980 Country of origin: Italy Material Surcharge 8,90 % 1,62 19,86 EAC - Eurasian Conformity''')
doc253.ents = [
   Span(doc253, 3, 4, label ="NORDER"),
   Span(doc253, 9, 12, label ="CONTRACT"),
   Span(doc253, 12, 13, label ="CONTRACT1"),
   Span(doc253, 13, 14, label ="POS"),
   Span(doc253, 14, 15, label ="AMOUNT"),
   Span(doc253, 16, 17, label ="ARTICLE"),
   Span(doc253, 17, 18, label ="PRICE"),
   Span(doc253, 18, 19, label ="UNIT"),
   Span(doc253, 20, 21, label ="SUMMA"),
   Span(doc253, 45, 46, label ="TARIFF"),
   Span(doc253, 50, 51, label ="COUNTRY"),
   Span(doc253, 53, 54, label ="PR_SURCH"),
   Span(doc253, 55, 56, label ="SURCHARGE"),
   Span(doc253, 56, 57, label ="TOTAL")]
docs.append(doc253)
print("doc254, 62, #NORDER 2407619; CONTRACT SR-1-06; CONTRACT1 132; POS 27900; AMOUNT 2; ARTICLE 1020013419; PRICE 9,12; UNIT 1; SUMMA 18,24; TARIFF 84212980; COUNTRY Italy; PR_SURCH 8,90; SURCHARGE 1,62; TOTAL 19,86; ")
doc254 = nlp('''Order number: 2407619 Purchase order number: N SR-1-06 132 27900 2 PC 1020013419 9,12 1 PC 18,24 RTE-15-D-10-B RTE-25D10B/S1 packed per each item    Product description: filter element Export - Customs tariff no.: 84212980 Country of origin: Italy Material Surcharge 8,90 % 1,62 19,86 EAC - Eurasian Conformity''')
doc254.ents = [
   Span(doc254, 3, 4, label ="NORDER"),
   Span(doc254, 9, 12, label ="CONTRACT"),
   Span(doc254, 12, 13, label ="CONTRACT1"),
   Span(doc254, 13, 14, label ="POS"),
   Span(doc254, 14, 15, label ="AMOUNT"),
   Span(doc254, 16, 17, label ="ARTICLE"),
   Span(doc254, 17, 18, label ="PRICE"),
   Span(doc254, 18, 19, label ="UNIT"),
   Span(doc254, 20, 21, label ="SUMMA"),
   Span(doc254, 46, 47, label ="TARIFF"),
   Span(doc254, 51, 52, label ="COUNTRY"),
   Span(doc254, 54, 55, label ="PR_SURCH"),
   Span(doc254, 56, 57, label ="SURCHARGE"),
   Span(doc254, 57, 58, label ="TOTAL")]
docs.append(doc254)
print("doc255, 55, #NORDER 2407621; CONTRACT SR-1-06; CONTRACT1 131; POS 28000; AMOUNT 25; ARTICLE 1130000260; PRICE 23,45; UNIT 100; SUMMA 5,86; TARIFF 73269098; COUNTRY Germany; PR_SURCH 10,40; SURCHARGE 0,61; TOTAL 6,47; ")
doc255 = nlp('''Order number: 2407621 Purchase order number: N SR-1-06 131 28000 25 PC 1130000260 23,45 100 PC 5,86 DP-1a-W4 DP 1a W4 packed per each item Product description: cover plate Export - Customs tariff no.: 73269098 Country of origin: Germany Material Surcharge 10,40 % 0,61 6,47''')
doc255.ents = [
   Span(doc255, 3, 4, label ="NORDER"),
   Span(doc255, 9, 12, label ="CONTRACT"),
   Span(doc255, 12, 13, label ="CONTRACT1"),
   Span(doc255, 13, 14, label ="POS"),
   Span(doc255, 14, 15, label ="AMOUNT"),
   Span(doc255, 16, 17, label ="ARTICLE"),
   Span(doc255, 17, 18, label ="PRICE"),
   Span(doc255, 18, 19, label ="UNIT"),
   Span(doc255, 20, 21, label ="SUMMA"),
   Span(doc255, 43, 44, label ="TARIFF"),
   Span(doc255, 48, 49, label ="COUNTRY"),
   Span(doc255, 51, 52, label ="PR_SURCH"),
   Span(doc255, 53, 54, label ="SURCHARGE"),
   Span(doc255, 54, 55, label ="TOTAL")]
docs.append(doc255)

random.shuffle(docs)
doc_bin = DocBin(docs = docs[:200])
doc_bin.to_disk('./train26.spacy')

doc_bin = DocBin(docs = docs[200:])
doc_bin.to_disk('./dev26.spacy')