from datetime import datetime

def parse_date(date_string: str) -> datetime:
    return datetime.strptime(date_string, "%Y-%m-%d")