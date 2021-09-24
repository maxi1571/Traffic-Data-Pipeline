import os
import pandas as pd
import mysql.connector
import numpy as np
from mysql.connector import Error


class DBoperations:

    def DBConnect(self,dbName=None):
        conn=mysql.connector.connect(host='localhost',port="3306", user='root', password="",
                            database=dbName)
        cur = conn.cursor()
        return conn, cur


    def createDB(self,dbName: str) -> None:
        """

        Parameters
        ----------
        dbName :
            str:
        dbName :
            str:
        dbName:str :


        Returns
        -------

        """
        conn, cur = DBoperations.DBConnect(self)
        cur.execute(f"CREATE DATABASE IF NOT EXISTS {dbName};")
        conn.commit()
        cur.close()

    def createTables(self,dbName: str) -> None:
        """

        Parameters
        ----------
        dbName :
            str:
        dbName :
            str:
        dbName:str :


        Returns
        -------

        """
        conn, cur = DBoperations.DBConnect(self,'traffic_data')
        sqlFile = './schema.sql'
        fd = open(sqlFile, 'r')
        readSqlFile = fd.read()
        fd.close()

        sqlCommands = readSqlFile.split(';')

        for command in sqlCommands:
            try:
                res = cur.execute(command)
            except Exception as ex:
                print("Command skipped: ", command)
                print(ex)
        conn.commit()
        cur.close()

        return




    def insert_to_table(self,dbName: str, df: pd.DataFrame, table_name: str) -> None:
        """

        Parameters
        ----------
        dbName :
            str:
        df :
            pd.DataFrame:
        table_name :
            str:
        dbName :
            str:
        df :
            pd.DataFrame:
        table_name :
            str:
        dbName:str :

        df:pd.DataFrame :

        table_name:str :


        Returns
        -------

        """
        conn, cur = DBoperations.DBConnect(self,'traffic_data')

    

    
        for _, row in df.iterrows():
            sqlQuery = f"""INSERT INTO {table_name}
            (ID,Fwy,Dir,District,County,City,State_PM,Abs_PM,Latitude,Longitude,Length,Type,Lanes,Name,User_ID_1,User_ID_2,User_ID_3,User_ID_4)
            VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s);"""




            data = (row[0], row[1], row[2], row[3], (row[4]), (row[5]), row[6], row[7], row[8], row[9], row[10], row[11],
                    row[12], row[13],row[14], row[15],row[16], row[17])

            try:
                # Execute the SQL command
                cur.execute(sqlQuery, data)
                # Commit your changes in the database
                conn.commit()
                print("Data Inserted Successfully")
            except Exception as e:
                conn.rollback()
                print("Error: ", e)
        return
 
    
if __name__ == "__main__":
    db1 = DBoperations()
    db1.createDB('traffic_data')
    db1.createTables('stations')
    df = pd.read_csv('./data/I80_stations.csv')
    df=df.fillna(0)
    db1.insert_to_table('traffic_data', df=df, table_name='stations')

