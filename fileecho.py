#Read in the echo.txt file and display it in the terminal using print()
#This is a guided practice. Either follow the video or your instructor in class.


with open("echo.txt", "r") as file:

    content = file.read()


print(content)