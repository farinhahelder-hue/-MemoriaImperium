# Memoria Imperium - YouTube Content System

Your streamlined AI-powered workflow for creating YouTube content.

## 🚀 Quick Start

### 1. Get Gemini API Key (Free)
```
→ https://aistudio.google.com/
→ Get API Key → Create API Key
→ Copy the key (starts with AIza...)
```

### 2. Add API Key to GitHub
```
→ Go to: https://github.com/farinhahelder-hue/-MemoriaImperium/settings/secrets
→ Click "New repository secret"
→ Name: GEMINI_API_KEY
→ Value: (paste your API key)
```

### 3. Generate AI Content
1. Go to **Actions** tab
2. Select **"Gemini AI Content Generator"**
3. Click **Run workflow**
4. Enter:
   - **Topic:** "Battle of Cannae"
   - **Content Type:** "full"
   - **Target Length:** "15"
5. Click **Run workflow**
6. Wait ~30 seconds
7. Download artifact!

---

## 🤖 Available Workflows

| Workflow | What It Does | AI-Powered |
|----------|--------------|------------|
| **Gemini AI Content Generator** | Generates research, outline, script, SEO | ✅ Yes |
| **Video Assembly (FFmpeg)** | Concatenate clips, add intro/outro, compress | ❌ |
| **Video Production Pipeline** | Process assets, thumbnails, chapters | ❌ |

---

## 📁 Project Structure

```
MemoriaImperium/
├── .github/workflows/     # GitHub Actions automations
│   ├── gemini-content-gen.yml  # 🤖 AI content generation
│   ├── video-ffmpeg.yml        # Video assembly
│   └── video-assembler.yml     # Production pipeline
├── research/              # Topic research documents
├── prompts/               # AI prompting templates
├── scripts/               # Video scripts
├── drafts/                # Content calendar
└── workflow/              # Helper scripts
```

---

## 📋 Workflow Pipeline

```
Topic → GitHub Action → Gemini AI → Generated Content → You Edit → Publish
         (30 sec)       (research, script, SEO)
```

---

## 🎬 Output Files

When you run the workflow, you get:

```
research/YYYY-MM-DD_topic/
├── gemini-research.md      # Facts, figures, sources
├── gemini-outline.md      # Video structure with timing
├── gemini-script.md       # Full narration script
└── gemini-seo-metadata.md # Titles, tags, thumbnails
```

---

## 💰 Cost

**Gemini API Free Tier:**
- 15 requests/minute
- 1,500 requests/day
- **$0/month** for most creators

---

## 🔗 Links

- [Your Channel](https://www.youtube.com/@MemoriaImperium)
- [GitHub Repository](https://github.com/farinhahelder-hue/-MemoriaImperium)
- [Gemini API](https://ai.google.dev/gemini-api/docs)
- [Google Flow](https://flow.google.com)

---

*Setup complete! Start generating content with AI.*
