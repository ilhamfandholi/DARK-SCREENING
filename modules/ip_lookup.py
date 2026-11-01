
import urllib.request
import json

def ip_lookup():
    print("\n=== IP ADDRESS LOOKUP ===")

    target = input("Masukkan IP (kosong = IP sendiri): ").strip()

    if not target:
        url = "https://ipwho.is/"
    else:
        url = f"https://ipwho.is/{target}"

    try:
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "DarkScreening/1.0"}
        )

        with urllib.request.urlopen(request, timeout=10) as response:
            data = json.loads(response.read().decode())

        if not data.get("success"):
            print("IP tidak valid atau data tidak tersedia.")
            return

        print("\n--- SCAN RESULT ---")
        print("IP       :", data.get("ip"))
        print("Country  :", data.get("country"))
        print("City     :", data.get("city"))
        print("Region   :", data.get("region"))
        print("ISP      :", data.get("connection", {}).get("isp"))
        print("Org      :", data.get("connection", {}).get("org"))
        print("Timezone :", data.get("timezone", {}).get("id"))

    except Exception as error:
        print("SCAN ERROR:", error)
