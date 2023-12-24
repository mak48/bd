import time
from configuration import *
import psycopg2
import pandas
from sqlalchemy import create_engine

d = pandas.read_csv(csv_file)
d["tpep_pickup_datetime"] = pandas.to_datetime(d["tpep_pickup_datetime"])
d["tpep_dropoff_datetime"] = pandas.to_datetime(d["tpep_dropoff_datetime"])
d = d.drop(columns=["Airport_fee"])
def copg():
    answers = []
    eng = create_engine(path)
    connection = psycopg2.connect(**databasa)
    d.to_sql("trips", eng, if_exists="replace")
    cursor = connection.cursor()
    for i in range(k):
        all = 0
        for j in range(repeat):
            a= time.perf_counter()
            cursor.execute(queries[i].replace('''STRFTIME('%Y', "tpep_pickup_datetime")''', '''EXTRACT(year FROM "tpep_pickup_datetime")'''))
            b= time.perf_counter()
            all +=b-a
        answers.append(all/repeat)
    cursor.close()
    connection.close()
    eng.dispose()
    print("psycopg2:", answers[0], answers[1], answers[2], answers[3])