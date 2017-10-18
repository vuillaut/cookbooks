#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTool
baseCommand: ptimehillas2precoevent
inputs:
  config:
    type: File
    inputBinding:
      position: 2
      prefix: -c
  ptimehillas_file:
    type: File
    inputBinding:
      prefix: -i
      separate: true
      position: 1

outputs:
  precoevent_file:
    type: File
    outputBinding:
      glob: '*'
