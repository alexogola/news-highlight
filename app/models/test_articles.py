import unittest
from articles import Articles

class TestArticles(unittest.TestCase):
    '''
    Test Class to test the behaviour of the articles class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('Lex','Trust the process','Fate leads the willing but drags the unwilling','https://philosophy.com','https://google.com/images','2019-02-01T13:31:03Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.author,'Lex')
        self.assertEquals(self.new_article.title,'Trust the process')
        self.assertEquals(self.new_article.description,'Fate leads the willing but drags the unwilling')
        self.assertEquals(self.new_article.url,'https://philosophy.com')
        self.assertEquals(self.new_article.urlToImage,'https://google.com/images')
        self.assertEquals(self.new_article.publishedAt,'2019-02-01T13:31:03Z')
