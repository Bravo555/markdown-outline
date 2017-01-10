import unittest
import markdown_outline

class TestMarkdownOutline(unittest.TestCase):
    def test_get_outline(self):
        with open('fixtures/document.md', 'r') as f:
            document = f.readlines()

        result = markdown_outline.get_outline(document)
        expected_result = (
            '["A document": ['
                '"Level 2 heading": ['
                    '"Level 3 heading": [], '
                    '"Another level 3 heading": []'
                '], '
                '"Next level 2 heading": []'
            ']]')
        self.assertEqual(str(result), expected_result)

if __name__ == '__main__':
    unittest.main()
