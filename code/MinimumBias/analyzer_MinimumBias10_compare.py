import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

# initialize MessageLogger and output report
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.categories.append('Demo')
process.MessageLogger.cerr.INFO = cms.untracked.PSet(
        limit = cms.untracked.int32(-1)
        )
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True), 
				SkipEvent = cms.untracked.vstring('ProductNotFound')
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(20000) )

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/MinimumBias/AOD/Apr21ReReco-v1/0000/743D998E-0A71-E011-B962-0018F3D0963C.root',
'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/MinimumBias/AOD/Apr21ReReco-v1/0000/80E349C2-1471-E011-AA84-0018F3D09688.root',
'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/MinimumBias/AOD/Apr21ReReco-v1/0000/56C41074-2B71-E011-9473-002618943916.root',
'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/MinimumBias/AOD/Apr21ReReco-v1/0000/B0335539-0871-E011-B1BB-003048D15E2C.root',
'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/MinimumBias/AOD/Apr21ReReco-v1/0000/B871A20D-E270-E011-AC5D-003048678DD6.root',
'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/MinimumBias/AOD/Apr21ReReco-v1/0000/72A9ED57-E270-E011-BC69-003048D15DCA.root',
'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/MinimumBias/AOD/Apr21ReReco-v1/0000/94D1FEB1-4571-E011-B79D-001A92971B16.root',
'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/MinimumBias/AOD/Apr21ReReco-v1/0000/BE7300EF-2B71-E011-8206-002618943911.root'
),
        lumisToProcess = cms.untracked.VLuminosityBlockRange('146428:1-146428:65','146428:74-146428:84')
			  #firstRun = cms.untracked.uint32(169957),
        #firstEvent = cms.untracked.uint32(488034889)
)

process.demo = cms.EDAnalyzer('PhysicsObjectsHistos',
        minTracks=cms.untracked.uint32(0)
)

process.TFileService = cms.Service("TFileService",
        fileName = cms.string('histo_MinimumBias10_RAW.root')
)

process.p = cms.Path(process.demo)
