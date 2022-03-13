from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import urllib3
import os
import time
import ssl

os.system("cls")

def ero(soup):
    title = soup.title.string
    title_delele = title.replace(' | Erofus - Sex and Porn Comics','')
    print("Comic Name : "+title_delele)
    for i in soup.findAll('div',class_='col-xs-12 col-sm-6 col-md-4 col-lg-2'):
        for j in i.find_all('div',class_='thumbnail'):
            for k in j.find_all('img'):
                link = k.get('src')
                link_delete = link.replace("/thumb/","")
                full_url = 'https://www.erofus.com/medium/'+link_delete
                f.write(full_url)
                f.write("\n")

def all(soup):
    title = soup.title.string
    for i in soup.findAll('img',{'class':'wp-manga-chapter-img img-responsive lazyload effect-fade'}):
        update_url = i.get('data-src')
        fix_url = update_url.replace('?ssl=1','')
        fix_url2 = fix_url.replace("\t","")
        final = fix_url2.replace("\n","")
        f.write(final)
        f.write("\n")

def hd(soup):
    for i in soup.findAll('div',class_='my-gallery scrollmenu pt-2'):
        for figure in i.find_all('a',href=True):
            f.write(figure.get('href'))
            f.write("\n")

def muses(soup):
    for i in soup.findAll('div',class_='gallery'):
        for a in i.find_all('img'):
            x = (a.get('data-src'))
            data = ('https://comics.8muses.com'+x)
            change_url = data.replace("/th/","/fm/")
            f.write(change_url)
            f.write("\n")
        

def xonline(soup):
    for j in soup.find_all(id='jig1'):
        for x in j.find_all(id='jig1-html'):
            for a in x.find_all('a'):
                f.write(a.get('href'))
                f.write("\n")

def egg(soup):
    for i in soup.findAll('div',class_='grid'):
        for j in i.find_all('img'):
            link = j.get('src')
            link_delete = link.replace('thumb300_','')
            f.write("https://eggporncomics.com"+link_delete)
            f.write("\n")

def xlecx(soup):
    for i in soup.findAll('div',class_='f-desc full-text clearfix'):
        for j in i.find_all('a',href=True):
            print(j.get('href'))
            f.write("\n")

def xyz(soup):
    for i in soup.findAll('div',class_='g1-content-narrow g1-typography-xl entry-content'):
        for j in i.find_all(id='jig1'):
            for x in j.find_all('a'):
                f.write(x.get('href'))
                f.write("\n")

def xxx(soup):
    for i in soup.findAll('div',class_='my-gallery'):
        for j in i.find_all('a',href=True):
            f.write(j.get('href'))
            f.write("\n")

def free(soup):
    for i in soup.findAll('div',{'class':'post-texto'}):
        for j in i.find_all('img'):
            f.write(j.get('src'))
            f.write("\n")

def nhentai(soup):
    title = soup.title.string
    title_delele = title.replace(' » nhentai: hentai doujinshi and manga',' ')
    print("Comic Name : "+title_delele)
    for i in soup.findAll('div',class_='thumbs'):
        for j in i.find_all('a',class_='gallerythumb'):
            for k in j.find_all('img','lazyload'):
                url_1 = k.get('data-src')
                url_2 = url_1.replace('https://t.','https://i.')
                url_3 = url_2.replace('t.jpg','.jpg')
                f.write(url_3)
                f.write("\n")

def manga(soup):    
	for i in soup.findAll('div',class_='col-md-12'):
		for j in i.find_all('div',class_='row portfolio-normal-width'):
			for k in j.find_all('div',class_='tac thumbs'):
				for l in k.find_all('figure'):
					for g in l.find_all('a'):
						f.write(g.get('href'))

def shikorina(soup):
    for i in soup.findAll('div',class_='content'):
        for j in i.find_all('ol',class_='add_imglist'):
            for k in j.find_all('li'):
                k.find('noscript').decompose()
                for l in k.find_all('img'):
                    result = l.get('data-src')
                    f.write('shikorina.net'+result)

def d3(soup):
    for i in soup.findAll("div",class_='thumbs'):
        for j in i.findAll("a"):
            f.write(j.get("data-img"))

def porncomixone(soup):
    for i in soup.findAll(id='unitegallery_2753_1'):
        for j in i.findAll("img"):  
            f.write(j.get("data-image"))

def asm(soup):
    for i in soup.findAll('div',class_='gallery'):
        for j in i.find_all('img'):
            j1 = j.get('data-src')
            j2 = j1.replace('//cimg','cimg')
            j3 = j2.replace('t.jpg','.jpg')
            f.write('https://'+j3)
            f.write("\n")   

def wozi(soup):
    for i in soup.findAll('div',class_='single-blog-content entry wpex-mt-20 wpex-mb-40 wpex-clr'):
        for j in i.find_all('img'):
            f.write(j.get('src'))
            f.write('\n')

def freecomics(soup):
    for i in soup.findAll(id='gallery-1'):
        for j in i.find_all('a'):
            f.write(j.get('href'))
            f.write('\n')

def cartoon18(soup):
    for i in soup.findAll('div',class_='fullwidth'):
        for ig in i.find_all('img'):
            f.write('www.cartoon18.com'+ig.get('data-src'))
            f.write('\n')
            
def comic_18(soup):
    for i in soup.findAll('div',class_='container'):
        for panel in i.find_all('div',class_='panel-body'):
            for content in panel.find_all('img',class_='lazy_img img-responsive-mw'):
                print(content.get('data-original'))

def doujins(soup):
    for i in soup.findAll(id='toggle-column'):
        for j in i.find_all('div',class_='swiper-zoom-container'):
            for thum in j.find_all('img',class_='swiper-lazy'):
                pure_url = thum.get('data-src')
                url_1 = pure_url.replace('amp;','')
                f.write(url_1)

def imhentai(soup):
    a = []
    # data url
    for i in soup.findAll(id='comments_div'):
        for j in i.find_all(id='append_thumbs'):
            for h in j.find_all('div',class_='gthumb'):
                for k in h.find_all('img',class_='lazy preloader'):
                    a.append(k.get('data-src'))
    # total pages
    for pages in soup.findAll('ul',class_='galleries_info'):
        for page in pages.find_all('li',class_='pages'):
            total_page = page.string
            total = int(total_page.replace('Pages: ',''))
            
    combine = a[1].replace('2t.jpg','')
    for x in range(1,total+1):
        f.write(f"{combine}{x}.jpg")

def hentaihere(soup):
    a = []
    # data url
    for i in soup.findAll('div',class_='col-xs-6 col-sm-3 col-md-2'):
        for j in i.find_all('div',class_='pos-rlt'):
            for thum in j.find_all('img',class_='arf-img-h3 arf-border-default'):
                pure_url = thum.get('src')
                url_1 = pure_url.replace('thumbnails/','')
                url_2 = url_1.replace('tmb.jpg','.jpg')
                a.append(url_2)
    # total pages
    for pages in soup.findAll('div',class_='wrapper-sm bg-black b-b'):
        for page in pages.find_all('li'):
            for li in page.find_all('a'):
                total_page = li.string
                if total_page is not None:
                    x1 = total_page.replace('pages]','')
                    x2 = x1.replace('[','')
                    total = int(x2)

    combine = a[0].replace('0001.jpg','')
    for x in range(1,total+1):
        f.write(f"{combine}{x:04d}.jpg")

def alternative():
    print("""
    Rules Alternative scraping
    this is alternative to get image url because 403
    1.You must find url of image 
    2.remove some format in link url like */*/1.jpg to */*/
    example : before = https://*/*/*/1.jpg
              after  = https://*/*/*/
    """)
    a             = str(input("URL       : "))
    page          = int(input("Pages     : "))
    print("""
    Format Number is how the link number goes : 
    1.x   = 1   for image
    2.xx  = 01  for image
    3.xxx = 001 for image
    4.x   = 1   for link
    """)
    format_number = int(input("option   : "))
    print("1.jpg | 2.png ")
    format_image  = int(input("format   : "))
    with open("url.csv","w") as f:
        f.write("pass\n")
        if format_number == 1 :
            for i in range(1,page+1):
                if format_image == 1:
                    result = a+f"{i:01d}.jpg\n"
                    f.write(result)
                elif format_number == 2:
                    result = a+f"{i:01d}.png\n"
                    f.write(result)
                else:
                    print("Error")
        elif format_number == 2:
            for i in range(1,page+1):
                if format_image == 1:
                    result = a+f"{i:02d}.jpg\n"
                    f.write(result)
                elif format_number == 2:
                    result = a+f"{i:02d}.png\n"
                    f.write(result)
                else:
                    print("Error")
        elif format_number == 3:
            for i in range(1,page+1):
                if format_image == 1:
                    result = a+f"{i:03d}.jpeg\n"
                    f.write(result)
                elif format_number == 2:
                    result = a+f"{i:03d}.png\n"
                    f.write(result)
                else:
                    print("Error")
        elif format_number == 4:
            for i in range(1,page+1):
                result = a+f"{i}\n"
                f.write(result)
# add def code using the name of function without ()
menu_code = ("""ero all hd muses xonline egg xlecx xyz xxx free nhentai 
manga shikorina d3 porncomixone asm wozi freecomics cartoon18 comic_18 doujins imhentai 
hentaihere
""").split()

if __name__ == "__main__":
    # like not complete
    print("""
====================================================================
|                          List Website                            |
====================================================================
| [1]  erofus               [11] nhentai          [21] doujins     |
| [2]  allporncomic (block) [12] xxxmangacomics   [22] ImHentai    |
| [3]  hdporncomic          [13] shikorina        [23] HentaiHere  |
| [4]  8muses               [14] porn3d           [24] Alternative |
| [5]  porncomixonline      [15] porncomixone     [25] Exit        |
| [6]  eggporncomics        [16] asmhentai                         |
| [7]  xlecx                [17] wozi                              |
| [8]  xyzcomics            [18] freeporncomics                    |
| [9]  xxx3dcomix           [19] cartoon18                         |
| [10] freeadultcomics      [20] 18comic                           |
====================================================================""")
    x = UserAgent()
    while True:
        command = int(input("> "))
        if command == len(menu_code)+2:
            print("Thank You For Using My Code")
            break
        elif command == len(menu_code)+1:
            alternative()
            break
        elif command >= len(menu_code)+3:
            exit()
        try:
            ssl._create_default_https_context = ssl._create_unverified_context
            link = str(input("URL : "))
            http = urllib3.PoolManager()
            head = {"User-Agent":x.random}
            response = http.request("GET",link,headers=head)
            soup = BeautifulSoup(response.data,"html.parser")
            if response.status == 200:
                with open("url.csv","w") as f:
                    f.write("pass\n")
                    #call function
                    menu_code[command-1](soup)
                print(f"Time : {time.process_time():.2f} Second")
            elif response.status == 404:
                print("Not Found")
            elif response.status == 403:
                print("Website Block Scraping")
            else:
                print("Problem found : ",response.status)
        except ConnectionError as res:
            print("Connection Error")
            
        print("+++++++++++++++++++++++++++++++++++++++")
        print("+█▀▀ █▀▀█ █▀▄▀█ █▀▀█ █   █▀▀ ▀▀█▀▀ █▀▀+")
        print("+█   █  █ █ ▀ █ █  █ █   █▀▀   █   █▀▀+")
        print("+▀▀▀ ▀▀▀▀ ▀   ▀ █▀▀▀ ▀▀▀ ▀▀▀   ▀   ▀▀▀+")
        print("+++++++++++++++++++++++++++++++++++++++")