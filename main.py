import json
from urllib import response
#from urllib import response
#from winreg import QueryValueEx
import requests
from secrets import spotify_user_id, discover_weekly_id
from datetime import date
from refresh import Refresh

class SaveSongs:
    def __init__(self):
        self.user_id=spotify_user_id
        self.spotify_token= ""
        self.discover_weekly_id=discover_weekly_id
        self.tracks = ""
        self.new_playlist_id = ""

    def find_songs(self):

        print("Finding songs in discover weekly...")
        #Loop through playlist tracks and add them to a list
        
        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(discover_weekly_id)

        response = requests.get(query, headers={"Content-Type": "application/json", "Authorization": "Bearer {}".format(self.spotify_token)})

        response_json = response.json()
        print(response)

        for i in response_json["items"]:
            self.tracks += (i["track"]["uri"] + ",")
        self.tracks = self.tracks[:-1]

        self.add_to_playlist()

    def createplaylist(self):
        #Create a playlist
        print("Trying to create a playlist...")
        today = date.today()

        todayformatted = today.strftime("%d/%n/%Y")

        query = "https://api.spotify.com/v1/users/{}/playlists".format(spotify_user_id)

        request_body = json.dumps({"name": todayformatted + "discover weekly", "description": "Discover your weekly songs and enjoy Spotify", "public": True})

        response = requests.post(query, data=request_body, headers={"Content-Type": "application/json", "Authorization": "Bearer {}".format(self.spotify_token)})

        response_json = response.json()
        
        return response_json["id"]

    def add_to_playlist(self):
        #add all songs to new playlist

        print("Adding songs...")
        
        self.new_playlist_id = self.createplaylist()

        query = "https://api.spotify.com/v1/playlists/{}/tracks?uris={}".format(self.new_playlist_id,self.tracks)

        response = requests.post(query, headers={"Content-Type": "application/json", "Authorization": "Bearer {}".format(self.spotify_token)})

        print(response.json)

    def call_refresh(self):

        print("Refreshing Token...")

        refreshCaller = Refresh()

        self.spotify_token = refreshCaller.refresh()

        self.find_songs()

a = SaveSongs()
a.call_refresh()
