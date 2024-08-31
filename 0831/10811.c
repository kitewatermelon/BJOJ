#include <stdio.h>

int main()
{   
    int n, m;
    scanf("%d %d", &n, &m);
    int arr[n];
    for (int i = 0; i < n; i++)
        arr[i] = i+1;
    
    for (int i = 0; i < m; i++)
    {
        int a, b;
        scanf("%d %d", &a, &b);
        a--; b--;
        while (a < b)
        {
            int temp = arr[a];
            arr[a] = arr[b];
            arr[b] = temp; 
            a++ ; b--;
        }
    }
    
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);

    return 0;
}
