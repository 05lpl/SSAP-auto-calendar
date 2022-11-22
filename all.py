import pandas as pd
import xlrd 
from datetime import date, datetime, timedelta, timezone



workbook=xlrd.open_workbook("/Users/william/Downloads/SS-Calander-main/WK13.xls")#填入课表 xls文件地址
#获取所有sheet的名字

worksheet=workbook.sheet_by_name("EAP")#填写年级
nrows=worksheet.nrows  #获取该表总行数
print(nrows)  #32

ncols=worksheet.ncols  #获取该表总列数
print(ncols) #13


fyear=2022#输入第一天的年
fmonth=11#输入第一天的月
fday=21#输入第一天的日






day1=[]
days=[2,4,5,6,7]
for k in days:
        
        for i in worksheet.col_values(k):
            if(i=="AP Chemistry-Class 1-Cecelia-S404"or i=="AP Physics C M- Class 1-Roger-S302"or i=="SAT1-SAT Reading-Serena-S402" or i=="SAT1-SAT Grammar-Anita-S402"  or i=="Contemporary English-Class 5-Wayne-S302"  or i=="EAP3-Self Study-班主任管理纪律"  or i=="EAP3-升学指导-S604"  or i=="AP Calculus BC-Class 3-Robi-S106" or i=="SAT1-P.E-Yubin" or i=="World History Honors-Class 3-Jonaivi-S102" or i=="Class Meeting"or i =="Contemporary English-Class 5-Arvin-S302"or i=="SAT1-SAT Math-Elaine-S402" or i=="SAT1-Chinese-Celine-S402"):
                day1.append(i)
            
                
            elif((i.find("自习")==0)):
                
                day1.append(i)
                

ICAL_PATH = 'export.ics'


timestart1=['00:1000','00:5500','01:4000','02:2500','03:1000','06:2000','07:1500','08:0500']
timeend1=['00:5000','01:3500','02:2000','03:0500','03:5000','07:0000','07:5500','08:4500']

timestart2=['00:0000','00:5000','01:3700','02:2500','03:1000','06:2000','07:1500','08:0500']
timeend2=['00:4000','01:3000','02:1700','03:0500','03:5000','07:0000','07:5500','08:4500']

cl=0

ical = open(ICAL_PATH, 'w')
ical.write('BEGIN:VCALENDAR\n')

ical.write('VERSION:2.0\n')
ical.write('CALSCALE:GREGORIAN\n')
ical.write('METHOD:PUBLISH\n')


#

def toicsmon(a,t,date): #mon
    print(a)
    ical.write('BEGIN:VEVENT\n')
    c=a.split('-')
    if (len(c) == 1):
        ical.write('SUMMARY:{}\n'.format(c[0]))
        
    if (len(c)== 2):
        
        ical.write('SUMMARY:{}\n'.format(c[0]))
        
    if (len(c)== 3):
        
        ical.write('SUMMARY:{}\n'.format(c[0]))
        ical.write('LOCATION:{} {}\n'.format(c[2], c[1]))
        
    if (len(c) == 4):
        
        if 'class' in a[1].lower():
            ical.write('SUMMARY:{}\n'.format(c[0]))
            ical.write('LOCATION:{} {}\n'.format(c[3], c[2]))
        else:
            ical.write('SUMMARY:{}\n'.format(c[0]))
            ical.write('LOCATION:{} {}\n'.format(c[3], c[2]))
            
            
    dtstart_list = timestart1[t].split(':')
    dtend_list = timeend1[t].split(':')
    
    truedate=""
    if((fday+date)<10):
        truedate="0"+str(fday+date)
    else:
        truedate=(fday+date)
        
    tem=""
    tem+="DTSTART:"+str(fyear)+str(fmonth)+str(truedate)+("T")+str(dtstart_list[0])+str(dtstart_list[1])+("Z")+'\n'
    print(tem)
    tem=tem.replace(" ", "")
    ical.write(tem)
    
    tem=""
    tem+="DTEND:"+str(fyear)+str(fmonth)+str(truedate)+("T")+str(dtend_list[0])+str(dtend_list[1])+("Z")+'\n'
    print(tem)
    tem=tem.replace(" ", "")
    ical.write(tem)
    ical.write('END:VEVENT\n')
    
#   
    
def toicsttf(a,t,date): #tue to fri
    print(a)
    ical.write('BEGIN:VEVENT\n')
    c=a.split('-')
    if (len(c) == 1):
        ical.write('SUMMARY:{}\n'.format(c[0]))
        
    if (len(c)== 2):
        
        ical.write('SUMMARY:{}\n'.format(c[0]))
        
    if (len(c)== 3):
        
        ical.write('SUMMARY:{}\n'.format(c[0]))
        ical.write('LOCATION:{} {}\n'.format(c[2], c[1]))
        
    if (len(c) == 4):
        
        if 'class' in a[1].lower():
            ical.write('SUMMARY:{}\n'.format(c[0]))
            ical.write('LOCATION:{} {}\n'.format(c[3], c[2]))
        else:
            ical.write('SUMMARY:{}\n'.format(c[0]))
            ical.write('LOCATION:{} {}\n'.format(c[3], c[2]))
            
    
    dtstart_list = timestart2[t].split(':')
    dtend_list = timeend2[t].split(':')
    
    truedate=""
    if((fday+date)<10):
        truedate="0"+str(fday+date)
    else:
        truedate=(fday+date)
    
    tem=""
    tem+="DTSTART:"+str(fyear)+str(fmonth)+str(truedate)+("T")+str(dtstart_list[0])+str(dtstart_list[1])+("Z")+'\n'
    print(tem)
    tem=tem.replace(" ", "")
    ical.write(tem)
    
    tem=""
    tem+="DTEND:"+str(fyear)+str(fmonth)+str(truedate)+("T")+str(dtend_list[0])+str(dtend_list[1])+("Z")+'\n'
    print(tem)
    tem=tem.replace(" ", "")
    ical.write(tem)
    ical.write('END:VEVENT\n')
    
    
cll=0            
date=0
for i in day1:
    cl+=1
    now=i
    
    if cll==8:
        date+=1
        cll=0
        
    if cl<=8:
        toicsmon(now,cll,date)
    elif cl>8 and cl<=16:
        toicsttf(now,cll,date)
    elif cl>16 and cl<=24:
        toicsttf(now,cll,date)
    elif cl>24 and cl<=32:
        toicsttf(now,cll,date)
    elif cl>32 and cl<=40:
        toicsttf(now,cll,date)
    cll+=1    
    print(date)
        
ical.write('END:VCALENDAR\n')
ical.close()


