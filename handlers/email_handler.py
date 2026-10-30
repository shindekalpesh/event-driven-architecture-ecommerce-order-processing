def send_confirmation_email(event):

    print(
        f"[EMAIL] Sending confirmation to"
        f"{event.customer_eamail}"
    )

    print(
        f"[EMAIL] Order {event.order_id} confirmed."
    )