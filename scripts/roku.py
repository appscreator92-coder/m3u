import requests
import os
import xml.etree.ElementTree as ET

playlist = [f'#EXTM3U x-tvg-url="https://i.mjh.nz/Roku/all.xml.gz"']

resp = requests.get('https://raw.githubusercontent.com/matthuisman/i.mjh.nz/refs/heads/master/Roku/all.xml')

root = ET.fromstring(resp.text)

for type_tag in root.findall('channel'):
    chnlid = type_tag.get('id')
    name = type_tag.find('display-name').text
    ico = type_tag.find('icon').get('src')
    lcn = type_tag.find('lcn').text
    playlist.append(f'#EXTINF:-1 tvg-id="{chnlid}" tvg-chno="{lcn}" tvg-name="{name}" tvg-logo="{ico}",{lcn} {name}')
    playlist.append(f'https://jmp2.uk/rok-{chnlid}.m3u8')

with open('./roku.m3u', 'w') as f:
    for line in playlist:
        f.write(f"{line}\n")

f.close()
