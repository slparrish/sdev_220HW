"""ParrishScott_M06Ex132n3.py by: Scott Parrish v: 0.1 12/02/2023
program to read the contents of the file today.txt and convert the string to 
a date object."""
import time


fmt = "%B %d, %Y"   # Format for strf/ptime January 1, 1970
today_file = open('today.txt', 'r')     # Open date file for reading
today_string = today_file.read()        # Read the string
today_file.close()                      # Close the file
parsd = time.strptime(today_string, fmt)   # Parse string to obj using format fmt
print(parsd)