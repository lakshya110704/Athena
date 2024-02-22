from flask import Flask, request, jsonify
import torch
import torch.nn as nn
from torch.nn import functional as F

from train import Block

app = Flask(__name__)

class BigramLanguageModel(nn.Module):
    def __init__(self, vocab_size, n_embd, block_size, n_head, n_layer):
        super().__init__()
        self.token_embedding_table = nn.Embedding(vocab_size, n_embd)
        self.position_embedding_table = nn.Embedding(block_size, n_embd)
        self.blocks = nn.Sequential(*[Block(n_embd, n_head=n_head) for _ in range(n_layer)])
        self.ln_f = nn.LayerNorm(n_embd)
        self.lm_head = nn.Linear(n_embd, vocab_size)

    def forward(self, idx, targets=None):
        B, T = idx.shape
        tok_emb = self.token_embedding_table(idx)
        pos_emb = self.position_embedding_table(torch.arange(T, device=idx.device))
        x = tok_emb + pos_emb
        x = self.blocks(x)
        x = self.ln_f(x)
        logits = self.lm_head(x)

        if targets is None:
            loss = None
        else:
            B, T, C = logits.shape
            logits = logits.view(B * T, C)
            targets = targets.view(B * T)
            loss = F.cross_entropy(logits, targets)

        return logits, loss

    def generate(self, idx, max_new_tokens):
        for _ in range(max_new_tokens):
            idx_cond = idx[:, -block_size:]
            logits, loss = self(idx_cond)
            logits = logits[:, -1, :]
            probs = F.softmax(logits, dim=-1)
            idx_next = torch.multinomial(probs, num_samples=1)
            idx = torch.cat((idx, idx_next), dim=1)
        return idx

vocab_size = 3296  # Assuming the correct vocabulary size
n_embd = 64
block_size = 32
n_head = 4
n_layer = 4
device = 'cuda' if torch.cuda.is_available() else 'cpu'

model = BigramLanguageModel(vocab_size, n_embd, block_size, n_head, n_layer)
model_path = '/Users/lakshya/Desktop/Projects/LLM/generated_text.txt'
try:
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()
except Exception as e:
    print(f"Error loading pre-trained model: {type(e).__name__} - {str(e)}")

def generate_text(prompt, model):
    chars = [ord(c) for c in prompt]
    prompt_tensor = torch.tensor(chars, dtype=torch.long, device=device).unsqueeze(0)
    generated_tensor = model.generate(prompt_tensor, max_new_tokens=200)
    generated_text = ''.join([chr(idx) for idx in generated_tensor.squeeze().tolist()])
    return generated_text

@app.route('/generate_text', methods=['POST'])
def generate_text_api():
    data = request.json
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({'error': 'Please provide a prompt.'}), 400

    generated_text = generate_text(prompt, model)

    return jsonify({'generated_text': generated_text})

if __name__ == '__main__':
    app.run(debug=True)
