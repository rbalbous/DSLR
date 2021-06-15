import csv
import math
import sys
import time
from tools import *

def print_elem(element, len_data):
		print("max:    ", end = '')
		for i in range (6, len_data):
			print("%15.2f" % {element}, end = '')
		print('')

def init_tab(data):
	name = [x for x in data[0]]
	len_data = len(data[0])
	elem = [[row[i] for row in data] for i in range(len_data)]
	print("        ", end = '')
	for i in range (6, len_data):
		print("%15.10s" % name[i], end = '')
	print('')
	print("max:    ", end = '')
	for i in range (6, len_data):
		print("%15.2f" % max(elem[i][1:]), end = '')
	print('')
	print("min:    ", end = '')
	for i in range (6, len_data):
		print("%15.2f" % min(elem[i][1:]), end = '')
	print('')
	print("mean:   ", end = '')
	for i in range (6, len_data):
		print("%15.2f" % mean(elem[i][1:]), end = '')
	print('')
	print("std:    ", end = '')
	for i in range (6, len_data):
		print("%15.2f" % std(elem[i][1:]), end = '')
	print('')
	print("q1:     ", end = '')
	for i in range (6, len_data):
		print("%15.2f" % q1(elem[i][1:]), end = '')
	print('')
	print("q3:     ", end = '')
	for i in range (6, len_data):
		print("%15.2f" % q3(elem[i][1:]), end = '')
	print('')
	print("median: ", end = '')
	for i in range (6, len_data):
		print("%15.2f" % median(elem[i][1:]), end = '')
	print('')


def main():
	sys.argv.pop(0)
	for item in sys.argv:
		try:
			with open(item) as fd:
				tab = csv.reader(fd)
				data = list(tab)
				init_tab(data)
		except:
			print("not a csv file")


if __name__ == "__main__":
	main()
