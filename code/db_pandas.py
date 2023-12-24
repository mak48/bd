import time
from configuration import *
from sqlalchemy import create_engine
import pandas

def panda():
    answers = []
    engine = create_engine("sqlite:///mydatabase.db")
    for i in range(k):
        all = 0
        for j in range(repeat):
            a= time.perf_counter()
            pandas.read_sql(queries[i], con=engine)
            b = time.perf_counter()
            all += b -a
        answers.append(all/repeat)
    engine.dispose()
    print("pandas:", answers[0], answers[1], answers[2], answers[3])