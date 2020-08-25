#include <iostream>
#include <string.h>
using namespace std;





int main()
{
   char letter[1000];
   cout<<"Enter the string \n";
   cin>>letter;
   int n = strlen(letter);
   int count = 0;
   for(int i=0;i<n/2;i++)
   {
       if(letter[i]==letter[n-i-1])
       {
           count++;
       }

   }
   if(count == n/2)
   {
       cout<<"string is palindrome \n";
   }else{
       cout<<"string is not palindrome \n";
   }
    return 0;
}
