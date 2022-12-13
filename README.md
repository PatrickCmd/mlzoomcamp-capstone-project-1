# MLZOOMCAMP CAPSTONE PROJECT 1

This is capstone project for the [MLZoomCamp](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp) course [here](https://github.com/PatrickCmd/mlzoomcamp/blob/main/course-zoomcamp/cohorts/2022/projects.md#capstone-1) sponsored by [DataTalks.Club](https://datatalks.club/)

## Problem
Classify kitchen items into 6 categories: cups, glasses, plates, spoons, forks and knives

## Dataset
The chosen dataset for this project is from the Kitchenware Classification Dataset from [Kaggle](https://www.kaggle.com/competitions/kitchenware-classification/overview/description)

## Project Setup
For data preparation and model training I used [Saturn Cloud](https://saturncloud.io/) platform. See the instructions below from the competition starter notebook describing how to setup saturn cloud, adding kaggle credentials to be able to download kaggle datasets. The notebook for data preparation and model training and evaluation can be found [here](https://nbviewer.org/github/PatrickCmd/mlzoomcamp-capstone-project-1/blob/main/notebooks/Kitchenware-Classification-Competition-clean.ipynb)

I deploy the model as web service both locally and to the cloud specifically AWS. I use Tensforflow-Lite to deploy the model to AWS Lambda, see the section below for more instructions.

Also I get to deploy the model on kubernetes with Tensorflow-Serving and AWS EKS. Below is section to give more detailed instructions.

### Kitchenware Competition Starter

A starter notebook for [the Kitchenware classification competition](https://www.kaggle.com/competitions/kitchenware-classification/) on Kaggle: [keras-starter.ipynb](keras-starter.ipynb)

In this notebook, we show how to:


- Download the data from Kaggle and unzip it
- Read the data
- Train an xception model (using the same code as in [ML Zoomcamp](http://mlzoomcamp.com))
- Making predictions
- Submitting the results 

You can run this notebook in SaturnCloud:

<p align="center">
    <a href="https://app.community.saturnenterprise.io/dash/resources?recipeUrl=https://raw.githubusercontent.com/DataTalksClub/kitchenware-competition-starter/main/kitchenware-jupyter-recipe.json" target="_blank" rel="noopener">
        <img src="https://saturncloud.io/images/embed/run-in-saturn-cloud.svg" alt="Run in Saturn Cloud"/>
    </a>
</p>


Using the recipe:

- Download the credential file from Kaggle
- Put the content of the file to [SaturnCloud secrets](https://app.community.saturnenterprise.io/dash/o/community/secrets), save this secret as "kaggle" 
- Click on the button above to create a resource in SaturnCloud
- Verify that the kaggle secret is linked in the "secrets" tab
- Run the code and submit your predictions
- Improve the score

You can also see it as a video:


<a href="https://www.loom.com/share/c41e5691bd36414fa4df8de9c905cc58">
    <img src="https://user-images.githubusercontent.com/875246/206399525-097683c4-62bd-436b-815a-4ac8543502a9.png" />
</a>




## Model serving with serverless (AWS LAMBDA) and Tensorflow-Lite
Serverless is the concept of removing infrastructure considerations for deploying code. Instead of having to manage servers and infrastructure by ourselves, a serverless service takes care of that for us and only charges according to use.

We will use AWS Lambda for this session. Even though it's serverless, we will have to use Docker to package our model and serve predictions.

To learn more about `Tensorflow-Lite` and `AWS-LAMBDA` see the references from [Alvaro Navas](https://github.com/ziritrion/ml-zoomcamp/blob/main/notes/09_serverless.md) and [Muhammad Awon](https://github.com/MuhammadAwon/ml-engineering/blob/main/09-serverless/README.md)

For this project follow the instructions in the [tflite_code directory](./tflite_code/README.md)

## Model serving with Kubernetes and Tensorflow-Serving
**Kubernetes** is a container orchestration system used to automatically deploy, scale and operate containers.

I use Kubernetes along with TensorFlow Serving, a component of the TensorFlow Extended (TFX) family of technologies used to deploy models in production environments.

See reference from [Alvaro Navas Notes](https://github.com/ziritrion/ml-zoomcamp/blob/main/notes/10_kubernetes.md) and [Muhammad Awon Notes](https://github.com/MuhammadAwon/ml-engineering/blob/main/10-kubernetes/README.md) for explanation about [Kubernetes](https://kubernetes.io/) together with [Tensorflow-Serving](https://www.tensorflow.org/tfx/guide/serving)

See [Tensorflow-Serving Section](./tensforflow-serving/README.md) for more instructions on how to serve the image-classifier model for this project with kubernetes and tensorflow-serving both locally and with [AWS EKS](https://aws.amazon.com/eks/)
