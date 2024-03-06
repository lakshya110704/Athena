import torch
import torch.nn as nn
from torch.nn import functional as F
from flask import Flask, request, jsonify

from train import Block, block_size, stoi, itos, vocab_size

# Define your model architecture and any necessary functions
class BigramLanguageModel(nn.Module):
    def __init__(self, vocab_size, n_embd=64, n_head=4, n_layer=4, block_size=32):
        super().__init__()
        self.token_embedding_table = nn.Embedding(vocab_size, n_embd)
        self.position_embedding_table = nn.Embedding(block_size, n_embd)
        self.blocks = nn.Sequential(*[Block(n_embd, n_head=n_head) for _ in range(n_layer)])
        self.ln_f = nn.LayerNorm(n_embd)
        self.lm_head = nn.Linear(n_embd, vocab_size)

    def forward(self, idx, targets=None):
        B, T = idx.shape
        tok_emb = self.token_embedding_table(idx)
        pos_emb = self.position_embedding_table(torch.arange(T, device=device))
        x = tok_emb + pos_emb
        x = self.blocks(x)
        x = self.ln_f(x)
        logits = self.lm_head(x)

        if targets is None:
            loss = None
        else:
            B, T, C = logits.shape
            logits = logits.view(B*T, C)
            targets = targets.view(B*T)
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

# Define Flask app
app = Flask(__name__)

# Function to encode and decode input/output
def encode(s):
    return [stoi[c] for c in s]

def decode(l):
    return ''.join([itos[i] for i in l])

# Define API endpoint for generating response
@app.route('/generate_response', methods=['POST'])
def generate_response():
    try:
        user_input = request.json['user_input']
        max_tokens = request.json.get('max_tokens', 50)  # Default max tokens if not provided
        encoded_input = torch.tensor([encode(user_input)], device=device)
        generated_sequence = model.generate(encoded_input, max_tokens)
        generated_text = decode(generated_sequence[0].tolist())
        return jsonify({'response': generated_text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    # Assuming necessary imports and definitions
    # Define paths and device
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    MODEL_PATH = '/path/to/your/model.pth'
    # Load vocabulary, model, and other necessary definitions
    model = BigramLanguageModel(vocab_size)
    model.load_state_dict(torch.load(MODEL_PATH))
    model.eval()
    app.run(host=8000)
    app.run(debug=True)
    

