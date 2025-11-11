thonfrom datetime import datetime

def format_date(date_str):
    return datetime.fromisoformat(date_str[:-1]).date()