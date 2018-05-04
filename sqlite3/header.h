#include <iostream>
#include <sqlite3.h>
#include <iomanip>
#include <fcntl.h>
using namespace std;
//g++ -o test2 test2.cpp -lsqlite3


void insert_user(string user_name, string password, string type);

string quotesql(const string& s);

string query_select(string att,string table,string condition);


void login(int * is_exit);

void admin_func(int * is_exit);
void student_func(int * is_exit);
void teacher_func(int * is_exit);

void update_condition(string table_name, string att, string value, string condition);
void update_condition(string table_name, string att, int value, string condition);


/* void display(string table, string att, string keyword); */
void select_all(string table, string query_result[100]);
void select_like(string table, string att, string keyword, string query_result[100]);
