#include <header.h>

int n_element_delete;
string * list_option_delete = NULL;
string * query_result_user = NULL;

string display_option(){
  string a;
  cout << "--------------------------------ADMIN-------------------"<< endl;
  cout<< left << setw(15) << "1. Show User";
  cout<< left << setw(20) << "2. Search User";
  cout<< left << setw(20) << "3. Add User";
  cout<< left << setw(20) << "4. Delete User";
  cout<< left << setw(20) << "5. Logout [l]";
  cout<< left << setw(20) << "6. Exit [q]" ;
  cout<< left << setw(20) << "7. Help?? [h]"<< endl;
  cin >> a;
  return a;
}

void help(){
  cout << "\033[2J\033[1;1H";
  cout << "--------------------ADMIN-------------------"<< endl;
  cout << "* Change Password          [p]   [passwd]"<< endl<<endl;
  cout << "* Show User"<< endl;
  cout << "├── Show faculty           [f]   [t]   [1 1]"<< endl;
  cout << "└── Show Student           [s]         [1 1]"<< endl<<endl;
  cout << "* Search User by name"<< endl;
  cout << "├── Search Faculty by name [sfn] [stn] [2 1]"<< endl;
  cout << "└── Search Student by name [ssn]       [2 2]"<< endl<<endl;
  cout << "* Add User"<< endl;
  cout << "├── Add Faculty            [af]  [at]  [3 1]"<< endl;
  cout << "└── Add Student            [as]        [2 2]"<< endl<<endl;
  cout << "* Delete User"<< endl;
  cout << "├── Delete Faculty         [df]  [dt]  [4 1]"<< endl;
  cout << "└── Delete Student         [ds]        [4 2]"<< endl<<endl;
  cout << "--------------------------------------------"<< endl;
  std::cout << "Press enter to continue..."<< endl;
  std::cin.ignore(1024, '\n');
  std::cin.get();
  cout << "\033[2J\033[1;1H";
}

string * show_user(){
  string b ="";
  cout << "1. Show all Faculty"<< endl;
  cout << "2. Show all Student"<< endl;
  while(b != "1" && b != "2"){
    getline(std::cin, b);
  }
  if (b == "1") {
    return select_all("teacher");
  }
  return select_all("student");
}

string * search_user_name(){
  int a =0;
  string name;
  cout << "1. Search faculty by name"<< endl;
  cout << "2. Search student by name"<< endl;
  while(a != 1 && a != 2){
    cin >> a ;
  }
  if (a == 1) {
    cout<< "Enter name : ";
    cin >> name;
    return select_like("teacher", "NAME",name);
  }
  if (a == 2){
    cout<< "Enter name : ";
    cin >> name;
    return select_like("student", "NAME",name);
  }
  return select_all("student");
}

int insert_user(string user_name, string password, string type){
  sqlite3 *db;
  int rc;
  sqlite3_stmt * stmt;
  string sqlstatement =
    "INSERT INTO user (USER_NAME, PASSWORD, PERMISSION) VALUES("
    +quotesql(user_name) + ","
    +quotesql(password)+ ","
    +quotesql( type) + ");";

  // cout<< endl<< sqlstatement<< endl;
  if (sqlite3_open("test.db", &db) != SQLITE_OK)
	{
      cout << "Failed to open data\n";
      sqlite3_finalize(stmt);
      sqlite3_close(db);
      return sqlite3_open("test.db", &db);
	}

  sqlite3_prepare_v2( db, sqlstatement.c_str(), -1, &stmt, NULL );
  rc = sqlite3_step(stmt);

  if(rc != SQLITE_DONE)
    printf("User %s existed\n", user_name.c_str());
  else{
    printf("Create user %s success \n", user_name.c_str());
  }
  sqlite3_finalize(stmt);
  sqlite3_close(db);
  return rc;
}

int add_student(string user_name, string name, string dob){
  int result = insert_user(user_name, user_name, "student");
  if (result != SQLITE_DONE) {
    return result;
  }
  sqlite3 *db;
  int rc;
  sqlite3_stmt * stmt;
  string sqlstatement =
    "INSERT INTO student (USER_NAME, NAME, DOB, ADDRESS) VALUES("
    + quotesql(user_name) + ","
    + quotesql(name)+ ","
    + quotesql(dob)+ ","
    + quotesql(".") + ");";
  // cout << sqlstatement<< endl;
  if (sqlite3_open("test.db", &db) != SQLITE_OK)
	{
      cout << "Failed to open db\n";
      sqlite3_finalize(stmt);
      sqlite3_close(db);
      return sqlite3_open("test.db", &db);
	}
  sqlite3_prepare_v2( db, sqlstatement.c_str(), -1, &stmt, NULL );
  rc = sqlite3_step(stmt );
  sqlite3_finalize(stmt);
  sqlite3_close(db);
  return rc;
}

int add_teacher(string user_name, string name, string dob){
  int result = insert_user(user_name, user_name, "teacher");
  if (result != SQLITE_DONE) {
    return result;
  }
  sqlite3 *db;
  int rc;
  sqlite3_stmt * stmt;
  string sqlstatement =
    "INSERT INTO teacher (USER_NAME, NAME, DOB, PHONE, ADDRESS) VALUES("
    + quotesql(user_name) + ","
    + quotesql(name)+ ","
    + quotesql(dob)+ ","
    + quotesql(".") +","
    + quotesql(".") + ");";

  // cout << sqlstatement<< endl;
  if (sqlite3_open("test.db", &db) != SQLITE_OK)
	{
      cout << "Failed to open db\n";
      sqlite3_finalize(stmt);
      sqlite3_close(db);
      return sqlite3_open("test.db", &db);
	}
  sqlite3_prepare_v2( db, sqlstatement.c_str(), -1, &stmt, NULL );
  rc = sqlite3_step(stmt );
  sqlite3_finalize(stmt);
  sqlite3_close(db);
  return rc;
}

int delete_teacher(string user_name){
  delete_user(user_name);
  sqlite3 *db;
  int rc;
  sqlite3_stmt * stmt;

  string sqlstatement = "delete from teacher where USER_NAME == " + quotesql(user_name) + ";" ;
  // cout<< " delete teacher"<< endl<< sqlstatement;
  if (sqlite3_open("test.db", &db) != SQLITE_OK)
	{
      cout << "Failed to open db\n";
      sqlite3_finalize(stmt);
      sqlite3_close(db);
      return sqlite3_open("test.db", &db);
	}
  sqlite3_prepare_v2( db, sqlstatement.c_str(), -1, &stmt, NULL );
  rc = sqlite3_step(stmt );
  sqlite3_finalize(stmt);
  sqlite3_close(db);
  return rc;
}

int delete_student(string user_name){
  delete_user(user_name);
  sqlite3 *db;
  int rc;
  sqlite3_stmt * stmt;

  string sqlstatement = "delete from student where USER_NAME == " + quotesql(user_name) + ";" ;
  // cout<< " delete teacher"<< endl<< sqlstatement;
  if (sqlite3_open("test.db", &db) != SQLITE_OK)
	{
      cout << "Failed to open db\n";
      sqlite3_finalize(stmt);
      sqlite3_close(db);
      return sqlite3_open("test.db", &db);
	}
  sqlite3_prepare_v2( db, sqlstatement.c_str(), -1, &stmt, NULL );
  rc = sqlite3_step(stmt );
  sqlite3_finalize(stmt);
  sqlite3_close(db);
  return rc;
}
void delete_multi_teacher(){
  cout<< "Delete Teacher User Name or Number:";
  int n = -1;
  list_option_delete = split_space(&n);
  for (int i = 0; i < n; ++i) {
    if(list_option_delete[i].length() < 3) {
      list_option_delete[i] = query_result_user[atoi(list_option_delete[i].c_str())];
    }
  }

  for (int i = 0; i < n; ++i) {
    display_teacher_user(list_option_delete[i]);
  }

  string s;
  cout<<" Delete "<<n << " Teacher Y/n" << endl;
  std::cin.ignore(1024, '\n');
  s = cin.get();
  if (s == "n") {
    return;
  }

  for (int i = 0; i < n; ++i) {
    delete_teacher(list_option_delete[i]);
  }
}

void delete_multi_student(){
  cout<< "Delete Student User Name or Number:";
  int n = -1;
  list_option_delete = split_space(&n);
  for (int i = 0; i < n; ++i) {
    if(list_option_delete[i].length() < 3) {
      list_option_delete[i] = query_result_user[atoi(list_option_delete[i].c_str())];
    }
  }

  for (int i = 0; i < n; ++i) {
    display_student_user(list_option_delete[i]);
  }

    string s;
    cout<<" Delete "<<n << " Student Y/n" << endl;
    cin.ignore();
    getline(cin, s);
    if (s == "n") {
      return;
    }

  for (int i = 0; i < n; ++i) {
    delete_student(list_option_delete[i]);
  }
}

int delete_user(string user_name){
  if(user_name == "admin"){
    cout<< "CANNOT DELETE ADMIN";
    return -1;
  }
  sqlite3 *db;
  int rc;
  sqlite3_stmt * stmt;

  string sqlstatement = "delete from user where USER_NAME == " + quotesql(user_name) + ";" ;

  if (sqlite3_open("test.db", &db) != SQLITE_OK)
	{
      cout << "Failed to open db\n";
      sqlite3_finalize(stmt);
      sqlite3_close(db);
      return sqlite3_open("test.db", &db);
	}

  sqlite3_prepare_v2( db, sqlstatement.c_str(), -1, &stmt, NULL );
  rc = sqlite3_step(stmt );

  if(rc != SQLITE_DONE)
    printf("CANNOT DELETE TEACHER %s\n", user_name.c_str());

  sqlite3_finalize(stmt);
  sqlite3_close(db);
  return rc;
}

int admin_func(){
  string get, name, user_name, dob;
  int n_element_delete;
  string * list_option_delete = NULL;

  while(1) {
    get = display_option();

    if(get == "5" || get == "l") {
      cout << "Switch account"<< endl;
      return 0;
    }
    if(get == "6" || get == "q") {
      return 1;
    }

    if (get == "1") {
      cout << "Show User"<<endl;
      int r =0;
      cout << "1. Show all Faculty"<< endl;
      cout << "2. Show all Student"<< endl;

      do {
        cin >> r;
      } while (r!=1 && r!=2);

      if (r == 1) {
        query_result_user =  select_all("teacher");
      }
      else{
        query_result_user = select_all("student");
      }
    }

    else if (get == "p" || get == "passwd") {
      string pass;
      cout << "Change Password"<<endl;
      cout << "New Admin Password:"<<endl;
      cin >> pass;
      update_condition("user", "PASSWORD", pass, "PERMISSION == 'admin'" );
    }
    else if (get == "2") {
      cout << "Search"<<endl;
      query_result_user = search_user_name();
    }

    else if (get == "f" || get == "1 1" || get == "t" || get == "show fac") {
      cout << "Show all Faculty: " << endl;
      query_result_user = select_all("teacher");
    }

    else if (get == "s" || get == "1 2" || get == "show std") {
      cout << "Show all Student: " << endl;
      query_result_user = select_all("student");
    }

    else if (get == "user") {
      cout << "Show all User: " << endl;
      query_result_user = select_all("user");
    }
    else if (get == "ssn") {
      cout << "Student Name :";
      cin >> name;
      query_result_user = select_like("student", "NAME",name);
    }
    else if (get == "stn" || get == "sfn") {
      cout << "Faculty Name :";
      cin >> name;
      query_result_user = select_like("teacher", "NAME",name);
    }
    else if (get == "at" || get == "af" || get == "3 1") {
      cout<< "User Name | Name | Date of birth :";
      cin>> user_name;
      cin>> name;
      cin>> dob;
      add_teacher(user_name, name, dob );
    }
    else if (get == "as" || get == "3 2") {
      cout<< "User Name | Name | Date of birth :";
      cin>> user_name;
      cin>> name;
      cin>> dob;
      add_student(user_name, name, dob );
    }
    else if (get == "df" || get == "dt"|| get == "4 1") {
      delete_multi_teacher();
    }
    else if (get == "ds" || get == "4 2") {
      delete_multi_student();
    }
    else if (get == "du" ) {
      cout<< "Delete User Name :";
      cin>> user_name;
      delete_teacher(user_name);
    }
    else if (get == "7" || get == "h") {
      help();
    }
    else{
      cout << "\033[2J\033[1;1H";
    }

  }

  return 0;
}
