import csv, sqlite3
import os

sqlite_db_path = "data.db"
# if db doesn't exist, create it

if not os.path.exists(sqlite_db_path):
    open(sqlite_db_path, "w").close()


con = sqlite3.connect(sqlite_db_path)  # change to 'sqlite:///your_filename.db'
cur = con.cursor()
cur.execute(
    "CREATE TABLE cars (DealerId INT,vin TEXT,year INT,price INT,make TEXT,model TEXT,style TEXT,transmission TEXT,engine TEXT,mileage INT,color TEXT,stocknum TEXT,driveType TEXT,vehicleListPrice INT,PhotoURLs TEXT);"
)

with open("data.csv", "r") as fin:
    dr = csv.DictReader(fin)
    to_db = [
        (
            i["DealerId"],
            i["vin"],
            i["year"],
            i["price"],
            i["make"],
            i["model"],
            i["style"],
            i["transmission"],
            i["engine"],
            i["mileage"],
            i["color"],
            i["stocknum"],
            i["driveType"],
            i["vehicleListPrice"],
            i["PhotoURLs"],
        )
        for i in dr
    ]

column_names = [
    "DealerId",
    "vin",
    "year",
    "price",
    "make",
    "model",
    "style",
    "transmission",
    "engine",
    "mileage",
    "color",
    "stocknum",
    "driveType",
    "vehicleListPrice",
    "PhotoURLs",
]

sql_query = f"INSERT INTO cars ({', '.join(column_names)}) VALUES ({', '.join(['?']*len(column_names))});"

cur.executemany(sql_query, to_db)
con.commit()
con.close()
