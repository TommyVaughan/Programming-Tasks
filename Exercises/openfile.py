# Tommy Vaughan 02/03/2018
# Format the Data/iris.csv file
# print(line.split(',')[:4]) was my code which was still showing brackets and commas
# The group discussion directed me towards line splitting each column seperately.

with open("Data/iris.csv") as f:
 for line in f: 
  print('{:4} {:4} {:4} {:4}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3])) 

