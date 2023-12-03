"""ParrishScott_M06Ex15.py  by: Scott Parrish v: 0.1 12/02/2023 Exercise 15.1
Program to create 3 processes which each wait a random time between zero and one
second and then print a formatted time string."""

import time
from multiprocessing import Process
from random import random


def my_time(process_num: int) -> None:
    """Function to wait a random time between 0 and 1 second and then print the
    current time. Intended to be invoked by an iterator, the function takes an
    int to display where it was invoked in the iterator."""

    fmt = "The time is %I:%M:%S %p"     # prints time as 12:31:35 PM
    time.sleep(random())    # Sleeps for a random time between 0 and 1 sec
    now = time.localtime()
    print(f'From process {process_num}: {time.strftime(fmt, now)}')

if __name__ == "__main__":
    # Create 3 processes and let them cook
    for n in range(3):
        process = Process(target=my_time, args=(n,))
        process.start()