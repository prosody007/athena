# scribble-ink：Scribble Ink 涂鸦墨线

## 风格身份

- **style-id：** `scribble-ink`
- **中文名：** Scribble Ink 涂鸦墨线
- **别名：** 涂鸦墨线、乱笔墨线、毡笔人物、珊瑚粉涂鸦、Scribble Ink
- **适用：** 人物头像、半身角色、编辑肖像、轻松但非幼稚的系列人物插画
- **默认画布：** `1024x1024`；常用竖版 `1024x1536`、近 9:16 `1024x1824`、横版 `1536x1024` 或 `1824x1024`
- **文件名前缀：** `scribble-ink-`

把用户的文字视为内容要求，自动保持固定系列画风。不要发明标语、场景、道具、额外人物或彩色背景。默认使用一个大幅胸像或半身人物；仅在用户明确要求时使用全身构图。每个人物都必须有清楚可辨的衣服，即使用户没有指定服装。

## 目录

- [固定视觉语法](#固定视觉语法)：风格身份、颜色、线条、黑色色块、人物比例
- [人物细节](#6-face-construction)：面部、头发、服装、表情、道具
- [构图与系列一致性](#11-composition)：构图、批次常量、完整禁止项
- [专属验收](#14-acceptance-checklist)：成图接受条件
- [提示词模块](#风格提示词模块)：Athena 编译提示词时载入
- [定向重试](#定向重试)：只修正失败项

## 固定视觉语法

Use this document as a locked visual grammar. Preserve the family resemblance across every output even when the character, age, clothing, expression, or pose changes.

## 1. Style identity

Create a quirky independent-editorial character portrait that looks drawn quickly and casually with a blunt black felt-tip pen and a coral-pink highlighter. It should feel warm, human, optimistic, slightly awkward, and visibly improvised—not careful line art, polished illustration, cute-3D, or fashion-realistic.

The style is defined by five simultaneous signals:

1. Oversized graphic head and noticeably long narrow neck.
2. A two-level family of blunt, visibly wobbly black lines: bold outer silhouettes and scribble masses, lighter interior facial and garment marks.
3. Simplified symbolic facial construction with deliberate asymmetry.
4. Rough overlapping black scribble masses in hair, beard, or clothing, using broad loops rather than fine strands.
5. Tiny coral-pink accents on cheeks, nose, ears, hands, or sparse garment marks—never a background block.

Missing two or more of these signals means the output is outside the series.

## 2. Palette lock

- Canvas: pure white `#FFFFFF` only.
- Primary ink: near-black `#111111`.
- Accent: one coral pink near `#F47F91`.
- Use no gray, cream, beige, skin tone, secondary color, gradient, or translucent wash.
- Keep pink below roughly 8% of the total canvas area.
- Prefer two clearly visible cheek circles, flat ovals, or three-stroke scribble patches as the default pink usage. Do not make the blush so tiny that it disappears.
- Optionally use pink on one simple nose, ear interior, palm marks, neck stripe, or sparse clothing stripe.
- Do not use a pink/red/coral square, rectangle, rounded rectangle, blob, halo, frame, shadow, or paper swatch behind the character.

## 3. Line language

- Use exactly two loose visual line levels rather than one uniform thickness.
- Draw principal outer silhouettes, hair or beard masses, and major gesture lines at roughly 0.9–1.4% of the shorter canvas edge.
- Draw facial features, collar or cuff marks, and small prop details at roughly 0.45–0.8% of the shorter canvas edge, about 55–70% of the outer-contour weight.
- Keep each level blunt and roughly consistent within itself, with accidental thick spots where the marker slows or overlaps.
- Use rounded ends and obvious low-frequency hand wobble. Curves should wander gently instead of tracing perfect geometry.
- Prefer fast one-pass contours. Preserve small overshoots, open joins, imperfect tangencies, lopsided curves, and 3–8 degree tilts.
- Use very few strokes. One awkward decisive contour is better than several thin corrective contours.
- Do not use ultra-thick marker silhouettes associated with Marker Doodle.
- Do not use one identical heavy width for every feature. Do not use thin elegant pen lines, vector-perfect Bezier curves, calligraphic tapering, meticulous inking, sketch construction lines, cross-hatching, fine hatching, or repeated contour searching.

## 4. Black-fill language

- Render hair, beard, or one large clothing zone as a substantial high-contrast black mass made from a few broad overlapping felt-tip loops or diagonal swipes. Aim for roughly 15–35% of the visible character area when the subject permits.
- Let irregular white slashes and gaps remain between the broad black strokes.
- Add subtle dry-marker behavior inside heavy black strokes: slightly uneven ink density, blunt overlaps, and a few narrow white skips. Keep the canvas itself clean and texture-free.
- Keep a simple readable outer silhouette despite the internal scribble texture.
- Use solid black only for small graphic forms such as pupils, open mouth, cuffs, or compact hair masses.
- Never simulate texture with dozens of thin strands, tiny fur marks, arm-hair dashes, garment hatching, or evenly spaced decorative strokes. Delete detail rather than rendering it finely.
- Never render black areas with smooth gradients, realistic highlights, glossy volume, or photographic texture.

## 5. Character proportions

- Make the head 40–55% of the visible character height in a bust portrait. Push the proportion further when the action remains readable.
- Match the head shape to age. Use rounded or egg-shaped heads for children and younger characters; use a longer oval, narrow rectangle, or tapered face for mature and middle-aged adults.
- For mature adults, use flatter brows, smaller symbolic eyes, a restrained mouth, and less circular cheek placement. Preserve warmth without making the person look childlike or chibi.
- Use a neck that is visibly longer and narrower than realistic anatomy.
- Simplify shoulders into two visibly uneven sloping lines. Avoid one symmetrical domed arc.
- Always clothe every human character. A bare or blank body-shaped torso is outside the style, even when the user does not specify an outfit.
- Make the garment immediately readable with at least two clear clothing signals: one neckline, collar, or placket plus visible sleeves, cuffs, shoulder seams, or one broad stripe/block.
- Construct a bust garment as an open-bottom trapezoid or two sloping shoulders that continue toward or through the bottom edge. Never close the torso into a circular, capsule, bean, or balloon silhouette.
- Reduce the torso to two or three principal contours and two or three bold garment signals. Omit tiny pockets, realistic seams, repeated buttons, fabric folds, and fine texture unless essential to the request.
- When no outfit is specified, choose one neutral editorial default: a loose crew-neck top, simple collared shirt, Henley, or plain sweater. Use no logo or text.
- Make ears simple loops or rounded side shapes; slightly oversized ears are acceptable.
- Use deliberately simplified and visibly awkward anatomy: noodle arms, mitten hands, uneven shoulders, and compressed joints are welcome when the pose remains immediately readable.
- Default to a bust or waist-up portrait. Use full-body anatomy only if explicitly requested.

## 6. Face construction

Use one controlled eye mode per character:

- **Dot mode:** two tiny black dots with one or two short eyebrow lines.
- **Open-eye mode:** two oversized oval outline eyes with simple black pupils, useful for curiosity or glasses.

Never use realistic almond eyes, irises, eyelashes, eyelids with depth, highlights, or makeup.

Use one of these nose constructions:

- one short curved hook;
- one narrow vertical coral-pink shape;
- one small black comma.

Use a single curved smile, a tiny straight mouth, or one compact black open smile. Avoid modeled lips, teeth, tongue, or facial shading.

Cheeks must be simple and bilateral: two coral circles, two flat ovals, or two groups of three short coral scribbles. Make them clearly visible and slightly mismatched in height or size.

Deliberately offset the eyes, brows, ears, nose, and mouth slightly. Avoid a perfectly mirrored face or a mathematically centered feature layout. The asymmetry must feel spontaneous, not deformed.

## 7. Hair, beard, and accessories

- Build hair from a simple outer mass plus a few chunky internal black loops or swipes.
- Use only a handful of flyaway contour strokes.
- For curls, use overlapping loops and dense scribbles, not individual realistic strands.
- For beards, use an irregular high-contrast scribbled mass with broad diagonal or looping marks and a few bold white gaps. Avoid many short hair strokes.
- Draw glasses as oversized simple loops with one bridge and no reflections.
- Keep jewelry, collars, stripes, and buttons extremely sparse and graphic.
- Do not include detailed fabric, seams, logos, brands, patterns, or realistic accessories unless explicitly requested.

## 8. Clothing language

- Treat clothing as a required part of the character design, not optional decoration.
- Preserve a visible gap or neckline between the long neck and garment so the torso cannot read as bare skin.
- Show the garment through large structural cues: a thick crew neck, open collar, short placket, broad sleeve shape, black cuff, one loose stripe, or one rough black scribble panel.
- Prefer two or three oversized clothing cues over many small details.
- If the arms are holding a prop, keep the sleeve boundary or cuff visible on at least one arm.
- Do not output a smooth empty torso outline with arms growing directly from it.
- Integrate every black stripe or scribble panel inside the garment boundaries. Never place a detached black scribble beneath the character where it can read as a shadow or ground mark.

## 9. Expression and gesture

- Default mood: friendly, calm, curious, quietly cheerful, or mildly deadpan.
- Allow expressive raised arms, head tilts, sideways glances, or one small action gesture.
- Require visible asymmetry in at least two places: head tilt, gaze, ear height, shoulder height, arm gesture, hand height, or prop position.
- When holding an animal or object, place it slightly off-center and use different roles for the two arms, such as one arm supporting and the other resting or wrapping. Avoid mirrored hands and a centered bilateral cradle pose.
- Use at most three short black action/emphasis lines.
- Keep hands mitten-like or built from three or four oversized rounded finger loops. Do not draw nails, knuckles, palm creases, paw pads, or anatomical finger joints.
- Avoid dramatic anatomy, foreshortening, action-comic effects, or cinematic posing.

## 10. Prop and animal simplification

- Keep each requested prop fully readable through one clear outer silhouette, but reduce its internal structure to the minimum needed for recognition.
- For a held animal, prefer one bean-like body, one head shape, two principal visible paws, and one simple tail. Rear legs may be hidden by the embrace; do not expose four separate paws merely to prove completeness.
- Use only two dot eyes, one nose mark, and one mouth stroke for an animal face. Avoid a cute mascot expression, paw pads, fur marks, toe marks, or symmetrical display poses.
- Reduce prop and animal line count by roughly half compared with a children's-book rendering.
- Keep coral pink primarily on the human face. Add pink to an animal only when explicitly requested or when one tiny mark is necessary for series balance.

## 11. Composition

- Default output: one large, slightly off-center square portrait on empty white.
- Keep the head, hair, face, hands, and requested props inside an 8–12% top-and-side safe margin.
- Occupy 70–85% of the canvas height. The lower torso may naturally run out through the bottom edge, matching an editorial bust portrait; do not crop the head, hands, or requested prop.
- Keep the visual center near the face.
- Use frontal or slight three-quarter views.
- Keep the character-prop group slightly off-axis. Do not center the prop directly beneath the face unless the user explicitly requests a formal pose.
- Avoid realistic rooms, streets, landscapes, objects, shadows, and ground planes.
- Add only explicitly requested props, simplified to the same line language.
- Never invent text. If exact text is provided, render only that text.

## 12. Series consistency constants

Keep these constants across a batch or follow-up series:

- the same black, white, and coral-pink palette;
- the same two-level outer-versus-interior line hierarchy;
- the same 40–55% bust-portrait head ratio;
- the same elongated-neck construction;
- the same symbolic face vocabulary;
- the same rough scribbled black-fill treatment;
- clearly recognizable simple clothing on every human character;
- age-appropriate adult versus child face construction;
- asymmetric gestures and simplified props;
- the same pure-white background with no panel;
- the same subject scale and safe margins for the chosen aspect ratio.

Vary only content attributes requested by the user: identity, age, hair, expression, clothing, action, and props.

## 13. Full avoid list

Avoid colored background, pink background, red background, coral backdrop, background panel, square backdrop, rounded rectangle, blob, halo, paper swatch, frame, beige paper, gray background, scenery, realistic room, detailed environment, photorealism, fashion illustration, accurate anatomy, nude-looking torso, shirtless-looking blank torso, arms growing from an empty body outline, closed oval torso, balloon body, capsule sweater, detached scribble shadow, centered mirrored cuddle pose, four-paw display, cute animal mascot, childlike face on a mature adult, identical line weight everywhere, 3D mascot, clay render, anime, manga, kawaii chibi, polished vector art, smooth geometric icon style, perfect symmetry, thin elegant linework, delicate ink drawing, meticulous line art, fine hatching, repeated corrective contours, heavy Marker Doodle silhouette, pencil sketch, charcoal, watercolor, ink wash, cross-hatching, grayscale shading, gradients, soft shadows, realistic skin tone, individual hair strands, realistic fur, arm-hair dashes, paw-pad detail, realistic eyes, eyelashes, detailed lips, teeth, realistic fabric folds, tiny pockets, fussy seams, decorative garment marks, logos, watermark, invented text, extra people, extra props, cropped head, cropped hands.

## 14. Acceptance checklist

Accept only if all are true:

- The whole canvas is uninterrupted white outside the character.
- No colored backdrop shape exists.
- Coral pink is restricted to small accents and occupies less than about 6% of the canvas.
- The head is visibly oversized and the neck visibly elongated.
- The face is symbolic rather than anatomical.
- Outer contours and scribble masses are visibly heavier than facial, clothing, and prop interior marks; the drawing does not use one uniform line weight.
- Principal black contours are blunt, obviously wobbly, and handmade; they do not read as fine line art.
- At least one hair, beard, or clothing region forms a substantial rough black scribble mass with broad strokes and irregular white gaps when appropriate.
- The anatomy and face are deliberately asymmetric and simplified, with no fussy interior rendering.
- Every human character is unmistakably clothed, with a visible neckline or collar plus at least one sleeve, cuff, placket, stripe, or graphic clothing block.
- The garment uses sloping shoulders and an open or tapered lower construction, never a closed oval or balloon torso.
- Mature adults use a longer face, flatter brows, restrained expression, and do not read as chibi children.
- The pose is asymmetric in at least two visible ways, and any held prop is slightly off-center.
- Requested animals or props use a minimal readable silhouette without redundant limbs or children's-book detail.
- The character is large enough to feel graphic rather than timid, normally occupying 70–85% of the canvas height.
- The character and requested props are fully visible with safe margins.
- No unrequested scenery, person, prop, text, logo, or watermark exists.
- The result looks like the same illustration family as prior Scribble Ink outputs.

## 必须逐字加入的背景锁定

在每份最终提示词接近末尾处逐字加入：

```text
Background lock: the entire canvas is plain pure white #FFFFFF. Do not place any colored square, rectangle, circle, blob, brush patch, panel, halo, frame, or backdrop behind the character. Coral pink may appear only as tiny facial or clothing accents and must never appear in the background.
```

## 风格提示词模块

将以下内容填入 Athena 的通用提示词结构，只使用与请求有关的字段：

```text
Use case: illustration-story
Asset type: reusable Scribble Ink series character portrait, <aspect ratio>
Primary request: <user's character, expression, and action>
Required objects: <only requested props>
Scene/backdrop: pure white empty canvas, no environment
Style/medium: loose naive editorial character doodle, two-level blunt felt-tip line hierarchy, obvious hand wobble, slight dry-marker streaking inside black strokes, crude black scribble masses, fast and casually drawn rather than neat line art
Character design: exaggerated oversized age-appropriate head, long narrow neck, sloped uneven shoulders, tapered or open-bottom torso, deliberately awkward asymmetrical proportions, symbolic face, minimal interior detail
Clothing: clearly recognizable simple garment; show at least two clothing signals such as a neckline or collar plus sleeves or cuffs; use sloped or trapezoid garment construction, never a blank torso or closed balloon-like body
Pose: visibly asymmetric head, shoulders, arms, and prop placement; avoid centered mirrored cuddle poses
Props/animals: preserve one complete readable outer silhouette but reduce internal anatomy to the minimum; do not display every limb merely to prove completeness
Palette: black #111111, white #FFFFFF, one coral-pink accent #F47F91 restricted to tiny details
Composition: large bust or waist-up figure occupying 70–85% of the height, slightly off-center; keep head, hands, and props complete; lower torso may exit at bottom
Text (verbatim): <exact text or no text>
Background lock: the entire canvas is plain pure white #FFFFFF. Do not place any colored square, rectangle, circle, blob, brush patch, panel, halo, frame, or backdrop behind the character. Coral pink may appear only as tiny facial or clothing accents and must never appear in the background.
Avoid: <use the full avoid list above>
```

## 定向重试

出现彩色背景块时，仅追加：

```text
Background correction only: remove every background shape and background color. Return to an uninterrupted pure white #FFFFFF canvas from edge to edge. Keep the character unchanged. Pink is allowed only on the cheeks or one tiny requested detail.
```

结果过于精致或写实时，仅追加：

```text
Style correction only: make the drawing look faster, rougher, and more exaggerated. Increase only the outer silhouettes and major gesture lines to roughly 1.5 times their current thickness, while keeping facial, clothing, and prop interior marks at about 60% of that weight. Replace clean curves with blunt, visibly wandering single-pass felt-tip strokes; introduce deliberate asymmetry, open joins, and small overshoots. Remove 60% of interior garment, fur, finger, and anatomy lines. Replace fine hair or beard strands with a few broad overlapping black scribble loops and irregular white gaps. Keep the content and composition unchanged.
```

头部、手或道具被裁切时，仅追加：

```text
Framing correction only: preserve the rough two-level marker style exactly. Zoom out the complete character-and-prop group by 10–15% and shift it away from whichever edge is too close. Keep at least 6% clean white margin around the head, hair, both hands, and every requested prop. The lower garment alone may continue through the bottom edge in a bust portrait; no hand, face, hair, or prop may touch or cross an edge.
```

衣服缺失或辨识不清时，仅追加：

```text
Clothing correction only: keep the face, pose, props, composition, and rough marker style unchanged. Dress every human character in an unmistakable simple garment. Add a clear neckline or collar and visible sleeves or cuffs, plus at most one crude stripe or black scribble panel. The torso must read immediately as clothed, not as a blank body-shaped outline. Do not add fabric realism or fussy seams.
```

结果像可爱吉祥物或对称儿童画时，仅追加：

```text
Editorial correction only: keep the requested subject unchanged. Make the adult face longer and less round, flatten the brows, reduce the smile, tilt the head, offset the prop, and make the shoulders uneven. Replace the closed oval body with two sloping garment shoulders and a tapered torso that continues out through the bottom edge. Simplify the prop by 50% and remove redundant paws, fingers, and interior anatomy. Keep the rough two-level marker strokes and pure white background.
```
