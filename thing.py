song_list = [
    "STORY - Sam Tsui | SK-II MUSIC VIDEO",
    "Avicii - Wake Me Up (Lyric Video)",
    "Starley - Call On Me (Ryan Riback Remix) [Official Video]",
    "Conor Maynard - Turn Around ft. Ne-Yo (Official Video)",
    "Max Parker - Out of the Blue (Official Audio)",
    "Mondays - If I Was Your Girlfriend (ft. Lucy)",
    "Mondays feat. Lilla My - I'm Over You",
    "Zedd - Find You ft. Matthew Koma, Miriam Bryant (Official Music Video)",
    "Clean Bandit - Rockabye (feat. Sean Paul & Anne-Marie) [Official Video]",
    "Hailee Steinfeld & Alesso  - Let Me Go (Lyrics) ft Florida Georgia Line & watt",
    "PENTATONIX - The Sound Of Silence [Audio]",
    "Who I'm Meant To Be - Lyric Video | Anthem Lights",
    "Victorious Cast - Make It In America (Official Video) ft. Victoria Justice",
    "PENTATONIX - SING (LYRICS)",
    "Shawn Mendes - If I Can't Have You",
    "Castle On The Hill - Ed Sheeran (Lyrics)",
    "Hedley - Kiss You Inside Out (Lyric Video)",
    "Avicii - The Nights",
    "Turn Up the Music",
    "Shawn Mendes, Camila Cabello - Señorita (Lyrics)",
    "Chawki - Time Of Our Lives (Lyrics)",
    "Yeah 3x  - Chris Brown (Lyrics!)",
    "Holiday - Jason Chen (lyrics)",
    "Jason Chen - Still in Love (Lyrics)",
    "Ed Sheeran - Beautiful People (feat. Khalid) [Official Lyric Video]",
    "Lewis Capaldi - Someone You Loved (Lyrics)",
    "Dan + Shay, Justin Bieber - 10,000 Hours (LYRICS)",
    "Heffron Drive - One Way Ticket (Official Music Video)",
    "The Wanted - Chasing The Sun (Official Lyric Video)",
    "Sigrid - Don’t Feel Like Crying (Lyrics)",
    "Metric - Breathing Underwater Lyrics",
    "K-391, Alan Walker & Ahrix - End Of Time (Lyrics)",
    "The Weeknd - Blinding Lights (Official Audio)",
    "Alesso - REMEDY (Lyrics) ft. Conor Maynard",
    "Alesso, Tove Lo - Heroes (Lyrics) we could be",
    '"Smile For The Camera" - Jason Chen | Lyric Video',
    "Fool For You - Sam Tsui & Casey Breves",
    "Kygo, OneRepublic - Lose Somebody (Audio)",
    "Alan Walker - Heading Home (Lyrics) feat. Ruben",
    "Kygo - Stranger Things ft. OneRepublic (Official Audio)",
    "TheFatRat & Laura Brehm - We'll Meet Again",
    "Walk Off The Earth - I'll Be There (Lyrics)",
    "Sigala, Becky Hill - Wish You Well (Official Video)",
    "Becky Hill & Sigala - Heaven on My Mind (Official Audio)",
    "Kygo - Happy Now ft. Sandro Cavazza (Official Video)",
    "Becky Hill - Better Off Without You",
    "Becky Hill, WEISS - I Could Get Used To This (Lyrics)",
    "Alx Veliz - Dancing Kizomba (English Lyric Video)",
    "Becky Hill - Space (Official Video)",
]


def filter_titles(song_list):
    split_chars = ["(", "|", "[", "."]
    for char in split_chars:
        i = 0
        for song in song_list:
            song_list[i] = song.split(char)[0]
            i = i + 1
    replace_words = [
        "Lyrics",
        "lyrics",
        "LYRICS",
        "Lyric",
        "lyric",
        "LYRIC",
        "VIDEO",
        "video",
        "Video",
        "ft",
        "feat",
    ]
    for word in replace_words:
        i = 0
        for song in song_list:
            song_list[i] = song.replace(word, "")
            i = i + 1
    return song_list


filter_titles(song_list)
for song in song_list:
    print(song)