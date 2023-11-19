import re

date_patterns = [
    r'(?P<day>\d{2})[./-](?P<month>\d{2})[./-](?P<year>\d{4})',
    r'(?P<year>\d{4})[./-](?P<month>\d{2})[./-](?P<day>\d{2})'  ]

def normalize_date(date_str):
    for pattern in date_patterns:
        match = re.match(pattern, date_str)
        if match:
            day = match.group('day')
            month = match.group('month')
            year = match.group('year')
            return f'{year}-{month.zfill(2)}-{day.zfill(2)}'
    return None

with open('dates.txt', 'r') as file:
    dates = file.readlines()


for date in dates:
    date = date.strip()
    normal_date = normal_date(date)
    if normal_date:
        print(f" {normal_date}")
    else:
        print(f"Дата '{date}' не відповідає жодному відомому формату.")