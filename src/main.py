from metagpt.roles import Role
from metagpt.team import Team

# 导入自定义角色
# from roles.your_custom_role import YourCustomRole

def main():
    # 创建团队
    team = Team()
    
    # 添加角色到团队
    # team.hire([YourCustomRole()])
    
    # 开始项目
    team.run()

if __name__ == "__main__":
    main()
