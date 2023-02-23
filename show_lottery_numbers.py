import datetime
import sqlite3
import time

def show_lottery_numbers():
        localtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        date_today = datetime.date.today()
        today_date = str(date_today).replace("-", "/")
        yes_date = str(date_today - datetime.timedelta(days=1)).replace("-", "/")


        if localtime < today_date+" 20:00:00":
                conn = sqlite3.connect('lottery_project_DB.db')
                cur = conn.cursor()
                cur.execute("SELECT number1, number2, number3, number4, number5 \
                        FROM lottery_numbers \
                        WHERE yyyymmdd ='{}';".format(yes_date))
                rows = cur.fetchall()
                conn.close()

                for row in rows:
                        message  = ("現在時間為:\n"+localtime+"\n"+"\n"\
                                "今日尚未開獎\n前期({})樂透號碼為：\n".format(yes_date)\
                                +str(list(row)))
                        return message
                        
        else:
                conn = sqlite3.connect('lottery_project_DB.db')
                cur = conn.cursor()
                cur.execute("SELECT number1, number2, number3, number4, number5 \
                        FROM lottery_numbers \
                        WHERE yyyymmdd ='{}';".format(today_date))
                rows = cur.fetchall()
                conn.close()

                for row in rows:
                        message  = ("現在時間為\n"+localtime+"\n"+"\n"\
                                "今日已開獎，本期樂透號碼為：\n"\
                                    +str(list(row)))
                        return message
