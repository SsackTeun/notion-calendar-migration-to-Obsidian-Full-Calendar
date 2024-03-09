import os
import shutil

def copy_files_to_specific_directory(source_folder, target_folder):
    # 대상 폴더가 존재하지 않으면 생성합니다.
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
        print(f"Created target directory: {target_folder}")

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            source_file_path = os.path.join(root, file)
            destination_file_path = os.path.join(target_folder, file)
            
            # 동일한 파일명이 대상 디렉토리에 존재하는 경우, 새로운 파일명을 생성합니다.
            new_destination_file_path = destination_file_path
            counter = 1
            while os.path.exists(new_destination_file_path):
                file_name, file_extension = os.path.splitext(file)
                new_destination_file_path = os.path.join(target_folder, f"{file_name}_{counter}{file_extension}")
                counter += 1
            
            # 파일을 대상 디렉토리로 복사합니다.
            shutil.copy2(source_file_path, new_destination_file_path)
            print(f"Copied: {source_file_path} -> {new_destination_file_path}")

# 'source' 폴더 내부의 모든 파일을 'workspace/input' 폴더로 복사합니다.
source_folder = "source"
target_folder = "workspace/input"
copy_files_to_specific_directory(source_folder, target_folder)
