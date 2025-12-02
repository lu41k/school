from pandas import set_option, read_csv


set_option("display.max_columns", None)

data = read_csv("files/winemag-data-130k-v2.csv")

print(data.isna)
