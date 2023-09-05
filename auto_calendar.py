#!/usr/bin/env python3
import re
from option import options
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def init():
	delta = [0,0]
	for i in range(5):
		for j in range(11):
			delta.append(i+1)
	return delta

def get_time(time, delta):
	time = f"{opt.year}-{opt.month}-{opt.day} {time}:00"
	input_time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
	delta = timedelta(days = delta)
	input_time += delta
	ics_formatted_time = input_time.strftime("%Y%m%dT%H%M%S")
	return ics_formatted_time

def get_str(name, loc, start_time, end_time, delta):
	str = 'BEGIN:VEVENT\n'
	str += f"DTSTART;TZID=Asia/Shanghai:{get_time(start_time, delta)}\n"
	str += f"DTEND;TZID=Asia/Shanghai:{get_time(end_time, delta)}\n"
	str += f"SUMMARY:{name}\n"
	str += f"LOCATION:{loc}\n"
	str += 'END:VEVENT\n'
	# print(str)
	return str

def check(name):
	if opt.exclude is False:
		return False
	for str in opt.exclude_class:
		if name.count(str) > 0:
			return True
	return False

if __name__ == '__main__':

	deltas = init()
	opt = options().get_opt()
	print(opt)

	with open(opt.read_path,"r") as f:
		data=f.read()
	
	soup = BeautifulSoup(data, 'lxml')
	divs = soup.find_all('div')
	h2 = soup.find_all('h2')
	# get all the data we need

	for k in h2:
		if k.string is not None:
			date_list = re.findall(r"\d+", k.string)
			# print(date_list, k.string)
			opt.year = date_list[0]
			opt.month = date_list[1]
			opt.day = date_list[2]
			# print(opt.year,opt.month,opt.day)
			break

	classes = []
	for k in divs:
		if k.string is not None:
			if k.string == "确定":
				continue
			classes.append(k.string)
			# print(k.string)

	#此时classes已经存储了所有的信息，每两个为一组

	str = ""

	for k in range(len(classes)//2):
		i = 2 * k
		j = 2 * k + 1
		name = classes[i][:-11]
		if(check(name)):
			continue;
		time = classes[i][-11:]
		time_start, time_end = time.split('-')
		loc = classes[j]
		str += get_str(name, loc, time_start, time_end, deltas[k])
		# name是课程名称
		# time是时间
		# loc是地点

	str += "END:VCALENDAR"

	with open(opt.save_path, "a") as f:
		f.write(str)
