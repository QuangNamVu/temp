# import;
delete from user;
delete from teacher;
delete from student;
delete from subject;
.mode csv
.import sample/user.csv user
.import sample/teacher.csv teacher
.import sample/student.csv student
select * from teacher;
select * from user;
select * from student;

delete from teacher;
# Create table;
PRAGMA foreign_keys=off;
drop table user;
CREATE TABLE IF NOT EXISTS user(
USER_NAME         UNIQUE NOT NULL,
PASSWORD          TEXT,
PERMISSION        INT
);

drop table student;
CREATE TABLE IF NOT EXISTS student(
USER_NAME         TEXT PRIMARY KEY   NOT NULL,
NAME              TEXT,
DOB               DATETIME,
ADDRESS           TEXT,
CONSTRAINT fk_id
    FOREIGN KEY (USER_NAME)
    REFERENCES user(USER_NAME)
    ON DELETE CASCADE
);

drop table teacher;
CREATE TABLE IF NOT EXISTS teacher(
USER_NAME         TEXT    NOT NULL,
NAME              TEXT    NOT NULL,
DOB               DATETIME,
PHONE             TEXT,
ADDRESS           TEXT,
CONSTRAINT fk_id
    FOREIGN KEY (USER_NAME)
    REFERENCES user(USER_NAME)
    ON DELETE CASCADE
);

drop table subject;
CREATE TABLE subject(
MSMH          TEXT NOT NULL,
MSSV          TEXT      NOT NULL,
GV_ID         TEXT      NOT NULL,
TICH_LUY      REAL,
IS_PASS       NOT NULL DEFAULT 0,
PRIMARY KEY (MSMH,MSSV, GV_ID));


# PRAGMA
PRAGMA foreign_keys=on;
select NAME from teacher where USER_NAME == 'S0951';
select password from user where USER_NAME == 'S0951';
delete from user where USER_NAME == 'S0951';
select NAME from teacher where USER_NAME == 'S0951';

# Schema;
.schema user
.schema teacher
.schema student
.schema subject
# Insert;
INSERT INTO user (USER_NAME,PASSWORD,PERMISSION) 
VALUES ('NguyenVanB', 'password', 'teacher');
INSERT INTO teacher (USER_NAME,NAME,ADDRESS,DOB,DESCRIBE) 
VALUES ('NguyenVanB', 'Nguyen Van Binh','Dang Van Bi', '2007-18-3', 'motion');
## Student;
INSERT INTO student (MSSV,USE_NAME,PASS,DOB) 
VALUES (1511111, 'Tran Van A', 'password', '2007-18-3');
## Subject;
INSERT INTO student (MSSV,USE_NAME,PASS,DOB) 
VALUES (1511111, 'Tran Van A', 'password', '2007-18-3');

# Update;
update user set PASSWORD = 'std' where USER_NAME == 1710001;
select PERMISSION from user where USER_NAME == 'admin' AND PASSWORD == 'a';
# View select all;
select * from user;
select * from teacher;
select * from student;
DELETE FROM user WHERE USER_NAME == 'NguyenVanB';
# Drop;
drop table USER;
# Export sqlite to csv;
delete from user;
delete from teacher;
delete from student;
.headers on
.mode csv
.output sample/user.csv 
select * from user;
.output stdout

.output sample/teacher.csv 
select * from teacher;
.output stdout

.output sample/student.csv 
select * from student;
.output stdout

.headers off
# exit quit
.quit
C-D

# Link;
https://www.sqlite.org/cli.html
# List all table;
.tables
# search ;
SELECT * FROM USER WHERE USER_NAME LIKE '%17%';
# foreign key;
ALTER TABLE user ADD FOREIGN KEY (`Id`) REFERENCES nhan_vien(`GV_ID`);

# CASCADE
drop table departments;
CREATE TABLE departments
( department_id INTEGER PRIMARY KEY AUTOINCREMENT,
  department_name VARCHAR
);

drop table employees;
CREATE TABLE employees
( employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
  last_name VARCHAR NOT NULL,
  first_name VARCHAR,
  department_id INTEGER,
  CONSTRAINT fk_departments
    FOREIGN KEY (department_id)
    REFERENCES departments(department_id)
    ON DELETE CASCADE
);

INSERT INTO departments VALUES (30, 'HR');
INSERT INTO departments VALUES (999, 'Sales');

INSERT INTO employees VALUES (10000, 'Smith', 'John', 30);
INSERT INTO employees VALUES (10001, 'Anderson', 'Dave', 999);

select * from employees;
select * from departments;
PRAGMA foreign_keys=on;

delete from departments where department_id == 30;
select * from employees;

#cout
      cout << setw(40) << left  << (firstName + " " + lastName) << " "
           << setw(6)  << right << finalExam << " "
           << setw(6)  << right << fixed << setprecision(2) << finalAvg << " "
           << setw(7)  << right << letterGrade << "\n";
