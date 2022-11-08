import json, gzip

# {
#   "title": "Steve Jobs",
#   "text": "Steven Paul Jobs (; February 24, 1955 – October 5, 2011) was an American business magnate, industrial designer, investor, and media proprietor. He was the chairman, chief executive officer (CEO), and co-founder of Apple Inc.; the chairman and majority shareholder of Pixar; a member of The Walt Disney Company's board of directors following its acquisition of Pixar; and the founder, chairman, and CEO of NeXT. Jobs is widely recognized as a pioneer of the personal computer revolution of the 1970s and 1980s, along with his early business partner and fellow Apple co-founder Steve Wozniak.\nJobs was born in San Francisco, California, and put up for adoption. He was raised in the San Francisco Bay Area. He attended Reed College in 1972 before dropping out that same year, and traveled",
#   "document_id": 7412236
# }

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

        o.write(json.dumps({"idx": id, "title": name, "text": description}) + "\n")





