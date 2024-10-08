package ossfuzz

import (
	"bytes"
	"fmt"
	"strings"

	"github.com/BurntSushi/toml"
)

func FuzzToml(data []byte) int {
	if len(data) >= 2048 {
		return 0
	}

	var v any
	_, err := toml.Decode(string(data), &v)
	if err != nil {
		return 0
	}

	buf := new(bytes.Buffer)
	err = toml.NewEncoder(buf).Encode(v)
	if err != nil {
		panic(fmt.Sprintf("failed to encode decoded document: %s", err))
	}

	var v2 any
	_, err = toml.Decode(buf.String(), &v2)
	if err != nil {
		// TODO(manunio): remove this when 1.23 lands, see #407.
		if strings.Contains(err.Error(), "invalid datetime") {
			return 0
		}

		panic(fmt.Sprintf("failed round trip: %s", err))
	}

	return 1
}
