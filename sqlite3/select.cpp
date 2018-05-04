#include <header.h>

string query_select(string att,string table,string condition){
  sqlite3 *db;
  int rc;
  sqlite3_stmt * stmt;
  string s = "-1",query_stmt =
    "SELECT " + att +
    " from " + table +
    " where ( " + condition + " );";


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

void select_all(string table, string query_result[100]){
  // cout<< "---------------------------------------------------------------------------------------------"<<endl;

  if (table == "student") {
    cout<< "----------------------------------------------------------STUDENT-------------------------------------------------------------"<<endl;
  }

  if (table == "teacher") {
    cout<< "----------------------------------------------------------TEACHER-------------------------------------------------------------"<<endl;
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
      return;
    }
  if (sqlite3_prepare(db, query_stmt.c_str(), -1 , &stmt, NULL)  != SQLITE_OK){

    printf("%d\n", -1  );
    sqlite3_finalize(stmt);
    sqlite3_close(db);
    return;
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
}

void select_like (string table, string att, string keyword, string query_result[100]){
  if (table == "student") {
    cout<< "----------------------------------------------------------STUDENT-------------------------------------------------------------"<<endl;
  }

  if (table == "teacher") {
    cout<< "----------------------------------------------------------TEACHER-------------------------------------------------------------"<<endl;
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
      return;
    }
  if (sqlite3_prepare(db, query_stmt.c_str(), -1 , &stmt, NULL)  != SQLITE_OK){

    printf("%d\n", -1  );
    sqlite3_finalize(stmt);
    sqlite3_close(db);
    return;
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
}
