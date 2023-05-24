from aiogram import Bot
from aiogram.types import Message, FSInputFile, InputMediaVideo, InputMediaPhoto
from aiogram.utils.chat_action import ChatActionSender


async def get_audio(message: Message, bot: Bot):
    audio = FSInputFile('./resources/audio.mp3', filename='Audiosample.mp3')
    await bot.send_audio(message.from_user.id, audio=audio)


async def get_document(message: Message, bot: Bot):
    document = FSInputFile('./resources/document.txt', filename='Sample.txt')
    await bot.send_document(message.from_user.id, document=document, caption="Document caption")


async def get_media_group(message: Message, bot: Bot):
    """
    Cant group: photo + video + audio, photo + video + audio + document
    IF Set caption to single file it will be caption for whole group
    """
    image1 = InputMediaPhoto(type="photo", media=FSInputFile('./resources/img1.jpg'), caption='Photo 1 caption')
    image2 = InputMediaPhoto(type="photo", media=FSInputFile('./resources/img2.jpg'))
    video = InputMediaVideo(type="video", media=FSInputFile('./resources/video.mp4'))
    media = [image1, image2, video]
    await bot.send_media_group(message.from_user.id, media=media)


async def get_photo(message: Message, bot: Bot):
    image1 = FSInputFile('./resources/img1.jpg')
    await bot.send_photo(message.from_user.id, image1)


async def get_sticker(message: Message, bot: Bot):
    """
    Send FSInputFile('./resources/img1.png') file OR sticker id
    :param message:
    :param bot:
    :return:
    """
    sticker_id = "CAACAgIAAxkBAAIDkWRtlxvRWjc3DXdZBxeMDRZINF4DAAJHAgACx2NcFRNSzC5KeQxoLwQ"
    await bot.send_sticker(message.from_user.id, sticker=sticker_id)


async def get_video(message: Message, bot: Bot):
    async with ChatActionSender.upload_video(chat_id=message.from_user.id):
        video = FSInputFile('./resources/video.mp4')
        await bot.send_video(message.from_user.id, video)


async def get_video_note(message: Message, bot: Bot):
    """
    Issue - Does mot sending notes
    """
    async with ChatActionSender.upload_video(chat_id=message.from_user.id):
        video_note = FSInputFile('./resources/video1to1_3.mp4')
        await bot.send_video_note(message.from_user.id, video_note)


async def get_voice(message: Message, bot: Bot):
    async with ChatActionSender.upload_voice(chat_id=message.from_user.id):
        voice = FSInputFile('./resources/audio.ogg')
        await bot.send_voice(message.from_user.id, voice)
