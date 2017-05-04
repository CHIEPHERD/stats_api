def five_hello():
    for i in range(0, 5):
        print("Hello")
    file = open("testfile.txt", "w")

    file.write("Hello World\n")
    file.write("This is our new text file")
    file.write(" and this is anotherline.\n")
    file.write("Why? Because we can.")

    file.close()
    return 221
