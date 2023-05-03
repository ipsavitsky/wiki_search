import requests
from options import Options


class NoArticleFound(Exception):
    def __init__(self, failed_prompt: str):
        self.fprompt = failed_prompt


def fetch_wiki_data(opts: Options, prompt: str) -> str:
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
