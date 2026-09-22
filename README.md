# Athena

Athena is a reusable Codex image-style skill. It turns a short content description into a structured image-generation prompt, applies a named visual system, and verifies the generated bitmap for style, composition, cropping, color, text, and other common failures.

## Included styles

| Style ID | Description |
| --- | --- |
| `marker-doodle` | Pure black-and-white editorial doodles with bold marker lines, complete subjects, and generous whitespace. |
| `scribble-ink` | Loose, exaggerated felt-tip character drawings with optional coral accents. |
| `soft-clay` | Rounded, low-detail clay characters with soft studio lighting and restrained pastel sets. |
| `knit-doll` | Textile characters with felted knitwear and non-knit miniature shoes, staged inside bright Blender/C4D/Octane fairytale 3D environments. |
| `geometric-collage` | Trial, pending rendered-image review. Large modular geometric paper shapes, a restrained 2–4-color palette and generous negative space; optional exact 50/50 photograph-and-illustration layout. |

When no background is specified for `knit-doll`, Athena asks the user to choose one of six named fairytale presets, random selection, or a custom scene. Choosing custom pauses generation until the user supplies the scene description.

For `geometric-collage`, a subject description produces a standalone illustration. A requested photo comparison uses the supplied photograph above a separately generated illustration, composed into equal-height panels with `scripts/compose_photo_pair.py` (Python 3.9+ and Pillow 9.1+). Install the optional dependency with `python3 -m pip install "Pillow>=9.1"`. The compositor preserves the photograph's content through proportional fitting and adds a solid matte if needed; it does not outpaint. Reference-image input depends on the selected generation tool.

## Install

Clone the repository into your Codex skills directory:

```bash
git clone https://github.com/prosody007/athena.git ~/.codex/skills/athena
```

Athena compiles and validates prompts; image generation still requires an image-generation tool, API, or gateway available in the current Codex environment.

## Use

Open the style menu:

```text
Use $athena and show the available styles.
```

Generate with a specific style:

```text
使用 $athena，风格：knit-doll，生成：一个戴圆框眼镜、拿着手机大笑的年轻人，竖版，不要文字。
```

```text
使用 $athena，风格：marker-doodle，生成：一个男性坐在沙发上使用电脑，横版。
```

## Repository structure

```text
athena/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── scripts/
│   └── compose_photo_pair.py
└── references/
    ├── marker-doodle.md
    ├── scribble-ink.md
    ├── soft-clay.md
    ├── knit-doll.md
    └── geometric-collage.md
```

## License

MIT
