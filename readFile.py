__author__ = 'zhenyuwen'


#file = open('/Users/zhenyuwen/Downloads/Harvard.txt', 'r')
#print file.readline()

tweet_list=[];
tweet=[];
with open("/Users/zhenyuwen/Downloads/Harvard.txt") as file:
      for line in file:
          print line
          newline= line.replace('\t',"");
          newline1=newline.replace('\r\n',"")
       #    line.remove('\r\n');
          l=newline1.split(" ")
          print l
    # data= file.readlines()
    # print data
    #tweet= data.split("More");
    #print tweet