# !pip install bs4
# !pip install selenium
# !pip install googletrans

import review_Crawler as rc
import review_Translate as rt

url = "https://www.coupang.com/vp/products/1566808169?itemId=2679082613&vendorItemId=70669597878&sourceType=CATEGORY&categoryId=416032&isAddedCart="
pid = 12716256


review_all, rank_all = rc.crawl(url)
review_en = rt.preprocess(review_all)
rc.csv_write(pid, review_en, rank_all)
