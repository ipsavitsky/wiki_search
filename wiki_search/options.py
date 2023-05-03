from dataclasses import dataclass


@dataclass
class Options:
    class_prefix: str = "en"
    skip_tables: bool = True
