#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include "fft.h"

void c_conj(complex in[], complex out[], int n)
{
  int i = 0;
  for(i = 0; i < n; i++)
  {
    out[i].real = in[i].real;
    out[i].imag = -in[i].imag;
  } 
} 
 
void c_plus(complex a, complex b, complex *c)
{
  c->real = a.real + b.real;
  c->imag = a.imag + b.imag;
}
 
void c_sub(complex a, complex b, complex *c)
{
  c->real = a.real - b.real;
  c->imag = a.imag - b.imag;    
}
 
void c_mul(complex a, complex b, complex *c)
{
  c->real = a.real * b.real - a.imag * b.imag;
  c->imag = a.real * b.imag + a.imag * b.real;  
}
 
void c_div(complex a, complex b, complex *c)
{
  c->real = (a.real * b.real + a.imag * b.imag) / (b.real * b.real +b.imag * b.imag);
  c->imag = (a.imag * b.real - a.real * b.imag) / (b.real * b.real +b.imag * b.imag);
}

void c_abs(complex in[], float out[], int n)
{
  int i = 0;
  float t;
  for(i = 0; i < n; i++)
  {
    t = in[i].real * in[i].real + in[i].imag * in[i].imag;
    out[i] = sqrt(t);
  } 
}

void c_show(complex in[], int n){
    int i;
    printf("[");
    for ( i = 0; i < n; i++)
    {
        if(( i != 0 ) && ( i % 4 == 0 ))
            printf("\n");
        printf("\t%f+%fj", in[i].real, in[i].imag);
    }
    printf("\t]\n");
    
}

//Wn_i=e^{-j2*pi*i/n}=cos(2*pi*i/n)-jsin(2*pi*i/n)
void Wn_i(int n,int i,complex *Wn)
{
  Wn->real = cos(2*PI*i/n);
  Wn->imag = -sin(2*PI*i/n);
}

//ispow2 : whether a number is the power of 2
//paramter
//n : a number, int
//return
//1 for True or 0 for False
int ispow2(int n){
    if((n & (n - 1))==0){
        return 1;
    } else {
        return 0;
    }
}

//nextpow2 : to get a next power2 of N
//parameter
// n : a num, int
//return 
// next power of n, int
int nextpow2(int n){
    return pow(2,ceil(log2(n)));
}

//dec2bin : decimal -> binary
//parameter
//  n: number in decimal,int
//bin: binary array, int []
//  N: length of bin, int
void dec2bin(int n,int bin[], int N){
    int rem;
    int i;
    for (i = 0; i < N; i++)
    {   
        bin[N-1-i]=n%2;
        n=n/2;
    }    
}

//filplr : flip a number from left to right
//parameter
//bin: binary array, int[]
//  N: length of bin, int
void filplr(int bin[], int N){
    int i,j,tmp;
    for (i = 0, j=N-1; i < N/2; i++,j--)
    {
        tmp=bin[i];
        bin[i]=bin[j];
        bin[j]=tmp;
    }
}

//bin2dec : binary -> decimal
//parameter
//bin:binary array, int[]
//  N:length of bin, int
int bin2dec(int bin[], int N){
    int i;
    int n=0;

    for ( i = 0; i < N; i++)
    {
        n += bin[i] * pow(2,N-1-i);
    }
    return n;
}

//bit_rev_2 : to get a bit_reversed order of a complex number array
//parameter
// x : input array, complex []
// N : length of x 
void bit_rev_2(complex x[], int N){
    int i;
    int N1=log2(N);
    complex t[N];
    int tmp[N1];

    for ( i = 0; i < N; i++){
        t[i]=x[i];//copy xn to tmp
    }

    for(i=0;i < N;i++){
        dec2bin(i,tmp,N1);//dec2bin(0~N-1)
        filplr(tmp,N1);//filp left to right 
        x[i]=t[bin2dec(tmp,N1)];//generate new xn with bit_reversed order
    }
}

void bit_rev_1(complex x[], int N){
    int i,j,k;
    complex t;
    for(i=1,j=N/2;i<N-1;i++)
    {
        if(i<j)
        {
            t=x[j];
            x[j]=x[i];
            x[i]=t;
        }
        k=N/2;
        while(k<=j)
        {
            j=j-k;
            k=k/2;
        }
        j=j+k;
    }
}

//Fast Fourier Transform
void fft(complex xn[], int N)
{
  complex t,wn;//中间变量
  int n,l,r;
  int la,lb,lc;
  int level,levels;
  
  //bit-reverse order input
  bit_rev_2(xn, N);
  //bit_rev_2(xn, N);

  levels=log2(N);//total level
  
  //main loop
  for(level=1;level<=levels;level++)
  {
    la=pow(2, level); //la=2^m代表第m级每个分组所含节点数     
    lb=la/2;    //lb代表第m级每个分组所含碟形单元数
                 //同时它也表示每个碟形单元上下节点之间的距离
    /*----碟形运算----*/
    for(l=1;l<=lb;l++)
    {
      r=((l-1)*pow(2,levels-level)); 
      for(n=l-1;n<N-1;n=n+la) //遍历每个分组，分组总数为N/la
      {
        lc=n+lb;  //n,lc分别代表一个碟形单元的上、下节点编号     
        Wn_i(N,r,&wn);//wn=Wnr
        c_mul(xn[lc],wn,&t);//t = f[lc] * wn复数运算
        c_sub(xn[n],t,&(xn[lc]));//f[lc] = f[n] - f[lc] * Wnr
        c_plus(xn[n],t,&(xn[n]));//f[n] = f[n] + f[lc] * Wnr
      }
    }
  }
}
 
//inverse fast fourier transform
void ifft(complex Xk[], int N)
{
  int i;
  c_conj(Xk, Xk, N);//Xk*
  fft(Xk, N);//do N-pt fft for Xk*
  c_conj(Xk, Xk, N);//conjugate for the res
  for(i = 0; i < N; i++)
  {
    Xk[i].imag = (Xk[i].imag) / N;
    Xk[i].real = (Xk[i].real) / N;
  }
}
