import os
import torch
import argparse

class options():    
    def init(self):
        with open(self.opt.head_path, "r") as f:
            str = f.read()
        with open(self.opt.save_path, "w") as f:
            f.write(str)
    def get_opt(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--day", type=int, default=1, help="The starting day of the week.")
        parser.add_argument("--month", type=int, default=9, help="The starting day of the week.")
        parser.add_argument("--year", type=int, default=2023, help="The starting day of the week.")
        parser.add_argument("--save_path", type=str, default='export.ics', help="The path to store the calender.")
        parser.add_argument("--read_path", type=str, default="date.txt", help="The read path.")
        parser.add_argument("--head_path", type=str, default="header.txt", help="The first few lines of the document.")
        self.opt = parser.parse_args()
        self.init()
        return self.opt
