import pytest

from app import main


def test_expiration_day_today_not_outdated(monkeypatch):
    def expiration_day_today_outdated(products: list):
        import datetime
        return [product["name"] for product in products
                if product["expiration_date"] <= datetime.date.today()]

    monkeypatch.setattr(
        main, "outdated_products", expiration_day_today_outdated
    )

    test_result = pytest.main(["app/test_main.py"])
    assert test_result.value == 1, (
        "Product with expiration date equals today is not outdated."
    )
