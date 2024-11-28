from decimal import Decimal


def check_split(item_total, tax_rate, tip, people):
    """Calculate check value and evenly split.

    :param item_total: str (e.g. '$8.68')
    :param tax_rate: str (e.g. '4.75%)
    :param tip: str (e.g. '10%')
    :param people: int (e.g. 3)

    :return: tuple of (grand_total: str, splits: list)
             e.g. ('$10.00', [3.34, 3.33, 3.33])
    """
    sub_total = Decimal(item_total.strip("$"))
    tax_rate = 1 + Decimal(tax_rate.strip("%")) / 100
    tip_rate = 1 + Decimal(tip.strip("%")) / 100
    post_tax = round(sub_total * tax_rate, 2)
    grand_total = round(post_tax * tip_rate, 2)
    splits = [round(grand_total / people, 2) for _ in range(people)]
    splits[0] += grand_total - sum(splits)
    return f"${grand_total}", splits


if __name__ == "__main__":
    check_split("$186.70", "6.75%", "18%", 6)
    check_split("$191.57", "6.75%", "15%", 6)
