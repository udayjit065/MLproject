import os 
import sys 
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd 

from dotenv import load_dotenv

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")


def read_sql_data():
    logging.info("Reading SQL database started")
    try :
        mydb=pymysql.conect(
            host =host,
            user = user,
            password = password,
            db = db,
        )
        logging.info("connection established"mydb)
        df = pd.read_sql_query('Select * from students',mydb)
        print(df.head)
    except Exception as ex :
        raise CustomException(ex)