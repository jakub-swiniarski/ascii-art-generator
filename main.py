from PIL import Image

path=str(input("Input the image path: "));
img=Image.open(path);
width,height=img.size;
ratio=int(width/height);
img=img.rotate(90);
img=img.resize((100,100*ratio*2),Image.LANCZOS);
width,height=img.size;

pixels=img.load();
chars = [[0 for i in range(height)] for j in range(width)]; 

# ' ; ! % & $ #

f=open("output.txt","w");

for i in range(width):
    line="";
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
        
        line+=chars[i][j];
    f.write(line+"\n");

f.close();
