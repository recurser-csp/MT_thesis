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
        // cout<<sigma<<","<<length<<",";
        // for(i=1;i<=length;i++)
        // {
        //     cout<<position[i]<<",";
        // }
        // cout<<endl;
/*initializing positions of the char in the last column according to first column */


        int character[length+1],ref[length+1],mark[length+1];
        memset(mark,0,sizeof(mark));       
        int x,y,z,a,b,temp3,temp4;
        int pos = 1;
        int t;
        int flag_1=0;
        mark[1] =1;
        for(i=1;i<length;i++)
        {
            if(mark[count[position[pos]]] == 0 && count[position[pos]]<=length && isvalid(position[pos],initial_count,count,sigma))
            {
                character[pos] = count[position[pos]];
                ref[pos] = position[pos];
                count[position[pos]]++;
                pos = character[pos];
                mark[pos] = 1;     
            }
            else
            {
                t = position[pos];
                for(x = 1;x<=sigma;x++)
                {
                    t--;
                    if(t<=0)
                    {
                        t = sigma;
                    }
                    // cout<<t<<endl;
                    if(mark[count[t]] == 0 && count[t]<=length && isvalid(t,initial_count,count,sigma))
                    {
                        character[pos] = count[t];  
                        ref[pos] = t;  
                        count[t]++;
                        pos = character[pos];
                        flag_1=1;
                        mark[pos] = 1; 
                        break;    
                    }

                }
                if(flag_1==0)
                {
                    cout<<"Failed";
                    exit(1);
                }
            }
        }
        character[pos] = 1;
        ref[pos] = 0;
        // cout<<endl;
        // cout<<sigma<<","<<length<<",";
 
        // for (int i = 1; i <=  length; ++i)
        // {
        //     cout<<character[i]<<",";

        // }
        // cout<<endl;

        int start_index = 0;
        int ibwt[length+1];
        j = length-1;
        ibwt[length] = 1;
        i = 1;
        while(character[i]!=1)
        {
            ibwt[j] = character[i];
            i = character[i];
            j--;

        }
        // for(i=1;i<=length;i++)
        //     cout<<ibwt[i]<<",";
        // cout<<endl;


        int f = 0;
        for(i = 1; i<=length;i++)
        {
            f = 0;
            for(j = 0;j<=sigma;j++)
            {
                if(ibwt[i]<initial_count[j])
                {
                    // cout<<character[i]<<" "<<initial_count[j]<<endl;
    
                    f=1;

                }
                if(f==1)break;
            }
            ibwt[i] = j-1;
        
        }
                cout<<sigma<<","<<length<<",";

                for(i=1;i<=length;i++)
            cout<<ibwt[i]<<",";
        cout<<endl;


        // cout<<endl;
        // cout<<sigma<<","<<length<<",";
 
        // for (int i = 1; i <=  length; ++i)
        // {
        //     cout<<ref[i]<<",";

        // }
        // cout<<endl;



    }
}