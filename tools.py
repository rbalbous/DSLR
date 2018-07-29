import math
import numpy

def min(tab):
	min_tab = tab[0]
	for i in range(len(tab)):
		if min_tab > tab[i]:
			min_tab = tab[i]
	return min_tab

def max(tab):
	max_tab = tab[0]
	for i in range(len(tab)):
		if max_tab < tab[i]:
			max_tab = tab[i]
	return max_tab

def mean(tab):
	mean_tab = 0
	for i in range(len(tab)):
		mean_tab += tab[i]
	mean_tab /= len(tab)
	return mean_tab

def std(tab):
	std_tab = 0
	mean_tab = mean(tab)
	for i in range(len(tab)):
		std_tab += (tab[i] - mean_tab)**2
	std_tab = math.sqrt(std_tab / len(tab))
	return std_tab

def q1(tab):
	tab.sort()
	return (tab[math.ceil(len(tab)/4)] - 1)

def q3(tab):
	tab.sort()
	return (tab[math.ceil((3 * len(tab))/4) - 1])

def median(tab):
	tab.sort()
	tab_len = len(tab)
	if (tab_len % 2 == 0):
		median = (tab[(tab_len // 2)] + tab[(tab_len // 2) - 1]) / 2
	else:
		median = tab[math.floor(tab_len / 2)]
	return median
