from urllib.parse import urljoin
from urllib.request import urlopen
import bs4


class WebClient(object):
    def __init__(self):
        pass

    def get_web_page(self):
        # get web page
        webpage = urlopen("http://bid.udl.cat/ca/")
        html = webpage.read()
        return html

    def parse_web_page(self, html):
        soup = bs4.BeautifulSoup(html, features="lxml")
        news = soup.find_all("li", "box")
        information = []
        links = []
        dates = []
        for new in news:
            title_tag = new.find("a")
            title = title_tag['title']
            link = title_tag['href']
            link = urljoin("http://bid.udl.cat/ca/", link)
            time_tag = new.find('time')
            time = time_tag.text.strip()
            information.append((title, link, time))
        return information, dates, links

    def get_information(self):
        html = self.get_web_page()
        # read information web page
        info = self.parse_web_page(html)
        return info


if __name__ == "__main__":
    client = WebClient()
    information = client.get_information()
    print(information)


#hola