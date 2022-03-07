import psycopg2
import xlsxwriter
import pandas as pd
import logging


def run_query(query):
    try:
        connection = psycopg2.connect(database="postassgn", user="harshitaagrawal", password="postgres",
                                      host="localhost",
                                      port=5432)
        logging.info("Database Connected....")
        cur = connection.cursor()

        data = cur.execute(query)
        entries = cur.fetchall()
        c1 = []
        c2 = []
        c3 = []

        for entry in entries:
            temp_list = list(entry)
            c1.append(temp_list[0])
            c2.append(temp_list[1])
            c3.append(temp_list[2])

        df = pd.DataFrame({'Employee Number': c1, 'Employee Name': c2, 'Manager Name': c3})
        writer = pd.ExcelWriter('/Users/harshitaagrawal/Desktop/Excel_file_Q1.xlsx')
        df.to_excel(writer, sheet_name='Query1', index=False)
        writer.save()

    except:
        logging.error("There is an error...")

    finally:
        logging.info("I have no issues..")

    connection.close()


if __name__ == "__main__":
    query = "select e1.empno as employee_number," \
            " e1.ename as employee_name, " \
            "e2.ename as manager_name " \
            "from emp e1 " \
            "inner join emp e2 on e1.mgr = e2.empno"
    run_query(query)
