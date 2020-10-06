# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)

## v0.0.5

### Changed

- made compatible with python3 instead of python2

## v.0.0.4

### Added

- added ability to change colors for each row dynamically in the settings area of the web interface
- add INSTALL document

### Changed

- updated README
- update row description to reflect changes in layout and colors

## v0.0.3

### Added

- added settings constants to ```constants.py``` file to these can be referenced more easily
- added settings.html page as a way to manage advanced settings, only 24 hr clock for now

### Changed

- use orange/red for AM/PM (if using 12 hr clock) and white for alarm color
- don't adjust brightness for alarm, it's bright enough
- show time on index.html as either 24 or 12 hour format depending on setting
- adjusted spacing with a blank row between the date and time

## v.0.0.2

### Added

- added military_time setting to show either 24 or 12 hr values on the clock, right now only accessible when editing the file directly

### Changed

- changed the macro to allow generically setting any value in the settings file, not just the alarm time

## v0.0.1

### Added

- all project files. working version of this adapted from source: (https://github.com/pimoroni/unicorn-hat/blob/master/examples/binary_clock.py)[https://github.com/pimoroni/unicorn-hat/blob/master/examples/binary_clock.py]
