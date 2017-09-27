#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
from functools import reduce
L=[1,2,3,4]
def prod(x,y):
	return x*y
x=reduce(prod,L)
print("num is",x)
'''
'''
def is_palindrome(n):
    return str(n)==str(n)[::-1]   #字符串翻转
output = filter(is_palindrome, range(1, 1000))
print(list(output))
'''
'''
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]

def by_score(t):
    return t[1]

L2 = sorted(L, key=by_name)
#L2 = sorted(L, key=by_score, reverse=True)

print(L2)
'''
'''
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width=value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height=value
    @property
    def resolution(self):
        return self._width*self._height
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
'''
'''
import os
print(os.name)
print("current path:",os.path.abspath('.'))
#print(os.environ)
def findfile(path,filename):
    for x in os.listdir(path):
        if os.path.isfile(os.path.join(path,x)) and filename in x:
            print(os.path.abspath(os.path.join(path,x)))
        elif os.path.isdir(os.path.join(path, x)):
            findfile(os.path.join(path,x),filename)
findfile('.',"wrf")
'''
'''
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
'''
'''
import time, threading

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n=n+1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(10)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='childThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
'''
'''
import threading, multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()
'''
'''
from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
'''
'''
def consumer():
    r = ''
    while True:
        n = yield r
        print("value:",n)
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)
'''
'''
def gen():
    value=0
    while True:
        receive=yield value
        if receive=='e':
            break
        value = 'got: %s' % receive

g=gen()
print(g.send(None))
print(g.send('aaa'))
g.close()
print(g.send(3))

#print(g.send('e'))
'''
def write():
    while True:
        recv=yield
        print('>>>>>',recv)
def wrapper(core):
    yield from core

w = write()
wrap = wrapper(w)
wrap.send(None)  # "prime" the coroutine
for i in [0, 1, 2, 'spam', 4]:
    #if i == 'spam':
       # wrap.throw(SpamException)
    #else:
        print('produce')
        wrap.send(i)