#include <header.h>

string query_select(string att,string table,string condition){
  sqlite3 *db;
  int rc;
  sqlite3_stmt * stmt;
  string s = "-1";
  string query_stmt =
    "SELECT " + att +
    " from " + table +
    " where ( " + condition + " );";
  // cout << query_stmt;

  if (sqlite3_open("test.db", &db) != SQLITE_OK)
    {
      cout << "Failed to open db\n";
      sqlite3_finalize(stmt);
      sqlite3_close(db);
      return "-1";
    }

  if (sqlite3_prepare(db, query_stmt.c_str(), -1 , &stmt, NULL)  != SQLITE_OK){
    printf("%s\n", "error query"  );
    sqlite3_finalize(stmt);
    sqlite3_close(db);
    return s;
  }

  int res = 0;
  res = sqlite3_step(stmt);
  if (res == SQLITE_ROW) {
        s = (char *)sqlite3_column_text(stmt,0);
  }
  sqlite3_finalize(stmt);
  sqlite3_close(db);
  return s;
}

void  display_teacher_user(string user_name){
  sqlite3 *db;
  int rc;
  sqlite3_stmt * stmt;
  string query_stmt = "select * from teacher where USER_NAME == " + quotesql(user_name) +";" ;
  if (sqlite3_open("test.db", &db) != SQLITE_OK)
    {
      cout << "Failed to open db\n";
      sqlite3_finalize(stmt);
      sqlite3_close(db);
    }
  if (sqlite3_prepare(db, query_stmt.c_str(), -1 , &stmt, NULL)  != SQLITE_OK){

   printf("%d\n", -1  );
    sqlite3_finalize(stmt);
    sqlite3_close(db);
  }

  int ctotal = sqlite3_column_count(stmt);
  int res = 0;
  res = sqlite3_step(stmt);
  if (res == SQLITE_ROW) {
    cout<< left << setw(5)<< "";
    for (int i = 0; i < ctotal; ++i) {
      string s = (char *)sqlite3_column_text(stmt,i);
      cout<< left<< setw(23)<< s;
    }
    cout<< endl;
  }
  sqlite3_finalize(stmt);
  sqlite3_close(db);
}

void  display_student_user(string user_name){
  sqlite3 *db;
  int rc;
  sqlite3_stmt * stmt;
  string query_stmt = "select * from student where USER_NAME == " + quotesql(user_name) +";" ;
  if (sqlite3_open("test.db", &db) != SQLITE_OK)
    {
      cout << "Failed to open db\n";
      sqlite3_finalize(stmt);
      sqlite3_close(db);
    }
  if (sqlite3_prepare(db, query_stmt.c_str(), -1 , &stmt, NULL)  != SQLITE_OK){

    printf("%d\n", -1  );
    sqlite3_finalize(stmt);
    sqlite3_close(db);
  }

  int ctotal = sqlite3_column_count(stmt);
  int res = 0;
  res = sqlite3_step(stmt);
  if (res == SQLITE_ROW) {
    cout<< left << setw(5)<< "";
    for (int i = 0; i < ctotal; ++i) {
      string s = (char *)sqlite3_column_text(stmt,i);
      cout<< left<< setw(23)<< s;
    }
    cout<< endl;
  }
  sqlite3_finalize(stmt);
  sqlite3_close(db);
}

string * select_all(string table){
  cout << "\033[2J\033[1;1H";
  string * query_result = new string[100];

  if (table == "student") {
    cout<< "----------------------------------------------------------STUDENT-------------------------------------------------------------"<<endl;
  }

  if (table == "teacher") {
    cout<< "----------------------------------------------------------FACULTY-------------------------------------------------------------"<<endl;
  }
  sqlite3 *db;
  int rc;
  sqlite3_stmt * stmt;
  string query_stmt = "select * from " + quotesql(table) +";" ;
  // string query_stmt = "select * from ;" ;
  if (sqlite3_open("test.db", &db) != SQLITE_OK)
    {
      cout << "Failed to open db\n";
      sqlite3_finalize(stmt);
      sqlite3_close(db);
      return NULL;
    }
  if (sqlite3_prepare(db, query_stmt.c_str(), -1 , &stmt, NULL)  != SQLITE_OK){

    printf("%d\n", -1  );
    sqlite3_finalize(stmt);
    sqlite3_close(db);
    return NULL;
  }

  int ctotal = sqlite3_column_count(stmt);
  int res = 0;
  int count  = 0;
  while (1) {
    count ++;
    res = sqlite3_step(stmt);
    if (res == SQLITE_ROW) {
      cout<< left << setw(5)<< count;
      for (int i = 0; i < ctotal; ++i) {
        string s = (char *)sqlite3_column_text(stmt,i);
        cout<< left<< setw(23)<< s;
        // push to string MSSV(ID)
        if(!i){
          query_result[count] = s;
        }
      }
      cout<< endl;
    }
    else if (res == SQLITE_DONE || res == SQLITE_ERROR) {
      cout<< "------------------------------------------------------------------------------------------------------------------------------"<<endl;
      break;
    }
  }
  query_result[0] = to_string(count);
  sqlite3_finalize(stmt);
  sqlite3_close(db);
  return query_result;
}

string * select_like (string table, string att, string keyword){
  cout << "\033[2J\033[1;1H";
  string * query_result = new string[100];
  if (table == "student") {
    cout<< "-----------------------------------------------------------------STUDENT-------------------------------------------------------"<<endl;
  }

  else if (table == "teacher") {
    cout<< "-----------------------------------------------------------------FACULTY-------------------------------------------------------"<<endl;
  }
  else if (table == "subject") {
    cout<< "-----------------------------------------------------------------SUBJECT------------------------------------------------------"<<endl;
    cout<< "STT  Subject Id             Faculty                Subject Name           Slot              Status Full            Out of Date"<<endl;
    cout<< "------------------------------------------------------------------------------------------------------------------------------"<<endl;
  }
  sqlite3 *db;
  int rc;
  sqlite3_stmt * stmt;
  string query_stmt = "SELECT * FROM " + table+ " WHERE " + att + " LIKE '%" + keyword +"%';";

  if (sqlite3_open("test.db", &db) != SQLITE_OK)
    {
      cout << "Failed to open db\n";
      sqlite3_finalize(stmt);
      sqlite3_close(db);
      return NULL;
    }
  if (sqlite3_prepare(db, query_stmt.c_str(), -1 , &stmt, NULL)  != SQLITE_OK){

    printf("%d\n", -1  );
    sqlite3_finalize(stmt);
    sqlite3_close(db);
    return NULL;
  }

  int ctotal = sqlite3_column_count(stmt);
  int res = 0;
  int count  = 0;
  while (1) {
    count ++;
    res = sqlite3_step(stmt);
    if (res == SQLITE_ROW) {
      cout<< left << setw(5)<< count;
      for (int i = 0; i < ctotal; ++i) {
        string s = (char *)sqlite3_column_text(stmt,i);
        cout<< left<< setw(23)<< s;
        // push to string MSSV(ID)
        if(!i){
          query_result[count] = s;
        }
      }
      cout<< endl;
    }
    else if (res == SQLITE_DONE || res == SQLITE_ERROR) {
      cout<< "------------------------------------------------------------------------------------------------------------------------------"<<endl;
      break;
    }
  }
  query_result[0] = to_string(count);
  sqlite3_finalize(stmt);
  sqlite3_close(db);
  return query_result;
}


string * select_search (string table, string att, string keyword){
  cout << "\033[2J\033[1;1H";
  string * query_result = new string[100];
  if (table == "student") {
    cout<< "-----------------------------------------------------------------STUDENT-------------------------------------------------------"<<endl;
  }

  if (table == "teacher") {
    cout<< "-----------------------------------------------------------------FACULTY-------------------------------------------------------"<<endl;
  }
  if (table == "subject") {
    cout<< "-----------------------------------------------------------------SUBJECT------------------------------------------------------"<<endl;
    cout<< "STT  Subject Id             Faculty                Subject Name           Slot              Status Full            Out of Date"<<endl;
    cout<< "------------------------------------------------------------------------------------------------------------------------------"<<endl;
  }

  sqlite3 *db;
  int rc;
  sqlite3_stmt * stmt;
  string query_stmt = "SELECT * FROM " + table+ " WHERE " + att + " == '" + keyword+"';";
  // cout << query_stmt;

  if (sqlite3_open("test.db", &db) != SQLITE_OK)
    {
      cout << "Failed to open db\n";
      sqlite3_finalize(stmt);
      sqlite3_close(db);
      return NULL;
    }
  if (sqlite3_prepare(db, query_stmt.c_str(), -1 , &stmt, NULL)  != SQLITE_OK){

    printf("\nx\n");
    sqlite3_finalize(stmt);
    sqlite3_close(db);
    return NULL;
  }

  int ctotal = sqlite3_column_count(stmt);
  int res = 0;
  int count  = 0;
  while (1) {
    count ++;
    res = sqlite3_step(stmt);
    if (res == SQLITE_ROW) {
      cout<< left << setw(5)<< count;
      for (int i = 0; i < ctotal; ++i) {
        string s = (char *)sqlite3_column_text(stmt,i);
        cout<< left<< setw(23)<< s;
        // push to string MSSV(ID)
        if(!i){
          query_result[count] = s;
        }
      }
      cout<< endl;
    }
    else if (res == SQLITE_DONE || res == SQLITE_ERROR) {
      cout<< "------------------------------------------------------------------------------------------------------------------------------"<<endl;
      break;
    }
  }
  query_result[0] = to_string(count);
  sqlite3_finalize(stmt);
  sqlite3_close(db);
  return query_result;
}

string * select_where (string table, string condition){
  cout << "\033[2J\033[1;1H";
  string * query_result = new string[100];
  if (table == "student") {
    cout<< "-----------------------------------------------------------------STUDENT-------------------------------------------------------"<<endl;
  }

  if (table == "teacher") {
    cout<< "-----------------------------------------------------------------FACULTY-------------------------------------------------------"<<endl;
  }
  if (table == "subject") {
    cout<< "-----------------------------------------------------------------SUBJECT------------------------------------------------------"<<endl;
    cout<< "STT  Subject Id             Faculty                Subject Name           Slot              Status Full            Out of Date"<<endl;
    cout<< "------------------------------------------------------------------------------------------------------------------------------"<<endl;
  }
  if (table == "object") {
    cout<< "-----------------------------------------------------------------SUBJECT------------------------------------------------------"<<endl;
    cout<< "STT  Subject Id             Student Id             Faculty Id             Score             Total credit               Pass   "<<endl;
    cout<< "------------------------------------------------------------------------------------------------------------------------------"<<endl;
    // cout<< "3    CC01                   1712348                S1951                  7.5                    3                      1     "<<endl;
  }

  sqlite3 *db;
  int rc;
  sqlite3_stmt * stmt;
  string query_stmt = "SELECT * FROM " + table+ " WHERE " + condition+";";
  // cout << query_stmt;

  if (sqlite3_open("test.db", &db) != SQLITE_OK)
    {
      cout << "Failed to open db\n";
      sqlite3_finalize(stmt);
      sqlite3_close(db);
      return NULL;
    }
  if (sqlite3_prepare(db, query_stmt.c_str(), -1 , &stmt, NULL)  != SQLITE_OK){

    printf("\nx\n");
    sqlite3_finalize(stmt);
    sqlite3_close(db);
    return NULL;
  }

  int ctotal = sqlite3_column_count(stmt);
  int res = 0;
  int count  = 0;
  while (1) {
    count ++;
    res = sqlite3_step(stmt);
    if (res == SQLITE_ROW) {
      cout<< left << setw(5)<< count;
      for (int i = 0; i < ctotal; ++i) {
        string s = (char *)sqlite3_column_text(stmt,i);
        cout<< left<< setw(23)<< s;
        // push to string MSSV(ID)
        if(!i){
          query_result[count] = s;
        }
      }
      cout<< endl;
    }
    else if (res == SQLITE_DONE || res == SQLITE_ERROR) {
      cout<< "------------------------------------------------------------------------------------------------------------------------------"<<endl;
      break;
    }
  }
  query_result[0] = to_string(count);
  sqlite3_finalize(stmt);
  sqlite3_close(db);
  return query_result;
}
