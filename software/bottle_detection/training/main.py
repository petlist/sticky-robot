# Autogenerated with SMOP 
from smop.core import *
# main.m


# Guide
# 1. Select one image in the folder containing all the images ->(2)
# 2. follow instruction in the title of the figure

folderPath='positives_to_process'
# main.m:10
img_pos=matlabarray(cat(0,0,1000,1000))
# main.m:12
#[fn0,pn0]=uigetfile({'*.jpg'},'Select image (*.jpg)');
listing=dir(folderPath)
# main.m:15
i=1
# main.m:17
name=getfield(listing,cellarray([i]),'name')
# main.m:18
while name[1] == '.':

    i=i + 1
# main.m:20
    name=getfield(listing,cellarray([i]),'name')
# main.m:21


h=figure('Name','Bottle selection')
# main.m:24

hold('on')
## rectangle selection
while i <= size(listing,1):

    I=imread(cat(folderPath,'/',getfield(listing,cellarray([i]),'name')))
# main.m:32
    imshow(I)
    set(gcf,'Name',cat('Window the bottle or click if no bottles - ',getfield(listing,cellarray([i]),'name')))
    rect[i - 2,:]=getrect
# main.m:37
    if rect[i - 2,3] != 0 and rect[i - 2,4] != 0:
        rectangle('Position',rect[i - 2,:],'EdgeColor','r')
        set(gcf,'Name',cat('click in the rectangle to validate - ',getfield(listing,cellarray([i]),'name')))
        x,y=ginput(1,nargout=2)
# main.m:44
        if rect[i - 2,1] <= x and x <= (rect[i - 2,1] + rect[i - 2,3]) and rect[i - 2,2] <= y and y <= (rect[i - 2,2] + rect[i - 2,4]):
            i=i + 1
# main.m:47
        else:
            #set(gcf,'Name',['Enter in cmd-line the image number you want to process - ',getfield(listing,{i}, 'name')])
        #i = 2+input(['Current img=',num2str(i-2),' you want to select imag : ']);
            pass
    else:
        set(gcf,'Name',cat('Window the bottle or click if no bottles - ',getfield(listing,cellarray([i]),'name')))
        rect[i - 2,:]=getrect
# main.m:56
        if rect[i - 2,3] == 0 or rect[i - 2,4] == 0:
            rect[i - 2,:]=zeros(1,4)
# main.m:59
            i=i + 1
# main.m:60
        else:
            rectangle('Position',rect[i - 2,:],'EdgeColor','r')
            set(gcf,'Name',cat('click in the rectangle to validate - ',getfield(listing,cellarray([i]),'name')))
            x,y=ginput(1,nargout=2)
# main.m:66
            if rect[i - 2,1] <= x and x <= (rect[i - 2,1] + rect[i - 2,3]) and rect[i - 2,2] <= y and y <= (rect[i - 2,2] + rect[i - 2,4]):
                i=i + 1
# main.m:69
            else:
                #rect(i-2,:) = zeros(1,4);
            #set(gcf,'Name',['Enter in cmd-line the image number you want to process - ',getfield(listing,{i}, 'name')])
            #i = input(['Current img=',num2str(i),' you want to select imag : ']);
                pass


close_('all')
## insert into txt file

fileID=fopen(cat('.','/pos.txt'),'w')
# main.m:86
sp=' '
# main.m:87
npos=1
# main.m:88
newdir=matlabarray(cat('.','/positives'))
# main.m:90
mkdir(newdir)
newdir=matlabarray(cat('.','/negatives_from_matlab'))
# main.m:93
mkdir(newdir)
for i in arange(3,size(listing,1)).reshape(-1):
    if rect[i - 2,3] != 0 and rect[i - 2,4] != 0:
        rectText=matlabarray(cat(num2str(round(rect[i - 2,1])),sp,num2str(round(rect[i - 2,2])),sp,num2str(round(rect[i - 2,3])),sp,num2str(round(rect[i - 2,4])),sp))
# main.m:98
        fprintf(fileID,cat('positives/',getfield(listing,cellarray([i]),'name'),sp,num2str(npos),sp,rectText,'\\n'))
        copyfile(cat(folderPath,'/',getfield(listing,cellarray([i]),'name')),cat('.','/positives/',getfield(listing,cellarray([i]),'name')))
    else:
        copyfile(cat(folderPath,'/',getfield(listing,cellarray([i]),'name')),cat('.','/negatives_from_matlab/',getfield(listing,cellarray([i]),'name')))

fclose(fileID)