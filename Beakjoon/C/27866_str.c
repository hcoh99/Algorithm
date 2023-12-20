#include<stdio.h>
#include<string.h>

int main()
{

    char ss[100];
    scanf("%s" , ss);
    int k;
    scanf("%d" , &k);

    printf("%c" , ss[k-1]);

    return 0;
} 
