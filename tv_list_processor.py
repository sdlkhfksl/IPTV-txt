import requests
import re

# 从 GitHub 上获取文件内容
url = "https://raw.githubusercontent.com/lizongying/my-tv/main/app/src/main/java/com/lizongying/mytv/TVList.kt"
response = requests.get(url)
content = response.text

# 提取包含央视频道至CGTN纪录频道的完整段落
pattern = re.compile(r'央视频道.*?CGTN 纪录频道,.*?ProgramType\.Y_PROTO.*?;', re.DOTALL)
matches = pattern.findall(content)

# 检查是否有匹配项
if matches:
    matched_text = matches[0]

    # 提取电视频道信息
    channel_pattern = re.compile(r'TV\(\s*0,\s*"([^"]+)",\s*"([^"]+)",\s*listOf\(([^)]+)\)')
    result = []
    for channel_match in channel_pattern.finditer(matched_text):
        # 提取电视频道名称
        channel_name = channel_match.group(2)
        # 提取电视频道的所有URL
        urls = re.findall(r'"(http[^"]+)"', channel_match.group(3))
        # 构造每个电视频道对应所有链接的格式化字符串
        result.extend(f"{channel_name},{url}" for url in urls)

    # 将结果写入 txt 文件
    with open("tv2.txt", "w", encoding='utf-8') as f:
        f.write("\n".join(result))

    print(f"处理完成，结果已保存到 tv2.txt，共 {len(result)} 行。")
else:
    print("未找到匹配项。")
