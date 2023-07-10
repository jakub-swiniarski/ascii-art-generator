from PIL import Image

path=str(input("Input the image path: "));
img=Image.open(path);

pixels=img.load();
width, height = img.size;
pix = [[0 for x in range(height)] for y in range(width)]; 

print(pixels[1,1]);

for i in range(width):
    for j in range(height):
        pix[i][j]=pixels[i,j];

print(pix[1][1]);
