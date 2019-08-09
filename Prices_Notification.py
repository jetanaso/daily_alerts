import pandas as pd
#from selenium import webdriver
import requests
import emoji
import time
import urllib
#from subprocess import call
from datetime import datetime
#from datetime import date
#from datetime import timedelta
from PIL import Image, ImageDraw, ImageFont

#LineToken = 'Fq4vsJ7rDeDnfaBgucfrbPhn9YHfra2T1rxg4g6sLz4' #Test
#LineToken = 'T6sEBJfibA86LDqjpZAVH1B9AATnJHoiyAsx7vq33lV' #Price Alerts
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

#####################################################################################

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

#####################################################################################

while True:
    try:
        weekday = datetime.weekday(datetime.utcnow())
        if weekday==5:
            print("It's Saturday")
            pass
        elif weekday==6:
            print("It's Sunday")
            pass
        else:
            url = 'https://www.investing.com/indices/major-indices/'
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as response:
                html_source = response.read()
    
            data = pd.read_html(html_source)
            target = data[0]
            target = target.drop(columns=['Unnamed: 0', 'Unnamed: 8'])
    
            #West
            Dow = '{0:,.2f}'.format(target.iloc[0,1])
            Dow_change = '{0:,.2f}'.format(target.iloc[0,4])
            Dow_changepct = target.iloc[0,5]
            DowGroup = 'Dow = ' + str(Dow) + '   ' + str(Dow_change) + '   ' + str(Dow_changepct)
            
            SP = '{0:,.2f}'.format(target.iloc[1,1])
            SP_change = '{0:,.2f}'.format(target.iloc[1,4])
            SP_changepct = target.iloc[1,5]
            SPGroup = 'S&P = ' + str(SP) + '   ' + str(SP_change) + '   ' + str(SP_changepct)
            
            NQ = '{0:,.2f}'.format(target.iloc[2,1])
            NQ_change = '{0:,.2f}'.format(target.iloc[2,4])
            NQ_changepct = target.iloc[2,5]
            NQGroup = 'Nasdaq = ' + str(NQ) + '   ' + str(NQ_change) + '   ' + str(NQ_changepct)
            
            VIX = '{0:,.2f}'.format(target.iloc[4,1])
            VIX_change = '{0:,.2f}'.format(target.iloc[4,4])
            VIX_changepct = target.iloc[4,5]
            VIXGroup = 'VIX = ' + str(VIX) + '   ' + str(VIX_change) + '   ' + str(VIX_changepct)
            
            DAX = '{0:,.2f}'.format(target.iloc[8,1])
            DAX_change = '{0:,.2f}'.format(target.iloc[8,4])
            DAX_changepct = target.iloc[8,5]
            DAXGroup = 'DAX = ' + str(DAX) + '  ' + str(DAX_change) + '   ' + str(DAX_changepct)
            
            Bovespa = '{0:,.2f}'.format(target.iloc[6,1])
            Bovespa_change = '{0:,.2f}'.format(target.iloc[6,4])
            Bovespa_changepct = target.iloc[6,5]
            BovespaGroup = 'Bovespa = ' + str(Bovespa) + '  ' + str(Bovespa_change) + '   ' + str(Bovespa_changepct)
            
            Message1 = DowGroup+'\n'+SPGroup+'\n'+NQGroup+'\n'+VIXGroup+'\n'+DAXGroup+'\n'+BovespaGroup
            #print(Message1)
            
            #for Windows
            #emoji_text = emoji.emojize(':pray: Western Indices Alerts :pray:', use_aliases=True)
            #img = Image.new('RGB', (265, 125, color = (73, 109, 137))
            #font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 15)
            #d = ImageDraw.Draw(img)
            #d.text((10,10), Message1, font=font, fill=(255,255,0))
            #img.save('C:/Users/USER/Dropbox/Python/LINE_Notifications/Commodities/WesternIndices_notification.png')
            #ResponseLine = func_LineNotifyImage(emoji_text, 'C:/Users/USER/Dropbox/Python/LINE_Notifications/Commodities/WesternIndices_notification.png', LineToken)
            
            #for Raspberry Pi
            text = 'Western Indices Alerts'
            img = Image.new('RGB', (300, 130), color = (73, 109, 137))
            font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSansBold.ttf', 15)
            d = ImageDraw.Draw(img)
            d.text((10,10), Message1, font=font, fill=(255,255,0))
            img.save('/home/pi/Desktop/WesternIndices_notification.png')
			LineToken = 'Fq4vsJ7rDeDnfaBgucfrbPhn9YHfra2T1rxg4g6sLz4' #Test
            ResponseLine = func_LineNotifyImage(text, '/home/pi/Desktop/WesternIndices_notification.png', LineToken)
            
            #for Mac
            #img = Image.new('RGB', (300, 130), color = (73, 109, 137))
            #font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
            #d = ImageDraw.Draw(img)
            #d.text((10,10), Message1, font=font, fill=(255,255,0))
            #img.save('/Users/jetana/Dropbox/Python/LINE_Notifications/Commodities/WesternIndices_notification.png')
            #ResponseLine = func_LineNotifyImage('Western Indices Alerts', '/Users/jetana/Dropbox/Python/LINE_Notifications/Commodities/WesternIndices_notification.png', LineToken)
            
            ########################################################################################
    
            #East
            Nikkei = '{0:,.2f}'.format(target.iloc[28,1])
            Nikkei_change = '{0:,.2f}'.format(target.iloc[28,4])
            Nikkei_changepct = target.iloc[28,5]
            NikkeiGroup = 'Nikkei = ' + str(Nikkei) + '  ' + str(Nikkei_change) + '   ' + str(Nikkei_changepct)
    
            Kospi = '{0:,.2f}'.format(target.iloc[38,1])
            Kospi_change = '{0:,.2f}'.format(target.iloc[38,4])
            Kospi_changepct = target.iloc[38,5]
            KospiGroup = 'Kospi = ' + str(Kospi) + '  ' + str(Kospi_change) + '   ' + str(Kospi_changepct)
    
            A50 = '{0:,.2f}'.format(target.iloc[33,1])
            A50_change = '{0:,.2f}'.format(target.iloc[33,4])
            A50_changepct = target.iloc[33,5]
            A50Group = 'ChinaA50 = ' + str(A50) + '  ' + str(A50_change) + '   ' + str(A50_changepct)
    
            HK = '{0:,.2f}'.format(target.iloc[35,1])
            HK_change = '{0:,.2f}'.format(target.iloc[35,4])
            HK_changepct = target.iloc[35,5]
            HKGroup = 'HangSeng = ' + str(HK) + '  ' + str(HK_change) + '   ' + str(HK_changepct)
    
            TW = '{0:,.2f}'.format(target.iloc[36,1])
            TW_change = '{0:,.2f}'.format(target.iloc[36,4])
            TW_changepct = target.iloc[36,5]
            TWGroup = 'Taiwan = ' + str(TW) + '  ' + str(TW_change) + '   ' + str(TW_changepct)
    
            Idx = '{0:,.2f}'.format(target.iloc[39,1])
            Idx_change = '{0:,.2f}'.format(target.iloc[39,4])
            Idx_changepct = target.iloc[39,5]
            IdxGroup = 'Idx = ' + str(Idx) + '  ' + str(Idx_change) + '   ' + str(Idx_changepct)
    
            PSEi = '{0:,.2f}'.format(target.iloc[42,1])
            PSEi_change = '{0:,.2f}'.format(target.iloc[42,4])
            PSEi_changepct = target.iloc[42,5]
            PSEiGroup = 'PSEi = ' + str(PSEi) + '  ' + str(PSEi_change) + '   ' + str(PSEi_changepct)
    
            Sensex = '{0:,.2f}'.format(target.iloc[41,1])
            Sensex_change = '{0:,.2f}'.format(target.iloc[41,4])
            Sensex_changepct = target.iloc[41,5]
            SensexGroup = 'BSE Sensex = ' + str(Sensex) + '  ' + str(Sensex_change) + '   ' + str(Sensex_changepct)
    
            Message2 = NikkeiGroup+'\n'+KospiGroup+'\n'+A50Group+'\n'+HKGroup+'\n'+TWGroup+'\n'+IdxGroup+'\n'+PSEiGroup+'\n'+SensexGroup
            
            #for Windows
            #emoji_text = emoji.emojize(':pray: Eastern Indices Alerts :pray:', use_aliases=True)
            #img = Image.new('RGB', (300, 160), color = (73, 109, 137))
            #font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 15)
            #d = ImageDraw.Draw(img)
            #d.text((10,10), Message2, font=font, fill=(255,255,0))
            #img.save('C:/Users/USER/Dropbox/Python/LINE_Notifications/Commodities/EasternIndices_notification.png')
            #ResponseLine = func_LineNotifyImage(emoji_text, 'C:/Users/USER/Dropbox/Python/LINE_Notifications/Commodities/EasternIndices_notification.png', LineToken)
            
            #for Raspberry Pi
            text = 'Eastern Indices Alerts'
            img = Image.new('RGB', (300, 130), color = (73, 109, 137))
            font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSansBold.ttf', 15)
            d = ImageDraw.Draw(img)
            d.text((10,10), Message2, font=font, fill=(255,255,0))
            img.save('/home/pi/Desktop/EasternIndices_notification.png')
			LineToken = 'Fq4vsJ7rDeDnfaBgucfrbPhn9YHfra2T1rxg4g6sLz4' #Test
            ResponseLine = func_LineNotifyImage(text, '/home/pi/Desktop/EasternIndices_notification.png', LineToken)
            
            #for Mac
            #img = Image.new('RGB', (300, 160), color = (73, 109, 137))
            #font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
            #d = ImageDraw.Draw(img)
            #d.text((10,10), Message2, font=font, fill=(255,255,0))
            #img.save('/Users/jetana/Dropbox/Python/LINE_Notifications/Commodities/EasternIndices_notification.png')
            #ResponseLine = func_LineNotifyImage('Eastern Indices Alerts', '/Users/jetana/Dropbox/Python/LINE_Notifications/Commodities/EasternIndices_notification.png', LineToken)
            
            ########################################################################################
    
            #Commodities
            url = 'https://www.investing.com/commodities/real-time-futures/'
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as response:
                html_source = response.read()
    
            data = pd.read_html(html_source)
            commoditiesTarget = data[0]
            commoditiesTarget = commoditiesTarget.drop(columns=['Unnamed: 0', 'Unnamed: 9'])
            #print(commoditiesTarget)
    
            Brent = '{0:,.2f}'.format(commoditiesTarget.iloc[7,2])
            Brent_change = '{0:,.2f}'.format(commoditiesTarget.iloc[7,5])
            Brent_changepct = commoditiesTarget.iloc[7,6]
            BrentGroup = 'Brent = ' + str(Brent) + '  ' + str(Brent_change) + '   ' + str(Brent_changepct)
    
            WTI = '{0:,.2f}'.format(commoditiesTarget.iloc[6,2])
            WTI_change = '{0:,.2f}'.format(commoditiesTarget.iloc[6,5])
            WTI_changepct = commoditiesTarget.iloc[6,6]
            WTIGroup = 'WTI = ' + str(WTI) + '  ' + str(WTI_change) + '   ' + str(WTI_changepct)
    
            Gold = '{0:,.2f}'.format(commoditiesTarget.iloc[1,2])
            Gold_change = '{0:,.2f}'.format(commoditiesTarget.iloc[1,5])
            Gold_changepct = commoditiesTarget.iloc[1,6]
            GoldGroup = 'Gold = ' + str(Gold) + '  ' + str(Gold_change) + '   ' + str(Gold_changepct)
    
            NG = '{0:,.3f}'.format(commoditiesTarget.iloc[8,2])
            NG_change = '{0:,.3f}'.format(commoditiesTarget.iloc[8,5])
            NG_changepct = commoditiesTarget.iloc[8,6]
            NGGroup = 'Natural Gas = ' + str(NG) + '  ' + str(NG_change) + '   ' + str(NG_changepct)
    
            #Bond
            url = 'https://www.investing.com/rates-bonds/'
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as response:
                html_source = response.read()
    
            data = pd.read_html(html_source)
            BondTarget = data[0]
            BondTarget = BondTarget.drop(columns=['Unnamed: 0', 'Unnamed: 9'])
            #print(BondTarget)
    
            Bond2Y = '{0:,.3f}'.format(BondTarget.iloc[3,2])
            Bond2Y_change = '{0:,.3f}'.format(BondTarget.iloc[3,5])
            Bond2Y_changepct = BondTarget.iloc[3,6]
            Bond2YGroup = 'US Bond 2Y = ' + str(Bond2Y) + '  ' + str(Bond2Y_change) + '   ' + str(Bond2Y_changepct)
    
            Bond10Y = '{0:,.3f}'.format(BondTarget.iloc[1,2])
            Bond10Y_change = '{0:,.3f}'.format(BondTarget.iloc[1,5])
            Bond10Y_changepct = BondTarget.iloc[1,6]
            Bond10YGroup = 'US Bond 10Y = ' + str(Bond10Y) + '  ' + str(Bond10Y_change) + '   ' + str(Bond10Y_changepct)
    
            #Futures
            url = 'https://www.investing.com/indices/indices-futures'
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as response:
                html_source = response.read()
    
            data = pd.read_html(html_source)
            FuturesTarget = data[0]
            FuturesTarget = FuturesTarget.drop(columns=['Unnamed: 0', 'Unnamed: 9'])
            #print(FuturesTarget)
    
            DJfutures = '{0:,.2f}'.format(FuturesTarget.iloc[0,2])
            DJfutures_change = '{0:,.2f}'.format(FuturesTarget.iloc[0,5])
            DJfutures_changepct = FuturesTarget.iloc[0,6]
            DJfuturesGroup = 'DJ futures = ' + str(DJfutures) + '  ' + str(DJfutures_change) + '   ' + str(DJfutures_changepct)
    
            Message3 = BrentGroup+'\n'+WTIGroup+'\n'+GoldGroup+'\n'+NGGroup+'\n'+DJfuturesGroup+'\n'+Bond2YGroup+'\n'+Bond10YGroup
            
            #for Windows
            #emoji_text = emoji.emojize(':pray: Commodities Alerts :pray:', use_aliases=True)
            #img = Image.new('RGB', (300, 150), color = (73, 109, 137))
            #font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 15)
            #d = ImageDraw.Draw(img)
            #d.text((10,10), Message3, font=font, fill=(255,255,0))
            #img.save('C:/Users/USER/Dropbox/Python/LINE_Notifications/Commodities/Commodities_notification.png')
            #ResponseLine = func_LineNotifyImage(emoji_text, 'C:/Users/USER/Dropbox/Python/LINE_Notifications/Commodities/Commodities_notification.png', LineToken)
            
            #for Raspberri Pi
            text = 'Commodities Alerts'
            img = Image.new('RGB', (300, 130), color = (73, 109, 137))
            font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSansBold.ttf', 15)
            d = ImageDraw.Draw(img)
            d.text((10,10), Message3, font=font, fill=(255,255,0))
            img.save('/home/pi/Desktop/Commodities_notification.png')
			LineToken = 'T6sEBJfibA86LDqjpZAVH1B9AATnJHoiyAsx7vq33lV' #Price Alerts
            ResponseLine = func_LineNotifyImage(text, '/home/pi/Desktop/Commodities_notification.png', LineToken)
            
            #for MAC
            #img = Image.new('RGB', (300, 150), color = (73, 109, 137))
            #font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
            #d = ImageDraw.Draw(img)
            #d.text((10,10), Message3, font=font, fill=(255,255,0))
            #img.save('/Users/jetana/Dropbox/Python/LINE_Notifications/Commodities/Commodities_notification.png')
            #ResponseLine = func_LineNotifyImage('Commodities Alerts', '/Users/jetana/Dropbox/Python/LINE_Notifications/Commodities/Commodities_notification.png', LineToken)
            
    except Exception:
        pass
    finally:
        print("done")
        time.sleep(1800)
        #call(['python', 'C:/Users/USER/Dropbox/Python/LINE_Notifications/Commodities/SET_Notification.py'])