#!/usr/bin/python3
"""the  script that
- fetches https://alx-intranet.hbtn.io/status.
- uses urlib package
"""
import urllib.request


def main():
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        html = res.read()

    print("Body res:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf-8')))


if __name__ == "__main__":
    main()
