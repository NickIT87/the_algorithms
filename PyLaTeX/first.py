# -*- coding: utf-8 -*-
from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape, bold


def fill_document(doc):
    with doc.create(Section('A section')):
        doc.append('Some regular text and some ')
        doc.append(italic('italic text. '))
        doc.append(bold('bold text. '))

        with doc.create(Subsection('A subsection')):
            doc.append('Also some crazy characters: $&#{}')
            doc.append(NoEscape(r"$$f'(a) = \lim_{x \to a} \frac{f(x) - f(a)}{x-a}$$"))


if __name__ == "__main__":
    doc = Document('basic')

    #doc.preamble.append(NoEscape(r'\usepackage[T1, T2A]{fontenc}'))
    doc.preamble.append(NoEscape(r'\usepackage[english, russian]{babel}'))
    #doc.preamble.append(NoEscape(r'\usepackage[koi8-r]{inputenc}'))
    #doc.preamble.append(NoEscape(r'\DeclareUnicodeCharacter{2014}{texemdash}'))
    

    doc.preamble.append(Command('title', 'Рус'))
    doc.preamble.append(Command('author', 'Anonymus author'))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    doc.append(NoEscape(r'\maketitle'))
    
    fill_document(doc)

    doc.generate_pdf(clean_tex=False, compiler='pdflatex')
