---
# FT8Spy

FT8Spy is a system tray application written in Go that monitors a WSJT-X server for status messages and updates Discord Rich Presence accordingly. It uses the `fyne.io/systray` package for the system tray interface and `github.com/hugolgst/rich-go/client` for Discord Rich Presence integration.

## Features

- Monitors WSJT-X server for status messages.
- Updates Discord Rich Presence with information about WSJT-X status.
- Provides a system tray interface for easy access and quick exit.

## Installation

### Pre-built Executables

You can find pre-built executables for Windows in the [Releases](https://github.com/nodlek-ctrl/FT8Spy/releases) section.

## Configuration

- The Discord Rich Presence is updated with information about the WSJT-X status, including the mode and frequency when WSJT-X is open.
- Switch between frequencies or mode to force update the presence.
- The system tray icon provides a "Quit" option for easy termination of the application.

## Dependencies

- [fyne.io/systray](https://pkg.go.dev/fyne.io/systray): System tray package for Go.
- [github.com/hugolgst/rich-go/client](https://pkg.go.dev/github.com/hugolgst/rich-go/): Discord Rich Presence library for Go.
- [github.com/k0swe/wsjtx-go/v4](https://pkg.go.dev/github.com/k0swe/wsjtx-go/v4): WSJT-X client library for Go.

## Contributing

Feel free to contribute by opening issues or creating pull requests. Your feedback and enhancements are welcome!

## To Do
- [ ] Create Github Action to build for all systems (Current Priority)
- [ ] Document build process
- [ ] Make the progrm open and close with WSJT-X
- [ ] Support other digimode applications

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE Version 3 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The [fyne.io](https://fyne.io/) team for the system tray package.
- [hugolgst](https://github.com/hugolgst) for the Discord Rich Presence library.
- [k0swe](https://github.com/k0swe) for the WSJT-X client library.

---