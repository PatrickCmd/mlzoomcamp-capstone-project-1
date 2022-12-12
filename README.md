# mlzoomcamp-capstone-project-1


# Kitchenware Competition Starter

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
