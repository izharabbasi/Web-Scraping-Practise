from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum dolor sit amet. Consectetur edipiscim elit.</p>
<p>Here's another p without a class</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>'''

simple_soup = BeautifulSoup(SIMPLE_HTML, "html.parser")


def header():
    h1_tag = simple_soup.find("h1")
    print(h1_tag.string)


def list():
    list_item = simple_soup.find_all("li")
    one_list = [l.string for l in list_item]
    print(one_list)


def subtitle():
    paragraph = simple_soup.find("p", {"class": "subtitle"})
    print(paragraph.string)


def all_para():
    paragraphs = simple_soup.find_all("p")
    para = [
        p for p in paragraphs if "subtitle" not in p.attrs.get("class", [])]
    print(para[0].string)


header()
list()
subtitle()
all_para()
