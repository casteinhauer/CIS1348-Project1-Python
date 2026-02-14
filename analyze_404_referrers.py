import sys

logPath = sys.argv[1]     
outputPath = sys.argv[2]   

logInfoLst = [[],[]]

logFile = open(logPath,"r")
lines = logFile.readlines()
for line in lines:
    line = line.strip()
    lineParts = line.split(" ")
    
    refer = lineParts[10].replace("\"","")
    
    status = lineParts[8]
    if refer != "-" and status == "404":
        inList = False
        index = -1
        
        for i in range(len(logInfoLst[0])):
            log = logInfoLst[0][i]
            if log == refer:
                inList = True
                index = i
                break
        if inList:
            logInfoLst[1][index] +=1
        else:
            logInfoLst[0].append(refer)
            logInfoLst[1].append(1)
logFile.close()

outFile = open(outputPath,"w")
outFile.write("referrer\tcount\n")

while len(logInfoLst[0]) >0:
    greatestNum = -1
    index = -1
    
    for i in range(len(logInfoLst[0])):
        if logInfoLst[1][i] > greatestNum:
            index = i
            greatestNum = logInfoLst[1][i]
    
    outFile.write(logInfoLst[0][index] + "\t" + str(greatestNum) + "\n")
    logInfoLst[0].pop(index)
    logInfoLst[1].pop(index)