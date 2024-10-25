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
        "纬来体育,https://hls.yjjcfw.com/live/vl.m3u8?hwSecret=8b6d7dbcec85c678564613c8e13763e54b28361ef3560dd3c872267ef4237c64&hwTime=67286CF8",
        "纬来体育,https://v4-5d0c7b68cc16e296da25095c872bee1f.livehwc3.cn/hls.yjjcfw.com/live/vl.m3u8?hwTime=67286CF8&user_session_id=2a84eb39379ec398b4010984d656193f&hwSecret=8b6d7dbcec85c678564613c8e13763e54b28361ef3560dd3c872267ef4237c64&edge_slice=true&sub_m3u8=true",
        "纬来体育,http://hls.szsummer.cn/live/446035/playlist.m3u8?k=32f9ec7c13e4b390289143a8e1b2a898&t=1840341130",
        "纬来体育,http://cloud.yumixiu768.com/tmp/123.m3u8",
        "东森超视,rtmp://f13h.mine.nu/sat/tv331",
        "非凡新闻,rtmp://f13h.mine.nu/sat/tv581",
        "华视,rtmp://f13h.mine.nu/sat/tv111",
        "民视,rtmp://f13h.mine.nu/sat/tv051",
        "台视,rtmp://f13h.mine.nu/sat/tv071",
        "中视,rtmp://f13h.mine.nu/sat/tv091",
        "纬来育乐,rtmp://f13h.mine.nu/sat/tv701",
        "纬来体育,rtmp://f13h.mine.nu/sat/tv721",
        "纬来日本,rtmp://f13h.mine.nu/sat/tv771",
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
