import datetime
l=(20,2,2025)
t=(31,1,2024)

date1=datetime.date(l[2],l[1], l[0])
date2=datetime.date(t[2],t[1], t[0])
print(abs(date1-date2).days)
    
        
    
    
