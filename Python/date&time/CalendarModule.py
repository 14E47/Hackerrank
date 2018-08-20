import calendar

l = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
imonth, iday, iyear = map(int,input().split())
n = calendar.weekday(iyear,imonth,iday)
print(l[n])
