import requests

# Define the URLs
txt_url = 'https://raw.githubusercontent.com/sdlkhfksl/IPTV-txt/Files/tv2.txt'
m3u_url = 'https://raw.githubusercontent.com/sdlkhfksl/IPTV-txt/Files/tv2.m3u'

# Fetch content from the URLs using requests
txt_response = requests.get(txt_url)
m3u_response = requests.get(m3u_url)

# Check if the requests were successful
if txt_response.status_code == 200 and m3u_response.status_code == 200:
    # Read content from the responses
    txt_lines = txt_response.text.splitlines()
    m3u_lines = m3u_response.text.splitlines()

    output_lines = []

    for i, line in enumerate(m3u_lines):
        if line.startswith('#EXTINF:-1'):
            # Extract the string after ',' in #EXTINF line
            match_source = line.split(',')[1].strip()

            # Find the matching line in tv2.txt
            matching_txt_line = next((txt_line for txt_line in txt_lines if match_source in txt_line), None)

            if matching_txt_line:
                # Extract the URL from matching line in tv2.txt
                matching_url = matching_txt_line.split('http')[1].strip()

                # Replace the URL in the next line of #EXTINF in m3u
                next_line_index = i + 1
                m3u_lines[next_line_index] = f'http{matching_url}\n'

    # Write the updated m3u content to a new file
    with open('tv2_updated.m3u', 'w', encoding='utf-8') as updated_m3u_file:
        updated_m3u_file.writelines(m3u_lines)

    print("Conversion completed. Result saved to tv2_updated.m3u")
else:
    print(f"Failed to fetch content. Status codes: txt={txt_response.status_code}, m3u={m3u_response.status_code}")
