import db_alchemy
import db_duck
import db_pandas
import db_psycopg
import db_sqlite

print("print a subd\n(postgresql, sqlite, duckdb, pandas, or sqlalchemy)")
lib = input()

while (1):
    print('wait a minute...')
    if (lib=="postgresql"):
        db_psycopg.copg()
    elif (lib=="sqlite"):
        db_sqlite.lite()
    elif (lib=="pandas"):
        db_pandas.panda()
    elif (lib=="duckdb"):
        db_duck.duck()
    elif (lib=="sqlalchemy"):
        db_alchemy.alchemy()
    else:
        print("wrong")
    print("next")
    lib = input()