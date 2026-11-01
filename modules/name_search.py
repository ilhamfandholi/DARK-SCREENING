
from urllib.parse import quote_plus
import webbrowser


def name_search():
    print("\n=== DARK NAME SEARCH ===")

    name = input("Masukkan nama: ").strip()

    if not name:
        print("Nama tidak boleh kosong!")
        return

    query = quote_plus('"' + name + '"')

    searches = {
        "Google": f"https://www.google.com/search?q={query}",
        "Bing": f"https://www.bing.com/search?q={query}",
        "DuckDuckGo": f"https://duckduckgo.com/?q={query}",
        "Google News": f"https://www.google.com/search?tbm=nws&q={query}",
    }

    print("\n--- SEARCH RESULTS ---")

    for number, (site, url) in enumerate(searches.items(), 1):
        print(f"\n[{number}] {site}")
        print(url)

    choice = input(
        "\nBuka semua pencarian di browser? (y/n): "
    ).strip().lower()

    if choice == "y":
        for url in searches.values():
            webbrowser.open_new_tab(url)

        print("\nBrowser berhasil dibuka!")
    else:
        print("\nPencarian dibatalkan.")
