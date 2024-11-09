import os
import tokenize
from io import BytesIO

def CountTokensInScript(FilePath):
    with open(FilePath, 'r', encoding='utf-8') as f:
        ScriptContent = f.read()
    Tokens = tokenize.tokenize(BytesIO(ScriptContent.encode('utf-8')).readline)
    TokenCount = sum(1 for token in Tokens if token.type not in (tokenize.ENDMARKER, tokenize.COMMENT, tokenize.NL))
    return TokenCount

FilePath = os.path.join(os.path.dirname(__file__), 'Bot.py')
print("Number of tokens:", CountTokensInScript(FilePath) - 16) # Subtract 16 to exclude the function and the required imports