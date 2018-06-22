#include <iostream>
using namespace std;
struct node
{
    int data;
    node *next;
};

class linked_list
{
private:
    node *head,*tail;
public:
    linked_list()
    {
        head = NULL;
        tail = NULL;
    }

    void add_node(int n)
    {
        node *tmp = new node;
        tmp->data = n;
        tmp->next = NULL;

        if(head == NULL)
        {
            head = tmp;
            tail = tmp;
        }
        else
        {
            tail->next = tmp;
            tail = tail->next;
        }
    }

    node* gethead()
    {
        return head;
    }

    static void display(node *head)
    {
        while(head!=NULL){
            cout << head->data <<" ";
            head=head->next;
        }
    }

    static void concatenate(node *a,node *b)
    {
        if( a != NULL && b!= NULL )
        {
            if (a->next == NULL)
                a->next = b;
            else
                concatenate(a->next,b);
        }
    }
};

int main()
{
    linked_list a,b;
    int i,val,n,n1;
    cout<<"First List Size: ";
    cin>>n;
    cout<<"\nFirst List : ";
    for(i=0;i<n;i++){
    	cin>>val;
    	a.add_node(val);
    }
    cout<<"\nSecond List size: ";
    cin>>n1;
    cout<<"\nSecond List : ";
    for(i=0;i<n1;i++){
    	cin>>val;
    	b.add_node(val);
    }
    if(n>0 && n1>0){
    cout<<"\nFinal List : ";
    linked_list::concatenate(a.gethead(),b.gethead());
    linked_list::display(a.gethead());
	}
	else
	{
		cout<<"\n\n\tEnter valid Inputs";
	}
    return 0;
}
