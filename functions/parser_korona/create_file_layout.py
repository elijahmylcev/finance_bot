from bs4 import BeautifulSoup

def create_html(web_page_source):
    layout = BeautifulSoup(web_page_source, 'html.parser')

    with open('ind.html', 'w') as f:
        f.write(web_page_source)
