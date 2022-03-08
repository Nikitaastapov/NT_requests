import requests
import os
token = ''

file_name = 'file_for_upload.txt'
direct = os.getcwd()
path_to_file = os.path.join(direct, file_name)


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        
    def upload_link(self):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        params = {'path': '/upload.txt', 'overwrite': 'true'}
        response = requests.get(upload_url, headers = headers, params=params)
        return response.json()
        
    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        url_file = self.upload_link().get('href','')
        print(url_file)
        response = requests.put(url_file, data = open(file_path, 'rb'))
        response.raise_for_status()
        
      
        


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    uploader = YaUploader(token)
    # link = uploader.upload_link()
    # print(link)
    result = uploader.upload(path_to_file)