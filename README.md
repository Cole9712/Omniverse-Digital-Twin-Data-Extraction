# Scene Construction and Data Extraction via Nvidia Omniverse

> A project that collaboate with OneCup AI to build digital barn scenes and extract synthetic data for neural network training. It also includes 2 trained model based on YoloV5 using generated synthetic data.

**Omniverse**:
all the scenes we created using Omniverse, excluding the animal assets.

**Data Generation**:
`replicator.py` can be run by Omniverse Code to generate synthetic data, other files used to organize the data.

**Data Conversion**:
`dataConvertor.ipynb` to convert raw data to Yolov5 format. `getCOCOdata.py` to extract data contains cows from COCO2017 dataset.

**Run Result**:
Contains our 2 models information, including weights and metrics. Didn't include the dataset we used since it is too large.

`requirements.txt` can be used to install all the dependencies for python scripts in our project including Yolov5. In order to run Yolov5, should download Pytorch with GPU seperately.