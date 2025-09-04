# Hollow Knight: Silksong – 32:9 Ultrawide Fix

Silksong officially supports up to 21:9, but 32:9 users get black bars.  
This patched `Assembly-CSharp.dll` removes the aspect ratio cap so the game runs correctly in 32:9.  
Tested at **5120×1440** and **3840×1080** (Xbox Game Pass release).

## Install
1. Backup your original: `Hollow Knight- Silksong\Content\Hollow Knight Silksong_Data\Managed\Assembly-CSharp.dll`
2. Replace it with the patched `Assembly-CSharp.dll`.
3. Launch the game and enjoy!

## Notes
- Slight vignette/darkening still visible at the far edges (to be fixed later).
- May need re-patching after official updates.
