def initiate_shipping(event):

    print(
        f"[SHIPPING] Preparing shipment "
        f"for order {event.order_id}"
    )
