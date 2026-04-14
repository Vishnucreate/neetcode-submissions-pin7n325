import torch
import torch.nn as nn
from torchtyping import TensorType
from typing import List

class Solution:
    def get_dataset(self, positive: List[str], negative: List[str]) -> TensorType[float]:
        # 1. Build vocabulary: collect all unique words, sort them, assign integer IDs starting at 1
        combined = positive+negative

        vocabulary = sorted({word for sentence in combined for word in sentence.split()})

        token_id = {word:id+1 for id, word in enumerate(vocabulary)}

        encoded = [torch.tensor([token_id[word] for word in sentence.split()],dtype = torch.float32) for sentence in combined]

        return nn.utils.rnn.pad_sequence(encoded, batch_first=True)
        # 2. Encode each sentence by replacing words with their IDs
        # 3. Combine positive + negative into one list of tensors
        # 4. Pad shorter sequences with 0s using nn.utils.rnn.pad_sequence(tensors, batch_first=True)
        pass
