from datetime import datetime

def calculate_days_between_dates(date1, date2):
    date_format = "%Y-%m-%d"
    a = datetime.strptime(date1, date_format)
    b = datetime.strptime(date2, date_format)
    delta = b - a
    return delta.days

def main():
    date1 = "2023-01-01"
    date2 = "2023-12-31"
    days = calculate_days_between_dates(date1, date2)
    print(f"Days between {date1} and {date2}: {days}")

if __name__ == "__main__":
    main()
