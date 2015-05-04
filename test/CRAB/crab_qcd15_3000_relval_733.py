from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'qcd15_3000'
config.General.workArea = 'crab_733'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runValidator.py'

config.section_("Data")
config.Data.inputDataset = '/RelValQCD_FlatPt_15_3000HS_13/CMSSW_7_3_3-MCRUN2_73_V11-v1/MINIAODSIM'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.ignoreLocality = True
config.Data.publication = False


config.section_("Site")
config.Site.storageSite = 'T3_US_FNALLPC'

