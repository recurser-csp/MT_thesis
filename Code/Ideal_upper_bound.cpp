#include<bits/stdc++.h>
// #include<stdio.h>

using namespace std;
int isvalid(int a,int *i_c,int *c,int s)
{

    if(c[a]<i_c[a+1] || a == s)
    {
        // cout<<"valid\n";
        return 1;
    }
    else
    {
        // cout<<"invalid\n";
        return 0;
    }

}

int main(int argc, char *argv[])
{
    int sigma,length,limit;
    cin>>sigma>>length>>limit;



    while(length<limit)
    {
        length++;
/* initializing initial position of all different char in first column */
        // cout<<length<<endl; //my_code
        int c1,c2;
        c1=(length-1)/sigma;  //4.2.2
        c2= (length-1)%sigma;
        int initial_count[sigma+1],count[sigma+1], position[length+1];
        initial_count[0]=1;
        count[0]=1;
        initial_count[1]=2;
        count[1]=2;


        int i,j,k,temp1=0;
        for(i=2;i<=sigma;i++)
        {
            if(temp1>=1)
            {
                initial_count[i]=2+(i-1)*c1+temp1;
                count[i]=2+(i-1)*c1+temp1;
                temp1++;
            }
            else
            {
                initial_count[i]=2+(i-1)*c1;
                count[i]=2+(i-1)*c1;
                if(c2/(sigma-i+1)>0)
                    temp1=1;
            }

        }
        // cout<<endl<<"count array: \t";
        // for(i=0;i<=sigma;i++)
        // {
        //     cout<<count[i]<<" ";
        // }
/* initializing which char should come (from the sigma different char) at the last column */

        int temp2=sigma,flag=0;
        for(i=1;i<=length;i++)
        {
            position[i]=temp2;
            //cout<<position[i]<<"\t";
            temp2--;
            if(temp2<1)
            {
                if(flag==0)
                    flag=1;
                else
                    temp2=sigma;
            }
        }
        cout<<sigma<<","<<length<<",";
        for(i=1;i<=length;i++)
        {
            cout<<position[i]<<",";
        }
        cout<<endl;



    }
}