from pandas import set_option, read_csv


set_option("display.max_columns", None)

data = read_csv("files/winemag-data-130k-v2.csv")

new_data = data.drop(columns="region_2")
new_data = new_data.dropna(subset="country")

mean_price = new_data["price"].sum() / new_data["price"].count()

new_data["price"] = new_data["price"].fillna(value=mean_price)

# print(new_data.loc[10:20, ["country", "price"]])
# print(new_data[new_data.price > 300].loc[345:350, ["country", "price"]])
# print(new_data[(new_data.price > 300) & (new_data.country == "Italy")])

print(new_data.groupby(by=["country", "price"]).count())
