#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: Workflow

requirements:
  InitialWorkDirRequirement:
    listing:
      - $(inputs.code)
      - $(inputs.data)

inputs:
  data:
    type: Directory
  code:
    type: Directory

outputs:
  plot.png:
    type: File
    outputSource:
      compare/plot.png

steps:
  rawreco:
    run: rawreco.cwl
    in:
      code: code
      data: data
    out: [reco_RAW2DIGI_L1Reco_RECO_ALCA_USER_DQM_inDQM.root, rawreco.log]
  compare:
    run: compare.cwl
    in:
      code: code
      data: data
      reco_RAW2DIGI_L1Reco_RECO_ALCA_USER_DQM_inDQM: rawreco/reco_RAW2DIGI_L1Reco_RECO_ALCA_USER_DQM_inDQM.root
    out: [plot.png, compare.log]
