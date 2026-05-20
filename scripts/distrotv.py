import urllib3
import json

playlist = ['#EXTM3U x-tvg-url="https://raw.githubusercontent.com/amazeyourself/m3u/refs/heads/main/epg/distrotv.xml.gz"']

resp = urllib3.request(
    "GET",
    "https://tv.jsrdn.com/tv_v5/getfeed.php?type=live")

jsonresp = resp.json()

stringdata = json.dumps(jsonresp['shows'], indent=4)
channel_data = json.loads(stringdata)
ids = channel_data.keys()
names = []
logos = []
epgids = []

for i in ids:
    name = channel_data[i]['title']
    logo = channel_data[i]['img_logo']
    url = channel_data[i]['seasons'][0]['episodes'][0]['content']['url']
    epg = channel_data[i]['seasons'][0]['episodes'][0]['id']
    names.append(name)
    logos.append(logo)
    epgids.append(str(epg))
    playlist.append(f'''#EXTINF:-1 tvg-id="{epg}" tvg-name="{name}" tvg-logo="{logo}",{name}
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0
#KODIPROP:inputstream=inputstream.adaptive
#KODIPROP:inputstream.adaptive.manifest_headers="User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0"
#KODIPROP:mimetype=application/dash+xml''')
    playlist.append(url)

with open('distro.m3u', 'w', newline='') as f:
    for lines in playlist:
        f.write(f'{lines}\n')

f.close()
