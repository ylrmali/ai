from zipfile import ZipFile
import os
import cv2
from dotenv import load_dotenv, dotenv_values

"""Bu sınıf label ve size kontrolü yapar.Labeli eksik olan dosyaları remove eder"""

class VeriHazirlama():

    def __init__(self,path,size):
        self.path = path
        self.dir_path = os.path.dirname(path)
        self.size = size

    def zip_open(self):
        with ZipFile(self.path, 'r') as zObject:
            zObject.extractall(path=self.dir_path)
            return 'zip açıldı'

    def diziye_al(self):
        self.zip_open()
        png_filenames = []
        png_full_names = []
        xml_filenames = []
        xml_full_names = []

        for i in os.listdir(self.dir_path):
            if i.endswith(".png"):
                png_full_names.append(i)
                i = i[:-4]
                png_filenames.append(i)
            elif i.endswith(".xml"):
                xml_full_names.append(i)
                i = i[:-4]
                xml_filenames.append(i)

        return png_filenames, xml_filenames,png_full_names, xml_full_names

    def label_and_size_control(self):
        png_filenames, xml_filenames,png_full_names, xml_full_names = self.diziye_al()
        not_labels_img = []
        not_size = []

        for i in png_full_names:
            sayac = 0
            full_path =f"{self.dir_path}/{i}"
            img=cv2.imread(full_path)
            img = img.shape[0:2]

            if self.size != img :
                    not_size.append([i,img])
            i = i[:-4]
            for j in xml_filenames:
                if i == j :
                    sayac +=1
            if sayac == 0 :
                t = (i+".png")
                not_labels_img.append(t)

        return not_labels_img,not_size

    def remove(self):
        not_labels_img,not_size = self.label_and_size_control()
        if (len(not_labels_img))>0 or 0<(len(not_size)):
            error = "lütfen sorunlu dosyaları düzenleyin!"
            label_error = f"Labeli Olmayan Resimler: {not_labels_img}"
            size_error = f"Boyut Bilgisi Eşleşmeyen Resimler: {not_size}"

            for i in not_labels_img:
                os.remove(f"{self.dir_path}/{i}")

            return error, label_error, size_error


        else :
            return "Veriler Kontrolden Geçti"

# load_dotenv()
# file = os.getenv('FILE')
# print(f'{file}/image.png')

# path = "/web/media/project-files/a.zip"
# size = (2160, 3840)
# x = VeriHazirlama(path, size)
# print(x.remove())


