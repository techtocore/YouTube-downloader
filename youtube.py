import webbrowser
import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import webbrowser
from pytube import YouTube

x = input("Enter the search : ")

name = x

x = x.replace(' ','+')

t = PrettyTable(['No','Title'])

url = 'https://www.youtube.com/results?search_query=' + x

page = requests.get(url)

soup = BeautifulSoup(page.content,'html.parser')

y = soup.findAll('h3',class_='yt-lockup-title ')

n=1
for i in y:
     t.add_row([n,i.a['title']])
     n=n+1

print (t)
ch = int(input("Enter no to Download : "))

link = "https://www.youtube.com" + str(y[(int)(ch-1)].a['href'])
#webbrowser.open_new(link)

#print(link)

##################################

 
try:
    #object creation using YouTube which was imported in the beginning
    yt = YouTube(link)
except:
    print("Connection Error")
 

try:
    yt.streams.filter(subtype='mp4').first().download()
except:
    print("Aw, Snap! Something went wrong")
print('Download Completed!')



