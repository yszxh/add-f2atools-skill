# f2atools Skill (f2atools 技能)

**适用于 Claude 的 AI 图像/视频生成工具，基于 YYDS API。**

## 功能特性 (Features)
- **文生图/视频 (Text-to-Image/Video)**: 通过文本提示词生成视觉内容。
- **图生图/视频 (Image-to-Image/Video)**: 支持参考图片（本地路径转 Base64）。
- **YYDS API 集成**: 预配置接口地址 `https://vip.yyds168.net`。
- **流式解析**: 高效从 SSE 流中提取媒体 URL。

## 安装 (Installation)

1. 克隆此仓库：
   ```bash
   git clone https://github.com/yszxh/add-f2atools-skill.git
   ```
2. 将文件复制到您的 Claude 技能目录：
   - Windows: `%USERPROFILE%\.claude\skills\f2atools`
   - macOS/Linux: `~/.claude/skills/f2atools`

## 使用方法 (Usage)

```bash
/f2atools generate --prompt "赛博朋克风格的城市" --api_key "你的密钥"
```
