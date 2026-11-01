import os
from datetime import datetime


def generate_report():
    print("\n===== DARK SCREENING REPORT GENERATOR =====")

    title = input("Judul laporan: ").strip()

    if not title:
        title = "Untitled Report"

    print("\nMasukkan isi laporan.")
    print("Ketik END pada baris baru untuk selesai.\n")

    lines = []

    while True:
        line = input()

        if line.upper() == "END":
            break

        lines.append(line)

    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"report_{timestamp}.txt"
    filepath = os.path.join(output_folder, filename)

    with open(filepath, "w", encoding="utf-8") as file:
        file.write("====================================\n")
        file.write("         DARK SCREENING\n")
        file.write("          SCAN REPORT\n")
        file.write("====================================\n\n")

        file.write(f"Judul   : {title}\n")
        file.write(f"Tanggal : {datetime.now()}\n\n")

        file.write("HASIL LAPORAN:\n")
        file.write("------------------------------------\n")

        for line in lines:
            file.write(line + "\n")

        file.write("\n====================================\n")
        file.write("       END OF REPORT\n")
        file.write("====================================\n")

    print("\n[+] REPORT BERHASIL DISIMPAN!")
    print(f"[+] Lokasi: {filepath}")