# MD3 Design Token 完整参考手册

> 依据 Material Design 3 规范，完整的设计令牌 (Design Token) 体系。本文件供 skill 运行时作为参考数据加载。

---

## 1. 色彩系统 (HCT 色彩空间)

M3 使用 **HCT** (Hue-Chroma-Tone) 色彩空间替代传统 HSL/RGB。色彩方案 (ColorScheme) 包含 30+ 个颜色槽。

### 1.0 HCT 色彩空间详解

HCT 是 M3 的核心色彩模型，三个维度独立控制：

| 维度 | 范围 | 含义 |
|------|------|------|
| **Hue** (色相) | 0°–360° | 基础色彩，与 HSL 中的 Hue 相同 |
| **Chroma** (色度) | 0–~150 | 色彩鲜艳度/饱和度。0 = 灰色，越高越鲜艳 |
| **Tone** (色调) | 0–100 | 亮度。0 = 黑色，50 = 中等，100 = 白色 |

**Tone vs Luminance**: Tone 是感知均匀的亮度度量（基于 CIELAB L*），不像 HSL 的 L 那样在不同色相上视觉不均匀。这使得跨色调的对比度计算更精确。

**Tonal Palette 生成流程**:
```
Seed Color → HCT 分解 → 保持 H/C, 变化 T → 生成 0-100 共 13 个 Tone 色值
                                              (0, 10, 20, 30, 40, 50,
                                               60, 70, 80, 90, 95, 99, 100)
```

**Key Color → ColorScheme 映射** (亮色主题):
| Key Color | Primary Tone | Container Tone | On-Primary Tone |
|-----------|-------------|----------------|-----------------|
| Primary 源色 | Tone 40 | Tone 90 | Tone 100 (白) |
| Secondary | Tone 40 (偏移色相) | Tone 90 | Tone 100 |
| Tertiary | Tone 40 (偏移色相) | Tone 90 | Tone 100 |
| Error | 固定 #B3261E | Tone 90 | Tone 100 |
| Neutral | Tone 99 (bg) / 10 (text) | 5级容器 (99-90) | — |

### 1.0.1 Dynamic Color (动态取色 / Material You)

MD3 的杀手级特性 — 从壁纸自动提取色彩方案：

```
Wallpaper → Quantizer (提取主色) → Score (评分排序) → HCT 算法
                                                         ↓
                                              ColorScheme (亮色 + 暗色)
                                                         ↓
                                              全局 CssVariables
                                                         ↓
                                              所有组件自动更新
```

- **平台**: Android 12+ 原生支持，Web 可用 `@material/material-color-utilities`
- **种子色**: 壁纸主色 → primary，次色 → secondary/tertiary，中性色从壁纸亮度提取
- **用户可调**: 提供 ColorScheme 变体供用户选择（更鲜艳/更柔和）

### 1.1 完整亮色主题 (Light Theme) Token 表

| CSS 变量 | 色值 | 用途 |
|----------|------|------|
| `--md-sys-color-primary` | `#6750A4` | 主色，最重要的组件 |
| `--md-sys-color-on-primary` | `#FFFFFF` | 主色上的内容色 |
| `--md-sys-color-primary-container` | `#EADDFF` | 主色容器（如 FAB 背景） |
| `--md-sys-color-on-primary-container` | `#21005D` | 主色容器上的内容 |
| `--md-sys-color-secondary` | `#625B71` | 次要色 |
| `--md-sys-color-on-secondary` | `#FFFFFF` | 次要色上的内容 |
| `--md-sys-color-secondary-container` | `#E8DEF8` | 次要色容器（如 tonal button 背景） |
| `--md-sys-color-on-secondary-container` | `#1D192B` | 次要色容器上的内容 |
| `--md-sys-color-tertiary` | `#7D5260` | 第三色 |
| `--md-sys-color-on-tertiary` | `#FFFFFF` | 第三色上的内容 |
| `--md-sys-color-tertiary-container` | `#FFD8E4` | 第三色容器 |
| `--md-sys-color-on-tertiary-container` | `#31111D` | 第三色容器上的内容 |
| `--md-sys-color-error` | `#B3261E` | 错误色 |
| `--md-sys-color-on-error` | `#FFFFFF` | 错误色上的内容 |
| `--md-sys-color-error-container` | `#F9DEDC` | 错误色容器 |
| `--md-sys-color-on-error-container` | `#410E0B` | 错误色容器上的内容 |
| `--md-sys-color-background` | `#FFFBFE` | 页面背景 |
| `--md-sys-color-on-background` | `#1C1B1F` | 页面背景上的内容 |
| `--md-sys-color-surface` | `#FFFBFE` | 表面色（如 Card） |
| `--md-sys-color-on-surface` | `#1C1B1F` | 表面上的内容 |
| `--md-sys-color-surface-variant` | `#E7E0EC` | 表面变体 |
| `--md-sys-color-on-surface-variant` | `#49454F` | 表面变体上的内容 |
| `--md-sys-color-outline` | `#79747E` | 轮廓线（如 outlined button） |
| `--md-sys-color-outline-variant` | `#CAC4D0` | 轮廓变体 |
| `--md-sys-color-surface-dim` | `#DED8E1` | 暗淡表面 |
| `--md-sys-color-surface-bright` | `#FFFBFE` | 明亮表面 |
| `--md-sys-color-surface-container-lowest` | `#FFFFFF` | 最低容器表面 |
| `--md-sys-color-surface-container-low` | `#F7F2FA` | 低容器表面 |
| `--md-sys-color-surface-container` | `#F3EDF7` | 标准容器表面 |
| `--md-sys-color-surface-container-high` | `#ECE6F0` | 高容器表面 |
| `--md-sys-color-surface-container-highest` | `#E6E0E9` | 最高容器表面 |
| `--md-sys-color-inverse-surface` | `#313033` | 反转表面 |
| `--md-sys-color-inverse-on-surface` | `#F4EFF4` | 反转表面上的内容 |
| `--md-sys-color-inverse-primary` | `#D0BCFF` | 反转主色 |
| `--md-sys-color-shadow` | `#000000` | 阴影色 |
| `--md-sys-color-scrim` | `#000000` | 遮罩色（如 Dialog backdrop） |

### 1.2 暗色主题 (Dark Theme) Token 表

```
primary:          #D0BCFF    onPrimary:          #381E72
primaryContainer: #4F378B    onPrimaryContainer: #EADDFF
secondary:        #CCC2DC    onSecondary:        #332D41
secondaryContainer: #4A4458  onSecondaryContainer: #E8DEF8
tertiary:         #EFB8C8    onTertiary:         #492532
tertiaryContainer: #633B48   onTertiaryContainer: #FFD8E4
error:            #F2B8B5    onError:            #601410
errorContainer:   #8C1D18    onErrorContainer:   #F9DEDC
background:       #1C1B1F    onBackground:       #E6E1E5
surface:          #1C1B1F    onSurface:          #E6E1E5
surfaceVariant:   #49454F    onSurfaceVariant:   #CAC4D0
outline:          #938F99    outlineVariant:     #49454F
surfaceDim:       #141218    surfaceBright:      #3B383E
surfaceContainerLowest: #0F0D13  surfaceContainerLow: #1D1B20
surfaceContainer:      #211F26  surfaceContainerHigh: #2B2930
surfaceContainerHighest:#36343B
inverseSurface:   #E6E1E5    inverseOnSurface:  #313033
inversePrimary:   #6750A4    shadow: #000000    scrim: #000000
```

### 1.3 颜色使用规则

```
组件类型         → 使用颜色槽
Filled Button     → primary + onPrimary
Tonal Button      → secondaryContainer + onSecondaryContainer
Outlined Button   → transparent + primary + outline
FAB Primary       → primaryContainer + onPrimaryContainer
FAB Surface       → surfaceContainerHigh + primary
Card Elevated     → surfaceContainerLow + onSurface
TopAppBar         → surface + onSurface (沉浸式用 surface 色)
NavBar Active     → secondaryContainer (指示器)
Scrim/DialogBg    → scrim / surface
```

### 1.4 Contrast Levels — 对比度级别详解

MD3 通过调整色彩方案中 key color 的 **Tone** 值实现 3 种对比度级别：

| Level | 对标 | 适用场景 | Primary Tone 偏移 | Container Tone 偏移 | 表面色偏移 |
|-------|------|---------|-------------------|--------------------|-----------|
| **Standard** | WCAG AA (默认) | 日常使用 | Tone 40 (基准) | Tone 90 (基准) | 基准 |
| **Medium** | WCAG AA+ | 户外/高亮环境 | Tone 30 (–10) | Tone 95 (+5) | 加深 1 级 |
| **High** | WCAG AAA | 视觉障碍辅助 | Tone 20 (–20) | Tone 99 (+9) | 加深 2 级 |

**亮色主题下各级别关键色对比：**

| Token | Standard | Medium | High |
|-------|----------|--------|------|
| `primary` | `#6750A4` (T40) | `#4F378B` (T30) | `#381E72` (T20) |
| `on-primary` | `#FFFFFF` (T100) | `#FFFFFF` (T100) | `#FFFFFF` (T100) |
| `primary-container` | `#EADDFF` (T90) | `#D0BCFF` (T80) | `#C2A6FF` (T70) |
| `on-primary-container` | `#21005D` (T10) | `#21005D` (T10) | `#FFFFFF` (T100) |
| `surface` | `#FFFBFE` (T99) | `#F4EFF4` (T98) | `#E6E0E9` (T96) |
| `on-surface` | `#1C1B1F` (T10) | `#1C1B1F` (T10) | `#000000` (T0) |
| `outline` | `#79747E` (T50) | `#625B71` (T40) | `#49454F` (T30) |

**生成规则**: 将 seed color 的 Primary Tone 下调 (Standard T40 → Medium T30 → High T20)，Container Tone 上调，同时加深 Surface 系列。中性色变体同步从 Tone 99 下沉。

---

## 2. 字体系统 (Typography) 完整参考

默认字体: **Roboto** (Android) / **Google Sans** (可选标题)

| Token | Weight | Size | Letter Spacing | Line Height | CSS 变量前缀 |
|-------|--------|------|----------------|-------------|-------------|
| `display-large` | 400 | 57px | -0.25px | 64px | `--md-sys-typescale-display-large` |
| `display-medium` | 400 | 45px | 0px | 52px | `--md-sys-typescale-display-medium` |
| `display-small` | 400 | 36px | 0px | 44px | `--md-sys-typescale-display-small` |
| `headline-large` | 400 | 32px | 0px | 40px | `--md-sys-typescale-headline-large` |
| `headline-medium` | 400 | 28px | 0px | 36px | `--md-sys-typescale-headline-medium` |
| `headline-small` | 400 | 24px | 0px | 32px | `--md-sys-typescale-headline-small` |
| `title-large` | 400 | 22px | 0px | 28px | `--md-sys-typescale-title-large` |
| `title-medium` | 500 | 16px | 0.15px | 24px | `--md-sys-typescale-title-medium` |
| `title-small` | 500 | 14px | 0.1px | 20px | `--md-sys-typescale-title-small` |
| `body-large` | 400 | 16px | 0.5px | 24px | `--md-sys-typescale-body-large` |
| `body-medium` | 400 | 14px | 0.25px | 20px | `--md-sys-typescale-body-medium` |
| `body-small` | 400 | 12px | 0.4px | 16px | `--md-sys-typescale-body-small` |
| `label-large` | 500 | 14px | 0.1px | 20px | `--md-sys-typescale-label-large` |
| `label-medium` | 500 | 12px | 0.5px | 16px | `--md-sys-typescale-label-medium` |
| `label-small` | 500 | 11px | 0.5px | 16px | `--md-sys-typescale-label-small` |

### 组件字型映射

| 组件 | 使用字型 |
|------|---------|
| Button | label-large |
| FAB label | label-large |
| Card title | title-medium |
| Card body | body-medium |
| Dialog title | headline-small |
| Dialog body | body-medium |
| Dialog button | label-large |
| NavBar label | label-medium |
| Chip label | label-large |
| TextField label | body-large |
| AppBar title (small) | title-large |
| AppBar title (medium) | headline-small |
| AppBar title (large) | headline-medium |
| Switch label | body-large |
| Snackbar | body-medium |
| BottomSheet title | title-large |

---

## 3. 形状系统 (Shape) 完整参考

| Token | CSS 值 | 典型用途 |
|-------|--------|---------|
| `--md-sys-shape-none` | `0px` | Divider, Table |
| `--md-sys-shape-extra-small` | `4px` | Chip, Badge, Small tooltip |
| `--md-sys-shape-small` | `8px` | Card, TextField, Menu |
| `--md-sys-shape-medium` | `12px` | Dialog (默认), BottomSheet |
| `--md-sys-shape-large` | `16px` | FAB, Large Card |
| `--md-sys-shape-extra-large` | `28px` | Fullscreen Dialog, Modal |
| `--md-sys-shape-full` | `9999px` | Button (pill), Chip (部分), Badge (dot) |

### 组件 → 形状映射

| 组件 | 形状 |
|------|------|
| Button (all variants) | full |
| FAB | large |
| FAB small | medium |
| Card | medium |
| Dialog | extra-large |
| Chip | extra-small |
| TextField (filled) | extra-small (top-left + top-right) |
| TextField (outlined) | extra-small |
| Menu | extra-small |
| BottomSheet (top corners) | extra-large |
| Snackbar | extra-small |
| NavBar indicator | full |
| Switch track | full |
| Badge | full (dot) / extra-small (with label) |

---

## 4. 海拔系统 (Elevation / Tonal Elevation)

M3 采用 **Tonal Elevation**: 海拔升高不仅增加阴影，还会在 surface 上叠加一个颜色覆盖层。

| Level | Box Shadow | Surface Tonal Overlay | 典型用途 |
|-------|-----------|----------------------|---------|
| 0 | `none` | `0%` | Button, Chip, NavBar, Switch |
| 1 | `0 1px 2px rgba(0,0,0,0.3), 0 1px 3px 1px rgba(0,0,0,0.15)` | `5%` | Card (elevated), SearchBar (scroll) |
| 2 | `0 1px 2px rgba(0,0,0,0.3), 0 2px 6px 2px rgba(0,0,0,0.15)` | `8%` | FAB (resting), Menu |
| 3 | `0 4px 8px 3px rgba(0,0,0,0.15), 0 1px 3px rgba(0,0,0,0.3)` | `11%` | FAB (pressed), Dialog |
| 4 | `0 6px 10px 4px rgba(0,0,0,0.15), 0 2px 3px rgba(0,0,0,0.3)` | `12%` | BottomSheet |
| 5 | `0 8px 12px 6px rgba(0,0,0,0.15), 0 4px 4px rgba(0,0,0,0.3)` | `14%` | NavDrawer (modal) |

**M2→M3 关键变化**: M3 整体降低了海拔使用。Chip、NavBar、TopAppBar 默认无阴影。

---

## 5. 状态层 (State Layer)

状态层在组件上方叠加一个纯色，通过透明度控制强度。

| 状态 | 透明度 | 适用色 |
|------|--------|--------|
| hover | `0.08` | `on-surface` (一般) / `on-primary` (filled button) 等 |
| focus | `0.12` | 同上 |
| pressed | `0.12` | 同上 |
| dragged | `0.16` | 同上 |

实现示例:

```css
.component {
  position: relative;
}

.component::after {  /* state layer */
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: var(--md-sys-color-on-surface);
  opacity: 0;
  transition: opacity var(--md-sys-motion-duration-short2) var(--md-sys-motion-easing-standard);
  pointer-events: none;
}

.component:hover::after    { opacity: 0.08; }
.component:focus-visible::after { opacity: 0.12; }
.component:active::after   { opacity: 0.12; }
```

---

## 6. 动效系统 (Motion) 完整参考

### 6.1 缓动函数 (Easing)

| Token | 贝塞尔曲线 | 用途 |
|-------|-----------|------|
| `--md-sys-motion-easing-standard` | `cubic-bezier(0.2, 0, 0, 1)` | 标准过渡 |
| `--md-sys-motion-easing-standard-decelerate` | `cubic-bezier(0, 0, 0, 1)` | 元素出现/展开 |
| `--md-sys-motion-easing-standard-accelerate` | `cubic-bezier(0.3, 0, 1, 1)` | 元素消失/折叠 |
| `--md-sys-motion-easing-emphasized` | `cubic-bezier(0.2, 0, 0, 1)` | 强调动画 |
| `--md-sys-motion-easing-emphasized-decelerate` | `cubic-bezier(0.05, 0.7, 0.1, 1)` | 强调进入 |
| `--md-sys-motion-easing-emphasized-accelerate` | `cubic-bezier(0.3, 0, 0.8, 0.15)` | 强调退出 |

### 6.2 时长 (Duration)

```
short1: 50ms     short2: 100ms    short3: 150ms    short4: 200ms
medium1: 250ms   medium2: 300ms   medium3: 350ms   medium4: 400ms
long1: 450ms     long2: 500ms     long3: 550ms     long4: 600ms
extraLong1: 700ms  extraLong2: 800ms  extraLong3: 900ms  extraLong4: 1000ms
```

### 6.3 组件动画速查

| 交互 | 时长 | 缓动 |
|------|------|------|
| State layer (hover/press) | short2 (100ms) | standard |
| Ripple expand | short4 (200ms) | standard |
| Menu appear | medium1 (250ms) | emphasized-decelerate |
| Menu disappear | short4 (200ms) | emphasized-accelerate |
| Dialog appear | medium2 (300ms) | emphasized-decelerate |
| Dialog disappear | medium1 (250ms) | emphasized-accelerate |
| FAB extend/collapse | medium2 (300ms) | emphasized |
| Page transition | medium3 (350ms) | emphasized-decelerate |
| Snackbar appear | medium2 (300ms) | standard-decelerate |
| Snackbar disappear | medium1 (250ms) | standard-accelerate |

---

## 7. 断点 (Breakpoints) — 响应式

| 类型 | 范围 | CSS 媒体查询 |
|------|------|-------------|
| Compact | 0–599dp | `@media (max-width: 599px)` |
| Medium | 600–839dp | `@media (min-width: 600px) and (max-width: 839px)` |
| Expanded | 840dp+ | `@media (min-width: 840px)` |

### 响应式策略

| 组件 | Compact | Medium | Expanded |
|------|---------|--------|----------|
| Navigation | NavBar (bottom) | NavRail (side) | NavRail/Drawer |
| Dialog | Fullscreen | Default | Default |
| List-Detail | Separate pages | Side-by-side | Side-by-side |
| Card Grid | 1 column | 2 columns | 3-4 columns |
| AppBar | Small | Small | Small/Medium |

---

## 8. CSS 自定义属性完整声明块

```css
/* ============================================================
   MD3 Design Token — CSS Custom Properties 完整声明
   将以下代码块放在 :root {} 中以启用完整 MD3 主题
   ============================================================ */

:root {
  /* ----- Colors - Primary ----- */
  --md-sys-color-primary: #6750A4;
  --md-sys-color-on-primary: #FFFFFF;
  --md-sys-color-primary-container: #EADDFF;
  --md-sys-color-on-primary-container: #21005D;

  /* ----- Colors - Secondary ----- */
  --md-sys-color-secondary: #625B71;
  --md-sys-color-on-secondary: #FFFFFF;
  --md-sys-color-secondary-container: #E8DEF8;
  --md-sys-color-on-secondary-container: #1D192B;

  /* ----- Colors - Tertiary ----- */
  --md-sys-color-tertiary: #7D5260;
  --md-sys-color-on-tertiary: #FFFFFF;
  --md-sys-color-tertiary-container: #FFD8E4;
  --md-sys-color-on-tertiary-container: #31111D;

  /* ----- Colors - Error ----- */
  --md-sys-color-error: #B3261E;
  --md-sys-color-on-error: #FFFFFF;
  --md-sys-color-error-container: #F9DEDC;
  --md-sys-color-on-error-container: #410E0B;

  /* ----- Colors - Background & Surface ----- */
  --md-sys-color-background: #FFFBFE;
  --md-sys-color-on-background: #1C1B1F;
  --md-sys-color-surface: #FFFBFE;
  --md-sys-color-on-surface: #1C1B1F;
  --md-sys-color-surface-variant: #E7E0EC;
  --md-sys-color-on-surface-variant: #49454F;

  /* ----- Colors - Surface Container Hierarchy ----- */
  --md-sys-color-surface-dim: #DED8E1;
  --md-sys-color-surface-bright: #FFFBFE;
  --md-sys-color-surface-container-lowest: #FFFFFF;
  --md-sys-color-surface-container-low: #F7F2FA;
  --md-sys-color-surface-container: #F3EDF7;
  --md-sys-color-surface-container-high: #ECE6F0;
  --md-sys-color-surface-container-highest: #E6E0E9;

  /* ----- Colors - Outline ----- */
  --md-sys-color-outline: #79747E;
  --md-sys-color-outline-variant: #CAC4D0;

  /* ----- Colors - Inverse ----- */
  --md-sys-color-inverse-surface: #313033;
  --md-sys-color-inverse-on-surface: #F4EFF4;
  --md-sys-color-inverse-primary: #D0BCFF;

  /* ----- Colors - Shadow & Scrim ----- */
  --md-sys-color-shadow: #000000;
  --md-sys-color-scrim: #000000;

  /* ----- Typography — Display ----- */
  --md-sys-typescale-display-large-font: 'Roboto', sans-serif;
  --md-sys-typescale-display-large-weight: 400;
  --md-sys-typescale-display-large-size: 57px;
  --md-sys-typescale-display-large-tracking: -0.25px;
  --md-sys-typescale-display-large-line-height: 64px;

  --md-sys-typescale-display-medium-font: 'Roboto', sans-serif;
  --md-sys-typescale-display-medium-weight: 400;
  --md-sys-typescale-display-medium-size: 45px;
  --md-sys-typescale-display-medium-tracking: 0px;
  --md-sys-typescale-display-medium-line-height: 52px;

  --md-sys-typescale-display-small-font: 'Roboto', sans-serif;
  --md-sys-typescale-display-small-weight: 400;
  --md-sys-typescale-display-small-size: 36px;
  --md-sys-typescale-display-small-tracking: 0px;
  --md-sys-typescale-display-small-line-height: 44px;

  /* ----- Typography — Headline ----- */
  --md-sys-typescale-headline-large-font: 'Roboto', sans-serif;
  --md-sys-typescale-headline-large-weight: 400;
  --md-sys-typescale-headline-large-size: 32px;
  --md-sys-typescale-headline-large-tracking: 0px;
  --md-sys-typescale-headline-large-line-height: 40px;

  --md-sys-typescale-headline-medium-font: 'Roboto', sans-serif;
  --md-sys-typescale-headline-medium-weight: 400;
  --md-sys-typescale-headline-medium-size: 28px;
  --md-sys-typescale-headline-medium-tracking: 0px;
  --md-sys-typescale-headline-medium-line-height: 36px;

  --md-sys-typescale-headline-small-font: 'Roboto', sans-serif;
  --md-sys-typescale-headline-small-weight: 400;
  --md-sys-typescale-headline-small-size: 24px;
  --md-sys-typescale-headline-small-tracking: 0px;
  --md-sys-typescale-headline-small-line-height: 32px;

  /* ----- Typography — Title ----- */
  --md-sys-typescale-title-large-font: 'Roboto', sans-serif;
  --md-sys-typescale-title-large-weight: 400;
  --md-sys-typescale-title-large-size: 22px;
  --md-sys-typescale-title-large-tracking: 0px;
  --md-sys-typescale-title-large-line-height: 28px;

  --md-sys-typescale-title-medium-font: 'Roboto', sans-serif;
  --md-sys-typescale-title-medium-weight: 500;
  --md-sys-typescale-title-medium-size: 16px;
  --md-sys-typescale-title-medium-tracking: 0.15px;
  --md-sys-typescale-title-medium-line-height: 24px;

  --md-sys-typescale-title-small-font: 'Roboto', sans-serif;
  --md-sys-typescale-title-small-weight: 500;
  --md-sys-typescale-title-small-size: 14px;
  --md-sys-typescale-title-small-tracking: 0.1px;
  --md-sys-typescale-title-small-line-height: 20px;

  /* ----- Typography — Body ----- */
  --md-sys-typescale-body-large-font: 'Roboto', sans-serif;
  --md-sys-typescale-body-large-weight: 400;
  --md-sys-typescale-body-large-size: 16px;
  --md-sys-typescale-body-large-tracking: 0.5px;
  --md-sys-typescale-body-large-line-height: 24px;

  --md-sys-typescale-body-medium-font: 'Roboto', sans-serif;
  --md-sys-typescale-body-medium-weight: 400;
  --md-sys-typescale-body-medium-size: 14px;
  --md-sys-typescale-body-medium-tracking: 0.25px;
  --md-sys-typescale-body-medium-line-height: 20px;

  --md-sys-typescale-body-small-font: 'Roboto', sans-serif;
  --md-sys-typescale-body-small-weight: 400;
  --md-sys-typescale-body-small-size: 12px;
  --md-sys-typescale-body-small-tracking: 0.4px;
  --md-sys-typescale-body-small-line-height: 16px;

  /* ----- Typography — Label ----- */
  --md-sys-typescale-label-large-font: 'Roboto', sans-serif;
  --md-sys-typescale-label-large-weight: 500;
  --md-sys-typescale-label-large-size: 14px;
  --md-sys-typescale-label-large-tracking: 0.1px;
  --md-sys-typescale-label-large-line-height: 20px;

  --md-sys-typescale-label-medium-font: 'Roboto', sans-serif;
  --md-sys-typescale-label-medium-weight: 500;
  --md-sys-typescale-label-medium-size: 12px;
  --md-sys-typescale-label-medium-tracking: 0.5px;
  --md-sys-typescale-label-medium-line-height: 16px;

  --md-sys-typescale-label-small-font: 'Roboto', sans-serif;
  --md-sys-typescale-label-small-weight: 500;
  --md-sys-typescale-label-small-size: 11px;
  --md-sys-typescale-label-small-tracking: 0.5px;
  --md-sys-typescale-label-small-line-height: 16px;

  /* ----- Shape ----- */
  --md-sys-shape-none: 0px;
  --md-sys-shape-extra-small: 4px;
  --md-sys-shape-small: 8px;
  --md-sys-shape-medium: 12px;
  --md-sys-shape-large: 16px;
  --md-sys-shape-extra-large: 28px;
  --md-sys-shape-full: 9999px;

  /* ----- Motion Easing ----- */
  --md-sys-motion-easing-standard: cubic-bezier(0.2, 0, 0, 1);
  --md-sys-motion-easing-standard-decelerate: cubic-bezier(0, 0, 0, 1);
  --md-sys-motion-easing-standard-accelerate: cubic-bezier(0.3, 0, 1, 1);
  --md-sys-motion-easing-emphasized: cubic-bezier(0.2, 0, 0, 1);
  --md-sys-motion-easing-emphasized-decelerate: cubic-bezier(0.05, 0.7, 0.1, 1);
  --md-sys-motion-easing-emphasized-accelerate: cubic-bezier(0.3, 0, 0.8, 0.15);

  /* ----- Motion Duration ----- */
  --md-sys-motion-duration-short1: 50ms;
  --md-sys-motion-duration-short2: 100ms;
  --md-sys-motion-duration-short3: 150ms;
  --md-sys-motion-duration-short4: 200ms;
  --md-sys-motion-duration-medium1: 250ms;
  --md-sys-motion-duration-medium2: 300ms;
  --md-sys-motion-duration-medium3: 350ms;
  --md-sys-motion-duration-medium4: 400ms;
  --md-sys-motion-duration-long1: 450ms;
  --md-sys-motion-duration-long2: 500ms;
  --md-sys-motion-duration-long3: 550ms;
  --md-sys-motion-duration-long4: 600ms;
  --md-sys-motion-duration-extra-long1: 700ms;
  --md-sys-motion-duration-extra-long2: 800ms;
  --md-sys-motion-duration-extra-long3: 900ms;
  --md-sys-motion-duration-extra-long4: 1000ms;

  /* ----- State Layer Opacity ----- */
  --md-sys-state-layer-hover-opacity: 0.08;
  --md-sys-state-layer-focus-opacity: 0.12;
  --md-sys-state-layer-pressed-opacity: 0.12;
  --md-sys-state-layer-dragged-opacity: 0.16;
}
```

---

## 9. M2 → M3 Token 迁移指南

> 从 Material Design 2 升级到 Material Design 3 的 Design Token 映射与迁移策略。

### 9.1 Token 名称映射 (新增/更名/删除)

| M2 Token | M3 Token | 变更类型 |
|----------|----------|---------|
| `primary` | `primary` | **保留** |
| `primary-variant` | `primary-container` | **重命名** |
| `secondary` | `secondary` | **保留** |
| `secondary-variant` | `secondary-container` | **重命名** |
| `background` | `background` | **保留** |
| `surface` | `surface` | **保留** |
| — | `surface-container-lowest` | **新增** |
| — | `surface-container-low` | **新增** |
| — | `surface-container` | **新增** |
| — | `surface-container-high` | **新增** |
| — | `surface-container-highest` | **新增** |
| `error` | `error` | **保留** |
| `on-*` 系列 | `on-*` 系列 | **保留**（部分 on-* 的 anchor 变化） |
| — | `surface-dim` / `surface-bright` | **新增** |
| — | `outline-variant` | **新增** |
| — | `inverse-surface` / `inverse-on-surface` | **新增** |
| — | `inverse-primary` | **新增** |
| `shadow` | `shadow` | **保留**（色调值变化） |
| `scrim` | `scrim` | **保留** |

### 9.2 删除的概念

| M2 概念 | 替代方案 |
|---------|---------|
| `primary-variant` | 使用 `primary-container` + `on-primary-container` |
| `secondary-variant` | 使用 `secondary-container` + `on-secondary-container` |
| `elevation-overlay` (半透明覆盖) | M3 改用 Tonal Elevation（surface 上叠加色调） |
| 固定 5 种 elevation 级别 | M3 扩展为 6 级 + surface container 5 级层次 |
| `--mdc-*` 命名空间 | 全部改为 `--md-sys-*` 命名空间 |
| 固定色板 (50–900) | HCT Tonal Palette (Tone 0–100) |

### 9.3 迁移步骤

1. **全局替换命名空间**: `--mdc-*` → `--md-sys-*`
2. **替换 variant 映射**:
   ```
   primary-variant → primary-container
   on-primary          → on-primary-container (当用于 variant 上内容时)
   secondary-variant   → secondary-container
   ```
3. **替换 surface/background 层次**: 将原来的 `@surface` 拆分到 5 级 `surface-container-*`
4. **更新 elevation 实现**: 从纯 box-shadow 改为 Tonal Elevation (颜色叠加 + shadow)
5. **适配 HCT 色值**: M2 的 primary `#6200EE` → M3 默认 `#6750A4`（Tone 40 对照 HCT）
6. **验证对比度**: 使用 Contrast Level 工具验证 WCAG 合规性

### 9.4 代码迁移示例

**M2 迁移前:**
```css
:root {
  --mdc-theme-primary: #6200EE;
  --mdc-theme-primary-variant: #3700B3;
  --mdc-theme-secondary: #03DAC6;
  --mdc-theme-background: #FFFFFF;
  --mdc-theme-surface: #FFFFFF;
}
```
**M3 迁移后:**
```css
:root {
  --md-sys-color-primary: #6750A4;
  --md-sys-color-primary-container: #EADDFF;
  --md-sys-color-secondary: #625B71;
  --md-sys-color-secondary-container: #E8DEF8;
  --md-sys-color-background: #FFFBFE;
  --md-sys-color-surface: #FFFBFE;
}
```
