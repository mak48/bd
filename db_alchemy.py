import time
from configuration import *
from sqlalchemy import create_engine, text

def alchemy():
    answers = []
    engine = create_engine("sqlite:///mydatabase.db")
    conn = engine.connect()
    for i in range(k):
        all = 0
        for j in range(repeat):
            a = time.perf_counter()
            conn.execute(text(queries[i]))
            b= time.perf_counter()
            all += b - a
        answers.append(all/repeat)
    conn.close()
    engine.dispose()
    print("sqlalchemy:", answers[0], answers[1], answers[2], answers[3])