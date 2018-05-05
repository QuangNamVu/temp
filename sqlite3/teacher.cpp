#include <header.h>

int n_query_std;
string * query_result_std = NULL;

string display_option_teacher(string teacher_user_name){
  string a;
  cout << "----------------------- Faculty: " + teacher_user_name + "    --------------------"<< endl<< endl;
  cout<< left << setw(25) << "1. Change Password[p]";
  cout<< left << setw(20) << "2. View Course";
  cout<< left << setw(20) << "3. Open Course";
  cout<< left << setw(20) << "4. Summarize Score"<< endl;
  cout<< left << setw(25) << "5. Revise Score";
  cout<< left << setw(20) << "6. Logout [l]" ;
  cout<< left << setw(20) << "7. Exit [q]" ;
  cout<< left << setw(20) << "8. Help?? [h]"<<endl<< endl;
  cin >> a;
  return a;
}

void help_teacher(string teacher_user_name){
  cout << "\033[2J\033[1;1H";
  cout << "------------- Faculty: " + teacher_user_name + "-------"<< endl;
  cout << "* Change Password   [p]   [passwd]"<< endl<<endl;
  cout << "* View all course   [v]   [vs]"<< endl<<endl;
  cout << "* Open course       [o]   [oc]    "<< endl<< endl;
  cout << "* Summarize score   [ss]  [sum] "<< endl << endl;
  cout << "* Revise score      [rs]  [revise] "<< endl << endl;
  cout << "--------------------------------------------"<< endl<<endl;
  std::cout << "Press enter to continue..."<< endl;
  std::cin.ignore(1024, '\n');
  std::cin.get();
  cout << "\033[2J\033[1;1H";
}

int teacher_func(string teacher_user_name){
  string get, name, dob;
  int n_element_delete;
  string * list_option_delete = NULL;

  while(1) {
    get = display_option_teacher(teacher_user_name);

    if(get == "6" || get == "l") {
      cout << "Switch account"<< endl;
      return 0;
    }

    if(get == "7" || get == "q") {
      return 1;
    }

    if (get == "8" || get == "h") {
      help_teacher(teacher_user_name);
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
