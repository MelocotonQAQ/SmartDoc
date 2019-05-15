import sys,re

def lines(file):
    """
    生成器,在文本最后加一空行
    """
    for line in file: yield line
    yield '\n'
 
def blocks(file):
    """
    生成器,生成单独的文本块
    """
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []


print ('<html><body>')

title = True
for block in blocks(sys.stdin):
    block = re.sub(r'\*(.+?)\*',r'<em>\1</em>',block)
    if title:
        print('<p>')
        print (block)
        print ('</p>')
        title =False
    else:
        print('<p>')
        print (block)
        print('</p>')

print('</body></html>')