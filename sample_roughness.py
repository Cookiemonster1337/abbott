import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_data = pd.read_csv('C:/Users/Kapp/PycharmProjects/abbott/roughness/maxcoat.csv', sep=';')


behandlung = 'geschliffen'
print(df_data)
df_data = df_data[df_data['Vorbehandlung'] == behandlung]
mean_roughness = df_data['Ra_nf [µm]'].mean()

roughness = df_data['Ra_nf [µm]']
samples = df_data['Probe']
#
plt.barh(samples, roughness)
#plt.vlines(mean_roughness, 0, len(np.asarray(samples))-5, linestyle='--', colors='red')
plt.title('Rauheit (' + behandlung + ')', pad=10, fontsize=16)
xticks = [x / 100 for x in range(0, 30, 2)]
plt.xticks(xticks, fontsize=12)
plt.xlabel('Ra [µm]', labelpad=10, fontsize=14)
plt.yticks(fontsize=14)
plt.show()