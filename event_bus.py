from collections import defaultdict


class EventBus:
    """
    publishes and distributes events
    """
    def __init__(self):
        self.handlers = defaultdict(list)

    def subscribe(self, event_type, handler):
        self.handlers[event_type].append(handler)

    def publish(self, event):
        event_type = type(event)

        for handler in self.handlers[event_type]:
            handler(event)
