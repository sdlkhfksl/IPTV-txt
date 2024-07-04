import requests

# 获取链接的文本内容
url = "https://raw.githubusercontent.com/fanmingming/live/main/tv/m3u/ipv6.m3u"
response = requests.get(url)
m3u_content = response.text

# 移除第一行
m3u_content = m3u_content.split('\n', 1)[1]

# 初始化变量
group_name = ""
channel_name = ""
channel_link = ""
output_dict = {}

# 处理每两行为一组的情况
for line in m3u_content.split('\n'):
    if line.startswith("#EXTINF"):
        # 获取 group-title 的值
        group_name = line.split('group-title="')[1].split('"')[0]
        
        # 获取频道名
        channel_name = line.split(',')[-1]
    elif line.startswith("http"):
        # 获取频道链接
        channel_link = line
        # 合并频道名和频道链接
        combined_link = f"{channel_name},{channel_link}"

        # 将组名作为键，合并链接作为值存储在字典中
        if group_name not in output_dict:
            output_dict[group_name] = []
        output_dict[group_name].append(combined_link)

# 在央视频道组下添加新的频道
if "央视频道" in output_dict:
    new_channels = [
        "纬来体育,http://hls.szsummer.cn/live/446035/playlist.m3u8?k=32f9ec7c13e4b390289143a8e1b2a898&t=1840341130",
        "纬来体育,http://cloud.yumixiu768.com/tmp/123.m3u8",
        "香港佛陀教育协会(大陆线路),http://js1.amtb.cn/liveedge/_definst_/livetv/playlist.m3u8",
        "香港佛陀教育协会(欧美线路),http://de1.amtb.de/liveedge/_definst_/livetv/playlist.m3u8",
        "净空老法师讲经直播台(台湾线路),https://tw1.amtb.de/liveedge/_definst_/livetv/playlist.m3u8",
        "净空老法师讲经直播台(大陆线路),https://tw3.amtb.de/liveedge/_definst_/livetv/playlist.m3u8",
        "净空老法师讲经直播台(香港线路),https://hk1.amtb.de/liveedge/_definst_/livetv/playlist.m3u8",
        "净空老法师讲经直播台(新马线路),https://sg1.amtb.de/liveedge/_definst_/livetv/playlist.m3u8",
        "净空老法师讲经(台湾线路),https://hk1.amtb.de/liveedge/_definst_/masterck/playlist.m3u8",
        "净空老法师讲经(大陆线路),https://tw3.amtb.de/liveedge/_definst_/masterck/playlist.m3u8",
        "净空老法师讲经(香港线路),https://hk2.amtb.de/liveedge/_definst_/masterck/playlist.m3u8",
        "净空老法师讲经(新马线路),https://sg1.amtb.de/liveedge/_definst_/masterck/playlist.m3u8",
        "悟道法师讲经(台湾线路),https://tw1.amtb.de/liveedge/_definst_/wdmaster/playlist.m3u8",
        "悟道法师讲经(大陆线路),https://tw3.amtb.de/liveedge/_definst_/wdmaster/playlist.m3u8",
        "悟道法师讲经(香港线路),https://hk2.amtb.de/liveedge/_definst_/wdmaster/playlist.m3u8",
        "悟道法师讲经(新马线路),https://sg1.amtb.de/liveedge/_definst_/wdmaster/playlist.m3u8",
        "多元文化(台湾线路),https://tw2.amtb.de/liveedge/_definst_/cult/playlist.m3u8",
        "多元文化(大陆线路),https://tw3.amtb.de/liveedge/_definst_/cult/playlist.m3u8",
        "多元文化(欧美线路),https://de1.amtb.de/liveedge/_definst_/cult/playlist.m3u8",
        "多元文化(香港线路),https://hk2.amtb.de/liveedge/_definst_/cult/playlist.m3u8",
        "多元文化(新马线路),https://sg1.amtb.de/liveedge/_definst_/cult/playlist.m3u8",
        "繫念法會(台湾线路),https://tw1.amtb.de/liveedge/_definst_/sanshi_720p/playlist.m3u8",
        "繫念法會(大陆线路),https://tw3.amtb.de/liveedge/_definst_/sanshi_720p/playlist.m3u8",
        "繫念法會(欧美线路),https://de1.amtb.de/liveedge/_definst_/sanshi_720p/playlist.m3u8",
        "繫念法會(香港线路),https://hk1.amtb.de/liveedge/_definst_/sanshi_720p/playlist.m3u8",
        "繫念法會(新马线路),https://sg1.amtb.de/liveedge/_definst_/sanshi_720p/playlist.m3u8",
        "网络念佛堂(台湾线路),https://tw1.amtb.de/liveedge/_definst_/amtb/playlist.m3u8",
        "网络念佛堂(大陆线路),https://tw3.amtb.de/liveedge/_definst_/amtb/playlist.m3u8",
        "网络念佛堂(欧美线路),https://de1.amtb.de/liveedge/_definst_/amtb/playlist.m3u8",
        "网络念佛堂(香港线路),https://hk2.amtb.de/liveedge/_definst_/amtb/playlist.m3u8",
        "网络念佛堂(新马线路),https://sg1.amtb.de/liveedge/_definst_/amtb/playlist.m3u8"
    ]

    # 将新频道添加到 ‘央视频道’ 中
    output_dict["央视频道"].extend(new_channels)
# 将结果写入 tv.txt 文件
with open("tv.txt", "w", encoding="utf-8") as output_file:
    # 遍历字典，写入结果文件
    for group_name, links in output_dict.items():
        output_file.write(f"{group_name},#genre#\n")
        for link in links:
            output_file.write(f"{link}\n")
