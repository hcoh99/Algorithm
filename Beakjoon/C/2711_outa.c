#include<stdio.h>
#include<string.h>
int main()
{
    char outa[80];
    int a_num; //전체넘버
    scanf("%d" , &a_num);
    int l_num;
    char str_list[a_num][80];

    for(int i = 0; i<a_num;i++)
    {
        scanf("%d %s" ,&l_num , outa );
        for (int j = l_num; j<=(int)strlen(outa);j++)
        {
            outa[j-1] = outa[j];
            //if (j==outa[((int)strlen(outa))-1])
            //{
            //    outa[((int)strlen(outa))-1] ='\0';
            //}
        
        }
        strcpy(str_list[i] , outa);
        outa[0] ='\0';
    }
    for (int i =0; i<a_num;i++)
    {
        printf("%s" ,str_list[i]);
        printf("\n");
    }


}