from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import csv
import os

file = open(r'C:\Users\Varun\Desktop\Project\web-parsing\places.csv','w')
fields = ['Placename','City','State','Country','Weather','Time required','Entry fee','Timings','URL']

csv.register_dialect('MyDialect',lineterminator = '\n')

writer = csv.writer(file,dialect='MyDialect')

writer.writerow(fields)

URL = r'C:\My Web Sites\holidify-website\www.holidify.com\places\agra'

for file_name in os.listdir(URL):
    file_path = os.path.join(URL,file_name)
    if not os.path.isfile(file_path):
        break
    
    with open(file_path,'r') as html_file:
        html_content = html_file.readline()



# driver = webdriver.Chrome()
# driver.get(URL)

# try:
#     element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "currentWeather")))
#     weather = element.text
#     # print(weather)
# finally:
    
#     driver.quit()


# html_content = driver.page_source

    soup = BeautifulSoup(html_content,'lxml')
    # soup.prettify()
    # print(soup)

    container = soup.find('div',{'class':'row no-gutters destination-atf negative-margin-mobile mb-30'})
    print(container)

    place = container.find('h1').text.rstrip()
    # print(place)

    city_details = container.find('div',{'class':'mb-2 font-smaller'}).find_all('a')

    city = city_details[0].text.rstrip()
    state = city_details[1].text.rstrip()
    country = city_details[2].text.rstrip()

    # print(city, state, country)

    other_details = container.find('div',{'class':'flex-column'}).find_all('div',{'class':'col-12'})
    # print(other_details)

    # weather = element.text
    # print(weather)
    weather = other_details[0].text.rstrip()

    time_req = other_details[1].text.split(':')[1].rstrip()
    # print(time_req)
    entry_fee = other_details[2].text.split(':')[1].rstrip()
    # print(entry_fee)
    timings = other_details[3].text.split(':')[1].rstrip()
    # print(timings)

    # print(URL)
    data = []
    data.extend([place, city, state, country, weather, time_req,entry_fee,timings,URL])
    # print(data)


    writer.writerow(fields)
    writer.writerow(data)


file.close()