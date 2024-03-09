import os
import shutil

def move_files_to_destination(source_folder, destination_folder):
    # 대상 폴더가 존재하지 않으면 생성합니다.
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created target directory: {destination_folder}")

    # 소스 폴더 내 모든 파일을 순회합니다.
    for filename in os.listdir(source_folder):
        # 각 파일에 대한 전체 경로를 구성합니다.
        source_file_path = os.path.join(source_folder, filename)
        
        # 파일이 아닌 경우(하위 폴더 등)는 건너뜁니다.
        if os.path.isfile(source_file_path):
            # 파일을 대상 디렉토리로 이동합니다.
            destination_file_path = os.path.join(destination_folder, filename)
            shutil.move(source_file_path, destination_file_path)
            print(f"Moved: {source_file_path} -> {destination_file_path}")
        else:
            print(f"Skipped (not a file): {source_file_path}")

# 소스 폴더 경로
source_folder = "workspace/output"

# 사용자로부터 대상 폴더 경로 입력 받기
destination_folder = input("Enter the destination folder path: ").strip()

# 파일 이동 함수 호출
move_files_to_destination(source_folder, destination_folder)
