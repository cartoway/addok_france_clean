# Addok usage_name_BAN_FR

[Addok](https://github.com/etalab/addok) plugin to support more french addresses clean.

## Addressed problem


## Configuration

```python
PROCESSORS_PYPATHS = [  # Rename in TOKEN_PROCESSORS / STRING_PROCESSORS?
    ...
    'addok_france_clean.multi_token_synonymize',
    'addok.helpers.text.synonymize',
    'addok_fr.phonemicize',
]
```

Add `addok_france_clean.clean_query` on top.

```python
QUERY_PROCESSORS_PYPATHS = [
    'addok_france_clean.clean_query',
    ...
```

## How it works
