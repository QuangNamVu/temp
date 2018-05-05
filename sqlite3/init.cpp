#include <header.h>

static int callback(void *NotUsed, int argc, char **argv, char **azColName) {
  int i;
  for(i = 0; i<argc; i++) {
    printf("%s = %s\n", azColName[i], argv[i] ? argv[i] : "NULL");
  }
  printf("\n");
  return 0;
}

int query (const char * query) {
  sqlite3 *db;
  char *zErrMsg = 0;
  int rc;

  rc = sqlite3_open("test.db", &db);
  if( rc ) {
    fprintf(stderr, "Can't open database: %s\n", sqlite3_errmsg(db));
    return -1;
  }
  /* Create SQL statement */


  rc = sqlite3_exec(db, query, callback, 0, &zErrMsg);
  sqlite3_close(db);
  return 0;
}


void delete_all_table(){
  const char * sql =
    "delete from user;"                       \
    "delete from teacher;"                    \
    "delete from student;"                    \
    "delete from subject;";
  query(sql);
}

