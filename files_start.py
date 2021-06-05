


def main():

    #  open file for write access and create if doesn't exist
    # f = open("textfile.txt", "w+")


    #  Open file for appending text
    f = open("textfile.txt", "r")

    # # write lines of data to file
    # for i in range(10):
    #     f.write("This is line " + str(i) + "\r\n")



    # Open file and read the contents
    if f.mode == 'r':
        # contents = f.read()
        fl = f.readlines()
        for x in fl:
            print(x)

        # print(contents)

         # close file when done
    f.close()


if __name__ == "__main__":
    main()