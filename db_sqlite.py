import time
import pandas
from configuration import *
import sqlite3

d = pandas.read_csv(csv_file)
d["tpep_pickup_datetime"] = pandas.to_datetime(d["tpep_pickup_datetime"])
d["tpep_dropoff_datetime"] = pandas.to_datetime(d["tpep_dropoff_datetime"])
d = d.drop(columns=["Airport_fee"])
conn = sqlite3.connect("mydatabase.db")
d.to_sql("trips", conn, if_exists="replace")
cursor = conn.cursor()

def lite():
    answers = []
    for i in range(k):
        all = 0
        for j in range(repeat):
            a= time.perf_counter()
            cursor.execute(queries[i])
            b = time.perf_counter()
            all += b-a
        answers.append(all/repeat)
    cursor.close()
    conn.close()
    print("sqlite:", answers[0], answers[1], answers[2], answers[3])