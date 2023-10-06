from lang_parser.parser import GenericParser
from pathlib import PurePosixPath, Path


class DirParser(GenericParser):
    """
    A parser for DirBuster's 'simple' output type and the `find` command output.
    """
    def __init__(self, filename):
        super().__init__(filename, 'r')
        self.file_lines = []
        with open(filename, 'r') as f:
            self.file_lines = sorted([x.strip() for x in f.readlines()])
        self.parsed_content = None

    @staticmethod
    def _parse_into_dict(paths: list[str | Path]) -> dict:
        """Builds a tree like structure out of a list of paths"""
        def _recurse(dic: dict, chain: tuple[str, ...] | list[str]):
            if len(chain) == 0:
                return
            if len(chain) == 1:
                dic[chain[0]] = {}
                return
            key, *new_chain = chain
            if key not in dic:
                dic[key] = {}
            _recurse(dic[key], new_chain)
            return

        new_path_dict = {}
        for path in paths:
            _recurse(new_path_dict, PurePosixPath(path).parts)
        return new_path_dict
    
    def parse(self):
        self.parsed_content = self._parse_into_dict(self.file_lines)
        return self.parsed_content