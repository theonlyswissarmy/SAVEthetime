
            ╱╱╱╱╭╮╱╱╱╱╭╮╱╱╱╱╱╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╭╮
            ╱╱╱╱┃┃╱╱╱╱┃┃╱╱╱╱╱╱╱╱┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱╭╯╰╮
            ╭━━╮┃┃╭┳╮╭┫╰━┳╮╭┳━━╮┃┃╱╰╋━━┳╮╭┳━━┳━━┳━╮╭╮╱╭╮╭╮╭┳┳━┳━┳━━┳━╮╭━╯┣╮╭┳━╮╭━━┳━━┳━━┳━╮╱┃╰━┳━┻╮╭╯
            ┃╭╮┃┃┃┣┫╰╯┃╭╮┃┃┃┃━━┫┃┃╱╭┫╭╮┃╰╯┃╭╮┃╭╮┃╭╮┫┃╱┃┃┃╰╯┣┫╭┫╭┫╭╮┃╭╯┃╭╮┃┃┃┃╭╮┫╭╮┃┃━┫╭╮┃╭╮╮┃╭╮┃╭╮┃┃
            ┃╭╮┃┃╰┫┃┃┃┃╰╯┃╰╯┣━━┃┃╰━╯┃╰╯┃┃┃┃╰╯┃╭╮┃┃┃┃╰━╯┃┃┃┃┃┃┃┃┃┃╰╯┃┃╱┃╰╯┃╰╯┃┃┃┃╰╯┃┃━┫╰╯┃┃┃┃┃╰╯┃╰╯┃╰╮  
            ╰╯╰╯╰━┻┻┻┻┻━━┻━━┻━━╯╰━━━┻━━┻┻┻┫╭━┻╯╰┻╯╰┻━╮╭╯╰┻┻┻┻╯╰╯╰━━┻╯╱╰━━┻━━┻╯╰┻━╮┣━━┻━━┻╯╰╯╰━━┻━━┻━╯
            ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱╭━╯┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃


SAVEthetime will do EACH floor of a mirror dungeon automatically, interaction is still required for shops, I have an autoshop feature worked out, but it won't be great.
I'm not mapping out which EGO gifts are best.
This was originally made to just do the TKT dungeon, but I'm modifying it so that it'll the regular Mirror dungeons too. 

Make sure Tesseract-OCR is installed before doing anything, you can install it from here, -> https://github.com/tesseract-ocr/tesseract.
Screen resolution MUST be in 1920 x 1080 and game must be in fullscreen windowed

It'll take a little bit for the GUI to be done. Nothing more than a week though. In it's current state it can go through the mirror dungeon and do fine. 

MAKE SURE TO BE FULL SCREEN WINDOWED AT 1920x1080 BEFORE STARTING!


There's still more than a few kinks to work out with the bot, the main one being autoshop, which is going to be happening in the next push, after that is an improvement in how fights are done. after that is making the gui look pretty


Autoshop ideas:
1. Easy autoshop, just buy as much as possible 
2. Screenshot every item as we attempt to buy it, try to locate image type, bleed, rupture, sinking, slash, ect. if team is of applicable type, buy item, if keywordless, reference internal document. (this is probably what im going to do)

autoupgrade ideas
1. read RGB values, items with higer rgb arent grey, items with lower are, if not grey determine type, than upgrade if possible. Do this for every item.
2. Select item, if item is a valid selection, determine type, if type applicable, upgrade.
3. Always 20% heal.


EVENT ISSUES
1. Mess with CV2 thresholding mroe so that we get a better readout more consistantly
