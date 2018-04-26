#!/usr/bin/python
# encoding: utf-8
from calibre.web.feeds.recipes import BasicNewsRecipe

class wooyun(BasicNewsRecipe):
    title = u'乌云知识库'
    __author__ = u'无关风月'
    description = u'''乌云知识库，最专业的安全知识分享平台。本电子书由无关风月整理网站 <http://drops.wooyun.org/> 内容而来。'''
    timefmt = '[%Y-%m-%d]'
    no_stylesheets = True
    INDEX = 'http://drops.wooyun.org/'
    # auto_cleanup = True                   # 如果没有手动分析文章结构，可以考虑开启该选项自动清理正文内容
    language = 'zh-CN'
    keep_only_tags = [{'class': ['post']}]  # 仅保留文章的post中的内容，其中为自己分析得到的正文范围
    max_articles_per_feed = 10000           # 默认最多文章数是100，可改为更大的数字以免下载不全

    def parse_index(self):
        # soup = self.index_to_soup(self.INDEX)
        # pages_info = soup.findALL(**{'class': 'pages'}).text.split()
        # print 'pages_info:', pages_info
        start_page = 1      # int(pages_info[1])
        end_page = 47       # int(pages_info[3])
        articles = [] 
        for p in range(start_page, end_page+1):     # 处理每一个目录页
            soup_page = self.index_to_soup(self.INDEX + 'page/' + str(p))
            soup_titles = soup_page.findAll(**{'class': 'entry-title'})     # 从目录页中提取正文标题和链接
            for soup_title in soup_titles:
                href = soup_title.a
                articles.append({'title': href['title'][18:], 'url': href['href']}) 
            # print 'page %d done' % p
        articles.reverse()                 # 文章倒序，让其按照时间从前到后排列
        res = [(u'乌云知识库', articles)]    # 返回tuple，分别是电子书名字和文章列表
        self.abort_recipe_processing('test')  # 用来中断电子书生成，调试用
        return res