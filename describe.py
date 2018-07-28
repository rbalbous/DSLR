import csv
import math
import sys

def init_tab(file)
    first_line = 1
    for item in tab:
        for elem in item:
            try:
                tab_m.append([])
                first_line = 2
            except:
                first_line = 1
                print ("NaN")
                continue

def main():
    tab_m = []
    sys.argv.pop(0)
    for i in range (len(sys.argv)):
        try:
            with open(sys.argv[i]) as file:
                tab = csv.reader(file)
                init_tab(file)
        except:
            print("not a csv file")
            continue

if __name__ == "__main__":
    main()