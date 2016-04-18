# coding=UTF-8
from flask import Flask, render_template
import urllib2
import sys
import bs4

SEPARATORS = (' ', ',', '?', '!', '.', ':', '\n', '<', '>', ';', '"', '=', '(', ')')

app = Flask(__name__)


@app.route('/')
def index(args=None):
    """Homepage"""
    return render_template('template.html', args=args)


def parse_article_and_add_TM_to_source(input_url):
    content = urllib2.urlopen(input_url).read()
    soup = bs4.BeautifulSoup(content, "html.parser")
    my_tag = soup.find('div', {"class": "content html_format"})
    unicode_charachter_list = [x for x in unicode(my_tag)]
    j = 0
    for i in range(len(unicode_charachter_list)):
        if unicode_charachter_list[i] not in SEPARATORS:
            j += 1
            if j == 6 and unicode_charachter_list[i + 1] in SEPARATORS:
                j = 0
                unicode_charachter_list.insert(i + 1, u'\u2122')
        else:
            j = 0

    output_html = ''.join(unicode_charachter_list)

    return output_html


if __name__ == '__main__':
    print "Input parameters: ", sys.argv

    html_parsed = parse_article_and_add_TM_to_source(sys.argv[1])
    f = open('templates/template.html', "w")

    with f:
        f.write(html_parsed.encode('utf-8'))
    app.run(debug=True, port=5555)
