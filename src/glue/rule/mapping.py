from pyspark.sql.functions import avg, col, expr
import uuid


def department_etl(df):
    dept = df\
        .select('dept_name', 'salary_increment')\
        .groupby('dept_name')\
        .agg(avg("salary_increment").cast('integer').alias("salary_increment"))\
        .withColumnRenamed('dept_name', 'name')\
        .withColumn("id", expr("uuid()"))
    return dept


def employee_etl(df, dept):
    dept = dept.select('id', 'name')\
        .withColumnRenamed('id', 'department_id')
    emp = df\
        .withColumn('salary', col('salary').cast('integer'))\
        .join(dept, df['dept_name']==dept['name'])\
        .select('first_name', 'last_name', 'salary', 'department_id')\
        .withColumn("id", expr("uuid()"))
    return emp


def update_etl(df_dept, df_emp):
    sal_update = df_emp \
        .withColumnRenamed('id', 'employee_id')\
        .join(df_dept, df_emp['department_id']==df_dept['id'])\
        .withColumn('updated_salary', col('salary')*(col('salary_increment')+100)/100)\
        .select('employee_id', 'updated_salary')
    return sal_update
