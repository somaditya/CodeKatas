import requests
from lxml import html
from bs4 import BeautifulSoup

url = 'https://mvnrepository.com/artifact/com.amazonaws/aws-java-sdk-applicationautoscaling/1.11.188'

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

for textarea in soup.findAll("textarea", id ="gradle-a"):
    print(textarea.text.split("\n")[2])