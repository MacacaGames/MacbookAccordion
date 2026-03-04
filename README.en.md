# Lid Accordion

[繁體中文](README.md)

A side project that turns your MacBook into a virtual accordion by using the lid opening angle as the bellows.

Built in spare time at work, developed step by step with the help of ChatGPT.

---

## Overview

- Reads the MacBook lid angle sensor to simulate accordion bellows push/pull motion
- Play notes via keyboard keys; audio is synthesized in real time using `PolyAccordionSynth`
- Provides a GUI parameter panel for live adjustment of bellows sensitivity, timbre, and more
- Automatically falls back to simulation mode (↑↓ keys control angle) when the physical sensor is unavailable

---

## Technical Reference

The method for reading the MacBook Lid Angle Sensor is based on:

> [https://github.com/samhenrigold/LidAngleSensor](https://github.com/samhenrigold/LidAngleSensor)

---

## Requirements

| Item | Version / Notes |
|------|----------------|
| OS | macOS |
| Python | 3.x |
| Main packages | `pygame`, `numpy`, `sounddevice`, `pybooklid` |

---

## Build & Run

### 1. Package as a .app bundle

```bash
cd lid_accordion_mac_app_sounddevice
chmod +x build_mac_app.sh
./build_mac_app.sh
```

After packaging, the executable is located at:

```
dist/LidAccordion.app/Contents/MacOS/LidAccordion
```

### 2. Run directly with Python (development)

```bash
pip install pygame numpy sounddevice pybooklid
python lid_accordion.py
```

---

## Key Bindings

The keyboard is mapped to two octave ranges, laid out to mimic a piano's black and white keys.

### Group 1 (Mid range, MIDI 60–78)

| Type | Keys | Notes |
|------|------|-------|
| White keys | `Q` `W` `E` `R` `T` `Y` `U` `I` `O` `P` | C4 D4 E4 F4 G4 A4 B4 C5 D5 E5 |
| Black keys | `1` `2` `4` `5` `6` `8` `9` `0` | C#4 D#4 F#4 G#4 A#4 C#5 D#5 F#5 |

> Note: `3` and `7` are intentionally left unmapped to preserve piano black-key spacing.

### Group 2 (High range, MIDI 72–94)

| Type | Keys | Notes |
|------|------|-------|
| White keys | `Z` `X` `C` `V` `B` `N` `M` `,` `.` `/` | C5 D5 E5 F5 G5 A5 B5 C6 D6 E6 |
| Black keys | `A` `S` `D` `F` `G` `H` `J` `K` `L` `;` | C#5 D#5 F#5 G#5 A#5 C#6 D#6 F#6 G#6 A#6 |

### Octave Transpose

| Action | Effect |
|--------|--------|
| Release `Shift` | Shift up one octave (+12 semitones) |
| Release `Ctrl` | Shift down one octave (−12 semitones) |
| `Tab` | Reset to default octave (0) |

### Simulation Mode (when sensor is unavailable)

| Key | Effect |
|-----|--------|
| `↑` | Increase simulated lid angle (bellows open faster) |
| `↓` | Decrease simulated lid angle (bellows contract) |
| Mouse wheel | Scroll within the parameter panel |

---

## GUI Parameters

| Parameter | Description |
|-----------|-------------|
| Bellows sensitivity | Maximum bellows speed (affects angular velocity → volume mapping) |
| Ignore tiny movement | Dead zone threshold to ignore small tremors |
| How fast air builds | Air pressure accumulation rate |
| How fast air leaks | Air pressure leak rate |
| Volume rise smoothness | Smoothing coefficient for volume increase |
| Volume fall smoothness | Smoothing coefficient for volume decrease |
| Overall volume | Master volume |
| Note attack time | Note fade-in time (seconds) |
| Note release time | Note fade-out time (seconds) |
| Reed thickness (detune) | Dual sawtooth wave detune amount, simulating accordion reed thickness |
| Air / reed noise | Amount of airflow and reed noise |

---

## Roadmap

- [ ] Improve key layout for a more intuitive range mapping that better matches a real accordion keyboard
- [ ] Consider adding different timbres (tremolo, musette tuning, etc.)

---

## Version

`0.0.1` (Bundle ID: `games.macaca.lidaccordion`)
