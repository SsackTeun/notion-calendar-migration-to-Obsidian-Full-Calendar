# 이름|날짜|태그 가 들어 있는 파일 파싱

def parse(file_path):
    events = {}
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines[2:]:  # 테이블 헤더와 구분선 이후부터 시작
                if "|" in line:
                    parts = line.split("|")
                    if len(parts) >= 3:
                        raw_name = parts[1].strip()[2:-2]  # 이벤트 이름 추출
                        raw_date = parts[2].strip()
                        # "날짜" 또는 "---"와 같은 불필요한 줄을 무시합니다.
                        if raw_date == "날짜" or raw_date == "---" or raw_name == "":
                            continue
                        try:
                            if "→" in raw_date:
                                # 날짜 범위 처리
                                start_date, end_date = [date.strip() for date in raw_date.split("→")]
                                start_date_parts = start_date.replace("년 ", "-").replace("월 ", "-").replace("일", "").strip().split("-")
                                end_date_parts = end_date.replace("년 ", "-").replace("월 ", "-").replace("일", "").strip().split("-")

                                # 시작 날짜와 종료 날짜의 월과 일 부분을 두 자리 숫자로 포매팅합니다.
                                start_date = f"{start_date_parts[0]}-{start_date_parts[1].zfill(2)}-{start_date_parts[2].zfill(2)}"
                                end_date = f"{end_date_parts[0]}-{end_date_parts[1].zfill(2)}-{end_date_parts[2].zfill(2)}"

                                events[raw_name] = {"start_date": start_date, "end_date": end_date, "is_range": True}

                            else:
                                # 단일 날짜 처리
                                date_parts = raw_date.replace("년 ", "-").replace("월 ", "-").replace("일", "").strip().split("-")
                                if len(date_parts) == 3:
                                    date = f"{date_parts[0]}-{date_parts[1].zfill(2)}-{date_parts[2].zfill(2)}"
                                    events[raw_name] = {"date": date, "is_range": False}
                                else:
                                    print(f"Invalid date format for event '{raw_name}': '{raw_date}'")
                        except IndexError:
                            print(f"Error parsing date for event '{raw_name}': '{raw_date}'")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    
    return events