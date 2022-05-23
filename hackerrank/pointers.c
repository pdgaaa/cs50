#include <stdio.h>
#include <math.h>

void update(int *a,int *b) {
    // Complete this function    
    int sum = *a + *b;
    int absolute_diff = sqrt(pow(*a - *b, 2));
    *a = sum;
    *b = absolute_diff;
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
