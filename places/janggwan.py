#AJAX로 처리되는 동적인 데이타 selenium으로 가져오기
#BeautifulSoup만으로는 스크래핑 불가능
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class JangGwan:
    def start_requests(self,lat,lng):
        try:
            # Headless Browser를 위한 옵션 설정
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            options.add_argument('window-size=1920x1080')
            options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')

            # 크롬드라이버(chromedriver.exe)가 위치한 경로(절대 경로)
            driverPath = '{}\chromedriver.exe'.format(os.path.dirname(os.path.realpath(__file__)))
            driver = webdriver.Chrome(driverPath)
            #driver = webdriver.Chrome(driverPath,options=options)
            #2. WebDriver객체의 get메소드로 특정 사이트를 브라우저에 로딩(자동으로 크롬브라우저 실행)
            driver.get('https://www.google.co.kr/maps')

            search = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchboxinput"]')))
            search.send_keys("관광명소")
            searchBtn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="searchbox-searchbutton"]')))
            searchBtn.click()
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]/div')))
            gwanGwang = []
            #관광명소 정보
            #names = driver.find_elements_by_xpath('')

        except TimeoutException as e:
            print('해당 페이지에 태그 요소가 존재하지 않거나,해당 페이지가 시간 내에 열리지 않았어요:',e)