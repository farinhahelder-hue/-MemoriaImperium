# YouTube Content Creation: Google Flow

This document outlines how to use Google Workspace and Google AI tools to streamline your YouTube content creation process.

## 1. Ideation & Planning (Google Keep & Google Sheets)
- **Google Keep:** Use this for quick, on-the-go idea capture. Jot down video ideas, interesting articles, or fleeting thoughts from your phone or desktop.
- **Google Sheets (Content Calendar):** Create a master sheet to track your videos from idea to published.
    - Columns: Status (Idea, Scripting, Recording, Editing, Scheduled), Title, Target Date, Links to Docs/Assets.

## 2. Research & Scripting (Google Docs & Google AI Studio/Gemini)
- **Google AI Studio / Gemini:**
    - Use the prompts in `prompts/content_generation_prompts.md` to brainstorm titles, generate outlines, and get help drafting sections of your script.
    - *Tip:* If using Google AI Studio, you can build custom prompts and save them as reusable templates.
- **Google Docs:**
    - Use `scripts/script_template.md` to draft your video.
    - Benefit: Real-time collaboration, auto-save, and easy access from any device.

## 3. Asset Management (Google Drive)
- Set up a standard folder structure in Google Drive for every video:
    - `01_Videos/`
        - `[Date] - [Video Name]/`
            - `Assets/` (Logos, music, graphics)
            - `Footage/` (A-roll, B-roll)
            - `Exports/` (Final video renders)
            - `Thumbnails/`

## 4. Automation Ideas (Google Apps Script / Make / Zapier)
- *Optional advanced step:* You can use Google Apps Script or a tool like Zapier to automate tasks, such as:
    - Automatically creating a new Google Doc and Google Drive folder when you add a new row to your Google Sheets Content Calendar.

## Summary Workflow Loop:
1. Capture Idea (Keep) -> 2. Log in Calendar (Sheets) -> 3. Brainstorm & Outline (Gemini/AI Studio) -> 4. Write Script (Docs) -> 5. Store Assets (Drive) -> 6. Produce & Publish.
