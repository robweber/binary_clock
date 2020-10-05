# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)

## 10/5/2020

### Added

- added settings constants to ```constants.py``` file to these can be referenced more easily

### Changed

- use orange/red for AM/PM (if using 12 hr clock) and white for alarm color
- don't adjust brightness for alarm, it's bright enough

## 10/4/2020

### Added

- added military_time setting to show either 24 or 12 hr values on the clock, right now only accessible when editing the file directly

### Changed

- changed the macro to allow generically setting any value in the settings file, not just the alarm time

## 10/3/2020

### Added

- all project files. working version of this adapted from source: (https://github.com/pimoroni/unicorn-hat/blob/master/examples/binary_clock.py)[https://github.com/pimoroni/unicorn-hat/blob/master/examples/binary_clock.py]
