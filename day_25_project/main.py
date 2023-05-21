import pandas as pd

location = r""".\day_25_project\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"""

dt_squirrels = pd.read_csv(location)
squirrels_color = dt_squirrels["Primary Fur Color"].dropna()
squirrels_color_quantity = squirrels_color.groupby(squirrels_color).count()
s_r = pd.DataFrame(squirrels_color_quantity)
s_r.rename(columns={'Primary Fur Color':'Quantity'},inplace=True)
s_r.reset_index(inplace=True)
s_r.rename(columns={'Primary Fur Color':'Fur Color'},inplace=True)
s_r.to_csv(".\day_25_project\squirrel_count.csv")