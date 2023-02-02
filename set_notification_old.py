import pandas as pd
import urllib
from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime, timedelta
#from subprocess import call
from PIL import Image, ImageDraw, ImageFont
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and 
    getattr(ssl, '_create_unverified_context', None)): 
    ssl._create_default_https_context = ssl._create_unverified_context

################################################################################

LineToken = 'Fq4vsJ7rDeDnfaBgucfrbPhn9YHfra2T1rxg4g6sLz4' #Test
#LineToken = 'T6sEBJfibA86LDqjpZAVH1B9AATnJHoiyAsx7vq33lV' #Price Alerts

def func_LineNotify(Message,LineToken):
    url  = "https://notify-api.line.me/api/notify"
    data = ({'message':Message})
    LINE_HEADERS = {"Authorization":"Bearer " + LineToken}
    session  = requests.Session()
    response = session.post(url, headers=LINE_HEADERS, data=data)
    return response

def func_LineNotifyImage(Message, ImageFile, LineToken):
    url  = "https://notify-api.line.me/api/notify"
    data = ({'message': Message})
    file = {'imageFile': open(ImageFile,'rb')}
    LINE_HEADERS = {"Authorization":"Bearer " + LineToken}
    session  = requests.Session()
    response = session.post(url, headers=LINE_HEADERS, files=file, data=data)
    return response

def funcGetPrice(): #from Bloomberg
    QuotePage = i 
    Page = urllib.request.urlopen(QuotePage)
    soup = BeautifulSoup(Page, 'html.parser')

    Price       = soup.find('div', attrs={'class': 'price'}).text
    PriceDateTime = soup.find('div', attrs={'class': 'price-datetime'}).text.strip()
    PriceDateTime = PriceDateTime[5:]
    
    change_status_down = soup.find('div', attrs={'class':'price-container down'})
    change_status_up   = soup.find('div', attrs={'class':'price-container up'})

    if not change_status_up == None:
        Status = '+' 
        change_status = change_status_up
    else:
        Status = '-'
        change_status = change_status_down  
    
    Change_box   = soup.find('div', attrs={'class': 'change-container'})
    Change       = Change_box.text.strip()
    Change_val   = Change[:5]
    Change_pct   = Change[7:].strip()
    return(Price, PriceDateTime, Status, Change_val, Change_pct)

while True:
    try:
        weekday = datetime.weekday(datetime.utcnow() + timedelta(hours=7)) #Bangkok time
        if weekday==5:
            print("It's Saturday")
            pass
        elif weekday==6:
            print("It's Sunday")
            pass
        else:
            QuotePage = 'https://marketdata.set.or.th/mkt/marketsummary.do?language=en&country=US'
            Page = urllib.request.urlopen(QuotePage)
            soup = BeautifulSoup(Page, 'html.parser')
            PriceDateTime = soup.find('div', class_='row text-right table-noborder').text.strip()
            PriceDateTime = PriceDateTime[14:]
            #print(PriceDateTime)
            
            dfs = pd.read_html(QuotePage)
            #print(len(dfs))
            #print(dfs)
            
            df = pd.DataFrame(dfs[0])
            #df = df.apply(pd.to_numeric, errors='ignore')
            print(df)
            
            SET = '{0:,.2f}'.format(df.iloc[0,1])
            SET_change_val = '{:+.2f}'.format(df.iloc[0,2])
            SET_change_pct = '{:+.2f}'.format(df.iloc[0,3])
            Message1 = 'SET = ' + str(SET) + ' ' + str(SET_change_val) + ' ' + str(SET_change_pct) + '%'
            
            SET50 = '{0:,.2f}'.format(df.iloc[1,1])
            SET50_change_val = '{:+.2f}'.format(df.iloc[1,2])
            SET50_change_pct = '{:+.2f}'.format(df.iloc[1,3])
            Message2 = 'SET50 = ' + str(SET50) + ' ' + str(SET50_change_val) + ' ' + str(SET50_change_pct) + '%'
            
            SET100 = '{0:,.2f}'.format(df.iloc[2,1])
            SET100_change_val = '{:+.2f}'.format(df.iloc[2,2])
            SET100_change_pct = '{:+.2f}'.format(df.iloc[2,3])
            Message3 = 'SET100 = ' + str(SET100) + ' ' + str(SET100_change_val) + ' ' + str(SET100_change_pct) + '%'
            
            sSET = '{0:,.2f}'.format(df.iloc[3,1])
            sSET_change_val = '{:+.2f}'.format(df.iloc[3,2])
            sSET_change_pct = '{:+.2f}'.format(df.iloc[3,3])
            Message4 = 'sSET = ' + str(sSET) + ' ' + str(sSET_change_val) + ' ' + str(sSET_change_pct) + '%'
            
            SETHD = '{0:,.2f}'.format(df.iloc[4,1])
            SETHD_change_val = '{:+.2f}'.format(df.iloc[4,2])
            SETHD_change_pct = '{:+.2f}'.format(df.iloc[4,3])
            Message5 = 'SETHD = ' + str(SETHD) + ' ' + str(SETHD_change_val) + ' ' + str(SETHD_change_pct) + '%'
            
            MAI = '{0:,.2f}'.format(df.iloc[8,1])
            MAI_change_val = '{:+.2f}'.format(df.iloc[8,2])
            MAI_change_pct = '{:+.2f}'.format(df.iloc[8,3])
            Message6 = 'MAI = ' + str(MAI) + ' ' + str(MAI_change_val) + ' ' + str(MAI_change_pct) + '%'
            
            Message = PriceDateTime+'\n'+Message1+'\n'+Message2+'\n'+Message3+'\n'+Message4+'\n'+Message5+'\n'+Message6
            
            #for Windows
            #img = Image.new('RGB', (270, 145), color = (73, 109, 137))
            #font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 15) 
            #d = ImageDraw.Draw(img)
            #d.text((10,10), Message, font=font, fill=(255,255,0))
            #img.save('C:/Users/USER/Dropbox/Python/LINE_Notifications/Commodities/SET_notification.png')
            #ResponseLine = func_LineNotifyImage('SET Index', 'C:/Users/USER/Dropbox/Python/LINE_Notifications/Commodities/SET_notification.png', LineToken)
            
            #for Raspberry Pi
            text = 'SET Alerts'
            img = Image.new('RGB', (300, 130), color = (73, 109, 137))
            font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSansBold.ttf', 15)
            d = ImageDraw.Draw(img)
            d.text((10,10), Message, font=font, fill=(255,255,0))
            img.save('/home/pi/Desktop/SET_notification.png')
            ResponseLine = func_LineNotifyImage(text, '/home/pi/Desktop/SET_notification.png', LineToken)
            
            #for MAC
            #img = Image.new('RGB', (270, 145), color = (73, 109, 137))
            #font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSansBold.ttf', 15) 
            #Message = PriceDateTime+'\n'+Message1+'\n'+Message2+'\n'+Message3+'\n'+Message4+'\n'+Message5+'\n'+Message6
            #d = ImageDraw.Draw(img)
            #d.text((10,10), Message, font=font, fill=(255,255,0))
            #img.save('/home/pi/Desktop/SET_notification.png')
            #ResponseLine = func_LineNotifyImage('SET Index', '/home/pi/Desktop/SET_notification.png', LineToken)
            
    except Exception:
        print('fail')
        pass
    finally:
        time.sleep(1800)





