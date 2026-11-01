import webbrowser
from urllib.parse import quote


def username_search():
    print("\n===== PUBLIC USERNAME SEARCH =====")

    username = input("Masukkan username: ").strip()

    if not username:
        print("Username tidak boleh kosong!")
        return

    user = quote(username, safe="")
    query = quote(username)

    links = {
        "GitHub": f"https://github.com/{user}",
        "Reddit": f"https://www.reddit.com/search/?q={query}",
        "Instagram": f"https://www.instagram.com/{user}/",
        "TikTok": f"https://www.tiktok.com/@{user}",
        "YouTube": f"https://www.youtube.com/results?search_query={query}",
        "X (Twitter)": f"https://x.com/search?q={query}",
        "Google": f"https://www.google.com/search?q={query}"
    }

    print("\nHASIL PENCARIAN LINK:\n")

    for platform, url in links.items():
        print(f"[+] {platform}: {url}")

    print("\nLink ini hanya pintasan pencarian profil publik.")
    print("Tidak menjamin akun tersebut benar-benar ada.")

    open_browser = input("\nBuka semua link di browser? (y/n): ").lower()

    if open_browser == "y":
        for url in links.values():
            webbrowser.open_new_tab(url)

        print("\nBrowser berhasil dibuka!")

    else:
        print("\nPencarian selesai.")