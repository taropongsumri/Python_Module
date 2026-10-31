#! /bin/python3
import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    inv: dict[str, int] = {}

    for arg in args:
        parts = arg.split(":")

        if len(parts) != 2 or parts[0] == "":
            print(f"Error - invalid parameter '{arg}'")
            continue

        name = parts[0]
        if name in inv:
            print(f"Redundant item '{name}' - discarding")
            continue

        try:
            qty = int(parts[1])
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")
            continue

        if qty < 0:
            print(f"Quantity error for '{name}': negative quantity {qty}")
            continue

        inv.update({name: qty})
    return inv


def main() -> None:
    print("=== Inventory System Analysis ===")
    inv = parse_inventory(sys.argv[1:])

    print(f"Got inventory: {inv}")
    items = list(inv.keys())
    print(f"Item list: {items}")

    total = sum(inv.values())
    print(f"Total quantity of the {len(items)} items: {total}")

    if total > 0:
        for name in items:
            percent = round(inv[name] / total * 100, 1)
            print(f"Item {name} represents {percent}%")

    if len(items) > 0:
        most = items[0]
        least = items[0]
        for name in items:
            if inv[name] > inv[most]:
                most = name
            if inv[name] < inv[least]:
                least = name
        print(f"Item most abundant: {most} with quantity {inv[most]}")
        print(f"Item least abundant: {least} with quantity {inv[least]}")

    inv.update({"magic_item": 1})
    print(f"Updated inventory: {inv}")


if __name__ == "__main__":
    main()
