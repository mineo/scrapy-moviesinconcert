#!/usr/bin/env python
# coding: utf-8
# Copyright © 2016 Wieland Hoffmann
# License: MIT, see LICENSE for details
import scrapy


from ..items import MoviesinconcertItem
from itertools import chain, dropwhile


def concert_chunks(_list):
    """Split up `list` into data tuples.

    :type _list: list
    """
    for i in range(0, len(_list), 6):
        yield tuple(_list[i:i + 6])


def dropper(element):
    """Return true if we're not interested in an element.

    :param element: str
    """
    return (element is None) or (not element.strip())


class MoviesInConcertSpider(scrapy.Spider):
    """Scrapy spider for moviesinconcert.nl."""

    name = "moviesinconcert"

    start_urls = [
        'http://www.moviesinconcert.nl/index.php?page=concertlist'
    ]

    def parse(self, response):
        """Parse `response`.

        :type response: scrapy.http.Response
        """
        tds = response.xpath("//table/tr/td")
        data = (item for item in tds)
        data = (et.xpath("./text()|./a/@href|./a/text()").extract() or
                [None] for et in data)
        data = chain.from_iterable(data)
        data = dropwhile(dropper, data)
        data = list(data)
        for i in concert_chunks(data):
            date, country, state, city, link, title = i
            yield MoviesinconcertItem(
                date=date,
                country=country.strip(),
                state=state,
                city=city,
                title=title,
                link=link)
