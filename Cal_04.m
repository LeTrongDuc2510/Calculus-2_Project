clc;
clf;
hold on;
phi = linspace(0,2*pi,30); r = linspace(0,sqrt(13),30);%Output spaced valures of phi and r.
[r, phi] = meshgrid(r,phi); %transforms the domain specified by vectors r and phi into arrays r and phi
x = r.*cos(phi); y = r.*sin(phi);
z = 14- x.^2- y.^2; z1 = cos(phi).^2+sin(phi).^2; 
surf(x,y,z,'FaceColor','g','FaceAlpha',0.3);%draw the plane is bounded by x,y,z
surf(x,y,z1,'FaceColor','b','FaceAlpha',0.3);%draw the plane is bounded by x,y,z1
phi=linspace(0,2*pi,30); z2=linspace(0,1,30);
[z2, phi] = meshgrid(z2,phi);%transforms the domain specified by vectors z2 and phi into arrays z2 and phi
x1=sqrt(13).*cos(phi); y1=sqrt(13).*sin(phi);
surf(x1,y1,z2,'FaceColor','r','FaceAlpha',0.3);%draw the plane is bounded by x1,y1,z2
xlabel('x'); ylabel('y'); zlabel('z');
view (13,28)
grid on
rotate3d on
%calculate the flux
fun = @(a,b,c) 1 + 0.*a;
xmin = -sqrt(13);
xmax = sqrt(13);
ymin = @(a)-sqrt(13 - a.^2);
ymax = @(a) sqrt(13 - a.^2);
zmin = @(a,b) 1 + 0.*a;
zmax = @(a,b) 14 - a.^2 - b.^2;
q = integral3(fun,xmin,xmax,ymin,ymax,zmin,zmax,'Method','tiled');
disp(['The flux F is ' , num2str(q)]);