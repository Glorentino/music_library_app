# Apple music experience
# catergories songs, albums, artist, genre
# store, display, delete, 'play', 

class AppleMusic:
    def __init__(self):
        self.library = {} # shows albums
        self.songsLibrary = [] # show songs
        self.artistLibrary = {} # shows artist
        
    def store(self, storeInfo):
        songName, artist, albumName, genre = storeInfo
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
    
    def delete(self, deleteInfo):
        typeInfo, songName, artist, albumName, genre = deleteInfo
        if typeInfo == "song":
            self.songsLibrary.remove(songName+"-"+artist)
            self.library[albumName].remove(songName)
            self.artistLibrary[artist][albumName].remove(songName)
        if typeInfo == "artist":
            for album in self.artistLibrary[artist]:
                for song in self.artistLibrary[artist][album]:
                    self.songsLibrary.remove(song+"-"+artist)
                del self.library[album] 
            del self.artistLibrary[artist]
        if typeInfo == "album":
            for song in self.artistLibrary[artist][albumName]:
                self.songsLibrary.remove(song+"-"+artist)
            del self.artistLibrary[artist][albumName]
            del self.library[albumName]
        print(self.library)
        
        return "Removed from library"
    
    def display(self):
        return self.artistLibrary, self.library, self.songsLibrary

appleMusic = AppleMusic()
print(appleMusic.store(["Glorious Day", "Glory Baby", "Glory Days", "Soul"]))
print(appleMusic.store(["Glorious Day 2", "Glory Baby", "Glory Days", "Soul"]))
print(appleMusic.store(["Glorious Day 2", "Glory Baby", "Glory Days", "Soul"]))
print()
print(appleMusic.store(["Half moon Japanese", "Carmello Vision", "7", "R&B"]))
print(appleMusic.store(["Aisheteru", "Shota-Chwan", "Shota ASSaSIN", "Hip Hop"]))
print(appleMusic.display())
print(appleMusic.delete(["album", "Aisheteru", "Shota-Chwan", "Shota ASSaSIN", "Hip Hop"]))
