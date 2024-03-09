import os
import re
from datetime import datetime

directory = 'workspace/output'

def extract_date_info(content):
    """
    파일 내용에서 date, startRecur, endRecur 값을 추출합니다.
    """
    date_pattern = r'date:\s*(\d{4}-\d{2}-\d{2})'
    range_pattern = r'startRecur:\s*(\d{4}-\d{2}-\d{2})\s*endRecur:\s*(\d{4}-\d{2}-\d{2})'

    date_match = re.search(date_pattern, content)
    range_match = re.search(range_pattern, content, re.DOTALL)

    if date_match:
        return date_match.group(1), None, None
    elif range_match:
        return None, range_match.group(1), range_match.group(2)
    else:
        return None, None, None

def generate_new_filename(title, date, start, end):
    """
    새로운 파일명을 생성합니다.
    """
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    if date:
        new_name = f"{title}_{date}.md"
    elif start and end:
        new_name = f"{title}_{start}_to_{end}.md"
    else:
        new_name = f"{title}_{now}.md"
    return new_name

def replace_title_word_in_md_files(directory, search_word, replace_word):
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()

            if search_word in content:
                pattern = r'(title:\s*).+'
                # title 라인을 변경합니다.
                new_content = re.sub(pattern, lambda m: m.group(1) + replace_word, content, count=1)

                date, start, end = extract_date_info(content)
                new_filename = generate_new_filename(replace_word, date, start, end)
                new_filepath = os.path.join(directory, new_filename)

                # 변경된 내용을 쓰고 파일명을 변경합니다.
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(new_content)

                os.rename(filepath, new_filepath)
                print(f"Updated and renamed {filename} to {new_filename}")

# 사용자 입력
search_word = input("title 의 특정 단어가 포함된 .md 파일 찾기 : ").strip()
replace_word = input("대상 파일의 title 을 입력한 단어로 교체 : ").strip()

replace_title_word_in_md_files(directory, search_word, replace_word)
