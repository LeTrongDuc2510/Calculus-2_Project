clc;
clf; 
s = linspace(0, 14, 30); 
s1 = meshgrid(s); 
t1 = [];
%calculate the value of y 
for i=1:length(s) 
    tam = linspace(0, 14-s(i), 30); 
    t1 = [t1 tam']; 
end 
x = s1; y = t1; z = 14-x-y; z1 = 0*x; x1 = 0*x; y1 = 0*x;
hold on 
%draw the solid is bounded by x,x1,y,y1,z,z1
surf(x, y, z, 'FaceColor', 'g', 'FaceAlpha' , 0.3); 
surf(x, y, z1, 'FaceColor', 'r', 'EdgeColor', 'none');
surf(x1, y, z, 'FaceColor', 'b', 'FaceAlpha' , 0.3); 
surf(x, y1, z, 'FaceColor', 'y', 'FaceAlpha' , 0.3); 
xlabel('x'); ylabel('y'); zlabel('z'); 
view(120, 12) 
grid on 
rotate3d on
%calculate the mass of the solid by using integral function
syms x y z
mass = int(int(int(2*y,z,0,14-x-y),y,0,14-x),x,0,14);
disp('The mass of the solid E is ');
disp(mass);