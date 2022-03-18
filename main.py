# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import geopandas
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


def draw_map():
    # Use a breakpoint in the code line below to debug your script.
    data = geopandas.read_file('./europe.json')
    group_1 = ['SE', 'FI', 'DK', 'LU', 'DE', 'IE', 'FR', 'ES', 'PT', 'IT', 'BE', 'NL']
    group_2 = ['DK', 'EE', 'FI', 'FR', 'IE', 'LV', 'LU', 'NL', 'PT', 'ES', 'SE', 'DE', 'AT']
    group_3 = ['AT', 'DK', 'LV', 'SV', 'CZ', 'FI', 'NL', 'SE', 'DE']
    data = data[data['ISO2'] != 'RU']

    cmap = ListedColormap(["lightgreen", "gold", "lawngreen", "lightseagreen"])

    data['GROUP_1'] = float('NaN')
    data['GROUP_1'][data['ISO2'].isin(group_1)] = 1

    data['GROUP_2'] = float('NaN')
    data['GROUP_2'][data['ISO2'].isin(group_2)] = 1

    data['GROUP_3'] = float('NaN')
    data['GROUP_3'][data['ISO2'].isin(group_3)] = 5
    fig, ax = plt.subplots(1, 1)

    data.plot(facecolor="none", edgecolor="black", ax=ax)
    data.plot(column='GROUP_3', ax=ax, cmap=cmap, edgecolor='none', facecolor='grey')

    data.plot(column='GROUP_1', ax=ax, facecolor='none', hatch='/////', edgecolor='black')
    data.plot(facecolor="none", edgecolor="black", ax=ax)
    data.plot(column='GROUP_2', ax=ax, edgecolor="red", facecolor='none', linewidths=0.75)
    plt.show()

    fig.savefig('./fig.png', dpi=600, transparent=True)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    draw_map()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
