#include<iostream>
#include<math.h>
using namespace std;
int main () 
{
    int n,c=0,r,sum=0,a;
    cin>>n;
    a=n;
    while(a>0)
    {
    	a/=10;
    	c+=1;
    }
    while(n>0)
    {
    	r=n%10;
    	sum=sum+pow(r,c);
    	n=n/10;
    }
    cout<<sum;
}
