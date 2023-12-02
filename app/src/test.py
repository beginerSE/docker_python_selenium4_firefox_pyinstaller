import os
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import selenium

print("seleniumのバージョン",selenium.__version__)
from selenium.webdriver.firefox.options import Options as FirefoxOptions
options = FirefoxOptions()
cloud_options = {}
cloud_options['build'] = "build_1"
cloud_options['name'] = "test_abc"
options.set_capability('cloud:options', cloud_options)


download_dir = "/app/src/"  # Dockerコンテナ内のパスに注意
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir", download_dir)
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/zip")  # 例: PDFファイル
# options.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv") 
# options.headless = True  # ヘッドレスモードの有効化 (必要に応じて)

driver = webdriver.Remote(
    command_executor=os.environ["SELENIUM_URL"],
    options=options
)
driver.implicitly_wait(5)

# ここからコーディング

# driver.get("https://www.time-j.net/worldtime/country/jp")
# print(driver.find_element(By.XPATH, "/html/body/div/div[6]/div[1]/div/p[5]").text)

driver.get("https://github.com/beginerSE/docker_python_selenium_test")

import time
time.sleep(5)
element = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/main/turbo-frame/div/div/div/div[2]/div[1]/div[1]/span[1]/get-repo/details/summary/span[1]/span")
element.click()
time.sleep(5)
element = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/main/turbo-frame/div/div/div/div[2]/div[1]/div[1]/span[1]/get-repo/details/div/div/div[1]/tab-container/div[2]/ul/li[2]/a")
element.click()
time.sleep(5)
driver.quit()


# docker run -d -v /tempDownload:/home/seluser/Downloads -p 4444:4444 -p 5900:5900 docker_python_selenium_test-main-app
