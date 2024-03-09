# 기본 모듈
import os
import re
import shutil

# 만든 모듈
from module import parse_properties as properties # 이름 | 날짜 | 태그 파일 파싱
from module import modify_process as mod # 캘린더 파일을 파싱데이터에서 구분하여, 값처리

# calendar.md 에서 이름/날짜 파싱
calendar_file_path = "calendar.md"  # 여기에 실제 경로를 입력해주세요.

# 작업 디렉토리
input_file_path = "workspace/input"
output_file_path = "workspace/output"

# 리스트 생성
events_info = properties.parse(calendar_file_path)

# 파일 처리
mod.process_md_file(input_file_path, output_file_path,  events_info)



