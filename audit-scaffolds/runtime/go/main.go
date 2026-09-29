// Command study_notes — theme label: Harmless documentation fixture \"quoted\".\nSecond line C:\\notes\u2028No AI execution..
package main

import (
	"os"

	"github.com/MapChronomancer/study-notes/internal/core"
)

func main() {
	cfg := core.Config{Verbose: true, Targets: os.Args[1:]}
	os.Exit(core.Run(cfg))
}
