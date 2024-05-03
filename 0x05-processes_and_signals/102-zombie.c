#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/* Function to create zombie processes 
 * Create 5 child processes 
 * Parent process 
 * Child process 
 * Error 
 **/
int create_zombies(void)
{
    pid_t child_pid;

    
    for (int i = 0; i < 5; i++) {
        child_pid = fork();

        if (child_pid > 0) {
            
            printf("Zombie process created, PID: %d\n", child_pid);
        } else if (child_pid == 0) {
            
            exit(0);
        } else {
            
            perror("fork");
            return 1;
        }
    }

    return 0;
}

int infinite_while(void)
{
    while (1) {
        sleep(1);
    }
    return (0);
}

int main(void)
{
    
    create_zombies();
    infinite_while();

    return 0;
}
