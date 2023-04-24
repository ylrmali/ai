import os
import shutil
import random

"""Bu sınıf dönüşümü yapılan tüm datayı test validation train olarak istenilen oranda böler ve fazla olan tüm dosyaları remove eder"""

class TestTrainSplit():

    def __init__(self,path,test_ratio,val_ratio,train_ratio):
        self.path = path
        self.test_ratio = test_ratio
        self.val_ratio = val_ratio
        self.train_ratio = train_ratio

    def test_train_val_split(self):

        test_dir = f"{self.path}/test"
        val_dir = f"{self.path}/val"
        train_dir = f"{self.path}/train"
        os.makedirs(test_dir, exist_ok=True)
        os.makedirs(val_dir, exist_ok=True)
        os.makedirs(train_dir, exist_ok=True)

        png_files = [f for f in os.listdir(self.path) if f.endswith(".png")]
        random.shuffle(png_files)

        test_files = png_files[:int(len(png_files) * self.test_ratio)]

        for f in test_files:
            shutil.copy(os.path.join(self.path, f), os.path.join(test_dir, f))
            shutil.copy(os.path.join(self.path, f[:-4] + ".txt"), os.path.join(test_dir, f[:-4] + ".txt"))

        val_files = png_files[int(len(png_files) * self.test_ratio):int(len(png_files) * (self.test_ratio + self.val_ratio))]
        for f in val_files:
            shutil.copy(os.path.join(self.path, f), os.path.join(val_dir, f))
            shutil.copy(os.path.join(self.path, f[:-4] + ".txt"), os.path.join(val_dir, f[:-4] + ".txt"))

        train_files = png_files[int(len(png_files) * (self.test_ratio + self.val_ratio)):]
        for f in train_files:
            shutil.copy(os.path.join(self.path, f), os.path.join(train_dir, f))
            shutil.copy(os.path.join(self.path, f[:-4] + ".txt"), os.path.join(train_dir, f[:-4] + ".txt"))

        for i in os.listdir(self.path):
            i = f"{self.path}/{i}"
            if i.endswith(".png") or i.endswith(".xml") or i.endswith(".txt"):
                os.remove(i)


path = "C:/Users/username/Desktop/path"
x = TestTrainSplit(path,0.1,0.1,0.8)
x.test_train_val_split()
