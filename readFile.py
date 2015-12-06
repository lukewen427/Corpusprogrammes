__author__ = 'zhenyuwen'
import re
import glob
from os.path import basename

path = '/Users/zhenyuwen/Desktop/Twitter data_UK_.txt/*txt'
# path = '/Users/zhenyuwen/Desktop/new/*txt'
towrite='/Users/zhenyuwen/Desktop/tag/'
files=glob.glob(path)

#file = open('/Users/zhenyuwen/Downloads/Harvard.txt', 'r')
#print file.readline()

def setcontent(content):
    added="<content>"+" "+content+" "+"</content>";
    return added

def setusername(username):
    added="<username>"+" "+username+" "+"</username>";
    return added

def setdate(date):
    added="<date>"+" "+date+" "+"</date>";
    return added

def setretweets(retweets):
    added="<retweets>"+" "+retweets+" "+"</retweets>";
    return added

def setlikes(likes):
    added="<likes>"+" "+likes+" "+"</likes>";
    return added

def setreply(reply):
    added="<reply>"+" "+reply+" "+"</reply>";
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

def setView(content,tag):
    added="<"+tag+">"+" "+content+" "+"</"+tag+">";
    return added


for thepath in files:
    tweet_list=[];
    tweet=list();
    index=0;
    stopadd=False;
    nextStep=False;
    # with open("/Users/zhenyuwen/Downloads/Harvard.txt") as file:
    with open(thepath.title()) as file:
        for line in file:
          newline= line.replace('\t',"");
          newline1=newline.replace('\r\n',"")
          l=newline1.split(" ")
          match=re.search('\d[\.]',l[0])
          if(match):
              # print l[0]
              stopadd=False;
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
              if (stopadd==False):
                  if(l[0] in ("Reply")):
                      stopadd=True;
                  tweet.append(list(l));
        tweet_list.append(tweet);
        # print tweet_list;
        file.close();
        theWhole="";
        for i in range(tweet_list.__len__()):
          Ntweet=tweet_list[i];
          addtag="";
          # print Ntweet;
          # print len(Ntweet);
          content="";
          contentComplete=False;
          addusername=False;
          for a in range(len(Ntweet)):
              line0=Ntweet[a];
              # print list(line0);
              for i in range(line0.__len__()):
                  ismatch=re.search('\?[\@]',line0[i]);
                  if(ismatch):
                      break;
              # print ismatch;
              # print line0;
              if(ismatch and addusername==False):
                  # print list(line0);
                  count=0;
                  for count in range(line0.__len__()):
                      match5=re.search('\@',line0[count]);
                      if(match5):
                          break
                  username="";
                  e=0
                  if(addtag==""):
                      for e in range(1,count+1):
                        username+=line0[e];
                  else:
                      for e in range(count+1):
                        username+=line0[e];
                  date="";
                  for i in range(e+1,line0.__len__()):
                      date+=line0[i];
                  # print date;
                  addtag=addtag+setusername(username)+" "+setdate(date);
                  addusername=True;
              if(addusername==False and ismatch==None):
                   line="";
                   for i in range(1,line0.__len__()):
                      line=line+" "+line0[i];
                   addtag=addtag+line;
                   # print addtag;
              if(addusername==True and ismatch==None):
                  # print addtag;
                  if(content==""):
                      for h in range(line0.__len__()):
                          match=re.search("#(\w+)",line0[h]);
                          if(match):
                              hashTag=line0[h];
                              content=content+" "+sethashtag(hashTag);
                          else:
                              content=content+" "+line0[h];
                              # print content;
                  else:
                      if(contentComplete==False):
                          for f in range(line0.__len__()):
                              # print line0;
                              match2=re.search("retweets",line0[f])
                              if((line0[f] in ("like","likes","View")) or match2):
                                  contentComplete=True;
                                  # print content;
                                  addtag=addtag+" "+setcontent(content);
                                  break;
                      if(contentComplete==False):
                          for f in range(line0.__len__()):
                            # content=content+" "+line0[f];
                            match=re.search("#(\w+)",line0[f]);
                            if(match):
                              hashTag=line0[f];
                              content=content+" "+sethashtag(hashTag);
                            else:
                              content=content+" "+line0[f];
                      if(contentComplete==True):
                          for x in range(line0.__len__()):
                              # match1=re.search("retweets"+'\d',line0[x])
                              # if(match1):
                              #     retweet=line0[x-1]+" "+"retweets";
                              #     addtag=addtag+" "+setretweets(retweet);
                              if(line0[x]=="retweet" or line0[x]=="retweets"):
                                  # print line0[x];
                                  retweet=line0[x-1]+" "+"retweets";
                                  addtag=addtag+" "+setretweets(retweet);
                              if(line0[x]=="likes" or line0[x]=="like"):
                                  # if(len(line0)==3):
                                      # number= re.findall('\d',line0[x-1]);
                                      # print number;
                                      # print line0;
                                      # like=str(number[0])+" "+"likes";
                                  like=line0[x-1]+" "+"likes";
                                  addtag=addtag+" "+ setlikes(like);
                              if(line0[x]=="Reply"):
                                  addtag=addtag+" "+setreply("Reply");
                          if(line0[0]=="View"):
                              tag=line0[1];
                              viewcon="";
                              for xx in range(line0.__len__()):
                                  viewcon=viewcon+" "+line0[xx];
                              # print setView(viewcon,tag);
                              addtag=addtag+" "+setView(viewcon,tag);
                          match3=re.search("retweets"+'\d',line0[x])
                          # if not (match3 or line0[0]=="View" or line0[x]=="Reply" or line0[x]=="likes" or line0[x]=="like" ):
                          #      for z in range(line0.__len__()):
                          #          addtag=addtag+" "+line0[z];
          # print addtag;
          theWhole=theWhole+addtag;
          theWhole=theWhole+'\n\n';
        filename=basename(thepath.title());
        print filename;
        newfile = open(towrite+filename, 'w+');
        newfile.write(theWhole);
        newfile.close();



    # data= file.readlines()
    # print data
    #tweet= data.split("More");
    #print tweet








