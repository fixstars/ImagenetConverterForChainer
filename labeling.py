import os
import sys
import csv
import random
import urllib

def main():
    train_dir = sys.argv[1]
    val_dir = sys.argv[2]

    train_data = []
    label_table = {}
    i = 0
    for dir in sorted(os.listdir(train_dir)):
        label_table[dir] = i
        dir_path = os.path.abspath(train_dir + "/" + dir)
        for file in os.listdir(dir_path):
            file_path = os.path.abspath(dir_path + "/" + file)
            train_data.append([file_path, i])
        i = i+1

    filename, header = urllib.urlretrieve("https://raw.githubusercontent.com/tensorflow/models/36203f09dc257569be2fef3a950ddb2ac25dddeb/inception/inception/data/imagenet_2012_validation_synset_labels.txt")
    val_data = []
    i = 0
    for file, line in zip(sorted(os.listdir(val_dir)), open(filename, "r")):
        label = line.rstrip('\r\n')
        file_path = os.path.abspath(val_dir + "/" + file)
        label_id = label_table[label]
        val_data.append([file_path, label_id])

    random.shuffle(train_data)
    random.shuffle(val_data)

    with open("label_table.ssv", "w") as f:
        csv.writer(f, delimiter=' ').writerows(sorted(label_table.items(), key=lambda t : t[1]))
    with open("train.ssv", "w") as f:
        csv.writer(f, delimiter=' ').writerows(train_data)
    with open("val.ssv", "w") as f:
        csv.writer(f, delimiter=' ').writerows(val_data)

if __name__ == '__main__':
    main()
