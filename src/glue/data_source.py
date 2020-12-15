from glue.config import *


def from_s3(glueContext):
    """ extract csv file from s3 """
    return glueContext.read.csv(f"s3://{BUCKET_NAME}/{INPUT_FILE_NAME}", header="true")


def from_db(glueContext, table_name: str):
    """ extract data from postgresql table and convert to dataframe """
    connection_options = {
        "url": f"jdbc:postgresql://{DB_IP}:{DB_PORT}/{DB_NAME}",
        "dbtable": f"{table_name}",
        "user": f"{DB_USER}",
        "password": f"{DB_PASSWORD}"
    }

    df_db = glueContext.create_dynamic_frame.from_options(
        connection_type="postgresql",
        connection_options=connection_options)

    return df_db.toDF()


def to_db(db_df, table_name: str):
    """ load dataframe into postgresql """
    url = f"jdbc:postgresql://{DB_IP}:{DB_PORT}/{DB_NAME}"
    properties = {
        "user": f"{DB_USER}",
        "password": f"{DB_PASSWORD}",
        "stringtype": "unspecified"
    }
    db_df.write.jdbc(
        url=url,
        table=f"{table_name}",
        mode="append",
        properties=properties)

