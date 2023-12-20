#include<stdio.h>
#include<string.h>
int main()
{
    int a_score , n_score=1;
    int all=0 ;
    char ox[80];
    scanf("%d" , &a_score);
    int rst[a_score];
    for (int i=0; i<a_score;i++)
    {
        scanf("%s" , ox);
        for (int j = 0; j <=(int)strlen(ox);j++)
        {
            if (ox[j] == 'O')
            {
                all = all+n_score;
                n_score++;
            }
            else if (ox[j] =='X')
            {
                n_score=0;
                all = all+n_score;
                n_score=1;
            }
            
        }
        rst[i] = all;
        all = 0;
        n_score = 1;
    }
    for(int i = 0; i<a_score;i++)
    {
        printf("%d\n"  , rst[i]);
    }

}