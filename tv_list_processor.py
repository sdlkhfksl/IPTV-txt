import requests
import re

# 从 GitHub 上获取文件内容
url = "https://raw.githubusercontent.com/lizongying/my-tv/main/app/src/main/java/com/lizongying/mytv/TVList.kt"
response = requests.get(url)
content = response.text

# Use a less brittle regex to find the content block from "央视" to "CGTN 纪录频道".
# This pattern is more robust against minor formatting changes in the source file.
pattern = re.compile(r'"央视" to listOf\(.*?CGTN 纪录频道.*?\),', re.DOTALL)
matches = pattern.findall(content)

# 检查是否有匹配项
if matches:
    matched_text = matches[0]

    # This pattern captures the channel name and the list of URLs.
    channel_pattern = re.compile(r'TV\(\s*0,\s*"[^"]+",\s*"([^"]+)",\s*listOf\(([^)]*)\)')
    result = []
    for channel_match in channel_pattern.finditer(matched_text):
        # 提取电视频道名称
        channel_name = channel_match.group(1)
        # 提取电视频道的所有URL
        # The list of URLs can be empty, so we handle that.
        url_block = channel_match.group(2)
        urls = re.findall(r'"(http[^"]+)"', url_block)
        # Construct the formatted string for each channel and its URLs.
        # Fixed the variable shadowing bug here: use a different variable name `channel_url` instead of `url`.
        result.extend(f"{channel_name},{channel_url}" for channel_url in urls)

    # 将结果写入 txt 文件
    with open("tv2.txt", "w", encoding='utf-8') as f:
        f.write("\n".join(result))

    print(f"处理完成，结果已保存到 tv2.txt，共 {len(result)} 行。")
else:
    print("未找到匹配项。")
