#include <stdio.h>
#include <string.h>
#include <stddef.h>

#define FLAG "the flag isnt here"

__attribute__((naked)) void pop_rdi_ret() {
    __asm__("pop %rdi; ret");
}

int string_compare(char (*str1)[], char (*str2)[]);

typedef struct {
    char username[32];
    char password[32];
    int is_admin;
} User;

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);

    User user;
    user.is_admin = 0;

    char secret_username[32] = "HackTWK";
    
    char secret_password[32] = "abcdefghijklmnopqrstuvwxyz123456";

    printf("Please enter a username: ");
    fgets(user.username, sizeof(user.username), stdin);
    user.username[strcspn(user.username, "\r\n")] = '\0';



    if(string_compare(&user.username,&secret_username) == 0) {
        printf("Access denied!\n");
        printf("You typed: %s, but required was %s\n", user.username, secret_username);
        return 0;
    }



    printf("Please enter a password: ");

    gets(user.password);

    user.password[strcspn(user.password, "\n")] = '\0';

    if (string_compare(&user.password,&secret_password) == 1 && user.is_admin != 0) {
        printf("Access granted! Hier ist deine Flagge: %s\n", FLAG);
        return 0;
    } else if (string_compare(&user.password,&secret_password) == 1){
        printf("You are not Admin. Bye!\n");
    } else {
        printf("Nothing to see here. Bye!\n");
    }
    return 0;
}


int string_compare(char (*str1)[32], char (*str2)[32]) {
    size_t size1 = sizeof(*str1);
    size_t size2 = sizeof(*str2);

    if (size1 != size2) {
        return 0;
    }

    //printf("String is: %zu chars long\n", size1);
    
    for (size_t i = 0; i < size1; i++) {
        //printf("Str1: %hhX -- Str2: %hhX\n",(*str1)[i], (*str2)[i]);
        if ((*str1)[i] != (*str2)[i]) {
            return 0;
        }
        if((*str1)[i] == 0x00 && (*str2)[i] == 0x00) {
            return 1;
        }
    }

    return 1;
}
