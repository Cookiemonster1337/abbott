import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import glob

#l = [pd.read_csv(filename) for filename in glob.glob("/path/*.txt")]


#file_02Nm = 'W:/Projekte/MAXCoat_61906/04_Bearbeitung/GDL-Analyse/Abbott_Analyse/abbott_0,2_curve.txt'

for filename in glob.glob('W:/Projekte/MAXCoat_61906/04_Bearbeitung/GDL-Analyse/Abbott_Analyse/Depth/*.txt'):
    df_abbott_specs = pd.read_csv(filename, decimal=',', encoding='cp1252',
                              error_bad_lines=False, delim_whitespace=True,
                              index_col=False, keep_default_na=False, skiprows=4)


    y_pos = np.arange(len(np.asarray(df_abbott_specs['µm'])))
    values = np.asarray(df_abbott_specs['%'])
    objects = np.asarray(df_abbott_specs['µm'])
    #y_values = np.asarray(df_abbott_specs['µm'])


    graphname = filename.split('/')[-1].split('\\')[-1].strip('abbott_').strip(
        '_curve.tx')
    plt.barh(y_pos, values, label=graphname)
    plt.yticks(y_pos, objects)
    plt.gca().invert_yaxis()

plt.legend()
plt.show()