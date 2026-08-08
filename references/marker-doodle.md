# marker-doodle：黑白粗马克笔涂鸦

## 风格身份

- **style-id：** `marker-doodle`
- **中文名：** 黑白粗马克笔涂鸦
- **别名：** 马克笔涂鸦、黑白马克笔、粗线涂鸦、黑白粗马克笔
- **适用：** 人物、动物、简单动作、编辑插图、可供后续排版的独立母版
- **默认画布：** `1024x1824`，竖版近 9:16

把用户的文字视为内容简报，自动保持固定画风和完整主体构图。不要发明标语、道具、场景或额外人物。

## 固定视觉语言

除非用户明确覆盖且已解决风格冲突，必须同时应用以下规则：

- 仅使用纯黑墨色和干净纯白背景；不使用灰色或彩色。
- 使用天真、粗犷的马克笔编辑涂鸦，以及原始图形感的 spot illustration。
- 线条粗、近乎等宽、圆头，带轻微手绘不规则感。
- 人体有意简化、略显笨拙，头部比例偏大。
- 面部符号化：点状眼睛、一小笔鼻子、一小笔嘴和简单眉毛。
- 头发只用少量大轮廓表达，不画单根发丝。
- 保留一个占主导的纯黑大色块，通常是主要衣物或最大物体。
- 内部线条极少；不描绘褶皱、材质渲染或细碎装饰。
- 氛围平静、当代、独立杂志感，随性而非华丽。
- 使用大量干净白色负空间和清晰可读的剪影。

不得把人物描述为 photogenic、beautiful、fashionable、anatomically accurate 或 realistically proportioned；这些词会把结果推向常规时尚插画。

## 完整主体母版规则

把输出视为供后续排版使用的、不裁切的制作母版：

- 从上到下展示完整主体和完整轮廓。
- 四肢、手、脚、家具、设备、包、杯子及其他必需对象必须完整出现。
- 所有元素放在中央安全区内，四边保留 10–15% 白色边距。
- 镜头要比直觉更远，整体构图要比通常更小。
- 头顶、脚或家具下方、伸出物体两侧都必须留出可见白色空间。
- 头发、手肘、脚、沙发扶手、电脑边角、包带和道具均不得接触画布边缘。
- 禁止使用 `cropped at the edge`、`edge-to-edge figure`、`partially out of frame`、`close-up crop` 或 `dynamic cut-off composition` 等表述。
- 坐姿人物须展示整张椅子或沙发，包括靠背、扶手、座面、底座和可见椅脚。
- 站姿人物须展示完整身体和双脚，脚下保留白色空间。
- 多人构图须缩小整个群组，确保所有人物与物体位于同一个安全区内。

在每份最终提示词接近末尾处逐字加入：

```text
This is an uncropped master illustration: zoom out, show the entire subject and every required object fully inside the canvas, and preserve at least 15% clean white safety margin on all four sides. Nothing may touch or cross the image boundary.
```

## 风格提示词模块

将以下内容填入主 Skill 的通用提示词结构，只使用与请求有关的字段：

```text
Use case: illustration-story
Asset type: reusable uncropped editorial doodle master, <aspect ratio>
Primary request: <the user's subject and action>
Required objects: <only explicitly requested objects>
Scene/backdrop: completely clean white background; no environment unless explicitly requested
Style/medium: naive bold-marker editorial doodle, primitive graphic spot illustration, thick nearly uniform round-ended black strokes, deliberately simplified and slightly awkward
Subject design: slightly oversized head, symbolic face, simplified anatomy, a few large hair contours, one dominant uninterrupted solid-black shape, minimal internal detail
Composition/framing: complete subject centered within the safe zone, pulled-back view, generous white negative space, all objects fully visible
Color palette: pure black and white only
Text (verbatim): <exact text, or state no text>
Master framing constraint: This is an uncropped master illustration: zoom out, show the entire subject and every required object fully inside the canvas, and preserve at least 15% clean white safety margin on all four sides. Nothing may touch or cross the image boundary.
Avoid: cropping, cut-off limbs or objects, edge contact, close-up framing, realism, accurate anatomy, thin elegant linework, detailed face, individual hair strands, garment folds, fabric texture, pencil texture, cross-hatching, shading, gray wash, shadows, gradients, watercolor, anime, polished vector perfection, background clutter, logos, watermark, extra people, extra props
```

## 专属验收

出现以下任一情况即判定不通过：

- 任一必需元素不完整、被裁切或接触边缘。
- 主体占画布高度或宽度约 75% 以上。
- 结果更像写实时尚速写，而不是图形化粗马克笔涂鸦。
- 面部出现塑造过的嘴唇、睫毛、颧骨或写实阴影。
- 黑色区域出现明暗渐变或细致褶皱。
- 模型擅自增加文字、场景、道具或人物。

仅因构图失败而重试时，保持内容不变并追加：

```text
Framing correction only: zoom out by 30%. Reduce the complete composition to about 65% of the canvas. Show every part of every subject and object, with wide white space around the entire group. Do not crop anything.
```
