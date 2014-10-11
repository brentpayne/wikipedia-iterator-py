from bz2 import BZ2File

from kennyg.element import KeyValueCollector
from kennyg.sax_handler import KennyGSAXHandler
from kennyg.parser import parse

class YieldPageData(KeyValueCollector):
    def end(self, *args, **kwargs):
        yield self.value()

def __setup_kennyg_parser():
    schema = {
        'mediawiki': {
            'page': YieldPageData(title='title', text='text')
        }
    }
    return KennyGSAXHandler(schema)



def text_documents(gzip_file):
    kg = __setup_kennyg_parser()
    with BZ2File(gzip_file) as fp:
        for item in parse(fp, kg):
            yield item

if __name__ == '__main__':
    for document in text_documents('/Users/brentpayne/Documents/wikipedia/20140917/enwiki-latest-pages-articles.xml.bz2'):
        print document

