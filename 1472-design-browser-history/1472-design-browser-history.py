class BrowserHistory:

    def __init__(self, homepage: str):
        self.f=[homepage]
        self.x=0

    def visit(self, url: str) -> None:
        self.f=self.f[:self.x+1]
        self.f.append(url)
        self.x+=1


    def back(self, steps: int) -> str:
        self.x=max(0,self.x-steps)
        return self.f[self.x]

    def forward(self, steps: int) -> str:
        self.x=min(len(self.f)-1,self.x+steps)
        return self.f[self.x]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)