# property 내의 title 값중에 검색한 단어를 포함하는 title 을 일괄로 한단어로 변경
import os
import re

directory = 'workspace/output'
def replace_title_word_in_md_files(directory, search_word, replace_word):
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()

            # 'title:' 뒤에 오는 단어를 찾아서 교체하기
            # 교체할 문자열 뒤에 불필요한 개행 문자가 추가되지 않도록 주의
            pattern = r'(title:\s*).+'

            if search_word in content:
                print(content)
                # Lambda 함수를 사용하여 title 라인 끝의 개행문자를 유지
                new_content = re.sub(pattern, lambda m: m.group(1) + replace_word, content, count=1)

                # 파일에 수정된 내용을 쓰기
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f"Updated {filename}")

# 사용자 입력 받기
search_word = input("title 의 특정 단어가 포함된 .md 파일 찾기 : ").strip()
replace_word = input("대상 파일의 title 을 입력한 단어로 교체 : ").strip()

replace_title_word_in_md_files(directory, search_word, replace_word)
