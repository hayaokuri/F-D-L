import requests
import json

from datetime import datetime, timedelta, timezone
tokyo_tz = timezone(timedelta(hours=9))

class mytime:

    def GetTimeStamp():
        return (int)(datetime.now(tz=tokyo_tz).timestamp())

def GetGachaSubIdFP():
    url = "https://raw.githubusercontent.com/DNNDHH/GSubList/Main/update.json"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
    }
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    gachaList = response.json()
    timeNow = mytime.GetTimeStamp()
    priority = 0
    goodGacha = {}

    for gacha in gachaList:
        openedAt = gacha["openedAt"]
        closedAt = gacha["closedAt"]

        # 修正逻辑运算符
        if openedAt <= timeNow and timeNow <= closedAt:
            p = int(gacha["priority"])
            if p > priority:
                priority = p
                goodGacha = gacha

    # 检查是否找到了合适的 gacha
    if not goodGacha:
        return None  
    
    # 确认 'id' 键是否存在
    if "id" not in goodGacha:
        return None  

    return str(goodGacha["id"])
