function [Xf,f] = ctfs(x,Ts)
    Fs = 1/Ts;
    N = length(x);
    f = linspace(-Fs/2,Fs/2,N);
    
    Xf = 1/Ts*fftshift(fft(x));
end

