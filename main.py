# Apple music experience
# catergories songs, albums, artist, genre
# store, display, delete, 'play', 

class AppleMusic:
    def __init__(self):
        self.library = {} # shows albums
        self.songsLibrary = [] # show songs
        self.artistLibrary = {} # shows artist
        
    def store(self, inputInfo):
        songName, artist, albumName, genre = inputInfo
        if albumName not in self.library:
            self.library[albumName] = []
            self.library[albumName].append(songName)
            self.songsLibrary.append(songName+"-"+artist)
            
        elif albumName in self.library:
            if songName in self.library[albumName]:
                return "Already in library"
            self.library[albumName].append(songName)
            self.songsLibrary.append(songName+"-"+artist)
            
        if artist not in self.artistLibrary:
            self.artistLibrary[artist] = {}
            self.artistLibrary[artist][albumName] = []
            self.artistLibrary[artist][albumName].append(songName)
        
        elif artist in self.artistLibrary:
            if albumName not in self.artistLibrary[artist]:
                self.artistLibrary[artist][albumName] = []
                
            if songName not in self.artistLibrary[artist][albumName]:
                self.artistLibrary[artist][albumName].append(songName)
        return "Added to Library"
    
    def delete(self):
        pass
    def display(self):
        return self.artistLibrary, self.library, self.songsLibrary

appleMusic = AppleMusic()
print(appleMusic.store(["Glorious Day", "Glory Baby", "Glory Days", "Soul"]))
print(appleMusic.store(["Glorious Day 2", "Glory Baby", "Glory Days", "Soul"]))
print(appleMusic.store(["Glorious Day 3", "Glory Baby", "Glory Days", "Soul"]))
print(appleMusic.display())
