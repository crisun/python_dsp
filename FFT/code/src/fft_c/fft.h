#ifndef __FFT_H__
#define __FFT_H__
 
typedef struct
{
  float real;
  float imag;
}complex;
 
#define PI 3.1415926535897932384626433832795028841971
#define a_len(a) sizeof(a)/sizeof(a[0]) 

///////////////////////////////////////////
void c_conj(complex in[], complex out[], int n);
void c_plus(complex a, complex b, complex *c);
void c_mul(complex a, complex b, complex *c);
void c_sub(complex a, complex b, complex *c);
void c_div(complex a, complex b, complex *c);
void c_abs(complex in[], float out[], int n);
void c_show(complex in[], int n);
void Wn_i(int n,int i,complex *Wn);

//method 1
void bit_rev_1(complex x[], int N);
//method 2
int ispow2(int n);
int nextpow2(int n);
void dec2bin(int n, int bin[], int N);
void filplr(int bin[], int N);
int bin2dec(int bin[], int N);
void bit_rev_2(complex x[], int N);

void fft(complex xn[], int N);
void ifft(complex Xk[], int N);
////////////////////////////////////////////

#endif
