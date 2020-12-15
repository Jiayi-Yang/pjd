# Pumpjack ETL Code Challenge

### Structure

- [Database/FlywayFiles/sql](https://github.com/Jiayi-Yang/pjd/tree/master/Database/FlywayFiles/sql) sql to create database
- [src/glue](https://github.com/Jiayi-Yang/pjd/tree/master/src/glue) glue job for etl
  - `rule/mapping` : etl logic for three tables
  - `config.py`:  environment variables from env file
  - `data_source.py`: function to extract data and load data from/to s3/db
  - `etl_executor.py`: main script for the glue job

### Result

![department](https://github.com/Jiayi-Yang/pjd/blob/master/attachment/department.png)

![employee](https://github.com/Jiayi-Yang/pjd/blob/master/attachment/employee.png)

![updated_salaries](https://github.com/Jiayi-Yang/pjd/blob/master/attachment/updated_salaries.png)



# PostgreSQL Setup

- Reference:https://hub.docker.com/_/postgres

## Pull PostgreSQL Image from Docker Hub

```bash
docker pull postgres
```

## Run PostgreSQL Image

```bas
docker run --name pjd-db -e POSTGRES_DB=abc -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=password -p 5430:5432 -d postgres
```

## Connect PostgreSQL with pgAdmin

- Reference: https://www.pgadmin.org/

#### Step 1: Create Sever

- General: `pjd-db`
- Connection:
  - Host name: `localhost`
  - Port:`5430`
  - Maintenance database:`abc`
  - Username:`admin`
  - Password:`password`

#### Step 2: Create Schema

- Query Tool
- Run `pjd/database/flywayfiles/sql/V0001_Init_Schemas.sql` in the Query Tool

## DB Migrate

#### Step 1: Pull Flyway Docker Image

```bash
docker pull flyway/flyway
```

#### Step 2: Run Docker Flyway Migrate

- Another Option Without Modifiy Config File

```bash
docker run --rm -v /Users/jay/Documents/project/pjd/Database:/flyway/sql flyway/flyway -url=jdbc:postgresql://172.17.0.4:5432/abc -user=admin -password=password migrate
```



# Glue Setup with PyCharm Professional

- Reference: https://aws.amazon.com/blogs/big-data/developing-aws-glue-etl-jobs-locally-using-a-container/

## Pull Docker Image

```bash
docker pull amazon/aws-glue-libs:glue_libs_1.0.0_image_01
```

## Pycharm Setup

- Details: Follow this tutorial: https://aws.amazon.com/blogs/big-data/developing-aws-glue-etl-jobs-locally-using-a-container/ ***Setting up the Docker image with PyCharm Professional*** Section

- Step 1: Project Structure 

  - Add Content Root - `PyGlue.zip`
  - Mark `src` as `Sources`

- Step 2: Add Python Interpreter

  - Choose Docker
  - Server: Docker-Glue
  - Image name: `amazon/aws-glue-libs:glue_libs_1.0.0_image_01`
  - Python Interpreter path:python

- Step 3: Add Configuration

  - Python

  - Name: `etl_executor`

  - Script Path: `/Users/jay/Documents/project/pjd/src/glue/etl_executor.py`

  - Environment Variables

    ```bash
    PYTHONPATH=/home/aws-glue-libs/awsglue.zip:/home/spark-2.4.3-bin-spark-2.4.3-bin-hadoop2.8/python/lib/pyspark.zip:/home/spark-2.4.3-bin-spark-2.4.3-bin-hadoop2.8/python/lib/py4j-0.10.7-src.zip:/home/spark-2.4.3-bin-spark-2.4.3-bin-hadoop2.8/python
    ```

  - Docker container settings:+

    - Container path:`/root/.aws`
    - Host path:`/Users/jay/.aws`
    - √ Read Only

  - EnvFile

    - Enable EnvFile
    - `+` .envfile:`etl_env.env`