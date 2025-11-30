# print(100)
import requests
print(requests)
class a:
    pass
xyz=a()
print(xyz)    

data=requests.get("https://fakestoreapi.com/products")
print(data.status_code)
# print(data.text)
fetchedData=data.json()
for i in fetchedData:
    print(i)
# requests.post()
# requests.put()
# requests.delete()

# requests to make http requests 
# post :-- post req :-- requests
# get
# update
# delete