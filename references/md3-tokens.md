# MD3 Design Token 瀹屾暣鍙傝€冩墜鍐?
> 渚濇嵁 Material Design 3 瑙勮寖锛屽畬鏁寸殑璁捐浠ょ墝 (Design Token) 浣撶郴銆傛湰鏂囦欢渚?skill 杩愯鏃朵綔涓哄弬鑰冩暟鎹姞杞姐€?
---

## 1. 鑹插僵绯荤粺 (HCT 鑹插僵绌洪棿)

M3 浣跨敤 **HCT** (Hue-Chroma-Tone) 鑹插僵绌洪棿鏇夸唬浼犵粺 HSL/RGB銆傝壊褰╂柟妗?(ColorScheme) 鍖呭惈 25 涓鑹叉Ы銆?
### 1.1 瀹屾暣浜壊涓婚 (Light Theme) Token 琛?
| CSS 鍙橀噺 | 鑹插€?| 鐢ㄩ€?|
|----------|------|------|
| `--md-sys-color-primary` | `#6750A4` | 涓昏壊锛屾渶閲嶈鐨勭粍浠?|
| `--md-sys-color-on-primary` | `#FFFFFF` | 涓昏壊涓婄殑鍐呭鑹?|
| `--md-sys-color-primary-container` | `#EADDFF` | 涓昏壊瀹瑰櫒锛堝 FAB 鑳屾櫙锛?|
| `--md-sys-color-on-primary-container` | `#21005D` | 涓昏壊瀹瑰櫒涓婄殑鍐呭 |
| `--md-sys-color-secondary` | `#625B71` | 娆¤鑹?|
| `--md-sys-color-on-secondary` | `#FFFFFF` | 娆¤鑹蹭笂鐨勫唴瀹?|
| `--md-sys-color-secondary-container` | `#E8DEF8` | 娆¤鑹插鍣紙濡?tonal button 鑳屾櫙锛?|
| `--md-sys-color-on-secondary-container` | `#1D192B` | 娆¤鑹插鍣ㄤ笂鐨勫唴瀹?|
| `--md-sys-color-tertiary` | `#7D5260` | 绗笁鑹?|
| `--md-sys-color-on-tertiary` | `#FFFFFF` | 绗笁鑹蹭笂鐨勫唴瀹?|
| `--md-sys-color-tertiary-container` | `#FFD8E4` | 绗笁鑹插鍣?|
| `--md-sys-color-on-tertiary-container` | `#31111D` | 绗笁鑹插鍣ㄤ笂鐨勫唴瀹?|
| `--md-sys-color-error` | `#B3261E` | 閿欒鑹?|
| `--md-sys-color-on-error` | `#FFFFFF` | 閿欒鑹蹭笂鐨勫唴瀹?|
| `--md-sys-color-error-container` | `#F9DEDC` | 閿欒鑹插鍣?|
| `--md-sys-color-on-error-container` | `#410E0B` | 閿欒鑹插鍣ㄤ笂鐨勫唴瀹?|
| `--md-sys-color-background` | `#FFFBFE` | 椤甸潰鑳屾櫙 |
| `--md-sys-color-on-background` | `#1C1B1F` | 椤甸潰鑳屾櫙涓婄殑鍐呭 |
| `--md-sys-color-surface` | `#FFFBFE` | 琛ㄩ潰鑹诧紙濡?Card锛?|
| `--md-sys-color-on-surface` | `#1C1B1F` | 琛ㄩ潰涓婄殑鍐呭 |
| `--md-sys-color-surface-variant` | `#E7E0EC` | 琛ㄩ潰鍙樹綋 |
| `--md-sys-color-on-surface-variant` | `#49454F` | 琛ㄩ潰鍙樹綋涓婄殑鍐呭 |
| `--md-sys-color-outline` | `#79747E` | 杞粨绾匡紙濡?outlined button锛?|
| `--md-sys-color-outline-variant` | `#CAC4D0` | 杞粨鍙樹綋 |
| `--md-sys-color-surface-dim` | `#DED8E1` | 鏆楁贰琛ㄩ潰 |
| `--md-sys-color-surface-bright` | `#FFFBFE` | 鏄庝寒琛ㄩ潰 |
| `--md-sys-color-surface-container-lowest` | `#FFFFFF` | 鏈€浣庡鍣ㄨ〃闈?|
| `--md-sys-color-surface-container-low` | `#F7F2FA` | 浣庡鍣ㄨ〃闈?|
| `--md-sys-color-surface-container` | `#F3EDF7` | 鏍囧噯瀹瑰櫒琛ㄩ潰 |
| `--md-sys-color-surface-container-high` | `#ECE6F0` | 楂樺鍣ㄨ〃闈?|
| `--md-sys-color-surface-container-highest` | `#E6E0E9` | 鏈€楂樺鍣ㄨ〃闈?|
| `--md-sys-color-inverse-surface` | `#313033` | 鍙嶈浆琛ㄩ潰 |
| `--md-sys-color-inverse-on-surface` | `#F4EFF4` | 鍙嶈浆琛ㄩ潰涓婄殑鍐呭 |
| `--md-sys-color-inverse-primary` | `#D0BCFF` | 鍙嶈浆涓昏壊 |
| `--md-sys-color-shadow` | `#000000` | 闃村奖鑹?|
| `--md-sys-color-scrim` | `#000000` | 閬僵鑹诧紙濡?Dialog backdrop锛?|

### 1.2 鏆楄壊涓婚 (Dark Theme) Token 琛?
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

### 1.3 棰滆壊浣跨敤瑙勫垯

```
缁勪欢绫诲瀷         鈫?浣跨敤棰滆壊妲?Filled Button     鈫?primary + onPrimary
Tonal Button      鈫?secondaryContainer + onSecondaryContainer
Outlined Button   鈫?transparent + primary + outline
FAB Primary       鈫?primaryContainer + onPrimaryContainer
FAB Surface       鈫?surfaceContainerHigh + primary
Card Elevated     鈫?surfaceContainerLow + onSurface
TopAppBar         鈫?surface + onSurface (娌夋蹈寮忕敤 surface 鑹?
NavBar Active     鈫?secondaryContainer (鎸囩ず鍣?
Scrim/DialogBg    鈫?scrim / surface
```

---

## 2. 瀛椾綋绯荤粺 (Typography) 瀹屾暣鍙傝€?
榛樿瀛椾綋: **Roboto** (Android) / **Google Sans** (鍙€夋爣棰?

| Token | Weight | Size | Letter Spacing | Line Height | CSS 鍙橀噺鍓嶇紑 |
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

### 缁勪欢瀛楀瀷鏄犲皠

| 缁勪欢 | 浣跨敤瀛楀瀷 |
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

## 3. 褰㈢姸绯荤粺 (Shape) 瀹屾暣鍙傝€?
| Token | CSS 鍊?| 鍏稿瀷鐢ㄩ€?|
|-------|--------|---------|
| `--md-sys-shape-none` | `0px` | Divider, Table |
| `--md-sys-shape-extra-small` | `4px` | Chip, Badge, Small tooltip |
| `--md-sys-shape-small` | `8px` | Card, TextField, Menu |
| `--md-sys-shape-medium` | `12px` | Dialog (榛樿), BottomSheet |
| `--md-sys-shape-large` | `16px` | FAB, Large Card |
| `--md-sys-shape-extra-large` | `28px` | Fullscreen Dialog, Modal |
| `--md-sys-shape-full` | `9999px` | Button (pill), Chip (閮ㄥ垎), Badge (dot) |

### 缁勪欢 鈫?褰㈢姸鏄犲皠

| 缁勪欢 | 褰㈢姸 |
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

## 4. 娴锋嫈绯荤粺 (Elevation / Tonal Elevation)

M3 閲囩敤 **Tonal Elevation**: 娴锋嫈鍗囬珮涓嶄粎澧炲姞闃村奖锛岃繕浼氬湪 surface 涓婂彔鍔犱竴涓鑹茶鐩栧眰銆?
| Level | Box Shadow | Surface Tonal Overlay | 鍏稿瀷鐢ㄩ€?|
|-------|-----------|----------------------|---------|
| 0 | `none` | `0%` | Button, Chip, NavBar, Switch |
| 1 | `0 1px 2px rgba(0,0,0,0.3), 0 1px 3px 1px rgba(0,0,0,0.15)` | `5%` | Card (elevated), SearchBar (scroll) |
| 2 | `0 1px 2px rgba(0,0,0,0.3), 0 2px 6px 2px rgba(0,0,0,0.15)` | `8%` | FAB (resting), Menu |
| 3 | `0 4px 8px 3px rgba(0,0,0,0.15), 0 1px 3px rgba(0,0,0,0.3)` | `11%` | FAB (pressed), Dialog |
| 4 | `0 6px 10px 4px rgba(0,0,0,0.15), 0 2px 3px rgba(0,0,0,0.3)` | `12%` | BottomSheet |
| 5 | `0 8px 12px 6px rgba(0,0,0,0.15), 0 4px 4px rgba(0,0,0,0.3)` | `14%` | NavDrawer (modal) |

**M2鈫扢3 鍏抽敭鍙樺寲**: M3 鏁翠綋闄嶄綆浜嗘捣鎷斾娇鐢ㄣ€侰hip銆丯avBar銆乀opAppBar 榛樿鏃犻槾褰便€?
---

## 5. 鐘舵€佸眰 (State Layer)

鐘舵€佸眰鍦ㄧ粍浠朵笂鏂瑰彔鍔犱竴涓函鑹诧紝閫氳繃閫忔槑搴︽帶鍒跺己搴︺€?
| 鐘舵€?| 閫忔槑搴?| 閫傜敤鑹?|
|------|--------|--------|
| hover | `0.08` | `on-surface` (涓€鑸? / `on-primary` (filled button) 绛?|
| focus | `0.12` | 鍚屼笂 |
| pressed | `0.12` | 鍚屼笂 |
| dragged | `0.16` | 鍚屼笂 |

瀹炵幇绀轰緥:

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

## 6. 鍔ㄦ晥绯荤粺 (Motion) 瀹屾暣鍙傝€?
### 6.1 缂撳姩鍑芥暟 (Easing)

| Token | 璐濆灏旀洸绾?| 鐢ㄩ€?|
|-------|-----------|------|
| `--md-sys-motion-easing-standard` | `cubic-bezier(0.2, 0, 0, 1)` | 鏍囧噯杩囨浮 |
| `--md-sys-motion-easing-standard-decelerate` | `cubic-bezier(0, 0, 0, 1)` | 鍏冪礌鍑虹幇/灞曞紑 |
| `--md-sys-motion-easing-standard-accelerate` | `cubic-bezier(0.3, 0, 1, 1)` | 鍏冪礌娑堝け/鎶樺彔 |
| `--md-sys-motion-easing-emphasized` | `cubic-bezier(0.2, 0, 0, 1)` | 寮鸿皟鍔ㄧ敾 |
| `--md-sys-motion-easing-emphasized-decelerate` | `cubic-bezier(0.05, 0.7, 0.1, 1)` | 寮鸿皟杩涘叆 |
| `--md-sys-motion-easing-emphasized-accelerate` | `cubic-bezier(0.3, 0, 0.8, 0.15)` | 寮鸿皟閫€鍑?|

### 6.2 鏃堕暱 (Duration)

```
short1: 50ms     short2: 100ms    short3: 150ms    short4: 200ms
medium1: 250ms   medium2: 300ms   medium3: 350ms   medium4: 400ms
long1: 450ms     long2: 500ms     long3: 550ms     long4: 600ms
extraLong1: 700ms  extraLong2: 800ms  extraLong3: 900ms  extraLong4: 1000ms
```

### 6.3 缁勪欢鍔ㄧ敾閫熸煡

| 浜や簰 | 鏃堕暱 | 缂撳姩 |
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

## 7. 鏂偣 (Breakpoints) 鈥?鍝嶅簲寮?
| 绫诲瀷 | 鑼冨洿 | CSS 濯掍綋鏌ヨ |
|------|------|-------------|
| Compact | 0鈥?99dp | `@media (max-width: 599px)` |
| Medium | 600鈥?39dp | `@media (min-width: 600px) and (max-width: 839px)` |
| Expanded | 840dp+ | `@media (min-width: 840px)` |

### 鍝嶅簲寮忕瓥鐣?
| 缁勪欢 | Compact | Medium | Expanded |
|------|---------|--------|----------|
| Navigation | NavBar (bottom) | NavRail (side) | NavRail/Drawer |
| Dialog | Fullscreen | Default | Default |
| List-Detail | Separate pages | Side-by-side | Side-by-side |
| Card Grid | 1 column | 2 columns | 3-4 columns |
| AppBar | Small | Small | Small/Medium |

---

## 8. CSS 鑷畾涔夊睘鎬у畬鏁村０鏄庡潡

```css
/* ============================================================
   MD3 Design Token 鈥?CSS Custom Properties 瀹屾暣澹版槑
   灏嗕互涓嬩唬鐮佸潡鏀惧湪 :root {} 涓互鍚敤瀹屾暣 MD3 涓婚
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

  /* ----- Typography 鈥?Display ----- */
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

  /* ----- Typography 鈥?Headline ----- */
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

  /* ----- Typography 鈥?Title ----- */
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

  /* ----- Typography 鈥?Body ----- */
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

  /* ----- Typography 鈥?Label ----- */
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
