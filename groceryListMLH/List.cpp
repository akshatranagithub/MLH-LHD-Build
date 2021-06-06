#include<iostream>
using namespace std;
class list{
	public:
		char item[50];
		int quantity;
};
int main()
{
	int n;
	cout<<"\nEnter the number of items: ";
	cin>>n;
	list ob[n];
	for(int i = 0; i < n; i++)
	{
		cout<<"\nEnter the name of the item: ";
		cin>>ob[i].item;
		cout<<"Enter the number of item: ";
		cin>>ob[i].quantity;
		cout<<endl;
	}
	cout<<"\tItems\tQuantity";
	for(int i = 0; i < n; i++)
	{
		cout<<"\n\t"<<ob[i].item<<"\t   "<<ob[i].quantity<<endl;
	}
}
