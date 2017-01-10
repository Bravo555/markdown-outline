class Header():
    def __init__(self, text, level, children = None):
        self.text = text
        self.children = [] if children is None else children
        self.parent = None
        self.level = level

    def __repr__(self):
        return '"{}": {}'.format(self.text, str(self.children))

    def add_child(self, child):
        self.children.append(child)
        child.parent = self
        return child

def get_outline(document):
    outline = Header('<ROOT>', 0)
    current_header = outline
    for line in document:
        if line.startswith('#'):
            header_level = int(line.split()[0].count('#'))
            text = ' '.join(line.split()[1:])

            if header_level > current_header.level:
                if header_level > current_header.level + 1:
                    for expected_header_level in range(current_header.level + 1, header_level):
                        current_header = current_header.add_child(child = Header('<NO LEVEL ' + str(expected_header_level) + ' HEADER>',
                            current_header.level))

                current_header = current_header.add_child(Header(text, header_level))

            elif header_level == current_header.level:
                current_header = current_header.parent.add_child(Header(text, header_level))
                
            elif header_level < current_header.level:
                for expected_header_level in range(current_header.level - 1, header_level - 2, -1):
                    current_header = current_header.parent
                current_header = current_header.add_child(Header(text, header_level))

    return outline.children

def prettify(outline, level=0):
    if level == 0:
        print(outline.text)
    elif level > 0:
        print(' ' * (level - 1) * 2 + '˫', outline.text)
    if outline.children:
        for header in outline.children:
            prettify(header, level+1)
