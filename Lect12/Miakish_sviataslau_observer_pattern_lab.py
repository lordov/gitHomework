class Publisher:
    _observers = []
    def subscribe(self, observer):
        self._observers.append(observer)

    def notify_subscribers(self) -> None:
        for observer in self._observers:
            observer.update(self)
    
    def add_new_video(self) -> None:
        self.value = 2
        self.notify_subscribers()


class ObserverA:
    def update(self, product):
        if product.value  < 3:
            print("ObserverA: Reacted to the event")


class ObserverB:
    def update(self, product):
        if product.value  < 3:
            print("ObserverB: Reacted to the event")

publisher = Publisher()
print()
observer_a = ObserverA()
publisher.subscribe(observer_a)
publisher.add_new_video()
print()
observer_b = ObserverB()
publisher.subscribe(observer_b)
publisher.add_new_video()