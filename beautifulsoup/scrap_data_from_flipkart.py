from bs4 import BeautifulSoup
soup = BeautifulSoup(open("Flipkart.html"),'html.parser')
flip = soup.find(attrs={"data-reactid": "67"})

items = {}

for a in flip.find_all('a'):
    #print a.get('href')
    #print a.get_text()
    items[a.get_text()] = a.get('href')

print items


