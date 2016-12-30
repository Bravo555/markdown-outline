class Header():
    def __init__(self, text, level, children = None):
        self.text = text
        self.children = [] if children is None else children
        self.parent = None
        self.level = level

    def __repr__(self):
        return "'{}': {}".format(self.text, str(self.children))

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

def get_outline(document):
    outline = Header('<NO ROOT>', 1)
    current_header = outline
    for line in document:
        if line.startswith('#'):
            header_level = int(line.split()[0].count('#'))
            text = ' '.join(line.split()[1:])

            if header_level > current_header.level:
                if header_level > current_header.level + 1:
                    for expected_header_level in range(header_level - current_header.level):
                        child = Header('<NO LEVEL ' + str(expected_header_level + 1) + ' HEADER>',
                            current_header.level + 1)
                        current_header.add_child(child)
                        current_header = child
                current_header.add_child(Header(text, header_level))




    return outline

if __name__ == '__main__':
    doc = ['### h3 boi']
    outline = get_outline(doc)
