import torch
import os

cand_encode_path = "/workspace/BLINK_changed/data_scripts/20_percent/cand_encoding_bi_eval/"

candidate_encoding = torch.load(cand_encode_path + '/cand_enc_0')
encodings = [candidate_encoding]
for filename in os.listdir(cand_encode_path):
    if filename == 'cand_enc_0':
        continue

    cd_tmp = torch.load(os.path.join(cand_encode_path, filename))
    encodings.append(cd_tmp)

candidate_encoding = torch.cat(encodings, dim=0)
torch.save(candidate_encoding, cand_encode_path + "/entities_NILK_20_percent.t7")