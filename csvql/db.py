import duckdb
from pandas import DataFrame
from typing import Dict


class CSVdb:
    def __init__(self):
        self.con = duckdb.connect(database="csvql.duckdb", read_only=False)
    def close(self):
        self.con.close()
    def checkIfTableExists(self,table:str):
        self.con.execute("select count(*) from information_schema.tables where table_name = '{}'".format(table))
        return self.con.fetchall()[0][0]
    def getTables(self):
        self.con.execute("show tables")
        return self.con.fetchdf()
    def createTable(self, table: DataFrame, name: str):
        try:
            df_table = table
            self.con.execute("CREATE TABLE {} AS SELECT * FROM df_table".format(name))
            return {"Status": 1, "Message": "Table Created Successfully"}
        except Exception as e:
            return {"Status": 0, "Message": str(e)}
    def runQuery(self,query:str):
        self.con.execute(query)
        return self.con.fetchdf()
