from secrets import refresh_token, base_64
from urllib import response
import requests
import json

class Refresh:

    def __init__(self):
        self.refresh_token = refresh_token
        self.base_64 = base_64

    def refresh(self):
        #curl -H "Authorization: Basic ZmM1NDVjMWFjNmZiNGZlYjkxZjQ1Yzg5Y2FiZDdlMzA6NWUyNzRlODg0MDE4NGU0OTkyOTJkNzM4Njg0ZDRhODM=" -d grant_type=authorization_code -d code=AQDSIywJ49-LEmRq469WJ0BuNX_uMj56oKXJ_b1SGqxgAw7LcvBe1ajdlFbT8RD1s_IMPOnNoSJHVIkSDDpF6wwHyGmIfo5Lo3PXEXohNPtTmYbctOEWDAZIx7ZQmWIP7kcm5NUAK7KpAj5mws7eqMA27Si6dEq1tNcztQCKMeWTPnVJ-x71NpnSm988sw5PFfrX8vVXNPSO-FwJlaOwrfohxpHjlVcnrY4HoP0 -d redirect_uri=https%3A%2F%2Fgithub.com%2F3joe7 https://accounts.spotify.com/api/token

        query = "https://accounts.spotify.com/api/token"

        response = requests.post(query, data={"grant_type": "refresh_token", "refresh_token": refresh_token}, headers={"Authorization": "Basic " + base_64})

        response_json = response.json()

        return response_json["access_token"]

a = Refresh()
a.refresh()