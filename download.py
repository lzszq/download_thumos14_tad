import json
import os

def get_key():
    data = dict()
    with open('./thumos14.json', mode='r', encoding='utf-8') as f:
        data = json.loads(f.read())
        f.close()
    validation_keys = [key for key in data if key.find('validation') != -1]
    test_keys = [key for key in data if key.find('test') != -1]
    return validation_keys, test_keys

def download(keys, key_type):
    os.chdir(os.path.join(os.getcwd(), key_type))
    if key_type == 'validation':
        for i in keys:
            os.system(f"wget --no-check-certificate https://www.crcv.ucf.edu/THUMOS14/Validation_set/videos/{i}.mp4")
    elif key_type == 'test':
        for i in keys:
            os.system(f"wget --no-check-certificate https://www.crcv.ucf.edu/THUMOS14/test_set/TH14_test_set_mp4/{i}.mp4")


if __name__ == '__main__':
    validation_keys, test_keys = get_key()
    download(validation_keys, 'validation')
    download(test_keys, 'test')