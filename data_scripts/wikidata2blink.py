import json, gzip


with gzip.open("/workspace/nilk_data/wikidata-20170213-all.json.gz", 'rb', 'rb') as gf, open("documents.json", "w") as o:
    for ln in gf:
        if ln == b'[\n' or ln == b']\n':
            continue
        if ln.endswith(b',\n'):
            obj = json.loads(ln[:-2])
        else:
            obj = json.loads(ln)

        if "en" not in obj["labels"].keys():
            continue
        if "en" not in obj["descriptions"].keys():
            continue

        id = obj["id"]
        name = obj["labels"]["en"]["value"]

        description = obj["descriptions"]["en"]["value"]

        o.write(json.dumps({"document_id": id, "title": name, "text": description}) + "\n")





