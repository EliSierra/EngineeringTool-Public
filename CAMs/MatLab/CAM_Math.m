%Cam Math
%Eli Sierra
%2025

clc
clear


base_radius=.5; %inches
travel_radius = 1.5; %inches
Thickness = 0.35; %inches
D1= 340; %degrees to Rise (starts at 0)
D2 = 345; %degrees to Dwell (starts at D1)
D3 = 350; %degrees to Fall (starts at D2)
D4 = 360; %Degrees to dwell (starts at D3 and should always end at 360)

Tri = 250; %number of triangles per section

% base_radius=base_radius*25.4; %inches conversion
% travel_radius =travel_radius*25.4; %inches conversion
% Thickness = Thickness *25.4; %inches conversion
%% zone 1: 0 to D1 degrees (Rise)

angle1=linspace(0,D1,Tri);


Y1=(travel_radius/2)*(1-cos((pi*angle1)/D1));
polarplot(angle1/180*pi,Y1+base_radius);
hold all

%% zone 2: D1 degrees to D2 degrees (Dwell)

angle2=linspace(D1,D2,Tri);

Y2=travel_radius+angle2*0;
polarplot(angle2/180*pi,Y2+base_radius);


%% Zone 3: D2 degrees to D3 degrees (Return)


angle3=linspace(D2,D3,Tri);

Y3=(travel_radius/2)*(1+cos((pi*(angle3-D2))/(D3-D2)));
polarplot(angle3/180*pi,Y3+base_radius);

%% Zone 4: D3 degrees to D4 (360) degrees (Dwell)

angle4=linspace(D3,D4,Tri);
Y4=0+angle4*0; %ignore the "+angle2*0" its just to get it into a proper string
pl = polarplot(angle4/180*pi,Y4+base_radius);

hold off
%% Convert to Cartesion 

[x1,y11]=pol2cart(angle1/180*pi,Y1+base_radius);
[x2,y12]=pol2cart(angle2/180*pi,Y2+base_radius);
[x3,y13]=pol2cart(angle3/180*pi,Y3+base_radius);
[x4,y14]=pol2cart(angle4/180*pi,Y4+base_radius);

xf=[x1 x2 x3 x4];
xf=[xf,0];
yf=[y11 y12 y13 y14];
yf=[yf,0]; %adding center point to the plot. Real length of Array is 4 * Tri
partialsize=size(yf);
z1=linspace(0,0,partialsize(1,2));
z2=linspace(Thickness,Thickness,partialsize(1,2));
zf=[z1 z2]';
figure
plot(xf,yf);
ylim([-2 2]);

xyf=[xf xf;yf yf;z1 z2]';
%% Convert to Cartesion Bad
% 
% x1= Y1+base_radius .* cos(angle1/180*pi);
% y11= Y1+base_radius .* sin(angle1/180*pi);
% 
% x2= Y2+base_radius .*cos(angle2/180*pi);
% y12= Y2+base_radius .*sin(angle2/180*pi);
% 
% x3= Y3+base_radius .*cos(angle3/180*pi);
% y13=Y3+base_radius .*sin(angle3/180*pi);
% 
% x4= Y4+base_radius .*cos(angle4/180*pi);
% y14= Y4+base_radius .*sin(angle4/180*pi);
% 
% 
% figure 
% plot(xf,yf)

%% Convert to STL


P=[xf;yf]';
P=[P; P];
P=[P zf]; %All of my points from Cartesion plot

%Lower
n1=linspace(1,partialsize(1,2)-2,partialsize(1,2)-2);
n2=linspace(2,partialsize(1,2)-1,partialsize(1,2)-2);
n3=linspace(partialsize(1,2),partialsize(1,2),partialsize(1,2)-2);
Lower=[n1 n2 n3];

%Upper                4002              8000                3999
n4=linspace(partialsize(1,2)+1,partialsize(1,2)*2-2,partialsize(1,2)-2); %add one to account for center node
n5=linspace(partialsize(1,2)+2,partialsize(1,2)*2-1,partialsize(1,2)-2); 
n6=linspace(partialsize(1,2)*2,partialsize(1,2)*2,partialsize(1,2)-2); %Center node
upper=[n4 n5 n6];

nf=[n1 n4 n1 n4;n2 n5 n2 n5;n3 n6 n4 n2]';
%nf=[nf; n4 n5 n6];
nf=[nf;1 partialsize(1,2)-1 partialsize(1,2)];
nf=[nf;partialsize(1,2)+2 partialsize(1,2)*2-1 partialsize(1,2)*2];
%nf=[nf;100 1 2];

%% Connecting High to Low



TR = triangulation(nf,P);

stlwrite(TR,'cam.stl','text')

%% Convert to STEP (Doesn't work)

%igesout(xyf,'Cam.stp')