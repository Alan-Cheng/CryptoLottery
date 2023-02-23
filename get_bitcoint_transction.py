import requests
import json
import time
import sqlite3




def time_transfer(timestamp):
    struct_time = time.localtime(timestamp)
    time_string = time.strftime("%Y-%m-%d %H:%M:%S", struct_time).replace("-","/")
    return time_string



def get_txs_data(source_addr, dest_addr):
    url = 'https://blockchain.info/rawaddr/' + source_addr
    response = requests.get(url)
    data = response.json()  #是字典檔
    result = json.dumps(data, indent=4, sort_keys=True)

    txs_list = []
    for tx in data['txs']:
        txs_list.append([tx['hash'], time_transfer(tx['time']), tx['inputs'][0]['prev_out']['addr'], tx['out'][0]['addr'], tx['out'][0]['value']*0.00000001])
    
    for tx in txs_list:
        if(tx[2] == source_addr and tx[3] == dest_addr and tx[4] >= 0.0001):
            conn = sqlite3.connect('lottery_project_DB.db')
            cur = conn.cursor()
            cur.execute('CREATE TABLE IF NOT EXISTS transaction_record (yyyymmdd DATE PRIMARY KEY ,\
                source_addr TEXT, dest_addr TEXT,\
                    amount TEXT)')
            cur.execute("INSERT INTO transaction_record (yyyymmdd, source_addr, dest_addr,\
                        amount) \
                        values('{}','{}','{}',{});".format(tx[1], tx[2], tx[3], tx[4]))


            conn.commit()
            conn.close()

