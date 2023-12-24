#input information
csv_file = "C:\\Users\\makov\\Downloads\\nyc_yellow_tiny.csv"
databasa = {"dbname": "postgres", "user": "postgres", "password": "password", "host": "localhost", "port": 5432}
path = "postgresql://postgres:password@localhost:5432/postgres"
repeat = 5
k = 4
queries = [
    """SELECT "VendorID", COUNT(*)
        FROM trips GROUP BY 1;""",
    """SELECT "passenger_count", AVG("total_amount")
       FROM trips GROUP BY 1;""",
    """SELECT "passenger_count", STRFTIME('%Y', "tpep_pickup_datetime"), COUNT(*)
       FROM trips GROUP BY 1, 2;""",
    """SELECT "passenger_count", STRFTIME('%Y', "tpep_pickup_datetime"), ROUND("trip_distance"), COUNT(*)
       FROM trips GROUP BY 1, 2, 3 ORDER BY 2, 4 DESC;""",
]