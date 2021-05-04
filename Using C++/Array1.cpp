#include<iostream>
using namespace std;

int main(){

     int n;
  

    cout<<"Enter Size of array:";
    cin>>n;

    cout<<"Enter Elements:";

    int array[n];
    for(int i=0;i<n;i++){
        cin>>array[i];
    }
    
    cout<<"Array:";
    for(int i=0;i<n;i++){
        cout<<array[i]<<" ";
    }
    return 0;
}