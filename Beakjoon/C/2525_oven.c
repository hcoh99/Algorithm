#include<stdio.h>


int main()
{
    int h , m , w;
    int hour , nm , nh;
    scanf("%d %d" , &h , &m);
    scanf("%d" , &w);

    if(m+w>=60)
    {
        hour = (m+w) /60;
        nh=h + hour;
        nm = (m+w) % 60;
        if (nh>23)
        {
            nh = nh-24;
        }
    }
    else
    {
        nm = m+w;
        nh = h;
    }
    printf("%d %d" , nh , nm);
}
