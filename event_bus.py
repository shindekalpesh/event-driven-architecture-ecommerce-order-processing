from collections import defaultdict


class EventBus:
    """
    publishes and distributes events
    """
    def __init__(self, observer):
        self.handlers = {}
        self.observer = observer

    def subscribe(self, event_type, handler):
        self.handlers.setdefault(
            event_type, []
        ).append(handler)

    def publish(self, event):
        event_type = type(event)

        self.observer.event_published(event)

        for handler in self.handlers.get(
            event_type, []
        ):
            start_time = self.observer.handler_started(
                event, handler
            )

            try:
                handler(event)

                self.observer.handler_completed(event, handler, start_time)

            except Exception as error:

                self.observer.handler_failed(event, handler, error)

                # Continue processing other handlers
                continue
            
