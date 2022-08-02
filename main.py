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

