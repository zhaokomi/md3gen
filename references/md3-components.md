# MD3 组件规范完整参考

> Material Design 3 全部组件的详细规格。用于 `/md3 <component>` 命令生成代码时的规范依据。

---

## 组件索引

| 分类 | 组件 | 变体 |
|------|------|------|
| **Actions** | Button, FAB, IconButton, SegmentedButton | filled/outlined/text/elevated/tonal, 6 FAB variants, 4 icon button variants |
| **Communication** | Badge, Progress Indicator, Snackbar | —, linear/circular, — |
| **Containment** | Card, Dialog, BottomSheet, SideSheet, Divider | elevated/filled/outlined, basic/fullscreen, —, —, — |
| **Navigation** | NavigationBar, NavigationRail, NavigationDrawer, Tabs, AppBar, Search | bar/rail/drawer, primary/secondary, standard/modal, —, center/small/medium/large, — |
| **Selection** | Checkbox, Chip, DatePicker, Menu, RadioButton, Slider, Switch, TimePicker | —, assist/filter/input/suggestion, —, —, —, —, —, — |
| **Text Inputs** | TextField | filled/outlined |
| **Other** | Tooltip, ListItem, Carousel | plain/rich, 1-3line, — |

---

## Actions 动作组件

### Button 按钮

```
高度: 40dp
最小宽: 48dp
Horizontal padding: 24dp
Shape: full (9999px = pill)
Typography: label-large (14sp, 500w)
State layer: yes
Ripple: yes
```

#### Filled Button

```
背景: primary
文字: on-primary
轮廓: none
海拔: 0 (no shadow)
图标间距: 8dp
```

#### Outlined Button

```
背景: transparent
文字: primary
轮廓: outline (1px)
海拔: 0
```

#### Text Button

```
背景: transparent
文字: primary
轮廓: none
海拔: 0
Padding: 12dp horizontal
```

#### Elevated Button

```
背景: surface-container-low
文字: primary
轮廓: none
海拔: level 1
Shadow: level 1 box-shadow
```

#### Tonal Button

```
背景: secondary-container
文字: on-secondary-container
轮廓: none
海拔: 0
```

---

### FAB (Floating Action Button)

#### 尺寸表

| Variant | 尺寸 | 图标 | Shape | 文字 |
|---------|------|------|-------|------|
| Primary (default) | 56x56dp | 24dp | large (16px) | — |
| Small | 40x40dp | 24dp | medium (12px) | — |
| Large | 96x96dp | 36dp | large (16px) | — |
| Extended | h:56dp | 24dp | large (16px) | label-large |

#### 颜色表

| Variant | 背景 | 图标色 |
|---------|------|--------|
| Primary | primary-container | on-primary-container |
| Surface | surface-container-high | primary |
| Secondary | secondary-container | on-secondary-container |
| Tertiary | tertiary-container | on-tertiary-container |

#### M3 vs M2

- M2: 圆形, primary 背景
- M3: 圆角矩形 (16px), primary-container 背景
- M3 新增 Large (96dp) 尺寸

---

### IconButton 图标按钮

#### Variants

| Variant | 背景 | 图标色 |
|---------|------|--------|
| Standard | transparent | on-surface-variant |
| Filled | primary | on-primary |
| Tonal | surface-variant | on-surface-variant |
| Outlined | transparent | on-surface-variant (border: outline) |

```
尺寸: 40x40dp
图标: 24dp
Shape: full (9999px)
State layer: yes
```

#### Toggle IconButton

- 支持选中/未选中状态切换
- 选中态: filled variant 样式

---

## Communication 通信组件

### Badge 徽标

```
Shape: full (dot) / extra-small (with number)
最小尺寸: 6x6dp (dot) / 16dp height (with number)
Typography: label-small
Color: error
```

### Progress Indicator 进度指示器

#### Linear

```
Track height: 4dp
Active indicator: primary
Track: surface-variant (12% opacity on surface)
Stop indicator: primary-container (optional)
```

#### Circular

```
Size: 48dp (default) / 24dp (small)
Stroke width: 4dp
Active indicator: primary
Track: surface-variant
```

### Snackbar 消息条

```
Shape: extra-small (4px)
Background: inverse-surface
Text: inverse-on-surface
Typography: body-medium
Action button: inverse-primary
Max width: 360dp (Compact) / 480dp (Expanded)
Margin: 16dp (Compact) / 24dp (Expanded)
Position: bottom, centered
Duration: short (4s) / long (10s)
Elevation: level 3
```

---

## Containment 容器组件

### Card 卡片

```
Shape: medium (12px)
```

| Variant | Background | Elevation | Outline |
|---------|-----------|-----------|---------|
| Elevated | surface-container-low | level 1 | none |
| Filled | surface-container-highest | 0 | none |
| Outlined | surface | 0 | outline-variant (1px) |

### Dialog 对话框

```
Shape: extra-large (28px)
Min width: 280dp
Max width: 560dp (Compact/Medium) / fullscreen (Compact alternative)
```

| 区域 | Typography | 说明 |
|------|-----------|------|
| Title | headline-small (24sp) | 可带图标 |
| Content | body-medium (14sp) | 最多2段 |
| Actions | label-large (14sp) | 右对齐 |

```
Padding: 24dp
Content padding: 16dp top + 24dp bottom
Button spacing: 8dp
Title icon: 24dp (optional)
```

#### Fullscreen Dialog

```
Top app bar: 包含关闭按钮
Content: scrollable
Actions: 固定在底部
```

### BottomSheet 底部面板

```
Top corners shape: extra-large (28px)
Background: surface-container-low
Drag handle: on-surface-variant (38% opacity), 32x4dp
Min height: 1/3 screen
Max height: depends on content
```

### SideSheet 侧面板

M3 新增组件，从屏幕右侧滑入的模态面板。与 NavDrawer (左侧) 对称，适合详情编辑/筛选等操作。

```
Width: 360dp (standard) / fullscreen (compact)
Background: surface-container
Shape: start corners large (16px, inline-start — 面向内容侧圆角)
Elevation: level 3 (显示时)
Scrim: scrim (显示时覆盖主内容)
Duration: medium2 (300ms) enter, medium1 (250ms) exit
Easing: emphasized-decelerate (enter) / emphasized-accelerate (exit)
```

| 区域 | 规格 |
|------|------|
| **Header** | 可用 title-large (22sp)，leading icon 关闭按钮 |
| **Content** | body-medium (14sp)，可滚动 |
| **Actions** | 底部固定，label-large (14sp) |

**SideSheet vs NavigationDrawer:**

| 特性 | SideSheet | NavigationDrawer |
|------|-----------|-----------------|
| 方向 | 右侧滑入 | 左侧滑入 |
| 用途 | 详情/编辑/筛选面板 | 主导航菜单 |
| 关闭方式 | 右滑手势 / 点击scrim | 左滑手势 / 点击scrim |
| 背景色 | `surface-container` | `surface` |

**与 Predictive Back 配合**: SideSheet 支持预测性返回手势，右滑时预览主内容页。

### Divider 分割线

```
Height: 1dp
Color: outline-variant
Inset: 0dp (full-width) / 16dp (with list) / 72dp (with icon)
```

---

## Navigation 导航组件

### NavigationBar 底部导航栏

```
Height: 80dp
Background: surface
Elevation: 0 (M3 无阴影)
Item: max 5
Active indicator: secondary-container + outline
```

| Element | Size | Typography |
|---------|------|-----------|
| Icon (active) | 24dp | — |
| Icon (inactive) | 24dp | — |
| Label | — | label-medium (12sp) |
| Indicator | 32x64dp (full shape) | — |

### NavigationRail 侧边导航栏

```
Width: 80dp
Background: surface
Item: max 7
用法: Medium screen (600-839dp) 替代 NavBar
```

### NavigationDrawer 抽屉导航

```
Modal width: 360dp
Standard width: 360dp (permanent)
Background: surface
Shape: end corners large (16px)
Elevation: level 1 (standard) / level 0 (modal)
```

### Top App Bar 顶部应用栏

| Variant | 高度 | Scroll行为 |
|---------|------|-----------|
| Center-aligned | 64dp | 标题始终居中 |
| Small | 64dp | 标准行为 |
| Medium | 112dp | 折叠时标题缩小 |
| Large | 152dp | 折叠时标题缩小 |

```
Background: surface
Elevation: 0 (默认, 滚动后增加 level 2)
Typography: title-large (small) → headline-small (medium) → headline-medium (large)
Leading icon: 24dp (navigation icon / menu)
Trailing icons: 24dp (max 3)
```

**M2→M3 关键变化**: 删除了 `primary-variant` 定义，AppBar 更沉浸。

### Tabs 标签页

```
Height: 48dp
Divider: outline-variant (1dp, bottom)
Active indicator: primary (3dp height)
Typography: title-small (14sp)
```

### Search 搜索

```
SearchBar height: 56dp (collapsed) / varies (expanded)
Shape: full (pill) → extra-large (expanded view)
Background: surface-container-high
```

---

## Selection 选择组件

### Chip 标签

```
Height: 32dp
Shape: extra-small (4px)
Typography: label-large (14sp)
Leading icon: 18dp (optional)
Trailing icon: 18dp (optional, for close)
```

| Variant | 用途 | 默认状态 |
|---------|------|---------|
| Assist | 辅助操作 | 无选中态 |
| Filter | 多选筛选 | toggle 选中态 |
| Input | 输入型标签 | trailing 关闭图标 |
| Suggestion | 建议操作 | 无选中态 |

**M2→M3 关键变化**: Action Chip 拆分为 Assist + Suggestion；默认无阴影。

### Checkbox 复选框

```
Size: 24dp
Shape: extra-small (4px)
Unchecked: outline (2dp border)
Checked: primary fill + on-primary check icon
Indeterminate: primary fill + minus icon
State layer: yes
Touch target: 48x48dp
```

### RadioButton 单选按钮

```
Size: 20dp (outer circle) / 10dp (inner dot)
Unchecked: outline (2dp border)
Checked: primary outer + primary inner dot
```

### Switch 开关

```
Track: 52x32dp
Thumb: 24dp (unchecked) → 24dp (checked)
Track shape: full (9999px)
```

| State | Track Color | Thumb Color |
|-------|------------|-------------|
| Unchecked | surface-variant | outline |
| Checked | primary | on-primary |
| Hover | state layer (8%) | — |
| Focus | state layer (12%) | — |

**M2→M3**: 新增加对勾图标在 track 内；面积更大；无阴影。

### Slider 滑块

```
Track height: 4dp (inactive) / 4dp (active)
Active track: primary
Inactive track: surface-variant
Thumb: primary (20dp), on-primary (inner dot)
Tick marks: on-surface-variant (opacity 38%)
Labels: above thumb
```

### Menu 菜单

```
Shape: extra-small (4px)
Background: surface-container
Elevation: level 2
Min width: 112dp
Max width: 280dp
Item height: 48dp
Item padding: 12dp horizontal
Divider: inside menu, outline-variant
```

### DatePicker 日期选择器

```
Day cell: 40x40dp
Shape: full (selected day)
Today indicator: primary outline
Selected: primary-container + on-primary-container
Weekday headers: label-small
Month/Year: title-medium
```

### TimePicker 时间选择器

```
Dial face: surface-container-highest (40dp)
Dial selector: primary
Time input: body-large
Period selector (AM/PM): segmented button
```

---

## Text Inputs 文本输入

### TextField 文本输入框

| Variant | Shape | 特征 |
|---------|-------|------|
| Filled | top corners extra-small (4px) | filled background |
| Outlined | extra-small (4px) | transparent bg, outline edge |

```
Min height: 56dp
Padding: 16dp horizontal (start), 12dp (end)
```

| Element | Typography | Color |
|---------|-----------|-------|
| Label | body-large (16sp) → label-small (float) | on-surface-variant |
| Input text | body-large (16sp) | on-surface |
| Supporting text | body-small (12sp) | on-surface-variant / error |
| Trailing icon | 24dp | on-surface-variant |
| Leading icon | 24dp | on-surface-variant |

#### States

| State | Filled BG | Outline |
|-------|-----------|---------|
| Default | surface-container-highest | outline |
| Focus | surface-container-highest | primary (2px) |
| Error | surface-container-highest | error (2px) |
| Disabled | on-surface (4% opacity) | on-surface (12% opacity) |

---

## Other 其他组件

### Tooltip 工具提示

```
Background: inverse-surface
Text: inverse-on-surface
Typography: body-small (12sp)
Shape: extra-small (4px)
Padding: 4dp horizontal, 4dp vertical (plain) / 8dp (rich)
Delay: 500ms (show), 1500ms (show + persist)
```

### ListItem 列表项

```
Min height: 56dp (1-line) / 72dp (2-line) / 88dp (3-line)
Padding: 16dp horizontal (start), 24dp (end)
```

| Element | Size | Typography |
|---------|------|-----------|
| Leading icon | 24dp | — |
| Leading avatar | 40x40dp (circle) | — |
| Leading image | 56x56dp | — |
| Title | — | body-large |
| Subtitle | — | body-medium |
| Supporting text | — | body-medium |
| Trailing icon | 24dp | — |
| Trailing text | — | label-small |

### Carousel 轮播

M3 新增组件，支持水平滚动的内容轮播。支持多种 item 大小和对齐策略。

```
Height: item height (可变)
Item padding: 4dp (between items)
Scroll snap: mandatory (默认)
Scroll bar: 可选 (默认隐藏)
```

| 策略 | 说明 |
|------|------|
| **Multi-browse** | 多个 item 可见，最后一个 item peek 提示用户滚动 |
| **Hero** | 一个大 item 占主导，左右 peek 小部分 item |
| **Uncontained** | items 从屏幕边缘 bleed，无容器边界感 |
| **Full-screen** | 全屏 item，一次只显示一个，通常带 indicator dots |

| 属性 | 值 |
|------|-----|
| **Scroll transition** | 300ms (`medium2`) + `emphasized-decelerate` |
| **Snap alignment** | start / center / end |
| **Indicator dots** | `on-surface-variant` (inactive) / `primary` (active), 8dp spacing |
| **Focus ring** | primary, 2dp offset |
| **Keyboard** | Left/Right arrows 切换 item |

**Carousel Item 内部布局:**

```
┌─────────────────────────────────┐
│                                 │
│            Image/Media          │
│                                 │
├─────────────────────────────────┤
│  Title (title-medium)           │
│  Subtitle (body-medium)         │
│  Actions (text button)          │
└─────────────────────────────────┘
```

**与 Predictive Back 配合**: 全屏 Carousel 支持水平滑动返回，预览上一张 item。

### Toolbar / SegmentedButton

```
Height: 40dp
Shape: full (9999px)
Background: surface-container-high (unselected) / secondary-container (selected)
Outline: outline (entire group border)
Typography: label-large (14sp)
Divider: between segments, on-surface (12% opacity)
```

---

## Gestures 手势交互

### Predictive Back Gesture 预测性返回

M3 新增核心手势，系统级返回操作时动态预览目标页面，提供空间导航感知。

```
触发: 从屏幕边缘向内滑动 (Android gesture navigation)
视觉: 当前页缩小并跟随手指位移，目标页从后方逐渐显现
时长: medium2 (300ms)
缓动: emphasized-decelerate
```

| 阶段 | 动画 | 说明 |
|------|------|------|
| **Pulling** | 当前页跟随手指缩放+位移 | 缩放至 ~90%，透明度不变 |
| **Preview** | 目标页 fade in | 目标页从后方以 80% opacity 出现 |
| **Confirm** | 当前页 slide out + scale down | Shared Axis X 方向动画 |
| **Cancel** | 回弹 | 手指回滑至边缘，页面 elastic 回位 |

**适配组件列表：**

| 组件 | 预测方向 | 预览内容 |
|------|---------|---------|
| SideSheet | 右侧 ← 主内容 | 主页面从左侧出现 |
| NavDrawer | 左侧 ← 主内容 | 主页面从右侧出现 |
| BottomSheet | 上 ← 主内容 | 底部收起预览 |
| Dialog | 缩小 + 透明度 | 底层页面 fade in |
| Carousel (full-screen) | 左/右 ← prev/next | 相邻 item peek |
| Page Navigation | 左 ← 上一页 | 上一页从右侧 peek |

**CSS 实现关键点：**

```css
/* 预测性返回容器 */
.page-container {
  transition: transform var(--md-sys-motion-duration-medium2) var(--md-sys-motion-easing-emphasized);
  will-change: transform;
}

/* 目标页预览层 (z-index 低于当前页) */
.preview-page {
  position: absolute;
  inset: 0;
  z-index: -1;
  opacity: 0.8;
  transform: scale(0.95);
}

/* 当前页跟随手指 */
.page-container.swiping {
  transition: none; /* 拖拽时去掉过渡，跟随手指 */
  transform: translateX(var(--swipe-offset, 0px));
}

/* 松手确认后 */
.page-container.confirmed {
  transform: translateX(100%);
}

/* 取消回弹 */
.page-container.cancelled {
  transform: translateX(0);
  transition: transform var(--md-sys-motion-duration-medium2) var(--md-sys-motion-easing-emphasized);
}
```

**无障碍**: 不支持手势操作的用户应提供明确的返回按钮作为替代交互。

---

## 无障碍速查

| 组件 | 键盘操作 | ARIA |
|------|---------|------|
| Button | Enter, Space | role="button" |
| FAB | Enter, Space | role="button", aria-label |
| Dialog | Escape, Tab trap | role="dialog", aria-modal, aria-labelledby |
| Switch | Space | role="switch", aria-checked |
| Checkbox | Space | role="checkbox", aria-checked |
| Radio | Arrow keys | role="radio", aria-checked |
| Slider | Arrow keys, Home/End | role="slider", aria-valuenow |
| Menu | Arrow keys, Escape | role="menu", role="menuitem" |
| Tabs | Left/Right arrows | role="tablist", role="tab" |
| NavBar | Tab | role="navigation", aria-current |
| TextField | — | role="textbox" / aria-invalid (error) |
| Snackbar | — | role="alert", aria-live="polite" |
| ProgressBar | — | role="progressbar", aria-valuenow |
| Chip (input) | Backspace | role="button" |
