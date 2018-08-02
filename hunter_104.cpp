#include<iostream>
using namespace std;
int main () 
{
    string s;
    int i,j,sum=0;
    cin>>s;
    for(i=0;i<s.length();i++)
    {
    	for(j=0;j<=i;j++)
    	{
    	sum=sum+(s[j]-'0');
    	}
    }
    	cout<<sum;
}
