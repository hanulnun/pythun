from bs4 import BeautifulSoup
from urllib import request
import telegram

url = "http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=2778024489"
req = request.urlopen(url)
res = req.read()

soup = BeautifulSoup(res, 'html.parser')
keywords = soup.find_all('p', class_='info_guide')
keywords2 = soup.find_all('strong', class_='sale_price')
print(keywords)
print(keywords2)