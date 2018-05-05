#include <header.h>
string query_result[100];
string which_user;


int main(int argc, char* argv[]) {
  int is_exit = 0;
  cout << "\033[2J\033[1;1H";
  // delete_all_table();

  // while(!is_exit){
  //   is_exit = login();
  // }

  // admin_func();

  teacher_func("t1");
  // select_all("teacher");

  // delete_multi_student();
  // insert_user("t1", "passt", "teacher");
  // select * from teacher;
  // delete_student("1712378");
  // select_all("user");
  // select_all("teacher");
  return 0;
}
