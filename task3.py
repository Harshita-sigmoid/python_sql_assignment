import pandas as pd
from sqlalchemy import create_engine
import logging

engine = create_engine("postgresql+psycopg2://harshitaagrawal:postgres@localhost:5432/postassgn")


def read_sheets(data, file):
    try:
        if data == 'Q2':
            df = pd.read_excel(file, 'Q2')
            df.to_sql(name='new_compensation', con=engine, if_exists='append', index=False)

    except:
        print("Execution unsuccessful. Exception occurred.")
        logging.error("There is an error...")

    finally:
        print("Execution Successful.")
        logging.info("I have no issues..")


with pd.ExcelFile('sheet_q2.xlsx') as xls:
    for sheet_name in xls.sheet_names:
        read_sheets(sheet_name, xls)
