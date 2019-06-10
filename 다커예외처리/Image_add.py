import os
import json

class Dachore_image:
        def __init__(self,image_Name):
                self.image_Name = image_Name


        def Image_add(self,image_Name):
                check = True
                print (" image Pull... Docker Hub  ")
                print (" wait.. we are Ä¡ Å² ÆÀ..  ")
                if os.system('sudo docker pull '+image_Name) != 0: # error
                    check = False
                return check


        def Image_packageList(self,image_Name):
                package_list = os.popen('sudo docker run '+image_Name+' dpkg -l').read()
                package_list += os.popen ('sudo docker run '+image_Name+' rpm -qa').read()
                package = open('/home/ubuntu/test.txt','w')
                package.write(package_list)
                #print ("json_val = %s"%json_val)


        def Image_delete(self):
                os.system('sudo docker stop $(sudo docker ps -a -q)')
                os.system('sudo docker rm $(sudo docker ps -a -q)')
                os.system('sudo docker rmi $(sudo docker images -q)')