from metagpt.actions import Action

class ExampleTask(Action):
    def __init__(self):
        super().__init__()
    
    async def run(self):
        # 实现任务的具体逻辑
        pass
