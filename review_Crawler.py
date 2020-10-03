from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv
import os

def crawl(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument(
      "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36")

    driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)

    review_all = []
    rank_all = []

    driver.get(url)
    time.sleep(1)

    count_elem = driver.find_element_by_class_name('count')
    if count_elem.text == "":
        return
    count_elem.click()

    print(driver.find_element_by_class_name('prod-buy-header__title').text, end="")

    for i in range(1, 11):
        time.sleep(1)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        review = soup.select('div.sdp-review__article__list__review__content')
        ranks = soup.select('div.sdp-review__article__list__info__product-info__star-orange')


        if len(review) != len(ranks):
            break

        for elem in review:
            review_all.append(elem.text)
        for elem in ranks:
            rank_all.append(elem['data-rating'])

        paging = soup.select('button.sdp-review__article__page__num')

        if len(paging) <= i:
            break

        driver.find_element_by_xpath('/html/body/div[1]/section/div[2]/div[10]/ul[2]/'
                                     'li[2]/div/div[5]/section[4]/div[3]/button[%d]' %(i + 2)).click()
    print(" : ", str(len(review_all)), "개")
    driver.close()
    return review_all, rank_all


def csv_write(pid, review_all, rank_all):
    filename = str(pid) + '_result.csv'

    if os.path.isfile(filename):
        print("file already exists")
    else:
        with open(filename, 'w', newline='') as f:
            makewrite = csv.writer(f)
            makewrite.writerow(["productID", "review", "rank"])
            for review, rank in zip(review_all, rank_all):
                makewrite.writerow([pid, review, rank])