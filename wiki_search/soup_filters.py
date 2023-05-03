from bs4 import BeautifulSoup
from options import Options


def filter_soup(opts: Options, title: str, soup: BeautifulSoup) -> BeautifulSoup:
    body = soup.find("div", class_="mw-parser-output")
    for tag in body.find_all("table", class_="infobox"):
        tag.decompose()

    for tag in body.find_all("div", class_="navbox"):
        tag.decompose()

    if opts.skip_tables:
        for tag in body.find_all("table"):
            tag.decompose()
    else:
        for tag in body.find_all("table", class_="sidebar"):
            tag.decompose()

        for tag in body.find_all("table", class_="metadata"):
            tag.decompose()

    for tag in body.find_all("div", class_="metadata"):
        tag.decompose()

    for tag in body.find_all("style"):
        tag.decompose()

    for tag in body.find_all("span", class_="mw-editsection"):
        tag.decompose()

    for tag in body.find_all("span", class_="mw-cite-backlink"):
        tag.decompose()

    for tag in body.find_all("a"):
        tag["href"] = f"https://{opts.class_prefix}.wikipedia.org" + tag["href"]

    for tag in body.find_all("sup", class_="reference"):
        if "a" in tag:
            tag.string = tag["a"].text

    final_soup = BeautifulSoup()
    header_tag = final_soup.new_tag("h1")
    header_tag.string = title
    final_soup.append(header_tag)
    final_soup.append(body)

    return final_soup
