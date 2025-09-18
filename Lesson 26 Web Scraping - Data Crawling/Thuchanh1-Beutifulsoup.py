from bs4 import BeautifulSoup
import requests

# web mà chúng ta muốn lấy data - https://vnexpress.net/tong-bi-thu-viet-nam-chuyen-trang-thai-quoc-gia-vuon-len-4939631.html
url = 'https://vnexpress.net/tong-bi-thu-viet-nam-chuyen-trang-thai-quoc-gia-vuon-len-4939631.html'
reponse = requests.get(url)

# print(reponse.status_code) # 200 -> thành công
# print(reponse.text)

# dùng beutifulsoup để lấy data - cần phải xử lý HTML
soup = BeautifulSoup(reponse.text, 'html.parser') # lấy theo cấu trúc HTML

# # đi trích xuất và in ra 
# quote = soup.find_all('p', class_ = "Normal")
# for q in quote:
#     print(q.text)
#     break

# # đi trích xuất các chú thích
# notes = soup.find_all('p', class_="Image")
# for note in notes:
#     print(note.text)
