#include <stdio.h>
#include <string.h>
#include <stddef.h>

#ifdef PUBLIC_BUILD
    #define FLAG "HackTWK{FAKE_FLAG}"
#else
    #define FLAG "HackTWK{7H12_W42_4_S1mpl3_0v3rFLOW}"
#endif

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
    
    char secret_password[32] = {0x30, 0x4C, 0x66, 0x38, 0x59, 0x64, 0x54, 0x44, 0x6B, 0x34, 0x6F, 0x69, 0x43, 0x66, 0x63, 0x75, 0x42, 0x48, 0x4C, 0x61, 0x74, 0x56, 0x79, 0x30, 0x58, 0x54, 0x63, 0x6B, 0x5A, 0x43, 0x47, 0x51};

    printf("Please enter a username: ");
    fgets(user.username, sizeof(user.username), stdin);
    user.username[strcspn(user.username, "\r\n")] = '\0';

    if(string_compare(&user.username,&secret_username) == 0) {
        printf("Access denied!\n");
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
        if ((*str1)[i] != (*str2)[i]) {
            return 0;
        }
    }

    return 1;
}
