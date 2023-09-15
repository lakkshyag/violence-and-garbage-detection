import cv2
import os
from roboflow import Roboflow
import webbrowser


def delete_files_in_directory(directory_path):
   try:
     files = os.listdir(directory_path)
     for file in files:
       file_path = os.path.join(directory_path, file)
       if os.path.isfile(file_path):
         os.remove(file_path)
     print("All files deleted successfully.")
   except OSError:
     print("Error occurred while deleting files.")


def detector(frames, file, ty):
    videoInput = file
    capture = cv2.VideoCapture(videoInput)
 
    frameNr = 0
 
    while (True):
 
        success, frame = capture.read()
 
        if success:
            cv2.imwrite(f"C:/Strix/College/SiHStuff/test-app/frameOutput/frame_{frameNr}.jpg", frame)
            print(f"frame {frameNr} created")
 
        else:
            break
 
        frameNr = frameNr+1
 


    if ( ty == "Violence"):
        rf = Roboflow(api_key="ecy5yfI3mpe6CZGt17OG")                   #change api key wrt new model
        project = rf.workspace().project("violence-detection-ufkio")       #change url to new web
        model = project.version(1).model
        print("violence model api called")
    
    elif ( ty == "Garbage"):
        rf = Roboflow(api_key="1RHUIPDhWPkl2ZLBBlQK")                   #change api key wrt new model
        project = rf.workspace().project("garbage-classification-3")       #change url to new web
        model = project.version(2).model
        print("garbage model api called")

    frameNr = 0

    # folder path
    dir_path = "./frameOutput"
    count = 0

    count = len([entry for entry in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, entry))])   
    print('File count:', count)
    i = 0

    frameSelect = frames    
    if (frameSelect <= 0):
       frameSelect = 1                                                                #allow it to be changed

    while ( i <= count - 1 ):
        path = (f'./frameOutput/frame_{frameNr}.jpg')
        print(path)
        model.predict(path, confidence=40, overlap=30).save(f'./boundOutput/frame_{frameNr}.jpg')
        frameNr = frameNr + frameSelect
        i = i + frameSelect


    path = "./boundOutput/"
    outputVideo = "output.mp4"

    pre_imgs = os.listdir(path)

    img = []
    for i in pre_imgs:
        i = path+i
        print(i)
        img.append(i)

    cv2_fourcc = cv2.VideoWriter_fourcc(*'mp4v')                                                                         

    frame = cv2.imread(img[0])
    size = list(frame.shape)
    del size[2]
    size.reverse()
    print(size)

    

    fps = capture.get(cv2.CAP_PROP_FPS)
    print(f'fps:  {fps}')
    fps = fps / frameSelect
    print(f'fps:  {fps}')

    
    video = cv2.VideoWriter(outputVideo, cv2_fourcc, fps, size)          

    for i in range(len(img)):
        video.write(cv2.imread(img[i]))
        print('frame', i+1, ' of ', len(img))


    
    os.system('cmd /k ffmpeg -i C:/Strix/College/SiHStuff/test-app/output.mp4 -brand mp42 C:/Strix/College/SiHStuff/test-app/final.mp4')
    
    print("Supported Codec Ensured")


    webbrowser.open_new_tab("C:/Strix/College/SiHStuff/test-app/templates/download.html")

    video.release()
    pathToDelete = "./frameOutput/"
    delete_files_in_directory(pathToDelete)

    pathToDelete = "./boundOutput/"
    delete_files_in_directory(pathToDelete)
    capture.release()

    