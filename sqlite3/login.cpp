#include<header.h>

void login(int * is_exit){
  string user_name;
  string password;
  cout<< "User Name:";
  cin>> user_name;
  cout<< "Password :";
  cin>> password;

  string s = query_select("PERMISSION","user","USER_NAME ==" +quotesql(user_name) + " AND PASSWORD == "+quotesql(password));

  if(s == "admin"){
    cout<< "ADMIN"<< endl;
    admin_func(is_exit);
  }
  else if (s == "teacher") {
    cout<< "TEACHER"<< endl;
    teacher_func(is_exit);
  }
  else if (s == "student") {
    cout<< "STUDENT"<< endl;
    student_func(is_exit);
  }
  else{
    string ans;
    printf("Login Failed\nContinue ? Y/N \n");
    cin>> ans;
    // if (cin.get() == '\n'){
    if (ans != "Y" && ans !="y") {
      *is_exit = 1;
    }
  }
}
