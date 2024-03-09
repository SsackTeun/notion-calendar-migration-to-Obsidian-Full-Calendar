type_1_data = """
---
title: {title}
allDay: true
type: recurring
daysOfWeek: [S, F, R, W, T, M, U]
startRecur: {startdate}
endRecur: {enddate}
---
"""

type_2_data = """
---
title: {title}
allDay: true
date: {date}
endDate: {date}
completed: null
---
"""

# 메인 함수
# 수정된 함수
def process_md_file(input_file_path, output_file_path, events_info):
    print('Files count:', len(events_info))
    for event, info in events_info.items():
        # 정보에 따라 적절한 템플릿 선택 및 포맷팅, 여기서는 시작 공백을 제거하지 않음
        if info["is_range"]:
            formatted_data = type_1_data.format(title=event, startdate=info['start_date'], enddate=info['end_date'])
        else:
            formatted_data = type_2_data.format(title=event, date=info['date'])

        # 입력 파일을 읽음
        with open(f'{input_file_path}/{event}.md', 'r', encoding='utf-8') as file:
            content = file.read()

        # '---' 섹션과 기존 내용 사이의 첫 개행 문자 제거를 위한 처리
        start_index = content.find('---')
        end_index = content.find('---', start_index + 3)

        # formatted_data의 시작 부분 공백 제거
        formatted_data = formatted_data.lstrip()
        formatted_data = formatted_data.rstrip()
        # 새로운 내용으로 기존 내용을 교체
        new_content = content[:start_index] + formatted_data + content[end_index+3:]

        # 출력 파일에 수정된 내용 쓰기
        with open(f'{output_file_path}/{event}.md', 'w', encoding='utf-8') as file:
            file.write(new_content)

        print(f'Updated {event}.md')
