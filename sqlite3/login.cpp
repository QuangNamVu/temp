#include<header.h>

int login(){
  cout << "\033[2J\033[1;1H";
  string user_name;
  string password;
  cout<< "User Name:";
  cin>> user_name;
  cout<< "Password :";
  cin>> password;

  string s = query_select("PERMISSION","user","USER_NAME ==" +quotesql(user_name) + " AND PASSWORD == "+quotesql(password));

  if(s == "admin"){
    cout<< "ADMIN"<< endl;
    return admin_func();
  }
  if (s == "teacher") {
    cout<< "TEACHER"<< endl;
    return teacher_func(user_name);
  }
  if (s == "student") {
    cout<< "STUDENT"<< endl;
    return student_func(user_name);
  }

  string ans;
  printf("Login Failed\nContinue ? Y/N \n");
  cin>> ans;
  // if (cin.get() == '\n'){
  if (ans != "Y" && ans !="y") {
    return 1;
  }
    return 0;
}
