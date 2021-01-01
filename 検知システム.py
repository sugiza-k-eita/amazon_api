# 事前準備
# ①　pip install amightygirl.paapi5-python-sdk
# ②　amazonAPIを取得し、ACCECESKEYとSecretKey、Partner Tagを取得してください

from amazon.paapi import AmazonAPI
from time import sleep

ACCECES_KEY    = ""
#取得したAccess Key を代入してください
SECRET_KEY = ""
#取得したSecret Key を代入してください
TAG = ""
#取得したPartner Tag　を代入してください
COUNTRRY = "JP"

amazon = AmazonAPI(KEY, SECRET, TAG, COUNTRY)


product = amazon.get_product("")
#（）の中にはASIN名を代入
print(product.title)
count = 0        
while True:
    product = amazon.get_product("")
    #（）の中にはASIN名を代入
    print(product.titl
    if len(product) == 0:
        print("no switch found 404")
    else:
        print("検知しました")
        count =+ 1
        break

