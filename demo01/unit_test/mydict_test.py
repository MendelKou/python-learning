import unittest
from mydict import Dict
class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a=1,b='abc')
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'abc')
        self.assertTrue(isinstance(d,dict))
    def test_key(self):
        d = Dict()
        d['name'] = 'Bob'
        self.assertEqual(d.name,'Bob')
    def test_attr(self):
        d = Dict()
        d.age = 23
        self.assertEqual(d.age,23)
        self.assertTrue('age' in d)
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['x1']
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.x2
    # 每一个测试方法之前调用
    def setUp(self):
        print('setUp...')
    # 每一个测试方法之后调用
    def tearDown(self):
        print('tearDown...')

if __name__ == '__main__':
    unittest.main()
