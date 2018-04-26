#!/usr/bin/env python
# vim:fileencoding=utf-8

from calibre.web.feeds.recipes import BasicNewsRecipe

class mingchaonaxieshier_book(BasicNewsRecipe):
    '''自定义的Recipe都继承自Calibre提供的基类BasicNewsRecipe，必须实现parse_index()方法
    '''
    #电子书名称
    title          = '明朝那些事儿'
    __author__ = u"当年明月"
    description = '历史应该可以写得好看'

    # 封面 1、指定图片 2、设置标题，时间(显示在封面)
    cover_url = 'http://www.fox2008.cn/2mcnxsl/image/mcnxs01_d.jpg'
    timefmt = '[%Y-%m-%d]'
 
    # url_prefix = 'http://www.mingchaonaxieshier.com'

    language = 'zh-CN'
    max_articles_per_feed = 1
    simultaneous_downloads = 10
    # 设置每隔1s下载一个章节，默认值为0，当网络不好时，可以把这个值调大点
    # delay = 1 
    no_stylesheets = True
    remove_javascript = True
    #抓取每一个页面中保留的tag
    keep_only_tags = [{ 'class': 'content' }]
    #页面中删除的Tag
    # remove_tags=[{'id': 'comments'}, 'a']
    #指定Tag之后的元素都被删除
    remove_tags_after=[ dict(name='div', attrs={'style': ['margin:15px 0px 0px 0px; float:right']}) ]

    def get_title(self, link):
        return link.contents[0].strip()

    def parse_index(self):
        # index_to_soup()由BasicNewsRecipe实现，使用Beautifulsoup抓取一个网址，并获得这个网页内容的soup对象
        soup = self.index_to_soup('http://www.mingchaonaxieshier.com/')
        # 两层 1 一卷(部) 2 一章
        tables = soup.findAll('table')
        volumes = []
        for table in tables:
            # 每一卷的标题
            volume_name = self.get_title( table.find('a') )
            # 每一卷的文章
            articles = []
            # 找到每一个章节的标题和对应的URL，Calibre会下载每一个URL的html，使用上面的类属性进行解析
            for link in table.findAll('a'):
                # 每一章的标题
                til = self.get_title(link)
                # 每一章的 URL
                url = link['href']
                a = { 'title': til, 'url': url }
                # 向一卷里添加一章
                articles.append( a )
            volume = (volume_name, articles)
            # 添加一卷
            volumes.append( volume )
        # 返回一个列表，这个列表中是多个元组，每个元组是书的一卷('廖雪峰python教程', articles)，每一卷中又有多个章节articles
        return volumes