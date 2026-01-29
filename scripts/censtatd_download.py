import os
import json
import requests
import pandas as pd

URL = (
    "https://www.censtatd.gov.hk/api/get.php?id=310-31003&lang=en&param="
    "N4KABGBEDGBukC4yghSBxAIgBQPoGEB5AWW0IDkBRcgFUTAG1xU0AxTSAGmZckw+4s02fJS49UGUeKFQsrfKxlDI+AJIA1ZbwAa6AMrbJxA0bR6zUHYcEqTlyMUMSAuswC+tyAGd4SFJJE5PRMspAASgCGAO64xLgAFgDWACa4KQ4AmgD2mbgAjCkADrgApLjekK4eXkUApgBOAJbZGf4SPgAukQ2d9JAATAAMAwDMQ-lVEJ7MkE1tUKP5QwC0S0NDo8qQADaRAHYA5v11+1XuQA"
)


DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json, text/javascript, */*; q=0.01",
}


def fetch_api(url: str, timeout: int = 20, headers: dict | None = None) -> requests.Response:
    hdrs = DEFAULT_HEADERS.copy()
    if headers:
        hdrs.update(headers)
    resp = requests.get(url, timeout=timeout, headers=hdrs)
    # If server blocks the request, raise_for_status will show 403; caller may catch
    resp.raise_for_status()
    return resp


def save_text(text: str, path: str) -> None:
    with open(path, "w", encoding="utf8") as f:
        f.write(text)


def try_parse_json(text: str):
    try:
        return json.loads(text)
    except Exception:
        return None


def json_to_csv(obj, out_csv_path: str) -> bool:
    # Try common structures: list of dicts, or dict with 'data' key
    df = None
    if isinstance(obj, list):
        if len(obj) > 0 and isinstance(obj[0], dict):
            df = pd.DataFrame(obj)
    elif isinstance(obj, dict):
        # common payloads put the records under a key like 'data' or 'result'
        for k in ("data", "result", "records", "rows"):
            if k in obj and isinstance(obj[k], list):
                df = pd.DataFrame(obj[k])
                break
        # fallback: if values are a dict of lists, convert
        if df is None:
            # try to find a list-of-dicts among dict values
            for v in obj.values():
                if isinstance(v, list) and len(v) > 0 and isinstance(v[0], dict):
                    df = pd.DataFrame(v)
                    break
    if df is None:
        return False
    # write CSV with UTF-8
    df.to_csv(out_csv_path, index=False)
    return True


def main():
    out_dir = os.path.join(os.getcwd(), "data_example")
    os.makedirs(out_dir, exist_ok=True)
    raw_path = os.path.join(out_dir, "censtatd_raw.json")
    pretty_path = os.path.join(out_dir, "censtatd_pretty.json")
    csv_path = os.path.join(out_dir, "censtatd.csv")

    print("Fetching:", URL)
    resp = fetch_api(URL)
    text = resp.text
    save_text(text, raw_path)
    print(f"Saved raw response: {raw_path}")

    obj = try_parse_json(text)
    if obj is not None:
        with open(pretty_path, "w", encoding="utf8") as f:
            json.dump(obj, f, indent=2, ensure_ascii=False)
        print(f"Saved parsed JSON: {pretty_path}")
        converted = json_to_csv(obj, csv_path)
        if converted:
            print(f"Saved CSV: {csv_path}")
        else:
            print("Could not convert JSON to CSV automatically")
    else:
        print("Response is not valid JSON; saved raw text only.")


if __name__ == "__main__":
    main()
