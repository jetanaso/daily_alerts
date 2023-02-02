import emoji
import pandas as pd
from time import sleep
from datetime import datetime, time
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
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver_path = "/usr/bin/chromedriver"


mkt_open = time(10, 0, 0)
mkt_close = time(16, 45, 0)
now = datetime.now() # local (BKK)
print(now)
time_now = now.time()

weekday = datetime.weekday(datetime.utcnow())
if weekday==5:
    print("It's Saturday")
    pass
elif weekday==6:
    print("It's Sunday")
    pass
else:
    url = "https://www.set.or.th/en/home"

    count = 0
    while count < 100:
        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver = webdriver.Chrome(options=options, service=Service(driver_path))
        driver.get(url)
        html = driver.page_source
        # print(html)
        try:
            data = pd.read_html(html)
            driver.close()
            break
        except ValueError: # No tables found
            count += 1
            driver.close()
            sleep(1)

    df = data[0]
    df = df.set_index("Index")
    print(df)

    SET = "{:,.2f}".format(df.loc["SET", "Last"])
    SET_change_val = df.loc["SET", "Change"]
    SET_change_val = "+"+str(df.loc["SET", "Change"]) if SET_change_val > 0 else str(df.loc["SET", "Change"])
    SET_value = "{:,.0f}".format(df.loc["SET", "Value (M.Baht)"])
    if SET_value == "-" or time_now >= mkt_close:
        message_set = "SET = " + str(SET) + "  " + "(market closed)"
    else:
        message_set = "SET = " + str(SET) + "  " + str(SET_change_val) + "  " + str(SET_value) + " " + "MB"

    SET50 = "{:,.2f}".format(df.loc["SET50", "Last"])
    SET50_change_val = df.loc["SET50", "Change"]
    SET50_change_val = "+"+str(df.loc["SET50", "Change"]) if SET50_change_val > 0 else str(df.loc["SET50", "Change"])
    SET50_value = "{:,.0f}".format(df.loc["SET50", "Value (M.Baht)"])
    if SET50_value == "-" or time_now >= mkt_close:
        message_set50 = "SET50 = " + str(SET50) + "  " + "(market closed)"
    else:
        message_set50 = "SET50 = " + str(SET50) + "  " + str(SET50_change_val) + "  " + str(SET50_value) + " " + "MB"

    SET100 = "{:,.2f}".format(df.loc["SET100", "Last"])
    SET100_change_val = df.loc["SET100", "Change"]
    SET100_change_val = "+"+str(df.loc["SET100", "Change"]) if SET100_change_val > 0 else str(df.loc["SET100", "Change"])
    SET100_value = "{:,.0f}".format(df.loc["SET100", "Value (M.Baht)"])
    if SET100_value == "-" or time_now >= mkt_close:
        message_set100 = "SET100 = " + str(SET100) + "  " + "(market closed)"
    else:
        message_set100 = "SET100 = " + str(SET100) + "  " + str(SET100_change_val) + "  " + str(SET100_value) + " " + "MB"

    sSET = "{:,.2f}".format(df.loc["sSET", "Last"])
    sSET_change_val = df.loc["sSET", "Change"]
    sSET_change_val = "+"+str(df.loc["sSET", "Change"]) if sSET_change_val > 0 else str(df.loc["sSET", "Change"])
    sSET_value = "{:,.0f}".format(df.loc["sSET", "Value (M.Baht)"])
    if sSET_value == "-" or time_now >= mkt_close:
        message_sset = "sSET = " + str(sSET) + "  " + "(market closed)"
    else:
        message_sset = "sSET = " + str(sSET) + "  " + str(sSET_change_val) + "  " + str(sSET_value) + " " + "MB"

    SETCLMV = "{:,.2f}".format(df.loc["SETCLMV", "Last"])
    SETCLMV_change_val = df.loc["SETCLMV", "Change"]
    SETCLMV_change_val = "+"+str(df.loc["SETCLMV", "Change"]) if SETCLMV_change_val > 0 else str(df.loc["SETCLMV", "Change"])
    SETCLMV_value = "{:,.0f}".format(df.loc["SETCLMV", "Value (M.Baht)"])
    if SETCLMV_value == "-" or time_now >= mkt_close:
        message_setclmv = "SETCLMV = " + str(SETCLMV) + "  " + "(market closed)"
    else:
        message_setclmv = "SETCLMV = " + str(SETCLMV) + "  " + str(SETCLMV_change_val) + "  " + str(SETCLMV_value) + " " + "MB"

    SETHD = "{:,.2f}".format(df.loc["SETHD", "Last"])
    SETHD_change_val = df.loc["SETHD", "Change"]
    SETHD_change_val = "+"+str(df.loc["SETHD", "Change"]) if SETHD_change_val > 0 else str(df.loc["SETHD", "Change"])
    SETHD_value = "{:,.0f}".format(df.loc["SETHD", "Value (M.Baht)"])
    if SETHD_value == "-" or time_now >= mkt_close:
        message_sethd = "SETHD = " + str(SETHD) + "   " + "(market closed)"
    else:
        message_sethd = "SETHD = " + str(SETHD) + "   " + str(SETHD_change_val) + "   " + str(SETHD_value) + "  " + "MB"

    SETTHSI = "{:,.2f}".format(df.loc["SETTHSI", "Last"])
    SETTHSI_change_val = df.loc["SETTHSI", "Change"]
    SETTHSI_change_val = "+"+str(df.loc["SETTHSI", "Change"]) if SETTHSI_change_val > 0 else str(df.loc["SETTHSI", "Change"])
    SETTHSI_value = "{:,.0f}".format(df.loc["SETTHSI", "Value (M.Baht)"])
    if SETTHSI_value == "-" or time_now >= mkt_close:
        message_setthsi = "SETTHSI = " + str(SETTHSI) + "  " + "(market closed)"
    else:
        message_setthsi = "SETTHSI = " + str(SETTHSI) + "  " + str(SETTHSI_change_val) + "  " + str(SETTHSI_value) + " " + "MB"

    SETWB = "{:,.2f}".format(df.loc["SETWB", "Last"])
    SETWB_change_val = df.loc["SETWB", "Change"]
    SETWB_change_val = "+"+str(df.loc["SETWB", "Change"]) if SETWB_change_val > 0 else str(df.loc["SETWB", "Change"])
    SETWB_value = "{:,.0f}".format(df.loc["SETWB", "Value (M.Baht)"])
    if SETWB_value == "-" or time_now >= mkt_close:
        message_setwb = "SETWB = " + str(SETWB) + "  " + "(market closed)"
    else:
        message_setwb = "SETWB = " + str(SETWB) + "  " + str(SETWB_change_val) + "  " + str(SETWB_value) + " " + "MB"

    message_all = message_set+"\n"+message_set50+"\n"+message_set100+"\n"+message_sset+"\n"+message_setclmv+"\n"+message_sethd+"\n"+message_setthsi+"\n"+message_setwb
    print(message_all)

    # ACCESS_TOKEN = "Fq4vsJ7rDeDnfaBgucfrbPhn9YHfra2T1rxg4g6sLz4" #Test
    ACCESS_TOKEN = "T6sEBJfibA86LDqjpZAVH1B9AATnJHoiyAsx7vq33lV" #Price Alerts
    notify = LineNotify(ACCESS_TOKEN)

    # send SET
    emoji_text = emoji.emojize(":pray: SET Alerts :pray:", language="alias")
    canvas = Image.new("RGB", (270, 145), color = (73, 109, 137))
    # font = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf", 13)
    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSansBold.ttf", 13)
    d = ImageDraw.Draw(canvas)
    d.text((10,10), message_all, font=font, fill=(255, 255, 0))
    # image_path = "C:/projects/daily_alerts/temp/set_notification.png"
    image_path = "/home/pi/Desktop/set_notification.png"
    canvas.save(image_path)
    notify.send(emoji_text, image_path=image_path)