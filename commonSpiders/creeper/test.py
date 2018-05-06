import unittest

from commonSpiders.creeper.crawlermanagers.custom_crawlerprocess import CustomCrawlerProcess
from commonSpiders.net.extend_context import ContextExtend


class MyTestCase(unittest.TestCase):

    def test_crawler_process(self):
        aa = CustomCrawlerProcess()
        print(1)


    def test_extend(self):
        extend = ContextExtend(key='1a', obj=None)
        print(1)


if __name__ == '__main__':
    unittest.main()
