# Validation code for reprocessing AOD from 2010 RAW samples

The objective is to compare the outputs of reprocessed AOD files for 2010-2012 RAW samples with [CMS Open Data VM](https://github.com/cernopendata/opendata.cern.ch/issues/2426) results.

The inputs of this analysis are a list of selected RAW samples. These will be part of the next release from the CMS Open Data team, also each of the RAW datasets selected have a corresponding AOD data format file available in the [CERN Open Data Portal](http://opendata.cern.ch/).

Selected 2010 RAW datasets:
- ``/MinimumBias/Run2010B-v1/RAW``
- ``/Mu/Run2010B-v1/RAW``
- ``/Electron/Run2010B-v1/RAW``
- ``/Jet/Run2010B-v1/RAW`` 

Apart from the data reconstruction step, a simple comparison code to validate the reprocessing step on the Open Data VM is performed. Later we can compare the resulting file (newly rereconstructed from the RAW data samples) and the original AOD (available on the Open Data portal). The analyzer code loops over different physics objects (tracks, electrons, muons, photons, jets, taus and missing et) and fills histograms with P, pt, eta and phi of these objects.

The new AOD can be reprocessed from RAW with minor modifications (global tag, input file, commenting out unnecessary steps) to the configuration file.

### Run this code in [2010 CMS Open Data VM](http://opendata.cern.ch/record/250)
```
cmsrel CMSSW_4_2_8
cd CMSSW_4_2_8/src
cmsenv
mkdir WorkDir
cd WorkDir
git clone -b 2010 git://github.com/cms-legacydata-validation/RAWToAODValidation.git
cd RAWToAODValidation

#According to the dataset
cd code/Electron
scram b
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/FT_R_42_V10A FT_R_42_V10A
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/FT_R_42_V10A.db FT_R_42_V10A.db
ls -l
ls -l /cvmfs/
cmsRun raw_Electron10.py
```

## Process for 2010 RAW samples reconstruction test

- Select input RAW sample from the [EOS HTTP Browser](https://eospublichttp01.cern.ch/eos/opendata/cms/Run2010B/). For example, your input can be **root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Electron/RAW/v1/000/146/712/185AE5B4-CAC9-DF11-9DF4-0030487CD6D2.root**

- The reconstruction will be executed in the [CMS VM image for 2010](http://opendata.cern.ch/record/250) Data for which a `CMSSW_4_2_8/src/WorkDir` area will be created.

- To create the configuration files (after `cmsenv`) run: 

   ```cmsDriver.py reco -s RAW2DIGI,L1Reco,RECO --data --conditions FT_R_42_V10A::All --eventcontent AOD --customise Configuration/GlobalRuns/reco_TLR_42X.customisePPData --no_exec --python reco_cmsdriver2010.py```

- In the default configuration file some parameters must be corrected, such as:
   1) Change maxEvents parameter (default is 1) to -1, to process all events: 
       ```process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))```
   2) Establish input from the eospublic datasets. For example:
       ```ruby
       # Input source
       process.source = cms.Source("PoolSource",
           secondaryFileNames = cms.untracked.vstring(),
           fileNames = cms.untracked.vstring('root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Electron/RAW/v1/000/146/712/185AE5B4-CAC9-DF11-9DF4-0030487CD6D2.root')
       )
       ```
   3) Correct GlobalTag according to the [Guide for Condition Data](http://opendata.cern.ch/docs/cms-guide-for-condition-database).
       ```ruby
       #Additional statements
       process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/FT_R_42_V10A.db')
       process.GlobalTag.globaltag = 'FT_R_42_V10A::All'
       ```
   4) For the 2010 RAW samples, it  is necessary to remove from the configuration file an EDProducer of the name lumiProducer. For extracting this component is required to replace a sequence, `process.localreco` and to modify a parameter set (PSet) as part of an output module, `AODoutput`. 
       
       - For editing the sequence: 
             
         Replace `process.localreco = cms.Sequence(process.trackerlocalreco+process.muonlocalreco+process.calolocalreco+process.castorreco+process.lumiProducer)` with `process.localreco = cms.Sequence(process.trackerlocalreco+process.muonlocalreco+process.calolocalreco+process.castorreco)`
        
        - For editing the OutputModule: 
           
          Change the option `keep` for `drop` in the PSet: 
           
           ```ruby
           process.AODoutput = cms.OutputModule("PoolOutputModule",
           eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
           fileName = cms.untracked.string('reco_RAW2DIGI_L1Reco_RECO_USER.root'),
           outputCommands = cms.untracked.vstring('drop *', 
           …
           'keep LumiSummary_lumiProducer_*_*’, 
           …
           )
           ```
- Proceed to do `cmsRun` to your configuration file (Run time could be up to 12 hours)

- As an output of the reconstruction, we would get a root file such as "**reco_RAW2DIGI_L1Reco_RECO_USER.root**". This file can be transfered to EOS, since it can be a large file, following these [instructions](https://cern.service-now.com/service-portal/article.do?n=KB0001998). 

- As an analyzer the [validation code to plot basic physics objects from AOD](http://opendata.cern.ch/record/464) from the CERN Open Data Portal works successfully apart from minor changes such as:
   1) Change input name as `'file:reco_RAW2DIGI_L1Reco_RECO_USER.root'` or whichever your local AOD root file is called from the output of the reconstruction.
   2) Modify luminosity range accordingly (get lumi sections and runs in your input file using `edmLumisInFile.py`). For example: 
   
        `lumisToProcess = cms.untracked.VLuminosityBlockRange('163589:1-165121:max')`
        
       Selected run ranges for each of the RAW samples were stated above.
   3) Comment out all tau related components in the `src/PhysicsObjectsHistos.cc`
   4) Remove the file `python/demoanalyzer_cfi.py` as is not needed in the process. 

- Run analyzer using `cmsRun`, and view histograms by writing in the command line `root -l` followed by the name of your analyzer's output.  

## Process to compare results with 2010 Open Data AOD files

- Search for the corresponding dataset of the RAW sample in its AOD format in [DAS](https://cmsweb.cern.ch/das/). For example, for the dataset`/Electron/Run2010B-v1/RAW` the matching one would be `/Electron/Run2010B-Apr21ReReco-v1/AOD`.

- Once the appropriate dataset is found (using [DAS](https://cmsweb.cern.ch/das/)), search for files that contain the runs specified before. 
    
    `file dataset= /Electron/Run2010B-Apr21ReReco-v1/AOD run=146712`

- Verify the luminosity of each file in the list and select those that are used in the RAW sample file (using `edmLumisInFile.py`). 

   **WARNING**: Files in the Data Aggregation System are not organized by lumis continuously therefore there’s no correlation between them. Each one must be checked for the desired run and lumi sections.

- In the analyzer code, state as input the list of files that correspond to the runs and lumi sections originally in the RAW samples. These would be open data AOD files that are already public. 

- Adjust the luminosity range, if needed, in the `lumisToProcess`.

- Run analyzer using `cmsRun`, and view histograms by writing in the command line `root -l` followed by the name of your analyzer's output.

