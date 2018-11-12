import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys,os

df = pd.read_csv("result_seo.csv",usecols=["word","number"])
sub_x1 = []
sub_x1.append(list(df["number"]))
print(sub_x1)
sub_x2 = [int(a) for a in sub_x1]
x = np.array(sub_x2)
sub_label=[]
sub_label.append(list(df["word"]))
label = list(sub_label)
plt.pie(x, labels=label, counterclock=False, startangle=90)
