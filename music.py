from gmusicapi import Mobileclient
import sys
import datetime

#Grab username and password from arguments
if len(sys.argv) != 3:
	sys.exit("Enter a email and password as arguments [username]@[email] [password]")


username = sys.argv[1]
password = sys.argv[2]

#Shouldn't this be in a try? oh well
api = Mobileclient()
api.login(username, password, Mobileclient.FROM_MAC_ADDRESS)

# library = api.get_all_songs()
# tracks = [track['id'] for track in library]
# print(library[0])
# sys.exit()




#Get this week's dankest music from X source 
#TODO: Pull down popular tunes from a source
#As a placeholder, we will use Smash Mouth's "All Star"
dankTunes = ['All Star', 'Do I Wanna Know']

#Search and Create Playlist
songsToAdd = []
for tune in dankTunes:
	song = api.search(tune)
	id = song.get('song_hits')[0].get('track').get('storeId')
	songsToAdd.append(id)

#If any songs are found, add the found music to the playlist
if len(songsToAdd) > 0:
	playlist_id = api.create_playlist('Popular music on ' + str(datetime.date.today()))
	api.add_songs_to_playlist(playlist_id, songsToAdd)