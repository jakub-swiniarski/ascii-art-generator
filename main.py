from PIL import Image

path=str(input("Input the image path: "));
img=Image.open(path);

pixels=img.load();
width, height = img.size;
chars = [[0 for y in range(height)] for x in range(width)]; 

for i in range(width):
    for j in range(height):
        (r,g,b)=pixels[i,j];
        sum=r+g+b;
        if sum>600:
            pass;
        elif sum>500:
            pass;
        elif sum>400:
            pass;
        elif sum>300:
            pass;
        elif sum>200:
            pass;
        elif sum>100:
            pass;
        else:
            pass;
