from PIL import Image
from aip import AipOcr


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def baidu_discern(filename):
    """ 你的 APPID AK SK """
    APP_ID = '20723216'
    API_KEY = 'lCpubPuFZxG0GORxVQ0cih6m'
    SECRET_KEY = 'NGybXZTagscKzOCgNcvGOE2TrQXxlYRe'

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    image = get_file_content(filename)

    """ 调用网络图片文字识别, 图片参数为本地图片 """
    # ret = client.webImage(image)
    # ret = client.basicAccurate(image)
    # ret = client.basicGeneral(image)
    words = ret.get('words_result')
    if words:
        return ''.join(words[0]['words'].split(' '))


def get_img_content(filename, format=False):
    if format:
        # 转换图片格式
        new_filename = filename.split('.')[0] + '.png'
        Image.open(filename).save(new_filename)
        ret = baidu_discern(new_filename)
    else:
        ret = baidu_discern(filename)

    return ret

if __name__ == '__main__':
     # 非转换的
     ret = get_img_content('test.jpg', format=False)
     # 转换的
     # ret = get_img_content('../code.png', format=True)
     print(ret)