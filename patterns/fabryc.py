class MultimediaObject:
    def play(self):
        pass

# Конкретні класи мультимедійних об'єктів
class Audio(MultimediaObject):
    def play(self):
        return "Playing audio"

class Video(MultimediaObject):
    def play(self):
        return "Playing video"

class Photo(MultimediaObject):
    def play(self):
        return "Displaying photo"

# Фабричний клас для створення мультимедійних об'єктів
class MultimediaFactory:
    def create_media(self, media_type):
        if media_type == "audio":
            return Audio()
        elif media_type == "video":
            return Video()
        elif media_type == "photo":
            return Photo()
        else:
            raise ValueError("Invalid media type")

# Приклад використання
factory = MultimediaFactory()

audio = factory.create_media("audio")
print(audio.play())  # Playing audio

video = factory.create_media("video")
print(video.play())  # Playing video

photo = factory.create_media("photo")
print(photo.play())  # Displaying photo
