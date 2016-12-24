import sys
sys.path.append('../')
from markdown_outline import get_outline

with open('fixtures/document.md', 'r') as f:
	document = f.readlines()

def test_markdown_outline():
	result = get_outline(document)

	assert result == 
