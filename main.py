import docx
import re
import copy

sc = re.compile('\{.+\}')


class Citation(object):

    def __init__(self, name, caseid, page, year):
        self.name = name
        self.caseid = caseid
        self.page = page
        self.year = year


def insert_citation(r, c):
    r.text = c.name
    r2 = copy.deepcopy(r._r)
    r.underline = True
    r2.text = ", {}, {} ({})".format(c.caseid, c.page, c.year)
    r._r.addnext(r2)


def scan_refs(doc):

    references = []

    for p in doc.paragraphs:
        for r in p.runs:
            cite = sc.search(r.text)
            if cite:
                references.append(cite.group(0)[1:-1])
    print('located {} citations'.format(len(references)))

    return(references)


def insert_citations(doc, citation_data):
    for p in doc.paragraphs:
        for r in p.runs:
            cite = sc.search(r.text)
            if cite:
                cite = cite.group(0)[1:-1].split('|')
                idx = cite[0].strip()
                pg = cite[1].strip()
                try:
                	c = [x for x in citation_data if x.caseid == idx][0]
                except:
                	print('citation not found for {}'.format(idx))
                	continue
                insert_citation(r, c)


def main():
    print('enter document name:')
    name = input()
    doc = docx.Document(name + '.docx')

    cdata = []
    cdata.append(Citation("Cooper Indus. v. Leatherman", "532 U.S. 424", "431", "2001"))
    cdata.append(Citation("Hartman v. Moore", "547 U.S. 250", "250", "2006"))
    cdata.append(Citation("Reichle v. Howards", "132 S. Ct. 2088", "2093", "2012"))

    refs = scan_refs(doc)
    print(refs)

    insert_citations(doc, cdata)
    doc.save('out.docx')

if __name__ == "__main__":
	main()


# doc.save('test2.docx')

# print('enter clone name:')
# clone_name = input()
# doc2.save(clone_name + '.docx')


# def transfer_paragraph(p, doc):
# 	inserted_p = doc_dest._body._body._insert_p(p._p)
