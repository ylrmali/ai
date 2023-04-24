import os
from bs4 import BeautifulSoup

"""Bu sınıf kontrolden geçen datanın labellerini yolov5 formatına dönüştürür"""

class XmlToTxt():
    def __init__(self,path,class_dict):
        self.path = path
        self.class_dict = class_dict
        self.dir_path = os.path.dirname(path)

    def xml_full_path_get(self):
        xml_file_path = []
        for i in os.listdir(self.path):
            if i.endswith(".xml"):
                x=f"{self.dir_path}/{i}"
                xml_file_path.append(x)

        return xml_file_path

    def xml_to_txt(self):

        Xml_File_Paths = list(self.xml_full_path_get())

        for xml_file_path in Xml_File_Paths:
            txt_files = os.path.join(self.dir_path, os.path.basename(xml_file_path)[:-4]+'.txt')

            with open(xml_file_path, 'r') as xml_file:
                xml_data = xml_file.read()
            soup = BeautifulSoup(xml_data, 'xml')

            img_size = soup.find('size')
            img_width = int(img_size.find('width').text)
            img_height = int(img_size.find('height').text)

            objects = soup.find_all('object')
            obj_list = []



            class_lambda = lambda x: self.class_dict.get(x, 0)

            for obj in objects :
                label = class_lambda(obj.find('name').text)
                xmin = int(obj.find('xmin').text)
                ymin = int(obj.find('ymin').text)
                xmax = int(obj.find('xmax').text)
                ymax = int(obj.find('ymax').text)
                if img_width == 0 or img_height == 0:

                    continue
                else:
                    x = ((xmin + xmax) / 2.0) / img_width
                    y = ((ymin + ymax) / 2.0) / img_height
                    width = (xmax - xmin) / img_width
                    height = (ymax - ymin) / img_height

                    obj_list.append([label, x, y, width, height])

            with open(txt_files, 'w') as txt_file:
                for obj in obj_list:
                    txt_file.write(f'{obj[0]} {obj[1]:.6f} {obj[2]:.6f} {obj[3]:.6f} {obj[4]:.6f}\n')





path = "C:/Users/username/Desktop/path/"

"""Example class dict sayı atama işlemi için girdi """
"""Bu girdiler xmlden txt formatına dönüşürken nesne isimlerine sayı atamak için"""
"""class_dict = {'obje': 0, 'obje1': 1, 'obje2': 2,
                          'obje3': 3, 'obje4': 4, 'obje5': 5,
                          'obje6': 6, 'obje7': 7, 'obje8': 8,
                          'obje9': 9, 'obje10': 10, 'obje11': 11,
                          'obje12': 12, 'obje13': 13, 'obje14': 14,
                          'obje15': 15, 'obje16': 16, 'obje17': 17,
                          'obje18': 18, 'obje19': 19}"""

class_dict = {"obje15":15}
c=XmlToTxt(path,class_dict)
c.xml_to_txt()
