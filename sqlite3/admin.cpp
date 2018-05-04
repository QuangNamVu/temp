#include <header.h>

void admin_func(int * is_exit){
  cout<< "admin function"<< endl;
}

void insert_user(string user_name, string password, string type){
  sqlite3 *db;
  int rc;
  sqlite3_stmt * stmt;
  string sqlstatement =
    "INSERT INTO user (USER_NAME, PASSWORD, PERMISSION) VALUES("
    + quotesql(user_name) + ","
    + quotesql(password)+ ","
    + quotesql(type) + ");";

  if (sqlite3_open("test.db", &db) != SQLITE_OK)
    {
      cout << "Failed to open db\n";
      sqlite3_finalize(stmt);
      sqlite3_close(db);
      return;
    }

  sqlite3_prepare_v2( db, sqlstatement.c_str(), -1, &stmt, NULL );
  // 3622

  // SQLITE_API int sqlite3_step(sqlite3_stmt*);
  rc = sqlite3_step(stmt );

  if(rc != SQLITE_DONE)
    printf("User %s existed\n", user_name.c_str());
  else{
    printf("Create user %s success \n", user_name.c_str());
  }
  sqlite3_finalize(stmt);
  sqlite3_close(db);
}

void delete_user(string user_name, string password, string type){
  sqlite3 *db;
  int rc;
  sqlite3_stmt * stmt;

  string sqlstatement =
    "DELETE FROM user WHERE (USER_NAME, PASSWORD, PERMISSION) VALUES("
    + quotesql(user_name) + ","
    + quotesql(password)+ ","
    + quotesql(type) + ");";

  if (sqlite3_open("test.db", &db) != SQLITE_OK)
    {
      cout << "Failed to open db\n";
      sqlite3_finalize(stmt);
      sqlite3_close(db);
      return;
    }

  sqlite3_prepare_v2( db, sqlstatement.c_str(), -1, &stmt, NULL );
  // 3622

  // SQLITE_API int sqlite3_step(sqlite3_stmt*);
  rc = sqlite3_step(stmt );

  if(rc != SQLITE_DONE)
    printf("User %s existed\n", user_name.c_str());
  else{
    printf("Create user %s success \n", user_name.c_str());
  }
  sqlite3_finalize(stmt);
  sqlite3_close(db);
}

void display_user_student(){}
