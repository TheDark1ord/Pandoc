from panflute import *
import sys

headers = []


def duplicateHeaders(elem, doc):
    if type(elem) == Header:
        header = stringify(elem)
        if header in headers:
            print("Duplicate header: " + header, file=sys.stderr)
        else:
            headers.append(header)


def toUpper(elem, doc):
    if type(elem) == Str:
        elem.text = elem.text.upper()


def thirdLevelHeaders(elem, doc):
    if type(elem) == Header and elem.level <= 3:
        return elem.walk(toUpper)


def boldKeyword(doc):
    doc.replace_keyword("BOLD", Strong(Str("BOLD")))


def main(doc=None):
    return run_filters([duplicateHeaders, thirdLevelHeaders], finalize=boldKeyword, doc=doc)


if __name__ == "__main__":
    main()
