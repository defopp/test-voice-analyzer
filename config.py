import os
from dotenv import load_dotenv

load_dotenv()
uri = os.getenv("URI")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
domain = os.getenv("DOMAIN")

sql_host = os.getenv("host")
sql_user = os.getenv("user")
sql_password = os.getenv("password")
sql_database = os.getenv("database")
