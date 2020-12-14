import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import scipy.integrate as integrate
from scipy.interpolate import InterpolatedUnivariateSpline

file = 'W:/Projekte/MAXCoat_61906/04_Bearbeitung/GDL-Analyse/Abbott_Analyse/Curve/abbott_2_curve.txt'

df_abbott = pd.read_csv(file, decimal=',', encoding='cp1252',
                              error_bad_lines=False, delim_whitespace=True,
                              index_col=False, keep_default_na=False, skiprows=4)

x_values = np.asarray(df_abbott['%'])
y_values = np.asarray(df_abbott['µm'])

f = interp1d(x_values, y_values, kind='linear', fill_value="extrapolate")

#f = InterpolatedUnivariateSpline(x_values, y_values, k=2)

result_vvc = integrate.quad(f, 10, 80) - ((y_values.min() + f(10)) * 70)
result_vmc = ((f(80) - f(10)) * 70) - result_vvc

vmc_perc = result_vmc / (result_vmc + result_vvc)
print(result_vmc, result_vvc, vmc_perc)

#plt.plot(x_values, y_values)
plt.plot(x_values, f(x_values))
plt.vlines([10, 80], y_values.min(), y_values.max())
plt.hlines([f(10), f(80)], 0, 100, linestyle='--')
plt.gca().invert_yaxis()

plt.legend()
plt.show()