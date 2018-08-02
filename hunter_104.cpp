#include <iostream>
using namespace std;

int main () 
{
    int n,i;
    cin>>n;
    for(i=0;i<n;i++)
    {
    	for(int j=0;j<=i;j++)
    	{
    		cout<<"1";
    		if(i!=j)
    		cout<<" ";
    	}
    	cout<<"\n";
    }
    
}
