import urllib.request
import json


def main():
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5"

    webUrl = urllib.request.urlopen(urlData)
    print("result code: " + str(webUrl.getCode()))

    



if __name__ == "__main__":
    main()