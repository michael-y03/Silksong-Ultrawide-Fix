# Hollow Knight: Silksong – Ultrawide Fix

Silksong officially supports up to 21:9, but users with larger aspect ratios get black bars.  

This tool patches your local Assembly-CSharp.dll to remove the aspect ratio cap so the game runs correctly on larger screens.
✔️ Works with both **Steam** and **Game Pass** releases.

![Silksong in 32:9](image.png)

---

## Install (Easy Way)

1. Run the patcher:
   `python patch_silksong_ultrawide.py "...\Hollow Knight- Silksong\Content\Hollow Knight Silksong_Data\Managed\Assembly-CSharp.dll"`
2. Launch the game and enjoy!

Revert: restore the .bak file created alongside the DLL.

## DIY
If you’d rather patch your own DLL (useful if combining with other mods):  

- The game clamps aspect ratio between **16:9 (1.77)** and **~21:9 (2.39)**.  
- In `Assembly-CSharp.dll`, the **2.39 limit** is stored as the float `2.3916667`, which appears in hex as **`11 11 19 40`**.  
- To unlock up to **32:9 (3.56)**, replace all instances of **`11 11 19 40` → `39 8E 63 40`**.  
- There should be **3 occurrences** to replace.  

---

## Notes
- Game updates overwrite `Assembly-CSharp.dll`, so this fix may need to be reapplied after patches.
- This repository does not redistribute game files; the patcher modifies your local copy only.

## Nexus Mods
 - https://www.nexusmods.com/hollowknightsilksong/mods/1
