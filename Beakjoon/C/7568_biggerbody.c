#include<stdio.h>

int main()
{
    int mem , cnt = 1;
    int weight[50];
    int height[50];
    int rank[50];

    scanf("%d" , &mem);

    for (int i = 0; i<mem;i++)
    {
        scanf("%d %d" ,&weight[i] , &height[i] );

    }
    for (int i = 0; i<mem;i++)
    {
        for(int j = 0; j<mem;j++)
        {
            if ((weight[i]<weight[j])&&(height[i]<height[j]))
            {
                cnt++;
            }
        }
        rank[i] = cnt;
        cnt = 1;
    }
    for (int i = 0; i<mem;i++)
    {
        printf("%d" , rank[i]);
        printf(" ");
    }
    

}