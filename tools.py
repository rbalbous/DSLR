import math
import numpy as np

def min(tab):
	min_tab = float(tab[1])
	for item in tab:
		if item == '':
			continue
		if min_tab > float(item):
			min_tab = float(item)
	return min_tab

def max(tab):
	max_tab = float(tab[1])
	for item in tab:
		if item == '':
			continue
		if max_tab < float(item):
			max_tab = float(item)
	return max_tab

def mean(tab):
	mean_tab = 0
	for item in tab:
		if item == '':
			continue
		mean_tab += float(item)
	mean_tab /= len(tab)
	return mean_tab

def std(tab):
	std_tab = 0
	mean_tab = mean(tab)
	for item in tab:
		if item == '':
			continue
		std_tab += (float(item) - mean_tab)**2
	std_tab = math.sqrt(std_tab / len(tab))
	return std_tab

def q1(tab):
	tab.sort()
	return (float(tab[math.ceil(len(tab)/4)]) - 1)

def q3(tab):
	tab.sort()
	return (float(tab[math.ceil((3 * len(tab))/4) - 1]))

def median(tab):
	tab.sort()
	tab_len = len(tab)
	if (tab_len % 2 == 0):
		median = (float(tab[(tab_len // 2)]) + float(tab[(tab_len // 2) - 1])) / 2
	else:
		median = float(tab[math.floor(tab_len / 2)])
	return median
