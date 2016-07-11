import numpy as np
import pandas as pd
import requests
import re
import datetime
from bs4 import BeautifulSoup as bs4
from time import sleep

min_price = 3000
max_price = 16000
min_miles = 5000
max_miles = 80000
min_auto_year = 2008
#locations = ['sfbay','seattle','sandiego','lasvegas','portland','losangeles','chicago','newyork','cleveland','austin','detroit','denver','houston','dallas','sanantonio','miami','orlando','philadelphia','phoenix','indianapolis','atlanta','buffalo','cincinati','delaware','elpaso','fresno','iowa','ithaca','laredo','madison','memphis','merced','modesto','moterey','santacruz','montgomery','nashville','nh','neworleans','oaklahomacity','orangecounty','palmsprings','pittsburgh','pueblo','redding','reno','salem','saltlakecity','sandiego','slo','santabarbara','santamaria']
#locations = ['orangecounty','palmsprings','pittsburgh','pueblo','redding','reno','salem','saltlakecity','sandiego','slo','santabarbara','santamaria']
locations = ['sfbay']

models = ['outback','forester','impreza']


def find_prices(results):
    prices = []
    for rw in results:
        price = rw.find('span', {'class': 'price'})
        if price is not None:
            price = float(price.text.strip('$'))
        else:
            price = np.nan
        prices.append(price)
    return prices

def find_times(results):
    times = []
    for rw in results:
        if time is not None:
            time = time['datetime']
            time = pd.to_datetime(time)
        else:
            time = np.nan
        times.append(time)
    return times

def get_db_number(links):
    db_number = []
    for rw in links:
        tempnumber=re.findall("/(\d+).html",rw)
        db_number.append(int(tempnumber[0]))
    return db_number

def get_real_link(links,loc):
    real_link = []
    for i in xrange(len(links)):
        if(links[i][1] == '/'):
            real_link.append("http:"+links[i])
        else:
            real_link.append("http://"+loc+".craigslist.org"+links[i])
    return real_link            
        

#params = dict(hasPic=1, auto_make_model="subaru",min_price=3000,max_price=20000,min_auto_year=2005,auto_title_status=1,min_auto_miles=5000,max_auto_miles=100000)
#loc_prefixes = ['eby', 'nby', 'sfc', 'sby', 'scz', 'pen']



recorded_cars=[]

with open('subarus.csv') as f:
    lines = f.readlines()
    for line in lines:
        temp_recorded_car=re.findall("db:(\d+):db",line)
        recorded_car=int(temp_recorded_car[0])
        recorded_cars.append(recorded_car)
f.close()

# loc_prefixes = ['eby'] # NOT USED


file_ = open('subarus.csv', 'a')

results = []  
# Careful with this...too many queries == your IP gets banned temporarily
search_indices = np.arange(0, 100, 100)
for loc in locations:
    for model in models:
        for i in search_indices:
            #url = 'http://sfbay.craigslist.org/search/{0}/cto'.format(loc)
            url = 'http://'+loc+'.craigslist.org/search/cto'
            resp = requests.get(url, params={'hasPic':1, 'auto_make_model':'subaru'+'+'+model,'min_price':min_price,'max_price':max_price,'min_auto_year':min_auto_year,'auto_title_status':1,'min_auto_miles':min_miles,'max_auto_miles':max_miles, 's': i})
            txt = bs4(resp.text, 'html.parser')
            cars = txt.findAll(attrs={'class': "row"})
            print model, ", found:", len(cars)
            # # Find the size of all entries
            # size_text = [rw.findAll(attrs={'class': 'housing'})[0].text
            #              for rw in apts]
            # sizes_brs = [find_size_and_brs(stxt) for stxt in size_text]
            # sizes, n_brs = zip(*sizes_brs)  # This unzips into 2 vectors
         
            # Find the title and link
            title = [rw.find('a', attrs={'class': 'hdrlnk'}).text
                          for rw in cars]
            links = [rw.find('a', attrs={'class': 'hdrlnk'})['href']
                     for rw in cars]
            
            # Find the time
            time = [pd.to_datetime(rw.find('time')['datetime']) for rw in cars]
            price = find_prices(cars)
            #times = find_times(cars)
            db_numbers = get_db_number(links)
            real_links = get_real_link(links,loc)
            # print price
            # print links
            # print title
            # print time
            #print recorded_cars
            
            
            #SaveCars to text    
            for j in xrange(len(db_numbers)):
                if(db_numbers[j] not in recorded_cars):
                    #print real_links[j]
                    resp = requests.get(real_links[j])
                    html = bs4(resp.text, 'html.parser')
                    carattributes = html.find_all('p', attrs={'class': 'attrgroup'})
                    
                    yearlist = re.findall("<p class=\"attrgroup\"><span><b>(\d+)",str(carattributes))
                    if yearlist == []:
                        year = "unknown"
                    else:    
                        year = int(yearlist[0])
                    
                    odolist = re.findall("odometer: <b>(\d+)</b>",str(carattributes))
                    if odolist == []:
                        odo = 200.
                    else:    
                        odo = float(odolist[0])/1000 
                    
                    translist = re.findall("transmission: <b>(\w+)</b>",str(carattributes))
                    if translist == []:
                        trans = "unknown"
                    else:
                        trans = translist[0]
                    condlist = re.findall("condition: <b>(\w+)</b>",str(carattributes))
                    if condlist == []:
                        cond = "unknown"
                    else:
                        cond = condlist[0]
                    statuslist = re.findall("title status: <b>(\w+)</b>",str(carattributes))
                    if statuslist == []:
                        status = "unknown"
                    else:
                        status = statuslist[0]
                    
                    print loc, year, model, "$%.3f" % round(price[j]/1000,3), "%.3f" % round(odo,3)
                    file_.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")+", "+"%.3f" % round(price[j]/1000,3)+", "+"%.3f" % round(odo,3)+", "+str(year)+", "+model+", "+loc+", "+trans+", "+cond+", "+status+", "+title[j].replace(",", "-")+", "+time[j].to_datetime().strftime("%Y-%m-%d %H:%M")+", "+real_links[j]+", db:"+str(db_numbers[j])+":db \n")
            

file_.close()




# url_base = 'http://sfbay.craigslist.org/search/cto'
# 
# params = dict(hasPic=1, auto_make_model="subaru",min_price=3000,max_price=20000,min_auto_year=2005,auto_title_status=1,min_auto_miles=5000,max_auto_miles=100000)
# rsp = requests.get(url_base, params=params)
# 
# print(rsp.url)
# 
# print(rsp.text[:500])
# 
# 
# from bs4 import BeautifulSoup as bs4
# 
# # BS4 can quickly parse our text, make sure to tell it that you're giving html
# html = bs4(rsp.text, 'html.parser')
# 
# # BS makes it easy to look through a document
# print(html.prettify()[:1000])
# 
# # find_all will pull entries that fit your search criteria.
# # Note that we have to use brackets to define the `attrs` dictionary
# # Because "class" is a special word in python, so we need to give a string.
# cars = html.find_all('p', attrs={'class': 'row'})
# carprices = html.find_all('p',attrs={'class':''})
# print(len(cars))
# 
# 
# # We can see that there's a consistent structure to a listing.
# # There is a 'time', a 'name', etc.
# this_car = cars[15]
# print(this_car.prettify())
