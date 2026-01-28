# f2atools Skill

**AI image/video generation tool via Flow2API for Claude.**

## Features
- **Text-to-Image/Video**: Generate visuals from text prompts.
- **Image-to-Image/Video**: Support for reference images (local path to base64).
- **Flow2API Integration**: Pre-configured with `https://vip.yyds168.net`.
- **Stream Parsing**: Efficient extraction of media URLs from SSE streams.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yszxh/add-f2atools-skill.git
   ```
2. Copy the files to your Claude skills directory (usually `~/.claude/skills/f2atools`).

## Usage

```bash
/f2atools generate --prompt "cyberpunk city" --api_key "your-key"
```
