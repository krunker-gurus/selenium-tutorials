from selenium import webdriver
from selenium.webdriver.common.proxy import ProxyType, Proxy #proxy module
import time

proxy_ip = 'proxy:port' #get a free proxy from the websites in the description

#setting up proxy
proxy =Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = proxy_ip
proxy.ssl_proxy = proxy_ip

#linking proxy and setting up driver
capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)
driver = webdriver.Chrome('CHROMEDRIVER PATH', desired_capabilities=capabilities) # replace the chromedriver path

#loading test page
driver.get('https://httpbin.org/ip')
time.sleep(8)
driver.quit()
