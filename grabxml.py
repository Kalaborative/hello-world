import requests

f = requests.get("http://www.w3schools.com/xml/cd_catalog.xml")

with open("cdfile.xml", "wb") as code:
	code.write(f.content)

code.close()