import pymysql
import sys
import os
sys.path.append(os.getcwd())
from main import sql_database,sql_host,sql_password,sql_user

class MySql_Handler:

    def __init__(self,sql_user:str,sql_password:str,sql_database:str,sql_host:str):
        self.user = sql_user
        self.password = sql_password
        self.database = sql_database
        self.host = sql_host
    
    
    
    def data_in(self,filename:str,was_in:list):
        filename=filename+".mp3"

        try:                 #CONNECT
            self.connection = pymysql.connect(
                                host=self.host,
                                user=self.user,
                                password=self.password,
                                database=self.database,
                                cursorclass=pymysql.cursors.DictCursor)
            print("[MySQL]Connect START[OK]")

            with self.connection.cursor() as cursor:
                in_value = ""
                for i in was_in:
                    in_value += f"{i}."

                print(f"[MySQL]{filename} / {in_value}")
                add_wasin_value = f"UPDATE cdr SET userfield='{in_value}' WHERE filename='{filename}'"
                cursor.execute(add_wasin_value)
                self.connection.commit()
                print("[MySQL]Commit ACCEPT[OK]")
            
        except Exception as ex:
            print("[MySQL]connection ERROR[NOT OK]")
            print(ex)
        finally:
            self.connection.close()
            print("[MySQL]Connect CLOSE[OK]")

        


    



if __name__ == "__main__":
    # db = MySql_Handler(sql_user,sql_password,sql_database,sql_host)
    # db.data_in(None,["мрт","нет","да","прием"])
    pass    