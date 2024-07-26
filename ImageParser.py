import urllib.request
import turtle

#method to fill color into each pixel
def fillPixel(x, y, *f_colors):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.pencolor(*f_colors)
    t.fillcolor(*f_colors)
    t.begin_fill()

#method to draw each pixel
def drawPixel(pixel_size):
    for i in range(2):
        t.forward(pixel_size)
        t.right(90)
        t.forward(pixel_size)
        t.right(90)

while True:
    images = ["NYU Flag", "Thumbs Up", "Justin Bieber", "Pikachus"]
    listImages = lambda: {i+1: images[i] for i in range(len(images))}

    for key,val in listImages().items(): print(f"{key}: {val}")
    imageNum = input("\nEnter an image number or 'q' to quit: ")

    if imageNum.isdigit(): imageNum = int(imageNum)
    elif imageNum == "q": 
        print("\nBye, have a good day!")
        break
    
    #------PARSE IMAGES------#
    urlDict = {1:"https://raw.githubusercontent.com/khyeborg/assignment9b/master/image3a.txt\n",
               2:"https://raw.githubusercontent.com/khyeborg/assignment9b/master/image3b.txt\n",
               3:"https://raw.githubusercontent.com/khyeborg/assignment9b/master/image4b.txt\n",
               4:"https://raw.githubusercontent.com/khyeborg/assignment9b/master/image4a.txt\n"}

    try:
        #open URL
        url = urlDict[imageNum]
        response = urllib.request.urlopen(url)
        print(f"Success! I was able to find the image '{images[imageNum-1]}'")

        #collect data
        all_data = response.read().decode("utf-8")
        split_data = all_data.split(",")

        #variables
        width = int(split_data[0])
        height = int(split_data[1])
        bg_color = float(split_data[2])
        pixel_size = int(split_data[3])
        pixel_colors = split_data[4:]

        num_b = 0
        index_b_list = []

        #remove all 'b' in data: note that 'b' represents line break
        while True:
            if "b" in pixel_colors:
                num_b += 1
                index_b = pixel_colors.index("b")
                index_b_list.append(index_b)
                pixel_colors.remove("b")
            else: break

        #setup turtle
        turtle.reset()                #restart turtle screen
        turtle.setup(width, height)
        t = turtle.Turtle()
        s = turtle.Screen()
        t.hideturtle()
        s.bgcolor(bg_color, bg_color, bg_color)
        x = (width/2) * (-1)
        y = height/2
        turtle.tracer(0)
        s.title(f"Image Parser - {images[imageNum-1]}")

        #TURTLE: COLOR!!
        if pixel_colors[0] == "true":
            #move through colors in groups of 3
            color1 = pixel_colors[1]
            color2 = pixel_colors[2]
            color3 = pixel_colors[3]
            index1 = pixel_colors.index(color1)
            index2 = pixel_colors.index(color2)
            index3 = pixel_colors.index(color3)

            for color in range(1, len(pixel_colors)-12000):
                if color in index_b_list or (x > (width/2)):
                    x = (width/2) * (-1)
                    y -= pixel_size
                    f_color1 = float(pixel_colors[index1])
                    f_color2 = float(pixel_colors[index2])
                    f_color3 = float(pixel_colors[index3])

                    fillPixel(x, y, f_color1, f_color2, f_color3)
                    drawPixel(pixel_size)

                    x += pixel_size
                    t.end_fill()
                
                #colors directly before/after 'b'
                else:
                    f_color1 = float(pixel_colors[index1])
                    f_color2 = float(pixel_colors[index2])
                    f_color3 = float(pixel_colors[index3])

                    fillPixel(x, y, f_color1, f_color2, f_color3)
                    drawPixel(pixel_size)

                    x += pixel_size
                    t.end_fill()
                
                index1 += 3
                index2 += 3
                index3 += 3

            turtle.update()

        #TURTLE: NO COLOR!!
        else:
            for color in range(len(pixel_colors)):
                if color in index_b_list:
                    x = (width/2) * (-1) #necessary?
                    y -= pixel_size
                    f_color = float(pixel_colors[color])

                    fillPixel(x, y, f_color, f_color, f_color)
                    drawPixel(pixel_size)

                    x += pixel_size
                    t.end_fill()

                #colors directly before/after 'b'
                else:
                    f_color = float(pixel_colors[color])

                    fillPixel(x, y, f_color, f_color, f_color)
                    drawPixel(pixel_size)

                    x += pixel_size
                    t.end_fill()
                
            turtle.update()

    except KeyError:
        print("Invalid image number. Please enter a valid image number.")
        continue

    except Exception as e:
        print(f"Error processing image: {str(e)}")
        continue

turtle.done()