
# Semantic Segmentation

I have created a Semantic Segmentation model to segment potholes from an input video.



## About the model

- I have trained a **U-Net model** from scratch using Tensorflow and Keras.
- I have used a **custom Data Generator** to feed the images and the masks as input to the U-Net model.
- The depth of the U-Net model can be customised. (recommended depth - **3 to 5** for **(256,256,3)** images).
- The maximum allowed depth of the U-Net model is determined by the dimensions of the input frames.


## Structure of the U-Net Model

![App Screenshot](U-Net\U_Net.png)


## Run Locally

Following were the versions of the libraries I used

- Tensorflow - 2.10.1
- OpenCV (cv2) - 4.6.0
- Numpy - 1.23.5
- Moviepy - 1.0.3

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd SemanticSegmentation
```
**Important!**
Set the paths to the input and output video files

Run segfile.py

```bash
  python segfile.py
```




## Sample Video

**Input Video**


**Output Video**
## Acknowledgements

 - [Pothole Image segmentation dataset](https://www.kaggle.com/datasets/farzadnekouei/pothole-image-segmentation-dataset)
 - [U-Net architecture](https://pyimagesearch.com/2022/02/21/u-net-image-segmentation-in-keras/)

