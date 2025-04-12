def route_message(self, text):
    if not any(self.categories.values()):
        return ['uncategorized']  # Safety net