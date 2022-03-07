import pandas as pd
from sqlalchemy import create_engine
import logging

engine = create_engine("postgresql+psycopg2://harshitaagrawal:postgres@localhost:5432/postassgn")


def read_sheets(data, file):
    try:
        if data == 'Q2':
            df = pd.read_excel(file, 'Q2')
            return df

    except:
        print("Execution unsuccessful. Exception occurred.")
        logging.error("There is an error...")

    finally:
        print("Execution Successful.")
        logging.info("I have no issues..")


def convert_to_excel(df):
    writer = pd.ExcelWriter('/Users/harshitaagrawal/Desktop/Excel_file_Q4.xlsx')
    df.to_excel(writer, sheet_name='Excel_file_Q4', index=False)
    writer.save()


with pd.ExcelFile('sheet_q2.xlsx') as xls:
    for sheet_name in xls.sheet_names:
        new_df = read_sheets(sheet_name, xls)

temp1_df = new_df.groupby(['Dept Name', 'Dept Number']).agg(
    Total_Compensation=pd.NamedAgg(column='Total Compensation', aggfunc="sum")
).reset_index()

# print(temp1_df)

convert_to_excel(temp1_df)
