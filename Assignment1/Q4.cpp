
#include<iostream>
#include<string.h>
using namespace std;



int main() {

cout<<"So what do you want to encrypt "<<"\n";
  string str;
  cin>>str;
  for(int i=0;i<str.length();i++)
  {
      str[i] += 5;
  }
  cout<<str;
	return 0;
}
