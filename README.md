# :camera:Project_Python_InstagramMacro

Python 기반의 Selenium(feat:Chrome Driver)을 사용하여 인스타그램에 로그인하고, 원하는 해시태그로 피드를 검색한 후 피드별로 좋아요를 클릭하고 댓글 등록을 반복하는 매크로 프로그램

## :heavy_check_mark:Developer Environment

  - Language: [:crocodile:Python 3.7]
  - IDE Tool: [:computer:Pycharm]
  - Package Manager: [:snake:Anaconda]
  - Using Package: [requests, selenium, beautifulsoup4, time, random]
  - Using WebDriver: ChromeDriver(use the same version as the Chrome browser version you use)
  
## :floppy_disk:Repository structure description
### 1.practice
  - [chapter01_crawl](https://github.com/smskit726/Project_Python_InstagramMacro/blob/master/practice/chapter01_crawl.py)
  - [chapter02_webdriver](https://github.com/smskit726/Project_Python_InstagramMacro/blob/master/practice/chapter02_webdriver.py)
  - [chapter03_selenium_crawl](https://github.com/smskit726/Project_Python_InstagramMacro/blob/master/practice/chapter03_selenium_crawl.py)
  - [chapter04_facebook_login](https://github.com/smskit726/Project_Python_InstagramMacro/blob/master/practice/chapter04_facebook_login.py)

### 2.libs
  - [crawler](https://github.com/smskit726/Project_Python_InstagramMacro/blob/master/libs/crawler.py)

### 3.instagram
  - [hashtag_reply_macro](https://github.com/smskit726/Project_Python_InstagramMacro/blob/master/instagram/hashtag_reply_macro.py)  

## :speech_balloon:How to use?

1. Download : [Chrome Driver](https://chromedriver.chromium.org/downloads) same as Chrome browser version
2. settings : set the some elements on hashtag_reply_macro in instagram Project
  - path : set the path Chrome Driver
