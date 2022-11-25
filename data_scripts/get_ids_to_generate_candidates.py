import json
import torch

from blink.biencoder.biencoder import load_biencoder
from blink.biencoder.data_process import (
    get_candidate_representation,
)
import argparse

# PYTHONPATH=. python3 ../BLINK_changed/data_scripts/get_ids_to_generate_candidates.py --biencoder_config output/epoch_4/config.json --biencoder_model output/epoch_4/pytorch_model.bin --entites_file ../BLINK_changed/data_scripts/documents.json --save_ids .
# after run generate_candidates.py

parser = argparse.ArgumentParser()
parser.add_argument('--biencoder_config', type=str, required=True, help='filepath to saved model config')
parser.add_argument('--biencoder_model', type=str, required=True, help='filepath to saved model')
parser.add_argument('--entites_file', type=str, required=True, help='filepath to entities to encode (.jsonl file)')
parser.add_argument('--save_ids', type=str, help='filepath to entities pre-parsed into IDs')

args = parser.parse_args()


# Load biencoder model and biencoder params just like in main_dense.py
with open(args.biencoder_config) as json_file:
    biencoder_params = json.load(json_file)
    biencoder_params["path_to_model"] = args.biencoder_model
biencoder = load_biencoder(biencoder_params)

# Read 10 entities from entity.jsonl
# entities = []
# count = 10
# with open(args.entites_file) as f:
#     for i, line in enumerate(f):
#         entity = json.loads(line)
#         entities.append(entity)
#         if i == count-1:
#             break

# Get token_ids corresponding to candidate title and description
tokenizer = biencoder.tokenizer
max_context_length, max_cand_length = biencoder_params["max_context_length"], biencoder_params["max_cand_length"]
max_seq_length = max_cand_length
ids = []

with open(args.entites_file) as f:
    for line in f:
        entity = json.loads(line)
        candidate_desc = entity['text']
        candidate_title = entity['title']
        cand_tokens = get_candidate_representation(
            candidate_desc,
            tokenizer,
            max_seq_length,
            candidate_title=candidate_title
        )

        token_ids = cand_tokens["ids"]
        ids.append(token_ids)

ids = torch.tensor(ids)
torch.save(ids, args.save_ids)
