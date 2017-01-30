/* File : fibonacci.c
 *
 * Implementation of the algorithm in C
 */
#include "fibonacci.h"

#include <stdio.h>  // printf()
#include <stdlib.h> // atoi()
#include <time.h>   // clock_t, clock()

int compute_fibonacci(int n)
{
    int temp;
    int a = 1;
    int b = 1;
    for (int x=0; x<n; x++)
    {
        temp = a;
        a += b;
        b = temp;
    }
    return a;
}

struct MsgMetaData populate_struct(dtype msgType, dtype jobId, dtype msgSize)
{
    struct MsgMetaData metaData;
    metaData.type = msgType;
    metaData.job = jobId;
    metaData.size = msgSize;
    return metaData;
}

int main(int argc, char *argv[])
{
    // Make this volatile to prevent compiler from completely optimizing out the loop
    volatile int n = 20;
    if (argc > 1)
    {
        n = atoi(argv[1]);
    }

    int number_of_times = 100000;
    if (argc > 2)
    {
        number_of_times = atoi(argv[2]);
    }

    int fib_n = compute_fibonacci(n);

    // Compute single execution time
    clock_t begin = clock();
    compute_fibonacci(n);
    clock_t end = clock();
    double single_time = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("single execution time: %.2g s\n", single_time);

    // Compute average execution time over many times
    double time_spent = 0;
    for (int i = 0; i < number_of_times; i++)
    {
        begin = clock();
        compute_fibonacci(n);
        end = clock();
        time_spent += (double)(end - begin) / CLOCKS_PER_SEC;
    }
    double avg_time = time_spent / number_of_times;

    printf("fib(%d) = %d  [average execution time: %.2g s]\n", n, fib_n, avg_time);


    // Create and populate a struct
    struct MsgMetaData myStruct = populate_struct(1, 2, 3);

    printf("msg type = %d,  job id = %d,  msg size = %d\n", myStruct.type, myStruct.job,
           myStruct.size);

    return EXIT_SUCCESS;
}
