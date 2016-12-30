import sys
sys.path.append('../')
from markdown_outline import get_outline

with open('fixtures/document.md', 'r') as f:
    document = f.readlines()

result = get_outline(document)
expected_result = (
    '["A document": ['
        '"Level 2 heading": ['
            '"Level 3 heading": [], '
            '"Another level 3 heading": []'
        '], '
        '"Next level 2 heading": []'
    ']]')

def test_markdown_outline():
    assert str(result) == expected_result
