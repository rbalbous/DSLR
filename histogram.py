import csv
import sys
import matplotlib.pyplot as plt

def init_tab(data):
    name = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]
    house = [[item for item in data if item[1] == name[i]] for i in range(4)]


    fig = plt.figure(figsize=(25, 15), facecolor='beige')
    fig.canvas.set_window_title('[Histogram]')
    color = {'Gryffindor':'crimson', 'Slytherin':'green', 'Ravenclaw':'teal', 'Hufflepuff':'purple'}
    plt.subplot(5, 3, 1)
    plt.text(0.2, 0.2, 'Gryffindor', fontdict={'color':color['Gryffindor'],'size':12})
    plt.text(0.2, 0.6, 'Ravenclaw', fontdict={'color':color['Ravenclaw'],'size':12})
    plt.text(0.6, 0.2, 'Hufflepuff', fontdict={'color':color['Hufflepuff'],'size':12})
    plt.text(0.6, 0.6, 'Slytherin', fontdict={'color':color['Slytherin'],'size':12})
    plt.xticks([], [])
    plt.yticks([], [])
    plt.title('Houses')
    for i, feature in enumerate(house):
        plt.subplot(5, 3, i + 2)
        plt.title(feature)
        plt.grid(True)
        for idx, item in enumerate(name):
            plt.hist(item, 20, facecolor=color[name[idx]], alpha=0.5)
    plt.subplots_adjust(top=0.9, bottom=0.1, left=0.1, right=0.9, hspace=0.5, wspace=0.3)
    plt.show()  


def main():
    sys.argv.pop(0)
    for item in sys.argv:
        # try:
        with open(item) as fd:
            tab = csv.reader(fd)
            data = list(tab)
            init_tab(data)
        # except:
        #     print("not a csv file")


if __name__ == "__main__":
    main()