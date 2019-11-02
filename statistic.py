import os, sys

statistic = []

with open("result.txt", ‘r’) as f:
	s = f.readline().split()
	f.close()
	statistic.append(s)