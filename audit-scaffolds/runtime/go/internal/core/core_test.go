package core

import "testing"

func TestRunEmpty(t *testing.T) {
	if got := Run(Config{}); got != 0 {
		t.Fatalf("Run(empty) = %d, want 0", got)
	}
}
