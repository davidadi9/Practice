//go:build ignore

package main

import (
	"bytes"
	"go/format"
	"log"
	"os"
	"path/filepath"
	"regexp"
	"text/template"
)

var tmpl = `
{{define "analyzers"}}
// Code generated by generate.go. DO NOT EDIT.

package {{.dir}}

import (
	"honnef.co/go/tools/analysis/lint"
{{- range $check := .checks}}
	"honnef.co/go/tools/{{$.dir}}/{{$check}}"
{{- end}}
)

var Analyzers = []*lint.Analyzer{
{{- range $check := .checks}}
	{{$check}}.SCAnalyzer,
{{- end}}
}
{{end}}

{{define "tests"}}
// Code generated by generate.go. DO NOT EDIT.

package {{.check}}

import (
	"testing"

	"honnef.co/go/tools/analysis/lint/testutil"
)

func TestTestdata(t *testing.T) {
	testutil.Run(t, SCAnalyzer)
}
{{end}}
`

func main() {
	log.SetFlags(0)

	dir, err := os.Getwd()
	if err != nil {
		log.Fatalln("couldn't determine current directory:", err)
	}

	dir = filepath.Base(dir)

	var t template.Template
	if _, err = t.Parse(tmpl); err != nil {
		log.Fatalln("couldn't parse templates:", err)
	}

	dirs, err := filepath.Glob("*")
	if err != nil {
		log.Fatalln("couldn't enumerate checks:", err)
	}

	checkRe := regexp.MustCompile(`^[a-z]+\d{4}$`)
	out := dirs[:0]
	for _, dir := range dirs {
		if checkRe.MatchString(dir) {
			out = append(out, dir)
		}
	}
	dirs = out

	buf := bytes.NewBuffer(nil)

	if err := t.ExecuteTemplate(buf, "analyzers", map[string]any{"checks": dirs, "dir": dir}); err != nil {
		log.Fatalln("couldn't generate analysis.go:", err)
	}

	b, err := format.Source(buf.Bytes())
	if err != nil {
		log.Fatalln("couldn't gofmt analysis.go:", err)
	}
	if err := os.WriteFile("analysis.go", b, 0666); err != nil {
		log.Fatalln("couldn't write analysis.go:", err)
	}

	for _, dir := range dirs {
		buf.Reset()
		dst := filepath.Join(dir, dir+"_test.go")
		if err := t.ExecuteTemplate(buf, "tests", map[string]any{"check": dir}); err != nil {
			log.Fatalf("couldn't generate %s: %s", dst, err)
		}

		b, err := format.Source(buf.Bytes())
		if err != nil {
			log.Fatalf("couldn't gofmt %s: %s", dst, err)
		}
		if err := os.WriteFile(dst, b, 0666); err != nil {
			log.Fatalf("couldn't write %s: %s", dst, err)
		}
	}
}
