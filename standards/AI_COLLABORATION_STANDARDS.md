# AI协作规范标准 v1.1

## 📋 核心原则

### 1. 验证优先机制
```
需求理解 → 方案确认 → 分步执行 → 效果验证
```
- 重要决策前必须确认理解
- 复杂任务分步骤执行
- 每步都验证效果

### 2. 透明化决策
- 说明技术原理和前提条件
- 提示可能的风险和后果
- 提供替代方案选择

### 3. 知识边界识别
- 明确技术假设
- 识别不确定因素
- 建立回退机制

### 4. 项目结构规范
**重要原则：我不喜欢什么不明确的东西都往根目录放，这样显得很乱**

**文件组织原则：**
- 所有协作相关文件必须放在专门的文件夹中
- 避免在项目根目录放置临时或测试文件
- 保持项目结构清晰，便于维护和版本控制
- 新增功能模块必须有独立的目录结构

**标准目录结构：**
```
项目根目录/
├── ai_collaboration/          # AI协作相关文件
│   ├── sync_standards.py     # 同步脚本
│   ├── AI_COLLABORATION_STANDARDS.md  # 规范文档
│   ├── project_config.json   # 项目配置
│   └── sync_logs/            # 同步日志
├── src/                      # 源代码
├── docs/                     # 文档
├── tools/                    # 工具脚本
└── configs/                  # 配置文件
```

## 🎯 具体协作规范

### 技术决策流程
1. **需求确认**：理解你的真实需求
2. **方案设计**：基于技术原理设计方案
3. **风险评估**：说明可能的问题和后果
4. **分步实施**：复杂任务分解执行
5. **效果验证**：确认达到预期目标

### 沟通规范
- 直接回答核心问题
- 避免过度工程化验证
- 平衡详细分析与简洁回答
- 预估执行时间并告知

## 📚 经验教训库

### 已解决的问题
1. **类别映射陷阱**
   - 问题：X-AnyLabeling内部映射与配置文件不一致
   - 解决：严格对应background(0), monster(1), npc(2)
   - 教训：GUI工具映射必须与配置文件完全一致

2. **数据集结构混乱**
   - 问题：图像和标注文件混合
   - 解决：严格分离labels(只放.txt)和images(只放图像)
   - 教训：必须严格按照标准组织数据结构

3. **检测阈值重要性**
   - 问题：高阈值隐藏模型真实能力
   - 解决：多阈值测试(0.3→0.1提升NPC检测率0%→60%)
   - 教训：不要被单一测试结果误导

4. **上下文消耗管理**
   - 问题：过度工程化回答
   - 解决：直接回答核心问题，避免复杂验证
   - 教训：简洁回答与详细分析需要平衡

5. **项目结构混乱**
   - 问题：各种文件随意放在根目录
   - 解决：建立专门的文件夹存放特定类型文件
   - 教训：保持项目结构清晰是长期维护的基础

### 避免重复踩坑检查清单
- [ ] 验证类别映射一致性
- [ ] 检查数据集结构标准性
- [ ] 使用多阈值测试模型
- [ ] 手动验证检测准确性
- [ ] 直接回答核心问题
- [ ] 检查项目结构规范性

## 🔄 版本管理

### 当前版本：v1.1
- 创建日期：2025-09-25
- 基于：GameAssetExtractor项目经验
- 状态：已验证有效

### 更新记录
- v1.0：建立基础协作规范
- v1.1：添加项目结构规范和GitHub同步方案
- 后续版本将记录新的经验教训

## 📈 应用范围

### 适用项目类型
- AI模型训练项目
- 数据处理项目
- 工具开发项目
- 自动化脚本项目

### 适用场景
- 技术方案设计
- 问题排查解决
- 经验知识传递
- 协作效率提升

## 🎯 使用指南

### 新项目启动时
1. 复制此规范到项目ai_collaboration目录
2. 根据项目特点调整规范
3. 建立项目特定的检查清单

### 遇到问题时
1. 查阅经验教训库
2. 使用检查清单验证
3. 按照决策流程执行

### 项目完成后
1. 记录新的经验教训
2. 更新规范文档
3. 同步到其他项目

## 🌐 GitHub同步方案设计

### 核心设计思路
**问题：** 一个人管理多个AI项目，需要统一的规范管理  
**解决：** 动态主项目机制 + 智能同步系统

### 项目角色定义
**所有项目都是"主项目"：**
```
每个AI项目都具备：
├── 拉取GitHub规范的能力
├── 同步到其他项目的能力  
└── 接收其他项目同步的能力
```

### 工作流程
**场景1：在GameAssetExtractor工作**
```
1. 进入项目：cd D:/GameAssetExtractor
2. 执行同步：python ai_collaboration/sync_standards.py
3. 系统检测：当前项目 = GameAssetExtractor
4. 拉取更新：从GitHub拉取最新规范
5. 本地更新：更新GameAssetExtractor的规范
6. 同步其他：自动同步到MerchantAI和X-AnyLabeling-main
```

**场景2：在MerchantAI工作**
```
1. 进入项目：cd D:/MerchantAI  
2. 执行同步：python ai_collaboration/sync_standards.py
3. 系统检测：当前项目 = MerchantAI
4. 拉取更新：从GitHub拉取最新规范
5. 本地更新：更新MerchantAI的规范
6. 同步其他：自动同步到GameAssetExtractor和X-AnyLabeling-main
```

### 文件结构设计
**每个项目都有相同的同步脚本：**
```
GameAssetExtractor/
├── ai_collaboration/          # 专门的同步文件夹
│   ├── sync_standards.py     # 同步脚本
│   ├── AI_COLLABORATION_STANDARDS.md  # 规范文档
│   ├── project_config.json   # 项目配置
│   └── sync_logs/            # 同步日志
│       └── sync_history.json
├── src/
├── tools/
└── ...

MerchantAI/
├── ai_collaboration/          # 相同的同步文件夹
│   ├── sync_standards.py     # 相同的同步脚本
│   ├── AI_COLLABORATION_STANDARDS.md  # 规范文档
│   ├── project_config.json   # 项目配置
│   └── sync_logs/            # 同步日志
│       └── sync_history.json
├── src/
├── tools/
└── ...
```

### 技术实现逻辑
**智能检测机制：**
```python
def detect_current_project():
    current_path = os.getcwd()
    if "GameAssetExtractor" in current_path:
        return "GameAssetExtractor"
    elif "MerchantAI" in current_path:
        return "MerchantAI"
    elif "X-AnyLabeling-main" in current_path:
        return "X-AnyLabeling-main"
```

**同步逻辑：**
```python
def sync_standards():
    current_project = detect_current_project()
    
    # 步骤1：拉取GitHub最新规范
    pull_from_github(current_project)
    
    # 步骤2：更新当前项目规范
    update_local_standards(current_project)
    
    # 步骤3：同步到其他项目
    for project in all_projects:
        if project != current_project:
            sync_to_project(project)
```

### 配置文件设计
**全局配置（GitHub仓库）：**
```json
{
    "version": "1.1.0",
    "last_updated": "2025-01-25",
    "projects": [
        "GameAssetExtractor",
        "MerchantAI", 
        "X-AnyLabeling-main"
    ]
}
```

**本地配置（每个项目）：**
```json
{
    "project_name": "GameAssetExtractor",
    "collaboration_folder": "ai_collaboration",
    "github_repo": "your-username/ai-collaboration-standards",
    "local_path": "D:/GameAssetExtractor",
    "target_projects": [
        "D:/MerchantAI",
        "D:/X-AnyLabeling-main"
    ]
}
```

### 核心优势
**1. 灵活性：** 任何项目都能成为"主项目"  
**2. 独立性：** 每个项目都能独立工作  
**3. 一致性：** 所有项目保持规范同步  
**4. 简单性：** 只需要在一个项目中执行同步命令  
**5. 结构清晰：** 所有协作文件集中在专门文件夹中

---

**维护者**：AI协作团队  
**最后更新**：2025-09-25  
**版本**：v1.1
