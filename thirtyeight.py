import matplotlib.pyplot as plt
products     = ['USB-C Hub', 'Mechanical KB', 'Webcam HD', 'Monitor 24in', 'Headphones']
daraz_prices = [3500, 9500, 5800, 42000, 12860]
olx_prices   = [2800, 8900, 6200, 38000, 13975]
plt.figure(figsize=(10,6))
x=range(len(products))
plt.bar(x,daraz_prices, width=0.4,label='Daraz',color='blue')
plt.bar([i+0.4 for i in x],olx_prices, width=0.4,label='OLX',color='orange')
plt.xticks([i+0.2 for i in x],products,rotation=45)
plt.xlabel('Products')
plt.ylabel('price')
plt.title('price comparison:DARAZ vs OLX')
plt.legend()
plt.show()
