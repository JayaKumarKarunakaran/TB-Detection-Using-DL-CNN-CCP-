# Title: Tuberculosis (TB) Detection from Chest X-ray using Deep Transfer Learning (PyTorch)

## Domain: Core course project 

## Introduction:
![image](https://github.com/user-attachments/assets/cfb21288-ca12-4fde-82f9-47a7f5788ebb)


### Background

Tuberculosis (TB) is a communicable disease which is a major public health problem in Nepal. It is one of
the top 10 causes of death worldwide and in Nepal, and the leading cause of death from a single infectious
agent (ranking above HIV/AIDS).

In Nepal, an estimated 69,000 fell ill with TB during FY 2077/78. National Tuberculosis Programme (NTP)
registered 28,677 (nearly 58% missing vs. the projection) all forms of TB cases (38% female and 62% male).
Out of 28,677 all forms of TB cases, 28,182 incident TB cases.

> Source : Department of Health Services
> 2077/78 (2020/21) | Annual Report

### Goal and Objective

The goal of this project is to develop an AI-based solution for detecting tuberculosis from chest X-ray images using transfer learning approach. The solution aims to improve the accuracy and efficiency of TB diagnosis. We aim to use the pre-trained model to detect the signs of TB in chest X-ray images and fine-tune the model to improve the performance. Our solution aims to assist healthcare providers and help in addressing the TB epidemic, particularly in under-served areas where access to healthcare is limited.
Advances in Artificial Intelligence (AI) and deep learning have opened new avenues for automating the diagnostic process. One of the most promising techniques for medical image analysis is Convolutional Neural Networks (CNNs). CNNs, a type of deep learning model, can learn intricate patterns from images, making them highly suitable for tasks such as TB detection from chest X-rays. 
![image](https://github.com/user-attachments/assets/9806d6d8-060b-4fad-b193-5fcbda9cc5bb)

Incorporating transfer learning techniques using pre-trained models like ResNet and DenseNet enhanced the model’s performance and training efficiency. Data augmentation techniques further improved the model’s ability to generalize and reduced the risk of overfitting.
By using a CNN model implemented in PyTorch, the study aims to automate the detection of TB and improve diagnostic accuracy.

# Deep Transfer Learning:![image](https://github.com/user-attachments/assets/82bcd32b-ce3b-455c-862f-8ad0dae77987)


### Dataset:

We have used Tuberculosis (TB) Chest X-ray Database to train and evaluate our model.acquired the Tuberculosis (TB) Chest X-ray Database from a reputable source i.e. Kaggle. We then organized the dataset in a directory structure.

#### [Tuberculosis (TB) Chest X-ray Database](https://www.kaggle.com/datasets/tawsifurrahman/tuberculosis-tb-chest-xray-dataset)

A team of researchers from Qatar University, Doha, Qatar, and the University of Dhaka, Bangladesh along with their collaborators from Malaysia in collaboration with medical doctors from Hamad Medical Corporation and Bangladesh have created a database of chest X-ray images for Tuberculosis (TB) positive cases along with Normal images.
The research employs a Convolutional Neural Network (CNN) architecture for TB detection from chest X-rays using the PyTorch framework. The design follows a sequential model with multiple convolutional layers, pooling layers, fully connected layers, and softmax activation in the output layer. Transfer learning was also explored by leveraging pre-trained models like ResNet and DenseNet to enhance model accuracy and efficiency.
![image](https://github.com/user-attachments/assets/be590840-7ab0-4993-88dd-284b94a1836e)
 In our current release, there are 700 TB images publicly accessible and 2800 TB images can be downloaded from NIAID TB portal[3] by signing an agreement, and 3500 normal images.

