"""Entry for json files to be restructured
"""
#!/usr/bin/python3

from test import Modify


if __name__ == '__main__':
    modifier = Modify()
    modifier.load_json()  # Load JSON data before applying operations
    modifier.main()
