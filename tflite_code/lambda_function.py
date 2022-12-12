#!/usr/bin/env python
# coding: utf-8

import numpy as np
import tflite_runtime.interpreter as tflite
from keras_image_helper import create_preprocessor

preprocessor = create_preprocessor("xception", target_size=(299, 299))


interpreter = tflite.Interpreter(model_path="image-classifier-model.tflite")
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]["index"]
output_index = interpreter.get_output_details()[0]["index"]

classes = np.array(["cup", "fork", "glass", "knife", "plate", "spoon"])


def predict(url):
    X = preprocessor.from_url(url)

    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)

    category = classes[preds.argmax(axis=1)]

    return {"category": category[0]}


def lambda_handler(event, context):
    url = event["url"]
    result = predict(url)
    return result


if __name__ == "__main__":
    url = "https://thumbs.dreamstime.com/b/glass-clean-drinking-water-44066082.jpg"
    print(predict(url))
