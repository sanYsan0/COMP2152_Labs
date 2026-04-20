# ============================================================
#  WEEK 14 LAB — Q2: HTTP SECURITY HEADER CHECKER
#  COMP2152 — Sanyoung Yoon
# ============================================================

import urllib.request


# Security headers every website should have
REQUIRED_HEADERS = {
    "Content-Type":              "Defines the content format",
    "X-Frame-Options":           "Vulnerable to clickjacking",
    "X-Content-Type-Options":    "Vulnerable to MIME sniffing",
    "Strict-Transport-Security": "No HTTPS enforcement",
    "Content-Security-Policy":   "No XSS protection policy",
    "X-XSS-Protection":         "No XSS filter",
}


# TODO: Complete check_headers(url)
#   Make a request to url using urllib.request.urlopen
#   Get response headers: dict(response.headers)
#   For each header in REQUIRED_HEADERS:
#     If the header exists in response → append {"header": name, "present": True, "value": value}
#     If missing → append {"header": name, "present": False, "value": "MISSING"}
#   Return the list
#   If the request fails, return an empty list
def check_headers(url):
    response = urllib.request.urlopen(url)
    headers = dict(response.headers)

    results = {}

    for header in REQUIRED_HEADERS:
        if header in headers:
            results[header] = ("present", headers[header])
        else:
            results[header] = ("missing", REQUIRED_HEADERS[header])

    return results


# TODO: Complete generate_report(url, results)
#   Print the URL
#   missing_count = 0
#   For each result:
#     If present: print f"  ✓ {header}: {value}"
#     If missing: print f"  ✗ {header}: MISSING — {REQUIRED_HEADERS[header]}"
#       Increment missing_count
#   Print f"  Missing {missing_count} of {len(results)} security headers!"
def generate_report(url, results):
    print("\n" + "="*50)
    print(f"Checking: {url}")
    print("="*50)

    for header, (status, info) in results.items():
        if status == "present":
            print(f"  ✓ {header}: {info}")
        else:
            print(f"  ✗ {header}: MISSING — {info}")

if __name__ == "__name__":
    urls = [
        "http://example.com",
        "http://httpbin.org/get"
    ]

    for url in urls:
        results = check_headers(url)
        generate_report(url, results)


# --- Main (provided) ---
if __name__ == "__main__":
    print("=" * 60)
    print("  Q2: HTTP SECURITY HEADER CHECKER")
    print("=" * 60)

    urls = [
        "http://httpbin.org",
        "https://www.google.com",
    ]

    for url in urls:
        print(f"\n--- Checking {url} ---")
        results = check_headers(url)
        if results:
            generate_report(url, results)
        else:
            print("  (could not connect or not implemented)")

    print("\n" + "=" * 60)