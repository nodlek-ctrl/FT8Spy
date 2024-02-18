/*
FT8Spy is a Discord Rich Presence client for WSJT-X.
Copyright (C) 2024  Keldon Fletcher

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
*/

package main

import (
	"fmt"
	"log"

	"fyne.io/systray"
	"github.com/hugolgst/rich-go/client"
	"github.com/k0swe/wsjtx-go/v4"
)

const megahertzDivider = 1000000.0

func main() {
	err := client.Login("1207218142099677234")
	if err != nil {
		log.Fatal(err)
	}

	wsjtxServer, err := wsjtx.MakeServer()
	if err != nil {
		log.Fatal(err)
	}
	wsjtxChannel := make(chan interface{}, 5)
	errChannel := make(chan error, 5)

	go wsjtxServer.ListenToWsjtx(wsjtxChannel, errChannel)

	go func() {
		for {
			message := <-wsjtxChannel
			if m, ok := message.(wsjtx.StatusMessage); ok {
				freq := float64(m.DialFrequency) / megahertzDivider
				mode := m.Mode

				state := fmt.Sprintf("%s on %.3f MHz", mode, freq)

				err := client.SetActivity(client.Activity{
					State:      state,
					Details:    "Running WSJT-X",
					LargeImage: "logo",
					Buttons: []*client.Button{
						{
							Label: "Get FT8Spy!",
							Url:   "https://github.com/nodlek-ctrl/FT8Spy",
						},
					},
				})

				if err != nil {
					log.Fatal(err)
				}
			}
		}
	}()

	// Initialize system tray
	onExit := func() {
		log.Println("Exited")
	}
	systray.Run(onReady, onExit)
}

func onReady() {
	systray.SetTemplateIcon(Data, Data)
	systray.SetTitle("FT8Spy")
	mQuit := systray.AddMenuItem("Quit", "Quit FT8Spy")
	mQuit.Enable()
	go func() {
		<-mQuit.ClickedCh
		systray.Quit()
	}()
}
