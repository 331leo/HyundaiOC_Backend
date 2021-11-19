from datetime import date, datetime

weekdays_en = {0:"mon", 1:"tue", 2:"wen", 3:"thu", 4:"fri"}
weekdays_kr = {0:"월", 1:"화", 2:"수", 3:"목", 4:"금"}


def now_weekday(kr=False):
    return weekdays_en[datetime.now().weekday()] if not kr else weekdays_kr[datetime.now().weekday()]

def get_date_string():
    now = datetime.now()
    return f"{now.year}년 {now.month}월 {now.day}일 ({now_weekday(kr=True)})"

def current_school_time():
    now = datetime.now().strftime("%H:%M")
    period = -1
    if "07:50"<=now<="08:55":
        period=0
    elif "08:56"<=now<="09:55":
        period=1
    elif "09:56"<=now<="10:55":
        period=2
    elif "10:56"<=now<="11:55":
        period=3
    elif "11:56"<=now<="13:05":
        period=-2 # 점심
    elif "13:06"<=now<="13:55":
        period=4
    elif "13:56"<=now<="14:55":
        period=5
    elif "14:56"<=now<="15:55":
        period=6
    return period

# 7:50 ~ 8:55
# 8:56 ~ 9:55
# 9:56 ~ 10:55
# 10:56 ~ 11:55
# 11:56 ~ 13:05 (점심)
# 13:06 ~ 13:55
# 13:56 ~ 14:55
# 14:56 ~ 15:55
