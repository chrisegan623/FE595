import requests as requests
import time as time

url  = "http://theyfightcrime.org"
male= list()
female = list()

def my_func(url):
        request = requests.get(url)
        text = request.text
        text = text.split('<P>')
        text = (text[1])
        text = text.split('.')

        male.append(text[0])
        female.append(text[1])

if __name__ == '__main__':
    count = 0
    while count < 50:
        my_func(url)
        time.sleep(2)
        count += 1

    with open('male.txt', 'w') as m:
        for item in male:
            m.write("%s\n" % item)

    with open('female.txt', 'w') as f:
        for item in female:
            f.write("%s\n" % item)
