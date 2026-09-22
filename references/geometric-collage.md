# 方块几何拼贴 · Geometric Collage

style-id: `geometric-collage`

状态：试用，待成图验收。首次成功生成后须完整检查本文件的专属验收项，再判断实际风格表现；不要将规范收录等同于视觉一致性已获验证。

用少量完整大块面保留主体最鲜明的视觉记忆：方块化结构、克制的纸片叠压、从题材提炼的少色系统，以及大面积留白。适用于人物、建筑、动物、植物、器物与景观。上下照片对照是可选版式；纯插画也保持同一视觉语言。

## 输入与版式

- `illustration`：只输出几何拼贴插画。用户只描述主体、未要求照片对照时使用。默认 `1024x1024`。
- `photo-pair`：上方原照片、下方对应插画，宽度相同，高度严格各占成品的 50%。用户要求上下对照或保留上方原图时使用。默认成品 `1536x1536`，每半幅 `1536x768`；“上下 1:1”指两半面积相等，不代表每一半都必须是正方形。用户明确指定每半幅正方形时，使用如 `1024x2048` 的成品。
- 照片对照需要可读取的原图。缺图时请求原图或本地路径；可以先整理规范。只有用户同意做示意，或在可选询问后明确说明采用虚构题材时，才用合成摄影感图片做演示，并在交付时标注，不能称其为原照片或已验证身份保真。
- 用户指定仅插画时，不添加照片；指定上下对照时，不擅自改成交付单幅插画。

## 视觉语言

### 识别与概括

从参考图或用户描述中提取少量真正有辨识度的线索：外轮廓、身体朝向、姿态、发型或物种特征、关键服饰、体量比例，以及人物和动物／器物之间的接触关系。先保住这些线索，再删去无关细节。不完整复制照片，不写实描摹，不用照片滤镜代替结构重建。

以矩形、方形、圆角方块和少量椭圆、三角形、不规则纸片组织主体。大块面承担轮廓与结构，较小块只用于必要的识别点。尽量把连续的衣服、躯干、墙面或叶丛保留为整体；不要用大量碎片填满它们。适度夸张，但成熟、简洁、有秩序。

- 人物：偏方形面部、清晰下颌、块面五官和整体化发型；动作靠肩、臂、躯干的转折表达。不得把成年人幼儿化。
- 建筑：方整体量、立面分区、少量窗洞节奏与结构转折；不得把每块砖、每个窗框都单独拼贴。
- 动植物：保留物种轮廓、主要斑纹、身体或枝叶的走势，皮毛和叶片不要切成密集小片。
- 器物与景观：保留关键比例、开口、支撑关系与空间层次；曲线适度方块化，但不能丢失识别性。

### 构图

小尺度主体，大面积安静留白；主体形成一个明确视觉中心。可参考主体外接框占画幅宽度约 35–55%、高度约 45–65%，依题材、姿势和用户用途调整，不把范围当作硬指标。照片对照时，该构图要求只作用于下半幅插画，不强迫原照片跟着缩小。

根据朝向、比例和重心自由安排偏心位置，重视正负形与块面轻重。独立素材默认保留完整主体；海报构图或用户允许时可贴边、局部裁切，但不能裁掉关键识别点。复杂背景删除，只留下必要的支撑、地面或环境形状，不出现第二中心。

### 色彩

从照片提取 2–4 种主导颜色，整理成协调色系；奶油白或纸色作为底色，不计入主色数量。允许少量同色系明暗变化，但不得扩成杂乱色盘。没有照片时依据题材选择 2–4 种协调颜色。

颜色可适度提亮、提纯、去灰，同时保留原图最具辨识度的色彩关系。奶油白、杏色、蜜桃粉、珊瑚橙、雾蓝、灰绿、鼠尾草绿、暖棕、柔紫是可选方向，不是每次必须混用的固定清单。必要的深色识别点可少量保留；不要把整体做成土黄、脏灰、暗褐、荧光或廉价糖果配色。

### 材质

扁平色块带细腻纸张颗粒、柔和噪点与轻微艺术印刷质感。纸片边缘干净但略有手工感，叠压关系主要靠形状与颜色表达。避免明显投影、厚纸浮雕、逼真折纸、3D 渲染、光滑矢量与塑料感。纸感不能盖过块面，也不要用严重磨损或脏旧纹理制造“高级感”。

## 照片对照执行

1. 查看实际原图，记录可见主体、姿态、识别点、关键关系、主色与不可裁掉的位置。上半幅保持原图真实质感、自然光影和色彩氛围，只在用户要求时轻微调色；不要改变身份、结构或姿势。
2. 单独生成下半幅插画，提示词明确只生成插画，不生成照片、上下分屏或边框。使用 Athena 选定的执行层与合法尺寸，优先直接生成目标半幅大小。目标半幅不满足模型尺寸限制时，使用同比例合法母版，后续等比适配。
3. 检查当前执行层是否真的支持参考图输入。当前 `ddit-image-generation/scripts/generate.py` 只接受文字提示，不能把路径写入提示词就当作上传了照片。可通过观察原图、描述视觉线索生成几何重构，并目视核验对应关系；如果无法保住关键特征，要披露局限。不得擅自切换图片编辑端点。
4. 在本地将原照片与验收后的插画合成。使用 [../scripts/compose_photo_pair.py](../scripts/compose_photo_pair.py)，确保分界线严格在 `H/2`，无额外间隔、标签或分割线。上半幅直接使用原图，不能用模型重绘结果冒充保留原照。
5. 默认等比完整容纳原图。比例不符时，助手脚本添加指定底色留边；这是留边适配，不是自然扩展环境。若必须满幅，选择与原图比例匹配的半幅画布，或在确认主体不会被裁掉后制作裁切副本。自然环境扩展需要支持该操作的执行层与适用授权；不能承诺当前文字生成脚本能完成保真扩图。

合成示例（需要 Python 与 Pillow；插画需先通过生成执行层制作）：

```bash
python3 scripts/compose_photo_pair.py \
  --photo /absolute/path/source.jpg \
  --illustration /absolute/path/collage.png \
  --out /absolute/path/photo-collage-pair.png \
  --width 1536 --height 1536 --background '#F7F1E7'
```

## 插画提示词骨架

将占位字段替换为本次观察或用户信息，不把不可见细节写成事实：

```text
Asset type: A mature editorial paper-collage illustration, no text.
Primary request: [subject, visible action and relationship].
Identity anchors: [distinctive silhouette, proportions, direction, key clothing or markings].
Style/medium: Modernist geometric cut-paper collage. Reconstruct the subject with a small number of large, complete modular shapes; rectangles, squares and rounded blocks dominate, supported by a few ovals, triangles and irregular pieces. Preserve visual recognition through structure, not realistic tracing.
Subject design: [subject-specific geometry]. Keep continuous major masses intact. Small shapes only for essential identity cues. Restrained adult editorial sensibility.
Composition/framing: One small-scale focal group with generous quiet negative space, [position and direction]. Preserve [essential contacts/supports]. Background reduced to [necessary shapes or none].
Color palette: [2–4 extracted dominant colors] on [paper color]; limited tonal variation, fresh yet restrained, preserving the source's defining color relationships.
Materials/textures: Flat paper color fields, subtle warm paper grain, soft noise and delicate print texture. Clean slightly handmade edges, color and shape overlaps, no dimensional relief.
Constraints: [required features]. Illustration only.
Avoid: Tiny fragmented mosaic, excessive facets, photorealistic tracing, childish chibi proportions, smooth vector finish, thick outlines, 3D, glossy gradients, strong shadows, distressed dirt, muddy dark palette, neon, candy colors, cluttered background, invented text or labels.
```

## 专属验收

- 识别点和叙事关系：对照时能凭轮廓、姿态、配色和主要特征对应到照片；纯插画时符合用户描述。单次示意不能证明所有题材或真人身份一致性。
- 造型：少而大的完整块面占主导，结构清楚，不是碎片马赛克、低多边形照片滤镜或写实描摹。
- 构图：小主体、足够留白、一个视觉中心，背景不抢主位；关键接触关系与支撑关系合理。
- 颜色：2–4 种主色及底色形成系统，保留源图气质，无杂乱碎色。
- 质感：细腻纸感、轻微印刷颗粒，扁平，不光滑、不立体、不脏旧。
- 照片对照：尺寸实测，上下区域严格等高；原照没有拉伸、主体扭曲或被模型替换。留边、裁切、调色或扩图的实际处理要如实披露。

按 Athena 的一次定向重试规则修正失败项。交付附 `layout: illustration` 或 `layout: photo-pair`；虚构摄影感示意需明确标注尚未验证原照保真。
