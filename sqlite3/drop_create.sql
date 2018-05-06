drop table user;
CREATE TABLE  user(
USER_NAME         UNIQUE NOT NULL,
PASSWORD          TEXT,
PERMISSION        TEXT);

drop table student;
CREATE TABLE  student(
USER_NAME         TEXT PRIMARY KEY   NOT NULL,
NAME              TEXT,
DOB               DATETIME,
ADDRESS           TEXT);

drop table teacher;
CREATE TABLE  teacher(
USER_NAME         TEXT    NOT NULL,
NAME              TEXT    NOT NULL,
DOB               DATETIME,
PHONE             TEXT,
ADDRESS           TEXT);

drop table object;
CREATE TABLE object(
MSMH             TEXT     NOT NULL,
MSSV             TEXT     NOT NULL,
GV_ID            TEXT     NOT NULL,
DIEM             FLOAT    NOT NULL DEFAULT -1,
TIN_CHI          INT      NOT NULL DEFAULT 0,
IS_PASS          INT      NOT NULL DEFAULT 0,
PRIMARY KEY (MSMH, GV_ID, MSSV)
);

drop table subject;
CREATE TABLE subject(
MSMH          TEXT NOT NULL,
GV_ID         TEXT NOT NULL,
NAME          TEXT DEFAULT NULL,
N_STUDENT     INT NOT NULL DEFAULT 50,
IS_FULL       INT NOT NULL DEFAULT 0,
IS_OUT_DATE   INT NOT NULL DEFAULT 0,
PRIMARY KEY (MSMH, GV_ID));
