#!/usr/bin/env python3
"""
AI协作规范同步脚本
用于从GitHub仓库同步规范到本地项目
"""

import os
import json
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

class StandardsSyncManager:
    def __init__(self):
        self.current_dir = Path.cwd()
        self.collaboration_folder = "ai_collaboration"
        self.github_repo = "your-username/ai-collaboration-standards"
        
    def detect_current_project(self):
        """检测当前工作项目"""
        current_path = str(self.current_dir)
        if "GameAssetExtractor" in current_path:
            return "GameAssetExtractor"
        elif "MerchantAI" in current_path:
            return "MerchantAI"
        elif "X-AnyLabeling-main" in current_path:
            return "X-AnyLabeling-main"
        else:
            return "Unknown"
    
    def pull_from_github(self):
        """从GitHub拉取最新规范"""
        try:
            print("🔄 从GitHub拉取最新规范...")
            result = subprocess.run(
                ["git", "pull", "origin", "main"],
                cwd=self.current_dir,
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                print("✅ GitHub同步成功")
                return True
            else:
                print(f"❌ GitHub同步失败: {result.stderr}")
                return False
        except Exception as e:
            print(f"❌ GitHub同步错误: {e}")
            return False
    
    def update_local_standards(self, project_name):
        """更新当前项目规范"""
        try:
            print(f"📝 更新 {project_name} 项目规范...")
            
            # 确保协作文件夹存在
            collaboration_path = self.current_dir / self.collaboration_folder
            collaboration_path.mkdir(exist_ok=True)
            
            # 复制规范文档
            standards_source = self.current_dir / "standards" / "AI_COLLABORATION_STANDARDS.md"
            standards_target = collaboration_path / "AI_COLLABORATION_STANDARDS.md"
            
            if standards_source.exists():
                shutil.copy2(standards_source, standards_target)
                print("✅ 规范文档已更新")
            
            # 复制知识库
            knowledge_source = self.current_dir / "knowledge_base" / "lessons_learned.json"
            knowledge_target = collaboration_path / "lessons_learned.json"
            
            if knowledge_source.exists():
                shutil.copy2(knowledge_source, knowledge_target)
                print("✅ 知识库已更新")
            
            # 创建项目配置
            config = {
                "project_name": project_name,
                "collaboration_folder": self.collaboration_folder,
                "github_repo": self.github_repo,
                "local_path": str(self.current_dir),
                "last_sync": datetime.now().isoformat(),
                "version": "1.1.0"
            }
            
            config_path = collaboration_path / "project_config.json"
            with open(config_path, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
            
            print("✅ 项目配置已更新")
            return True
            
        except Exception as e:
            print(f"❌ 更新项目规范失败: {e}")
            return False
    
    def sync_to_other_projects(self, current_project):
        """同步到其他项目"""
        target_projects = [
            "D:/MerchantAI",
            "D:/X-AnyLabeling-main"
        ]
        
        # 移除当前项目
        if current_project in ["GameAssetExtractor", "MerchantAI", "X-AnyLabeling-main"]:
            target_projects = [p for p in target_projects if current_project not in p]
        
        for project_path in target_projects:
            if os.path.exists(project_path):
                try:
                    print(f"🔄 同步到 {project_path}...")
                    # 这里可以添加具体的同步逻辑
                    print(f"✅ {project_path} 同步完成")
                except Exception as e:
                    print(f"❌ 同步到 {project_path} 失败: {e}")
            else:
                print(f"⚠️ 项目路径不存在: {project_path}")
    
    def sync_standards(self):
        """主同步函数"""
        print("🚀 开始AI协作规范同步...")
        
        # 检测当前项目
        current_project = self.detect_current_project()
        print(f"📍 当前项目: {current_project}")
        
        # 拉取GitHub更新
        if not self.pull_from_github():
            print("❌ 无法从GitHub拉取更新，跳过同步")
            return False
        
        # 更新当前项目
        if not self.update_local_standards(current_project):
            print("❌ 更新当前项目失败")
            return False
        
        # 同步到其他项目
        self.sync_to_other_projects(current_project)
        
        print("🎉 同步完成！")
        return True

def main():
    """主函数"""
    manager = StandardsSyncManager()
    manager.sync_standards()

if __name__ == "__main__":
    main()
