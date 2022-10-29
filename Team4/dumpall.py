#!/usr/bin/env python3
import pathlib
import json
import requests

url = 'http://anthologiagraeca.org/api'
parameters = {
    'format':'json'
}

url_books = 'http://anthologiagraeca.org/api/books'
url_keywords = 'http://anthologiagraeca.org/api/keywords'
url_keywords_categories = 'http://anthologiagraeca.org/api/keyword_categories'
url_passages = 'http://anthologiagraeca.org/api/passages'
def loadresources(url):
    results = []
    pagination = True
    while pagination == True :
        tmp = requests.get(url, parameters).json()
        for result in tmp['results'] :
            results.append(result)
        if tmp['next'] is None:
            pagination = False
        else:
            url = tmp['next']
    return results


def save_encoded_json(result, path):
    p=pathlib.Path(__file__).parent / path
    str_result = json.dumps(result, indent=4, ensure_ascii=False).encode('utf-8')
    with p.open('w+') as stream :
        stream.write(str_result.decode())


# save_encoded_json(loadresources(url_books), "books.json")
# save_encoded_json(loadresources(url_books), "books.json")
save_encoded_json(loadresources(url_keywords), "keywords.json")
save_encoded_json(loadresources(url_keywords_categories), "keyword_categories.json")
# save_encoded_json(loadresources(url_passages), "passages.json")

