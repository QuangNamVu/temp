#include <header.h>


void display(string table, string att, string keyword){
  sqlite3 *db;
  int rc;
  sqlite3_stmt * stmt;
  string sqlstatement = "SELECT FROM " + table+ " WHERE " + att + " LIKE " + quotesql(keyword);
  cout<< sqlstatement<< endl;

  // if (sqlite3_open("test.db", &db) != SQLITE_OK)
  //   {
  //     cout << "Failed to open db\n";
  //     sqlite3_finalize(stmt);
  //     sqlite3_close(db);
  //     return;
  //   }

  // sqlite3_prepare_v2( db, sqlstatement.c_str(), -1, &stmt, NULL );
  // // 3622

  // // SQLITE_API int sqlite3_step(sqlite3_stmt*);
  // rc = sqlite3_step(stmt );

  // if(rc != SQLITE_DONE)
  //   printf("User %s existed\n", user_name.c_str());
  // else{
  //   printf("Create user %s success \n", user_name.c_str());
  // }
  // sqlite3_finalize(stmt);
  // sqlite3_close(db);
}
