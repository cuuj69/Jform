"""Entry for json files to be restructured
"""

from test import Modify


if __name__ == '__main__':
    modifier = Modify()
    modifier.load_json()  # Load JSON data before applying operations
    modifier.main()
