# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 16:05:00 2017

@author: amyhu
"""

from selenium import webdriver
import time

url = 'https://twitter.com/search?q=unitedairline&src=typd'
#url='https://twitter.com/search?q=apple&src=typd'

#open the browser and visit the url
#-----------------------------------------
#Windows
driver = webdriver.Chrome('./chromedriver')

#--------------------------------------------
driver.get(url)

#scroll down twice to load more tweets
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

for i in range(68):
         
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)




#find all elements with a class that ends in 'tweet-text'
tweets=driver.find_elements_by_css_selector("[data-item-type=tweet]")


#write the tweets to a file
fw=open('tweets_try_ua.txt','w',encoding='utf-8')
for tweet in tweets:
    txt,retweets,favorites,replies,date='NA','NA','NA','NA','NA'
    
    try: txt=tweet.find_element_by_css_selector("[class$=tweet-text]").text
    except: print ('no text') 
    
    try:
        retweetElement=tweet.find_element_by_css_selector("[class$=js-actionRetweet]")
        retweets=retweetElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text                                      
    except:
        print ('no retweets')
        
    try: 
        favoriteElement=tweet.find_element_by_css_selector("[class$=js-actionFavorite]")
        favorites=favoriteElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text 
    except:
        print ('no favorites')
        
    try:
        replyElement=tweet.find_element_by_css_selector("[class$=js-actionReply]")
        replies=replyElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text 
    except:
        print ('no replies')
        
    try:
        date=tweet.find_element_by_css_selector('[class^=tweet-timestamp]').get_attribute('title')[10:]
        print(date)
        #print(date.get_attribute("innerHTML"))               # to find out the real name of 'data-original-title'
    except:
        print('no date')     

    fw.write(txt.replace('\n',' ')+'\t'+'retreets:'+'\t'+str(retweets)+'\t'+'favorites:'+'\t'+str(favorites)+'\t'+'replies:'+'\t'+str(replies)+'\t'+'data:'+'\t'+str(date)+'\n')


fw.close()


driver.quit()#close the browser