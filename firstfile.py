from bs4 import BeautifulSoup
import requests
import re
import csv


source = requests.get('https://whattomine.com/coins?aq_380=0&aq_fury=0&aq_470=0&aq_480=1&aq_570=0&aq_580=0&aq_vega56=0&aq_vega64=0&aq_5600xt=0&aq_5700=0&aq_5700xt=0&aq_vii=0&aq_68=0&aq_68xt=0&aq_1050Ti=0&aq_10606=0&aq_1070=0&aq_1070Ti=0&aq_1080=0&aq_1080Ti=0&aq_1660=0&aq_1660Ti=0&aq_166s=0&aq_2060=0&aq_2070=0&aq_2080=0&aq_2080Ti=1&a_2080Ti=true&aq_3060Ti=0&aq_3070=0&aq_3080=0&aq_3090=0&eth=true&factor%5Beth_hr%5D=55.2&factor%5Beth_p%5D=180.0&e4g=true&factor%5Be4g_hr%5D=55.2&factor%5Be4g_p%5D=180.0&zh=true&factor%5Bzh_hr%5D=100.0&factor%5Bzh_p%5D=220.0&cnh=true&factor%5Bcnh_hr%5D=1450.0&factor%5Bcnh_p%5D=160.0&cng=true&factor%5Bcng_hr%5D=3100.0&factor%5Bcng_p%5D=220.0&cnr=true&factor%5Bcnr_hr%5D=1000.0&factor%5Bcnr_p%5D=190.0&cnf=true&factor%5Bcnf_hr%5D=2300.0&factor%5Bcnf_p%5D=160.0&eqa=true&factor%5Beqa_hr%5D=375.0&factor%5Beqa_p%5D=220.0&cc=true&factor%5Bcc_hr%5D=10.8&factor%5Bcc_p%5D=220.0&cr29=true&factor%5Bcr29_hr%5D=12.0&factor%5Bcr29_p%5D=220.0&cz29=true&factor%5Bcz29_hr%5D=6.8&factor%5Bcz29_p%5D=220.0&ct31=true&factor%5Bct31_hr%5D=2.45&factor%5Bct31_p%5D=220.0&ct32=true&factor%5Bct32_hr%5D=0.68&factor%5Bct32_p%5D=220.0&eqb=true&factor%5Beqb_hr%5D=37.8&factor%5Beqb_p%5D=220.0&rmx=true&factor%5Brmx_hr%5D=1380.0&factor%5Brmx_p%5D=190.0&ns=true&factor%5Bns_hr%5D=2800.0&factor%5Bns_p%5D=220.0&ops=true&factor%5Bops_hr%5D=58.5&factor%5Bops_p%5D=220.0&eqz=true&factor%5Beqz_hr%5D=56.5&factor%5Beqz_p%5D=220.0&zlh=true&factor%5Bzlh_hr%5D=72.0&factor%5Bzlh_p%5D=220.0&kpw=true&factor%5Bkpw_hr%5D=31.5&factor%5Bkpw_p%5D=220.0&ppw=true&factor%5Bppw_hr%5D=31.5&factor%5Bppw_p%5D=220.0&x25x=true&factor%5Bx25x_hr%5D=7.9&factor%5Bx25x_p%5D=220.0&mtp=true&factor%5Bmtp_hr%5D=4.6&factor%5Bmtp_p%5D=220.0&vh=true&factor%5Bvh_hr%5D=0.83&factor%5Bvh_p%5D=160.0&factor%5Bcost%5D=0.1&sort=Profitability24&volume=0&revenue=24h&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bitforex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=dove&factor%5Bexchanges%5D%5B%5D=exmo&factor%5Bexchanges%5D%5B%5D=gate&factor%5Bexchanges%5D%5B%5D=graviex&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=hotbit&factor%5Bexchanges%5D%5B%5D=ogre&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=stex&dataset=&commit=Calculate').text
soup = BeautifulSoup(source, 'lxml')
csvwriter = open("coins.csv", "w")
headers = 'COINS(excluding Nicehash) \n'
csvwriter.write(headers)
coinind = 0
for coin in soup.find_all('div', {'class':'ml-5'}):
    coinline = coin.a
    try:
        if coinline == 0:
            print('nicehash')
        else:
            csvwriter.write(coinline.text)
            if coinind == 0:
                csvwriter.write('(will earn the most)')
            coinind = coinind + 1
            csvwriter.write('\n')
    except AttributeError:
        pass



csvwriter.close()






