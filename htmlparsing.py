from html import parser
from html.parser import HTMLParser
from sys import meta_path

metacount = 0

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print("Encountered comment: ", data)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position", pos[1])

    def handle_starttag(self, tag, attrs):
        global metacount
        if tag == 'meta':
            metacount += 1
        print("Encountered tag: ", data)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position", pos[1])

        if attrs.__len__() > 0:
            print("\Attribut    es")


    def handle_endtag(self, tag):
        print("Encountered tag: ", data)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position", pos[1])

def main():
    parser = MyHTMLParser()
    f = open("samplehtml.html")
    if f.mode == 'r':
        contents = f.read()
        parser.feed(contents)


if __name__ == "__main__":
    main()