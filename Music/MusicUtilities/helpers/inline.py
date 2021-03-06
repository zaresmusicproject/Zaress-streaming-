from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    Message,
)
from Music.config import GROUP, CHANNEL


def play_markup(videoid, user_id):
    buttons= [
            [
                InlineKeyboardButton(text="â¨ đđŋđŧđđŊ đ đđđđŽđšđŽđģ", url=f"https://t.me/anonymoustelegrm"),
            ],
            [      
                InlineKeyboardButton(text="âī¸ đđđ§đŽ", callback_data=f'other {videoid}|{user_id}'),
                InlineKeyboardButton(text="đī¸ đđđđđ", callback_data=f'close2')
            ],
        ]
    return buttons 


def others_markup(videoid, user_id):
    buttons= [
            [
                InlineKeyboardButton(text="âļī¸", callback_data=f'resumevc2'),
                InlineKeyboardButton(text="â¸ī¸", callback_data=f'pausevc2'),
                InlineKeyboardButton(text="â­ī¸", callback_data=f'skipvc2'),
                InlineKeyboardButton(text="âšī¸", callback_data=f'stopvc2'),
            ],
            [
                InlineKeyboardButton(text="đ¸ á´á´á´ Ęá´á´Ę ĘÉĒęąá´", callback_data=f'playlist {videoid}|{user_id}'),
                InlineKeyboardButton(text="đ¸ á´á´á´ ÉĸĘá´á´á´ ĘÉĒęąá´", callback_data=f'group_playlist {videoid}|{user_id}')
            ],
            [
                InlineKeyboardButton(text="đŽ Éĸá´á´ á´á´á´ÉĒá´", callback_data=f'gets audio|{videoid}|{user_id}'),
                InlineKeyboardButton(text="đŽ Éĸá´á´ á´ ÉĒá´á´á´", callback_data=f'gets video|{videoid}|{user_id}')
            ],
            [
                InlineKeyboardButton(text="âĒ Back To Button", callback_data=f'goback {videoid}|{user_id}'),
            ],
        ]
    return buttons 




play_keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "âļī¸", callback_data="resumevc"
                    ),
                    InlineKeyboardButton(
                        "â¸ī¸", callback_data="pausevc"
                    ),
                    InlineKeyboardButton(
                        "â­ī¸", callback_data="skipvc"
                    ),
                    InlineKeyboardButton(
                        "âšī¸", callback_data="stopvc"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Close Menu", callback_data="close"
                    )
                ]    
            ]
        )



def audio_markup(videoid, user_id):
    buttons= [
            [
                InlineKeyboardButton(text="âļī¸", callback_data=f'resumevc2'),
                InlineKeyboardButton(text="â¸ī¸", callback_data=f'pausevc2'),
                InlineKeyboardButton(text="â­ī¸", callback_data=f'skipvc2'),
                InlineKeyboardButton(text="âšī¸", callback_data=f'stopvc2')
            ],
            [
                InlineKeyboardButton(text="đ đđĨđ¨đŦđ đđđ§đŽ", callback_data="close2")              
            ],
        ]
    return buttons 


def search_markup(ID1, ID2, ID3, ID4, ID5, duration1, duration2, duration3, duration4, duration5, user_id, query):
    buttons= [
            [
                InlineKeyboardButton(text="1ī¸âŖ", callback_data=f'Music2 {ID1}|{duration1}|{user_id}'),
                InlineKeyboardButton(text="2ī¸âŖ", callback_data=f'Music2 {ID2}|{duration2}|{user_id}'),
                InlineKeyboardButton(text="3ī¸âŖ", callback_data=f'Music2 {ID3}|{duration3}|{user_id}')
            ],
            [ 
                InlineKeyboardButton(text="4ī¸âŖ", callback_data=f'Music2 {ID4}|{duration4}|{user_id}'),
                InlineKeyboardButton(text="5ī¸âŖ", callback_data=f'Music2 {ID5}|{duration5}|{user_id}')
            ],
            [ 
                
                InlineKeyboardButton(text="âŦī¸", callback_data=f'popat 1|{query}|{user_id}'), 
                InlineKeyboardButton(text="ââ", callback_data=f"ppcl2 smex|{user_id}") ,
                InlineKeyboardButton(text="âĄī¸", callback_data=f'popat 1|{query}|{user_id}')             
            ],
        ]
    return buttons   

def search_markup2(ID6, ID7, ID8, ID9, ID10, duration6, duration7, duration8, duration9, duration10 ,user_id, query):
    buttons= [
            [
                InlineKeyboardButton(text="6ī¸âŖ", callback_data=f'Music2 {ID6}|{duration6}|{user_id}'),
                InlineKeyboardButton(text="7ī¸âŖ", callback_data=f'Music2 {ID7}|{duration7}|{user_id}'),
                InlineKeyboardButton(text="8ī¸âŖ", callback_data=f'Music2 {ID8}|{duration8}|{user_id}')
            ],
            [ 
                InlineKeyboardButton(text="9ī¸âŖ", callback_data=f'Music2 {ID9}|{duration9}|{user_id}'),
                InlineKeyboardButton(text="đ", callback_data=f'Music2 {ID10}|{duration10}|{user_id}')
            ],
            [ 
                
                InlineKeyboardButton(text="âŦī¸", callback_data=f'popat 2|{query}|{user_id}'), 
                InlineKeyboardButton(text="â", callback_data=f"ppcl2 smex|{user_id}") ,
                InlineKeyboardButton(text="âĄī¸", callback_data=f'popat 2|{query}|{user_id}')             
            ],
        ]
    return buttons 


def personal_markup(link):
    buttons= [
            [
                InlineKeyboardButton(text="Watch On Youtube", url=f'{link}')
            ],
            [ 
                InlineKeyboardButton(text="đ đđĨđ¨đŦđ", callback_data=f'close2')
            ],
        ]
    return buttons   
  
start_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        "đ Commands", url="https://telegra.ph/Skyzo-11-10"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "đ Close Menu", callback_data="close2"
                    )
                ]    
            ]
        )
    
confirm_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        "Yes", callback_data="cbdel"
                    ),
                    InlineKeyboardButton(
                        "No", callback_data="close2"
                    )
                ]    
            ]
        )

confirm_group_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        "Yes", callback_data="cbgroupdel"
                    ),
                    InlineKeyboardButton(
                        "No", callback_data="close2"
                    )
                ]    
            ]
        )

close_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        "đ đđđđđ", callback_data="close2"
                    )
                ]    
            ]
        )

play_list_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        "Users Playlist", callback_data="P_list"
                    ),
                    InlineKeyboardButton(
                        "Groups Playlist", callback_data="G_list"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "đ đđđđđ", callback_data="close2"
                    )
                ]
            ]
        )

def playlist_markup(user_name, user_id):
    buttons= [
            [
                InlineKeyboardButton(text=f"Groups", callback_data=f'play_playlist {user_id}|group'),
                InlineKeyboardButton(text=f"{user_name[:8]}", callback_data=f'play_playlist {user_id}|personal'),
            ],
            [
                InlineKeyboardButton(text="đ á´Ęá´ęąá´ á´Ęá´ĘĘÉĒęąá´", callback_data="close2")              
            ],
        ]
    return buttons
