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

### Step 2: Create Schema

- Query Tool
- Run `pjd/database/flywayfiles/sql/V0001_Init_Schemas.sql` in the Query Tool