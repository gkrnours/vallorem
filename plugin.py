from itertools import chain

from pelican import contents, generators, readers, signals
from pelican.urlwrappers import Category
from markdown import Markdown

from vallorem.model import db, Page

class SQLGenerator(generators.Generator):
    ctx = None
    def __init__(self, context, settings, path, theme, output_path):
        self.ctx = context

    def generate_context(self):
        md = Markdown()
        with db.session() as s:
            pages = s.query(Page).all()
        for p in pages:
            content = md.convert(p.content)
            metadata = {
                'title': p.titre,
                'category': Category(p.categorie, {})
            }
            page = contents.Page(content, metadata)
            self.ctx['pages'].append(page)

def add_generators(pelican_object):
    return SQLGenerator

def register():
    signals.get_generators.connect(add_generators)