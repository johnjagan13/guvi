#include <iostream>
#include<math.h>
using namespace std;
int main () 
{
    int n,i,e=0,arr[100],sum=0;
    string s;
    cin>>s;
    n=s.length();
    for(i=0;i<n;i++)
    {
    	int c=s[(i+1)%n]-'0';
    	//cout<<c<<" ";
    	int p=s[i]-'0';
    	sum+=pow(p,c);
    }
    cout<<"\n"<<sum;
}
