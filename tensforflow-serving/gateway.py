#!/usr/bin/env python
# coding: utf-8

import os

import grpc
import numpy as np
import tensorflow as tf
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from keras_image_helper import create_preprocessor
from pydantic import BaseModel, Field
from tensorflow_serving.apis import predict_pb2, prediction_service_pb2_grpc

from proto import np_to_protobuf

host = os.getenv("TF_SERVING_HOST", "localhost:8500")

channel = grpc.insecure_channel(host)
stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)

preprocessor = create_preprocessor("xception", target_size=(299, 299))

classes = np.array(["cup", "fork", "glass", "knife", "plate", "spoon"])


class Data(BaseModel):
    url: str = Field(...)

    class Config:
        allowed_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "url": "https://thumbs.dreamstime.com/b/glass-clean-drinking-water-44066082.jpg",
            }
        }


class ResponseModel(BaseModel):
    category: str


def prepare_request(X):
    pb_request = predict_pb2.PredictRequest()

    pb_request.model_spec.name = "image-classifier-model"
    pb_request.model_spec.signature_name = "serving_default"

    pb_request.inputs["input_2"].CopyFrom(np_to_protobuf(X))
    return pb_request


def prepare_response(pb_response):
    preds = pb_response.outputs["dense_1"].float_val
    preds = np.array([preds])
    category = classes[preds.argmax(axis=1)]

    return {"category": category[0]}


def predict(url):
    X = preprocessor.from_url(url)
    pb_request = prepare_request(X)
    pb_response = stub.Predict(pb_request, timeout=20.0)
    response = prepare_response(pb_response)
    return response


app = FastAPI()


@app.post(
    "/predict",
    response_description="Predict classification of the image",
    response_model=ResponseModel,
)
async def predict_endpoint(data_info: Data):
    data = jsonable_encoder(data_info)
    url = data["url"]
    result = predict(url)
    return result


if __name__ == "__main__":
    url = "https://img.freepik.com/free-psd/close-up-ceramic-plate-mockup_53876-98747.jpg?w=2000"
    response = predict(url)
    print(response)
