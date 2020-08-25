#include<iostream>
#include<string.h>
using namespace std;



int main() {

   int a,b;
   cout<<"Enter 1st and 2nd limit"<<"\n";
   cin>>a>>b;
   cout<<"The prime numbers are"<<"\n";
   for(int i=a;i<= b ; i++)
   {
      bool isPrime = 1;
       for(int j=2;j<i;j++)
       {
           if(i%j==0)
           {
               isPrime=0;
           }
       }
       if(isPrime)
       {
           cout<<i<<"\n";
       }
   }
	return 0;
}
