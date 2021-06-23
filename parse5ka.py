from pathlib import Path
import json
import time
import requests


class Parse5ka:
    headers = {"User-Agent": "AZ"}

    def __init__(self, start_url: str, save_dir: Path):
        self.start_url = start_url
        self.save_dir = save_dir

    def _get_response(self, url: str) -> requests.Response:
        while True:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                return response
            time.sleep(0.2)

    def run(self):
        for product in self._parse(self.start_url):
            file_name = f"{product['id']}.json"
            file_path = self.save_dir.joinpath(file_name)
            self._save(product, file_path)

    def _parse(self, url):
        while url:
            response = self._get_response(url)
            data = response.json()
            url = data["next"]
            for product in data["results"]:
                yield product

    def _save(self, data: dict, file_path: Path):
        file_path.write_text(json.dumps(data, ensure_ascii=False))


class CatParser(Parse5ka):

    def __init__(self, cat_url, *args, **kwargs):
        self.cat_url = cat_url
        super().__init__(*args, **kwargs)

    def _get_cat(self):
        response = self._get_response(self.cat_url)
        data = response.json()
        return data

    def run(self):
        for cat in self._get_cat():
            cat["products"] = []
            params = f"?categories={cat['parent_group_code']}"
            url = f"{self.start_url}{params}"

            cat["products"].extend(list(self._parse(url)))
            file_name = f"{cat['parent_group_code']}.json"
            cat_path = self.save_dir.joinpath(file_name)
            self._save(cat, cat_path)


def get_dir_path(dir_name: str) -> Path:
    dir_path = Path(__file__).parent.joinpath(dir_name)
    if not dir_path.exists():
        dir_path.mkdir()
    return dir_path


if __name__ == "__main__":
    url = "https://5ka.ru/api/v2/special_offers/"
    cat_url = "https://5ka.ru/api/v2/categories/"
    product_path = get_dir_path("products")
    parser = Parse5ka(url, product_path)
    cat_parser = CatParser(cat_url, url, get_dir_path("cat_products"))
    cat_parser.run()
