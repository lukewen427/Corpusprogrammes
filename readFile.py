__author__ = 'zhenyuwen'


#file = open('/Users/zhenyuwen/Downloads/Harvard.txt', 'r')
#print file.readline()

with open("/Users/zhenyuwen/Downloads/Harvard.txt") as file:
    # for line in file:
    #    print line
    data= file.readlines()
    print data
    #tweet= data.split("More");
    #print tweet