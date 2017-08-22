import multiprocessing
import bs4 as bs
import requests
import random
import string


def random_starting_url():
    name = ''.join([random.choice(string.ascii_lowercase) for _ in range(3)])
    url = ''.join(["http://", name, ".com"])
    return url


def check_links(url, link):
    if link.startswith("/"):
        return "".join([url, link])
    elif not link.startswith("http"):
        return None
    else:
        return link


def get_links(url):
    try:
        source = requests.get(url).text
        soup = bs.BeautifulSoup(source, "lxml")
        links = [link.get("href") for link in soup.findAll("a")]
        links = [check_links(url, link) for link in links]
        return links
    except Exception as e:
        print(e)


def save(data):
    with open("s12.txt", "w") as f:
        for i in data:
            if i is None:
                pass
            else:
                for ii in i:
                    if ii is None:
                        pass
                    else:
                        f.write("".join([ii, "\n"]))


def main():
    number_of_sites = 50
    p = multiprocessing.Pool(processes=number_of_sites)
    starting_urls = [random_starting_url() for _ in range(number_of_sites)]
    # starting_urls = ["http://google.com", "http://naver.com", "http://daum.net"]
    data = p.map(get_links, [link for link in starting_urls])
    p.close()
    save(data)

if __name__ == "__main__":
    main()
    with open("s12.txt", "r") as f:
        print(f.read())
