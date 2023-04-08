import pandas as pd
from datetime import date,datetime
import mySql_fetch as sql


def create_csv():
    now = date.today()
    res = sql.today(now)
    sorting(res)

def sorting(res):
    df=pd.DataFrame(res)
    sorted_df = df.sort_values(by=["rollno"], ascending=True)
    sorted_df['Time'] = sorted_df['Time'].apply(lambda x: x.time())
    #sorted_df = sorted_df.assign(Time= lambda x : x.time())
    sorted_df.to_csv('present.csv', index=False)

def markAttendance(name):
    dates = date.today()
    now = datetime.now()
    th  =now.strftime('%H')
    tm = now.strftime('%M')
    m = 1
    if int(th)<9 or (int(th)==9) and (int(tm)<=00):
        m = 1
    else:
        m = -1
    
    attendance = "Present" if m>0  else "Late" 

    sql.mark_attend(name , dates , now , attendance)