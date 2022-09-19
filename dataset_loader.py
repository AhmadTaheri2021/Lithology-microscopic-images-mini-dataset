'''
    Copyright 2022 Ahmad Taheri. All Rights Reserved.
    
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
    
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
def Dataset_loader(path_):
   
   def image_laoder_X():
    tr_images_path = {}
    tr_images_path["Argillaceous_limestone"] = glob("/content/drive/MyDrive/data/DS_Lithology_new/train_set/class0/*.png")
    tr_images_path["Limestone"] = glob("/content/drive/MyDrive/data/DS_Lithology_new/train_set/class1/*.png")
    tr_images_path["Dolomitic_limestone"] = glob("/content/drive/MyDrive/data/DS_Lithology_new/train_set/class2/*.png")
    
    ts_images_path = {}
    ts_images_path["Argillaceous_limestone"] = glob("/content/drive/MyDrive/data/DS_Lithology_new/test_set/class0/*.png")
    ts_images_path["Limestone"] = glob("/content/drive/MyDrive/data/DS_Lithology_new/test_set/class1/*.png")
    ts_images_path["Dolomitic_limestone"] = glob("/content/drive/MyDrive/data/DS_Lithology_new/test_set/class2/*.png")
    '''
    print('Argillaceous_limestone size : {}'.format(len(images_path["Argillaceous_limestone"])))
    print('Limestone size : {}'.format(len(images_path["Limestone"])))
    print('Dolomitic_limestone size : {}'.format(len(images_path["Dolomitic_limestone"])))
    total_sample_size = len(images_path["Argillaceous_limestone"]) + len(images_path["Limestone"]) + len(images_path["Dolomitic_limestone"])
    print('Total size : {}'.format(total_sample_size))
    '''
    train_sample_size = len(tr_images_path["Argillaceous_limestone"]) + len(tr_images_path["Limestone"]) + len(tr_images_path["Dolomitic_limestone"])
    test_sample_size = len(ts_images_path["Argillaceous_limestone"]) + len(ts_images_path["Limestone"]) + len(ts_images_path["Dolomitic_limestone"])
    total_sample_size = train_sample_size + test_sample_size
    return tr_images_path,ts_images_path, total_sample_size

    #------------------------------------------------------
   tr_images_path, ts_images_path, total_sample_size = image_laoder_X()

   X_tr = []
   Y_tr = []

   for label in tr_images_path:
        for image_path in tr_images_path[label]:
            image = cv2.imread(image_path)
            image = cv2.resize(image,(224, 224))
            X_tr.append(image)
            Y_tr.append(images_class[label])  

   X_tr = np.array(X_tr)
   Y_tr = np.array(Y_tr)


   X_ts = []
   Y_ts = []

   for label in ts_images_path:
        for image_path in ts_images_path[label]:
            image = cv2.imread(image_path)
            image = cv2.resize(image,(224, 224))
            X_ts.append(image)
            Y_ts.append(images_class[label])  


   X_ts = np.array(X_ts)
   Y_ts = np.array(Y_ts)
 

   return X_tr, Y_tr, X_ts, Y_ts
