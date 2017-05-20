#!/usr/bin/env python3
######################

import getData as gd
import requests
import timeit

#setup postgresql test
#gd.createDB()
#gd.createSongsTable()
#gd.createArtistsTable()
#gd.createAlbumsTable()

#getSongs test
access_header = gd.getAccessHeader()
start_time = timeit.default_timer()

featuredPlaylists = requests.get("https://api.spotify.com/v1/browse/featured-playlists", headers=access_header).json()["playlists"]["items"]
allFeaturedPlaylistData = {}
for i in featuredPlaylists:
	tracks = requests.get(i["href"] + "/tracks", headers=access_header).json()["items"]
	tracksList = []
	for j in tracks:
		tracksList.append(j["track"]["id"])
	allFeaturedPlaylistData[i["id"]] = gd.getSongs(tracksList)
elapsed = timeit.default_timer() - start_time
print("Duration: " + str(elapsed))
count = 0
for i in allFeaturedPlaylistData:
	for j in i:
		count += 1
print("Loaded all data for " + str(count) + " songs")