#include <stdio.h>
// Should NOT generate warning
int main(){
    int x = 5;
    float y = x;
    float z = 0.5 + 1;
    printf("%d %f %f", x, y, z);
    return 1;
}
