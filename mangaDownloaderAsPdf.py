import requests
from PIL import Image

totalPic = input("Pls enter Total pic: ") 
chapter = input("Pls enter Chapter: ") 

# https://mangakisa.com/boku-no-hero-academia - anima home page
# totalPic = 13
# chapter = 162
imagesList = [] 

for x in range(1,int(totalPic)+1):
    url = "https://s3.mkklcdnv3.com/mangakakalot/r1/read_boku_no_hero_academia_manga/chapter_"+ str(chapter) + "/"+ str(x) + ".jpg" #baseurl + str(page) + "/?s=" + book
    fileName = "D:\Mobile\Image"+ str(x) + '.jpg'
    print(fileName)
    req = requests.get(url)
    file = open(fileName, 'wb')
    for chunk in req.iter_content(100000):
        file.write(chunk)
    file.close()
    imgOpen = Image.open(fileName)
    convertImg = imgOpen.convert('RGB')
    imagesList.append(convertImg)

imagesList[0].save(r"D:\Mobile\Image"+ str(chapter) + '.pdf',save_all=True, append_images=imagesList)
