# MD3 页面模板规范

> 15+ 常用页面模板的组件组合方案与布局规范。

---

## 模板总览

```
/login          →  登录/注册页
/dashboard      →  仪表盘
/settings       →  设置页
/list           →  列表页
/detail         →  详情页
/onboarding     →  引导页
/profile        →  个人主页
/checkout       →  结账/支付页
/chat           →  聊天界面
/feed           →  动态/信息流
/gallery        →  图片画廊
/calendar       →  日历视图
/form           →  表单页
/empty          →  空状态页
/error          →  错误/404页
```

---

## 1. Login — 登录/注册页

### 组件清单

```
Top section:
  - App icon / Logo (centered, 64-96dp)
  - Headline text (headline-medium)

Middle section:
  - TextField (filled) × 2-3: email, password, (confirm)
  - Text button: "忘记密码?"
  - Error message area (body-small, error color)

Bottom section:
  - Filled button (full width): "登录" / "注册"
  - Outlined button / Text button: "创建账号" / "已有账号"
  - Or divider: "或" (optional)
  - Social login icons (optional)
```

### 布局

```
Compact (<600dp):
  ┌──────────────────┐
  │     Logo          │
  │   Welcome Text    │
  │  ┌──────────────┐ │
  │  │  Email       │ │
  │  │  Password    │ │
  │  │  [Login Btn] │ │
  │  └──────────────┘ │
  └──────────────────┘

Expanded (840dp+):
  ┌──────────────────────────────────┐
  │  ┌──────────┐  ┌──────────────┐ │
  │  │  Hero    │  │  Form        │ │
  │  │  Image   │  │  Email       │ │
  │  │  /Brand  │  │  Password    │ │
  │  │          │  │  [Login Btn] │ │
  │  └──────────┘  └──────────────┘ │
  └──────────────────────────────────┘
```

---

## 2. Dashboard — 仪表盘

### 组件清单

```
Top: TopAppBar (center-aligned), title: "Dashboard"
  - Trailing icon: notification badge

Content:
  - Summary cards (Card elevated, 2-4 items)
    - Each: icon + value (display-small) + label (body-medium)
  - Chart area (Card filled, optional)
  - Recent activity list (ListItem)
  - Quick actions row (IconButton or Chip assist)

Bottom: NavigationBar (3-5 items)
```

### 响应式

```
Compact: single column cards
Medium: 2-column grid, NavRail replaces NavBar
Expanded: 3-4 column grid, NavRail always visible
```

---

## 3. Settings — 设置页

### 组件清单

```
Top: TopAppBar (small), leading: back arrow

Content:
  - Section headers (title-small, on-surface-variant)
  - ListItem groups with dividers
  - Switch / Checkbox for toggles
  - Radio group for selections
  - Slider for continuous values
  - Outlined button: "退出登录" (error color)
```

### 结构

```yaml
sections:
  - header: "账号"
    items:
      - title: "个人信息"       type: navigation
      - title: "修改密码"       type: navigation
      - title: "通知设置"       type: navigation
  - header: "外观"
    items:
      - title: "暗色模式"       type: switch
      - title: "主题色"         type: radio
      - title: "字体大小"       type: slider
  - header: "隐私"
    items:
      - title: "隐私政策"       type: navigation
      - title: "清除缓存"       type: button
      - title: "退出登录"       type: button (destructive)
```

---

## 4. List — 列表页

### 组件清单

```
Top: TopAppBar (small), trailing: search icon

Search area (collapsible):
  - SearchBar (optional, --with-search)
  
Content:
  - ListItem × N (3-line or 2-line)
    - Leading: avatar / icon / image
    - Title + subtitle + metadata
    - Trailing: icon / chip / text
  - Divider between items
  - FAB (primary, --with-fab): add new item
  - Pull to refresh

Empty state (if no items): see /md3 template empty
```

---

## 5. Detail — 详情页

### 组件清单

```
Top: TopAppBar (small/medium, --with-appbar)
  - Leading: back arrow
  - Title: item name
  - Trailing: more menu / favorite

Hero section:
  - Image (16:9, rounded top)
  - Title: headline-small
  - Subtitle + metadata row

Content section:
  - Description text (body-medium)
  - Attribute list (key-value pairs)
  - Related items (horizontal scroll cards)

Bottom:
  - BottomSheet or fixed action bar (--with-bottomsheet)
  - Filled button: primary action
```

---

## 6. Onboarding — 引导页

### 组件清单 (`--steps=N`)

```
Content area:
  - Pager / HorizontalPager for N steps
  - Each page:
    - Illustration (200-300dp)
    - Headline: headline-medium
    - Body: body-medium (supporting text)

Bottom:
  - Page indicators (dots)
  - Navigation buttons:
    - "跳过" (text button, top-right)
    - "下一步" (filled button) / "开始使用" (last page)
```

---

## 7. Profile — 个人主页

### 组件清单

```
Top: TopAppBar (center), trailing: settings/edit

Header:
  - Avatar (large, 80-100dp, circular)
  - Name: headline-small
  - Bio / stats: body-medium

Content:
  - TabBar: 帖子/收藏/标签
  - Tab content: grid gallery / list
  - Edit profile FAB or button
```

---

## 8. Checkout — 结账/支付页

### 组件清单

```
Top: TopAppBar (small), title: "确认订单"

Content:
  - Shipping address card (Card outlined)
  - Order items list (ListItem, compact, with image)
  - Price summary:
    - 小计 / 运费 / 优惠 / 合计
    - Total: title-large, bold

Bottom (fixed):
  - Payment method selector
  - Filled button: "支付 ¥XX.XX" (full width)
```

---

## 9. Chat — 聊天界面

### 组件清单

```
Top: TopAppBar (center), 
  - Leading: back
  - Title: contact name + online status (body-small)
  - Trailing: call / video / menu

Content:
  - Message list (scrollable)
  - Message bubbles:
    - Sent: primary-container bg, right aligned, large end radius
    - Received: surface-container-highest bg, left aligned
    - Timestamp: label-small
  - Date separators: Chip in center

Bottom (fixed):
  - TextField (filled) with attach/send icons
  - Emoji / attachment options
```

---

## 10. Feed — 动态/信息流

### 组件清单

```
Top: TopAppBar (center), title: app name

Content:
  - Card (outlined/elevated) × N
  - Each card:
    - Header: avatar + name + time
    - Content: text (body-medium) + image (16:9 optional)
    - Actions: like (IconButton) + comment + share
  - Infinite scroll / load more

Staggered FAB: create new post (optional)
```

---

## 11. Gallery — 图片画廊

### 组件清单

```
Top: TopAppBar (small), trailing: filter/grid toggle

Content:
  - SegmentedButton: All / Albums / Favorites
  - Grid layout (2-4 cols by screen size)
  - Each item: image, aspect ratio 1:1, rounded corners
  - Tap → detail view / lightbox
```

---

## 12. Calendar — 日历视图

### 组件清单

```
Top: TopAppBar (small), title: month/year picker

Content:
  - Week header row (label-small, 7 columns)
  - Day grid (7 × 5-6 rows)
  - Day cell: 40x40dp, full circle when selected
  - Today: primary outline
  - Events dots below day number

Bottom:
  - Event list for selected day
  - FAB: add event
```

---

## 13. Form — 表单页

### 组件清单

```
Top: TopAppBar (small), title: form title

Content:
  - TextField × N (filled/outlined)
  - Error states with supporting text
  - Dropdown / Select fields
  - Date picker trigger
  - Switch / Checkbox groups
  - Photo upload area

Bottom:
  - Filled button: "提交" (full width)
  - Cancel text button
```

---

## 14. Empty — 空状态页

### 组件清单

```
Center:
  - Illustration (200dp)
  - Title: headline-small
  - Description: body-medium (on-surface-variant, centered)
  - Action: filled button (primary action)
```

---

## 15. Error — 错误页/404

### 组件清单

```
Center:
  - Large illustration (200dp)
  - Error code: display-large (primary, 404)
  - Title: headline-small, "页面未找到"
  - Description: body-medium
  - Actions:
    - Filled button: "返回首页"
    - Text button: "重试" / "联系支持"
```

---

## 通用布局容器

所有模板使用相同的根布局结构：

```html
<div class="md3-page" data-theme="light">
  <!-- Top App Bar -->
  <header class="md3-top-app-bar">...</header>
  
  <!-- Main Content (scrollable) -->
  <main class="md3-content">
    <!-- template-specific content -->
  </main>
  
  <!-- Bottom Navigation (if needed) -->
  <nav class="md3-navbar">...</nav>
  
  <!-- FAB (if needed, positioned fixed) -->
  <button class="md3-fab">+</button>
</div>
```

CSS 基础布局：

```css
.md3-page {
  display: flex;
  flex-direction: column;
  min-height: 100dvh;
  background: var(--md-sys-color-background);
  color: var(--md-sys-color-on-background);
}

.md3-content {
  flex: 1;
  overflow-y: auto;
  padding: 16px;
}
```
