class StockSpanner:
    
    def __init__(self):
        self.stack = []

    """
    This method is used to retrieve the span of a price.
    It utilises a stack to track the previous value and span.

    Values are popped until the current price is lower than
    the highest value in the stack or the stack is exhausted.

    Popped values are added to obtain current span.
    """
    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span
