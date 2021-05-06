#include<iostream>
using namespace std;

// Defining function
int binarysearch(int arr[], int n, int key){
    int s=0;
    int e=n;
    int mid;
    while(s<=e){
        mid=(s+e)/2;

        if(arr[mid]==key){
            return mid;
        }
        else if(arr[mid]>key){
            e=mid-1;
        }
        else{
            s=mid+1;
        }
    }
    return -1;
}

int main(){

    cout<<"Enter Size:";
    int n;
    cin>>n;

    cout<<"Enter Elements:";
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

    cout<<"Search Number:";
    int key;
    cin>>key;

    cout<<"Number Found at Index:"<<binarysearch(arr,n,key)<<endl;

    return 0;
}