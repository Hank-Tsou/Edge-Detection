# Canny Edge Detection
```
This project is trying to implement Canny Edge Detection
```
### Canny Edge Detection
```
Input image: input_image.jpg
Command line >> python Canny_Edge_Detection.py  -i input_image.png
```

The program will show the result include original image and result image. 
```
NOTE: The running time for this program is about 10 sec on macbook-pro
```
	    
![image](https://user-images.githubusercontent.com/28382639/35772842-1c2cafc0-08fa-11e8-9d69-b59e27a92081.png)

```
Useful link as below for implementation:
```
- [Image Filtering](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/tree/master/tutorials/Image_Processing/4_Image_Filtering)
- [Image Padding](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/tree/master/tutorials/Core_Operation)
- [Image Thresholding](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/tree/master/tutorials/Image_Processing/2_Image_Thresholding)
- [Image Gradient](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/tree/master/tutorials/Image_Processing/5_Image_Gradient)

## Code
- [Canny Edge Detection Implementation](https://github.com/Hank-Tsou/Implement-Edge-Detection/blob/master/Canny_Edge_Detection.py)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Author: Hank Tsou
* Contact: hank630280888@gmail.com
* Project from California State Polytechnic University, Pomona, Computer Science, CS-519 Computer Vision











# Edge Detection
#### Implement Edge detection and compare with OpenCV function.
#### 3. Edge Detection [input image name: 'input_image.png'] 

>> This file include: </br>
>>* Readme_1-3</br>
>>* input image.png</br>
>>* (Question 3-a) 1_canny_edge_detector.py</br>
>>* (Question 3-b) 2_compare.py</br>

>> #### (A) How to run the code [1_canny_edge_detector.py]
>>> (a) Using the command prompt and direct to the file position. (my example)
>>> <pre> >> [C:\Users\hank\Desktop\Computer Vision\Assignment_1\1-3]

>>> (b) input >> "python 1_canny_edge_detector.py" to run the code.
>>> <pre> >> [C:\Users\hank\Desktop\Computer Vision\Assignment_1\1-3>python 1_canny_edge_detector.py]

>>> (c) The program will ask to input the image name and threshold value. The program can also 
>>> calculate the threshold value itself if the user input 2 (Auto). Remember have to put '' 
>>> (single quote) when input the image name => 'image name'
>>> <pre> >> [image name(with .jpg .png): 'input_image.png']</br> >> [image threshold values(1.Input 2.Auto(the program will calculate itself)): 1]</br> >> [min_VAL: 54]</br> >> [max_VAL: 108]

>>> (d) The program will show the gray image and edge image. (output_Image_a)

>>> ![image](https://user-images.githubusercontent.com/28382639/35772842-1c2cafc0-08fa-11e8-9d69-b59e27a92081.png)

>> #### (B) Compare with openCV function [2_compare.py]
>>> (a) Using the command prompt and direct to the file position. (my example)
>>> <pre> >> [C:\Users\hank\Desktop\Computer Vision\Assignment_1\1-3]

>>> (b) input >> python 2_compare.py to run the code.
>>> <pre> >> [C:\Users\hank\Desktop\Computer Vision\Assignment_1\1-3>python 2_compare.py]

>>> (c) The program will show the word
>>> "use image 'Lenna.png' and auto threshold to compare with opencv function"

>>> (d) The program will show original image, my result image and openCV result image.(output_Image_b)

>>> ![image](https://user-images.githubusercontent.com/28382639/35772844-34e56638-08fa-11e8-8271-0b49bff2b1bd.png)

