#!/usr/bin/python3

import re

line = input("Enter text: ")
names = re.findall("(\w+_\w+)", line)
new_names = []

for name in names:
  new_names.append(name[:name.find('_')].capitalize() + name[name.find('_') + 1:].capitalize())

for new_name in new_names:
  print(new_name)

for i in range(0,len(new_names) - 1):
  line = line.replace(names[i],new_names[i])

print(line)