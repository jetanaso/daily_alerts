import emoji
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image, ImageDraw, ImageFont
from line_notify import LineNotify
import warnings
warnings.filterwarnings("ignore")

options = Options()
options.BinaryLocation = "/usr/bin/chromium-browser"
options.add_argument("--headless")
options.add_argument("ignore-certificate-errors")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver_path = "/usr/bin/chromedriver"
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver = webdriver.Chrome(options=options, service=Service(driver_path))

now = datetime.now() # local (BKK)
print(now)

weekday = datetime.weekday(datetime.utcnow())
if weekday==5:
    print("It's Saturday")
    pass
elif weekday==6:
    print("It's Sunday")
    pass
else:
    url = "https://www.investing.com/indices/major-indices/"
    driver.get(url)
    html = driver.page_source
    data = pd.read_html(html)

    target = data[0]
    target = target.drop(columns=["Unnamed: 0", "Unnamed: 8"])

    # West
    Dow = "{0:,.2f}".format(target.iloc[0,1])
    Dow_change = "{0:,.2f}".format(target.iloc[0,4])
    Dow_changepct = target.iloc[0,5]
    DowGroup = "Dow = " + str(Dow) + "   " + str(Dow_change) + "   " + str(Dow_changepct)

    SP = "{0:,.2f}".format(target.iloc[1,1])
    SP_change = "{0:,.2f}".format(target.iloc[1,4])
    SP_changepct = target.iloc[1,5]
    SPGroup = "S&P = " + str(SP) + "   " + str(SP_change) + "   " + str(SP_changepct)

    NQ = "{0:,.2f}".format(target.iloc[2,1])
    NQ_change = "{0:,.2f}".format(target.iloc[2,4])
    NQ_changepct = target.iloc[2,5]
    NQGroup = "Nasdaq = " + str(NQ) + "   " + str(NQ_change) + "   " + str(NQ_changepct)

    VIX = "{0:,.2f}".format(target.iloc[4,1])
    VIX_change = "{0:,.2f}".format(target.iloc[4,4])
    VIX_changepct = target.iloc[4,5]
    VIXGroup = "VIX = " + str(VIX) + "   " + str(VIX_change) + "   " + str(VIX_changepct)

    DAX = "{0:,.2f}".format(target.iloc[8,1])
    DAX_change = "{0:,.2f}".format(target.iloc[8,4])
    DAX_changepct = target.iloc[8,5]
    DAXGroup = "DAX = " + str(DAX) + "  " + str(DAX_change) + "   " + str(DAX_changepct)

    Bovespa = "{0:,.2f}".format(target.iloc[6,1])
    Bovespa_change = "{0:,.2f}".format(target.iloc[6,4])
    Bovespa_changepct = target.iloc[6,5]
    BovespaGroup = "Bovespa = " + str(Bovespa) + "  " + str(Bovespa_change) + "   " + str(Bovespa_changepct)

    message_west = DowGroup+"\n"+SPGroup+"\n"+NQGroup+"\n"+VIXGroup+"\n"+DAXGroup+"\n"+BovespaGroup
    print(message_west)

    # East
    Nikkei = "{0:,.2f}".format(target.iloc[28,1])
    Nikkei_change = "{0:,.2f}".format(target.iloc[28,4])
    Nikkei_changepct = target.iloc[28,5]
    NikkeiGroup = "Nikkei = " + str(Nikkei) + "  " + str(Nikkei_change) + "   " + str(Nikkei_changepct)

    Kospi = "{0:,.2f}".format(target.iloc[38,1])
    Kospi_change = "{0:,.2f}".format(target.iloc[38,4])
    Kospi_changepct = target.iloc[38,5]
    KospiGroup = "Kospi = " + str(Kospi) + "  " + str(Kospi_change) + "   " + str(Kospi_changepct)

    A50 = "{0:,.2f}".format(target.iloc[33,1])
    A50_change = "{0:,.2f}".format(target.iloc[33,4])
    A50_changepct = target.iloc[33,5]
    A50Group = "ChinaA50 = " + str(A50) + "  " + str(A50_change) + "   " + str(A50_changepct)

    HK = "{0:,.2f}".format(target.iloc[35,1])
    HK_change = "{0:,.2f}".format(target.iloc[35,4])
    HK_changepct = target.iloc[35,5]
    HKGroup = "HangSeng = " + str(HK) + "  " + str(HK_change) + "   " + str(HK_changepct)

    TW = "{0:,.2f}".format(target.iloc[36,1])
    TW_change = "{0:,.2f}".format(target.iloc[36,4])
    TW_changepct = target.iloc[36,5]
    TWGroup = "Taiwan = " + str(TW) + "  " + str(TW_change) + "   " + str(TW_changepct)

    Idx = "{0:,.2f}".format(target.iloc[39,1])
    Idx_change = "{0:,.2f}".format(target.iloc[39,4])
    Idx_changepct = target.iloc[39,5]
    IdxGroup = "Idx = " + str(Idx) + "  " + str(Idx_change) + "   " + str(Idx_changepct)

    PSEi = "{0:,.2f}".format(target.iloc[42,1])
    PSEi_change = "{0:,.2f}".format(target.iloc[42,4])
    PSEi_changepct = target.iloc[42,5]
    PSEiGroup = "PSEi = " + str(PSEi) + "  " + str(PSEi_change) + "   " + str(PSEi_changepct)

    Sensex = "{0:,.2f}".format(target.iloc[41,1])
    Sensex_change = "{0:,.2f}".format(target.iloc[41,4])
    Sensex_changepct = target.iloc[41,5]
    SensexGroup = "BSE Sensex = " + str(Sensex) + "  " + str(Sensex_change) + "   " + str(Sensex_changepct)

    message_east = NikkeiGroup+"\n"+KospiGroup+"\n"+A50Group+"\n"+HKGroup+"\n"+TWGroup+"\n"+IdxGroup+"\n"+PSEiGroup+"\n"+SensexGroup
    print(message_east)

    # Commodities
    url = "https://www.investing.com/commodities/real-time-futures/"
    driver.get(url)
    html = driver.page_source
    data = pd.read_html(html)

    commoditiesTarget = data[0]
    commoditiesTarget = commoditiesTarget.drop(columns=["Unnamed: 0", "Unnamed: 9"])

    Brent = "{0:,.2f}".format(commoditiesTarget.iloc[8,2])
    Brent_change = "{0:,.2f}".format(commoditiesTarget.iloc[8,5])
    Brent_changepct = commoditiesTarget.iloc[8,6]
    BrentGroup = "Brent = " + str(Brent) + "  " + str(Brent_change) + "   " + str(Brent_changepct)

    WTI = "{0:,.2f}".format(commoditiesTarget.iloc[7,2])
    WTI_change = "{0:,.2f}".format(commoditiesTarget.iloc[7,5])
    WTI_changepct = commoditiesTarget.iloc[7,6]
    WTIGroup = "WTI = " + str(WTI) + "  " + str(WTI_change) + "   " + str(WTI_changepct)

    Gold = "{0:,.2f}".format(commoditiesTarget.iloc[1,2])
    Gold_change = "{0:,.2f}".format(commoditiesTarget.iloc[1,5])
    Gold_changepct = commoditiesTarget.iloc[1,6]
    GoldGroup = "Gold = " + str(Gold) + "  " + str(Gold_change) + "   " + str(Gold_changepct)

    NG = "{0:,.3f}".format(commoditiesTarget.iloc[9,2])
    NG_change = "{0:,.3f}".format(commoditiesTarget.iloc[9,5])
    NG_changepct = commoditiesTarget.iloc[9,6]
    NGGroup = "Natural Gas = " + str(NG) + "  " + str(NG_change) + "   " + str(NG_changepct)

    # Bond
    url = "https://www.investing.com/rates-bonds/"
    driver.get(url)
    html = driver.page_source
    data = pd.read_html(html)

    BondTarget = data[0]
    BondTarget = BondTarget.drop(columns=["Unnamed: 0", "Unnamed: 9"])

    Bond2Y = "{0:,.3f}".format(BondTarget.iloc[3,2])
    Bond2Y_change = "{0:,.3f}".format(BondTarget.iloc[3,5])
    Bond2Y_changepct = BondTarget.iloc[3,6]
    Bond2YGroup = "US Bond 2Y = " + str(Bond2Y) + "  " + str(Bond2Y_change) + "   " + str(Bond2Y_changepct)

    Bond10Y = "{0:,.3f}".format(BondTarget.iloc[1,2])
    Bond10Y_change = "{0:,.3f}".format(BondTarget.iloc[1,5])
    Bond10Y_changepct = BondTarget.iloc[1,6]
    Bond10YGroup = "US Bond 10Y = " + str(Bond10Y) + "  " + str(Bond10Y_change) + "   " + str(Bond10Y_changepct)

    # Futures
    url = "https://www.investing.com/indices/indices-futures"
    driver.get(url)
    html = driver.page_source
    data = pd.read_html(html)
    driver.close()

    FuturesTarget = data[0]
    FuturesTarget = FuturesTarget.drop(columns=["Unnamed: 0", "Unnamed: 9"])

    DJfutures = "{0:,.2f}".format(FuturesTarget.iloc[0,2])
    DJfutures_change = "{0:,.2f}".format(FuturesTarget.iloc[0,5])
    DJfutures_changepct = FuturesTarget.iloc[0,6]
    DJfuturesGroup = "DJ futures = " + str(DJfutures) + "  " + str(DJfutures_change) + "   " + str(DJfutures_changepct)

    message_commodities = BrentGroup+"\n"+WTIGroup+"\n"+GoldGroup+"\n"+NGGroup+"\n"+DJfuturesGroup+"\n"+Bond2YGroup+"\n"+Bond10YGroup
    print(message_commodities)

    # ACCESS_TOKEN = "Fq4vsJ7rDeDnfaBgucfrbPhn9YHfra2T1rxg4g6sLz4" #Test
    ACCESS_TOKEN = "T6sEBJfibA86LDqjpZAVH1B9AATnJHoiyAsx7vq33lV" #Price Alerts
    notify = LineNotify(ACCESS_TOKEN)

    # send WEST
    emoji_text = emoji.emojize(":pray: Western Indices Alerts :pray:", language="alias")
    # font = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf", 13)
    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSansBold.ttf", 13)
    canvas = Image.new("RGB", (270, 115), color = (73, 109, 137))

    d = ImageDraw.Draw(canvas)
    d.text((10,10), message_west, font=font, fill=(255, 255, 0))
    # image_path = "C:/projects/daily_alerts/temp/west_notification.png"
    image_path = "/home/pi/Desktop/west_notification.png"
    canvas.save(image_path)
    notify.send(emoji_text, image_path=image_path)

    # send EAST
    emoji_text = emoji.emojize(":pray: Eastern Indices Alerts :pray:", language="alias")
    canvas = Image.new("RGB", (270, 145), color = (73, 109, 137))
    d = ImageDraw.Draw(canvas)
    d.text((10,10), message_east, font=font, fill=(255, 255, 0))
    # image_path = "C:/projects/daily_alerts/temp/east_notification.png"
    image_path = "/home/pi/Desktop/east_notification.png"
    canvas.save(image_path)
    notify.send(emoji_text, image_path=image_path)

    # send COMMODITIES
    emoji_text = emoji.emojize(":pray: Commodities Alerts :pray:", language="alias")
    canvas = Image.new("RGB", (270, 130), color = (73, 109, 137))
    d = ImageDraw.Draw(canvas)
    d.text((10,10), message_commodities, font=font, fill=(255, 255, 0))
    # image_path = "C:/projects/daily_alerts/temp/commodities_notification.png"
    image_path = "/home/pi/Desktop/commodities_notification.png"
    canvas.save(image_path)
    notify.send(emoji_text, image_path=image_path)
