from PIL import Image

path=str(input("Input the image path: "));
img=Image.open(path);
width,height=img.size;
ratio=int(width/height);
img=img.rotate(90);
img=img.transpose(Image.FLIP_TOP_BOTTOM);
img=img.resize((100,int(100*ratio*1.77)),Image.LANCZOS);
width,height=img.size;

pixels=img.load();
chars = [[0 for i in range(height)] for j in range(width)]; 

f=open("output.txt","w");

for i in range(width):
    for j in range(height):
        (r,g,b)=pixels[i,j];
        sum=r+g+b;
        if sum>600:
            chars[i][j]="'";

        elif sum>550:
            chars[i][j]='"';

        elif sum>500:
            chars[i][j]=":";

        elif sum>450:
            chars[i][j]=";"

        elif sum>400:
           chars[i][j]="!";
    
        elif sum>350:
            chars[i][j]="+";

        elif sum>300:
           chars[i][j]="%";
 
        elif sum>250:
            chars[i][j]="?"

        elif sum>200:
           chars[i][j]="/";
 
        elif sum>150:
            chars[i][j]="&";

        elif sum>100:
            chars[i][j]="$";
            
        elif sum>50:
            chars[i][j]="#";

        else:
            chars[i][j]="@";
        
        f.write(chars[i][j]);
    f.write("\n");

f.close();
print("The output is saved in 'output.txt'.");
