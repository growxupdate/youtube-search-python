import asyncio
from youtubesearchpython.__future__ import *


# ---------- COMMON INPUT HELPERS ----------

def ask(text, default=None):
    if default is not None:
        value = input(f"{text} [{default}]: ").strip()
        return value if value else default
    return input(f"{text}: ").strip()


def ask_int(text, default):
    value = input(f"{text} [{default}]: ").strip()
    return int(value) if value.isdigit() else default


# ---------- TEST FUNCTIONS (ALL FROM YOUR 3 FILES) ----------

async def test_search():
    print("\nInputs needed: query, limit, language, region")
    q = ask("Search query", "NoCopyrightSounds")
    limit = ask_int("Limit", 1)
    lang = ask("Language", "en")
    region = ask("Region", "US")

    search = Search(q, limit=limit, language=lang, region=region)
    print(await search.next())


async def test_videos_search():
    print("\nInputs needed: query, limit, language, region")
    q = ask("Video search query", "NoCopyrightSounds")
    limit = ask_int("Limit", 10)
    lang = ask("Language", "en")
    region = ask("Region", "US")

    search = VideosSearch(q, limit=limit, language=lang, region=region)
    print(await search.next())


async def test_channels_search():
    print("\nInputs needed: query, limit, language, region")
    q = ask("Channel search query", "NoCopyrightSounds")
    limit = ask_int("Limit", 1)
    lang = ask("Language", "en")
    region = ask("Region", "US")

    search = ChannelsSearch(q, limit=limit, language=lang, region=region)
    print(await search.next())


async def test_playlists_search():
    print("\nInputs needed: query, limit, language, region")
    q = ask("Playlist search query", "NoCopyrightSounds")
    limit = ask_int("Limit", 1)
    lang = ask("Language", "en")
    region = ask("Region", "US")

    search = PlaylistsSearch(q, limit=limit, language=lang, region=region)
    print(await search.next())


async def test_custom_search():
    print("\nInputs needed: query, sortOrder, language, region")
    q = ask("Search query", "NoCopyrightSounds")
    lang = ask("Language", "en")
    region = ask("Region", "US")

    search = CustomSearch(q, VideoSortOrder.uploadDate, language=lang, region=region)
    print(await search.next())


async def test_channel_search():
    print("\nInputs needed: query, channelId")
    q = ask("Search query", "Watermelon Sugar")
    cid = ask("Channel ID", "UCZFWPqqPkFlNwIxcpsLOwew")

    search = ChannelSearch(q, cid)
    print(await search.next())


async def test_playlist_get():
    print("\nInputs needed: playlist URL")
    url = ask("Playlist URL", "https://www.youtube.com/playlist?list=PLRBp0Fe2GpgmsW46rJyudVFlY6IYjFBIK")
    print(await Playlist.get(url))


async def test_playlist_info():
    print("\nInputs needed: playlist URL")
    url = ask("Playlist URL", "https://www.youtube.com/playlist?list=PLRBp0Fe2GpgmsW46rJyudVFlY6IYjFBIK")
    print(await Playlist.getInfo(url))


async def test_playlist_videos():
    print("\nInputs needed: playlist URL")
    url = ask("Playlist URL", "https://www.youtube.com/playlist?list=PLRBp0Fe2GpgmsW46rJyudVFlY6IYjFBIK")
    print(await Playlist.getVideos(url))


async def test_suggestions():
    print("\nInputs needed: query")
    q = ask("Suggestion query", "ishq sufiyannaaaa")
    print(await Suggestions.get(q))


async def test_hashtag():
    print("\nInputs needed: hashtag, limit")
    tag = ask("Hashtag (without #)", "ncs")
    limit = ask_int("Limit", 1)

    hashtag = Hashtag(tag, limit=limit)
    print(await hashtag.next())


async def test_video_search_pagination():
    print("\nInputs needed: query, pages")
    q = ask("Search query", "NoCopyrightSounds")
    pages = ask_int("How many pages", 3)

    search = VideosSearch(q)
    index = 0
    for _ in range(pages):
        result = await search.next()
        for v in result["result"]:
            index += 1
            print(f"{index}. {v['title']}")


# ---------- MENU ----------

TESTS = {
    "1": ("Search (mixed)", test_search),
    "2": ("VideosSearch", test_videos_search),
    "3": ("ChannelsSearch", test_channels_search),
    "4": ("PlaylistsSearch", test_playlists_search),
    "5": ("CustomSearch (upload date)", test_custom_search),
    "6": ("ChannelSearch", test_channel_search),
    "7": ("Playlist.get", test_playlist_get),
    "8": ("Playlist.getInfo", test_playlist_info),
    "9": ("Playlist.getVideos", test_playlist_videos),
    "10": ("Suggestions.get", test_suggestions),
    "11": ("Hashtag search", test_hashtag),
    "12": ("VideosSearch pagination demo", test_video_search_pagination),
}


async def main():
    while True:
        print("\n========== YouTube-Search-Python TEST MENU ==========")
        for k, (name, _) in TESTS.items():
            print(f"{k}. {name}")
        print("0. Exit")

        choice = input("\nSelect test number: ").strip()

        if choice == "0":
            break

        test = TESTS.get(choice)
        if not test:
            print("Invalid choice ❌")
            continue

        try:
            print(f"\n▶ Running {test[0]}")
            await test[1]()
        except Exception as e:
            print("\n❌ ERROR:", e)

        print("\n-------------------------------------------")


if __name__ == "__main__":
    asyncio.run(main())
