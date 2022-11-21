# {
#   "context_left": "3 console.\nSome users claim that Nvidia's Linux drivers impose artificial restrictions, like limiting the number of monitors that can be used at the same time, but the company has not commented on these accusations.\nIn 2014, with Maxwell GPUs, Nvidia started to require firmware by them to unlock all features of its graphics cards. Up to now, this state has not changed and makes writing open-source drivers difficult.\nDeep learning.\nNvidia GPUs are often used in deep learning, and accelerated analytics due to Nvidia's API CUDA which allows programmers to utilize the higher number of cores present in GPUs to parallelize programs. This parallelization can dramatically increase training speed of machine learning algorithms due to their extensive use of matrix and vector operations. They were included in many Tesla vehicles before",
#   "context_right": "announced at Tesla Autonomy Day in 2019 that the company developed its own SoC and Full Self-Driving computer now and would stop using Nvidia hardware for their vehicles. According to \"TechRepublic\", Nvidia GPUs \"work well for deep learning tasks because they are designed for parallel computing and do well to handle the vector and matrix operations that are prevalent in deep learning\". These GPUs are used by researchers, laboratories, tech companies and enterprise companies. In 2009, Nvidia was involved in what was called the \"big bang\" of deep learning, \"as deep-learning neural networks were combined with Nvidia graphics processing units (GPUs)\". That year, the Google Brain used Nvidia GPUs to create Deep Neural Networks capable of machine learning, where Andrew Ng determined that GPUs could increase the speed",
#   "mention": "Elon Musk",
#   "label_title": "Elon Musk",
#   "label": "Elon Reeve Musk (; born June 28, 1971) is an entrepreneur and business magnate. He is the founder, CEO and chief engineer at SpaceX; early stage investor, CEO, and product architect of Tesla, Inc.; founder of The Boring Company; and co-founder of Neuralink and OpenAI. A centibillionaire, Musk is one of the richest people in the world.\nMusk was born to a Canadian mother and South African father and raised in Pretoria, South Africa. He briefly attended the University of Pretoria before moving to Canada aged 17 to attend Queen's University. He transferred to the University of Pennsylvania two years later, where he received bachelors' degrees in economics and physics. He moved to California in 1995 to attend Stanford University but decided instead to pursue a business career, co-founding",
#   "label_id": 304371
# }
#

#!!!! The label_id corresponds to the line number (0-indexed) for the label in documents.jsonl. For e.g.,

import json

label_map = {}

line_number = 0
with open("documents.json") as f:
    for l in f:
        line = json.loads(l)
        id = line["document_id"]
        title = line["title"]
        text = line["text"]

        label_map[id] = (title, text, line_number)

        line_number += 1


with open("/workspace/nilk_data/train.json") as f, open("train.json", "w") as o, open("train_nil.json", "w") as on:
    for l in f:
        try:
            line = json.loads(l)
        except:
            print(l)

        id = line["wikidata_id"]
        is_nil = line["nil"]
        mention = line["mention"]
        context = line["context"]
        offset = line["offset"]

        if not is_nil:
            if id not in label_map:
                print("Missing wikidata id: " + id)
                continue

            title, text, line_number = label_map[id]

            o.write(json.dumps({"context_left": context[:offset], "context_right": context[offset + len(mention):], "mention": mention, "label_title": title, "label": text, "label_id": line_number}) + "\n")
        else:
            on.write(json.dumps({"context_left": context[:offset], "context_right": context[offset + len(mention):], "mention": mention}) + "\n")
