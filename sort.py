# encoding: utf-8
# Creating IMAGE_FOLDER.tar archives with photos in JPG
# for backing up to amazon Glacier
#
# MIT license: (author: menangen)

PHOTO_FOLDER = 'D:/temp/photo'  # example is 'D:\temp\photo'
DESTINATION = PHOTO_FOLDER

import glob, os, tarfile

list_files = os.listdir(PHOTO_FOLDER)
folders_for_processing = []

for file_or_directory in list_files:
    if os.path.isdir(PHOTO_FOLDER + '/' + file_or_directory):
        folders_for_processing.append(file_or_directory)
    else:
        print "File %s in %s" % (file_or_directory, PHOTO_FOLDER)

for one_folder in folders_for_processing:
    jpg_files_list = glob.glob(PHOTO_FOLDER + "/" + one_folder + "/*.jpg")
    #movie_files_list = glob.glob(PHOTO_FOLDER + "/" + one_folder + "/" + "*.MOV")

    with tarfile.open("%s/%s.tar" % (DESTINATION, one_folder), "w") as tar:
        for one_jpeg in jpg_files_list:
            tar.add(one_jpeg, arcname=one_folder + "/" + one_jpeg.split("/")[-1].split("\\")[-1])

        print "Created %s/%s.tar" % (DESTINATION, one_folder)