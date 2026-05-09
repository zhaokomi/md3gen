---
name: md3gen
description: >
  Material Design 3 组件与模板快速生成器。当用户需要生成 MD3 风格 UI 组件（Button、Card、Dialog、FAB、NavBar、Chip 等 40+ 组件）、页面模板（登录页、仪表盘、设置页、列表页等 15+ 模板）、或 MD3 主题/令牌配置时使用。支持 React (MUI v5+ / 纯 CSS)、Vue 3 (Vuetify 3 / 纯 CSS)、Angular Material、Flutter、Lit/Web Components、纯 HTML/CSS 六大技术栈。支持动态取色 (Dynamic Color)、HCT 色彩空间、暗色模式自动适配、RTL、无障碍检查、响应式断点 (Compact/Medium/Expanded)。
  触发短语：/md3、MD3、Material Design 3、Material You、material design 组件、md3 button/card/dialog、HCT 色彩、动态配色。
---

# MD3 组件快速生成器 (md3gen)

> 依据 Material Design 3 最新规范，快速生成跨框架 UI 组件、页面模板与主题配置。

## 工作流概览

```
用户触发 /md3 命令
       │
       ├── 命令解析 (组件/模板/主题)
       │         │
       │         ▼
       │    ┌─────────────────────────────┐
       │    │  1. 加载参考文件              │
       │    │     组件生成 → md3-components │
       │    │     模板生成 → md3-templates  │
       │    │     主题生成 → md3-tokens     │
       │    └─────────────┬───────────────┘
       │                  ▼
       │    ┌─────────────────────────────┐
       │    │  2. 确定目标框架+样式方案    │
       │    │     (读取用户配置或询问)     │
       │    └─────────────┬───────────────┘
       │                  ▼
       │    ┌─────────────────────────────┐
       │    │  3. 生成组件代码             │
       │    │     参考 §3 示例格式         │
       │    │     (TSX/JSX/Vue/HTML/CSS)  │
       │    └─────────────┬───────────────┘
       │                  ▼
       │    ┌─────────────────────────────┐
       │    │  4. 自检: 是否符合 MD3 规范  │
       │    │     - 颜色槽使用是否正确      │
       │    │     - 字体阶梯是否匹配        │
       │    │     - 圆角/海拔是否合规        │
       │    │     - 状态层是否存在          │
       │    │     - 暗色模式是否适配        │
       │    └─────────────┬───────────────┘
       │                  ▼
       │             输出代码 + 使用说明
```

**CRITICAL**: 生成具体组件时，必须先用 Read 工具读取 `references/md3-components.md` 获取该组件的详细规格（尺寸、颜色、字型映射等）。SKILL.md 中的组件规则（§2）是摘要，详细规格在 references 中。

## 命令参考 (CRITICAL — 识别用户意图)

### 组件生成

| 命令 | 参数 | 说明 |
|------|------|------|
| `/md3 button [variant]` | filled, outlined, text, elevated, tonal | 5 种按钮变体 |
| `/md3 card [variant]` | elevated, filled, outlined | 3 种卡片变体 |
| `/md3 chip [variant]` | assist, filter, input, suggestion | 4 种标签变体 |
| `/md3 dialog [type]` | basic, fullscreen | 2 种对话框 |
| `/md3 fab [variant]` | primary, secondary, tertiary, surface, small, large | 6 种 FAB |
| `/md3 navbar [type]` | bar, rail, drawer | 3 种导航 |
| `/md3 textfield [variant]` | filled, outlined | 2 种输入框 |
| `/md3 switch` | — | 开关 |
| `/md3 checkbox` | — | 复选框 |
| `/md3 radio` | — | 单选按钮 |
| `/md3 slider` | — | 滑块 |
| `/md3 progress [type]` | linear, circular | 进度条 |
| `/md3 iconbutton [variant]` | standard, filled, tonal, outlined | 4 种图标按钮 |
| `/md3 badge` | — | 徽标 |
| `/md3 divider` | — | 分割线 |
| `/md3 listitem` | — | 列表项 |
| `/md3 menu` | — | 菜单 |
| `/md3 snackbar` | — | 消息条 |
| `/md3 bottomsheet` | — | 底部面板 |
| `/md3 tabs` | — | 标签页 |
| `/md3 tooltip` | — | 工具提示 |
| `/md3 searchbar` | — | 搜索栏 |
| `/md3 datepicker` | — | 日期选择器 |
| `/md3 timepicker` | — | 时间选择器 |
| `/md3 appbar` | center, small, medium, large | 应用栏 |

### 页面模板生成

| 命令 | 参数 |
|------|------|
| `/md3 template login` | 登录/注册页 |
| `/md3 template dashboard` | 仪表盘 |
| `/md3 template settings` | 设置页 |
| `/md3 template list` | 列表页 (支持 --with-search, --with-fab) |
| `/md3 template detail` | 详情页 (支持 --with-appbar, --with-bottomsheet) |
| `/md3 template onboarding` | 引导页 (支持 --steps=N) |
| `/md3 template profile` | 个人主页 |
| `/md3 template checkout` | 结账/支付页 |
| `/md3 template chat` | 聊天界面 |
| `/md3 template feed` | 动态/信息流 |
| `/md3 template gallery` | 图片/媒体画廊 |
| `/md3 template calendar` | 日历视图 |
| `/md3 template form` | 表单页 |
| `/md3 template empty` | 空状态页 |
| `/md3 template error` | 错误页/404 |

### 主题系统

| 命令 | 说明 |
|------|------|
| `/md3 theme generate --seed=#6750A4` | 从种子色生成完整色彩方案 |
| `/md3 theme dark` | 生成暗色主题 |
| `/md3 theme light` | 生成亮色主题 |
| `/md3 theme export --format=css` | 导出 CSS Custom Properties |
| `/md3 theme export --format=scss` | 导出 SCSS 变量 |
| `/md3 theme export --format=json` | 导出 JSON tokens |
| `/md3 theme export --format=tailwind` | 导出 Tailwind CSS preset |
| `/md3 theme export --format=flutter` | 导出 Flutter ThemeData |

### 自然语言页面

| 命令 | 说明 |
|------|------|
| `/md3 page [自然语言描述]` | 自动规划组件组合，生成完整页面 |

例: `/md3 page "一个音乐播放器界面，底部有播放控制栏"`

### 配置

| 命令 | 说明 |
|------|------|
| `/md3 config --framework=react --style=css` | 设置默认技术栈 |
| `/md3 config --lang=zh` | 设置界面语言 |

---

## 1. MD3 核心设计令牌 (Design Tokens)

生成任何组件前，必须先确保以下 CSS 自定义属性已就位。这些令牌是所有组件的基础。

### 1.1 色彩系统 — 25 个颜色槽 (Color Roles)

3 组颜色槽：**AccentColor**（primary/secondary/tertiary）+ **NeutralColor**（background/surface/surfaceContainer 5级）+ **AdditionalColor**（error/outline/inverse/shadow/scrim）。每组含主色+容器色配对的 4 色调。

**亮色主题基准值 (seed: #6750A4):**

| Token | 值 | Token | 值 |
|-------|-----|-------|-----|
| `--md-sys-color-primary` | `#6750A4` | `--md-sys-color-surface` | `#FFFBFE` |
| `--md-sys-color-on-primary` | `#FFFFFF` | `--md-sys-color-on-surface` | `#1C1B1F` |
| `--md-sys-color-primary-container` | `#EADDFF` | `--md-sys-color-surface-variant` | `#E7E0EC` |
| `--md-sys-color-on-primary-container` | `#21005D` | `--md-sys-color-on-surface-variant` | `#49454F` |
| `--md-sys-color-secondary` | `#625B71` | `--md-sys-color-outline` | `#79747E` |
| `--md-sys-color-on-secondary` | `#FFFFFF` | `--md-sys-color-outline-variant` | `#CAC4D0` |
| `--md-sys-color-secondary-container` | `#E8DEF8` | `--md-sys-color-error` | `#B3261E` |
| `--md-sys-color-on-secondary-container` | `#1D192B` | `--md-sys-color-on-error` | `#FFFFFF` |
| `--md-sys-color-tertiary` | `#7D5260` | `--md-sys-color-error-container` | `#F9DEDC` |
| `--md-sys-color-on-tertiary` | `#FFFFFF` | `--md-sys-color-on-error-container` | `#410E0B` |
| `--md-sys-color-tertiary-container` | `#FFD8E4` | `--md-sys-color-background` | `#FFFBFE` |
| `--md-sys-color-on-tertiary-container` | `#31111D` | `--md-sys-color-on-background` | `#1C1B1F` |

### 1.2 字体系统 (Typography) — 15 级阶梯

| Token | Weight | Size | Letter-Spacing | Line-Height |
|-------|--------|------|----------------|-------------|
| `display-large` | 400 | 57px | -0.25px | 64px |
| `display-medium` | 400 | 45px | 0px | 52px |
| `display-small` | 400 | 36px | 0px | 44px |
| `headline-large` | 400 | 32px | 0px | 40px |
| `headline-medium` | 400 | 28px | 0px | 36px |
| `headline-small` | 400 | 24px | 0px | 32px |
| `title-large` | 400 | 22px | 0px | 28px |
| `title-medium` | 500 | 16px | 0.15px | 24px |
| `title-small` | 500 | 14px | 0.1px | 20px |
| `body-large` | 400 | 16px | 0.5px | 24px |
| `body-medium` | 400 | 14px | 0.25px | 20px |
| `body-small` | 400 | 12px | 0.4px | 16px |
| `label-large` | 500 | 14px | 0.1px | 20px |
| `label-medium` | 500 | 12px | 0.5px | 16px |
| `label-small` | 500 | 11px | 0.5px | 16px |

### 1.3 形状系统 (Shape) — 7 级圆角

| Token | 值 | 典型用途 |
|-------|-----|---------|
| `--md-sys-shape-none` | `0px` | 表格、分隔线 |
| `--md-sys-shape-extra-small` | `4px` | Chip、Badge |
| `--md-sys-shape-small` | `8px` | Card、TextField |
| `--md-sys-shape-medium` | `12px` | Dialog、Sheet |
| `--md-sys-shape-large` | `16px` | 大卡片 |
| `--md-sys-shape-extra-large` | `28px` | Modal、超大容器 |
| `--md-sys-shape-full` | `9999px` | Button (pill)、FAB |

### 1.4 海拔系统 (Elevation) — 6 级 Tonal Elevation

| Level | Box Shadow | Surface Tonal Overlay |
|-------|-----------|----------------------|
| 0 | `none` | `0%` |
| 1 | `0 1px 2px rgba(0,0,0,0.3), 0 1px 3px 1px rgba(0,0,0,0.15)` | `5%` |
| 2 | `0 1px 2px rgba(0,0,0,0.3), 0 2px 6px 2px rgba(0,0,0,0.15)` | `8%` |
| 3 | `0 4px 8px 3px rgba(0,0,0,0.15), 0 1px 3px rgba(0,0,0,0.3)` | `11%` |
| 4 | `0 6px 10px 4px rgba(0,0,0,0.15), 0 2px 3px rgba(0,0,0,0.3)` | `12%` |
| 5 | `0 8px 12px 6px rgba(0,0,0,0.15), 0 4px 4px rgba(0,0,0,0.3)` | `14%` |

### 1.5 状态层 (State Layer) — 交互遮盖

| 状态 | 透明度 | 说明 |
|------|--------|------|
| hover | `0.08` | 悬停 hover |
| focus | `0.12` | 聚焦 focus |
| pressed | `0.12` | 按下 active |
| dragged | `0.16` | 拖拽中 |

状态层在组件上叠加一层纯色（on-surface / on-primary 等对应色），透明度如上述。

### 1.6 动效系统 (Motion)

| 缓动类型 | 贝塞尔曲线 |
|----------|-----------|
| `standard` | `cubic-bezier(0.2, 0, 0, 1)` |
| `standard-decelerate` | `cubic-bezier(0, 0, 0, 1)` |
| `standard-accelerate` | `cubic-bezier(0.3, 0, 1, 1)` |
| `emphasized` | `cubic-bezier(0.2, 0, 0, 1)` |
| `emphasized-decelerate` | `cubic-bezier(0.05, 0.7, 0.1, 1)` |
| `emphasized-accelerate` | `cubic-bezier(0.3, 0, 0.8, 0.15)` |

| 时长 Token | 值 | 典型用途 |
|-----------|-----|---------|
| `short1`-`short4` | 50-200ms | 微交互（涟漪、hover） |
| `medium1`-`medium4` | 250-400ms | 展开/折叠、过渡 |
| `long1`-`long4` | 450-600ms | 页面转换 |
| `extra-long1`-`extra-long4` | 700-1000ms | 复杂编排动画 |

---

## 2. 组件生成规则

### 2.1 通用要求 (所有组件必须遵守)

1. **颜色**: 必须使用 `var(--md-sys-color-*)` 语法，禁止硬编码色值
2. **Typography**: 必须使用 `var(--md-sys-typescale-*-*)` 或等效映射
3. **Shape**: 必须使用 `var(--md-sys-shape-*)` 
4. **State Layer**: 必须有 state layer 元素（hover/focus/pressed 透明度叠加）
5. **Ripple**: 推荐实现 ripple 效果（可选但推荐）
6. **Dark Mode**: 所有组件必须适配暗色模式（通过 prefers-color-scheme 或 class）
7. **RTL**: 使用逻辑属性（inline-start/end 替代 left/right）
8. **无障碍**: 支持 aria 属性、键盘操作（Enter/Space）、focus-visible
9. **触摸目标**: 最小触摸区域 48x48dp

### 2.2 组件具体规范

#### Button (5 variants)

| Variant | 背景 | 文字色 | 轮廓 | 海拔 |
|---------|------|--------|------|------|
| **filled** | `primary` | `on-primary` | none | 0 |
| **outlined** | transparent | `primary` | `outline` (1px) | 0 |
| **text** | transparent | `primary` | none | 0 |
| **elevated** | `surface-container-low` | `primary` | none | level1 |
| **tonal** | `secondary-container` | `on-secondary-container` | none | 0 |

高度: **40dp** (M3 标准)，最小宽: 48dp，padding: 0 24dp，shape: **full** (pill)，字型: **label-large**

#### Card (3 variants)

| Variant | 背景 | 海拔 | 轮廓 |
|---------|------|------|------|
| **elevated** | `surface-container-low` | level1 | none |
| **filled** | `surface-container-highest` | 0 | none |
| **outlined** | `surface` | 0 | `outline-variant` (1px) |

Shape: **medium** (12px)

#### FAB (6 variants)

FAB 大小规范:

| Variant | 尺寸 | 形状 | 背景 |
|---------|------|------|------|
| **primary** (默认) | 56x56dp | large (16px) | `primary-container` |
| **surface** | 56x56dp | large (16px) | `surface-container-high` |
| **secondary** | 56x56dp | large (16px) | `secondary-container` |
| **tertiary** | 56x56dp | large (16px) | `tertiary-container` |
| **small** | 40x40dp | medium (12px) | `primary-container` |
| **large** | 96x96dp | large (16px) | `primary-container` |

图标大小: 24dp (normal), 36dp (large)

#### Dialog

| 属性 | 值 |
|------|-----|
| Shape | extra-large (28px) |
| 最小宽 | 280dp |
| 最大宽 | 560dp |
| Title 字型 | headline-small |
| 内容字型 | body-medium |
| 按钮字型 | label-large |

#### Navigation Bar

- 高度: **80dp**
- 无阴影 (elevation: 0)
- 背景: `surface`
- 选中态: 使用 `secondary-container` 形状指示器 + outline
- 图标: 24dp，active + inactive 两种
- 标签字型: **label-medium** (12px)

#### Chip

M3 中 Chip 分类变化: Action Chip 拆分为 **Assist** 和 **Suggestion** 两种。

| Variant | 用途 | 海拔 |
|---------|------|------|
| **assist** | 辅助操作 (原 action chip) | 0 |
| **filter** | 筛选/多选 | 0 |
| **input** | 输入型标签 | 0 |
| **suggestion** | 建议操作 (原 action chip) | 0 |

Shape: **extra-small** (4px), 高度: 32dp

#### Top App Bar

| Variant | 高度 | 特点 |
|---------|------|------|
| **center-aligned** | 64dp | 标题居中 |
| **small** | 64dp | 标题居左 |
| **medium** | 112dp | 大标题 |
| **large** | 152dp | 超大标题，折叠效果 |

- 默认无阴影，滚动后增加阴影
- 无 `primary-variant`（M2 概念已删除）

#### Switch

- 更大面积，更高高度
- 无阴影 (拟物→扁平)
- Track 内显示对勾等可识别图形
- 对色盲用户友好

---

## 3. 代码生成示例 (AI 输出格式参考)

生成组件时，请参考以下示例结构。确保每个组件输出都包含：组件代码、样式代码、Props 表、无障碍说明。

### 示例: Filled Button (React + 纯 CSS)

**用户输入**: `/md3 button filled react`

**输出**:

```tsx
// Button.tsx
import React, { forwardRef, ButtonHTMLAttributes } from 'react';
import './Button.css';

type ButtonVariant = 'filled' | 'outlined' | 'text' | 'elevated' | 'tonal';

interface MD3ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: ButtonVariant;
  icon?: React.ReactNode;
  loading?: boolean;
}

export const MD3Button = forwardRef<HTMLButtonElement, MD3ButtonProps>(
  ({ variant = 'filled', icon, loading, children, className, disabled, ...props }, ref) => {
    const stateLayerColor = variant === 'filled'
      ? 'var(--md-sys-color-on-primary)'
      : 'var(--md-sys-color-primary)';

    return (
      <button
        ref={ref}
        className={`md3-button md3-button--${variant} ${disabled || loading ? 'md3-button--disabled' : ''} ${className || ''}`}
        disabled={disabled || loading}
        aria-busy={loading}
        {...props}
      >
        <span className="md3-button__state-layer" style={{ '--state-layer-color': stateLayerColor } as React.CSSProperties} />
        <span className="md3-button__content">
          {loading ? <span className="md3-button__spinner" /> : icon ? <span className="md3-button__icon">{icon}</span> : null}
          <span className="md3-button__label">{children}</span>
        </span>
      </button>
    );
  }
);
MD3Button.displayName = 'MD3Button';
```

```css
/* Button.css */
.md3-button {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  height: 40px;
  min-width: 48px;
  padding: 0 24px;
  border: none;
  border-radius: var(--md-sys-shape-full);
  cursor: pointer;
  overflow: hidden;
  font: var(--md-sys-typescale-label-large-weight) var(--md-sys-typescale-label-large-size)/var(--md-sys-typescale-label-large-line-height) var(--md-sys-typescale-label-large-font);
  letter-spacing: var(--md-sys-typescale-label-large-tracking);
  transition: box-shadow var(--md-sys-motion-duration-medium1) var(--md-sys-motion-easing-standard);
}

/* State Layer */
.md3-button__state-layer {
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: var(--state-layer-color, var(--md-sys-color-primary));
  opacity: 0;
  transition: opacity var(--md-sys-motion-duration-short2) var(--md-sys-motion-easing-standard);
  pointer-events: none;
}
.md3-button:hover .md3-button__state-layer        { opacity: var(--md-sys-state-layer-hover-opacity, 0.08); }
.md3-button:focus-visible .md3-button__state-layer { opacity: var(--md-sys-state-layer-focus-opacity, 0.12); }
.md3-button:active .md3-button__state-layer        { opacity: var(--md-sys-state-layer-pressed-opacity, 0.12); }

/* Filled variant */
.md3-button--filled {
  background: var(--md-sys-color-primary);
  color: var(--md-sys-color-on-primary);
}

/* Outlined variant */
.md3-button--outlined {
  background: transparent;
  color: var(--md-sys-color-primary);
  border: 1px solid var(--md-sys-color-outline);
}

/* ... 其他 variant 以此类推 */

.md3-button--disabled {
  opacity: 0.38;
  pointer-events: none;
}
```

| Props | 类型 | 默认值 | 说明 |
|-------|------|--------|------|
| `variant` | `filled \| outlined \| text \| elevated \| tonal` | `filled` | 按钮变体 |
| `icon` | `ReactNode` | — | 前置图标 |
| `loading` | `boolean` | `false` | 加载态 |
| `disabled` | `boolean` | `false` | 禁用态 |

**无障碍**: `aria-busy` 在加载时设置，`disabled` 属性原生支持键盘跳过。

### 示例: Filled Button (纯 HTML/CSS)

```html
<button class="md3-button md3-button--filled">
  <span class="md3-button__state-layer"></span>
  <span class="md3-button__content">
    <span class="md3-button__label">Button</span>
  </span>
</button>
```

---

## 4. 框架适配指南

生成代码前，务必先读取对应框架的详细规范。以下是各框架的代码结构策略和目录约定。

### React + MUI v5+

**目录约定**: `src/components/{ComponentName}.tsx`
**策略**: 通过 MUI 的 `createTheme` 注入 MD3 tokens，直接使用 `<Button variant="filled">` 等 MUI 组件。
**MUI theme 配置模板**:

```tsx
// theme.ts
import { createTheme } from '@mui/material/styles';
const md3Theme = createTheme({
  palette: {
    primary: { main: '#6750A4', contrastText: '#FFFFFF' },
    secondary: { main: '#625B71' },
    // ... 完整 M3 palette
  },
  typography: {
    fontFamily: 'Roboto, sans-serif',
  },
  shape: { borderRadius: 20 }, // M3 pill buttons
});
```

### React + 纯 CSS

**目录约定**: `src/components/{ComponentName}.tsx` + `{ComponentName}.css`
**策略**: 纯 React 组件 + CSS 样式文件。所有样式使用 `var(--md-sys-*)` 变量，先引入 `md3-theme-base.css`。

### Vue 3 + Vuetify 3

**目录约定**: `src/components/{ComponentName}.vue`
**策略**: Vuetify 3 原生支持 M3，使用 Vuetify 组件 + theme 配置即可。

### Vue 3 + 纯 CSS

**目录约定**: `src/components/{ComponentName}.vue`（`<style scoped>` 在单文件内）
**策略**: 使用 `<style scoped>`，手动定义 CSS 自定义属性。组件逻辑用 Composition API。

### Angular Material

**目录约定**: `src/app/components/{component-name}/{component-name}.component.ts`
**策略**: Angular Material v15+ 支持 M3 theming API (`@use '@angular/material' with ($theme...)`)。

### Flutter

**目录约定**: `lib/widgets/{widget_name}.dart`
**策略**: `MaterialApp(theme: ThemeData(useMaterial3: true, colorSchemeSeed: Color(0xFF6750A4)))`，使用 M3 原生 Widget。

### 纯 HTML/CSS

**输出结构**:
```
index.html       # 主页面，引入 md3-theme-base.css
component.css    # 组件样式
```
**策略**: 纯粹的 HTML 标签 + CSS Custom Properties。无任何构建工具依赖，直接在浏览器打开 `index.html`。

### Lit / Web Components

**目录约定**: `src/components/{component-name}.ts`
**策略**: Lit 的 `static styles = css\`...\`` 中使用 MD3 CSS 变量，Shadow DOM 自动隔离样式。支持 Custom Elements 注册。

### 通用原则

1. 先引入 `assets/md3-theme-base.css` 确保所有 MD3 CSS 变量已定义
2. 所有颜色用 `var(--md-sys-color-*)`，禁止硬编码
3. 所有组件必须适配暗色模式（通过 `prefers-color-scheme` 已内置在 theme-base.css）

---

## 5. 响应式布局: Compact / Medium / Expanded

```
Compact (0-599dp)           Medium (600-839dp)          Expanded (840dp+)
┌──────────────┐        ┌─────────────────────┐     ┌───────────────────────────┐
│ 单一列       │        │ 双列/侧边导航        │     │ Navigation Rail/Drawer    │
│ 底部导航栏    │        │ Navigation Rail      │     │ 多列内容                  │
│ 全屏对话框    │        │ 标准对话框           │     │ 侧边详情面板              │
└──────────────┘        └─────────────────────┘     └───────────────────────────┘
```

**断点值** (CSS):
```css
/* Compact: 0-599dp */
/* Medium: 600-839dp */
/* Expanded: 840dp+ */
@media (min-width: 600px) { /* Medium + Expanded */ }
@media (min-width: 840px) { /* Expanded */ }
```

生成模板时需根据目标断点输出响应式布局。

---

## 6. 组合命令：自然语言页面生成

当用户使用 `/md3 page "描述"` 时：

1. **解析意图**: 从自然语言中提取需要的组件和布局
2. **规划组件**: 列出所需组件清单（如: AppBar + FAB + Card List + NavBar）
3. **确定布局**: Compact/Medium/Expanded 策略
4. **生成代码**: 一次性生成所有组件 + 页面容器
5. **自检**: 验证 MD3 合规性

---

## 7. 主题导出

使用 `scripts/generate_tokens.py` 脚本可自动化生成不同格式的主题文件。脚本位于 skill 的 `scripts/` 目录，可使用 Bash 工具直接执行。

### 从种子色生成:

```bash
# 绝对路径（推荐）
python {skill_dir}/scripts/generate_tokens.py --seed '#6750A4' --format css --output theme.css
python {skill_dir}/scripts/generate_tokens.py --seed '#6750A4' --format tailwind --output tailwind-m3.js
```

### 暗色/亮色主题切换:

```css
/* 亮色主题 (默认) */
:root { /* light tokens */ }

/* 暗色主题 */
@media (prefers-color-scheme: dark) {
  :root { /* dark tokens */ }
}

/* 或使用 class 切换 */
[data-theme="dark"] { /* dark tokens */ }
```

---

## 8. 输出规范

### 每个组件输出必须包含：
1. **组件代码** (tsx/vue/html) — 完整可运行
2. **样式代码** (css/scss) — 使用 MD3 tokens
3. **使用示例** — 至少 2 个 variant 示例
4. **Props/属性表** — 所有可配置项
5. **无障碍说明** — aria 属性、键盘交互

### 每个模板输出必须包含：
1. **完整页面代码** — 可直接预览
2. **使用的组件清单**
3. **响应式策略说明** (Compact/Medium/Expanded)
4. **暗色模式截图说明**

---

## 9. MD3 合规性自检清单

生成代码后自检以下项:

- [ ] 所有颜色都使用 `var(--md-sys-color-*)` (非硬编码)
- [ ] Typography 使用了正确的 type scale
- [ ] Shape 使用了正确的圆角级别
- [ ] 有 state layer 实现
- [ ] 暗色模式有适配
- [ ] 触摸目标 ≥ 48x48dp
- [ ] 支持键盘操作 (Enter/Space)
- [ ] 有 aria 属性
- [ ] 使用了逻辑属性 (RTL 友好)
- [ ] Elevation 使用 Tonal Elevation (非纯阴影)

---

## 资源文件

- `references/md3-tokens.md` — 完整 MD3 Design Token 参考（颜色/字体/形状/海拔/动效/状态层）
- `references/md3-components.md` — 40+ 组件完整规格（尺寸/颜色映射/字型映射/变体参数）
- `references/md3-templates.md` — 15 个页面模板布局规范（组件组合/响应式策略）
- `scripts/generate_tokens.py` — 从种子色自动生成所有格式主题文件（CSS/SCSS/JSON/Tailwind/Flutter）
- `assets/md3-theme-base.css` — 完整 MD3 CSS 自定义属性（亮色+暗色），直接引入即可启用
- `assets/quick-start.html` — MD3 项目快速启动 HTML 模板
