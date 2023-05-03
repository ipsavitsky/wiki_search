import argparse
import logging as log
import sys

from bs4 import BeautifulSoup
from markdownify import MarkdownConverter
from rich.console import Console
from rich.markdown import Markdown

from .options import Options
from .soup_filters import filter_soup
from .wikipedia import NoArticleFound, fetch_wiki_data

log.basicConfig(level=log.INFO)

console = Console()
options = Options()

parser = argparse.ArgumentParser(description="Search a Wikipedia article and print it")
parser.add_argument("--locale", type=str, default="en")
parser.add_argument("--skip_tables", action="store_false")
parser.add_argument("keyword", type=str, help="The keyword to search")
args = parser.parse_args()

options.class_prefix = args.locale
options.skip_tables = args.skip_tables

try:
    page_info = fetch_wiki_data(options, args.keyword)
except NoArticleFound as e:
    console.print(f'No article "{e.fprompt}" found')
    sys.exit(1)

soup = BeautifulSoup(page_info["text"]["*"], "html.parser")

filtered_soup = filter_soup(options, page_info["title"], soup)

md = MarkdownConverter(escape_underscores=False, autolinks=False).convert_soup(
    filtered_soup
)

markdown = Markdown(md)

with console.pager():
    console.print(markdown)
