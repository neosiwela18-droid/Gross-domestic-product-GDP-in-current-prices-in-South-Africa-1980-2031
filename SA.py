import pandas as pd
import matplotlib.pyplot as plt
import mplcursors

df = pd.read_csv(r"gross_domestic_product_gdp_in_current_prices_in_south_africa_from_1980_to_2031_in_billion_u.s._dollars.csv")

y = df["gdp"]
x = df["year"]
fig, ax = plt.subplots()
sc = ax.plot(x,y, marker ="o", color ="b")

plt.xlabel("Year")
plt.ylabel("GDP (in billion U.S. dollars)")
plt.title("Gross domestic product (GDP) in current prices in South Africa 1980-2031")
mplcursors.cursor(sc, hover=True)

plt.show()
