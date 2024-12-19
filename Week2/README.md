# Week 2 assignment

## Overview
This assignment focuses on understanding the representation of images as arrays and implementing fundamental image processing techniques using convolution operations. You will create functions for general convolutions and specific tasks such as blurring, sharpening, edge detection, erosion, and dilation.

## Goals
1. **Implement a Generalized Convolution Function**:
   - Takes the image matrix and kernel matrix as inputs.
   - Outputs the transformed image matrix.
   - Applications include blurring, sharpening, and edge detection.

2. **Implement Specific Functions**:
   - **Blur**: Applies a mean filter to smooth the image.
   - **Image Sharpening**: Enhances image details.
   - **Edge Detection**: Detects boundaries in the image.
   - **Erode**: Shrinks bright regions and removes noise.
   - **Dilate**: Expands bright regions to join separated elements.

## References
- **Image Representation and Pixels**:
  - [Pixels, Arrays, and Images](https://levelup.gitconnected.com/pixels-arrays-and-images-ef3f03638fe7)
  - [Images as Numpy Arrays](https://rcvaram.medium.com/images-are-just-numpy-arrays-ceb7b0307fcf)
- **Convolutions**:
  - [Introduction to Convolutions](https://youtu.be/mbXtzv1syCc?feature=shared)
  - [Convolution Applications](https://youtu.be/C_zFhWdM4ic?feature=shared)
- **Blur**:
  - [Mean Filter](https://www.educative.io/answers/how-to-blur-an-image-using-a-mean-filter)
- **Sharpening**:
  - [Sharpening Kernels](https://blog.demofox.org/2022/02/26/image-sharpening-convolution-kernels/)
- **Edge Detection**:
  - [Edge Detection Kernels](https://upscfever.com/upsc-fever/en/data/deeplearning4/2.html)


## Additional Notes
- **Kernel Matrix**: Choose appropriate kernel matrices for each task. Refer to the provided links for guidance.
- **Formats**: Be mindful of BGR (OpenCV) vs. RGB (Matplotlib) formats when working with images.


