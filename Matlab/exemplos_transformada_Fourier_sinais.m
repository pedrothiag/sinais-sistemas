clc
clear
close all

Ts = 1e-5;
t = 0:Ts:2;

x1 = exp(-2*t).*(t>=0 & t<=1.5);
[Xf1,f] = ctfs(x1,Ts);

figure,
subplot(211)
plot(t,x1,'k','Linewidth',1.0);
ylabel('{\itx}({\itt})')
xlabel('{\itt}')
set(gca,'FontName','Times')
subplot(212)
plot(f,abs(Xf1),'k','Linewidth',1.0);
ylabel('{\itX}({\itf})')
xlabel('{\itf}')
xlim([-30 30])
set(gca,'FontName','Times')

x1t = ictfs(Xf1,Ts);
figure,
plot(t,x1t,'k','Linewidth',1.0);
ylabel('{\itx}({\itt})')
xlabel('{\itt}')
set(gca,'FontName','Times')

x2 = sin(2*pi*10*t);
[Xf2,f] = ctfs(x2,Ts);

figure,
subplot(211)
plot(t,x2,'k','Linewidth',1.0);
ylabel('{\itx}({\itt})')
xlabel('{\itt}')
set(gca,'FontName','Times')
subplot(212)
plot(f,abs(Xf2),'k','Linewidth',1.0);
ylabel('{\itX}({\itf})')
xlabel('{\itf}')
xlim([-30 30])
set(gca,'FontName','Times')

x2t = ictfs(Xf2,Ts);
figure,
plot(t,x2t,'k','Linewidth',1.0);
ylabel('{\itx}({\itt})')
xlabel('{\itt}')
set(gca,'FontName','Times')