import datetime


day = datetime.datetime.now()

ymd_hm = day.strftime("%y%m%d_%H%M")
    
print(ymd_hm)