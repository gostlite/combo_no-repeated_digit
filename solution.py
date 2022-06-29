#!/usr/bin/python3


for num in range(1, 90):
    if not num % 10 < num / 10:
        print(f"{num:02d} ", end="")
