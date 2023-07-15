from PIL import Image;
#import numpy as np;

path=str(input("Input the image path: "));
img=Image.open(path);
width,height=img.size;
ratio=int(width/height);
img=img.rotate(90);
img=img.transpose(Image.FLIP_TOP_BOTTOM);
img=img.resize((100,int(100*ratio*1.77)),Image.LANCZOS);
width,height=img.size;

pixels=img.load();
img.close();

f=open("output.txt","w");

for i in range(width):
    for j in range(height):
        (r,g,b)=pixels[i,j];
        sum=r+g+b;
        if sum>600:
            char="'";

        elif sum>550:
            char='"';

        elif sum>500:
            char=":";

        elif sum>450:
            char=";"

        elif sum>400:
            char="!";
    
        elif sum>350:
            char="+";

        elif sum>300:
            char="%";
 
        elif sum>250:
            char="?"

        elif sum>200:
            char="/";
 
        elif sum>150:
            char="&";

        elif sum>100:
            char="$";
            
        elif sum>50:
            char="#";

        else:
            char="@";
        
        f.write(char);
    f.write("\n");

f.close();
print("The output is saved in 'output.txt'.");
