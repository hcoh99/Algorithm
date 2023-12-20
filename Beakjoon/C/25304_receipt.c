#include<stdio.h>

int main()
{
    int t_price ,p=0;
    int t_num ;
    int price[100];
    int num[10];

    scanf("%d" , &t_price);
    scanf("%d" , &t_num);

    for (int i = 0; i<t_num; i++)
    {
        scanf("%d %d" , &price[i] , &num[i]);
        p = p + (price[i] * num[i]);
    }

    if (t_price == p)
    {
        printf("Yes");
    }
    else
    {
        printf("No");
    }

}