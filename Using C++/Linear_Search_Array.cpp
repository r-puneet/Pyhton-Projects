#include<iostream>
using namespace std;

// creating function
int linearSearch(int arr[], int a, int key){
    for(int i=0;i<a;i++){
        if(arr[i]==key){
            return i;
        }
    }
    return -1;
}

int main(){
    
    cout<<"Size of Array:";
    int a;
    cin>>a;

    cout<<"Enter elements:";
    int arr[10];
    for(int i=0;i<a;i++){
        cin>>arr[i];
    }

    cout<<"Search Number:";
    int key;
    cin>>key;

    // Calling Function
    cout<<"Number found at index:"<<linearSearch(arr,a,key)<<endl;

    return 0;
}