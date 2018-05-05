#include<header.h>

void update_condition(string table_name, string att, string value, string condition){
  sqlite3 *db;
  int rc;
  sqlite3_stmt * stmt;
  string sqlstatement =
    "update "+  table_name+" set " +att + "= " + quotesql(value) +" where ("
    + condition + ");";
  // cout<< sqlstatement<< endl;
  if (sqlite3_open("test.db", &db) != SQLITE_OK)
    {
      cout << "Failed to open db\n";
      sqlite3_finalize(stmt);
      sqlite3_close(db);
      return;
    }

  sqlite3_prepare_v2( db, sqlstatement.c_str(), -1, &stmt, NULL );
  // 3622

  rc = sqlite3_step(stmt );

  if(rc != SQLITE_DONE)
    cout<< "CANNOT CHANGE " << att<< endl;
  else{
    cout<< "CHANGE " << att<< " SUCCESS" << endl;
  }
  sqlite3_finalize(stmt);
  sqlite3_close(db);
}

void update_condition(string table_name, string att, int v, string condition){
  string value = to_string(v);
  sqlite3 *db;
  int rc;
  sqlite3_stmt * stmt;
  string sqlstatement =
    "update "+  table_name+" set " +att + "= " + quotesql(value) +" where ("
    + condition + ");";
  // cout<< sqlstatement<< endl;
  if (sqlite3_open("test.db", &db) != SQLITE_OK)
    {
      cout << "Failed to open db\n";
      sqlite3_finalize(stmt);
      sqlite3_close(db);
      return;
    }

  sqlite3_prepare_v2( db, sqlstatement.c_str(), -1, &stmt, NULL );
  // 3622

  rc = sqlite3_step(stmt );

  if(rc != SQLITE_DONE)
    cout<< "cannot change " << att<< endl;
  else{
    cout<< "Change " << att<< " success" << endl;
  }
  sqlite3_finalize(stmt);
  sqlite3_close(db);
}
