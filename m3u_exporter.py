import cloudscraper
import re

url = "https://tv.iill.top/m3u/Gather"
headers = {
    "User-Agent": "TiviMate/3.1.6 (Android 10; Build/XYZ)",
    "Accept": "application/x-mpegURL, application/vnd.apple.mpegurl, */*",
    "Referer": "https://tv.iill.top",
    "Connection": "keep-alive",
    "Range": "bytes=0-",
}

scraper = cloudscraper.create_scraper()
response = scraper.get(url, headers=headers)
m3u_content = response.text

# 修复后的正则表达式
pattern = r'#EXTINF:-1.*?(?:tvg-name="([^"]*)".*?)?group-title="([^"]+)".*?[\s\S]*?\n(https?://\S+)'
matches = re.findall(pattern, m3u_content)

filtered_channels = []

for match in matches:
    tvg_name, group_title, channel_url = match
    tvg_name = tvg_name.strip() if tvg_name else ""
  
    is_cctv = ('CCTV' in tvg_name) and (group_title == '•咪咕「TV」')
    is_nba = (group_title == '•咪咕「NBA」')
  
    if is_cctv or is_nba:
        filtered_channels.append({
            "tvg_name": tvg_name if tvg_name else group_title,
            "group_title": group_title,
            "url": channel_url
        })

# 生成M3U输出
output = '#EXTM3U x-tvg-url="https://epg.iill.top/epg" catchup="append" catchup-source="?playseek=${(b)yyyyMMddHHmmss}-${(e)yyyyMMddHHmmss}"\n'

for channel in filtered_channels:
    output += f'#EXTINF:-1 tvg-name="{channel["tvg_name"]}" group-title="{channel["group_title"]}", {channel["tvg_name"]}\n'
    output += f'{channel["url"]}\n'

# Append the new content to the output
additional_channels = [
    ("东森超视", "https://live.fanmingming.com/tv/东森超视.png", "rtmp://f13h.mine.nu/sat/tv331"),
    ("非凡新闻", "https://live.fanmingming.com/tv/非凡新闻.png", "rtmp://f13h.mine.nu/sat/tv581"),
    ("华视", "https://live.fanmingming.com/tv/华视.png", "rtmp://f13h.mine.nu/sat/tv111"),
    ("民视", "https://live.fanmingming.com/tv/民视.png", "rtmp://f13h.mine.nu/sat/tv051"),
    ("台视", "https://live.fanmingming.com/tv/台视.png", "rtmp://f13h.mine.nu/sat/tv071"),
    ("中视", "https://live.fanmingming.com/tv/中视.png", "rtmp://f13h.mine.nu/sat/tv091"),
    ("纬来育乐", "https://live.fanmingming.com/tv/纬来育乐.png", "rtmp://f13h.mine.nu/sat/tv701"),
    ("纬来体育", "https://live.fanmingming.com/tv/纬来体育.png", "rtmp://f13h.mine.nu/sat/tv721"),
    ("纬来日本", "https://live.fanmingming.com/tv/纬来日本.png", "rtmp://f13h.mine.nu/sat/tv771")
]

for channel in additional_channels:
    tvg_name, tvg_logo, url = channel
    output += f'#EXTINF:-1 tvg-name="{tvg_name}" tvg-logo="{tvg_logo}", {tvg_name}\n'
    output += f'{url}\n'

print(output)
