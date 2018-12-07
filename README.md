# Validation code for reprocessing AOD from 2012 RAW samples

The objective is to compare the outputs of reprocessed AOD files for 2010-2012 RAW samples with [CMS Open Data VM](https://github.com/cernopendata/opendata.cern.ch/issues/2426) results.

The inputs of this analysis are a list of selected RAW samples. These will be part of the next release from the CMS Open Data team, also each of the RAW datasets selected have a corresponding AOD data format file available in the [CERN Open Data Portal](http://opendata.cern.ch/).

Selected 2012 RAW datasets:
- ``/MinimumBias/Run2012B-v1/RAW`` 
- ``/SingleMu/Run2012B-v1/RAW`` 
- ``/SingleElectron/Run2012B-v1/RAW``
- ``/DoubleMuParked/Run2012B-v1/RAW``
- ``/DoubleElectron/Run2012B-v1/RAW`` 
- ``/JetHT/Run2012B-v1/RAW`` 

Apart from the data reconstruction step, a simple comparison code to validate the reprocessing step on the Open Data VM is performed. Later we can compare the resulting file (newly rereconstructed from the RAW data samples) and the original AOD (available on the Open Data portal). The analyzer code loops over different physics objects (tracks, electrons, muons, photons, jets, taus and missing et) and fills histograms with P, pt, eta and phi of these objects.

The new AOD can be reprocessed from RAW with minor modifications (global tag, input file, commenting out unnecessary steps) to the configuration file.
