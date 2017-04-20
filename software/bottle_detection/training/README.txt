To start the training you have to create positive and negative images.

Open a terminal, go to this directory and type:

python3 img_capture.py pos 200 10

in order to create 200 positive images. 10 stands for every 10 tenth's of a second. So if you want to do a image every second type 10. Per image you want not more than 1 bottle!

To create negative images type:

python3 img_capture.py neg 400 5

in order to crate 400 negative images with a rate of every 0.5 seconds. This creates all the images in the folder negatives and a file neg.txt.

next run the matlabscript main.m to create pos.txt and postprocess the images.

At this point you should have the following files: 
 - README.txt
 - img_capture.py
 - start_training
 - pos.txt
 - neg.txt
 - negatives/
     - all negative images
 - positives/
     - all positive images

it is important to not have any other files in this folder. Since a directory data will be created, so if it does already exist there will be errors.

to start the training type and run the following:

./start_training numPos numNeg w h numPosTotal

replace the arguments by integers!
