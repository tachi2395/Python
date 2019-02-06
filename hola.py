from PIL import Image
import glob, os, shutil

path = "C:/Users/LSA_2/OneDrive/Imagenes/Álbum de cámara/kantai"
#path = "/home/aceron/Downloads/p"

fland = path + "/l"
fport = path + "/p"

cont = 0
land = 0
port = 0

os.chdir(path)
for file in glob.glob("*.*"):
	cont = cont + 1

	f = path + "/" + file

	im = Image.open(f)
	w = im.width
	h = im.height

	if (h > w):
		port = port+1
		shutil.copy2(f, fport+"/"+file)
	else:
		land = land+1
		shutil.copy2(f, fland+"/"+file)
		
		

print ("Landscape: %d" % land)
print ("Portrait: %d" % port)
print ("Archivos procesados: %d" % cont)
