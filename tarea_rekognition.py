import boto3
import logging
from rekognition_objects import (RekognitionText, )
from botocore.exceptions import ClientError
logger = logging.getLogger(__name__)
handler = logging.FileHandler('log.txt','a')

handler.setFormatter(logging.Formatter("[%(asctime)s]:%(message)s"))
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
    filename=input("Name of the image (control): ")
    t = input("Name of the image (test): ")
    # Control
    control_image = from_file("images/"+filename, rekognition_client)
    print(f"Detecting text in {filename}...")
    texts = detect_text(control_image, filename, rekognition_client)

    # Test
    test_image = from_file("images/"+t, rekognition_client)
    print(f"Detecting text in {t}...")
    a  = detect_text(test_image, t, rekognition_client)

    tmp = set()
    tmp2 = set()
    for i in texts:
        if i.kind == "WORD":
            tmp.add(i.text.lower())
    for i in a:
        if i.kind == "WORD":
            tmp2.add(i.text.lower())

    if tmp == tmp2:
        print("Result: true")
        logger.debug("(Output):true")
    else:
        print("Result: false")
        logger.debug("(Output):false")

    s = 0
    for i in texts:
        logger.debug("(Rekognition %s):text:%s, confidence:%s, kind:%s",filename, i.text, i.confidence, i.kind)
        if i.kind == "WORD":
            s += len(i.text)
    logger.debug("Total characters: %d", s)
    s = 0
    for i in a:
        logger.debug("(Rekognition %s):text:%s, confidence:%s, kind:%s",t, i.text, i.confidence, i.kind)
        if i.kind == "WORD":
            s += len(i.text)
    logger.debug("Total characters: %d", s)
    print("Done.")
    input("Press enter to continue.")
    print('-'*88)


if __name__ == '__main__':
    usage_demo()