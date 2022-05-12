from datetime import datetime

#logFile = r'C:\Users\alex1c\sources\spacySt\StauffInvoices\log\log.txt'

def appendLogEvent(methName, desc):
    logFile = r'C:\Users\alex1c\sources\spacySt\StauffInvoices\log\log.txt'
    with open(logFile, 'a') as logFile:
        #print(datetime.datetime.now())
        logFile.write(str(datetime.now()) + ' ' + ' method: ' + methName + ', event: ' + desc + '\n')

appendLogEvent('test1', 'test publication ')

print('78/78'.replace('/', '\\'))