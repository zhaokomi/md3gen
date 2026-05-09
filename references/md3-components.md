# MD3 缁勪欢瑙勮寖瀹屾暣鍙傝€?
> Material Design 3 鍏ㄩ儴缁勪欢鐨勮缁嗚鏍笺€傜敤浜?`/md3 <component>` 鍛戒护鐢熸垚浠ｇ爜鏃剁殑瑙勮寖渚濇嵁銆?
---

## 缁勪欢绱㈠紩

| 鍒嗙被 | 缁勪欢 | 鍙樹綋 |
|------|------|------|
| **Actions** | Button, FAB, IconButton, SegmentedButton | filled/outlined/text/elevated/tonal, 6 FAB variants, 4 icon button variants |
| **Communication** | Badge, Progress Indicator, Snackbar | 鈥? linear/circular, 鈥?|
| **Containment** | Card, Dialog, BottomSheet, SideSheet, Divider | elevated/filled/outlined, basic/fullscreen, 鈥? 鈥? 鈥?|
| **Navigation** | NavigationBar, NavigationRail, NavigationDrawer, Tabs, AppBar, Search | bar/rail/drawer, primary/secondary, standard/modal, 鈥? center/small/medium/large, 鈥?|
| **Selection** | Checkbox, Chip, DatePicker, Menu, RadioButton, Slider, Switch, TimePicker | 鈥? assist/filter/input/suggestion, 鈥? 鈥? 鈥? 鈥? 鈥? 鈥?|
| **Text Inputs** | TextField | filled/outlined |
| **Other** | Tooltip, ListItem, Carousel | plain/rich, 1-3line, 鈥?|

---

## Actions 鍔ㄤ綔缁勪欢

### Button 鎸夐挳

```
楂樺害: 40dp
鏈€灏忓: 48dp
Horizontal padding: 24dp
Shape: full (9999px = pill)
Typography: label-large (14sp, 500w)
State layer: yes
Ripple: yes
```

#### Filled Button

```
鑳屾櫙: primary
鏂囧瓧: on-primary
杞粨: none
娴锋嫈: 0 (no shadow)
鍥炬爣闂磋窛: 8dp
```

#### Outlined Button

```
鑳屾櫙: transparent
鏂囧瓧: primary
杞粨: outline (1px)
娴锋嫈: 0
```

#### Text Button

```
鑳屾櫙: transparent
鏂囧瓧: primary
杞粨: none
娴锋嫈: 0
Padding: 12dp horizontal
```

#### Elevated Button

```
鑳屾櫙: surface-container-low
鏂囧瓧: primary
杞粨: none
娴锋嫈: level 1
Shadow: level 1 box-shadow
```

#### Tonal Button

```
鑳屾櫙: secondary-container
鏂囧瓧: on-secondary-container
杞粨: none
娴锋嫈: 0
```

---

### FAB (Floating Action Button)

#### 灏哄琛?
| Variant | 灏哄 | 鍥炬爣 | Shape | 鏂囧瓧 |
|---------|------|------|-------|------|
| Primary (default) | 56x56dp | 24dp | large (16px) | 鈥?|
| Small | 40x40dp | 24dp | medium (12px) | 鈥?|
| Large | 96x96dp | 36dp | large (16px) | 鈥?|
| Extended | h:56dp | 24dp | large (16px) | label-large |

#### 棰滆壊琛?
| Variant | 鑳屾櫙 | 鍥炬爣鑹?|
|---------|------|--------|
| Primary | primary-container | on-primary-container |
| Surface | surface-container-high | primary |
| Secondary | secondary-container | on-secondary-container |
| Tertiary | tertiary-container | on-tertiary-container |

#### M3 vs M2

- M2: 鍦嗗舰, primary 鑳屾櫙
- M3: 鍦嗚鐭╁舰 (16px), primary-container 鑳屾櫙
- M3 鏂板 Large (96dp) 灏哄

---

### IconButton 鍥炬爣鎸夐挳

#### Variants

| Variant | 鑳屾櫙 | 鍥炬爣鑹?|
|---------|------|--------|
| Standard | transparent | on-surface-variant |
| Filled | primary | on-primary |
| Tonal | surface-variant | on-surface-variant |
| Outlined | transparent | on-surface-variant (border: outline) |

```
灏哄: 40x40dp
鍥炬爣: 24dp
Shape: full (9999px)
State layer: yes
```

#### Toggle IconButton

- 鏀寔閫変腑/鏈€変腑鐘舵€佸垏鎹?- 閫変腑鎬? filled variant 鏍峰紡

---

## Communication 閫氫俊缁勪欢

### Badge 寰芥爣

```
Shape: full (dot) / extra-small (with number)
鏈€灏忓昂瀵? 6x6dp (dot) / 16dp height (with number)
Typography: label-small
Color: error
```

### Progress Indicator 杩涘害鎸囩ず鍣?
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

### Snackbar 娑堟伅鏉?
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

## Containment 瀹瑰櫒缁勪欢

### Card 鍗＄墖

```
Shape: medium (12px)
```

| Variant | Background | Elevation | Outline |
|---------|-----------|-----------|---------|
| Elevated | surface-container-low | level 1 | none |
| Filled | surface-container-highest | 0 | none |
| Outlined | surface | 0 | outline-variant (1px) |

### Dialog 瀵硅瘽妗?
```
Shape: extra-large (28px)
Min width: 280dp
Max width: 560dp (Compact/Medium) / fullscreen (Compact alternative)
```

| 鍖哄煙 | Typography | 璇存槑 |
|------|-----------|------|
| Title | headline-small (24sp) | 鍙甫鍥炬爣 |
| Content | body-medium (14sp) | 鏈€澶?娈?|
| Actions | label-large (14sp) | 鍙冲榻?|

```
Padding: 24dp
Content padding: 16dp top + 24dp bottom
Button spacing: 8dp
Title icon: 24dp (optional)
```

#### Fullscreen Dialog

```
Top app bar: 鍖呭惈鍏抽棴鎸夐挳
Content: scrollable
Actions: 鍥哄畾鍦ㄥ簳閮?```

### BottomSheet 搴曢儴闈㈡澘

```
Top corners shape: extra-large (28px)
Background: surface-container-low
Drag handle: on-surface-variant (38% opacity), 32x4dp
Min height: 1/3 screen
Max height: depends on content
```

### Divider 鍒嗗壊绾?
```
Height: 1dp
Color: outline-variant
Inset: 0dp (full-width) / 16dp (with list) / 72dp (with icon)
```

---

## Navigation 瀵艰埅缁勪欢

### NavigationBar 搴曢儴瀵艰埅鏍?
```
Height: 80dp
Background: surface
Elevation: 0 (M3 鏃犻槾褰?
Item: max 5
Active indicator: secondary-container + outline
```

| Element | Size | Typography |
|---------|------|-----------|
| Icon (active) | 24dp | 鈥?|
| Icon (inactive) | 24dp | 鈥?|
| Label | 鈥?| label-medium (12sp) |
| Indicator | 32x64dp (full shape) | 鈥?|

### NavigationRail 渚ц竟瀵艰埅鏍?
```
Width: 80dp
Background: surface
Item: max 7
鐢ㄦ硶: Medium screen (600-839dp) 鏇夸唬 NavBar
```

### NavigationDrawer 鎶藉眽瀵艰埅

```
Modal width: 360dp
Standard width: 360dp (permanent)
Background: surface
Shape: end corners large (16px)
Elevation: level 1 (standard) / level 0 (modal)
```

### Top App Bar 椤堕儴搴旂敤鏍?
| Variant | 楂樺害 | Scroll琛屼负 |
|---------|------|-----------|
| Center-aligned | 64dp | 鏍囬濮嬬粓灞呬腑 |
| Small | 64dp | 鏍囧噯琛屼负 |
| Medium | 112dp | 鎶樺彔鏃舵爣棰樼缉灏?|
| Large | 152dp | 鎶樺彔鏃舵爣棰樼缉灏?|

```
Background: surface
Elevation: 0 (榛樿, 婊氬姩鍚庡鍔?level 2)
Typography: title-large (small) 鈫?headline-small (medium) 鈫?headline-medium (large)
Leading icon: 24dp (navigation icon / menu)
Trailing icons: 24dp (max 3)
```

**M2鈫扢3 鍏抽敭鍙樺寲**: 鍒犻櫎浜?`primary-variant` 瀹氫箟锛孉ppBar 鏇存矇娴搞€?
### Tabs 鏍囩椤?
```
Height: 48dp
Divider: outline-variant (1dp, bottom)
Active indicator: primary (3dp height)
Typography: title-small (14sp)
```

### Search 鎼滅储

```
SearchBar height: 56dp (collapsed) / varies (expanded)
Shape: full (pill) 鈫?extra-large (expanded view)
Background: surface-container-high
```

---

## Selection 閫夋嫨缁勪欢

### Chip 鏍囩

```
Height: 32dp
Shape: extra-small (4px)
Typography: label-large (14sp)
Leading icon: 18dp (optional)
Trailing icon: 18dp (optional, for close)
```

| Variant | 鐢ㄩ€?| 榛樿鐘舵€?|
|---------|------|---------|
| Assist | 杈呭姪鎿嶄綔 | 鏃犻€変腑鎬?|
| Filter | 澶氶€夌瓫閫?| toggle 閫変腑鎬?|
| Input | 杈撳叆鍨嬫爣绛?| trailing 鍏抽棴鍥炬爣 |
| Suggestion | 寤鸿鎿嶄綔 | 鏃犻€変腑鎬?|

**M2鈫扢3 鍏抽敭鍙樺寲**: Action Chip 鎷嗗垎涓?Assist + Suggestion锛涢粯璁ゆ棤闃村奖銆?
### Checkbox 澶嶉€夋

```
Size: 24dp
Shape: extra-small (4px)
Unchecked: outline (2dp border)
Checked: primary fill + on-primary check icon
Indeterminate: primary fill + minus icon
State layer: yes
Touch target: 48x48dp
```

### RadioButton 鍗曢€夋寜閽?
```
Size: 20dp (outer circle) / 10dp (inner dot)
Unchecked: outline (2dp border)
Checked: primary outer + primary inner dot
```

### Switch 寮€鍏?
```
Track: 52x32dp
Thumb: 24dp (unchecked) 鈫?24dp (checked)
Track shape: full (9999px)
```

| State | Track Color | Thumb Color |
|-------|------------|-------------|
| Unchecked | surface-variant | outline |
| Checked | primary | on-primary |
| Hover | state layer (8%) | 鈥?|
| Focus | state layer (12%) | 鈥?|

**M2鈫扢3**: 鏂板鍔犲鍕惧浘鏍囧湪 track 鍐咃紱闈㈢Н鏇村ぇ锛涙棤闃村奖銆?
### Slider 婊戝潡

```
Track height: 4dp (inactive) / 4dp (active)
Active track: primary
Inactive track: surface-variant
Thumb: primary (20dp), on-primary (inner dot)
Tick marks: on-surface-variant (opacity 38%)
Labels: above thumb
```

### Menu 鑿滃崟

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

### DatePicker 鏃ユ湡閫夋嫨鍣?
```
Day cell: 40x40dp
Shape: full (selected day)
Today indicator: primary outline
Selected: primary-container + on-primary-container
Weekday headers: label-small
Month/Year: title-medium
```

### TimePicker 鏃堕棿閫夋嫨鍣?
```
Dial face: surface-container-highest (40dp)
Dial selector: primary
Time input: body-large
Period selector (AM/PM): segmented button
```

---

## Text Inputs 鏂囨湰杈撳叆

### TextField 鏂囨湰杈撳叆妗?
| Variant | Shape | 鐗瑰緛 |
|---------|-------|------|
| Filled | top corners extra-small (4px) | filled background |
| Outlined | extra-small (4px) | transparent bg, outline edge |

```
Min height: 56dp
Padding: 16dp horizontal (start), 12dp (end)
```

| Element | Typography | Color |
|---------|-----------|-------|
| Label | body-large (16sp) 鈫?label-small (float) | on-surface-variant |
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

## Other 鍏朵粬缁勪欢

### Tooltip 宸ュ叿鎻愮ず

```
Background: inverse-surface
Text: inverse-on-surface
Typography: body-small (12sp)
Shape: extra-small (4px)
Padding: 4dp horizontal, 4dp vertical (plain) / 8dp (rich)
Delay: 500ms (show), 1500ms (show + persist)
```

### ListItem 鍒楄〃椤?
```
Min height: 56dp (1-line) / 72dp (2-line) / 88dp (3-line)
Padding: 16dp horizontal (start), 24dp (end)
```

| Element | Size | Typography |
|---------|------|-----------|
| Leading icon | 24dp | 鈥?|
| Leading avatar | 40x40dp (circle) | 鈥?|
| Leading image | 56x56dp | 鈥?|
| Title | 鈥?| body-large |
| Subtitle | 鈥?| body-medium |
| Supporting text | 鈥?| body-medium |
| Trailing icon | 24dp | 鈥?|
| Trailing text | 鈥?| label-small |

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

## 鏃犻殰纰嶉€熸煡

| 缁勪欢 | 閿洏鎿嶄綔 | ARIA |
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
| TextField | 鈥?| role="textbox" / aria-invalid (error) |
| Snackbar | 鈥?| role="alert", aria-live="polite" |
| ProgressBar | 鈥?| role="progressbar", aria-valuenow |
| Chip (input) | Backspace | role="button" |
