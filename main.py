# tusk 1
import hashlib
s = "Python Bootcamp"
hash_object = hashlib.md5(s.encode( ))
print(f"hashing string :{hash_object.hexdigest()}")
# tusk 2
import os.path
import shutil

try:
    import requests
except ImportError:
    from pip._internal import main as pip
    pip(['install', 'requests'])
    import requests
try:
    os.mkdir('./home')
    os.mkdir('./home/user')
except:
    print('dir already created')
path = './home/user'

num_files = len([f for f in os.listdir(path)
                if os.path.isfile(os.path.join(path, f))])

file_name = f'TikTok-example-{num_files + 1}.gif'
url_vidos = 'https://v16m-webapp.tiktokcdn-us.com/ed129ecb01ab00e202682e99f68a9288/62e7cb0d/video/tos/useast5/tos-useast5-pve-0068-tx/d69985b1677b4a73a584b56d604011ca/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=4020&bt=2010&cs=0&ds=3&ft=ebtHKH-qMyq8ZjFl1we2N9befl7Gb&mime_type=video_mp4&qs=0&rc=OTU4MzU0NzVnaDpnOGg8OEBpajM5Z2c6ZmYzZTMzZzczNEAuMC9jLWBgNmExMzJfY18tYSMxX28vcjRnMGRgLS1kMS9zcw%3D%3D&l=20220801064449EF653E99EF32BC2EAB55'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
           'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/75.0.3770.80 Safari/537.36'}


def download_video(url=''):
    try:
        r = requests.get(url,headers=headers,stream = True)

        with open(file_name,'wb') as file:
            file.write(r.content)

        shutil.move(file_name, path)
        return 'Sucessful'
    except Exception as _ex:
        return 'Not work. Check your URL adress'

download_video(url_vidos)

# import requests
# from bs4 import BeautifulSoup
#
# '''
# URL of the archive web-page which provides link to
# all video lectures. It would have been tiring to
# download each video manually.
# In this example, we first crawl the webpage to extract
# all the links and then download videos.
# '''
#
# # specify the URL of the archive here
# archive_url = "https://www.youtube.com/watch?v=ii0dHWklzFg"
#
#
# def get_video_links():
#     # create response object
#     r = requests.get(archive_url)
#
#     # create beautiful-soup object
#     soup = BeautifulSoup(r.content, 'html5lib')
#
#     # find all links on web-page
#     links = soup.findAll('a')
#
#     # filter the link sending with .mp4
#     video_links = [archive_url + link['href'] for link in links if link['href'].endswith('mp4')]
#     print(video_links)
#     return video_links
#
#
# def download_video_series(video_links):
#     for link in video_links:
#
#         '''iterate through all links in video_links
#         and download them one by one'''
#
#         # obtain filename by splitting url and getting
#         # last string
#         file_name = link.split('/')[-1]
#
#         print("Downloading file:%s" % file_name)
#
#         # create response object
#         r = requests.get(link, stream=True)
#
#         # download started
#         with open(file_name, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=1024 * 1024):
#                 if chunk:
#                     f.write(chunk)
#
#         print("%s downloaded!\n" % file_name)
#
#     print("All videos downloaded!")
#     return
#
#
# if __name__ == "__main__":
#     # getting all video links
#     video_links = get_video_links()
#
#     # download all videos
#     download_video_series(video_links)
# import requests
#
# url = ""
#
# querystring = {"url":"https://www.tiktok.com/@khaby.lame/video/7067201445686152454?is_from_webapp=1&sender_device=pc&web_id=7085812281682642434"}
# https://v16m-webapp.tiktokcdn-us.com/ed129ecb01ab00e202682e99f68a9288/62e7cb0d/video/tos/useast5/tos-useast5-pve-0068-tx/d69985b1677b4a73a584b56d604011ca/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=4020&bt=2010&cs=0&ds=3&ft=ebtHKH-qMyq8ZjFl1we2N9befl7Gb&mime_type=video_mp4&qs=0&rc=OTU4MzU0NzVnaDpnOGg8OEBpajM5Z2c6ZmYzZTMzZzczNEAuMC9jLWBgNmExMzJfY18tYSMxX28vcjRnMGRgLS1kMS9zcw%3D%3D&l=20220801064449EF653E99EF32BC2EAB55
# headers = {
# 	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
# 	"X-RapidAPI-Host": "tiktok-videos-without-watermark.p.rapidapi.com"
# }
#
# response = requests.request("GET",  params=querystring)
#
# print(response.text)
# import requests
#
# url = "https://tiktok-download-video-no-watermark.p.rapidapi.com/tiktok/info"
#
# querystring = {"url":"https://vt.tiktok.com/ZGJBQHoHA/"}
#
# headers = {
# 	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
# 	"X-RapidAPI-Host": "tiktok-download-video-no-watermark.p.rapidapi.com"
# }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# print(response.text)
#
# from flask import Flask, request, send_file
# import requests
# import json
# import re
#
# app = Flask(__name__)
#
#
# # Принимать только доступ к методу get
# @app.route("/douyin/", methods=["GET"])
# def check():
#     headers = {
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#         'accept-encoding': 'gzip, deflate, br',
#         'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
#         'cache-control': 'max-age=0',
#         'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36',
#     }
#     # Возвращаемое содержимое по умолчанию
#
#
# Return_dict = {'code': 1, 'result': False, 'msg': 'Запрос выполнен успешно'}
# # Определяем, пуст ли ввод
# if request.args is None:
#     return_dict['return_code'] = '504'
# Return_dict['return_info'] = 'Параметр запроса пуст'
# json.dumps(return_dict, ensure_ascii=False)
# # Получить входящие параметры
# get_data = request.args.to_dict()
# url = get_data.get('url')
#
# # Получить параметры интерфейса
# html = requests.get(url=url, headers=headers)
# title = re.findall('itemId: "(.*?)",', html.text)[0]
# dytk = re.findall('dytk: "(.*?)" }', html.text)[0]
#
# from flask import Flask, request, send_file
# import requests
# import json
# import re
#
# app = Flask(__name__)
# @app.route("/douyin/", methods=["GET"])
# def check():
#     headers = {
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#         'accept-encoding': 'gzip, deflate, br',
#         'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
#         'cache-control': 'max-age=0',
#         'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36',
#     }
#     # Возвращаемое содержимое по умолчанию
#     Return_dict = {'code': 1, 'result': False, 'msg': 'Запрос выполнен успешно'}
#     # Определяем, пуст ли ввод
#     if request.args is None:
#         return_dict['return_code'] = '504'
#     Return_dict['return_info'] = 'Параметр запроса пуст'
#     return json.dumps(return_dict, ensure_ascii=False)
#     # Получить входящие параметры
#
#
#     get_data = request.args.to_dict()
#     url = get_data.get('url')
#
#     # Получить параметры интерфейса
#     html = requests.get(url=url, headers=headers)
#     title = re.findall('itemId: "(.*?)",', html.text)[0]
#     dytk = re.findall('dytk: "(.*?)" }', html.text)[0]
#
#     # Интерфейс стыковки
#     url_item = 'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=' + title + '&dytk=' + dytk
#
#     # Получить ссылку на видео TikTok без водяных знаков
#     html_item = requests.get(url=url_item, headers=headers)
#     # Строка в словарь
#     content = json.loads(html_item.text)
#
#     # Получение информации, связанной с видео
#     # data = {}
#     # Описание видео
#     # data['videoDesc'] = content['item_list'][0]['desc']
#     # Обложка видео, маленькое изображение
#     # data['dynamiCoverUrl'] = content['item_list'][0]['video']['dynamic_cover']['url_list'][0]
#     # Обложка видео, большое изображение
#     # data['staticCoverUrl'] = content['item_list'][0]['video']['origin_cover']['url_list'][0]
#     # Количество комментариев к видео
#     # data['comments'] = content['item_list'][0]['statistics']['comment_count']
#     # Количество лайков на видео
#     # data['prise'] = content['item_list'][0]['statistics']['digg_count']
#
#     # Видео интерфейс
#     url_video = content['item_list'][0]['video']['play_addr']['url_list'][1]
#     response = requests.get(url_video, headers=headers, allow_redirects=True)
#
#     # Получите перенаправленную ссылку, это тоже ссылка для скачивания видео без водяного знака, но на этот раз она бесполезна
#     redirect = response.url
#     # print(redirect)
#     # Ссылка для скачивания видео
#     # data['videoPlayAddr'] = redirect
#     # Вернуть информацию о видео
#     # return_dict['result'] = data
#     # Вернуть результат
#     # return json.dumps(return_dict, ensure_ascii=False)
#
#     video = requests.get(url=redirect, headers=headers).content
#     video_name = "douyin.mp4"
#     with open(video_name, 'wb') as f:
#         f.write(video)
#         f.flush()
#     return send_file('douyin.mp4')
#
# # Принимать только доступ к методу get
#
# if __name__ == "__main__":
#  # Локальная отладка
#     app.run(debug=True)
#  # Разверните и подключитесь
#

#
# url = 'https://www.tiktok.com/@hero.video1/video/7116207760416574726'
#
# import requests
#
#
# def save_file_from_www(link):
#     filename = link.split('/')[-1] +'.mp4'
#     r = requests.get(link, allow_redirects=True)
#     open(filename, 'wb').write(r.content)
#
#
# link1 = 'https://v16m-webapp.tiktokcdn-us.com/ed129ecb01ab00e202682e99f68a9288/62e7cb0d/video/tos/useast5/tos-useast5-pve-0068-tx/d69985b1677b4a73a584b56d604011ca/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=4020&bt=2010&cs=0&ds=3&ft=ebtHKH-qMyq8ZjFl1we2N9befl7Gb&mime_type=video_mp4&qs=0&rc=OTU4MzU0NzVnaDpnOGg8OEBpajM5Z2c6ZmYzZTMzZzczNEAuMC9jLWBgNmExMzJfY18tYSMxX28vcjRnMGRgLS1kMS9zcw%3D%3D&l=20220801064449EF653E99EF32BC2EAB55'
# link2 = 'https://raw.githubusercontent.com/WISEPLAT/python-code/master/python-xml/yandex_xml_commercial.xml'
# link3 = 'https://youtu.be/cvo68BcuIm8'
#
# save_file_from_www(link3)
#
# save_file_from_www(link1)
# save_file_from_www(link2)
# save_file_from_www(link3)
# import requests
# print('Start')
# url = 'https://planbphoto.com/wp-content/uploads/Serze.jpg'
# r = requests.get(url)
# filename = url.split('/')[-1]
#
# with open(filename,'wb') as out_file:
#     out_file.write(r.content)
# print("Downolad completed")

# import requests
#
#
# def save_file_from_www(link):
#     filename = link.split('/')[-1]
#     r = requests.get(link, allow_redirects=True)
#     open(filename, 'wb').write(r.content)
#
#
# link1 = 'https://v16m-webapp.tiktokcdn-us.com/ed129ecb01ab00e202682e99f68a9288/62e7cb0d/video/tos/useast5/tos-useast5-pve-0068-tx/d69985b1677b4a73a584b56d604011ca/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=4020&bt=2010&cs=0&ds=3&ft=ebtHKH-qMyq8ZjFl1we2N9befl7Gb&mime_type=video_mp4&qs=0&rc=OTU4MzU0NzVnaDpnOGg8OEBpajM5Z2c6ZmYzZTMzZzczNEAuMC9jLWBgNmExMzJfY18tYSMxX28vcjRnMGRgLS1kMS9zcw%3D%3D&l=20220801064449EF653E99EF32BC2EAB55'
# link2 = 'https://raw.githubusercontent.com/WISEPLAT/python-code/master/python-xml/yandex_xml_commercial.xml'
# link3 = 'https://www.culture.ru/storage/images/5cb82d851c1b7c86f5572a72874daa92/59108e2912262e451d2121b407846c44.jpg'
#
# save_file_from_www(link1)
# save_file_from_www(link2)
# save_file_from_www(link3)

# import requests
# print('Start')
# url = 'https://www.instagram.com/tv/CguGR9ijE5v/?utm_source=ig_web_copy_link'
# r = requests.get(url)
# filename = url.split('/')[-1] + '.mp4'
#
# with open(filename,'wb') as out_file:
#     out_file.write(r.content)
# print("Downolad completed")

# import urllib.request
# destination = 'name '
# url = 'https://www.instagram.com/tv/CguGR9ijE5v/?utm_source=ig_web_copy_link'
# urllib.request.urlretrieve(url, destination)
#
# import requests #импортируем модуль
# import wget
# url_vidos = input("Enter the Youtube-url\n") # получаем ссылку на видео
# def download_wget(url='',file_type ='video'):
#     wget.download(url=url,out =f'wget_video.mp4')
# def downolad_img(url=''):
#     try:
#         response = requests.get(url=url)
#         with open('req_img.jpg','wb') as file:
#             file.write(response.content)
#         return 'Img sucessfully'
#     except Exception as _ex:
#         return 'Upps.. Check the URl please'
# def downolad_video(url=''):
#     try:
#         response = requests.get(url=url)
#         with open('req_video.mp4','wb') as file:
#             file.write(response.content)
#         return 'Img sucessfully'
#     except Exception as _ex:
#         return 'Upps.. Check the URl please'
#
#
# download_wget(url_vidos)