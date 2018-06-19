from scrapy import cmdline
cmdline.execute("scrapy crawl quotes -o quotes.json".split())
#cmdline.execute("scrapy crawl ads".split())