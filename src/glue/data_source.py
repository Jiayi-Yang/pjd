from awsglue.dynamicframe import DynamicFrame
from glue.config import *


def from_s3(glueContext):
    return glueContext.read.csv(f"s3://{BUCKET_NAME}/{INPUT_FILE_NAME}", header="true")


def from_db(glueContext, table_name: str):
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
    # write_options = {
    #     "url": f"jdbc:postgresql://{DB_IP}:{DB_PORT}/{DB_NAME}",
    #     "dbtable": f"{table_name}",
    #     "user": f"{DB_USER}",
    #     "password": f"{DB_PASSWORD}"
    # }
    # # Convert DF to DynamicFrame
    # db_df_dynamic = DynamicFrame.fromDF(db_df, glueContext, "df_dynamic")
    # # Load Into DB
    # glueContext.write_from_options(frame_or_dfc=db_df_dynamic,
    #                                connection_type="postgresql",
    #                                connection_options=write_options)

