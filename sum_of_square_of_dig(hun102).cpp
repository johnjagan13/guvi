#include <iostream>
using namespace std;

int main () 
{
    int n,sum=0,r,t;
    cin>>n;
    t=n;
    while(t!=0)
    {
    	r=t%10;
    	sum=sum+(r*r);
    	t=t/10;
    	
    }
    cout<<sum;
}
