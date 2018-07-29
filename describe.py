import csv
import math
import sys
import time
from tools import *

def shoz_results(tab_elem)

def init_tab(tab):
	first_row = 1
	tab_elem = []
	print('ok')
	for row in tab:
		for i in range(len(row)):
			if (first_row == 1):
				tab_elem.append([])
				tab_elem[i].append(row[i])
				print(tab_elem[i])
			else:
				try:
					float(row[i])
					if float(row[i]) == float(row[i]):
						tab_elem[i].append(float(row[i]))
				except:
					# time.sleep(0.3)
					continue
		first_row = 0
	show_results(tab_elem)
	tab_elem[6].pop(0)
	print(tab_elem[6])
	print(mean(tab_elem[6]))

def main():
    sys.argv.pop(0)
    for i in range (len(sys.argv)):
        print (sys.argv[i])
        try:
            with open(sys.argv[i]) as fd:
                tab = csv.reader(fd)
                print (sys.argv[i])
                init_tab(tab)
        except:
            print("not a csv file")
            continue

if __name__ == "__main__":
    main()