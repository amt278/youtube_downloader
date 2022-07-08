###################### after finish ################################
def finish():
    print('download finished\n')

############################# download vidoe #############################
from pytube import YouTube

link = 'https://www.youtube.com/watch?v=OlZoEMdM530&ab_channel=Codezilla'
video = YouTube(link)

for stream in video.streams:
    print(stream)

# for stream in video.streams.filter(progressive=False):
#     print(stream)

# print(video.streams.get_highest_resolution())

# print(video.streams.get_lowest_resolution())

# video.streams.get_lowest_resolution().download(output_path='/Users/Adham/Downloads', filename='video by py')
# video.register_on_complete_callback(finish())



################################# download playlist #########################################################
from pytube import Playlist

playlist_link = 'https://www.youtube.com/watch?v=cARGOrtiWt4&list=PLuXY3ddo_8nwyBVa1I3xHXYgpQHJ1Z0wn'
playlist = Playlist(playlist_link)

# for video in playlist.videos:
#     video.streams.get_lowest_resolution().download(output_path='/Users/Adham/Downloads')
#     video.register_on_complete_callback(finish())
