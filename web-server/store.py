import requests

def getCategories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories', verify=False)
    print(r.status_code)
    print(r.text)
    categories = r.json()
    for c in categories:
        print(c['name'])