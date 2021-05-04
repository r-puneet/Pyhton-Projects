#include<iostream>
#include<climits>
using namespace std;

int main(){

    int n;
    cout<<"Enter size of array:";
    cin>>n;

    cout<<"Enter elements:";
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

    cout<<"Array:";
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }

    cout<<endl;

    int maxnum=INT_MIN;
    int minnum=INT_MAX;

    for(int i=0;i<n;i++){
        maxnum=max(maxnum,arr[i]);
        minnum=min(minnum,arr[i]);
    }
    cout<<"Maximum Element:"<<maxnum<<endl;
    cout<<"Minimum Element:"<<minnum;

    return 0;
}

