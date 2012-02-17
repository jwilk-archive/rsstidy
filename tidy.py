import lxml.html
import lxml.etree

def remove(obj):
    obj.getparent().remove(obj)

def remove_all(document, *paths):
    for path in paths:
        for obj in document.findall(path):
            remove(obj)

def fix_html(htmlbytes):
    if b'charset="iso-8859-2"' in htmlbytes:
        htmlstr = htmlbytes.decode('ISO-8859-2')
    else:
        htmlstr = htmlbytes
    document = lxml.html.document_fromstring(htmlstr)
    subdocument = document.find(".//div[@id='gazeta_article']")
    if subdocument is not None:
        document = subdocument
    document = lxml.etree.ElementTree(document)
    remove_all(document,
        "//div[@class='articleToolBoxBottom']",
        "//div[@class='author']",
        "//div[@class='authordate']",
        "//div[@class='editorPicks ']",
        "//div[@class='index mod_zi6']",
        "//div[@class='kyoceraBox']",
        "//div[@class='mod_inner']",
        "//div[@class='more']",
        "//div[@class='seealso']",
        "//div[@class='test']",
        "//div[@class='tylko_int']",
        "//div[@id='articleComments']",
        "//div[@id='articleCopyright']",
        "//div[@id='article_toolbar']",
        "//div[@id='banP4']",
        "//div[@id='gazeta_article_author']",
        "//div[@id='gazeta_article_brand']",
        "//div[@id='gazeta_article_image']",
        "//div[@id='gazeta_article_likes']",
        "//div[@id='gazeta_article_share']",
        "//div[@id='gazeta_article_tags']",
        "//div[@id='gazeta_article_tools']",
        "//div[@id='recommendations']",
        "//div[@id='socialNewTools']",
        "//ul[@id='articleToolbar']",
        '//img',
        '//like',
        '//link',
        '//meta',
        '//script',
        '//style',
    )
    return document

# vim:ts=4 sw=4 et
