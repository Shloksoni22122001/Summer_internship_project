# Image Processing using OpenCV

## Description ✍️
- **Detecting the Red and Blue Objects within the Given Frame and Making a Line Between Them**
- This repository contains Python code that utilizes OpenCV for detecting and tracking red and blue objects within an image or video.
- The code identifies the largest contours of the red and blue objects, draws rectangles around them, and connects them with a line.

### Ideation 
- The Idea to make this project was from the Company 'Kshatra Infotech Pvt. Ltd.'
## Authors 👑

- [@Shloksoni😎](https://www.github.com/Shloksoni22122001)




## Demo
![](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbnc0NzJjM3RpYjloM2M2b3dkdWIxY2pyYTN6ZWZlcTR3dXZzcGE3MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xGoD5xVymqYIx2tUTL/giphy-downsized-large.gif)
## Installation ⬇️
### Dependencies
1. python == 3.10.9
2. opencv-python == 4.6.0
3. numpy == 1.25.0


⚠️ Note: These were the dependencies on which this project was done. It may or may not work as efficiently/correctly on other versions

### Installing dependencies
Creating the conda environment:
```
conda create -n <Environment_name> python=3.10.9
```
Activating the conda environment:
```
conda activate <Environment_name>
```
Installing opencv
```
conda install -c conda-forge opencv==4.6.0
```
Installing numpy
```
conda install -c conda-forge numpy==1.25.0
```

**or you can also refer environment.yml** 🤝

(!to run the environment.yml directly here is the command)

```
conda env update --name <Environment_name> --file <Path/To>environment.yml --prune
```
## Usage/Examples 👨‍💻

- It is used to detect red and blue objects from the image/video or live camera its parts or chunks of codes can be used in various places as per requirement 😊

- Every line or chunks are explained in code along with comments 🫡

1. Run the main script:

    ⚠️**After activating the environment only**

    ```
    python <path/to>solution.py
    ```

2. The script will open the webcam and start processing the video stream in real-time. It will detect and track red and blue objects, drawing rectangles around them and connecting them with a line.

3. Press 'q' to exit the application.
## Acknowledgements ®️

- [OpenCV](https://opencv.org/) - Open Source Computer Vision Library
- [NumPy](https://numpy.org/) - Numerical Computing Library

## Customization ⚙️

- If you want to use a different video file instead of the webcam, uncomment the line `# image = cv2.imread('path/to/your/image.jpg')` in the code and provide the path to your image file.

- You can adjust the color ranges and other parameters in the `PreProcessing()` function to fine-tune the object detection based on your specific requirements.

## License 🪪

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/)
## **Conclusion**✔️

In this project, we have explored image processing techniques using OpenCV to detect and track red and blue objects. The code utilizes color masking and contour analysis to identify the largest contours of the objects, draws rectangles around them, and connects them with a line. This can be useful in various applications such as object tracking, computer vision, and robotics. Feel free to explore the code and adapt it to suit your specific needs.
