import csv
import math
import sys
import time
from tools import *


def init_tab(data):
	name = [x for x in data[0]]
	len_data = len(data[0])
	elem = [[row[i] for row in data] for i in range(len_data)]
	# len_data = 10
	print("          ", end = '')
	for i in range (6, len_data):
		print("%-15.9s" % name[i], end = '')
	print('')
	print("max:    ", end = '')
	for i in range (6, len_data):
		print("%-15.2f" % max(elem[i][1:]), end = '')
	print('')
	print("min:    ", end = '')
	for i in range (6, len_data):
		print("%-15.2f" % min(elem[i][1:]), end = '')
	print('')
	print("mean:   ", end = '')
	for i in range (6, len_data):
		print("%-15.2f" % mean(elem[i][1:]), end = '')
	print('')
	print("std:    ", end = '')
	for i in range (6, len_data):
		print("%-15.2f" % std(elem[i][1:]), end = '')
	print('')
	print("q1:     ", end = '')
	for i in range (6, len_data):
		print("%-15.2f" % q1(elem[i][1:]), end = '')
	print('')
	print("q3:     ", end = '')
	for i in range (6, len_data):
		print("%-15.2f" % q3(elem[i][1:]), end = '')
	print('')
	print("median: ", end = '')
	for i in range (6, len_data):
		print("%-15.2f" % median(elem[i][1:]), end = '')
	print('')
	# for i in range(6, len_data):
		# print(f"max: {max(elem[i][1:])}, min(elem[i][1:]), mean(elem[i][1:]), std(elem[i][1:]), q1(elem[i][1:]), q3(elem[i][1:]), median(elem[i][1:])")


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