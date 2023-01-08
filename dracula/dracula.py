#!/usr/bin/env python3

"""Dracula script | Jesse Ryan"""
count= 0

with open("dracula.txt","r") as file_object:
    with open("vampytimex.txt", "w") as fang:
        for line in file_object:
            if "vampire" in line.lower():
                print(line)
                count += 1
                fang.write(line)

print(count)
