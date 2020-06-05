import requests
import time
import os
import json

os.environ['no_proxy'] = '*' 

url='http://localhost:3000'

proxies = {
  "http": None,
  "https": None,
}

# ここをコメントアウトすると、データをクリアできる
# response = requests.post(url + '/delVentilation',proxies=proxies)
# print("del {}:{}".format(response.status_code,response.text))

for i in range(5):
    param={'temperature':str(25+i), 'humidity':str(30+i),'numOfpeople':str(10+i)}
    response = requests.post(url + '/addVentilation' , data=param,proxies=proxies)
    print("add[{}] {}:{}".format(i,response.status_code,response.text))
    time.sleep(2)


url='http://localhost:3000/getVentilation/10'
response = requests.get(url,proxies=proxies)
print("show {}:{}".format(response.status_code,response.text))
