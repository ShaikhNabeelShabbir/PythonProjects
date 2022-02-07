import pyshorteners as url
def get_shortener():
    link = input("enter your link\n")
    x = (url.Shortener().tinyurl.short(link))
    print(x)

while True:
    print("1)shortened your link\n2)quit")
    user=int(input("Enter your choice: "))
    if user==1:
        get_shortener()
    elif user==2:
        quit()
    else:
        print("invalid input")

