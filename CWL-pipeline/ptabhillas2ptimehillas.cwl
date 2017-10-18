#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTool
baseCommand: ptablehillas2ptimehillas
inputs:
  config:
    type: File
    inputBinding:
      position: 2
      prefix: -c
  ptabhillas_file:
    type: File
    inputBinding:
      prefix: -i
      separate: true
      position: 1

outputs:
  ptimehillas_file:
    type: File
    outputBinding:
      glob: '*.ptimehillas'
