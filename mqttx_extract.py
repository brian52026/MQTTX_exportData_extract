import json
import sys
import os

def main():
    
    # 檢查輸入參數，附加 JSON 檔案
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <path to log file>")
        input("Press Enter to exit...")
        exit(1)
    
    log_file_path = sys.argv[1]
    if not os.path.exists(log_file_path):
        print(f"Path {log_file_path} does not exist")
        input("Press Enter to exit...")
        exit(1)
        
    # 讀取 JSON 檔案
    with open(log_file_path, 'r', encoding='utf-8') as file:
        print('Working file:', log_file_path)
        data = json.load(file)

    # 使用者輸入 topic 名稱
    topic = input('請輸入要擷取的 topic 名稱: ')

    # 查找對應的片段並擷取 payload 和 createAt
    results = []
    for entry in data:
        for message in entry.get("messages", []):
            if message["topic"] == topic:
                results.append(f"[ {message['createAt']} ] : {message['payload']}")

    if results:
        log_filename = f'{topic.replace("/", "_")}.log'
        # 將結果寫入 log 檔案
        with open(log_filename, 'w') as log_file:
            for result in results:
                log_file.write(result + '\n')
        
        print(f'擷取的資料已保存到 {log_filename}')
    else:
        print(f'找不到指定的 topic: {topic}')

if __name__ == '__main__':
    main()
