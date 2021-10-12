import csv
import sys
import matplotlib.pyplot as plt
from tools import mean
import numpy as np

def load_csv(filename):
    dataset = list()
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        try:
            for _ in reader:
                row = list()
                for value in _:
                    try:
                        value = float(value)
                    except:
                        if not value:
                            value = np.nan
                    row.append(value)
                dataset.append(row)
        except csv.Error as e:
            print(f'file {filename}, line {reader.line_num}: {e}')
    return np.array(dataset, dtype=object)

def histogram(X, legend, title, xlabel, ylabel):
    h1 = X[:327]
    h1 = h1[~np.isnan(h1)]
    plt.hist(h1, color='red', alpha=0.5)

    h2 = X[327:856]
    h2 = h2[~np.isnan(h2)]
    plt.hist(h2, color='yellow', alpha=0.5)

    h3 = X[856:1299]
    h3 = h3[~np.isnan(h3)]
    plt.hist(h3, color='blue', alpha=0.5)

    h4 = X[1299:]
    h4 = h4[~np.isnan(h4)]
    plt.hist(h4, color='green', alpha=0.5)

    plt.legend(legend, loc='upper right', frameon=False)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def init_tab(data):
    Gryffindor = [float(item[16]) for item in data if item[1] == "Gryffindor" and item[16]]
    Ravenclaw = [float(item[16])  for item in data if item[1] == "Ravenclaw" and item[16]]
    Slytherin = [float(item[16])  for item in data if item[1] == "Slytherin" and item[16]]
    Hufflepuff = [float(item[16])  for item in data if item[1] == "Hufflepuff" and item[16]]
    houses = [Gryffindor, Ravenclaw, Slytherin, Hufflepuff]
    names = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]
#    print(Gryffindor)
    plt.hist(Gryffindor, color='red', alpha=0.5)
    plt.hist(Ravenclaw, color='yellow', alpha=0.5)
    plt.hist(Slytherin, color='blue', alpha=0.5)
    plt.hist(Hufflepuff, color='green', alpha=0.5)

    plt.title('Care of magical creatures')
    plt.xlabel('Grades')
    plt.ylabel('Students')
    plt.show()


def main():
    # try:
        with open('./dataset_train.csv') as fd:
            tab = csv.reader(fd)
            data = list(tab)
            init_tab(data)
    # except:
    #     print("not a csv file")


if __name__ == "__main__":
    main()


# def init_tab(data):
#     name = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]
#     house = [[item[6:] for item in data if item[1] == name[i]] for i in range(4)]
#     subjects = [subj for subj in data[0]][6:]

    