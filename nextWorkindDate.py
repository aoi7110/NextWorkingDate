import json
import datetime

# 日本の祝日を設定（必要に応じて更新）
JAPANESE_HOLIDAYS = {
    "2025-01-01",  # 元日
    "2025-01-13",  # 成人の日
    "2025-02-11",  # 建国記念の日
    "2025-02-23",  # 天皇誕生日
    "2025-03-20",  # 春分の日
    "2025-04-29",  # 昭和の日
    "2025-05-03",  # 憲法記念日
    "2025-05-04",  # みどりの日
    "2025-05-05",  # こどもの日
    "2025-07-21",  # 海の日
    "2025-08-11",  # 山の日
    "2025-09-15",  # 敬老の日
    "2025-09-23",  # 秋分の日
    "2025-10-13",  # 体育の日
    "2025-11-03",  # 文化の日
    "2025-11-23",  # 勤労感謝の日
    "2025-12-23",  # 天皇誕生日（2025年以降は変更の可能性あり）
}

def get_next_business_day(start_date):
    """翌営業日を取得する"""
    next_day = start_date + datetime.timedelta(days=1)
    
    while next_day.weekday() >= 5 or next_day.strftime("%Y-%m-%d") in JAPANESE_HOLIDAYS:
        next_day += datetime.timedelta(days=1)
    
    return next_day.strftime("%Y-%m-%d")

def lambda_handler(event, context):
    """AWS Lambda エントリポイント"""
    today = datetime.date.today()
    next_business_day = get_next_business_day(today)

    return {
        "statusCode": 200,
        "body": json.dumps({"next_business_day": next_business_day})
    }