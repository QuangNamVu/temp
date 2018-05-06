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
