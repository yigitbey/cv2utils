import cv2
import pytest
from cv2utils import FaceCascade


def test_detect_faces():

    image = cv2.imread("face.jpg")
    face_detector = FaceCascade()
    result = face_detector.detect_faces(image)

    assert len(result) == 1
    assert type(result[0]) is dict
    assert 'box' in result[0]
    assert 'label' in result[0]
    assert type(result[0]['box']) is list
    assert all([True if type(i) is int else False for i in result[0]['box']]) is True
    assert type(result[0]['label']) is str
    assert len(result[0]['box']) == 4
    

def test_invalid_image():
    not_image = cv2.imread("requirements-test.txt")
    face_detector = FaceCascade()
    with pytest.raises(ValueError):
        face_detector.detect_faces(not_image)


def test_no_face():
    face_detector = FaceCascade()
    no_face = cv2.imread("no_face.jpg")
    result = face_detector.detect_faces(no_face)
    
    assert len(result) == 0
