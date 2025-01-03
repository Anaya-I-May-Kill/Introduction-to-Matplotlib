import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

train = pd.read_csv("company_sales_data.csv")

print(train)

profitList = train ['total_profit'].tolist()
monthList = train ['month_number'].tolist()

plt.plot(monthList , profitList , label = 'Profit data of last year',
         color = 'r' , marker = 'o' , markerfacecolor = 'k',
         linestyle = '--' , linewidth = 3)

plt.xlabel('Month Number')
plt.ylabel('Profit in dollar')
plt.legend(loc = 'lower right')
plt.title('Company Sales data of last year')
plt.xticks(monthList)
plt.yticks([100000 , 200000 , 300000 , 400000 , 500000])
plt.show()