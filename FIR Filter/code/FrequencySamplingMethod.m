close all;
clear;
clc;
%Sa(t)
fs=125;
N=1024;
t=0:3*pi/N:3*pi;
sa=sinc(t/pi);
plot(t/pi*fs,abs(sa));
xlabel('Frequency/MHz');
ylabel('Magnitude')
title('低通滤波器输出频谱')
grid on;
% fs=125;
% N=1024;
% t=0:pi/N:pi-pi/N;
% f=sinc(t/pi);
% plot(t/pi*fs,abs(f));
%plot(t(1:N/2)/pi*fs,20*log10(abs(f(1:N/2))));
%axis([0 fs/2 -60 2])
% xlabel('Frequency/MHz');
% ylabel('Magnitude/dB');
% title('补偿前的输出频谱')
% grid on;
%==============================================================
fs=125;%采样频率
fp=55;%通带边界频率
I=1;%过渡带插值
wp=fp*2/fs*pi;
N=128;N1=32;%N为频域采样点，N1为时域截断点数
t=0:2*pi/N:wp;
Np=length(t)-1;
Ns=N-2*Np-1;
%t=0:2*pi/N:wp;
% Np=fix(N*wp/(2*pi));%[0,wp]点数
% Ns=N-2*Np-1;%[wp,2pi-wp]阻带点数
%Hk=[ones(1,Np+1) zeros(1,Ns) -ones(1,Np+1)];
Hgk=[1./sinc(t/2/pi) zeros(1,Ns) -fliplr(1./sinc(t/2/pi))];%频域采样值
Hgk=Hgk(1:length(Hgk)-1);
Hgk(Np+2)=I;Hgk(N-Np)=-I;%过渡带插值
figure;
stem((0:1/N:1-1/N)*fs,Hgk);
title('频域抽样')
grid on;
%=============================================================
theta=-(N-1)*pi*(0:N-1)/N;%相位
Hk=Hgk.*exp(1i*theta);%构造采样值mag+phase
hn=real(ifft(Hk));%得到时域单位冲击响应
hn1=hn(N/2-N1/2+1:N/2+N1/2);%对hn做N1点截断
figure;%阶段前后对比图
subplot(311);
stem(hn);
title('h(n)')
subplot(312);
stem(hn1)
title('截断后h1 (n)')
hn1=hn1.*hamming(N1)';%对截断后序列加窗平滑
subplot(313);
stem(hn1);
title('加窗后h1 (n)')
figure;
freqz(hn1);
%=============================================================
N=1024;
Hw=fft(hn1,N);
wk=[0:N-1]/N*fs;
figure;
plot(wk(1:512),20*log10(abs(Hw(1:512))));
grid on;
axis([0 fs/2 -10 3])
xlabel('Frequency/MHz')
ylabel('Magnitude/dB')
title('补偿滤波器频率响应');
%============================================================
figure;
subplot(211);
N=1024;
t=0:pi/N:pi-pi/N;
f=sinc(t/pi);
plot(t(1:N/2)/pi*fs,20*log10(abs(f(1:N/2))));
axis([0 fs/2 -4 0.5])
xlabel('Frequency/MHz')
ylabel('Magnitude/dB')
title('补偿之前的输出频谱')
grid on;

fx=f.*abs(Hw);
subplot(212);
%1 db
plot(wk(1:512),20*log10(abs(fx(1:512))));
axis([0 fs/2  -10 2]);
%2
%plot(wk,abs(fx));
xlabel('Frequency/MHz')
ylabel('Magnitude/dB')
title('补偿之后的输出频谱')
grid on;
%===========================================================
Fs=125;
Fp=50;
order=31;
d = fdesign.isinclp('N,Fp,Ap,Ast',order,Fp/(Fs/2),0.01,20);
hd2 = design(d,'SincFrequencyFactor',0.5,'SincPower',1);
figure;
N=1024;
Hw2=fft(hd2.Numerator,N);
wk=[0:N-1]/N*Fs;
%plot(wk(1:N/2),abs(Hw2(1:N/2)));
plot(wk(1:N/2),20*log10(abs(Hw2(1:N/2))));
hold on;
%plot(wk(1:N/2),abs(Hw(1:N/2)));
plot(wk(1:N/2),20*log10(abs(Hw(1:N/2))));
legend('Matlab fdesign.isinclp','Frequency Sampling method','Location','best')
grid on;
xlabel('Frequency/MHz');
ylabel('Magnitude/dB');
figure;
Hw3=abs(Hw2-Hw);
plot(wk(1:N/2),Hw3(1:N/2));
%=========================================================================
hn2=round(hn1*(2^11-1));
%========================================================================
