"""
initializes the architecture and connects all the components.
it connects the EventBus to the handlers and injects the EventBus into the OrderService.
"""

from event_bus import EventBus
from order_service import OrderService
from events import OrderCreated

from observation.metrics import MetricsCollector
from observation.observer import EventObserver

from handlers.email_handler import (
    send_confirmation_email
)

from handlers.inventory_handler import (
    update_inventory
)

from handlers.shipping_handler import (
    initiate_shipping
)

from handlers.analytics_handler import (
    track_order
)

# 1. Initialize metrics
metrics = MetricsCollector()

# 2. Initialize observer
observer = EventObserver(metrics)

# 3. Initialize Event Bus
event_bus = EventBus(observer)

# 4. Register handlers
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

event_bus.subscribe(
    OrderCreated,
    track_order
)

# 5. Initialize Order Service
order_service = OrderService(event_bus=event_bus)

# 6. Place an order
order_service.create_order(
    order_id=102,
    customer_email="mike.ross@gmail.com",
    product_id=502,
    quantity=4
)

# 7. Display metrics
metrics.display()