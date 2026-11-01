
import dns.resolver


def dns_scanner():
    print("\n=== DARK DNS SCANNER ===")

    domain = input("Masukkan domain (contoh google.com): ").strip()

    if not domain:
        print("Domain tidak boleh kosong!")
        return

    records = ["A", "AAAA", "MX", "NS", "TXT"]

    for record in records:
        print(f"\n--- {record} RECORD ---")

        try:
            answers = dns.resolver.resolve(domain, record)

            for answer in answers:
                print(answer)

        except dns.resolver.NoAnswer:
            print("Tidak ada record.")

        except dns.resolver.NXDOMAIN:
            print("Domain tidak ditemukan!")
            break

        except dns.resolver.NoNameservers:
            print("Nameserver tidak merespons.")

        except Exception as error:
            print("ERROR:", error)
