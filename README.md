
# Semantic Segmentation

I have created a Semantic Segmentation model to segment potholes from an input video.



## About the model

- I have trained a **U-Net model** from scratch using Tensorflow and Keras.
- I have used a **custom Data Generator** to feed the images and the masks as input to the U-Net model.
- The depth of the U-Net model can be customised. (recommended depth - **3 to 5** for **(256,256,3)** images).
- The maximum allowed depth of the U-Net model is determined by the dimensions of the input frames.


## Structure of the U-Net Model
![U_Net](https://github.com/lilNewbie/SemanticSegmentation/assets/90834922/2d0c8b3d-7713-4245-9a63-820d48c8c9cc)

## Run Locally

Following were the versions of the libraries I used

- Tensorflow - 2.10.1
- OpenCV (cv2) - 4.6.0
- Numpy - 1.23.5
- Moviepy - 1.0.3

Clone the project

```bash
  git clone https://github.com/lilNewbie/SemanticSegmentation.git
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




## Running the Train file (SemanticSegmentation_Pothole.ipynb)

- The U-Net model was trained in Google Colab.
- You will need to use your [Kaggle public API](https://www.kaggle.com/docs/api) to access the dataset via Colab



## Sample Video

**Input Video**
<video width="630" height="250" src="https://github.com/lilNewbie/SemanticSegmentation/assets/90834922/f966d4e2-5a32-4bb1-b489-57d4c038f8cb.mp4"></video>

**Output Video**
<video width="630" height="250" src="https://github.com/lilNewbie/SemanticSegmentation/assets/90834922/fd07b97f-f9d5-4116-82be-c4098d01a721.mp4"></video>

The difference in input and output clarity is due to resizing the input frames for prediction and later resizing it back to its actual dimensions



## References

 - [Pothole Image segmentation dataset](https://www.kaggle.com/datasets/farzadnekouei/pothole-image-segmentation-dataset)
 - [U-Net architecture](https://pyimagesearch.com/2022/02/21/u-net-image-segmentation-in-keras/)

