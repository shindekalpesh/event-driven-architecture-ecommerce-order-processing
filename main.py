"""
initializes the architecture and connects all the components.
it connects the EventBus to the handlers and injects the EventBus into the OrderService.
"""

from event_bus import EventBus
from order_service import OrderService
from events import OrderCreated

from handlers.email_handler import (
    send_confirmation_email
)

from handlers.inventory_handler import (
    update_inventory
)

from handlers.shipping_handler import (
    initiate_shipping
)

# 1. Create Event Bus
event_bus = EventBus()

# 2. Register Event Subscribers
event_bus.subscribe(
    OrderCreated,
    send_confirmation_email
)

event_bus.subscribe(
    OrderCreated,
    update_inventory
)

event_bus.subscribe(
    OrderCreated,
    initiate_shipping
)

# 3. Create Order Service
order_service = OrderService(event_bus=event_bus)

# 4. Place an order
order_service.create_order(
    order_id=101,
    customer_email="harvey.specter@gmail.com",
    product_id=501,
    quantity=2
)