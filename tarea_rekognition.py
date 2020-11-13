import requests
import boto3
import logging
from rekognition_objects import (RekognitionText, )
from botocore.exceptions import ClientError
logger = logging.getLogger(__name__)
handler = logging.FileHandler('log.txt','a')

handler.setFormatter(logging.Formatter(logging.BASIC_FORMAT))
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

confidence_value = 97.0

def detect_text(image, image_name, rekognition_client):
    try:
        response = rekognition_client.detect_text(Image=image)
        texts = [RekognitionText(text) for text in response['TextDetections']]
        logger.info("Found %s texts in %s.", len(texts), image_name)
    except ClientError:
        logger.exception("Couldn't detect text in %s.", image_name)
        raise
    else:
        return texts

def from_file(image_file_name, rekognition_client):
    with open(image_file_name, 'rb') as img_file:
        image = {'Bytes': img_file.read()}
    return image


def usage_demo():
    print('-'*88)
    print("Tarea Rekognition Adbias Palacios")
    print('-'*88)
    rekognition_client = boto3.client('rekognition')
    ###
    filename=input("Name of the image: ")
    t = input("Text of the image: ")
    book_image = from_file(filename, rekognition_client)
    print(f"Detecting text in {filename}...")
    texts = detect_text(book_image, filename, rekognition_client)
    a = t.strip().split()
    tmp = set()
    for i in texts:
        if i.kind == "WORD" and float(i.confidence) > confidence_value:
            tmp.add(i)
    if tmp == set(a):
        print("true")
    else:
        print("false")
    # print("Detected text:")
    # print("*"*88)
    logger.debug("Text given by the user: '%s'", t)

    s = 0
    for i in texts:
        logger.debug("Rekognition:text:%s, confidence:%s, kind:%s", i.text, i.confidence, i.kind)
        if i.kind == "WORD":
            s += len(i.text)
    logger.debug("Total characters: %d", s)
    # print("*"*88)
    print("Done.")
    input("Press enter to continue.")
    print('-'*88)


if __name__ == '__main__':
    usage_demo()