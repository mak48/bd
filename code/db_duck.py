import time
from configuration import *
import duckdb

def duck():
    answers = []
    duckdb.install_extension("sqlite")
    conn = duckdb.connect()
    conn.execute('CREATE TABLE trips AS FROM read_csv_auto(?);',(csv_file,))
    cursor = conn.cursor()
    for i in range(k):
        total = 0
        for j in range(repeat):
            a = time.perf_counter()
            cursor.execute(queries[i])
            b = time.perf_counter()
            total += b - a
        answers.append(total / repeat)
    cursor.close()
    conn.close()
    print("duckdb:", answers[0], answers[1], answers[2], answers[3])