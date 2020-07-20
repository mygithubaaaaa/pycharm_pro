from aip import AipOcr

APP_ID = '20723216'
API_KEY = 'lCpubPuFZxG0GORxVQ0cih6m'
SECRET_KEY = 'NGybXZTagscKzOCgNcvGOE2TrQXxlYRe'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filepath):
    with open(filepath, 'rb') as fp:
        return fp.read()


image = get_file_content('test.jpg')
test = client.basicAccurate(image)
image_content = ""
for word in test['words_result']:
    image_content = image_content + word['words']
# with open('image_content.txt', 'w') as f:
#     f.write(image_content)
print(image_content)
