__author__ = 'zhenyuwen'
import re

#file = open('/Users/zhenyuwen/Downloads/Harvard.txt', 'r')
#print file.readline()

def setcontent(content):
    added="<content>"+content+"</content>";
    return added

def setusername(username):
    added="<username>"+username+"</username>";
    return added

def setdate(date):
    added="<date>"+date+"</date>";
    return added

def setretweets(retweets):
    added="<retweets>"+retweets+"retweets";
    return added

def setlikes(likes):
    added="<likes>"+likes+"</likes>";
    return added

def setreply(reply):
    added="<reply>"+reply+"</reply>";
    return added

def setsummary(summary):
    added="<summary>"+summary+ "</summary>";
    return added

def setconversation(conversation):
    added="<conversation>"+conversation+"</conversation>";
    return added

def setmedia(media):
    added ="<media>"+media+"</media>";
    return added

def sethashtag(hashtag):
    added="<hashtag>"+hashtag+"</hashtag>";
    return added

def setviewdetails(viewdetails):
    added="<viewdetails>"+viewdetails+"</viewdetails>";
    return added



tweet_list=[];
tweet=list();
index=0;
with open("/Users/zhenyuwen/Desktop/Twitter/WUTwitter/Harvard.txt") as file:
      for line in file:
          newline= line.replace('\t',"");
          newline1=newline.replace('\r\n',"")
       #    line.remove('\r\n');
          l=newline1.split(" ")
          if(l[0] in ("", "More","Retweet","Like")):
              print ""
          else:
              match=re.search('\d[\.]',l[0])
              if(match):
                  # print l[0]
                  if (tweet_list.__len__()<0):
                      tweet=list();
                      tweet.append(list(l));
                  else:
                      if(tweet.__len__()>0):
                          newlist=list(tweet);
                          tweet_list.append(newlist)
                      tweet=list();
                      tweet.append(list(l));
              else:
                  tweet.append(list(l));


      for i in range(tweet_list.__len__()):
          Ntweet=tweet_list[i];
          addtag="";
          # print Ntweet;
          # print len(Ntweet);
          content="";
          contentComplete=False;
          for a in range(len(Ntweet)):
              line0=Ntweet[a];
              if(a==0):
                  # print line0;
                  username=line0[1]+line0[2]+line0[3];
                  if(len(line0)==8):
                      date=str(line0[5])+str(line0[6])+str(line0[7]);
                      # print date;
                  else:
                      date=str(line0[5])+str(line0[6]);
                      # print date;
                  addtag=setusername(username)+" "+setdate(date);
              else:
                  if(content==""):
                      for h in range(line0.__len__()):
                          match=re.search("#(\w+)",line0[h]);
                          if(match):
                              # print "yes";
                              # print line0[h];
                              hashTag=line0[h];
                              content=content+" "+sethashtag(hashTag);
                          else:
                              content=content+" "+line0[h];
                              # print content;
                  else:
                      for f in range(line0.__len__()):
                          if(line0[f] in ("retweets"+'\b',"likes","View")):
                              contentComplete=True;
                              addtag=addtag+" "+setcontent(content);
                      if(contentComplete==False):
                          for f in range(line0.__len__()):
                            content=content+" "+line0[f];
      print addtag;


    # data= file.readlines()
    # print data
    #tweet= data.split("More");
    #print tweet








