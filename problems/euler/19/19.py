from itertools import cycle

months = { 
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31 
} 

def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False

def days_of_year(year):
    all_days = []
    date_str = "{}-{:02d}-{:02d}"
    for month, days in months.iteritems():
        for day in range(1,days+1):
            all_days.append(date_str.format(year, month, day))
        if month == 2 and is_leap_year(year):
            all_days.append(date_str.format(year, month, 29))
    return all_days

def get_dates_between(start_year, end_year):
    days = []
    for year in range(start_year, end_year + 1):
        days.extend(days_of_year(year))
    return days

def main():
    date = get_dates_between(1900, 2000)
    weekdays = ["Mo","Di","Mi","Do","Fr","Sa","So"]
    relevant_dates = [(d, w) for d, w in zip(date, cycle(weekdays))
                             if not d.startswith('1900')
                                and d.endswith('01')
                                and w == 'So']
    print len(relevant_dates)

if __name__ == "__main__":
    main()
