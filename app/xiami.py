class song:
    def info(self):
        print "song"

class album:
    def info(self):
        print "album"

class collect:
    '''user defined collection'''
    def info(self):
        print "collect"

class artist:
    def info(self):
        print "artist"

class user:
    def fav_song(self):
        print "song"
    def fav_album(self):
        print "album"
    def fav_artist(self):
        print "fav artist"
    def fav_mv(self):
        print "fav mv"

class xiami:
    def info(self):
        print "xiami"
    def login(self, user):
        print "auth"

if __name__ == "__main__":
    xm = xiami()
    xm.info()
