# -*- coding: utf-8 -*-

'''
    编码转化
'''

def gbk2unicode(s):
    """
    gbk 编码转为为unicode编码
    :param s: 编码为gbk格式的bytes类型
    :return: unicode 的 str类型
    """
    return s.decode('gbk', 'ignore')

def utf82unicode(s):
    return s.decode('utf-8', 'ignore')

def gbk2utf8(s):
    return s.decode('gbk', 'ignore').encode('utf-8')

def utf82gbk(s):
    return s.decode('utf-8', 'ignore').encode('gbk')