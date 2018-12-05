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
#'file:reco_Mu10_AOD.root'

'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Mu/AOD/Apr21ReReco-v1/0001/DC091472-0570-E011-AC36-E0CB4E29C505.root',
'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Mu/AOD/Apr21ReReco-v1/0001/94A25687-1A71-E011-999A-E0CB4E553643.root',
'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Mu/AOD/Apr21ReReco-v1/0001/74626827-0670-E011-93E5-E0CB4E1A1152.root',
'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Mu/AOD/Apr21ReReco-v1/0001/86151647-0570-E011-90A4-E0CB4E19F9A3.root',
'root://eospublic.cern.ch//eos/opendata/cms//Run2010B/Mu/AOD/Apr21ReReco-v1/0000/0EE58BCF-4570-E011-BB49-E0CB4E29C4F6.root'
                ),
  lumisToProcess = cms.untracked.VLuminosityBlockRange('146589:58-146589:150')
			    #firstRun = cms.untracked.uint32(169957),
                            #firstEvent = cms.untracked.uint32(488034889)
                            )

process.demo = cms.EDAnalyzer('PhysicsObjectsHistos',

                                         minTracks=cms.untracked.uint32(0)
                              )

process.TFileService = cms.Service("TFileService",
 #fileName = cms.string('histo_Mu10_RAW.root')
                fileName = cms.string('histo_Mu10_AOD.root')
                                   )


process.p = cms.Path(process.demo)
