# violence-and-garbage-detection
A python + flask application which runs YOLOv5 models on videos by splitting the video into images, calling therespective APIs and then merging the frames into an image.

boundOutput has all the images with a bounded box after the model is run on all the images which are in imageOutput; created by splitting the video into image frames. These folders get empited after the process is completed. Templates contains all the frontend stuff for the application

To run the model on the video, add a .mp4 file in the same folder and then select that file in the application, along with the number of frames you want to skip while creating the model and the model you want to train. More frames skipped = lesser time.  The output file will also be generated in this folder.
