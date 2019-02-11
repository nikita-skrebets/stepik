import requests

with open('dataset_3378_3.txt', 'r') as inf:
    url = inf.readline().strip()
    index = url.rfind('/')
    urlBase = url[:(index + 1)]
    fileName = url[index + 1:]

triesLeft = 1000
while triesLeft > 0:
    rq = requests.get(urlBase + fileName)
    content = rq.text.strip()
    if content[:2] == 'We':
        print(content)
        break
    fileName = content
    triesLeft -= 1
    print(triesLeft)
