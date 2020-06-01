"""
 打开word2id.pkl
"""
import pickle
f = open('word2id.pkl','rb')
data = pickle.load(f)
print(data)

if __name__ == '__main__':
    data = []
    sent_, tag_ = [], []
    with open("test_data", encoding='utf-8') as fr:
        lines = fr.readlines()
        for line in lines:
            if line != '\n':
                [char, label] = line.strip().split()
                sent_.append(char)
                tag_.append(label)
            else:
                data.append((sent_, tag_))
                sent_, tag_ = [], []
    print(data)