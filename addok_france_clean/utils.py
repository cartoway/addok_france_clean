import re
from addok.helpers.text import Token

def clean_query(q):
  q = str(q) # Hack, why I need this ?
  q = re.sub(r'\bb\.? ?p\.? ?[\d]*', '', q, flags=re.IGNORECASE) # Orverload
  q = re.sub(r'\bc\.? ?s\.? ?[\d]*', '', q, flags=re.IGNORECASE) # Orverload
  q = re.sub(r'\blieu[ -]?dit', '', q, flags=re.IGNORECASE)
  q = re.sub(r'\br\.? ?[n|d]\.? ?[\d]*', '', q, flags=re.IGNORECASE)
  q = re.sub(r'\bb(a|â)t(\.|iment)?\s*([0-9]+|[A-Z]\s+)', '', q, flags=re.IGNORECASE)
  q = re.sub(r'\bporte ?([0-9]+|[A-Z]\s+)', '', q, flags=re.IGNORECASE)
  q = re.sub(r'\bbureau ?([0-9]+|[A-Z]\s+)', '', q, flags=re.IGNORECASE)
  q = re.sub(r'\b([eé]tage) ?[0-9]{1,2}', '', q, flags=re.IGNORECASE)
  q = re.sub(r'\bN[o°](?=[ 0-9])', '', q, flags=re.IGNORECASE)
  q = re.sub('\(.*?\)', '', q, flags=re.IGNORECASE)
  return q

GENERAL_CHARLES_DE_GAULLE = ('général', 'charles', 'de', 'gaulle')
PREFIX_TREE = {
  'charles': {'de': {'gaulle': GENERAL_CHARLES_DE_GAULLE}},
  'general': {'de': {'gaulle': GENERAL_CHARLES_DE_GAULLE}},
  'général': {'de': {'gaulle': GENERAL_CHARLES_DE_GAULLE}},
  'de': {'gaulle': GENERAL_CHARLES_DE_GAULLE},
  'la': {'fayette': ('lafayette',)},
}

def multi_token_synonymize_pos(tokens, pos, shift, tree):
  key = str(tokens[pos + shift])
  y = tree.get(key)
  if y is None:
    return (None, None)
  elif isinstance(y, dict):
    if pos + shift + 1 >= len(tokens):
      return (None, None)
    else:
      return multi_token_synonymize_pos(tokens, pos, shift + 1, tree[key])
  else:
    return (y, shift + 1)

def multi_token_synonymize(tokens):
  tokens = list(tokens)
  for i in range(len(tokens)):
    (replace, lenght) = multi_token_synonymize_pos(tokens, i, 0, PREFIX_TREE)
    if replace is not None:
      tokens = tokens[:i] + [Token(r) for r in replace] + tokens[i+lenght:]
      break

  for position, token in enumerate(tokens):
    token.position = position
    yield token
