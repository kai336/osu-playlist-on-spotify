# this program retrives played songs from osu!

import requests
import os
from get_token import get_accses_token

osu_user_id = os.environ['OSU_USER_ID']
osu_client_id = os.environ['OSU_CLIENT_ID']
osu_client_secret = os.environ['OSU_CLIENT_SECRET']
get_accses_token()
osu_access_token = os.environ['OSU_ACCESS_TOKEN']

beatmaps = set()
limit = 100
offset = 0
# search your all played songs by using most played + offset
prev = None
while True:
    print(f"offset={offset}")
    osu_url = f"https://osu.ppy.sh/api/v2/users/{osu_user_id}/beatmapsets/most_played?limit={limit}&offset={offset}"
    headers = {
        'Authorization': f'Bearer {osu_access_token}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    # get the json data of most played beatmaps
    osu_response = requests.get(osu_url, headers=headers)
    print(osu_response)
    most_played = osu_response.json()
    # if reach the last page, then break
    if prev == most_played:
        break
    prev = most_played
    # add info of title and artist
    for play in most_played:
        beatmap = play['beatmapset'] # get the beatmap
        title = beatmap['title']
        artist = beatmap['artist']
        beatmaps.add((title, artist))
    offset += limit

print(f"number of songs: {len(beatmaps)}")
print(beatmaps)