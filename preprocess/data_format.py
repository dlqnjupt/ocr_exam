def read(filename):
    # 打开文件
    fr = open(filename, 'r', encoding='UTF-8')
    # 读取文件所有行
    content = fr.readlines()
    contentLines = ''
    # 依次迭代所有行
    for line in content:
        # 去除空格
        line = line.strip()
        # 每行末尾则加一个空格
        line += " "
        # 如果是空行，则跳过
        if len(line) == 0:
            continue
        contentLines = contentLines + line
    return contentLines.split(" ")


# filename为写入CSV文件的路径，_list为要写入数据列表.
def text_save(filename, data_list, label_list):
    file = open(filename, 'a', encoding='UTF-8')
    for i in range(len(data_list)):
        s = data_list[i] + "	" + label_list[i] + "\n"
        file.write(s)
    file.close()
    print("保存文件成功")


if __name__ == '__main__':
    data_list = read("original_data/test1.txt")
    label_list = read("original_data/test_tgt.txt")
    print(data_list)
    print(label_list)
    text_save("test_data", data_list, label_list)
