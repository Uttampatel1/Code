from pygame import mixer 
# Starting the mixer 
mixer.init() 
# Loading the song 
mixer.music.load("/store/emvlated/0/x Python codes/song.mp3") 
# Setting the volume 
mixer.music.set_volume(0.7) 
# Start playing the song 
mixer.music.play() 
# infinite loop 
while True :
    print("Press 'p' to pause, 'r' to resume") 
    print("Press 'e' to exit the program") 
    query = input("  ") 
    if query == 'p':
        mixer.music.pause()      
    elif query == 'r': 
        mixer.music.unpause() 
    elif query == 'e': 
        mixer.music.stop() 
        break