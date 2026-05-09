#!/usr/bin/env python3
"""
MD3 Theme Token Generator
浠庣瀛愯壊鑷姩鐢熸垚 Material Design 3 涓婚鏂囦欢锛屾敮鎸佸绉嶈緭鍑烘牸寮忋€?
Usage:
    python generate_tokens.py --seed '#6750A4' --format css --output theme.css
    python generate_tokens.py --seed '#6750A4' --format scss --output _theme.scss
    python generate_tokens.py --seed '#6750A4' --format json --output tokens.json
    python generate_tokens.py --seed '#6750A4' --format tailwind --output tailwind-m3.js
    python generate_tokens.py --seed '#6750A4' --format flutter --output theme.dart
    python generate_tokens.py --seed '#6750A4' --format all --output-dir ./theme
"""

import argparse
import json
import colorsys
import math
import os

# ============================================================
#  HCT 鑹插僵绌洪棿杩戜技杞崲 (绠€鍖栫増)
#  Material Color Utilities 鐨勬牳蹇冪畻娉曠畝鍖?# ============================================================

def hex_to_rgb(hex_color: str) -> tuple:
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_hex(r: float, g: float, b: float) -> str:
    """Convert RGB to hex string."""
    r = max(0, min(255, round(r)))
    g = max(0, min(255, round(g)))
    b = max(0, min(255, round(b)))
    return f'#{r:02X}{g:02X}{b:02X}'


def linearize(c: float) -> float:
    """Linearize an RGB component."""
    c = c / 255.0
    if c <= 0.04045:
        return c / 12.92
    return ((c + 0.055) / 1.055) ** 2.4


def delinearize(c: float) -> float:
    """Delinearize to sRGB component."""
    if c <= 0.0031308:
        return max(0, c * 12.92 * 255)
    return max(0, (1.055 * (c ** (1 / 2.4)) - 0.055) * 255)


def luminance(r: int, g: int, b: int) -> float:
    """Calculate relative luminance of an sRGB color."""
    return 0.2126 * linearize(r) + 0.7152 * linearize(g) + 0.0722 * linearize(b)


def tone_from_luminance(lum: float) -> float:
    """Convert luminance to tone (L* in LCh, approximated)."""
    if lum <= 0.008856:
        return lum * 903.3
    return 116 * (lum ** (1/3)) - 16


def luminance_from_tone(tone: float) -> float:
    """Convert tone back to luminance (approximate)."""
    if tone <= 8:
        return tone / 903.3
    return ((tone + 16) / 116) ** 3


def blend_colors(color1: tuple, color2: tuple, ratio: float) -> tuple:
    """Blend two RGB colors by ratio (0-1)."""
    return tuple(
        int(c1 * (1 - ratio) + c2 * ratio)
        for c1, c2 in zip(color1, color2)
    )


def generate_tonal_palette(seed_hex: str) -> dict:
    """
    Generate a tonal palette from a seed color.
    Returns a dict with tones 0-100 as keys and hex colors as values.
    
    This is a simplified approximation of Material's HCT algorithm.
    In production, use the material-color-utilities library.
    """
    seed_rgb = hex_to_rgb(seed_hex)
    seed_h, seed_s, seed_l = colorsys.rgb_to_hls(
        seed_rgb[0]/255, seed_rgb[1]/255, seed_rgb[2]/255
    )
    
    # Calculate chroma from saturation
    seed_chroma = seed_s * 150  # Approximate
    
    palette = {}
    
    for tone in range(0, 101):
        # Simplified tone mapping
        target_l = tone / 100.0
        
        # Adjust saturation: lower tones = more muted, higher tones = less saturated
        if tone < 20:
            adj_chroma = seed_chroma * (tone / 20) * 0.6
        elif tone > 80:
            adj_chroma = seed_chroma * ((100 - tone) / 20) * 0.6
        else:
            adj_chroma = seed_chroma * 0.6
        
        # Convert back to RGB
        r, g, b = colorsys.hls_to_rgb(seed_h, target_l, adj_chroma / 150)
        palette[tone] = rgb_to_hex(r * 255, g * 255, b * 255)
    
    return palette


def generate_scheme(seed_hex: str) -> dict:
    """
    Generate a complete M3 ColorScheme from a seed color.
    """
    primary_palette = generate_tonal_palette(seed_hex)
    
    # Secondary: shift hue by ~30 degrees, lower chroma
    seed_rgb = hex_to_rgb(seed_hex)
    seed_h, seed_s, seed_l = colorsys.rgb_to_hls(
        seed_rgb[0]/255, seed_rgb[1]/255, seed_rgb[2]/255
    )
    secondary_h = (seed_h + 0.0833) % 1.0  # +30 degrees
    secondary_rgb = colorsys.hls_to_rgb(secondary_h, seed_l, seed_s * 0.7)
    secondary_hex = rgb_to_hex(secondary_rgb[0]*255, secondary_rgb[1]*255, secondary_rgb[2]*255)
    secondary_palette = generate_tonal_palette(secondary_hex)
    
    # Tertiary: shift hue by ~60 degrees
    tertiary_h = (seed_h + 0.1667) % 1.0
    tertiary_rgb = colorsys.hls_to_rgb(tertiary_h, seed_l, seed_s * 0.5)
    tertiary_hex = rgb_to_hex(tertiary_rgb[0]*255, tertiary_rgb[1]*255, tertiary_rgb[2]*255)
    tertiary_palette = generate_tonal_palette(tertiary_hex)
    
    # Neutral: desaturated
    neutral_rgb = colorsys.hls_to_rgb(seed_h, seed_l, 0.05)
    neutral_hex = rgb_to_hex(neutral_rgb[0]*255, neutral_rgb[1]*255, neutral_rgb[2]*255)
    neutral_palette = generate_tonal_palette(neutral_hex)
    
    # Neutral variant: slightly more chromatic
    nv_rgb = colorsys.hls_to_rgb(seed_h, seed_l, 0.08)
    nv_hex = rgb_to_hex(nv_rgb[0]*255, nv_rgb[1]*255, nv_rgb[2]*255)
    nv_palette = generate_tonal_palette(nv_hex)
    
    def get_safe(palette, tone, fallback_tone=None):
        """Get a palette color, falling back to a nearby tone if needed."""
        if tone in palette:
            return palette[tone]
        if fallback_tone is not None and fallback_tone in palette:
            return palette[fallback_tone]
        return palette[min(palette.keys(), key=lambda x: abs(x - tone))]
    
    light_scheme = {
        'primary': get_safe(primary_palette, 40),
        'onPrimary': '#FFFFFF',
        'primaryContainer': get_safe(primary_palette, 90),
        'onPrimaryContainer': get_safe(primary_palette, 10),
        
        'secondary': get_safe(secondary_palette, 40),
        'onSecondary': '#FFFFFF',
        'secondaryContainer': get_safe(secondary_palette, 90),
        'onSecondaryContainer': get_safe(secondary_palette, 10),
        
        'tertiary': get_safe(tertiary_palette, 40),
        'onTertiary': '#FFFFFF',
        'tertiaryContainer': get_safe(tertiary_palette, 90),
        'onTertiaryContainer': get_safe(tertiary_palette, 10),
        
        'error': '#B3261E',
        'onError': '#FFFFFF',
        'errorContainer': '#F9DEDC',
        'onErrorContainer': '#410E0B',
        
        'background': get_safe(neutral_palette, 99),
        'onBackground': get_safe(neutral_palette, 10),
        'surface': get_safe(neutral_palette, 99),
        'onSurface': get_safe(neutral_palette, 10),
        'surfaceVariant': get_safe(nv_palette, 90),
        'onSurfaceVariant': get_safe(nv_palette, 30),
        
        'surfaceDim': get_safe(neutral_palette, 87),
        'surfaceBright': get_safe(neutral_palette, 98),
        'surfaceContainerLowest': '#FFFFFF',
        'surfaceContainerLow': get_safe(neutral_palette, 96),
        'surfaceContainer': get_safe(neutral_palette, 94),
        'surfaceContainerHigh': get_safe(neutral_palette, 92),
        'surfaceContainerHighest': get_safe(neutral_palette, 90),
        
        'outline': get_safe(nv_palette, 50),
        'outlineVariant': get_safe(nv_palette, 80),
        
        'inverseSurface': get_safe(neutral_palette, 20),
        'inverseOnSurface': get_safe(neutral_palette, 95),
        'inversePrimary': get_safe(primary_palette, 80),
        
        'shadow': '#000000',
        'scrim': '#000000',
    }
    
    dark_scheme = {
        'primary': get_safe(primary_palette, 80),
        'onPrimary': get_safe(primary_palette, 20),
        'primaryContainer': get_safe(primary_palette, 30),
        'onPrimaryContainer': get_safe(primary_palette, 90),
        
        'secondary': get_safe(secondary_palette, 80),
        'onSecondary': get_safe(secondary_palette, 20),
        'secondaryContainer': get_safe(secondary_palette, 30),
        'onSecondaryContainer': get_safe(secondary_palette, 90),
        
        'tertiary': get_safe(tertiary_palette, 80),
        'onTertiary': get_safe(tertiary_palette, 20),
        'tertiaryContainer': get_safe(tertiary_palette, 30),
        'onTertiaryContainer': get_safe(tertiary_palette, 90),
        
        'error': '#F2B8B5',
        'onError': '#601410',
        'errorContainer': '#8C1D18',
        'onErrorContainer': '#F9DEDC',
        
        'background': get_safe(neutral_palette, 6),
        'onBackground': get_safe(neutral_palette, 90),
        'surface': get_safe(neutral_palette, 6),
        'onSurface': get_safe(neutral_palette, 90),
        'surfaceVariant': get_safe(nv_palette, 30),
        'onSurfaceVariant': get_safe(nv_palette, 80),
        
        'surfaceDim': get_safe(neutral_palette, 6),
        'surfaceBright': get_safe(neutral_palette, 24),
        'surfaceContainerLowest': get_safe(neutral_palette, 4),
        'surfaceContainerLow': get_safe(neutral_palette, 10),
        'surfaceContainer': get_safe(neutral_palette, 12),
        'surfaceContainerHigh': get_safe(neutral_palette, 17),
        'surfaceContainerHighest': get_safe(neutral_palette, 22),
        
        'outline': get_safe(nv_palette, 60),
        'outlineVariant': get_safe(nv_palette, 30),
        
        'inverseSurface': get_safe(neutral_palette, 90),
        'inverseOnSurface': get_safe(neutral_palette, 20),
        'inversePrimary': get_safe(primary_palette, 40),
        
        'shadow': '#000000',
        'scrim': '#000000',
    }
    
    return {
        'seed': seed_hex,
        'light': light_scheme,
        'dark': dark_scheme,
    }


# ============================================================
#  鏍煎紡鐢熸垚鍣?# ============================================================

TOKEN_TO_CSS_VAR = {
    'primary': '--md-sys-color-primary',
    'onPrimary': '--md-sys-color-on-primary',
    'primaryContainer': '--md-sys-color-primary-container',
    'onPrimaryContainer': '--md-sys-color-on-primary-container',
    'secondary': '--md-sys-color-secondary',
    'onSecondary': '--md-sys-color-on-secondary',
    'secondaryContainer': '--md-sys-color-secondary-container',
    'onSecondaryContainer': '--md-sys-color-on-secondary-container',
    'tertiary': '--md-sys-color-tertiary',
    'onTertiary': '--md-sys-color-on-tertiary',
    'tertiaryContainer': '--md-sys-color-tertiary-container',
    'onTertiaryContainer': '--md-sys-color-on-tertiary-container',
    'error': '--md-sys-color-error',
    'onError': '--md-sys-color-on-error',
    'errorContainer': '--md-sys-color-error-container',
    'onErrorContainer': '--md-sys-color-on-error-container',
    'background': '--md-sys-color-background',
    'onBackground': '--md-sys-color-on-background',
    'surface': '--md-sys-color-surface',
    'onSurface': '--md-sys-color-on-surface',
    'surfaceVariant': '--md-sys-color-surface-variant',
    'onSurfaceVariant': '--md-sys-color-on-surface-variant',
    'surfaceDim': '--md-sys-color-surface-dim',
    'surfaceBright': '--md-sys-color-surface-bright',
    'surfaceContainerLowest': '--md-sys-color-surface-container-lowest',
    'surfaceContainerLow': '--md-sys-color-surface-container-low',
    'surfaceContainer': '--md-sys-color-surface-container',
    'surfaceContainerHigh': '--md-sys-color-surface-container-high',
    'surfaceContainerHighest': '--md-sys-color-surface-container-highest',
    'outline': '--md-sys-color-outline',
    'outlineVariant': '--md-sys-color-outline-variant',
    'inverseSurface': '--md-sys-color-inverse-surface',
    'inverseOnSurface': '--md-sys-color-inverse-on-surface',
    'inversePrimary': '--md-sys-color-inverse-primary',
    'shadow': '--md-sys-color-shadow',
    'scrim': '--md-sys-color-scrim',
}


def generate_css(scheme: dict) -> str:
    """Generate CSS Custom Properties from scheme."""
    lines = [
        '/* ============================================================',
        f'   MD3 Theme 鈥?Generated from seed: {scheme["seed"]}',
        '   ============================================================ */',
        '',
    ]
    
    # Light theme
    lines.append(':root {')
    for token_name, css_var in TOKEN_TO_CSS_VAR.items():
        lines.append(f'  {css_var}: {scheme["light"][token_name]};')
    lines.append('}')
    lines.append('')
    
    # Dark theme
    lines.append('@media (prefers-color-scheme: dark) {')
    lines.append('  :root {')
    for token_name, css_var in TOKEN_TO_CSS_VAR.items():
        lines.append(f'    {css_var}: {scheme["dark"][token_name]};')
    lines.append('  }')
    lines.append('}')
    lines.append('')
    
    # Dark theme via class (for manual toggle)
    lines.append('/* Manual dark mode toggle */')
    lines.append('[data-theme="dark"] {')
    for token_name, css_var in TOKEN_TO_CSS_VAR.items():
        lines.append(f'  {css_var}: {scheme["dark"][token_name]};')
    lines.append('}')
    
    return '\n'.join(lines)


def generate_scss(scheme: dict) -> str:
    """Generate SCSS variables from scheme."""
    lines = [
        f'// MD3 Theme 鈥?Generated from seed: {scheme["seed"]}',
        '',
        '// Light theme',
    ]
    
    for token_name, css_var in TOKEN_TO_CSS_VAR.items():
        scss_name = css_var.replace('--md-sys-color-', '').replace('-', '-')
        lines.append(f'${scss_name}: {scheme["light"][token_name]};')
    
    lines.append('')
    lines.append('// Dark theme')
    for token_name, css_var in TOKEN_TO_CSS_VAR.items():
        scss_name = css_var.replace('--md-sys-color-', '').replace('-', '-')
        lines.append(f'${scss_name}-dark: {scheme["dark"][token_name]};')
    
    return '\n'.join(lines)


def generate_json_tokens(scheme: dict) -> str:
    """Generate JSON tokens from scheme."""
    tokens = {
        'seed': scheme['seed'],
        'light': {},
        'dark': {},
    }
    
    for token_name, css_var in TOKEN_TO_CSS_VAR.items():
        token_key = css_var.replace('--md-sys-color-', '')
        tokens['light'][token_key] = {
            'value': scheme['light'][token_name],
            'type': 'color',
        }
        tokens['dark'][token_key] = {
            'value': scheme['dark'][token_name],
            'type': 'color',
        }
    
    return json.dumps(tokens, indent=2, ensure_ascii=False)


def generate_tailwind(scheme: dict) -> str:
    """Generate Tailwind CSS preset from scheme."""
    tailwind_colors = {}
    
    for token_name, css_var in TOKEN_TO_CSS_VAR.items():
        key = css_var.replace('--md-sys-color-', '')
        # Convert kebab-case to camelCase
        parts = key.split('-')
        camel = parts[0] + ''.join(p.capitalize() for p in parts[1:])
        tailwind_colors[camel] = scheme['light'][token_name]
    
    lines = [
        '// Tailwind CSS MD3 Preset',
        f'// Generated from seed: {scheme["seed"]}',
        '',
        'module.exports = {',
        '  theme: {',
        '    extend: {',
        '      colors: {',
        '        md3: {',
    ]
    
    for name, color in tailwind_colors.items():
        lines.append(f'          {name}: "{color}",')
    
    # Dark variants
    lines.append('        },')
    lines.append('        "md3-dark": {')
    for token_name, css_var in TOKEN_TO_CSS_VAR.items():
        key = css_var.replace('--md-sys-color-', '')
        parts = key.split('-')
        camel = parts[0] + ''.join(p.capitalize() for p in parts[1:])
        lines.append(f'          {camel}: "{scheme["dark"][token_name]}",')
    
    lines.extend([
        '        },',
        '      },',
        '      borderRadius: {',
        '        "md3-none": "0px",',
        '        "md3-xs": "4px",',
        '        "md3-sm": "8px",',
        '        "md3-md": "12px",',
        '        "md3-lg": "16px",',
        '        "md3-xl": "28px",',
        '        "md3-full": "9999px",',
        '      },',
        '    },',
        '  },',
        '  plugins: [],',
        '};',
    ])
    
    return '\n'.join(lines)


def generate_flutter(scheme: dict) -> str:
    """Generate Flutter ThemeData from scheme."""
    lines = [
        '// Flutter MD3 Theme',
        f'// Generated from seed: {scheme["seed"]}',
        '',
        "import 'package:flutter/material.dart';",
        '',
        'final md3LightScheme = ColorScheme.light(',
    ]
    
    flutter_mappings = {
        'primary': ('primary', 'light'),
        'onPrimary': ('onPrimary', 'light'),
        'primaryContainer': ('primaryContainer', 'light'),
        'onPrimaryContainer': ('onPrimaryContainer', 'light'),
        'secondary': ('secondary', 'light'),
        'onSecondary': ('onSecondary', 'light'),
        'secondaryContainer': ('secondaryContainer', 'light'),
        'onSecondaryContainer': ('onSecondaryContainer', 'light'),
        'tertiary': ('tertiary', 'light'),
        'onTertiary': ('onTertiary', 'light'),
        'tertiaryContainer': ('tertiaryContainer', 'light'),
        'onTertiaryContainer': ('onTertiaryContainer', 'light'),
        'error': ('error', 'light'),
        'onError': ('onError', 'light'),
        'errorContainer': ('errorContainer', 'light'),
        'onErrorContainer': ('onErrorContainer', 'light'),
        'background': ('background', 'light'),
        'onBackground': ('onBackground', 'light'),
        'surface': ('surface', 'light'),
        'onSurface': ('onSurface', 'light'),
        'surfaceVariant': ('surfaceVariant', 'light'),
        'onSurfaceVariant': ('onSurfaceVariant', 'light'),
        'outline': ('outline', 'light'),
        'outlineVariant': ('outlineVariant', 'light'),
        'inverseSurface': ('inverseSurface', 'light'),
        'inverseOnSurface': ('inverseOnSurface', 'light'),
        'inversePrimary': ('inversePrimary', 'light'),
        'shadow': ('shadow', 'light'),
        'scrim': ('scrim', 'light'),
    }
    
    for token_name, (flutter_name, theme) in flutter_mappings.items():
        hex_val = scheme[theme][token_name].lstrip('#')
        lines.append(f'  {flutter_name}: const Color(0xFF{hex_val}),')
    
    lines.append(');')
    lines.append('')
    
    lines.append('final ThemeData md3LightTheme = ThemeData(')
    lines.append('  useMaterial3: true,')
    lines.append('  colorScheme: md3LightScheme,')
    lines.append(');')
    
    return '\n'.join(lines)


# ============================================================
#  CLI
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description='MD3 Theme Token Generator 鈥?Generate M3 themes in various formats'
    )
    parser.add_argument(
        '--seed', type=str, default='#6750A4',
        help='Seed color hex (default: #6750A4 鈥?M3 default purple)'
    )
    parser.add_argument(
        '--format', type=str, default='css',
        choices=['css', 'scss', 'json', 'tailwind', 'flutter', 'all'],
        help='Output format (default: css)'
    )
    parser.add_argument(
        '--output', type=str, default=None,
        help='Output file path'
    )
    parser.add_argument(
        '--output-dir', type=str, default='./theme',
        help='Output directory for --format all'
    )
    
    args = parser.parse_args()
    
    print(f'馃帹 Generating MD3 theme from seed: {args.seed}')
    
    scheme = generate_scheme(args.seed)
    
    generators = {
        'css': (generate_css, '.css'),
        'scss': (generate_scss, '.scss'),
        'json': (generate_json_tokens, '.json'),
        'tailwind': (generate_tailwind, '.js'),
        'flutter': (generate_flutter, '.dart'),
    }
    
    if args.format == 'all':
        os.makedirs(args.output_dir, exist_ok=True)
        for fmt, (gen_fn, ext) in generators.items():
            content = gen_fn(scheme)
            output_path = os.path.join(args.output_dir, f'md3-theme{ext}')
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'  鉁?Generated {output_path}')
        print(f'\n鉁?All theme files generated in {args.output_dir}/')
    else:
        gen_fn, ext = generators[args.format]
        content = gen_fn(scheme)
        
        if args.output:
            output_path = args.output
        else:
            output_path = f'md3-theme{ext}'
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f'  鉁?Generated {output_path}')
        print(f'\n馃挕 Tip: Use --format all to generate all formats at once.')


if __name__ == '__main__':
    main()
