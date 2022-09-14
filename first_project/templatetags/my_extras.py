from django import template

register = template.Library()
'''自定义filter中的函数'''
# register.filter('cut', cut) 这种方法定义也可以
@register.filter(name='cut')  # 通过修饰器定义
def cut(value, arg):
    """
    将value中的arg全部去掉
    """
    return value.replace(arg, '')


