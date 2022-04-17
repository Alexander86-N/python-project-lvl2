from pathlib import Path
from gendiff.parsing import parser


def fetches_data(data):
    """ Determines the file format and opens it. """
    path = Path(data)
    extension = path.suffix
    with open(data) as f:
        return parser(f, extension[1:])
