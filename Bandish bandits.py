import csv
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("Data1.csv")
fig = ff.create_distplot([df["Avg Rating"]],["Avg"])

fig.show()