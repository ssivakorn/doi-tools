# doi-tools

DOI lookup tools
----------------
Do a look up for DOI from paper author's name and title.
Credit: http://www.crossref.org/guestquery/

Usage
-----
In short, do this

```sh
$ python3 doilookup.py -a "sivakorn" -t "I am Robot: (Deep) Learning to Break Semantic Image CAPTCHAs"
```

```sh
sivakorn|I am Robot: (Deep) Learning to Break Semantic Image CAPTCHAs|http://dx.doi.org/10.1109/EuroSP.2016.37
```

For more help, do
```sh
$ python3 doilookup.py -h
```

```sh
Simple script to lookup DOI from author and title

optional arguments:
  -h, --help            show this help message and exit
  -a AUTHOR, --author AUTHOR
                        author's lastname
  -t TITLE, --title TITLE
                        paper title
  --html HTML           get full html output page: [filename]
```


