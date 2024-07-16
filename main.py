from PIL import Image;

path          = str(input("Input the image path: "));
width_desired = int(input("Input the desired image width (characters): "))
img           = Image.open(path);
width, height = img.size;
ratio         = width / height;
img           = img.resize((width_desired, int(width_desired / ratio / 2)), Image.LANCZOS);
width, height = img.size;
pixels        = img.load();

img.close();

f=open("output.txt", "w");

for y in range(height):
    for x in range(width):
        (r, g, b) = pixels[x, y];
        sum = r + g + b;
        if sum > 600:
            char = "'";

        elif sum > 550:
            char = '"';

        elif sum > 500:
            char = ":";

        elif sum > 450:
            char = ";"

        elif sum > 400:
            char = "!";
    
        elif sum > 350:
            char = "+";

        elif sum > 300:
            char = "?";
 
        elif sum > 250:
            char = "/"

        elif sum > 200:
            char = "%";
 
        elif sum > 150:
            char = "#";

        elif sum > 100:
            char = "&";
            
        elif sum > 50:
            char = "$";

        else:
            char = "@";
        
        f.write(char);
    f.write("\n");

f.close();
print("The output is saved in 'output.txt'.");
