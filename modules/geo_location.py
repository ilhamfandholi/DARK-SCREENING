
import urllib.request
import json


def geo_location():
    print("\n=== GEO LOCATION SCANNER ===")

    target = input("Masukkan IP: ").strip()

    if not target:
        print("IP tidak boleh kosong!")
        return

    url = f"https://ipwho.is/{target}"

    try:
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "DarkScreening/1.0"}
        )

        with urllib.request.urlopen(request, timeout=10) as response:
            data = json.loads(response.read().decode())

        if not data.get("success"):
            print("Lokasi tidak ditemukan!")
            return

        print("\n--- GEO LOCATION RESULT ---")
        print("IP        :", data.get("ip"))
        print("Country   :", data.get("country"))
        print("City      :", data.get("city"))
        print("Region    :", data.get("region"))
        print("Latitude  :", data.get("latitude"))
        print("Longitude :", data.get("longitude"))
        print("Timezone  :", data.get("timezone", {}).get("id"))

        latitude = data.get("latitude")
        longitude = data.get("longitude")

        print("\nMAP:")
        print(f"https://www.google.com/maps?q={latitude},{longitude}")

    except Exception as error:
        print("SCAN ERROR:", error)
