import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_data = pd.read_csv('C:/Users/Kapp/PycharmProjects/abbott/roughness/maxcoat.csv', sep=';')


df_data_none = df_data[df_data['Vorbehandlung'] == 'keine']
mean_roughness_none = df_data_none['Ra_nf [µm]'].mean()
std_roughness_none = df_data_none['Ra_nf [µm]'].std()


df_data_pp = df_data[df_data['Vorbehandlung'] == 'plasmapoliert']
mean_roughness_pp = df_data_pp['Ra_nf [µm]'].mean()
std_roughness_pp = df_data_pp['Ra_nf [µm]'].std()


df_data_gps = df_data[df_data['Vorbehandlung'] == 'GPS']
mean_roughness_gps = df_data_gps['Ra_nf [µm]'].mean()
std_roughness_gps = df_data_gps['Ra_nf [µm]'].std()

df_data_ms = df_data[df_data['Vorbehandlung'] == 'ms']
mean_roughness_ms = df_data_ms['Ra_nf [µm]'].mean()
std_roughness_ms = df_data_ms['Ra_nf [µm]'].std()

roughness = mean_roughness_none, mean_roughness_pp, mean_roughness_gps, mean_roughness_ms
std= std_roughness_none, std_roughness_pp, std_roughness_gps, std_roughness_ms

samples = ['unbehandelt', 'plasmapoliert', 'glasperlstrahlen', 'mikrostrahlen']

plt.barh(samples, roughness, color=['blue', 'orange', 'green'], xerr=std)
#plt.vlines(mean_roughness, 0, len(np.asarray(samples))-1, linestyle='--', colors='red')
plt.title('Rauheit Vergleich', pad=10, fontsize=16)
#for t in treatments:

xticks = [x / 100 for x in range(0, 100, 5)]
plt.xticks(xticks, fontsize=12)
plt.xlabel('Ra [µm]', labelpad=10, fontsize=14)
plt.yticks(fontsize=14)
plt.show()