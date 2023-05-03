"""Wikipedia search options module"""
from dataclasses import dataclass


@dataclass
class Options:
    """Wikipedia search options class"""

    class_prefix: str = "en"
    skip_tables: bool = True
