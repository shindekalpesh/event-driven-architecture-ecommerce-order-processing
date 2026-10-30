E-commerce order processing using Event-driven Architecture.

## 1. Requirement Gathering:
### Functional Requirements:
- FR1 : Customer should be able to place an order.
- FR2 : System should save the order
- FR3 : System should publish an `OrderCreated` event.
- FR4 : Email handler should receive the event.
- FR5 : Inventory handler should receive the event.
- FR6 : Shipping handler should receive the event.

### Non-Functional Requirements:
- NFR1 : Loose coupling : Order Service should not know about the individual handlers.
- NFR2 : Extensibility : We should be able to add new handlers easily.
- NFR3 : Maintainability : Event publishing and event handling should be separate.
- NFR4 : Reliability : A failure in one handler should not prevent other handlers from eecuting.

## Folder strucutre:

```text
event-driven-architecture-ecommerce-order-processing/
│
├── main.py
├── events.py
├── event_bus.py
├── order_service.py
│
├── handlers/
│   ├── __init__.py
│   ├── email_handler.py
│   ├── inventory_handler.py
│   └── shipping_handler.py
│
└── README.md
```