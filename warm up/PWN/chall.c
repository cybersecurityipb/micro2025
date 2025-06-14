#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct input{
    char buffer[100];
    long long int target;
};

int main(){
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);

    struct input variable;
    variable.target = 10;

    printf("Kata-kata hari ini : ");
    fgets(variable.buffer, 120, stdin);
    if (strlen(variable.buffer) > 64){
        printf("Aihh dikit lagi cakep tuh\n");
    } else if (variable.target != 10) {
        system("cat flag.txt");
    } else {
        printf("Wow\n");
    }

    return 0;
}
