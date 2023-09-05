#!/usr/bin/env python3
import os
from option import options

if __name__ == '__main__':

	opt = options().get_opt()
	print(opt)

	if opt.first is True:
		os.system("pip3 install beautifulsoup4")
		os.system("pip3 install lxml")

	os.system("python3 main.py")
