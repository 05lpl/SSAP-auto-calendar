#!/usr/bin/env python3
import pandas as pd
import xlrd 
from datetime import date, datetime, timedelta, timezone
from bs4 import BeautifulSoup
import re
with open("date.txt","r") as f:
	data=f.readline()
	
	
soup = BeautifulSoup(data, 'lxml')	
a=[]
a=soup.find_all(class_='fc-text')
paragraphs = []
new=[]
for x in a:
	paragraphs.append(re.findall(r'>([^"]*)<', str(x)))
for x in paragraphs:
	new.append(str(x))
location=[]

name=[]
for j in new:

	if len(j)<12:
		location.append(j)
	else:
		name.append(j)

newname=[]
for i in range(0,len(name)):
	newname.append((name[i])[2:-21])



	
	#newname 课程名列表
	#location 课程位置
	
	#------------------------------------------
	
	
	
fyear=2023#输入第一天的年
fmonth="06"#输入第一天的月
fday=26#输入第一天的日






day1=[]
days=[2,4,5,6,7]

	

ICAL_PATH = 'export.ics'

#
#timestart1=['08:1000','08:5500','09:4000','10:2500','11:1000','14:2000','15:1500','16:4500']
#timeend1=['08:5000','09:3500','10:2000','11:0500','11:5000','15:0000','15:5500','16:4500']
#
#timestart2=['08:0000','08:5000','09:3700','10:2500','11:1000','14:2000','15:1500','16:0500']
#timeend2=['08:4000','09:3000','010:1700','11:0500','11:5000','15:0000','15:5500','16:4500']

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

def toicsmon(name,locations,date,t): #mon
	
	ical.write('BEGIN:VEVENT\n')
	ical.write('SUMMARY:{}\n'.format(name))
	ical.write('LOCATION:{}\n'.format(locations))
	
	# t = locations
	# print("THis is t", t)
			
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
	print("This is a", a)
	if(type(a) == int): 
		return
	ical.write('BEGIN:VEVENT\n')
	c=a.split('-')
	print("This is c", c)
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
	
	
if __name__ == '__main__':
	cll=0            
	date=0
	for i in day1:
		cl+=1
		now=i
		
		if cll==8:
			date+=1
			cll=0
			
		if cl<=8:
			toicsmon(now,cll,date,cll)
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
	
	
	cll=0            
	date=0
	for i in range(0,len(name)):
		cl+=1
		now=i
		
		if cll==8:
			date+=1
			cll=0
			
		if cl<=8:
			print(newname[i],location[i])
			toicsmon(newname[i],location[i],date,cll)
			
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

	