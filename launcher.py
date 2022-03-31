import os
os.system(f'python3 sussy.py {open("target.txt").read().split(":")[0]} -p {open("target.txt").read().split(":")[1]} -ua -v -s 10000 --sleeptime 0')
