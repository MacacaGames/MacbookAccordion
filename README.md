# Lid Accordion

[English](README.en.md)

用 MacBook 的開蓋角度當作風箱，把 MacBook 變成一台虛擬手風琴的 Side Project。

利用上班空閒時間，透過 ChatGPT 協助逐步實作完成。

---

## 專案概述

- 偵測 MacBook 螢幕開蓋角度（Lid Angle Sensor），模擬手風琴的風箱推拉動作
- 搭配鍵盤按鍵彈奏音符，透過多音訊合成（PolyAccordionSynth）即時產生音效
- 提供 GUI 參數面板，可即時調整風箱靈敏度、音色等參數
- 若無法讀取實體感應器，自動切換為模擬模式（鍵盤 ↑↓ 控制角度）

---

## 技術參考

MacBook Lid Angle Sensor 的讀取方式參考自：

> [https://github.com/samhenrigold/LidAngleSensor](https://github.com/samhenrigold/LidAngleSensor)

---

## 環境需求

| 項目 | 版本／說明 |
|------|-----------|
| OS | macOS |
| Python | 3.x |
| 主要套件 | `pygame`, `numpy`, `sounddevice`, `pybooklid` |

---

## Build 與執行

### 1. 打包成 .app

```bash
cd lid_accordion_mac_app_sounddevice
chmod +x build_mac_app.sh
./build_mac_app.sh
```

打包完成後，執行檔位於：

```
dist/LidAccordion.app/Contents/MacOS/LidAccordion
```

### 2. 直接以 Python 執行（開發用）

```bash
pip install pygame numpy sounddevice pybooklid
python lid_accordion.py
```

---

## 按鍵配置

鍵盤對應兩組音域，佈局模擬鋼琴黑白鍵排列。

### 第一組（中音區，MIDI 60–78）

| 類型 | 按鍵 | 對應音符 |
|------|------|---------|
| 白鍵 | `Q` `W` `E` `R` `T` `Y` `U` `I` `O` `P` | C4 D4 E4 F4 G4 A4 B4 C5 D5 E5 |
| 黑鍵 | `1` `2` `4` `5` `6` `8` `9` `0` | C#4 D#4 F#4 G#4 A#4 C#5 D#5 F#5 |

> 注意：`3`、`7` 對應鍵盤間距無對應音符（刻意留空以符合鋼琴黑鍵位置）

### 第二組（高音區，MIDI 72–94）

| 類型 | 按鍵 | 對應音符 |
|------|------|---------|
| 白鍵 | `Z` `X` `C` `V` `B` `N` `M` `,` `.` `/` | C5 D5 E5 F5 G5 A5 B5 C6 D6 E6 |
| 黑鍵 | `A` `S` `D` `F` `G` `H` `J` `K` `L` `;` | C#5 D#5 F#5 G#5 A#5 C#6 D#6 F#6 G#6 A#6 |

### 八度移調

| 操作 | 效果 |
|------|------|
| `Shift` 放開 | 上移一個八度（+12 半音） |
| `Ctrl` 放開 | 下移一個八度（−12 半音） |
| `Tab` | 重置回預設八度（0） |

### 模擬模式（無感應器時）

| 按鍵 | 效果 |
|------|------|
| `↑` | 增加模擬開蓋角度（風箱加速） |
| `↓` | 減少模擬開蓋角度（風箱收縮） |
| 滑鼠滾輪 | 在參數區內捲動 |

---

## GUI 參數說明

| 參數 | 說明 |
|------|------|
| Bellows sensitivity | 風箱速度的最大值（影響角速度 → 音量映射） |
| Ignore tiny movement | 忽略小幅度晃動的死區閾值 |
| How fast air builds | 氣流累積速率 |
| How fast air leaks | 氣流洩漏速率 |
| Volume rise smoothness | 音量上升的平滑係數 |
| Volume fall smoothness | 音量下降的平滑係數 |
| Overall volume | 整體音量 |
| Note attack time | 音符淡入時間（秒） |
| Note release time | 音符淡出時間（秒） |
| Reed thickness (detune) | 雙鋸齒波音調差量，模擬手風琴簧片厚度感 |
| Air / reed noise | 氣流與簧片雜音量 |

---

## 未來規劃

- [ ] 優化按鍵配置，使音域佈局更直覺、更符合手風琴鍵盤習慣
- [ ] 考慮加入不同音色（tremolo、musette 調音等）

---

## 版本

`0.0.1`（Bundle ID: `games.macaca.lidaccordion`）
