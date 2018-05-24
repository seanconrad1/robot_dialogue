# --------------------------------
# Sean Conrad
# 5/23/18
# Dialogue between computer and user
# --------------------------------


import datetime
import time
import sys


def slow_text(word):  # Add a parameter 'speed' to control speeds of different things
    # Makes the text type letter by letter slowly.
    for l in word:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.2)


ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
print(st + " Sean >> ")
slow_text("Hey Denise \n\n")


ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
print(st + " Denise >> ")
slow_text("Hey Sean \n\n")

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
print(st + " Sean >> ")
slow_text("I'm just chillin wbu? \n\n")

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
print(st + " Denise >> ")
slow_text("Venmo'ing you a ton of money \n\n")

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
print(st + " Sean >> ")
slow_text("Oh heck ya! \n\n")



