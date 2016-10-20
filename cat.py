#coding=utf-8
import urllib2
import os
import re
import time



def get_page(url):
    html = urllib2.urlopen(url)
    pagelist = []         
    for line in html:    
        if '猫' in line:    #获取有猫的图片的页面数字代码
            pattern = filter(str.isdigit, line) 
            pagelist = pagelist + [pattern]
    page = pagelist    #将数字代码转化为列表方便提取
    return page

 

def find_imgs(page_url):
    html = urllib2.urlopen(page_url)
    for line in html:       #过滤每个url中的每一行
        if '.tooopen.com/images/20' and 'tooopen_sy_'and '.jpg' in line:
            imagecode = filter(str.isdigit, line)

    img_addrs = 'http://img'+imagecode[0:2]+'.tooopen.com/images/'+imagecode[2:10]+'/tooopen_sy_'+imagecode[10:]+'.jpg'
    return img_addrs     #获得图片网址

def save_imgs(img_addrs,folder):
    picurl = img_addrs
    image = urllib2.urlopen(img_addrs).read()
    filename = str(int(time.time()))+'.jpg' #用urllib2提供的接口下载图片
    output = open(filename,'w')
    output.write(image)   
    output.close()

def download_mm(folder,pages):
    os.mkdir(folder) #创建一个文件夹
    os.chdir(folder) #跳转到文件夹中
    folder_top = os.getcwd() #获取工作目录
    pages = int(pages)
    tab = range(1,pages)
    for number in tab:
        url = 'http://www.tooopen.com/img/89_869_1_'+str(number)+'.aspx'
        page = get_page(url) #获得有图片的网页
        print '爬虫正在爬取主页面'+ url
        for i in page:
            page_num = i
            page_url = 'http://www.tooopen.com/view/' + str(page_num) + '.html' 
            #从上面的列表中获取有猫的图片
            if page_url is not 'http://www.tooopen.com/view/33.html':
                try:
                    img_addrs = find_imgs(page_url) #获取图片url
                    print '正在抓取'+page_url 
                    try:
                        save_imgs(img_addrs,folder) 
                        os.chdir(folder_top)  #保存图片后回到工作目录，循环            
                    except:
                        continue 
                         
                except:
                    continue
            else:
                continue
        os.chdir(folder_top)#save the pic     
        

if __name__ == '__main__':
    timeformat ='%Y-%m-%d %X'
    timenow = time.strftime( timeformat,time.localtime( time.time() ) )
    folder = str(timenow)  
    print folder+'爬虫开始工作'
    time.sleep(0.2)
    pages = raw_input('请输入你要搜索的页数(默认1页）：')

    print '少女祈祷中………'
    
    if pages == '':
        pages = 1

    download_mm(str(folder),pages)

    print '爬虫运行完成，猫图保存在名为“',folder,'”的文件夹中，按任意键退出~~'
    raw_input()
    exit()










