#include <iostream>
#include <sqlite3.h>
#include <iomanip>
#include <fcntl.h>
#include <vector>
/* #include <conio.h> */
using namespace std;
//g++ -o test2 test2.cpp -lsqlite3


int import();

void add_user(string user_name, string password, string type);

string quotesql(const string& s);
string * split_space(int * size );

string query_select(string att,string table,string condition);


int login();

int admin_func();
int teacher_func(string teacher_user_name);
int student_func(string teacher_user_name);

void update_condition(string table_name, string att, string value, string condition);
void update_condition(string table_name, string att, int value, string condition);


string * select_all(string table);

string * select_like(string table, string att, string keyword);

int insert_user(string user_name, string password, string type);
int add_teacher(string user_name, string name, string dob);
int add_student(string user_name, string name, string dob);

int delete_user(string user_name);
int delete_teacher(string user_name);
int delete_student(string user_name);

void delete_all_table();

void delete_multi_student();

void display_student_user(string user_name);
void display_teacher_user(string user_name);
