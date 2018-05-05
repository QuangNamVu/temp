#include<header.h>

string quotesql( const string& s ){
  return string("'") + s + string("'");
}

vector<string> split(const string& s)
{
   vector<string> ret;
   typedef string::size_type string_size;
   string_size i = 0;

   // invariant: we have processed characters [original value of i, i)
   while (i != s.size()) {
      // ignore leading blanks
      // invariant: characters in range [original i, current i) are all spaces
      while (i != s.size() && isspace(s[i]))
         ++i;

      // find end of next word
      string_size j = i;
      // invariant: none of the characters in range [original j, current j)is a space
      while (j != s.size() && !isspace(s[j]))
         j++;

      // if we found some nonwhitespace characters
      if (i != j) {
         // copy from s starting at i and taking j - i chars
         ret.push_back(s.substr(i, j - i));
         i = j;
      }
   }
   return ret;
}

string * split_space(int * size ) {
  string s;
  // read and split each line of input
  cin.ignore();
  getline(cin, s);
  vector<string> v = split(s);
  *size = v.size();
  // cout<< v.size();
  string * result = new string[v.size()];
  for (vector<string>::size_type i = 0; i != v.size(); ++i)
    result[i] = v[i];
  return result;
}
