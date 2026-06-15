import matplotlib.pyplot as plt
import numpy as np
products=['running shoes','smart watches','leather bags']
daraz_prices=[5000,15000,8000]
olx_prices=[4500,12000,7500]

x=np.arange(len(products))
width=0.35

plt.bar(x-width/2,daraz_prices,width,label='Daraz',color='blue')
plt.bar(x+width/2,olx_prices,width,label='OLX',color='orange')
plt.xlabel('Products')
plt.ylabel('Prices')
plt.title('Product Prices on Daraz and OLX')
plt.legend()
plt.show()
