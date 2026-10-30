from events import OrderCreated

class OrderService:
    """
    The Order Seervice:
    1. Creates an order.
    2. Simulates saving it.
    3. Creates an 'OrderCreated' event.
    4. Publishes that event.
    """
    def __init__(self, event_bus):
        self.event_bus = event_bus

    def create_order(
            self,
            order_id,
            customer_email,
            product_id,
            quantity
    ):
        # Step 1: Create the order
        print(f"[ORDER] Creating order: {order_id}")

        # Step 2: Simulate saving the order
        print(f"[ORDER] Saving order: {order_id}")

        # Step 3: Simulate saving the order
        event = OrderCreated(
            order_id=order_id,
            customer_email=customer_email,
            product_id=product_id,
            quantity=quantity
        )

        # Step 4: Publiush the event
        self.event_bus.publish(event)

        print(f"[ORDER] Order processing completed.")
