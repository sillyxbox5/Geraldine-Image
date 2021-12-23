
print("Welcome to Geraldine-Image Beta")
output_url='output_url'
import requests
r = requests.post(
    "https://api.deepai.org/api/text2img",
    data={
        'text': input("What text do you want to turn into an image: "),
    },
    headers={'api-key': 'f3799613-ba06-4076-b6f3-198a787f5d7b'}
)
link=r.json()
link=link[output_url]
import urllib.request
urllib.request.urlretrieve(link, "output.jpg")
#print(link)
print("Done, Check output.jpg")
