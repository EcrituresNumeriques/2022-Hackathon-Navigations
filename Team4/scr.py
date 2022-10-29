#!/usr/bin/env python3
import pathlib
from pathlib import Path
import json
import requests
from pprint import pprint
from collections import defaultdict


def save_encoded_json(result, path):
    p = pathlib.Path(__file__).parent / path
    str_result = json.dumps(result, indent=4, ensure_ascii=False).encode("utf-8")
    with p.open("w+") as stream:
        stream.write(str_result.decode())


HERE = Path(__file__).parent
BOOKS = json.load((HERE / "books.json").open("r"))
PASSAGES = json.load((HERE / "passages.json").open("r"))


for book in BOOKS:
    book.update({"name": str(book.get("number", "undefined"))})


def rupdate(book):
    tmp = {}
    tmp.update({"nb_epi": 0, "list_id_epi": [], "nb_kw": 0, "list_id_kw": []})
    tmp.update(book)
    return tmp


BOOKS = {book.get("name"): rupdate(book) for book in BOOKS}
tmp = BOOKS
BOOKS = defaultdict(lambda: rupdate({"name": "undefined", "number": 0, "url": ""}))
BOOKS.update(tmp)

for passage in PASSAGES:
    book_name = str(passage.get("book", {}).get("number", "undefined"))
    BOOKS[book_name]["list_id_epi"].append(passage.get("id"))
    BOOKS[book_name]["list_id_kw"].extend(passage.get("keywords"))
    BOOKS[book_name]["nb_epi"] += 1
    BOOKS[book_name]["nb_kw"] += len(passage.get("keywords"))

edges = {}

for node_1 in BOOKS:
    for node_2 in BOOKS:
        if node_1 != node_2:
            set_kw_1 = set(BOOKS[node_1]["list_id_kw"])
            set_kw_2 = set(BOOKS[node_2]["list_id_kw"])
            edges[tuple(sorted([node_1, node_2]))] = len(
                set_kw_1.intersection(set_kw_2)
            )


edges = [{"source": a, "target": b, "value": value} for (a, b), value in edges.items() if value != 0]

nodes = [value for _, value in BOOKS.items()]
data={ "nodes": nodes, "links": edges}

def save_encoded_json(result, path):
    p=pathlib.Path(__file__).parent / path
    str_result = json.dumps(result, indent=4, ensure_ascii=False).encode('utf-8')
    with p.open('w+') as stream :
        stream.write(str_result.decode())

save_encoded_json(data, "data.json")

