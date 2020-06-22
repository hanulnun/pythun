from bs4 import BeautifulSoup
from urllib import request
import telegram

# url = "http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=2778024489"
# req = request.urlopen(url)
# res = req.read()
#
# soup = BeautifulSoup(res, 'html.parser')
# keywords = soup.find_all('p', class_='info_guide')
# keywords2 = soup.find_all('strong', class_='sale_price')
# print(keywords)
# print(keywords2)
#
# url2 = "http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=2827952509"
# req = request.urlopen(url2)
# res = req.read()
#
# soup = BeautifulSoup(res, 'html.parser')
# keywords = soup.find_all('p', class_='info_guide')
# keywords2 = soup.find_all('strong', class_='sale_price')
# print(keywords)
# print(keywords2)

#티몬 페이코 상품권(매달 바뀌는걸지도..)
#http://www.tmon.co.kr/deal/3665422650(6월)
#http://www.tmon.co.kr/deal/3580303486(5월)

telegram_token = '1206664250:AAFiDuoarJacXgn5NNZ_5N8Q9YyFv0sE5vE'
bot = telegram.Bot(token=telegram_token)
#8427228
bot.sendMessage(chat_id='8427228', text="http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=2778024489")


