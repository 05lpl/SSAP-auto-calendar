import os
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
        parser.add_argument("--read_path", type=str, default="我的日程.html", help="The read path.")
        parser.add_argument("--head_path", type=str, default="header.txt", help="The first few lines of the document.")
        parser.add_argument("--exclude", action="store_true", default=False, help="Whether to exclude some class or not.")
        parser.add_argument("--exclude_class", nargs='+', default=["早自习","升旗","晚自习"])
        parser.add_argument("--repeat", action="store_false", default=False, help="Whether to repeat the calendar or not.")
        parser.add_argument("--repeat_weeks", type=int, default=20, help="repeat how many weeks.")
        parser.add_argument("--alarms", action="store_true", default=False, help="Whether to use the alarm or not.")
        parser.add_argument("--alarm_set_time", type=int, default=5, help="When does the alarm start.")
        parser.add_argument("--alarm_mode", type=str, default="display", help="The mode of the alarm.")
        parser.add_argument("--watch_mode", action="store_true", default=False, help="Show location on watches")
        parser.add_argument("--precise_location", action="store_true", default=False, help="Show precise location")
        self.opt = parser.parse_args()
        self.init()
        return self.opt
