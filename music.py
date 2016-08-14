from gmusicapi import Mobileclient
import sys
import datetime
import billboard

#Grab username and password from arguments
if len(sys.argv) != 3:
	sys.exit("Enter a email and password as arguments [email] [password]")


username = sys.argv[1]
password = sys.argv[2]

#Shouldn't this be in a try? oh well
api = Mobileclient()
api.login(username, password, Mobileclient.FROM_MAC_ADDRESS)




dankTunes = []
#Get this week's dankest music from X source
chart = billboard.ChartData('billboard-200')
for song in chart:
	dankTunes.append(song.artist + ' ' + song.title)
#TODO: Pull down popular tunes from a source

#Search and Create Playlist
songsToAdd = []
for tune in dankTunes:
	song = api.search(tune)
	if len(song.get('song_hits')) > 0: 
		id = song.get('song_hits')[0].get('track').get('storeId')
		songsToAdd.append(id)

#If any songs are found, add the found music to the playlist
if len(songsToAdd) > 0:
	playlist_id = api.create_playlist('Popular music on ' + str(datetime.date.today()))
	api.add_songs_to_playlist(playlist_id, songsToAdd)