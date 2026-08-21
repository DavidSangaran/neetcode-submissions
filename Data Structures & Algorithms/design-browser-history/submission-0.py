class Page:
    def __init__(self, homepage: str):
        self.next = None
        self.prev = None
        self.homepage = homepage

class BrowserHistory:
    COUNT = 0
    def __init__(self, homepage: str):
        self.head = Page("dummyhead")
        self.tail = Page("dummytail")
        self.currPos = self.head
        self.visit(homepage)

    def visit(self, url: str) -> None:
        getPos = self.currPos
        newPage = Page(url)
        newPage.prev = getPos
        newPage.next = self.tail
        getPos.next = newPage
        self.currPos = newPage

    def back(self, steps: int) -> str:
        getPos = self.currPos.prev
        i = 0
        while getPos.prev and i < steps:
            self.currPos = getPos
            getPos = getPos.prev
            i+=1
        return self.currPos.homepage

    def forward(self, steps: int) -> str:
        getPos = self.currPos.next
        i = 0
        while getPos.next and i < steps:
            self.currPos = getPos
            getPos = getPos.next
            i+=1
        return self.currPos.homepage

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)