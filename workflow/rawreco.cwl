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

stdout: rawreco.log

outputs:
  rawreco.log:
    type: stdout
  reco_RAW2DIGI_L1Reco_RECO_ALCA_USER_DQM_inAOD.root:
    type: File
    outputBinding:
       glob: "results/reco_RAW2DIGI_L1Reco_RECO_ALCA_USER_DQM_inAOD.root"

arguments:
  - prefix: -c
    valueFrom: |
      cp -r ../../code .; \
      scram b; \
      cd ../../code; \
      mkdir -p ../../../results; \
      ln -sf /cvmfs/cms-opendata-conddb.cern.ch/FT_53_LV5_AN1_RUNA FT_53_LV5_AN1 \
      ln -sf /cvmfs/cms-opendata-conddb.cern.ch/FT_53_LV5_AN1_RUNA.db FT_53_LV5_AN1_RUNA.db \
      cmsRun configFile.py
