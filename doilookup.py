# Copyright (c) 2015 Suphannee Sivakorn
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
# USA

from __future__ import print_function
import argparse
import requests
import re
import sys

# Results generated from crossref.org database. Thank you!
SEARCH_URL = "http://www.crossref.org/guestquery"
SEARCH_NOTFOUND = "search not found"
PAYLOAD = {
    # default payload
    "queryType": "author-title",
    "auth2": "",    # author
    "atitle2": "",  # title
    "multi_hit": "true",
    "article_title_search": "Search"
}


def lookup(author, title, html=None):
    """ DOI lookup function
    author: paper author's last name
    title: paper title
    html: html file name to be saved
    returns outputs of DOIs found
    """
    founds = []

    payload = dict(PAYLOAD)
    payload["auth2"] = author
    payload["atitle2"] = title
    ret = requests.post(SEARCH_URL, data=payload)
    body = ret.text

    if html:
        with open(html, 'w') as filep:
            filep.write(body)

    matches = re.findall('<a href="?\'?([^"\'>]*)', body)
    if matches:
        for match in matches:
            if "http://dx.doi.org/" in match:
                founds.append(match)
    return founds

def main(argv):
    """ Main program ... duh.
    """
    parser = argparse.ArgumentParser(
                description="Simple script to lookup DOI from author and title")
    parser.add_argument("-a", "--author",
                        required=True, help="author's lastname")
    parser.add_argument("-t", "--title",
                        required=True, help="paper title")
    parser.add_argument("--html",
            help="get full html output page: [filename]")

    args = parser.parse_args()
    author = args.author
    title = args.title
    html = args.html

    # Do it
    founds = lookup(author, title, html)
    for item in founds:
        print("%s|%s|%s" % (author, title, item), file=sys.stdout)


if __name__ == "__main__":
    main(sys.argv)

