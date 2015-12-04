#练习

#请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：

# -*- coding: utf-8 -*-
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        if isinstance(value, int) or isinstance(value, float):
            self._width=value
        else:
            raise ValueError('width must be a number!')
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        if isinstance(value, int) or isinstance(value, float):
            self._height=value
        else:
            raise ValueError('height must be a number!')
    @property
    def resolution(self):
        return self._width*self._height

# test:
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution