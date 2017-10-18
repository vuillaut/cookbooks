#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTool
baseCommand: prun2ptablehillas
inputs:
  config:
    type: string
    inputBinding:
      position: 2
      prefix: -c
  prun_file:
    type: File
    inputBinding:
      prefix: -i
      separate: true
      position: 1

outputs:
  ptablehillas_file:
    type: File
    outputBinding:
      glob: '*.ptabhillas'
