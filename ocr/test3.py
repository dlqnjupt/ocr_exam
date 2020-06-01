import tr
import json

if __name__ == '__main__':
    # detect and recognize text lines with angle, return list of ((cx, cy, width, height, angle), text, confidence)
    list = tr.run_angle("example2.png")
    filename = "data.json"
    # 将数据写到"data.json"
    with open(filename, 'w') as file_obj:
        json.dump(list, file_obj)