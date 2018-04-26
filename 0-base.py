#!/usr/bin/env python
# vim:fileencoding=utf-8
from __future__ import unicode_literals, division, absolute_import, print_function
from calibre.web.feeds.news import BasicNewsRecipe


class book(BasicNewsRecipe):
    '''自定义的Recipe都继承自Calibre提供的基类BasicNewsRecipe，必须实现parse_index()方法
    '''
    # 电子书名称
    title = u'网游之近战法师'
    __author__ = u'蝴蝶蓝'
    description = u'一个超级武者,在玩网游时误选了法师,习惯以暴制暴,以力降力的他,只能将错就错,摇身一变,成为一个近战暴力法师,当力量与法术完美结合时,一条新的游戏之路,被他打开了! 火球术？闪电链？寒霜冰镜……等等，我是来练功夫的，法术关我什么事？我是法师？哦，对，我是法师。不过……你真的坚信我是法师？好吧，看刀！看剑！看拳！看暗器！什么？你又说我不是法师？如果你不相信，我证明给你看'
    timefmt = '[%Y-%m-%d]'
    # 最大章节数
    max_articles_per_feed = 1000
    # 设置每隔1s下载一个章节，默认值为0，当网络不好时，可以把这个值调大点
    delay = 0
    no_stylesheets = True
    # 抓取每一个页面中保留的tag  [ dict(name='div', attrs={'class':'advert'}), dict(name='div', attrs={'class':'advert'}) ]
    keep_only_tags = [{ 'id': 'content' }]
    # 页面中删除的Tag
    # remove_tags=[{'class':'x-wiki-info'}]
    # 指定Tag之后的元素都被删除
    # remove_tags_after=[{'class':'x-wiki-content'}]

    def get_title(self, link):
        return link.contents[0].strip()

    url_prefix = 'http://www.xxbiquge.com'
    def parse_index(self):
        # index_to_soup()由BasicNewsRecipe实现，使用Beautifulsoup抓取一个网址，并获得这个网页内容的soup对象
        soup = self.index_to_soup('http://www.xxbiquge.com/3_3253/')
        # 整块目录
        div = soup.find('dl')
        # 找到每一个章节的标题和对应的URL，Calibre会下载每一个URL的html，使用上面的类属性进行解析
        articles = []
        for link in div.findAll('a'):
            a = { 'title': self.get_title(link), 'url': self.url_prefix + link['href'] }
            articles.append(a)
        # 返回一个列表，这个列表中是多个元组，每个元组是书的一卷('卷名称', articles)，每一卷中又有多个章节articles
        return [ ('网游之近战法师', articles) ]
