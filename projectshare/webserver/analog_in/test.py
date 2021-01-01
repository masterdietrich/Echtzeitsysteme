import datetime


if __name__ == '__main__':
    datei = open("test.txt",'a')
    text =chr(91)+"%s" % datetime.datetime.now() + chr(93) + " "
    datei.write(text)
    datei.close()

