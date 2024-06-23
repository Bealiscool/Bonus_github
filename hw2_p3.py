def leap_year(year):
    if year % 4 != 0:
        return False
    else:
        if year % 100==0:
            if year % 400==0:
                return True
            else:
                return False
        else:
            return True

def day_of_week(year, month, day):
    if month<=2:
        month=month+12
        year=year-1
    century=year//100
    year_th=year%100
    
    week_day=(day+(13*(month+1)//5)+year_th+(year_th//4)+(century//4)-(2*century))%7-1
    return week_day
def month_day(year, month):
    if month==1:
        return 31
    elif month==2:
        if leap_year(year)==True:
            return 29
        else:
            return 28
    elif month==3:
        return 31
    elif month==4:
        return 30
    elif month==5:
        return 31
    elif month==6:
        return 30
    elif month==7:
        return 31
    elif month==8:
        return 31
    elif month==9:
        return 30
    elif month==10:
        return 31
    elif month==11:
        return 30
    elif month==12:
        return 31
def print_calendar(year, month):
    print("Sun Mon Tue Wed Thu Fri Sat")
    start_day=day_of_week(year, month, 1)
    days_in_month=month_day(year, month)
    today=1
    for i in range(6):
        for j in range(7):
            if i==0 and j<start_day:
                print("    ", end="")
            elif today<=days_in_month:
                if today<10:
                    print("0",end="")
                    print(today, end="  ")
                else:
                    print(today, end="  ")
                today=today+1
            else:
                print("  ",end="")
            
        print("")

year_str=input("Please input Year")
month_str=input("Please input Month")

year=int(year_str)
month=int(month_str)
print(leap_year(year))
print_calendar(year,month)