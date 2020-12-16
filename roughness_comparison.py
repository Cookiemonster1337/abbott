import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_data = pd.read_csv('C:/Users/Julian/PycharmProjects/abbott/roughness/maxcoat.csv', sep=';')


df_data_none = df_data[df_data['Vorbehandlung'] == 'keine']
mean_roughness_none = df_data_none['Ra_nf [µm]'].mean()

df_data_pp = df_data[df_data['Vorbehandlung'] == 'plasmapoliert']
mean_roughness_pp = df_data_pp['Ra_nf [µm]'].mean()

df_data_gps = df_data[df_data['Vorbehandlung'] == 'GPS']
mean_roughness_gps = df_data_gps['Ra_nf [µm]'].mean()

df_data_exz = df_data[df_data['Vorbehandlung'] == 'schleifen']
mean_roughness_exz = df_data_exz['Ra_nf [µm]'].mean()

roughness = mean_roughness_none, mean_roughness_pp, mean_roughness_gps, mean_roughness_exz
samples = ['unbehandelt', 'plasmapoliert', 'glasperlstrahlen', 'schleifen']

plt.barh(samples, roughness, color=['blue', 'orange', 'green'])
#plt.vlines(mean_roughness, 0, len(np.asarray(samples))-1, linestyle='--', colors='red')
plt.title('Rauheit Vergleich', pad=10, fontsize=16)
#for t in treatments:

xticks = [x / 100 for x in range(0, 100, 5)]
plt.xticks(xticks)
plt.xlabel('Ra [µm]', labelpad=10)
plt.show()