from PIL import Image

path=str(input("Input the image path: "));
img=Image.open(path);

pixels=img.load();
width, height = img.size;
chars = [[0 for y in range(height)] for x in range(width)]; 

# ' ; ! % & $ #

f=open("output","w");

for i in range(width):
    for j in range(height):
        (r,g,b)=pixels[i,j];
        sum=r+g+b;
        if sum>600:
            chars[i][j]="'";

        elif sum>500:
            chars[i][j]=";";

        elif sum>400:
           chars[i][j]="!";
 
        elif sum>300:
           chars[i][j]="%";
 
        elif sum>200:
           chars[i][j]="&";
 
        elif sum>100:
            chars[i][j]="$";
            
        else:
            chars[i][j]="#";
            
        f.write(chars[i][j]);
    f.write("\n");
f.close();
