import requests

res = requests.get("https://zipcloud.ibsnet.co.jp/api/search?zipcode=0294102")

# print(res.text["status"])
json = res.json()
result01 = json["results"](0)
print(res.json()["results"][0]["address1"])
print(res.json()["results"][0]["address2"])
print(res.json()["results"][0]["address3"])
print(res.json()["results"][0]["prefcode"])
