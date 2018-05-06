#include <header.h>

int n_query_std;
string * query_result_std = NULL;

string display_option_teacher(string teacher_user_name){
  string a;
  cout << endl<< "---------------------------------------------------------------- Faculty: " + teacher_user_name + "    -------------------------------------------"<< endl<< endl;
  cout<< left << setw(25) << "1. Change Password[p]";
  cout<< left << setw(25) << "2. View My Courses[c]";
  cout<< left << setw(25) << "3. Search Course[scn]";
  cout<< left << setw(25) << "4. Open Course[o][a]";
  cout<< left << setw(20) << "5. Summarize Score"<< endl;
  cout<< left << setw(25) << "6. Revise Score";
  cout<< left << setw(25) << "7. Logout [l]" ;
  cout<< left << setw(25) << "8. Exit [q]" ;
  cout<< left << setw(20) << "9. Help? [h]"<<endl<< endl;
  cin >> a;
  return a;
}

void help_teacher(string teacher_user_name){
  cout << "\033[2J\033[1;1H";
  cout << "------------- Faculty: " + teacher_user_name + "-------"<< endl;
  cout << "* Change Password         [p]   [passwd]"<< endl<<endl;
  cout << "* View all course         [c]           "<< endl<<endl;
  cout << "└── View all student      [v]           "<< endl;
  cout << "    in course                           "<< endl;
  cout << "* Search course           [s]   [sc]"<<endl;
  cout << "└── Search course by name [scn]     "<< endl;
  cout << "└── Search course         [scn]     "<< endl;
  cout << "    by faculty            [scf] [sct]"<< endl<<endl;
  cout << "* Open course             [o]   [oc]    "<< endl<< endl;
  cout << "* Summarize score         [ss]  [sum] "<< endl << endl;
  cout << "* Revise score            [rs]  [revise] "<< endl << endl;
  cout << "--------------------------------------------"<< endl<<endl;
  std::cout << "Press enter to continue..."<< endl;
  std::cin.ignore(1024, '\n');
  std::cin.get();
  cout << "\033[2J\033[1;1H";
}

int add_course(string MSMH, string gv_id, string name, int n_student){
  sqlite3 *db;
  int rc;
  sqlite3_stmt * stmt;
  string sqlstatement =
    "INSERT INTO subject (MSMH, GV_ID, NAME, N_STUDENT) VALUES("
    + quotesql(MSMH) + ","
    + quotesql(gv_id)+ ","
    + quotesql(name)+ ","
    + quotesql(to_string(n_student)) + ");";

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
  if(rc != SQLITE_DONE)
  //   printf("\nCourse Existed %s\n", .c_str());
  // printf("\nCourse Existed %s\n", .c_str());
  cout<< "\nCourse Existed %s\n"<< MSMH;
  return rc;
}

int delete_course(string msmh, string gv_id){
  sqlite3 *db;
  int rc;
  sqlite3_stmt * stmt;
  string sqlstatement =
    "DELETE FROM subject where (MSMH, GV_ID) == ("
    + quotesql(msmh)+","+ quotesql(gv_id)+ ");";
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
  if(rc != SQLITE_DONE)
    printf("\nCourse Not found %s\n", msmh.c_str());
  return rc;
}


int teacher_func(string teacher_user_name){
  string get, name, dob;
  int n_element_delete;
  string * list_option_delete = NULL;

  while(1) {
    get = display_option_teacher(teacher_user_name);

    if(get == "7" || get == "l") {
      cout << "Switch account"<< endl;
      return 0;
    }

    if(get == "8" || get == "q") {
      return 1;
    }

    if (get == "9" || get == "h") {
      help_teacher(teacher_user_name);
    }
    else if (get =="c" ) {
      query_result_std = select_search("subject","GV_ID", teacher_user_name);
    }
    else if (get == "scn" ) {
      string subjname;
      cout<< "Course Name: "<< endl;
      cin.ignore();
      getline(cin, subjname);
      query_result_std = select_like("subject","NAME", subjname);
    }
    else if (get == "v" ) {
      string course_id;
      cout<< "Course Id: "<< endl;
      cin.ignore();
      getline(cin, course_id);
      query_result_std = select_where("object", "MSMH =='" +course_id + "' AND GV_ID =='"+ teacher_user_name+ "'");
    }
    else if (get == "scn" ) {
      string subjname;
      cout<< "Course Name: "<< endl;
      cin.ignore();
      getline(cin, subjname);
      query_result_std = select_search("object","NAME", subjname);
    }
    else if (get == "a" ||get == "o" || get == "oc") {
      int number;
      string c_id, c_name;
      cout<< "Course Id | Slot : ";
      cin>>c_id>> number;
      cout<< "Course Name: ";
      cin.ignore();
      getline(cin, c_name);
      add_course(c_id, teacher_user_name, c_name, number);
    }

    else if (get == "dc" || get == "d") {
      string c_id;
      cout<< "Course Id : ";
      cin>>c_id;
      delete_course(c_id, teacher_user_name);
    }

    else if (get == "p" || get == "passwd") {
      string pass;
      cout << "Change Password"<<endl;
      cout << "New Teacher Password:"<<endl;
      cin >> pass;
      update_condition("user", "PASSWORD", pass, "USER_NAME == " + quotesql(teacher_user_name));
    }
    else{
      cout << "\033[2J\033[1;1H";
    }

  }

  return 0;
}
