DELETE FROM subject where (MSMH, GV_ID, NAME) == ('C0101','S1951','cong nghe pm');

INSERT INTO object (MSMH, MSSV, GV_ID, DIEM, TIN_CHI, IS_PASS)
VALUES ('CC51','1792346','S1951','7.5', '3', 1);

INSERT INTO object (MSMH, MSSV, GV_ID, DIEM, TIN_CHI, IS_PASS)
VALUES ('CC51','1992346','S1951','7.5', '3', 1);

INSERT INTO subject (MSMH, NAME) 
VALUES ('CC01','mo hinh hoa');
INSERT INTO subject (MSMH,GV_ID,NAME) 
VALUES ('CC01',S1951,'mo hinh hoa');

# Read
.read drop_create.sql
.read import.sql
.read show.sql

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
SELECT * FROM object WHERE GV_ID == 't;
select * from subject;
select * from object;

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
