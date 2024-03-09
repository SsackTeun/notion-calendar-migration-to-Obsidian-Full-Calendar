import os
import shutil

def delete_contents_in_folder(folder_path):
    # 폴더 내의 모든 아이템(파일 및 하위 폴더)을 순회
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        # 아이템이 파일인 경우 삭제
        if os.path.isfile(item_path):
            os.remove(item_path)
            print(f"Deleted file: {item_path}")
        # 아이템이 폴더인 경우, 해당 폴더와 그 내용을 삭제
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)
            print(f"Deleted folder and its contents: {item_path}")

# 'workspace/output' 및 'workspace/input' 폴더 내의 파일 및 하위 폴더 삭제, 단 폴더는 유지
folders = ["workspace/output", "workspace/input", "source"]
for folder in folders:
    if os.path.exists(folder) and os.path.isdir(folder):
        delete_contents_in_folder(folder)
    else:
        print(f"Folder does not exist: {folder}")

# 현재 경로의 'calendar.md' 파일 삭제
def delete_specific_file(file_name):
    if os.path.exists(file_name) and os.path.isfile(file_name):
        os.remove(file_name)
        print(f"Deleted file: {file_name}")
    else:
        print(f"File does not exist: {file_name}")

delete_specific_file("calendar.md")
