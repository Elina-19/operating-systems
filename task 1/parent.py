#!/usr/bin/python3

import os
import random
import time
import sys

def fork():
    child = os.fork()
    if child > 0:
        print(f'Parent[{os.getpid()}]: I ran children process with PID {child}.')
    else:
        os.execl(sys.executable, sys.executable, "child.py", str(random.randint(5, 10)))


n = int(input())
for i in range(n):
    fork()

count = 0
while count != n
    pid, status = os.wait()
    if pid > 0:
        print(f'Parent[{os.getppid()}]: Child with PID {pid} terminated. Exit Status {status}.')
        if status != 256:
            fork()
        else:
        	count = count + 1
