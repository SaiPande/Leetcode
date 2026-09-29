class Logger:

    def __init__(self):
        self.freq = {}
        #self.output = []


    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.freq:
            currval = self.freq[message]
            if currval > timestamp:
                return False
            else:
                self.freq[message] = timestamp+10
                return True
        else:
            self.freq[message] = timestamp+10
            return True



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)