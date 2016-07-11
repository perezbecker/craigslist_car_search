
# import pandas
# colnames = [data'price', 'miles', 'model', 'location', 'transmission','condition','title','postdate','link','db']
# data = pandas.read_csv('subarus.csv', delimiter=',', names=colnames)
# 
# prices = data.price.tolist()
# miles = data.miles.tolist()
# models = data.model.tolist()
# locations = data.location.tolist()
# postdates = data.postdate.tolist()



import csv
import datetime
import matplotlib.pyplot as plt
import pylab
import numpy


#yeardict={' 2005':50,' 2006':100,' 2007':300,' 2008':500,' 2009':700,' 2010':900,' 2011':1100,' 2012':1300,' 2013':1500,' 2014':1700,' 2015':1900,' 2016':2100,' 2017':2300}
yeardict={' 2005':10,' 2006':10,' 2007':10,' 2008':50,' 2009':100,' 2010':300,' 2011':600,' 2012':1000,' 2013':1500,' 2014':2000,' 2015':2500,' 2016':3000,' 2017':3500}




with open('subarus.csv', 'rb') as f:
    reader = csv.reader(f)
    sudata = list(reader)
f.close()


prices=[]
miles=[]
models=[]
locations=[]
postdates=[]
years=[]




for i in xrange(len(sudata)):
    prices.append(sudata[i][1])
    miles.append(sudata[i][2])
    years.append(sudata[i][3])
    models.append(sudata[i][4])
    locations.append(sudata[i][5])
    postdates.append((datetime.datetime.now()-datetime.datetime.strptime(sudata[i][10]," %Y-%m-%d %H:%M")).days)


sf_outback_prices=[]
sf_outback_miles=[]
sf_outback_years=[]
for i in xrange(len(prices)):
    if(locations[i]==' sfbay' and models[i]==' outback' and postdates[i] > 2):
        sf_outback_prices.append(prices[i])
        sf_outback_miles.append(miles[i])
        sf_outback_years.append(yeardict[years[i]])

sf_forester_prices=[]
sf_forester_miles=[]
sf_forester_years=[]
for i in xrange(len(prices)):
    if(locations[i]==' sfbay' and models[i]==' forester' and postdates[i] > 2):
        sf_forester_prices.append(prices[i])
        sf_forester_miles.append(miles[i])
        sf_forester_years.append(yeardict[years[i]])

sf_impreza_prices=[]
sf_impreza_miles=[]
sf_impreza_years=[]
for i in xrange(len(prices)):
    if(locations[i]==' sfbay' and models[i]==' impreza' and postdates[i] > 2):
        sf_impreza_prices.append(prices[i])
        sf_impreza_miles.append(miles[i])
        sf_impreza_years.append(yeardict[years[i]])
        

bos_outback_prices=[]
bos_outback_miles=[]
bos_outback_years=[]
for i in xrange(len(prices)):
    if(locations[i] !=' sfbay' and models[i]==' outback'):
        bos_outback_prices.append(prices[i])
        bos_outback_miles.append(miles[i])
        bos_outback_years.append(yeardict[years[i]])

bos_forester_prices=[]
bos_forester_miles=[]
bos_forester_years=[]
for i in xrange(len(prices)):
    if(locations[i] !=' sfbay' and models[i]==' forester'):
        bos_forester_prices.append(prices[i])
        bos_forester_miles.append(miles[i])
        bos_forester_years.append(yeardict[years[i]])

bos_impreza_prices=[]
bos_impreza_miles=[]
bos_impreza_years=[]
for i in xrange(len(prices)):
    if(locations[i] !=' sfbay' and models[i]==' impreza'):
        bos_impreza_prices.append(prices[i])
        bos_impreza_miles.append(miles[i])
        bos_impreza_years.append(yeardict[years[i]])


new_sf_outback_prices=[]
new_sf_outback_miles=[]
new_sf_outback_years=[]
for i in xrange(len(prices)):
    if(locations[i]==' sfbay' and models[i]==' outback' and postdates[i] <= 2):
        new_sf_outback_prices.append(prices[i])
        new_sf_outback_miles.append(miles[i])
        new_sf_outback_years.append(yeardict[years[i]])

new_sf_forester_prices=[]
new_sf_forester_miles=[]
new_sf_forester_years=[]
for i in xrange(len(prices)):
    if(locations[i]==' sfbay' and models[i]==' forester' and postdates[i] <= 2):
        new_sf_forester_prices.append(prices[i])
        new_sf_forester_miles.append(miles[i])
        new_sf_forester_years.append(yeardict[years[i]])

new_sf_impreza_prices=[]
new_sf_impreza_miles=[]
new_sf_impreza_years=[]
for i in xrange(len(prices)):
    if(locations[i]==' sfbay' and models[i]==' impreza' and postdates[i] <= 2):
        new_sf_impreza_prices.append(prices[i])
        new_sf_impreza_miles.append(miles[i])
        new_sf_impreza_years.append(yeardict[years[i]])


# f, axarr = plt.subplots(3, sharex=True)
# axarr[0].scatter(sf_outback_prices, sf_outback_miles, s=sf_outback_years, marker="o", facecolors='none', edgecolors='b', label='SF Outback')
# axarr[0].scatter(bos_outback_prices, bos_outback_miles, s=bos_outback_years, marker="o",facecolors='none', edgecolors='g', label='US Outback')
# axarr[0].scatter(new_sf_outback_prices, new_sf_outback_miles, s=new_sf_outback_years, marker="o", facecolors='none', edgecolors='r', label='NEW SF Outback')
# axarr[0].set_title('Sharing X axis')
# #axarr[0].set_xticks(numpy.arange(2,20,1))
# axarr[0].set_yticks(numpy.arange(0,100,10))
# axarr[0].grid()
# 
# 
# axarr[1].scatter(sf_forester_prices, sf_forester_miles, s=sf_forester_years, c='b', marker="x", label='SF Forester')
# axarr[1].scatter(bos_forester_prices, bos_forester_miles, s=bos_forester_years, c='g', marker="x", label='US Forester')
# axarr[1].scatter(new_sf_forester_prices, new_sf_forester_miles, s=new_sf_forester_years, c='r', marker="x", label='NEW SF Forester')
# axarr[1].set_xticks(numpy.arange(2,20,1))
# axarr[1].set_yticks(numpy.arange(0,100,10))
# axarr[1].grid()
# 
# axarr[2].scatter(sf_impreza_prices, sf_impreza_miles, s=sf_impreza_years, c='b', marker="+", label='SF Impreza')
# axarr[2].scatter(bos_impreza_prices, bos_impreza_miles, s=bos_impreza_years, c='g', marker="+", label='US Impreza')
# axarr[2].scatter(new_sf_impreza_prices, new_sf_impreza_miles, s=new_sf_impreza_years, c='r', marker="+", label='NEW SF Impreza')
# axarr[2].grid()

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(sf_outback_prices, sf_outback_miles, s=sf_outback_years, marker="o", facecolors='none', edgecolors='b', label='SF Outback')
ax1.scatter(sf_forester_prices, sf_forester_miles, s=sf_forester_years, c='b', marker="x", label='SF Forester')
ax1.scatter(sf_impreza_prices, sf_impreza_miles, s=sf_impreza_years, c='b', marker="+", label='SF Impreza')
ax1.scatter(bos_outback_prices, bos_outback_miles, s=bos_outback_years, marker="o",facecolors='none', edgecolors='g', label='US Outback')
ax1.scatter(bos_forester_prices, bos_forester_miles, s=bos_forester_years, c='g', marker="x", label='US Forester')
ax1.scatter(bos_impreza_prices, bos_impreza_miles, s=bos_impreza_years, c='g', marker="+", label='US Impreza')
ax1.scatter(new_sf_outback_prices, new_sf_outback_miles, s=new_sf_outback_years, marker="o", facecolors='none', edgecolors='r', label='NEW SF Outback')
ax1.scatter(new_sf_forester_prices, new_sf_forester_miles, s=new_sf_forester_years, c='r', marker="x", label='NEW SF Forester')
ax1.scatter(new_sf_impreza_prices, new_sf_impreza_miles, s=new_sf_impreza_years, c='r', marker="+", label='NEW SF Impreza')
# ax1.legend(loc='upper right')


ax1.set_xticks(numpy.arange(5,18,1))
ax1.set_yticks(numpy.arange(0,100,10))


plt.xlabel('Price (k-$)')
plt.ylabel('Mileage (k-miles)')
plt.grid()
plt.show()



