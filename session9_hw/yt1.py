from __future__ import unicode_literals
import youtube_dl

list_video_download = ['https://www.youtube.com/watch?v=Wv2rLZmbPMA', 'https://www.youtube.com/watch?v=GIDoQsQyS0s','https://www.youtube.com/watch?v=n6BwAWiHcSg&t=182s']
list_info = []
# list_video_download.append('https://www.youtube.com/watch?v=n6BwAWiHcSg&t=182s')
for link  in list_video_download:
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        r = ydl.extract_info(link,download = False)
        list_info.append(r)
print(list_info)
# with open('baitap.txt', 'a') as out:    
#     out.write('i love coding more than anything else' + '\n')
import json
with open('data.json', 'w') as outfile:
    json.dump(list_info, outfile)
    