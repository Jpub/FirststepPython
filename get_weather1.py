import requests
import xml.etree.ElementTree as ET
api_url = 'http://web.kma.go.kr/wid/queryDFSRSS.jsp?zone=1159068000'
weather_data = requests.get(api_url).content
xml_data = ET.fromstring(weather_data)
for tag in xml_data.iter("data"):
print (tag.find("hour").text + "/" + tag.find("temp").text 
