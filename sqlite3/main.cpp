#include <header.h>
string query_result[100];

int main(int argc, char* argv[]) {
  string user_name, password;


  int is_exit =0;


  select_all("teacher", query_result);
  select_like("student", "NAME", "ANH", query_result);

  return 0;
}
