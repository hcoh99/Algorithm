#include<stdio.h>

int main()
{
    int num[100]={0};
    int hap = 0 , tm;
    int avg , max=0 ,rst = 0;

    for (int i = 0;i<10;i++)
    {
        scanf("%d" , &tm);
        hap = hap+tm;
        tm = tm/10;
        num[tm]++;
        tm=0;
    }
    avg = hap/10;

    for (int i=0; i<100;i++)
    {
        if (max<num[i])
        {
            max = num[i];
            rst = i*10;
        }
        
    }
        printf("%d\n" , avg);
        printf("%d" , rst);
}