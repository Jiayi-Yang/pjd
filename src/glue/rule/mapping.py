from pyspark.sql.functions import avg, col, expr


def department_etl(df):
    """ department etl
    Return Columns
    --------------
        id:uuid
        name:str
        salary_increment:int
    """
    dept = df \
        .select('dept_name', 'salary_increment') \
        .groupby('dept_name') \
        .agg(avg("salary_increment").cast('integer').alias("salary_increment")) \
        .withColumnRenamed('dept_name', 'name') \
        .withColumn("id", expr("uuid()"))
    return dept


def employee_etl(df, dept):
    """ employee etl

    Return Columns
    --------------
        id:uuid
        first_name:str
        last_name:str
        salary:double
        department_id:uuid (fk from department.id)
    """
    dept = dept.select('id', 'name') \
        .withColumnRenamed('id', 'department_id')
    emp = df \
        .withColumn('salary', col('salary').cast('double')) \
        .join(dept, df['dept_name'] == dept['name']) \
        .select('first_name', 'last_name', 'salary', 'department_id') \
        .withColumn("id", expr("uuid()"))
    return emp


def update_etl(df_dept, df_emp):
    """ updated_salaries etl

    Return Columns
    --------------
        employee_id:uuid (from employee.id)
        updated_salary:double
    """
    sal_update = df_emp \
        .withColumnRenamed('id', 'employee_id') \
        .join(df_dept, df_emp['department_id'] == df_dept['id']) \
        .withColumn('updated_salary', col('salary') * (col('salary_increment') + 100) / 100) \
        .select('employee_id', 'updated_salary')
    return sal_update
