#!/usr/bin/env python
import functools
import os
import random
import time
import commands as cmd
from piui import PiUi
import serial

ser = serial.Serial("/dev/ttyACM0", 9600)
#time.sleep(2)
#ser.write("3")
#time.sleep(1)
#ser.write("1")

current_dir = os.path.dirname(os.path.abspath(__file__))


class Room(object):
    def __init__(self):
        self.title = None
        self.ui = PiUi(img_dir=os.path.join(current_dir, 'imgs'))

    def main_menu(self):
        self.page = self.ui.new_ui_page(title="Rohith's Room")
        self.page = self.ui.new_ui_page(title="Main Control Board")
        self.list = self.page.add_list()
        self.lig = self.list.add_item("Lights", chevron=False, toggle=True,
                                      ontoggle=functools.partial(self.ontoggle, "Light"))
        self.fan = self.list.add_item("Fan", chevron=False, toggle=True,
                                      ontoggle=functools.partial(self.ontoggle, "Fan"))
        self.page.add_element("hr")

     

        #self.tempbtn = self.page.add_button("Temp", self.get_temp)
        self.page.add_element("hr")
        ser.write("5")
        temp = ser.readline()
        self.title = self.page.add_textbox("<center>Temperature is " + " Loading.... " + " degree Celsius </center>",'h3')
		
		self.get_temp()

        self.ui.done()

    def main(self):
        self.main_menu()
        self.ui.done()

    def get_temp(self):
        ser.write("5")
        time.sleep(1)
        temp = ser.readline()
        self.title.set_text("<center>Temperature is " + str(temp) + " degree Celsius </center>")


   

    def ontoggle(self, what, value):


        if str(value) == "True" and what == "Light":
            ser.write("4")


        elif str(value) == "False" and what == "Light":
            ser.write("3")

        elif str(value) == "True" and what == "Fan":
            ser.write("2")

        elif str(value) == "False" and what == "Fan":
            ser.write("1")


def main():
    piui = Room()
    piui.main()


if __name__ == '__main__':
    main()
