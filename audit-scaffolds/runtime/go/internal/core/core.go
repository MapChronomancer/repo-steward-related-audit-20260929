// Package core holds the runtime logic for study-notes.
package core

import "fmt"

// Config controls a Run.
type Config struct {
	Verbose bool
	Targets []string
}

// Run executes over the configured targets and returns an exit code.
func Run(cfg Config) int {
	if cfg.Verbose {
		fmt.Printf("[study-notes] %d targets\n", len(cfg.Targets))
	}
	for _, t := range cfg.Targets {
		process(t, cfg.Verbose)
	}
	return 0
}

func process(name string, verbose bool) {
	if verbose {
		fmt.Printf("  -> %s\n", name)
	}
}
