# Design Guide

This project follows a **Corporate Clean Blue, Gradient Glass UI, Metallic Chrome** aesthetic. When writing HTML/CSS, designing new components, or modifying existing ones, strictly adhere to the following principles:

## Typography
- **Body Font**: `Outfit`, sans-serif. Used for general text, clean, modern, and highly readable.
- **Headings & Accents**: `Syncopate`, sans-serif. Used for titles, headers, and key buttons. Always uppercase with slight negative letter-spacing for a technical, corporate look.

## Color Palette
- **Backgrounds**: Deep, rich corporate blue gradients (`#070e17` to `#111f38`) with subtle radial glowing color spots.
- **Primary Accents**: Electric corporate blue (`#0077ff`) and glowing success green (`#00d084`).
- **Text**: Main text is crisp off-white (`#f0f5fa`). Muted text is a cool gray-blue (`#8b9eb7`).
- **Chrome Effect**: Prominent text (like `h1` titles) should use silver/metallic linear gradients masked to the text.

## UI Elements & Glassmorphism
- **Panels & Cards**: Utilize translucent glass container backgrounds (e.g., `rgba(20, 35, 60, 0.4)`) with heavy backdrop blurs (`blur(24px) saturate(180%)`).
- **Borders & Edges**: Use extremely faint white borders (`rgba(255, 255, 255, 0.08)`) coupled with inset bounding highlights (e.g., `inset 0 1px 0 rgba(255, 255, 255, 0.1)`) to reflect light like physical glass edges.
- **Buttons**: Strong linear gradients with outer drop shadows (glows) and an inner sheen. Hover states should include a metallic sweeping shine or lifting effect.
- **Form Inputs**: Deep, dark inputs (`rgba(0, 0, 0, 0.2)`) with subtle inner shadows to appear recessed into the glass panels.
- **Corners**: Polished, smooth rounded radii (`8px` for small elements, `16px` for cards, `24px` for large structural layouts).