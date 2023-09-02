clc
clear
close all

Ts = 1e-5;
Fs = 1/Ts;
t = 0:Ts:1;
N = length(t); 
f = linspace(-Fs/2,Fs/2,N);

Fm = 1000;
xm = cos(2*pi*Fm*t);
Fc = 10000;
xc = cos(2*pi*Fc*t);

figure,
set(gcf,'Position',[100 100 700 400])
subplot(211)
plot(t,xm,'k','Linewidth',1.0)
xlim([0.1 0.103])
xlabel('{\it t} (s)')
ylabel('{\it x_m}({\itt})')
set(gca,'FontName','Times')
subplot(212)
plot(t,xc,'k','Linewidth',1.0)
xlim([0.1 0.103])
xlabel('{\it t} (s)')
ylabel('{\it x_c}({\itt})')
set(gca,'FontName','Times')

x = xm + xc;
y = x + x.^2;

figure,
set(gcf,'Position',[100 100 700 400])
plot(t,y,'k','Linewidth',1.0)
xlim([0.1 0.103])
xlabel('{\it t} (s)')
ylabel('{\it y}({\itt})')
set(gca,'FontName','Times')

 
Yw = fftshift(fft(y));

figure,
set(gcf,'Position',[100 100 700 400])
plot(f,abs(Yw),'k','Linewidth',1.0);
xlabel('{\it f} (Hz)')
ylabel('|{\itY}({\itf})|')
set(gca,'FontName','Times')

Yfilter = bandpass(y,[Fc-Fm-1000 Fc+Fm+1000],Fs);

figure,
set(gcf,'Position',[100 100 700 400])
plot(t,Yfilter,'k','Linewidth',1.0)
xlim([0.1 0.103])
xlabel('{\it t} (s)')
ylabel('{\it y_f}({\itt})')
set(gca,'FontName','Times')
  
Yw = fftshift(fft(Yfilter));

figure,
set(gcf,'Position',[100 100 700 400])
plot(f,abs(Yw),'k','Linewidth',1.0);
xlabel('{\it f} (Hz)')
ylabel('|{\itY_f}({\itf})|')
set(gca,'FontName','Times')

r = (Yfilter).^2;   

Rw = fftshift(fft(r));
figure,
set(gcf,'Position',[100 100 700 400])
plot(f,abs(Rw),'k','Linewidth',1.0);
xlabel('{\it f} (Hz)')
ylabel('|{\itR}({\itf})|')
set(gca,'FontName','Times')

rFilter = lowpass(r,Fm,Fs,'Steepness',0.98);
RFilterw = fftshift(fft(rFilter));

figure,
set(gcf,'Position',[100 100 700 400])
plot(f,abs(RFilterw),'k','Linewidth',1.0);
xlabel('{\it f} (Hz)')
ylabel('|{\itR_f}({\itf})|')
set(gca,'FontName','Times')

figure,
set(gcf,'Position',[100 100 700 400])
plot(t,rFilter,'k','Linewidth',1.0)
xlim([0.1 0.103])
xlabel('{\it t} (s)')
ylabel('{\it r_f}({\itt})')
set(gca,'FontName','Times')