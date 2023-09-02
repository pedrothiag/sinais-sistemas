clc
clear
close all

w = [315 943 1888];
qsi = [0.066 0.033 0.058];

num1 = [1/(w(1)^2) -2*qsi(1)/w(1) 1];
dem1 = [1/(w(1)^2) 2*qsi(1)/w(1) 1];
sys1 = tf(num1,dem1);

num2 = [1/(w(2)^2) -2*qsi(2)/w(2) 1];
dem2 = [1/(w(2)^2) 2*qsi(2)/w(2) 1];
sys2 = tf(num2,dem2);

num3 = [1/(w(3)^2) -2*qsi(3)/w(3) 1];
dem3 = [1/(w(3)^2) 2*qsi(3)/w(3) 1];
sys3 = tf(num3,dem3);

syseq12 = series(sys1,sys2);
sys = series(syseq12,sys3);

b = cell2mat(sys.numerator);
a = cell2mat(sys.denominator);

wf = linspace(0,400*2*pi,400*2*pi + 1);
h = freqs(b,a,wf);
mag = abs(h);
phase = angle(h);
phasedeg = phase;

delaygroup = -1.0*diff(unwrap(phasedeg));

figure,
subplot(2,1,1)
plot(wf/(2*pi),mag,'k','Linewidth',1.0)
grid on
xlabel('{\itf} (Hz)')
ylabel('|{\itH}({\itf})|')
yticks([1])
set(gca,'FontName','Times')
set(gca,'FontSize',10)
subplot(2,1,2)
plot(wf/(2*pi),phasedeg,'k','Linewidth',1.0)
grid on
xlabel('{\itf} (Hz)')
ylabel('\angle{\itH}({\itf}) (rad)')
set(gca,'FontName','Times')
set(gca,'FontSize',10)
set(gcf,'Position',[300 300 800 450])

figure,
subplot(2,1,1)
plot(wf/(2*pi),unwrap(phasedeg),'k','Linewidth',1.0)
grid on
xlabel('{\itf} (Hz)')
ylabel('\angle{\itH}({\itf}) (rad)')
set(gca,'FontName','Times')
set(gca,'FontSize',10)
subplot(2,1,2)
plot(wf(1:end-1)/(2*pi),delaygroup,'k','Linewidth',1.0)
grid on
xlabel('{\itf} (Hz)')
ylabel('grad\{\angle{\itH}({\itf})\} (s)')
set(gca,'FontName','Times')
set(gca,'FontSize',10)
set(gcf,'Position',[300 300 800 450])

Ts = 1e-5;
T = 0.1;
t = 0:Ts:T;
w_hamm = 0.54 - 0.46*cos(2*pi*t/T);
x1 = cos(2*pi*80*t).*w_hamm;
x2 = cos(2*pi*180*t).*w_hamm;
x3 = cos(2*pi*330*t).*w_hamm;
x = [zeros(1,5000) x1 x2 x3 zeros(1,10000)];
tc = (0:length(x)-1)*Ts;
Fs = 1/Ts;
N = length(x);
f = linspace(-Fs/2,Fs/2,N); 
Xf = 1/Ts*fftshift(fft(x));

figure,
subplot(2,1,1)
plot(tc,x,'k','Linewidth',1.0);
grid on
xlabel('{\itt} (s)')
ylabel('{\itx}({\itt})')
set(gca,'FontName','Times')
set(gca,'FontSize',10)
xlim([0 max(tc)])
subplot(2,1,2)
plot(f,abs(Xf),'k','Linewidth',1.0);
grid on
xlabel('{\itf} (Hz)')
ylabel('|{\itX}({\itf})|')
set(gca,'FontName','Times')
set(gca,'FontSize',10)
xlim([0 400])
set(gcf,'Position',[300 300 800 450])

y = lsim(sys,x,tc);
 
figure,
subplot(2,1,1)
plot(tc,y(1:length(tc)),'k','Linewidth',1.0);
grid on
xlabel('{\itt} (s)')
ylabel('{\ity}({\itt})')
set(gca,'FontName','Times')
set(gca,'FontSize',10)
xlim([0 max(tc)])
ylim([-1 1])
subplot(2,1,2)
plot(tc,x,'k','Linewidth',1.0);
grid on
xlabel('{\itt} (s)')
ylabel('{\itx}({\itt})')
set(gca,'FontName','Times')
set(gca,'FontSize',10)
xlim([0 max(tc)])
ylim([-1 1])
set(gcf,'Position',[300 300 800 450])