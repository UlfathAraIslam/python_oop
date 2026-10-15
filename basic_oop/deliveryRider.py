class Rider:
    def __init__(self, name, deliveries=0):
        self.name = name
        self.deliveries = deliveries

    def pay(self):
        return self.deliveries * 100   # ফ্ল্যাট রেট প্লেসহোল্ডার