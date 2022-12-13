import requests
import json

class Yandex():
    def __init__(self, token):
        self.token = token
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'


    def get_headers(self):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        return headers


    def create_folder(self, path):
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'
        requests.put(f'{self.url}?path={path}', headers=self.get_headers()).json()


    def get_url_upload(self,file_path):
        params = {'path': file_path, 'overwrite': 'True'}
        response = requests.get(f'{self.url}/upload', headers=self.get_headers(), params=params).json()
        return response



    def upload(self, file_path, filename):
        href = self.get_url_upload(file_path=file_path).get("href", "")
        load_file = requests.put(href, data=open(filename, 'rb'))



if __name__ == '__main__':
    ya = Yandex()
    ya.upload('Homework2/test.txt', 'test.txt')





