from time import perf_counter

from observation.logger import get_logger


class EventObserver:

    def __init__(self, metrics):
        self.logger = get_logger("EventObserver")
        self.metrics = metrics

    def event_published(self, event):
        event_name = type(event).__name__

        self.logger.info(
            f"Event published: {event_name}"
        )

        self.metrics.increment(
            f"events.punlished.{event_name}"
        )

    def handler_started(self, event, handler):

        event_name = type(event).__name__
        handler_name = handler.__name__

        self.logger.info(
            f"Handler started: {handler_name}"
        )

        self.metrics.increment(
            f"handlers.started.{handler_name}"
        )

        return perf_counter()

    def handler_completed(self, event, handler, start_time):

        duration = perf_counter() - start_time

        handler_name = handler.__name__

        self.logger.info(
            f"Handler completed: {handler_name} "
            f"in {duration:.6f}s"
        )

        self.metrics.increment(
            f"handlers.completed.{handler_name}"
        )

        self.metrics.record_time(
            f"handler.duration.{handler_name}",
            duration
        )

    def handler_failed(self, event, handler, error):

        handler_name = handler.__name__

        self.logger.error(
            f"Handler failed: {handler_name} | "
            f"Error: {error}"
        )

        self.metrics.increment(
            f"handlers.failed.{handler_name}"
        )