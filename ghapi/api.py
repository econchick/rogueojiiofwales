# -*- coding: utf-8 -*-
import urlparse
from django.http import QueryDict
from ghapi.linkheader import parse_link_value
import requests

def get_next_page(response):
    link = response.headers.get('link', None)
    if not link:
        return None
    output = parse_link_value(link)
    for url, info in output.items():
        if info.get('rel', None) == 'next':
            return QueryDict(urlparse.urlparse(url).query)['page']
    return None

class GitHub(object):
    def __init__(self, token=None):
        headers = {}
        if token:
            headers['Authorization'] = 'token %s' % token
        self.session = requests.session(headers=headers)

    def get(self, path, params=None):
        """
        Gets a resource, eg 'users/ojii'.

        Returns parsed json data as a python dictionary
        """
        return self._get(path, params)[0]

    def _get(self, path, params=None):
        if params is None:
            params = {}
        params['per_page'] = 100
        response = self.session.get('https://api.github.com/%s' % path, params=params)
        response.raise_for_status()
        return response.json, response


    def get_iter(self, path, params=None):
        """
        Returns an iterator over a resource, eg 'repos/divio/django-cms/watchers' that automatically handles
        pagination.
        """
        if params is None:
            params = {}
        data, response = self._get(path, params)
        for thing in data:
            yield thing
        next_page = get_next_page(response)
        if next_page:
            params['page'] = next_page
            for thing in self.get(path, params):
                yield thing
