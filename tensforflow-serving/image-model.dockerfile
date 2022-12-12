FROM tensorflow/serving:2.7.0

COPY image-classifier-model /models/image-classifier-model/1
ENV MODEL_NAME="image-classifier-model"