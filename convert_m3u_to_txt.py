import re
import requests

def download_m3u_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to download M3U file. Status code: {response.status_code}")

def convert_m3u_to_txt(m3u_content):
    lines = m3u_content.split('\n')
    result = []

    current_group = None
    for line in lines:
        if line.startswith('#EXTINF:'):
            match_name = re.search(r'tvg-name="([^"]+)"', line)
            match_group = re.search(r'group-title="([^"]+)"', line)

            if match_name and match_group:
                tvg_name = match_name.group(1)
                group_title = match_group.group(1)

                if current_group != group_title:
                    if current_group is not None:
                        result.append(f'{current_group},#genre#')

                    current_group = group_title

                result.append(f'{tvg_name},{line.split(" ")[-1]}')
    
    if current_group is not None:
        result.append(f'{current_group},#genre#')

    return '\n'.join(result)

if __name__ == "__main__":
    m3u_url = "https://raw.githubusercontent.com/fanmingming/live/main/tv/m3u/ipv6.m3u"
    
    m3u_content = download_m3u_content(m3u_url)
    txt_content = convert_m3u_to_txt(m3u_content)

    with open('tv.txt', 'w') as f:
        f.write(txt_content)
