
% Guide
% 1. Select one image in the folder containing all the images ->(2)
% 2. follow instruction in the title of the figure



clearvars; close all; clc;

folderPath = 'positives_to_process';

img_pos = [0,0,1000,1000];

%[fn0,pn0]=uigetfile({'*.jpg'},'Select image (*.jpg)');
listing = dir(folderPath);

i = 1;
name = getfield(listing,{i}, 'name');
while name(1)=='.'
    i = i+1;
    name = getfield(listing,{i}, 'name');
end

h = figure('Name','Bottle selection');%,'Position',img_pos)
hold on



%% rectangle selection
while i <= size(listing,1)
    
    I = imread([folderPath,'/',getfield(listing,{i}, 'name')]);
    imshow(I);
    %set(h,'Position',img_pos);
    
    set(gcf,'Name',['Window the bottle or click if no bottles - ',getfield(listing,{i}, 'name')])
    rect(i-2,:) = getrect;
    
    if rect(i-2,3)~=0 && rect(i-2,4)~=0
        
        rectangle('Position',rect(i-2,:),'EdgeColor','r')
        
        set(gcf,'Name',['click in the rectangle to validate - ',getfield(listing,{i}, 'name')])
        [x,y]=ginput(1);
        
        if rect(i-2,1)<=x && x<=(rect(i-2,1)+rect(i-2,3)) && rect(i-2,2)<=y && y<=(rect(i-2,2)+rect(i-2,4))
            i = i+1;
        else
            %set(gcf,'Name',['Enter in cmd-line the image number you want to process - ',getfield(listing,{i}, 'name')])
            %i = 2+input(['Current img=',num2str(i-2),' you want to select imag : ']);
        end
        
    else
        
        set(gcf,'Name',['Window the bottle or click if no bottles - ',getfield(listing,{i}, 'name')])
        rect(i-2,:) = getrect;
        
        if rect(i-2,3)==0 || rect(i-2,4)==0
            rect(i-2,:) = zeros(1,4);
            i = i+1;
        else
            
            rectangle('Position',rect(i-2,:),'EdgeColor','r')
            
            set(gcf,'Name',['click in the rectangle to validate - ',getfield(listing,{i}, 'name')])
            [x,y]=ginput(1);
            
            if rect(i-2,1)<=x && x<=(rect(i-2,1)+rect(i-2,3)) && rect(i-2,2)<=y && y<=(rect(i-2,2)+rect(i-2,4))
                i = i+1;
            else
                %rect(i-2,:) = zeros(1,4);
                %set(gcf,'Name',['Enter in cmd-line the image number you want to process - ',getfield(listing,{i}, 'name')])
                %i = input(['Current img=',num2str(i),' you want to select imag : ']);
            end
            
        end
        
    end
 
end

close all;

%% insert into txt file

fileID = fopen(['.','/pos.txt'],'w');
sp = ' ';
npos = 1;

newdir = ['.','/positives']
mkdir(newdir)

newdir = ['.','/negatives_from_matlab']
mkdir(newdir)

for i = 3:size(listing,1)
    if rect(i-2,3)~=0 && rect(i-2,4)~=0
        rectText = [num2str(round(rect(i-2,1))),sp,num2str(round(rect(i-2,2))),sp,num2str(round(rect(i-2,3))),sp,num2str(round(rect(i-2,4))),sp];
        %fprintf(fileID, [getfield(listing,{i}, 'folder'),'/positives/',getfield(listing,{i}, 'name'),sp,num2str(npos),sp,rectText,'\n'])
        fprintf(fileID, ['positives/',getfield(listing,{i}, 'name'),sp,num2str(npos),sp,rectText,'\n'])
        copyfile([folderPath,'/',getfield(listing,{i}, 'name')],['.','/positives/',getfield(listing,{i}, 'name')])
    else
        copyfile([folderPath,'/',getfield(listing,{i}, 'name')],['.','/negatives_from_matlab/',getfield(listing,{i}, 'name')])
    end
end
fclose(fileID)