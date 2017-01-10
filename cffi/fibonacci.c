/* File : fibonacci.c
 *
 * Implementation of the algorithm in C to be compiled to a dynamic library
 */

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
