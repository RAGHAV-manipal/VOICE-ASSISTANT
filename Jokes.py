import requests
#from ss import *

#Key = "6acf75890e814474b7a3b349419b9388"

url = "https://official-joke-api.appspot.com/random_joke"
json_data = requests.get(url).json()

ar =["",""]
'''def news():
    for i in range(3):
        ar.append("Number "+str(i+1)+", " + json_data["articles"][i]["title"]+ ".")

    return ar'''
'''arr = news()
print(arr)'''
ar[0] = json_data["setup"]
ar[1] = json_data["punchline"]
def joke():
    return ar
