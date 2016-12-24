class Header():
    def __init__(self, text, level, children=[]):
        self.text = text
        self.children = children
        self.parent = None
        self.level = level

    def __repr__(self):
        return "'{}': {}".format(self.text, str(self.children))

    def add_child(self, child):
        self.children.append(child)
        return 0

        # child.parent = self



def get_outline(document):
    outline = Header('<NO HEADER>', 0)
    current_header = outline
    for line in document:
        if line.startswith('#'):
            header_level = int(line.split()[0].count('#'))
            text = ' '.join(line.split()[1:])

            if header_level > current_header.level:
                for expected_header_level in range(header_level - current_header.level - 1):
                    child = Header('<NO LEVEL ' + str(expected_header_level + 1) + ' HEADER>',
                        current_header.level + 1)
                    current_header = current_header.add_child()

                current_header = current_header.add_child(Header(text, header_level))




    return outline

if __name__ == '__main__':
    doc = ['### h3 boi']
    outline = get_outline(doc)
