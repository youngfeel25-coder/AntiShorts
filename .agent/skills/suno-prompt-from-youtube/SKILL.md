---
name: suno-prompt-from-youtube
description: "Analyze any YouTube music video in deep detail and generate a production-ready Suno AI prompt (Style of Music + Lyrics structure). Use for: extracting musical DNA from a reference track (BPM, key, scale, instrumentation layers, vocal style, arrangement timeline, production technique) and converting it into Suno AI's 9-dimension prompt format. Triggers on requests like: analyze this YouTube song and make a Suno prompt, create a Suno AI version of this track, make music like this YouTube video, generate style tags and lyrics for Suno."
---

# YouTube → Suno AI Prompt Generator

Analyze a YouTube reference track and produce a copy-paste-ready Suno AI prompt set (Style of Music + Lyrics structure).

## Workflow

### Step 1: Deep Audio Analysis

Run this exact command on the provided YouTube URL:

```bash
manus-analyze-video "<URL>" "당신은 세계 최고의 음악 프로듀서입니다. 이 곡을 Suno AI로 완벽하게 재현하기 위한 목적으로 다음 항목을 극도로 상세하게 분석해주세요. 1) 정확한 BPM과 박자 구조, 2) Key와 스케일 종류(Natural Minor/Harmonic Minor/Phrygian 등), 3) 레이어별 악기 분해: 드럼 패턴, 베이스 라인, 기타 주법, 오케스트라 파트(현악/관악/합창단 SATB), 신스 역할, 4) 보컬 스타일(음역대/창법/감정), 5) 합창단 배치와 화음, 6) 감정 아크(에너지 곡선), 7) 섹션별 타임스탬프와 Intensity(1-10), 8) 프로덕션 기법(리버브/딜레이/공간감), 9) Suno AI 재현용 핵심 키워드 20개"
```

### Step 2: Map to 9-Dimension Framework

Convert each analysis item to the 9 Suno dimensions. For the full mapping table and Lazenca reference example, read `references/9-dimension-mapping.md`.

| Analysis Item | → Suno Dimension |
|---|---|
| 장르/서브장르 | Genre & Style |
| BPM + 박자 | Tempo & Rhythm |
| Key + 스케일 | Key & Scale |
| 분위기/감정 | Mood & Emotion |
| 레이어별 악기 | Instrumentation |
| 프로덕션 스타일 | Density & Brightness |
| 섹션 타임스탬프 | Arrangement/Structure |
| 믹스 공간감 | Soundscape/Ambiance |
| 프로덕션 기법 | Production Quality |

### Step 3: Build the Style of Music String

Combine the 9 dimensions into a comma-separated keyword string for Suno's **Style of Music** field. Keep it under 120 characters. Prioritize: genre tags → BPM → key → instrument techniques → mood → production feel.

**Quality checklist before finalizing:**
- BPM stated as a number (`88 BPM`, not "fast")
- Key stated explicitly (`D minor`, `E minor`)
- Each instrument has a technique descriptor (`palm-mute guitar`, not just `guitar`)
- Vocal style is specific (`gritty baritone power vocal`, not just `male vocal`)
- At least one spatial keyword (`large hall reverb`, `wall of sound`)

### Step 4: Build the Lyrics Structure

Create a lyrics template using Suno's section markers that mirrors the reference track's arrangement timeline. Use these markers:

```
[Intro]  [Verse 1]  [Pre-Chorus]  [Chorus]  [Bridge]
[Guitar Solo]  [Breakdown]  [Final Chorus]  [Outro]
[Choir]  [Instrumental Break]
```

Add parenthetical delivery notes inside sections: `(dark, theatrical, suppressed energy)`, `(full explosion — power vocal)`.

For ready-made templates (Lazenca-style vocal, instrumental, dark EDM), read `references/suno-prompts.md`.

### Step 5: Deliver

Present two clearly labeled copy-paste boxes:
1. **Style of Music** — the keyword string
2. **Lyrics** — the full structured lyrics

Include a brief summary table of the extracted musical DNA.
