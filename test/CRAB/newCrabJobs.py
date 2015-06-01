from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'ZEE740_PU25s'
config.General.workArea = 'crab_740pre9'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runValidator.py'

config.section_("Data")
config.Data.inputDataset = '/RelValZEE_13/CMSSW_7_4_0-PU25ns_MCRUN2_74_V7_gensim_740pre7-v1/MINIAODSIM'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.ignoreLocality = True
config.Data.publication = False


config.section_("Site")
config.Site.storageSite = 'T3_US_FNALLPC'
