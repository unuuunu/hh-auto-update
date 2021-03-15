from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

SERVICE_LOG_PATH = r'../Log/geckodriver.log'
HH_URL = r'https://hh.ru/'


def main():
    config = {
        'executable_path': GeckoDriverManager().install(),
        'service_log_path': SERVICE_LOG_PATH,
    }
    with webdriver.Firefox(**config) as driver:
        driver.get(HH_URL)
        print(driver.current_url)


if __name__ == '__main__':
    main()
