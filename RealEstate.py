import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Rent_Info.csv')
prices = data['Price']
prices = prices.str.replace('$', '').str.replace(',', '').str.strip()
prices = pd.to_numeric(prices)
data['Price'] = prices

vacancies = pd.read_csv('Rent_Info.csv')
pr = vacancies['Price']
pr = pr.str.replace('$', '').str.replace(',', '').str.strip()
pr = pd.to_numeric(pr)
vacancies['Price'] = pr
for x in vacancies.index:
    if vacancies.loc[x, 'vacancies'] == 0:
        vacancies.drop(x, inplace = True)

graph = data.plot()

average_rent = prices.mean()

lost_revenue = []
price_2 = data['Price']
vacancies_2 = data["vacancies"]


new_data = pd.read_csv('Rent_Info.csv')
new_data['Price'] = prices
new_data["lost_revenue"] = price_2 * vacancies_2