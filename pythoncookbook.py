#!/usr/bin/env python2
# vim:fileencoding=utf-8
from calibre.web.feeds.news import BasicNewsRecipe

class Git_Pocket_Guide(BasicNewsRecipe):
    title = 'Python Cookbook'
    __author__  = 'Lionly'
    description = 'Python Cookbook 电子书'
    remove_tags_before = dict(name='section', attrs={'class':'chapter'})
    remove_tags_after  = dict(name='section', attrs={'class':'chapter'})

    cover_url = 'http://orm-other.s3.amazonaws.com/pythonckbksplash/pythonckbk_cover.jpg'

    url_prefix = 'http://chimera.labs.oreilly.com/books/1230000000393/'
    # no_stylesheets = True
    no_stylesheets = False
    keep_only_tags = [{ 'class': 'chapter' }]

    def get_title(self, link):
        return link.contents[0].strip()

    def parse_index(self):
        soup = self.index_to_soup(self.url_prefix + 'index.html')

        div = soup.find('div', { 'class': 'toc' })

        articles = []
        for link in div.findAll('a'):
            if '#' in link['href']:
                continue

            if not 'ch' in link['href']:
                continue

            til = self.get_title(link)
            url = self.url_prefix + link['href']
            a = { 'title': til, 'url': url }

            articles.append(a)

        ans = [('Python Cookbook', articles)]

        return ans
