#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Example 1:组成几个三位数
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i!=j and i!=k and j!=k:
#                 print i,j,k


#Example 2:发放奖金
# i = int(raw_input('净利润：'))
# attr = [1000000,600000,400000,200000,100000,0]
# rat  = [0.01,0.015,0.03,0.05,0.075,0.1]
# bonus = 0
# for idx in range(0,6):
#     if i>attr[idx]:
#         bonus += (i-attr[idx])*rat[idx]
#         print bonus
#         i = attr[idx]
# print bonus


#Example 3:加数之后为完全平方数
# for i in range(1,85):
#     if 168%i==0:
#         j = 168/i
#         if i>j and (i+j)%2==0 and (i-j)%2==0:
#             n = (i-j)/2
#             x = n*n - 100
#             print x


#Example 4:输出某一天是一年的第几天
# import sys
# year = int(raw_input('年:\n'))
# month = int(raw_input('月:\n'))
# day = int(raw_input('日:\n'))

# months = (0,31,59,90,120,151,181,212,243,273,304,334)
# if 0<month<=12:
#     sum = months[month-1]
# else: 
#     print 'data error'
#     sys.exit(0)

# sum += day

# if ((year%400==0)or((year%4==0)and(year%100!=0))) and month>2:
#     sum += 1

# print 'it is the %dth day.' % sum 


#Example 5:排序
# def comp(x,y):
#     if x>y:
#         return -1
#     elif x<y:
#         return 1
#     else:
#         return 0

# l = []
# for i in range(3):
#     x = int(raw_input('integer:\n'))
#     l.append(x)
# l.sort(comp)
# print l


#Example 6:斐波那契数列
# def fib(n):
#     a,b = 1,1
#     for i  in range(n-1):
#         a,b = b,a+b
#     return a

# print fib(10)


#Example 7:复制表
# a = [1,2,3]
# b = a[:]
# print b


#Example 8:打印九九乘法表
# for i in range(1,10):
#     print
#     for j in range(1,i+1):
#         print '%d*%d=%d' % (j,i,j*i),


#Example 9:暂停1s输出
# import time 
# myD = {1:'a',2:'b'}
# for key,value in dict.items(myD):
#     print key,value
#     time.sleep(1)


#Example 10:暂停1s输出并格式化时间
# import time
# print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
# time.sleep(1)
# print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))


#Example 11:兔子生兔子，和斐波那契数列类似，不过需要打印
# f1,f2 = 1,1
# for i in range(1,22):
#     print '%12ld %12ld' % (f1,f2)
#     if i%3==0:
#         print ''
#     f1 = f1+f2
#     f2 = f1+f2


#Example 12:判断101-200之间的素数
# from math import sqrt
# h = 0
# leap = 1
# for m in range(101,201):
#     k = int(sqrt(m))
#     for i in range(2,k+1):
#         if m%i==0:
#             leap = 0
#             break
#     if leap ==1:
#         h += 1
#         print m
#     leap = 1
# print 'total is %d' % h


#Example 13:水仙花数
# for n in range(100,1000):
#     i = n/100
#     j = n%100/10
#     k = n%10
#     if n == i**3 + j**3 + k**3:
#         print n


#Example 14:将一个正整数分解质因数
# n = int(raw_input('请输入一个正整数'))
# if not isinstance(n,int) or n<=0:
#     exit(0)
# n1 = n
# l = []
# while n>1:
#     for i in range(2,n+1):
#         if n%i==0:
#             n /= i
#             l.append(str(i))
#             break
# print '%d = ' %n1 + ' * '.join(l)


#Example 15:成绩ABC
# score = int(raw_input('请输入成绩:\n'))
# if 90<=score<=100:
#     print 'A'
# elif 80<=score<90:
#     print 'B'
# elif 0<=score<80:
#     print 'C'
# else:
#     print'请输入正确的成绩'
#     exit(0)


#Example 16:输出指定格式的日期


#Example 17:统计不同字符个数
# import string 
# s = raw_input('请输入一个字符串:\n')
# i = 0
# digit = 0
# while i<len(s):
#     c = s[i]
#     i += 1
#     if c.isdigit():
#         digit += 1
# print digit


#Example 18:计算一个数的重复和
# Tn = 0
# Sn = []
# a = int(raw_input("请输入要求和的数:\n"))
# n = int(raw_input("请输入重复的次数:\n"))
# for i in range(n):
#     Tn += a
#     a = a*10
#     Sn.append(Tn)
#     print Tn
# print reduce(lambda x,y:x+y,Sn)


#Example 19:计算1000以内的完数
# for i in range(2,1001):
#     s = i
#     n = 0
#     k = []
#     for j in range(1,i):
#         if i%j == 0:
#             n += 1
#             s -= j
#             k.append(j)
#     if s == 0:
#         print "\n%d" % i
#         for m in range(n):
#             print k[m],


#Example 20:计算小球反弹高度
# height = []
# tour = [] 
# tei = 10
# hei = 100.0
# for i in range(1,tei+1):
#     if i == 1:
#         tour.append(hei)
#     else:
#         tour.append(hei*2)
#     hei /= 2
#     height.append(hei)
# print "一共走了{0}米".format(sum(tour))
# print "第十次弹起了{0}米".format(height[-1])


#Example 21:猴子吃桃子
# x = 1
# y = 0
# for i in range(9,0,-1):
#     y = (x+1)*2
#     x = y
# print y


#Example 22:乒乓球比赛
# for i in range(ord('x'),ord('z')+1):
#     for j in range(ord('x'),ord('z')+1):
#         if i!=j:
#             for k in range(ord('x'),ord('z')+1):
#                 if (i!=j and j!=k and k!=i):
#                     if i!=ord('x') and k!=ord('x') and k!=ord('z'):
#                         print "a--%s\tb--%s\tc--%s\t" % (chr(i),chr(j),chr(k))


#Example 23:打印菱形


#Example 24:求数列前20项和
# a = 2.0
# b = 1.0
# s = 0.0
# for i in range(1,21):
#     s += a/b
#     t = a
#     a = a+b
#     b = t
# print s


#Example 25:累乘
# s = 0
# l = range(1,21)
# def op(x):
#     r = 1
#     for i in range(1,x+1):
#         r *= i
#     return r
# print sum(map(op,l))


#Exercise 1:文件读写
# import os
# fo = open("hello.py","r+")
# print fo.read()
# print fo.name
# os.chdir("/Users/imacbook/Desktop/")
# print os.getcwd()
# fo1 = open("hello1.c","r+")
# print fo1.read()


#Example 26:递归
# def fact(j):
#     sum = 1
#     if j==0:
#         sum = 1
#     else:
#         sum = j*fact(j-1)
#     return sum 
# print fact(5)


#Example 27:递归倒序打印字符串
# def func(s,l):
#     if l==0:
#         return 
#     print s[l-1]
#     func(s,l-1)

# func("abcde",5)


#Example 28:递归推算第五个人多少岁
# def func(p):
#     if p==1:
#         return 10
#     else:
#         return 2+func(p-1)

# print func(5)


#Example 29:求数字的位数并且逆序打印出他们(不超过五位数)
# def func(x):
#     a = x/10000
#     b = x%10000/1000
#     c = x%1000/100
#     d = x%100/10
#     e = x%10
#     if a!=0:
#         print "5位数",e,d,c,b,a
#     elif b!=0:
#         print "4位数",e,d,c,b
#     elif c!=0:
#         print "3位数",e,d,c
#     elif d!=0:
#         print "2位数",e,d
#     else:
#         print "1位数",e
# func(12345)


#Exmaple 30:判断回文数
# a = int(raw_input('请输入一个数字:\n'))
# x = str(a)
# flag = True
# for i in range(len(x)):
#     if x[i] != x[-i-1]:
#         flag = False
#         break
# if flag:
#     print "yes"
# else:
#     print "no"


#打开应用程序
import os 
os.system("/Applications/QQMusic.app/Contents/MacOS/QQMusic ")
