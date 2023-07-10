from PIL import Image

path=str(input("Input the image path: "));
img=Image.open(path);

pixels=img.load();
width, height = img.size;

print(pixels[1,1]);
