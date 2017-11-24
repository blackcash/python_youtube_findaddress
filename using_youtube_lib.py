from pytube import YouTube
youtube_adr = input("please input youtube address : ")
yt_data = YouTube(youtube_adr)
sls = yt_data.streams.filter(subtype='mp4').all()
for index in range(0,len(sls)):
    print (index, sls[index] , type(sls[index]))    
while(1):
    try:
        item = input("Enter a number: ")    
        iitem = int(item)
        break
    except:
        print ("please input number!!")

sls[iitem].download()    
print ("finish!!")