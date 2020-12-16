import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob


for filename in glob.glob('C:/Users/Julian/Desktop/neu/Präsentation/Kontaktwiderstände/Gasdiffusionslagen/Freudenberg H23/h23_reference.csv'):
    df_data = pd.read_csv(filename, delimiter=',', sep='\t')
    print(df_data)

    # df_data.sort_values(by=['pressure_rounded[bar]'], inplace=True)
    # df_x = df_data['pressure_rounded[bar]']
    # df_y_mean = df_data['main_resistance_mean[mOhm]']
    # df_y_scatter = df_data['main_resistance[mOhm]']

    df_data_10bar = df_data[df_data['pressure_rounded[bar]'] == 10]
    df_data_10bar.sort_values(by=['cycle'], inplace=True)

    cycles = np.unique(df_data_10bar['cycle'])

    x_values = np.asarray(cycles)

    res_list = []

    for c in cycles:
        df_data_cycles = df_data_10bar[df_data_10bar['cycle'] == c]

        res = (df_data_cycles['voltage[mV]'] / df_data_cycles['current[mA]']) * 1000 * 4.15 / 2
        res_list.append(res)

    y_values = np.asarray(res_list)


    plt.plot(x_values, y_values)
    plt.xlabel('Zyklen')
    plt.ylabel('spez. Widerstand [mOhm*cm²]')
    plt.ylim(0, 10)

plt.show()
