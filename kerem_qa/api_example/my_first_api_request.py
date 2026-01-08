
import requests
base_url = "https://petstore.swagger.io/v2"
url = "/pet/findByStatus?status=available"
exp_id = 1767855217000

response = requests.get(base_url + url)
print (response.status_code)
response.headers   # show the headers of the response
response_as_json = response.json()   # show the response as json object
response.text # show the response as string
l = len(response_as_json)

for i in range (l):
    id = response_as_json[i]["id"]
    if id == exp_id:
        print ("%%%%%%%%%%%%%%%%%%%%%%%%%")
        category = response_as_json[i]["category"]
        category_name  = category["name"]
        print (f"category name is {category_name}")
        print (response_as_json[i]["name"])

    print (id)
print ("##### test end ######")

