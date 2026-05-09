# MD3 椤甸潰妯℃澘瑙勮寖

> 15+ 甯哥敤椤甸潰妯℃澘鐨勭粍浠剁粍鍚堟柟妗堜笌甯冨眬瑙勮寖銆?
---

## 妯℃澘鎬昏

```
/login          鈫? 鐧诲綍/娉ㄥ唽椤?/dashboard      鈫? 浠〃鐩?/settings       鈫? 璁剧疆椤?/list           鈫? 鍒楄〃椤?/detail         鈫? 璇︽儏椤?/onboarding     鈫? 寮曞椤?/profile        鈫? 涓汉涓婚〉
/checkout       鈫? 缁撹处/鏀粯椤?/chat           鈫? 鑱婂ぉ鐣岄潰
/feed           鈫? 鍔ㄦ€?淇℃伅娴?/gallery        鈫? 鍥剧墖鐢诲粖
/calendar       鈫? 鏃ュ巻瑙嗗浘
/form           鈫? 琛ㄥ崟椤?/empty          鈫? 绌虹姸鎬侀〉
/error          鈫? 閿欒/404椤?```

---

## 1. Login 鈥?鐧诲綍/娉ㄥ唽椤?
### 缁勪欢娓呭崟

```
Top section:
  - App icon / Logo (centered, 64-96dp)
  - Headline text (headline-medium)

Middle section:
  - TextField (filled) 脳 2-3: email, password, (confirm)
  - Text button: "蹇樿瀵嗙爜?"
  - Error message area (body-small, error color)

Bottom section:
  - Filled button (full width): "鐧诲綍" / "娉ㄥ唽"
  - Outlined button / Text button: "鍒涘缓璐﹀彿" / "宸叉湁璐﹀彿"
  - Or divider: "鎴? (optional)
  - Social login icons (optional)
```

### 甯冨眬

```
Compact (<600dp):
  鈹屸攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹?  鈹?    Logo          鈹?  鈹?  Welcome Text    鈹?  鈹? 鈹屸攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹?鈹?  鈹? 鈹? Email       鈹?鈹?  鈹? 鈹? Password    鈹?鈹?  鈹? 鈹? [Login Btn] 鈹?鈹?  鈹? 鈹斺攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹?鈹?  鈹斺攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹?
Expanded (840dp+):
  鈹屸攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹?  鈹? 鈹屸攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹? 鈹屸攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹?鈹?  鈹? 鈹? Hero    鈹? 鈹? Form        鈹?鈹?  鈹? 鈹? Image   鈹? 鈹? Email       鈹?鈹?  鈹? 鈹? /Brand  鈹? 鈹? Password    鈹?鈹?  鈹? 鈹?         鈹? 鈹? [Login Btn] 鈹?鈹?  鈹? 鈹斺攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹? 鈹斺攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹?鈹?  鈹斺攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹?```

---

## 2. Dashboard 鈥?浠〃鐩?
### 缁勪欢娓呭崟

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

### 鍝嶅簲寮?
```
Compact: single column cards
Medium: 2-column grid, NavRail replaces NavBar
Expanded: 3-4 column grid, NavRail always visible
```

---

## 3. Settings 鈥?璁剧疆椤?
### 缁勪欢娓呭崟

```
Top: TopAppBar (small), leading: back arrow

Content:
  - Section headers (title-small, on-surface-variant)
  - ListItem groups with dividers
  - Switch / Checkbox for toggles
  - Radio group for selections
  - Slider for continuous values
  - Outlined button: "閫€鍑虹櫥褰? (error color)
```

### 缁撴瀯

```yaml
sections:
  - header: "璐﹀彿"
    items:
      - title: "涓汉淇℃伅"       type: navigation
      - title: "淇敼瀵嗙爜"       type: navigation
      - title: "閫氱煡璁剧疆"       type: navigation
  - header: "澶栬"
    items:
      - title: "鏆楄壊妯″紡"       type: switch
      - title: "涓婚鑹?         type: radio
      - title: "瀛椾綋澶у皬"       type: slider
  - header: "闅愮"
    items:
      - title: "闅愮鏀跨瓥"       type: navigation
      - title: "娓呴櫎缂撳瓨"       type: button
      - title: "閫€鍑虹櫥褰?       type: button (destructive)
```

---

## 4. List 鈥?鍒楄〃椤?
### 缁勪欢娓呭崟

```
Top: TopAppBar (small), trailing: search icon

Search area (collapsible):
  - SearchBar (optional, --with-search)
  
Content:
  - ListItem 脳 N (3-line or 2-line)
    - Leading: avatar / icon / image
    - Title + subtitle + metadata
    - Trailing: icon / chip / text
  - Divider between items
  - FAB (primary, --with-fab): add new item
  - Pull to refresh

Empty state (if no items): see /md3 template empty
```

---

## 5. Detail 鈥?璇︽儏椤?
### 缁勪欢娓呭崟

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

## 6. Onboarding 鈥?寮曞椤?
### 缁勪欢娓呭崟 (`--steps=N`)

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
    - "璺宠繃" (text button, top-right)
    - "涓嬩竴姝? (filled button) / "寮€濮嬩娇鐢? (last page)
```

---

## 7. Profile 鈥?涓汉涓婚〉

### 缁勪欢娓呭崟

```
Top: TopAppBar (center), trailing: settings/edit

Header:
  - Avatar (large, 80-100dp, circular)
  - Name: headline-small
  - Bio / stats: body-medium

Content:
  - TabBar: 甯栧瓙/鏀惰棌/鏍囩
  - Tab content: grid gallery / list
  - Edit profile FAB or button
```

---

## 8. Checkout 鈥?缁撹处/鏀粯椤?
### 缁勪欢娓呭崟

```
Top: TopAppBar (small), title: "纭璁㈠崟"

Content:
  - Shipping address card (Card outlined)
  - Order items list (ListItem, compact, with image)
  - Price summary:
    - 灏忚 / 杩愯垂 / 浼樻儬 / 鍚堣
    - Total: title-large, bold

Bottom (fixed):
  - Payment method selector
  - Filled button: "鏀粯 楼XX.XX" (full width)
```

---

## 9. Chat 鈥?鑱婂ぉ鐣岄潰

### 缁勪欢娓呭崟

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

## 10. Feed 鈥?鍔ㄦ€?淇℃伅娴?
### 缁勪欢娓呭崟

```
Top: TopAppBar (center), title: app name

Content:
  - Card (outlined/elevated) 脳 N
  - Each card:
    - Header: avatar + name + time
    - Content: text (body-medium) + image (16:9 optional)
    - Actions: like (IconButton) + comment + share
  - Infinite scroll / load more

Staggered FAB: create new post (optional)
```

---

## 11. Gallery 鈥?鍥剧墖鐢诲粖

### 缁勪欢娓呭崟

```
Top: TopAppBar (small), trailing: filter/grid toggle

Content:
  - SegmentedButton: All / Albums / Favorites
  - Grid layout (2-4 cols by screen size)
  - Each item: image, aspect ratio 1:1, rounded corners
  - Tap 鈫?detail view / lightbox
```

---

## 12. Calendar 鈥?鏃ュ巻瑙嗗浘

### 缁勪欢娓呭崟

```
Top: TopAppBar (small), title: month/year picker

Content:
  - Week header row (label-small, 7 columns)
  - Day grid (7 脳 5-6 rows)
  - Day cell: 40x40dp, full circle when selected
  - Today: primary outline
  - Events dots below day number

Bottom:
  - Event list for selected day
  - FAB: add event
```

---

## 13. Form 鈥?琛ㄥ崟椤?
### 缁勪欢娓呭崟

```
Top: TopAppBar (small), title: form title

Content:
  - TextField 脳 N (filled/outlined)
  - Error states with supporting text
  - Dropdown / Select fields
  - Date picker trigger
  - Switch / Checkbox groups
  - Photo upload area

Bottom:
  - Filled button: "鎻愪氦" (full width)
  - Cancel text button
```

---

## 14. Empty 鈥?绌虹姸鎬侀〉

### 缁勪欢娓呭崟

```
Center:
  - Illustration (200dp)
  - Title: headline-small
  - Description: body-medium (on-surface-variant, centered)
  - Action: filled button (primary action)
```

---

## 15. Error 鈥?閿欒椤?404

### 缁勪欢娓呭崟

```
Center:
  - Large illustration (200dp)
  - Error code: display-large (primary, 404)
  - Title: headline-small, "椤甸潰鏈壘鍒?
  - Description: body-medium
  - Actions:
    - Filled button: "杩斿洖棣栭〉"
    - Text button: "閲嶈瘯" / "鑱旂郴鏀寔"
```

---

## 閫氱敤甯冨眬瀹瑰櫒

鎵€鏈夋ā鏉夸娇鐢ㄧ浉鍚岀殑鏍瑰竷灞€缁撴瀯锛?
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

CSS 鍩虹甯冨眬锛?
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
