from metagpt.roles import Role

class CustomRole(Role):
    def __init__(self, name="CustomRole", profile="A custom role for specific tasks"):
        super().__init__(name, profile)
    
    async def run(self):
        # 实现角色的具体行为
        pass
