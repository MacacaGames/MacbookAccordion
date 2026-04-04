# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

MacBook Lid Accordion — a Python app that turns a MacBook into a virtual accordion by reading the lid angle sensor as bellows input. Keys are played via keyboard; audio is synthesized in real time. Falls back to simulation mode (arrow keys) when the sensor is unavailable.

Bundle ID: `games.macaca.lidaccordion`, version `0.0.1`.

## Commands

### Run directly (development)
```bash
pip install pygame numpy sounddevice pybooklid
python lid_accordion.py
```

### Build macOS .app bundle
```bash
chmod +x build_mac_app.sh
./build_mac_app.sh
# Output: dist/LidAccordion.app/Contents/MacOS/LidAccordion
```

The build script creates a venv, installs deps (including py2app), and runs `setup.py py2app`.

## Architecture

The entire application lives in a single file: `lid_accordion.py`.

### Key components (all in `lid_accordion.py`):

- **`PolyAccordionSynth`** — Thread-safe polyphonic synth engine. Generates audio via dual detuned sawtooth waves with tanh soft-clipping. Manages per-voice state (phase, envelope) and bellows-driven volume. Called from `sounddevice` audio callback at 44100 Hz / 256-sample blocks.

- **Bellows pipeline** (in `main()` loop) — Reads lid angle via `pybooklid.read_lid_angle()`, computes angular velocity, maps it through dead zone / fill / leak / smoothing params to produce a 0–1 bellows value fed to the synth.

- **Key mapping** — Four lookup tables (`WHITE_Q`, `BLACK_1`, `WHITE_Z`, `BLACK_A`) map pygame key constants to MIDI note numbers across two octave groups. Octave transposition via Shift/Ctrl/Tab key-up events.

- **GUI** — Pygame-based. Fixed header (mode, angle gauge, bellows bar) + scrollable parameter panel with `Slider` widgets and a custom `ScrollBar`. The `Param` dataclass holds per-parameter metadata (range, step, format, group).

- **`_ensure_sounddevice_portaudio_filesystem()`** — Workaround at top of file that extracts PortAudio binaries from py2app's zipped Python stdlib so `sounddevice` can find them at runtime.

### External dependencies
`pygame`, `numpy`, `sounddevice`, `pybooklid` (lid angle sensor via IOKit). `py2app` is build-only.
