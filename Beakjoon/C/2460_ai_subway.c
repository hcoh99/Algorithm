#include<stdio.h>

int main()
{
    int plus[10];
    int minus[10];
    int now[10];
    int tmp,Max=0;
    int i;


    for (i = 0; i<10;i++)
    {
        scanf("%d %d" , &minus[i] , &plus[i]);
        tmp = plus[i] - minus[i];
        if (i == 0)
        {
            now[0] = tmp;
        }
        else
        {
            now[i] = now[i-1] + tmp;
        }
        if (Max<now[i])
            Max = now[i];
        tmp = 0;
    }

    printf("%d" , Max);
}