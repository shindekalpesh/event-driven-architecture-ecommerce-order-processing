def update_inventory(event):

    print(
        f"[INVENTORY] Updating stock for"
        f"product{event.product_id}"
    )

    print(
        f"[INVENTORY] Reduced stock by "
        f"{event.quantity}"
    )