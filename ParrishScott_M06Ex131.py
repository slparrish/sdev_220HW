"""ParrishScott_M06Ex131.py  by: Scott Parrish  v: 0.1 12/02/2023
Program to write a formatted date string to the file today.txt
use the format January 1, 1970.  Creates or opens the file today.txt 
and overwrites any data in the file."""
import time


fmt = "%B %d, %Y"       # format for string
today = time.localtime() # create a time object for current date and time
today_fmt = time.strftime(fmt, today)   # create a date string from the today
                                        # object
today_file = open('today.txt', 'wt')    # Open/create the file for overwriting
today_file.write(today_fmt)             # write formatted string
today_file.close()                      # close file