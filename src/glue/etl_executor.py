from glue import sc, glueContext
import logging
from glue.data_source import from_s3, from_db, to_db
from glue.rule.mapping import department_etl, employee_etl, update_etl

if __name__ == '__main__':
    # Spark Logger
    sc.setLogLevel("WARN")

    logging.info('Department and Employee ETL Starts')

    # Extract data from S3
    df = from_s3(glueContext)

    # Department ETL
    dept = department_etl(df)

    # Employee ETL
    emp = employee_etl(df, dept)

    # Load Department and Employee into DB
    to_db(dept, 'department')
    to_db(emp, 'employee')
    logging.info('Department and Employee ETL Ends')

    logging.info('Update Salary ETL Starts')
    # Extract from DB
    df_dept = from_db(glueContext, 'department')
    df_emp = from_db(glueContext, 'employee')

    # Update Salary
    update_salary = update_etl(df_dept, df_emp)

    # Load to DB
    to_db(update_salary, 'updated_salaries')
    logging.info('Update Salary ETL Ends')

