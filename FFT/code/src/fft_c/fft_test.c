#include <stdio.h>
#include <math.h>
#include <time.h>
#include "fft.h"

#define N 128

int main(int argc, char const *argv[]){
    //test 1 
    int i,j;
    int N1=1000,N2=10000;
    clock_t start,end;
    complex xn[N];
    for(i = 0; i < N; i++){
        if(i>=N/2){
            xn[i].real = 0;
            xn[i].imag = 0;
        }else{
            xn[i].real = 1;
            xn[i].imag = 0;
        }
    }
    //c_show(xn, N);
    i=0,j=0;//100轮，一轮1000遍
    start = clock();
    for ( j = 0; j < N1 ; j++)
    {
        while(i<N2){
            fft(xn, N);
            i++;
        }
    }
    end = clock();
    //c_show(xn, N);
    printf("total time of all times:\t %f s\n",(double)(end-start)/CLOCKS_PER_SEC);
    printf("avg time of 1000 times:\t %f ms\n",(double)(end-start)/N1);
    printf("avg time of 1 time:\t %f ms\n",(double)(end-start)/N1/N2);
    
    //test 2
    // int i,j;
    // for ( i = 0; i < N ; i++)
    // {
    //     printf("%d\t",i);
    // }
    // printf("\n");
    // for ( i = 0; i < N ; i++){
    //     if (ispow2(i)==1){
    //         printf("%d\t",i);
    //     }else{
    //         j = nextpow2(i);
    //         printf("%d\t",j);
    //     }
    // }

    //test 3
    // int a[4]={0,1,0,1};
    // int b;
    // b=bin2dec(a);
    // printf("%d\n",b);
    // int a[N]={0};
    // complex b[N];
    // int i,j,res;
    
    // for ( i = 0; i < N; i++)
    // {
    //     b[i].real=i;
    //     b[i].imag=0;    
    // }
    // c_show(b,N);
    // bit_rev_2(b,N); 
    // c_show(b,N);
    // return 0;
}
