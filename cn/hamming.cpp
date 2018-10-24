#include<iostream>
using namespace std;
int main(){

 int data[10];
int datarec[10],c,c1,c2,c3,i;

cout<<"enter 4 bits ";

cin>>data[0];
cin>>data[1];
cin>>data[2];
cin>>data[4];

data[6]=data[0]^data[2]^data[4];

data[5]=data[0]^data[1]^data[4];
data[3]=data[0]^data[1]^data[2];

cout<<"encoded data is ";
for(i=0;i<7;i++)
 cout<<data[i];
cout<<"\n";
cout<<"enter data recived:";
for(i=0;i<7;i++)
 cin>>datarec[i];

c1=data[6]^data[4]^data[2]^data[0];

c2=data[5]^data[4]^data[1]^data[0];
c3=data[3]^data[2]^data[1]^data[0];

c=c3*4+c2*2+c1*1;

if(c==0)
{
 cout<<"no error while tramsmission";
}
else{
  cout<<"error on position"<<c;
  

   cout<<"\nData sent : ";
        for(i=0;i<7;i++)
            cout<<data[i];

        cout<<"\nData received : ";
        for(i=0;i<7;i++)
            cout<<datarec[i];


    cout<<"\nCorrect message is\n";

    if(datarec[7-c]==0)
     {
       datarec[7-c]=1;
     }

     else{datarec[7-c]=0;}
     for(i=0;i<7;i++) {
            cout<<datarec[i];
    }

}
return 0;
}


