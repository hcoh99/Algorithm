#include<stdio.h>

int main()
{
    int A , B ,C,t=0;
    int i;
    int num[10]={0};

    scanf("%d" , &A);
    scanf("%d" , &B);
    scanf("%d" , &C);

    t = A*B*C;

    do
    {
        num[t%10]++;
        t = t/10;
    } while (t!=0);
    
    for(i=0;i<10;i++)
    {
        printf("%d" , num[i]);
        printf("\n");
    }

}