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
#'file:reco_Jet10_AOD.root'

'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Jet/AOD/Apr21ReReco-v1/0003/E8DCCBFB-6571-E011-81BB-0030487D5DA5.root',
'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Jet/AOD/Apr21ReReco-v1/0003/BC94454E-6D71-E011-9D8B-0030487E4EC5.root'
                ),
  lumisToProcess = cms.untracked.VLuminosityBlockRange('146807:222-146807:311')
			    #firstRun = cms.untracked.uint32(169957),
                            #firstEvent = cms.untracked.uint32(488034889)
                            )

process.demo = cms.EDAnalyzer('PhysicsObjectsHistos',

                                         minTracks=cms.untracked.uint32(0)
                              )

process.TFileService = cms.Service("TFileService",
 #fileName = cms.string('histo_Jet10_RAW.root')
                                       fileName = cms.string('histo_Jet10_AOD.root')
                                   )


process.p = cms.Path(process.demo)
