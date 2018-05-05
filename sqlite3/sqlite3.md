INSERT INTO object (MSMH, MSSV, GV_ID, DIEM, TIN_CHI, IS_PASS)
VALUES ('CC01','1712346','S1951','7.5', '3', 1);

INSERT INTO subject (MSMH, NAME) 
VALUES ('CC01','mo hinh hoa');
# import;
delete from user;
delete from teacher;
delete from student;
delete from subject;
delete from object;
.mode csv
.import /home/coc/sqlite3/sample/user.csv user
.import /home/coc/sqlite3/sample/teacher.csv teacher
.import /home/coc/sqlite3/sample/student.csv student
.import /home/coc/sqlite3/sample/object.csv  object
.import /home/coc/sqlite3/sample/subject.csv subject
select * from object;
select * from subject;

delete from teacher;
# Create table;
drop table user;
drop table student;
drop table teacher;

CREATE TABLE  user(
USER_NAME         UNIQUE NOT NULL,
PASSWORD          TEXT,
PERMISSION        INT
);

CREATE TABLE  student(
USER_NAME         TEXT PRIMARY KEY   NOT NULL,
NAME              TEXT,
DOB               DATETIME,
ADDRESS           TEXT
);

CREATE TABLE  teacher(
USER_NAME         TEXT    NOT NULL,
NAME              TEXT    NOT NULL,
DOB               DATETIME,
PHONE             TEXT,
ADDRESS           TEXT);

drop table object;
CREATE TABLE object(
MSMH          TEXT      NOT NULL,
MSSV          TEXT      NOT NULL,
GV_ID         TEXT      NOT NULL,
DIEM          REAL      NOT NULL DEFAULT -1,
TIN_CHI       REAL      NOT NULL DEFAULT 0,
IS_PASS       REAL      NOT NULL DEFAULT 0,
PRIMARY KEY (MSMH,MSSV, GV_ID));


drop table subject;
CREATE TABLE subject(
MSMH          TEXT PRIMARY KEY   NOT NULL,
NAME          TEXT DEFAULT NULL,
IS_FULL       NOT NULL DEFAULT 0,
IS_OUT_DATE   NOT NULL DEFAULT 0);

# Insert;
INSERT INTO user (USER_NAME,PASSWORD,PERMISSION) 
VALUES ('NguyenVanB', 'password', 'teacher');
INSERT INTO teacher (USER_NAME,NAME,DOB) 
VALUES ('NguyenVanB', 'Nguyen Van Binh', '2007-18-3');
# Update;
update user set PASSWORD = 'std' where USER_NAME == 1710001;
select PERMISSION from user where USER_NAME == 'admin' AND PASSWORD == 'a';
# View select all;
DELETE FROM teacher WHERE USER_NAME == 'A';
select * from teacher;
select * from user;
select * from student;

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
