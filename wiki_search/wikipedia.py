"""Wikipedia api request module."""
import requests

from .options import Options


class NoArticleFound(Exception):
    """No found article exception class."""

    def __init__(self, failed_prompt: str):
        self.fprompt = failed_prompt


def fetch_wiki_data(opts: Options, prompt: str) -> str:
    """Fetch data html from Wiki api

    :param opts: Request options.
    :type opts: Options
    :param prompt: Prompt to search at Wikipedia.
    :type prompt: str
    :raises NoArticleFound: Raised if no article found at Wikipedia.
    :return: String of HTML returned by API
    :rtype: str
    """
    url = f"https://{opts.class_prefix}.wikipedia.org/w/api.php"
    params = {
        "action": "parse",
        "page": prompt,
        "format": "json",
        "prop": "text",
        "redirects": "",
    }
    data = requests.get(url, params=params).json()
    if "error" in data:
        raise NoArticleFound(prompt)
    return data["parse"]
