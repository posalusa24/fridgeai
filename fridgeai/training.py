import requests
import time
import os
from zipfile import ZipFile
from bs4 import BeautifulSoup

MODEL_FOLDER = 'data'


def _create_zipfile(folder_path, zipfile_path):
    with ZipFile(zipfile_path, 'w') as zip:
        for file in [
            os.path.join(folder_path, file)
            for file in os.listdir(folder_path)
        ]:
            zip.write(file, os.path.basename(file))


def _post_file(file_path, address):
    return requests.post(address, files={
        'file_1': open(file_path, 'rb')
    })


def _listFD(url, ext=''):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    return [
        url + '/' + node.get('href')
        for node in soup.find_all('a')
        if node.get('href').endswith(ext)
    ]


def send_training_data(images_folder_path):
    zipfile_path = os.path.basename(images_folder_path) + '.zip'

    _create_zipfile(images_folder_path, zipfile_path)
    _post_file(zipfile_path, 'http://127.0.0.1:8000/upload')
    os.remove(zipfile_path)


def model_sync():
    while True:
        tflites = [
            file for file in _listFD('http://fridgeai.my.to:8000')
            if os.path.splitext(file)[1] == '.tflite'
        ]
        local_tflites = [
            file for file in os.listdir(MODEL_FOLDER)
            if os.path.splitext(file)[1] == '.tflite'
        ]
        if (
            tflites and (
                not local_tflites or
                os.path.basename(tflites[0])
                != os.path.basename(local_tflites[0])
            )
        ):
            for file in local_tflites:
                os.remove(os.path.join(MODEL_FOLDER, file))
            model_path = os.path.join(
                MODEL_FOLDER, os.path.basename(tflites[0])
            )
            print('New tflite file found. Updating...')
            with open(model_path, 'wb') as model:
                res = requests.get(tflites[0])
                model.write(res.content)
            with open(os.path.join(MODEL_FOLDER, 'labels.json'), 'wb') as file:
                res = requests.get('http://fridgeai.my.to:8000/labels.json')
                file.write(res.content)
        time.sleep(5)
