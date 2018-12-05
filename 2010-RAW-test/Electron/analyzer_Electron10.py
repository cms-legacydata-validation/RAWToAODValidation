import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

# initialize MessageLogger and output report
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.categories.append('Demo')
process.MessageLogger.cerr.INFO = cms.untracked.PSet(
        limit = cms.untracked.int32(-1)
        )
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True), 
										SkipEvent = cms.untracked.vstring('ProductNotFound')
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(20000) )

process.source = cms.Source("PoolSource",
                                # replace 'myfile.root' with the source file you want to use
                                fileNames = cms.untracked.vstring(
#'file:reco_Electron10_AOD.root'

'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Electron/AOD/Apr21ReReco-v1/0002/9C765AA1-556E-E011-BCF9-002618943854.root',
'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Electron/AOD/Apr21ReReco-v1/0002/287DC1A2-556E-E011-A3B7-0026189438E9.root'
                ),
  lumisToProcess = cms.untracked.VLuminosityBlockRange('146712:18-146712:43')
			    #firstRun = cms.untracked.uint32(169957),
                            #firstEvent = cms.untracked.uint32(488034889)
                            )

process.demo = cms.EDAnalyzer('PhysicsObjectsHistos',

                                         minTracks=cms.untracked.uint32(0)
                              )

process.TFileService = cms.Service("TFileService",
 #fileName = cms.string('histo_Electron10_RAW.root')
                                       fileName = cms.string('histo_Electron10_AOD.root')
                                   )


process.p = cms.Path(process.demo)
