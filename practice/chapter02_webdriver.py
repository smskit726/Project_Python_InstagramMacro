# * chapter02.webdriver.py
# * : Selenium의 webdriver 사용방법(*Chrome Driver)
# *

from selenium import webdriver

# instagram 페이지에서 원하는 해시태그로 selenium 접속(*크롬 드라이버)
driver = webdriver.Chrome(executable_path='../webdriver/chromedriver.exe')

# https://www.instagram.com/explore/tags/피규어/
# URL 주소의 한글은 유니코드로 변환(한글이면 깨지는 경우가 있음)
url = 'https://www.instagram.com/explore/tags/%ED%94%BC%EA%B7%9C%EC%96%B4/'
driver.get(url)

# 실행 후 브라우저 종료
# driver.close()