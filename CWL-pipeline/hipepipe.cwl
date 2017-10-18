#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: Workflow
inputs:
  prun_file: File
  config: File

outputs:
  reconstructed_file:
    type: File
    outputSource: ptimehillas2precoevent/precoevent_file

steps:
  prun2ptabhillas:
    run: prun2ptabhillas.cwl
    in:
      prun_file: prun_file
      config: config
    out: [ptablehillas_file]

  ptabhillas2ptimehillas:
    run: ptabhillas2ptimehillas.cwl
    in:
      ptabhillas_file: prun2ptabhillas/ptablehillas_file
      config: config
    out: [ptimehillas_file]

  ptimehillas2precoevent:
    run: ptimehillas2precoevent.cwl
    in:
      ptimehillas_file: ptabhillas2ptimehillas/ptimehillas_file
      config: config
    out: [precoevent_file]
