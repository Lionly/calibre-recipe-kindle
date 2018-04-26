from calibre.web.feeds.news import BasicNewsRecipe
import os
import time


class AdvancedUserRecipe1277129332(BasicNewsRecipe):
    title = u'人民日报'
    oldest_article = 2
    max_articles_per_feed = 100
    __author__ = 'zzh'

    pubisher = 'people.com.cn'
    description = 'People Daily Newspaper'
    language = 'zh'
    category = 'News, China'
    remove_javascript = True
    use_embedded_content = False
    no_stylesheets = True
    encoding = 'GB2312'
    language = 'zh'
    conversion_options = {'linearize_tables': True}
    masthead_url = 'http://www.people.com.cn/img/2010wb/images/logo.gif'

    feeds = [
        (u'时政', u'http://www.people.com.cn/rss/politics.xml'),
        (u'国际', u'http://www.people.com.cn/rss/world.xml'),
        (u'经济', u'http://www.people.com.cn/rss/finance.xml'),
        (u'体育', u'http://www.people.com.cn/rss/sports.xml'),
        (u'教育', u'http://www.people.com.cn/rss/edu.xml'),
        (u'文化', u'http://www.people.com.cn/rss/culture.xml'),
        (u'社会', u'http://www.people.com.cn/rss/society.xml'),
        (u'传媒', u'http://www.people.com.cn/rss/media.xml'),
        (u'娱乐', u'http://www.people.com.cn/rss/ent.xml'),
        # (u'汽车', u'http://www.people.com.cn/rss/auto.xml'),
        (u'海峡两岸', u'http://www.people.com.cn/rss/haixia.xml'),
        # (u'IT频道', u'http://www.people.com.cn/rss/it.xml'),
        # (u'环保', u'http://www.people.com.cn/rss/env.xml'),
        # (u'科技', u'http://www.people.com.cn/rss/scitech.xml'),
        # (u'新农村', u'http://www.people.com.cn/rss/nc.xml'),
        # (u'天气频道', u'http://www.people.com.cn/rss/weather.xml'),
        (u'生活提示', u'http://www.people.com.cn/rss/life.xml'),
        (u'卫生', u'http://www.people.com.cn/rss/medicine.xml'),
        # (u'人口', u'http://www.people.com.cn/rss/npmpc.xml'),
        # (u'读书', u'http://www.people.com.cn/rss/booker.xml'),
        # (u'食品', u'http://www.people.com.cn/rss/shipin.xml'),
        # (u'女性新闻', u'http://www.people.com.cn/rss/women.xml'),
        # (u'游戏', u'http://www.people.com.cn/rss/game.xml'),
        # (u'家电频道', u'http://www.people.com.cn/rss/homea.xml'),
        # (u'房产', u'http://www.people.com.cn/rss/house.xml'),
        # (u'健康', u'http://www.people.com.cn/rss/health.xml'),
        # (u'科学发展观', u'http://www.people.com.cn/rss/kxfz.xml'),
        # (u'知识产权', u'http://www.people.com.cn/rss/ip.xml'),
        # (u'高层动态', u'http://www.people.com.cn/rss/64094.xml'),
        # (u'党的各项工作', u'http://www.people.com.cn/rss/64107.xml'),
        # (u'党建聚焦', u'http://www.people.com.cn/rss/64101.xml'),
        # (u'机关党建', u'http://www.people.com.cn/rss/117094.xml'),
        # (u'事业党建', u'http://www.people.com.cn/rss/117095.xml'),
        # (u'国企党建', u'http://www.people.com.cn/rss/117096.xml'),
        # (u'非公党建', u'http://www.people.com.cn/rss/117097.xml'),
        # (u'社区党建', u'http://www.people.com.cn/rss/117098.xml'),
        # (u'高校党建', u'http://www.people.com.cn/rss/117099.xml'),
        # (u'农村党建', u'http://www.people.com.cn/rss/117100.xml'),
        # (u'军队党建', u'http://www.people.com.cn/rss/117101.xml'),
        # (u'时代先锋', u'http://www.people.com.cn/rss/78693.xml'),
        # (u'网友声音', u'http://www.people.com.cn/rss/64103.xml'),
        # (u'反腐倡廉', u'http://www.people.com.cn/rss/64371.xml'),
        # (u'综合报道', u'http://www.people.com.cn/rss/64387.xml'),
        # (u'中国人大新闻', u'http://www.people.com.cn/rss/14576.xml'),
        # (u'中国政协新闻', u'http://www.people.com.cn/rss/34948.xml'),
    ]
    keep_only_tags = [
        dict(name='div', attrs={'class': 'text_c'}),
    ]
    remove_tags = [
        dict(name='div', attrs={'class': 'tools'}),
    ]
    remove_tags_after = [
        dict(name='div', attrs={'id': 'p_content'}),
    ]

    def append_page(self, soup, appendtag, position):
        pager = soup.find('img', attrs={'src': '/img/next_b.gif'})
        if pager:
            nexturl = self.INDEX + pager.a['href']
            soup2 = self.index_to_soup(nexturl)
            texttag = soup2.find('div', attrs={'class': 'text_c'})
            # for it in texttag.findAll(style=True):
            #   del it['style']
            newpos = len(texttag.contents)
            self.append_page(soup2, texttag, newpos)
            texttag.extract()
            appendtag.insert(position, texttag)

    def skip_ad_pages(self, soup):
        if ('advertisement' in soup.find('title').string.lower()):
            href = soup.find('a').get('href')
            return self.browser.open(href).read().decode('GB2312', 'ignore')
        else:
            return None

    def preprocess_html(self, soup):
        mtag = '<meta http-equiv="content-type" content="text/html;charset=GB2312" />\n<meta http-equiv="content-language" content="GB2312" />'
        soup.head.insert(0, mtag)
        for item in soup.findAll(style=True):
            del item['form']
        self.append_page(soup, soup.body, 3)
        return soup

    def get_cover_url(self):
        cover = None
        os.environ['TZ'] = 'Asia/Shanghai'
        time.tzset()
        year = time.strftime('%Y')
        month = time.strftime('%m')
        day = time.strftime('%d')
        cover = 'http://paper.people.com.cn/rmrb/page/' + year + '-' + \
            month + '/' + day + '/01/RMRB' + year + month + day + 'B001_b.jpg'
        br = BasicNewsRecipe.get_browser(self)
        try:
            br.open(cover)
        except:
            self.log("\nCover unavailable: " + cover)
            cover = None
        return cover
