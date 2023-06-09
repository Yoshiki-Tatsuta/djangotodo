from django.shortcuts import render
from django.http import HttpResponse

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
import datetime

# Create your views here.
def index(request):
    return render(request, "weather/index.html")


def get_weather(request):
    """天気を取得"""
    if request.method == 'POST':
            value = request.POST.get('city', None)
            if value == 'osakasi':
                    get_url = 'https://tenki.jp/forecast/6/30/6200/27100/' 
                    city_name = '大阪市'
            elif value == 'hujiiderasi':
                    get_url = 'https://tenki.jp/forecast/6/30/6200/27226/'
                    city_name = '藤井寺市'
            elif value == 'shinjuku':
                    get_url = 'https://tenki.jp/forecast/3/16/4410/13104/'
                    city_name = '新宿'
    
    url = get_url
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, "html.parser")
    rs = soup.find(class_='forecast-days-wrap clearfix')
    # 天気
    rs_wether = rs.findAll(class_='weather-telop')
    today_weather = rs_wether[0].text.strip()
    tomorrow_weather = rs_wether[1].text.strip()
    # 最高気温
    rs_hightemp = rs.findAll(class_='high-temp temp')
    today_hightemp = rs_hightemp[0].text.strip()
    tomorrow_hightemp = rs_hightemp[1].text.strip()
    # 最低気温
    rs_lowtemp = rs.findAll(class_='low-temp temp')
    today_lowtemp = rs_lowtemp[0].text.strip()
    tomorrow_lowtemp = rs_lowtemp[1].text.strip()
    # 降水確率
    rs_rain = soup.select('.rain-probability > td')
    today_rain_1 = rs_rain[0].text.strip()
    today_rain_2 = rs_rain[1].text.strip()
    today_rain_3 = rs_rain[2].text.strip()
    today_rain_4 = rs_rain[3].text.strip()
    tomorrow_rain_1 = rs_rain[4].text.strip()
    tomorrow_rain_2 = rs_rain[5].text.strip()
    tomorrow_rain_3 = rs_rain[6].text.strip()
    tomorrow_rain_4 = rs_rain[7].text.strip()
    
    day_today = date.today()
    day_tomorrow = date.today() + datetime.timedelta(days=1)
    # 取得結果を格納
    df_1 = ['天気', '最高気温', '最低気温', 
            '降水確率[00-06]', '降水確率[06-12]', '降水確率[12-18]', 
            '降水確率[18-24]']
    df_2 = [today_weather, today_hightemp, 
            today_lowtemp, today_rain_1, today_rain_2, 
            today_rain_3, today_rain_4]
    df_3 = [tomorrow_weather, tomorrow_hightemp, 
            tomorrow_lowtemp, tomorrow_rain_1, tomorrow_rain_2, 
            tomorrow_rain_3, tomorrow_rain_4]
    df_4 = [city_name]
    df_5 = [day_today]
    df_6 = [day_tomorrow]
    df_7 = [today_weather]
    ctx = {
        "df_data": df_1,
        "df_today": df_2,
        "df_tomo": df_3,
        "df_city": df_4,
        "df_day": df_5,
        "df_day2": df_6,
        "df_today_wea": df_7,
    }
    
    return render(request, "weather/getweather.html", ctx)
    