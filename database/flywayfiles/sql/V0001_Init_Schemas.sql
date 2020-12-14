-- Add UUID Extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Create the Schemas
CREATE TABLE department (
    id uuid DEFAULT uuid_generate_v4 (),
    name VARCHAR NOT NULL,
    salary_increment smallint NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE employee (
    id uuid DEFAULT uuid_generate_v4 (),
    first_name VARCHAR NOT NULL,
    last_name  VARCHAR NOT NULL,
    salary smallint NOT NULL,
    PRIMARY KEY (id),
	department_id uuid DEFAULT uuid_generate_v4 (),
    CONSTRAINT department_fk FOREIGN KEY (department_id) REFERENCES department (id)
);

CREATE TABLE updated_salaries (
    employee_id uuid,
    updated_salary smallint NOT NULL,
    PRIMARY KEY (employee_id)
);
