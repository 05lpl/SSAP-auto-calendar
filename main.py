import os
import re
from option import options
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def add_time(time, delta):
	delta = timedelta(days=delta)
	input_time = time + delta
	ics_formatted_time = input_time.strftime("%Y%m%dT%H%M%S")
	return ics_formatted_time

def get_time(time, delta):
	time = f"{opt.year}-{opt.month}-{opt.day} {time}:00"
	return add_time(datetime.strptime(time, "%Y-%m-%d %H:%M:%S"), delta)

def get_str(name, loc, start_time, end_time, delta):
	str = 'BEGIN:VEVENT\n'
	str += f"DTSTART;TZID=Asia/Shanghai:{get_time(start_time, delta)}\n"
	str += f"DTEND;TZID=Asia/Shanghai:{get_time(end_time, delta)}\n"
	str += f"SUMMARY:{name}\n"
	str += f"LOCATION:{loc}\n"
	if opt.repeat is True:
		str += f"RRULE:FREQ=WEEKLY;UNTIL={get_time(start_time, opt.repeat_weeks * 7)}\n"
	if opt.alarms is True:
		str += f"BEGIN:VALARM\n"
		str += f"TRIGGER:-PT{opt.alarm_set_time}M\n"
		if opt.alarm_mode == "audio" or opt.alarm_mode == 'all':
			str += f"ACTION:AUDIO\n"
		if opt.alarm_mode == "display" or opt.alarm_mode == 'all':
			str += f"ACTION:DISPLAY\n"
		str += f"END:VALARM\n"
	str += 'END:VEVENT\n'
	return str

def check(name):
	if opt.exclude is False:
		return False
	for str in opt.exclude_class:
		if name.count(str) > 0:
			return True
	return False

def check_next(k):
	change_spot = {'class': ['fc-highlight-container']}
	if k.attrs == change_spot:
		return True
	return False

if __name__ == '__main__':

	opt = options().get_opt()
	print(opt)

	with open(opt.read_path,"r") as f:
		data=f.read()
	
	soup = BeautifulSoup(data, 'lxml')
	divs = soup.find_all('div')
	h2 = soup.find_all('h2')
	# get all the data we need

	with open("debug.txt","w") as f:
		f.write(soup.prettify())

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
	flag = False #看课表是否出现
	pointer = 0  #星期几
	deltas = []  #星期几
	for i in range(len(divs)):
		k = divs[i]
		if k.string is not None:
			if k.string == "确定":
				continue
			classes.append(k.string)
			deltas.append(pointer)
			flag = True
		if flag and i+2<len(divs) and check_next(divs[i+2]):
			pointer += 1

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
		str += get_str(name, loc, time_start, time_end, deltas[k*2])
		# name是课程名称
		# time是时间
		# loc是地点

	str += "END:VCALENDAR\n"

	with open(opt.save_path, "a") as f:
		f.write(str)

