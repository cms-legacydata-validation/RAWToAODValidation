cwlVersion: v1.0
class: CommandLineTool

baseCommand: /bin/zsh

requirements:
  DockerRequirement:
    dockerPull:
      clelange/cmssw:5_3_32
  InitialWorkDirRequirement:
    listing:
      - $(inputs.code)
      - $(inputs.data)

inputs:
  data:
    type: Directory
  code:
    type: Directory

stdout: compare.log

outputs:
  compare.log:
    type: stdout
  plot.png:
    type: File
    outputBinding:
       glob: "results/plot.png"

arguments:
  - prefix: -c
    valueFrom: |
      cp -r ../../code .; \
      scram b; \
      cd ../../code; \
      mkdir -p ../../../results; \
      cmsRun demoanalyzer_cfg.py
