from dataclasses import dataclass


@dataclass
class OrderCreated:
    order_id: int
    customer_email: str
    product_id: int
    quantity: int

