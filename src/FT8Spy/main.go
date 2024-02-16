package main

import (
	"fmt"
	"log"

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
}
