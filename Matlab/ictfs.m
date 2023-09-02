function x = ictfs(Xf1,Ts)
    x = Ts*ifft(ifftshift(Xf1));
end

