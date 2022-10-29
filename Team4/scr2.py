#!/usr/bin/env python3
import pathlib
from pathlib import Path
import json
import requests
from pprint import pprint
from collections import defaultdict
import re

CRY_REGEX = r"https://anthologiagraeca.org/api/passages/urn:cts:greekLit:tlg7000.tlg001.ag:(.*)/\?format=json"


def save_encoded_json(result, path):
    p = pathlib.Path(__file__).parent / path
    str_result = json.dumps(result, indent=4, ensure_ascii=False).encode("utf-8")
    with p.open("w+") as stream:
        stream.write(str_result.decode())


HERE = Path(__file__).parent
KEYWORDS = json.load((HERE / "keywords.json").open("r"))

def match_epi_name(url):
    m = re.match(CRY_REGEX, url)
    return m.groups(0)[0]


matrix_kw = []

for kw in KEYWORDS:
    local_categories = kw.get("category", {}).get("names", [])
    category = "undefined"
    for local in local_categories:
        if local.get("language") == "fra":
            category = local.get("name", "WTF")
        
    local_names = kw.get("names", [])
    name = "undefined"
    for local in local_names:
        if local.get("language") == "fra":
            name=local.get('name', "WTF")    
    for url in kw.get("passages", []):
        epi_name = match_epi_name(url)
        print(epi_name)
        matrix_kw.append({
            "cat": category,
            "ordre": epi_name,
            "url": url,
            "name": name,
            "book": epi_name.split('.')[0]
        }   )

def save_encoded_json(result, path):
    p = pathlib.Path(__file__).parent / path
    str_result = json.dumps(result, indent=4, ensure_ascii=False).encode("utf-8")
    with p.open("w+") as stream:
        stream.write(str_result.decode())

save_encoded_json(matrix_kw, "data2.json")

