outStr = ""
count, i = 0,0

inStr = input("Type string : ")
count = len(inStr)

for i in  range(0, count) : 
    outStr += inStr[count - (i+1)] #마지막 문자부터 추출하여 저장
    print("Reversed string : %s" % outStr)