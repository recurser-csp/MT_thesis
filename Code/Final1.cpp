#include<bits/stdc++.h>

using namespace std;

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

/*initializing positions of the char in the last column according to first column */


        int character[length+1];
        int x,y,z,a,b,temp3,temp4;

        for(i=1;i<=length;i++)
        {

            x= position[i];
            y= count[x];
            count[x]++;
            character[i]=y;
            if(i==y)
            {
                if(i<length || (length-1)%sigma==0)
                {
                    character[i]=character[i-1];
                    character[i-1]=y;

                    a=position[i-1];
                    b=position[i];
                    for(j=i;j<=length;j++)
                    {
                        if(position[j-1]==a && position[j]==b)
                        {
                            temp3= position[j-1];
                            position[j-1]=position[j];
                            position[j]=temp3;
                        }
                    }
                }
                else /*i==length and some char repeat more than some other */
                {
                    z= initial_count[temp2+1];
                    initial_count[temp2+1]=z+1;
                    character[i]=z;
                    for(j=1;j<length;j++)
                    {
                        if(character[j]>=z)
                            character[j]++;
                    //cout<<"\t"<<character[j];
                        if(character[j]==j)
                        {
                            a=position[j-1];
                            b=position[j];
                            for(k=j;k<=length;k++)
                            {
                                if(position[k-1]==a && position[k]==b)
                                {
                                    temp3= position[k-1];
                                    position[k-1]=position[k];
                                    position[k]=temp3;
                                    temp4= character[k-1];
                                    character[k-1]=character[k];
                                    character[k]=temp4;
                                }
                            }

                        }
                    }
                }
            }
        }



        int mark[length+1];
        label:
        memset(mark,0,sizeof(mark));

        int cycle_pos =1;
        int flag_1=0;
        flag_1=0;
        for(i=1;i<=length;i++)
        {

            if(character[cycle_pos]==1 && i<length)
            {
                j=cycle_pos +1;
                while(mark[j]!=0 && j<=cycle_pos + sigma)
                {
                    j++;
                }
                if(j>cycle_pos+sigma)
                {
                    j=cycle_pos-1;
                    while(mark[j]!=0 && j>= cycle_pos-sigma)
                    {
                        j--;
                    }
                    if(j<cycle_pos-sigma || j == 0)
                    {
                          for(k=1;k<=length;k++)
                        {
                            if(mark[k] == 0 && k!= cycle_pos)
                            {
                                if(character[k]!=k-1 && character[k-1]!=k)
                                {

                                    temp3 = character[k-1];
                                    character[k-1] = character[k];
                                    character[k] = temp3;
                                    goto label;
                                }
                                else if(character[k]!=k+1 && character[k+1]!=k)
                                {
                                    temp3 = character[k+1];
                                    character[k+1] = character[k];
                                    character[k] = temp3;
                                    goto label;

                                }
                                else
                                {
                                    cout<<sigma<<","<<length<<",";
                                    cout<<"-1,"<<endl;
                                    flag_1 = 1;

                                }
                            }
                        }
                    }
                }
                if(flag_1)break;
        //cout<<endl<<"j="<<j<<"\t";
                temp3= character[cycle_pos];
                character[cycle_pos]=character[j];
                character[j]=temp3;
            }
            if(flag_1)break;
            // cout<<cycle_pos<<"\t";
            mark[cycle_pos]=1;
            cycle_pos=character[cycle_pos];

        }
        if(flag_1)continue;
        // cout<<"success\n";
        // cout<<"character Array:\t";
        cout<<sigma<<","<<length<<",";
              for(i=1;i<=length;i++)
            cout<<character[i]<<",";
        cout<<endl;

    }
}
