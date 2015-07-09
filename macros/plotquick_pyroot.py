#!/usr/bin/env python
# Ripped and adapted from http://wlav.web.cern.ch/wlav/pyroot/tpytree.html

from optparse import OptionParser
parser = OptionParser()

parser.add_option('--infile', metavar='F', type='string', action='store',
                  dest='infile',
                  default='test_qcd.root',
                  help='Input file')

parser.add_option('--algo', metavar='F', type='string', action='store',
                  default='AK4PFCHS',
                  dest='algo',
                  help='Algorithm to use. Options are AK4PFCHS, AK4PFPUPPI, AK4PFSK, and also for AK8')


parser.add_option('--sample', metavar='F', type='string', action='store',
                  default='qcd',
                  dest='sample',
                  help='Sample, only used for output root file name')
parser.add_option('--dynamic', '--db',
                  action='store_true',
                  default=False,
                  dest='dynamicBin',
                  help='Dynamic binning based on events per bin')
parser.add_option('--AbsMassResp', '--AMR',
                  action='store_false',
                  default=True,
                  dest='AMR',
                  help= ' --AMR will plot the mass response plots as m(RECO)/m(GEN) ')


(options, args) = parser.parse_args()
argv = []

if options.AMR :
    MRTitle = 'm^{RECO} - m^{GEN}'
    def MR( mreco , mgen ) :
        return( mreco - mgen )
else :
    MRTitle = 'm^{RECO}/m^{GEN}'
    def MR( mreco, mgen) :
        return( mreco/mgen )

import ROOT
import array

# open the file
tree = ROOT.TChain( options.algo + '/t' )
Evttree = ROOT.TChain( 'event/t' )
tree.Add( options.infile )
Evttree.Add( options.infile )

if '4' in options.algo :
    R = 0.4
else :
    R = 0.8
    
entries = tree.GetEntries()
# Get the jets
jets = ROOT.std.vector(ROOT.Math.LorentzVector(ROOT.Math.PtEtaPhiE4D('float')))()
genjets = ROOT.std.vector(ROOT.Math.LorentzVector(ROOT.Math.PtEtaPhiE4D('float')))()
#jets_pt = ROOT.std.vector('float')()
#jets_eta = ROOT.std.vector('float')()
#jets_phi = ROOT.std.vector('float')()
#jets_e = ROOT.std.vector('float')()
#jets_jec = ROOT.std.vector('float')()
jets_jecM = ROOT.std.vector(ROOT.std.map('string','float') )()

genjets_pt = ROOT.std.vector('float')()
genjets_eta = ROOT.std.vector('float')()
genjets_phi = ROOT.std.vector('float')()
genjets_e = ROOT.std.vector('float')()

DeltaR_gen_jet = ROOT.std.vector('float')()
genjets_Jarea = ROOT.std.vector('float')()
jets_Jarea = ROOT.std.vector('float')()
npus = ROOT.std.vector('float')()
tnpus = ROOT.std.vector('float')()


#nref = ROOT.std.vector('float')()#array.array('I', [0])
#refrank = ROOT.std.vector('float')() # array.array('I', [0])

lumi = array.array('I', [0])
npv = array.array('I',[0])

# Turn off all branches but the ones we want

tree.SetBranchAddress('p4',jets)
#tree.SetBranchAddress('jtpt', jets_pt)
#tree.SetBranchAddress('jteta', jets_eta)
#tree.SetBranchAddress('jtphi', jets_phi)
#tree.SetBranchAddress('jte', jets_e)
#tree.SetBranchAddress('jtjec', jets_jec)
tree.SetBranchAddress('jec_factors', jets_jecM)
tree.SetBranchAddress('gen_p4',genjets)
#tree.SetBranchAddress('refpt', genjets_pt)
#tree.SetBranchAddress('refeta', genjets_eta)
#tree.SetBranchAddress('refphi', genjets_phi)
#tree.SetBranchAddress('refe', genjets_e)
Evttree.SetBranchAddress('npv', npv)
Evttree.SetBranchAddress('lumi',lumi)
tree.SetBranchAddress('refdrjt',DeltaR_gen_jet)
tree.SetBranchAddress('refarea',genjets_Jarea)
tree.SetBranchAddress('jtarea',jets_Jarea)
Evttree.SetBranchAddress('npus',npus)
Evttree.SetBranchAddress('tnpus',tnpus)
#tree.SetBranchAddress('nref',nref)
#tree.SetBranchAddress('refrank',refrank)


# get a file to write hists to
f = ROOT.TFile("outplots_" + options.sample + "_" + options.algo + ".root", "RECREATE")
BinInfoFileName = "BinInfo_" + options.sample + "_" + options.algo + ".txt"


#f.mkdir("Barrel")
#f.mkdir("Endcap")
#f.mkdir("Forward")
#`f.mkdir("PreForward")
EtaRegions = [ "Barrel", "Endcap", "PreForward", "Forward" ]

for EtaReg in xrange(len(EtaRegions)) :
    f.mkdir(EtaRegions[EtaReg])
#0-1.479, 1.5-2.5, 2.5-3.0, 3.0-10.0


#Initialize histogram arrays

h_pt0 = [None]*len(EtaRegions)

h_pt_ptresponse0 = [None]*len(EtaRegions)
h_eta_ptresponse0 = [None]*len(EtaRegions)

h_pt_aptresponse0 = [None]*len(EtaRegions)
h_eta_aptresponse0 = [None]*len(EtaRegions)

h_m0 = [None]*len(EtaRegions)
h_m_mresponse0 = [None]*len(EtaRegions)
h_pt_mresponse0 = [None]*len(EtaRegions)
h_eta_mresponse0 = [None]*len(EtaRegions)
    
h_rho0 = [None]*len(EtaRegions)
h_rho_rhoresponse0 = [None]*len(EtaRegions)


h_eta_ptresponse_ptb = [None]*len(EtaRegions)
h_eta_ptresponse_ptb2 = [None]*len(EtaRegions)
h_eta_ptresponse_ptb3 = [None]*len(EtaRegions)
h_eta_ptresponse_ptb4 = [None]*len(EtaRegions)
h_eta_ptresponse_aptb = [None]*len(EtaRegions)
h_eta_ptresponse_aptb2 = [None]*len(EtaRegions)
h_eta_ptresponse_aptb3 = [None]*len(EtaRegions)
h_eta_ptresponse_aptb4 = [None]*len(EtaRegions)
h_eta_ptresponse_npvb = [None]*len(EtaRegions)
h_eta_ptresponse_npvb2 = [None]*len(EtaRegions)
h_eta_ptresponse_npvb3 = [None]*len(EtaRegions)
h_eta_ptresponse_npvb4 = [None]*len(EtaRegions)
h_eta_ptresponse_anpvb = [None]*len(EtaRegions)
h_eta_ptresponse_anpvb2 = [None]*len(EtaRegions)
h_eta_ptresponse_anpvb3 = [None]*len(EtaRegions)
h_eta_ptresponse_anpvb4 = [None]*len(EtaRegions)
    
h_eta_ptresponses = [None]*len(EtaRegions) 

h_eta_mresponse_ptb = [None]*len(EtaRegions)
h_eta_mresponse_ptb2 = [None]*len(EtaRegions)
h_eta_mresponse_ptb3 = [None]*len(EtaRegions)
h_eta_mresponse_ptb4 = [None]*len(EtaRegions)
h_eta_mresponse_npvb = [None]*len(EtaRegions)
h_eta_mresponse_npvb2 = [None]*len(EtaRegions)
h_eta_mresponse_npvb3 = [None]*len(EtaRegions)
h_eta_mresponse_npvb4 = [None]*len(EtaRegions)

h_eta_mresponses = [None]*len(EtaRegions) 
    
h_pt_ptresponse_npvb = [None]*len(EtaRegions) 
h_pt_ptresponse_npvb2 = [None]*len(EtaRegions)
h_pt_ptresponse_npvb3 = [None]*len(EtaRegions)
h_pt_ptresponse_npvb4 = [None]*len(EtaRegions)
h_pt_ptresponse_anpvb = [None]*len(EtaRegions)
h_pt_ptresponse_anpvb2 = [None]*len(EtaRegions)
h_pt_ptresponse_anpvb3 = [None]*len(EtaRegions)
h_pt_ptresponse_anpvb4 = [None]*len(EtaRegions)

h_pt_ptresponses = [None]*len(EtaRegions)
    
h_m_ptresponse_npvb = [None]*len(EtaRegions)  
h_m_ptresponse_npvb2 = [None]*len(EtaRegions) 
h_m_ptresponse_npvb3 = [None]*len(EtaRegions) 
h_m_ptresponse_npvb4 = [None]*len(EtaRegions) 
h_m_ptresponse_anpvb = [None]*len(EtaRegions)
h_m_ptresponse_anpvb2 = [None]*len(EtaRegions)
h_m_ptresponse_anpvb3 = [None]*len(EtaRegions)
h_m_ptresponse_anpvb4 = [None]*len(EtaRegions)
h_m_ptresponse_ptb = [None]*len(EtaRegions)  
h_m_ptresponse_ptb2 = [None]*len(EtaRegions) 
h_m_ptresponse_ptb3 = [None]*len(EtaRegions) 
h_m_ptresponse_ptb4 = [None]*len(EtaRegions) 
h_m_ptresponse_aptb = [None]*len(EtaRegions)  
h_m_ptresponse_aptb2 = [None]*len(EtaRegions) 
h_m_ptresponse_aptb3 = [None]*len(EtaRegions) 
h_m_ptresponse_aptb4 = [None]*len(EtaRegions) 

h_m_ptresponses = [None]*len(EtaRegions)
    
h_m_mresponse_npvb = [None]*len(EtaRegions)  
h_m_mresponse_npvb2 = [None]*len(EtaRegions) 
h_m_mresponse_npvb3 = [None]*len(EtaRegions) 
h_m_mresponse_npvb4 = [None]*len(EtaRegions) 
h_m_mresponse_ptb = [None]*len(EtaRegions)  
h_m_mresponse_ptb2 = [None]*len(EtaRegions) 
h_m_mresponse_ptb3 = [None]*len(EtaRegions) 
h_m_mresponse_ptb4 = [None]*len(EtaRegions) 
    
h_m_mresponses = [None]*len(EtaRegions) 
    
h_pt_mresponse_npvb = [None]*len(EtaRegions)  
h_pt_mresponse_npvb2 = [None]*len(EtaRegions) 
h_pt_mresponse_npvb3 = [None]*len(EtaRegions) 
h_pt_mresponse_npvb4 = [None]*len(EtaRegions) 

h_pt_mresponses = [None]*len(EtaRegions)

#1D General Plots

h_jetpt = [None]*len(EtaRegions)
h_jeteta = [None]*len(EtaRegions)
h_jetphi = [None]*len(EtaRegions)
h_jetE = [None]*len(EtaRegions)
h_jetArea = [None]*len(EtaRegions)
h_genjetpt = [None]*len(EtaRegions)
h_genjeteta = [None]*len(EtaRegions)
h_genjetphi = [None]*len(EtaRegions)
h_genjetE = [None]*len(EtaRegions)
h_genjetArea = [None]*len(EtaRegions)
h_NPV = [None]*len(EtaRegions)
h_LUMI = [None]*len(EtaRegions)
h_DeltaR_gen_jet = [None]*len(EtaRegions)
h_npus = [None]*len(EtaRegions)
h_tnpus = [None]*len(EtaRegions)
#h_nref = [None]*len(EtaRegions)
#h_refrank = [None]*len(EtaRegions)

#2D Comparison Plots

h_jetptvsNPV = [None]*len(EtaRegions)
h_jetetavsNPV = [None]*len(EtaRegions)
h_jetAreavsNPV = [None]*len(EtaRegions)
h_NPV_ptresponse = [None]*len(EtaRegions)
h_NPV_aptresponse = [None]*len(EtaRegions)
h_NPV_mresponse = [None]*len(EtaRegions)
      

h_NPV_ptresponse_aptb   = [None]*len(EtaRegions)
h_NPV_ptresponse_aptb2  = [None]*len(EtaRegions)
h_NPV_ptresponse_aptb3  = [None]*len(EtaRegions)
h_NPV_ptresponse_aptb4  = [None]*len(EtaRegions)

h_NPV_mresponse_ptb   = [None]*len(EtaRegions)
h_NPV_mresponse_ptb2  = [None]*len(EtaRegions)
h_NPV_mresponse_ptb3  = [None]*len(EtaRegions)
h_NPV_mresponse_ptb4  = [None]*len(EtaRegions)

h_NPV_mresponses = [None]*len(EtaRegions)

h_NPV_ptresponses = [None]*len(EtaRegions)

for EtaReg in xrange( len(EtaRegions) ) :
    f.cd(EtaRegions[EtaReg])

    # Make histograms
    h_pt0[EtaReg] = ROOT.TH1F("h_pt0", "Leading Jet p_{T};p_{T} (GeV);Number", 300, 0, 3000)
    h_pt_ptresponse0[EtaReg] = ROOT.TH2F('h_pt_ptresponse0', 'p_{T}^{RECO} / p_{T}^{GEN};p_{T}^{GEN}', 150, 0, 500, 25, 0, 2.5 )
    h_eta_ptresponse0[EtaReg] = ROOT.TH2F('h_eta_ptresponse0', 'p_{T}^{RECO} / p_{T}^{GEN};#eta^{GEN}', 50, -5.0, 5.0, 25, 0, 2.5 )

    h_pt_aptresponse0[EtaReg] = ROOT.TH2F('h_pt_aptresponse0', '(p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN};p_{T}^{GEN}', 150, 0, 500, 25, -1.0, 1.0 )
    h_eta_aptresponse0[EtaReg] = ROOT.TH2F('h_eta_aptresponse0', '(p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN};#eta^{GEN}', 50, -5.0, 5.0, 25, -1.0, 1.0 )

    h_m0[EtaReg] = ROOT.TH1F("h_m0", "Leading Jet m;m (GeV);Number", 250, 0, 500)
    h_m_mresponse0[EtaReg] = ROOT.TH2F('h_m_mresponse0', MRTitle + ';m^{GEN}', 25, 0, 250, 25, -50, 50 )
    h_pt_mresponse0[EtaReg] = ROOT.TH2F('h_pt_mresponse0', MRTitle + ';p_{T}^{GEN}', 50, 0, 500, 25, -50, 50 )
    h_eta_mresponse0[EtaReg] = ROOT.TH2F('h_eta_mresponse0', MRTitle + ';#eta^{GEN}', 50, -5.0, 5.0, 25, -50, 50 )
    
    h_rho0[EtaReg] = ROOT.TH1F("h_rho0", "Leading Jet #left(#frac{m}{p_{T}R}#right)^{2};#rho;Number", 250, 0, 1.0)
    h_rho_rhoresponse0[EtaReg] = ROOT.TH2F("h_rho_rhoresponse0", "Leading Jet #left(#frac{m}{p_{T}R}#right)^{2} Response;#rho_{GEN};#rho_{RECO}/#rho{GEN}", 50, 0, 1, 25, 0, 2.5)    

    #Lots of plots
    h_eta_ptresponse_ptb[EtaReg]     = ROOT.TH2F('h_eta_ptresponse_ptb',    ';|#eta^{GEN}|;p_{T}^{RECO} / p_{T}^{GEN}', 50, 0.0, 5.0, 25, 0, 2.5 )
    h_eta_ptresponse_ptb2[EtaReg]    = ROOT.TH2F('h_eta_ptresponse_ptb2',   ';|#eta^{GEN}|;p_{T}^{RECO} / p_{T}^{GEN}', 50, 0.0, 5.0, 25, 0, 2.5 )
    h_eta_ptresponse_ptb3[EtaReg]    = ROOT.TH2F('h_eta_ptresponse_ptb3',  ';|#eta^{GEN}|;p_{T}^{RECO} / p_{T}^{GEN}', 50, 0.0, 5.0, 25, 0, 2.5 )
    h_eta_ptresponse_ptb4[EtaReg]    = ROOT.TH2F('h_eta_ptresponse_ptb4', ';|#eta^{GEN}|;p_{T}^{RECO} / p_{T}^{GEN}', 50, 0.0, 5.0, 25, 0, 2.5 )
    h_eta_ptresponse_aptb[EtaReg]    = ROOT.TH2F('h_eta_ptresponse_aptb',    ';|#eta^{GEN}|;(p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}', 50, 0.0, 5.0, 25, -1.0, 1.0 )
    h_eta_ptresponse_aptb2[EtaReg]   = ROOT.TH2F('h_eta_ptresponse_aptb2',   ';|#eta^{GEN}|;(p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}', 50, 0.0, 5.0, 25, -1.0, 1.0 )
    h_eta_ptresponse_aptb3[EtaReg]   = ROOT.TH2F('h_eta_ptresponse_aptb3',  ';|#eta^{GEN}|;(p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}', 50, 0.0, 5.0, 25, -1.0, 1.0 )
    h_eta_ptresponse_aptb4[EtaReg]   = ROOT.TH2F('h_eta_ptresponse_aptb4', ';|#eta^{GEN}|;(p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}', 50, 0.0, 5.0, 25, -1.0, 1.0 )
    h_eta_ptresponse_npvb[EtaReg]    = ROOT.TH2F('h_eta_ptresponse_npvb',   ';|#eta^{GEN}|;p_{T}^{RECO} / p_{T}^{GEN}', 25, 0.0, 5.0, 25, 0, 2.5 )
    h_eta_ptresponse_npvb2[EtaReg]   = ROOT.TH2F('h_eta_ptresponse_npvb2',  ';;|#eta^{GEN}|;p_{T}^{RECO} / p_{T}^{GEN}', 25, 0.0, 5.0, 25, 0, 2.5 )
    h_eta_ptresponse_npvb3[EtaReg]   = ROOT.TH2F('h_eta_ptresponse_npvb3', ';|#eta^{GEN}|;p_{T}^{RECO} / p_{T}^{GEN}', 25, 0.0, 5.0, 25, 0, 2.5 )
    h_eta_ptresponse_npvb4[EtaReg]   = ROOT.TH2F('h_eta_ptresponse_npvb4', ';|#eta^{GEN}|;p_{T}^{RECO} / p_{T}^{GEN}', 25, 0.0, 5.0, 25, 0, 2.5 )
    h_eta_ptresponse_anpvb[EtaReg]   = ROOT.TH2F('h_eta_ptresponse_anpvb',   ';|#eta^{GEN}|;(p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}', 25, 0.0, 5.0, 25, -1.0, 1.0 )
    h_eta_ptresponse_anpvb2[EtaReg]  = ROOT.TH2F('h_eta_ptresponse_anpvb2',  ';;|#eta^{GEN}|;(p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}', 25, 0.0, 5.0, 25, -1.0, 1.0 )
    h_eta_ptresponse_anpvb3[EtaReg]  = ROOT.TH2F('h_eta_ptresponse_anpvb3', ';|#eta^{GEN}|;(p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}', 25, 0.0, 5.0, 25, -1.0, 1.0 )
    h_eta_ptresponse_anpvb4[EtaReg]  = ROOT.TH2F('h_eta_ptresponse_anpvb4', ';|#eta^{GEN}|;(p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}', 25, 0.0, 5.0, 25, -1.0, 1.0 )
    
    h_eta_ptresponses[EtaReg] = [
        h_eta_ptresponse_ptb[EtaReg],
        h_eta_ptresponse_ptb2[EtaReg],
        h_eta_ptresponse_ptb3[EtaReg],
        h_eta_ptresponse_ptb4[EtaReg],
        h_eta_ptresponse_aptb[EtaReg],
        h_eta_ptresponse_aptb2[EtaReg],
        h_eta_ptresponse_aptb3[EtaReg],
        h_eta_ptresponse_aptb4[EtaReg],
        h_eta_ptresponse_npvb[EtaReg],
        h_eta_ptresponse_npvb2[EtaReg],
        h_eta_ptresponse_npvb3[EtaReg],
        h_eta_ptresponse_npvb4[EtaReg],
        h_eta_ptresponse_anpvb[EtaReg],
        h_eta_ptresponse_anpvb2[EtaReg],
        h_eta_ptresponse_anpvb3[EtaReg],
        h_eta_ptresponse_anpvb4[EtaReg]
    ]

    h_eta_mresponse_ptb[EtaReg]  = ROOT.TH2F('h_eta_mresponse_ptb',    ';|#eta^{GEN}|;' + MRTitle, 25, 0.0, 5.0, 25, -25, 25 )
    h_eta_mresponse_ptb2[EtaReg] = ROOT.TH2F('h_eta_mresponse_ptb2',   ';|#eta^{GEN}|;' + MRTitle, 25, 0.0, 5.0, 25, -25, 25 )
    h_eta_mresponse_ptb3[EtaReg] = ROOT.TH2F('h_eta_mresponse_ptb3',  ';|#eta^{GEN}|;' + MRTitle, 25, 0.0, 5.0, 25, -25, 25 )
    h_eta_mresponse_ptb4[EtaReg] = ROOT.TH2F('h_eta_mresponse_ptb4', ';|#eta^{GEN}|;' + MRTitle, 25, 0.0, 5.0, 25, -25, 25 )
    h_eta_mresponse_npvb[EtaReg]  = ROOT.TH2F('h_eta_mresponse_npvb',   ';|#eta^{GEN}|;' + MRTitle, 25, 0.0, 5.0, 25, -25, 25 )
    h_eta_mresponse_npvb2[EtaReg] = ROOT.TH2F('h_eta_mresponse_npvb2',  ';|#eta^{GEN}|;' + MRTitle, 25, 0.0, 5.0, 25, -25, 25 )
    h_eta_mresponse_npvb3[EtaReg] = ROOT.TH2F('h_eta_mresponse_npvb3', ';|#eta^{GEN}|;' + MRTitle, 25, 0.0, 5.0, 25, -25, 25 )
    h_eta_mresponse_npvb4[EtaReg] = ROOT.TH2F('h_eta_mresponse_npvb4', ';|#eta^{GEN}|;' + MRTitle, 25, 0.0, 5.0, 25, -25, 25 )

    h_eta_mresponses[EtaReg] = [
        h_eta_mresponse_ptb[EtaReg],
        h_eta_mresponse_ptb2[EtaReg],
        h_eta_mresponse_ptb3[EtaReg],
        h_eta_mresponse_ptb4[EtaReg],
        h_eta_mresponse_npvb[EtaReg],
        h_eta_mresponse_npvb2[EtaReg],
        h_eta_mresponse_npvb3[EtaReg],
        h_eta_mresponse_npvb4[EtaReg]
    ]
    
    h_pt_ptresponse_npvb[EtaReg]  = ROOT.TH2F('h_pt_ptresponse_npvb', ';p_{T}^{GEN};p_{T}^{RECO} / p_{T}^{GEN}', 50, 0, 500, 25, 0, 2.5 )
    h_pt_ptresponse_npvb2[EtaReg] = ROOT.TH2F('h_pt_ptresponse_npvb2', ';p_{T}^{GEN};p_{T}^{RECO} / p_{T}^{GEN}', 50, 0, 500, 25, 0, 2.5 )
    h_pt_ptresponse_npvb3[EtaReg] = ROOT.TH2F('h_pt_ptresponse_npvb3', ';p_{T}^{GEN};p_{T}^{RECO} / p_{T}^{GEN}', 50, 0, 500, 25, 0, 2.5 )
    h_pt_ptresponse_npvb4[EtaReg] = ROOT.TH2F('h_pt_ptresponse_npvb4', ';p_{T}^{GEN};p_{T}^{RECO} / p_{T}^{GEN}', 50, 0, 500, 25, 0, 2.5 )
    h_pt_ptresponse_anpvb[EtaReg]  = ROOT.TH2F('h_pt_ptresponse_anpvb', ';p_{T}^{GEN};(p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}', 50, 0, 500, 25, -1.0, 1.0 )
    h_pt_ptresponse_anpvb2[EtaReg] = ROOT.TH2F('h_pt_ptresponse_anpvb2', ';p_{T}^{GEN};(p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}', 50, 0, 500, 25, -1.0, 1.0 )
    h_pt_ptresponse_anpvb3[EtaReg] = ROOT.TH2F('h_pt_ptresponse_anpvb3', ';p_{T}^{GEN};(p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}', 50, 0, 500, 25, -1.0, 1.0 )
    h_pt_ptresponse_anpvb4[EtaReg] = ROOT.TH2F('h_pt_ptresponse_anpvb4', ';p_{T}^{GEN};(p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}', 50, 0, 500, 25, -1.0, 1.0 )
    
    h_pt_ptresponses[EtaReg] = [
        h_pt_ptresponse_npvb[EtaReg],
        h_pt_ptresponse_npvb2[EtaReg],
        h_pt_ptresponse_npvb3[EtaReg],
        h_pt_ptresponse_npvb4[EtaReg],
        h_pt_ptresponse_anpvb[EtaReg],
        h_pt_ptresponse_anpvb2[EtaReg],
        h_pt_ptresponse_anpvb3[EtaReg],
        h_pt_ptresponse_anpvb4[EtaReg]
    ]
    
    h_m_ptresponse_npvb[EtaReg]  = ROOT.TH2F('h_m_ptresponse_npvb', ';m^{GEN};p_{T}^{RECO} / p_{T}^{GEN}', 50, 0, 250, 25, 0, 2.5 )
    h_m_ptresponse_npvb2[EtaReg] = ROOT.TH2F('h_m_ptresponse_npvb2', ';m^{GEN};p_{T}^{RECO} / p_{T}^{GEN}', 50, 0, 250, 25, 0, 2.5 )
    h_m_ptresponse_npvb3[EtaReg] = ROOT.TH2F('h_m_ptresponse_npvb3', ';m^{GEN};p_{T}^{RECO} / p_{T}^{GEN}', 50, 0, 250, 25, 0, 2.5 )
    h_m_ptresponse_npvb4[EtaReg] = ROOT.TH2F('h_m_ptresponse_npvb4', ';m^{GEN};p_{T}^{RECO} / p_{T}^{GEN}', 50, 0, 250, 25, 0, 2.5 )
    h_m_ptresponse_anpvb[EtaReg]  = ROOT.TH2F('h_m_ptresponse_anpvb', ';m^{GEN};(p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}', 50, 0, 250, 25, -1.0, 1.0 )
    h_m_ptresponse_anpvb2[EtaReg] = ROOT.TH2F('h_m_ptresponse_anpvb2', ';m^{GEN};(p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}', 50, 0, 250, 25, -1.0, 1.0 )
    h_m_ptresponse_anpvb3[EtaReg] = ROOT.TH2F('h_m_ptresponse_anpvb3', ';m^{GEN};(p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}', 50, 0, 250, 25, -1.0, 1.0 )
    h_m_ptresponse_anpvb4[EtaReg] = ROOT.TH2F('h_m_ptresponse_anpvb4', ';m^{GEN};(p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}', 50, 0, 250, 25, -1.0, 1.0 )
    h_m_ptresponse_ptb[EtaReg]  = ROOT.TH2F('h_m_ptresponse_ptb', ';m^{GEN};p_{T}^{RECO} / p_{T}^{GEN}', 50, 0, 250, 25, 0, 2.5 )
    h_m_ptresponse_ptb2[EtaReg] = ROOT.TH2F('h_m_ptresponse_ptb2', ';m^{GEN};p_{T}^{RECO} / p_{T}^{GEN}', 50, 0, 250, 25, 0, 2.5 )
    h_m_ptresponse_ptb3[EtaReg] = ROOT.TH2F('h_m_ptresponse_ptb3', ';m^{GEN};p_{T}^{RECO} / p_{T}^{GEN}', 50, 0, 250, 25, 0, 2.5 )
    h_m_ptresponse_ptb4[EtaReg] = ROOT.TH2F('h_m_ptresponse_ptb4', ';m^{GEN};p_{T}^{RECO} / p_{T}^{GEN}', 50, 0, 250, 25, 0, 2.5 )
    h_m_ptresponse_aptb[EtaReg]  = ROOT.TH2F('h_m_ptresponse_aptb', ';m^{GEN};(p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}', 50, 0, 250, 25, -1.0, 1.0 )
    h_m_ptresponse_aptb2[EtaReg] = ROOT.TH2F('h_m_ptresponse_aptb2', ';m^{GEN};(p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}', 50, 0, 250, 25, -1.0, 1.0 )
    h_m_ptresponse_aptb3[EtaReg] = ROOT.TH2F('h_m_ptresponse_aptb3', ';m^{GEN};(p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}', 50, 0, 250, 25, -1.0, 1.0 )
    h_m_ptresponse_aptb4[EtaReg] = ROOT.TH2F('h_m_ptresponse_aptb4', ';m^{GEN};(p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}', 50, 0, 250, 25, -1.0, 1.0 )

    h_m_ptresponses[EtaReg] = [
        h_m_ptresponse_ptb[EtaReg],
        h_m_ptresponse_ptb2[EtaReg],
        h_m_ptresponse_ptb3[EtaReg],
        h_m_ptresponse_ptb4[EtaReg],
        h_m_ptresponse_aptb[EtaReg],
        h_m_ptresponse_aptb2[EtaReg],
        h_m_ptresponse_aptb3[EtaReg],
        h_m_ptresponse_aptb4[EtaReg], 
        h_m_ptresponse_npvb[EtaReg],
        h_m_ptresponse_npvb2[EtaReg],
        h_m_ptresponse_npvb3[EtaReg],
        h_m_ptresponse_npvb4[EtaReg],
        h_m_ptresponse_anpvb[EtaReg],
        h_m_ptresponse_anpvb2[EtaReg],
        h_m_ptresponse_anpvb3[EtaReg],
        h_m_ptresponse_anpvb4[EtaReg]
    ]

    h_NPV_ptresponse_aptb[EtaReg]  = ROOT.TH2F('h_NPV_ptresponse_aptb', ';NPV;(p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}', 25, 0, 50, 25, -1.0, 1.0 )
    h_NPV_ptresponse_aptb2[EtaReg] = ROOT.TH2F('h_NPV_ptresponse_aptb2', ';NPV;(p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}', 25, 0, 50, 25, -1.0, 1.0 )
    h_NPV_ptresponse_aptb3[EtaReg] = ROOT.TH2F('h_NPV_ptresponse_aptb3', ';NPV;(p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}', 25, 0, 50, 25, -1.0, 1.0 )
    h_NPV_ptresponse_aptb4[EtaReg] = ROOT.TH2F('h_NPV_ptresponse_aptb4', ';NPV;(p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}', 25, 0, 50, 25, -1.0, 1.0 )

    h_NPV_ptresponses[EtaReg] = [
        h_NPV_ptresponse_aptb[EtaReg],
        h_NPV_ptresponse_aptb2[EtaReg],
        h_NPV_ptresponse_aptb3[EtaReg],
        h_NPV_ptresponse_aptb4[EtaReg]
    ]


    h_NPV_mresponse_ptb[EtaReg]  = ROOT.TH2F('h_NPV_mresponse_ptb', ';NPV;(p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}', 25, 0, 50, 25, -25, 25 )
    h_NPV_mresponse_ptb2[EtaReg] = ROOT.TH2F('h_NPV_mresponse_ptb2', ';NPV;(p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}', 25, 0, 50, 25, -25, 25 )
    h_NPV_mresponse_ptb3[EtaReg] = ROOT.TH2F('h_NPV_mresponse_ptb3', ';NPV;(p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}', 25, 0, 50, 25, -25, 25 )
    h_NPV_mresponse_ptb4[EtaReg] = ROOT.TH2F('h_NPV_mresponse_ptb4', ';NPV;(p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}', 25, 0, 50, 25, -25, 25 )

    h_NPV_mresponses[EtaReg] = [
        h_NPV_mresponse_ptb[EtaReg],
        h_NPV_mresponse_ptb2[EtaReg],
        h_NPV_mresponse_ptb3[EtaReg],
        h_NPV_mresponse_ptb4[EtaReg]
    ]
    
    h_m_mresponse_npvb[EtaReg]  = ROOT.TH2F('h_m_mresponse_npvb', ';m^{GEN};' + MRTitle, 50, 0, 250, 25, -25, 25 )
    h_m_mresponse_npvb2[EtaReg] = ROOT.TH2F('h_m_mresponse_npvb2', ';m^{GEN};' + MRTitle, 50, 0, 250, 25, -25, 25 )
    h_m_mresponse_npvb3[EtaReg] = ROOT.TH2F('h_m_mresponse_npvb3', ';m^{GEN};' + MRTitle, 50, 0, 250, 25, -25, 25 )
    h_m_mresponse_npvb4[EtaReg] = ROOT.TH2F('h_m_mresponse_npvb4', ';m^{GEN};' + MRTitle, 50, 0, 250, 25, -25, 25 )
    h_m_mresponse_ptb[EtaReg]  = ROOT.TH2F('h_m_mresponse_ptb', ';m^{GEN};' + MRTitle, 50, 0, 250, 25, -25, 25 )
    h_m_mresponse_ptb2[EtaReg] = ROOT.TH2F('h_m_mresponse_ptb2', ';m^{GEN};' + MRTitle, 50, 0, 250, 25, -25, 25 )
    h_m_mresponse_ptb3[EtaReg] = ROOT.TH2F('h_m_mresponse_ptb3', ';m^{GEN};' + MRTitle, 50, 0, 250, 25, -25, 25 )
    h_m_mresponse_ptb4[EtaReg] = ROOT.TH2F('h_m_mresponse_ptb4', ';m^{GEN};' + MRTitle, 50, 0, 250, 25, -25, 25 )
    
    h_m_mresponses[EtaReg] = [
        h_m_mresponse_ptb[EtaReg],
        h_m_mresponse_ptb2[EtaReg],
        h_m_mresponse_ptb3[EtaReg],
        h_m_mresponse_ptb4[EtaReg],
        h_m_mresponse_npvb[EtaReg],
        h_m_mresponse_npvb2[EtaReg],
        h_m_mresponse_npvb3[EtaReg],
        h_m_mresponse_npvb4[EtaReg]
    ]
    
    h_pt_mresponse_npvb[EtaReg]  = ROOT.TH2F('h_pt_mresponse_npvb', ';p_{T}^{GEN};' + MRTitle, 50, 0, 500, 25, -25, 25 )
    h_pt_mresponse_npvb2[EtaReg] = ROOT.TH2F('h_pt_mresponse_npvb2', ';p_{T}^{GEN};' + MRTitle, 50, 0, 500, 25, -25, 25 )
    h_pt_mresponse_npvb3[EtaReg] = ROOT.TH2F('h_pt_mresponse_npvb3', ';p_{T}^{GEN};' + MRTitle, 50, 0, 500, 25, -25, 25 )
    h_pt_mresponse_npvb4[EtaReg] = ROOT.TH2F('h_pt_mresponse_npvb4', ';p_{T}^{GEN};' + MRTitle, 50, 0, 500, 25, -25, 25 )

    h_pt_mresponses[EtaReg] = [
        h_pt_mresponse_npvb[EtaReg],
        h_pt_mresponse_npvb2[EtaReg],
        h_pt_mresponse_npvb3[EtaReg],
        h_pt_mresponse_npvb4[EtaReg]
    ]

    #1D General Plots

    h_jetpt[EtaReg]  = ROOT.TH1F('h_jetpt', ';jet p_{T}^{RECO}', 50, 0, 500 )
    h_jeteta[EtaReg]  = ROOT.TH1F('h_jeteta', ';jet eta', 50, -5.0, 5.0 ) 
    h_jetphi[EtaReg]  = ROOT.TH1F('h_jetphi', ';jet phi', 50, -3.14, 3.14 )
    h_jetE[EtaReg]  = ROOT.TH1F('h_jetE', ';jet Energy(GeV)', 50, 0, 500) 
    h_jetArea[EtaReg]  = ROOT.TH1F('h_jetArea', ';jet Area', 50, 0, 5.0 ) 
    h_genjetpt[EtaReg]  = ROOT.TH1F('h_genjetpt', ';jet p_{T}^{GEN}', 50, 0, 500 ) 
    h_genjeteta[EtaReg]  = ROOT.TH1F('h_genjeteta', ';genjet eta' , 50, -5.0, 5.0 ) 
    h_genjetphi[EtaReg]  = ROOT.TH1F('h_genjetphi', ';genjet phi;', 50, -3.14, 3.14 ) 
    h_genjetE[EtaReg]  = ROOT.TH1F('h_genjetE', ';gen jet Energy(GeV)', 50, 0, 500 ) 
    h_genjetArea[EtaReg]  = ROOT.TH1F('h_genjetArea', ';gen Jet Area', 50, 0, 5.0 ) 
    h_NPV[EtaReg]  = ROOT.TH1F('h_NPV', ';NPV', 50, 0, 50) 
    h_LUMI[EtaReg]  = ROOT.TH1F('h_LUMI', ';LUMI', 50, 0, 100000) 
    h_DeltaR_gen_jet[EtaReg]  = ROOT.TH1F('h_DeltaR_gen_jet', ';{Delta}R', 50, 0, 0.5)
    h_npus[EtaReg]  = ROOT.TH1F('h_npus', ';npus', 50, 0, 100 ) 
    h_tnpus[EtaReg]  = ROOT.TH1F('h_tnpus', ';tnpus', 50, 0, 100) 
    #h_nref[EtaReg]  = ROOT.TH1F('h_nref', ';nref', 50, 0, 50 ) 
    #h_refrank[EtaReg]  = ROOT.TH1F('h_refrank', ';refrank', 50, 0, 50) 
    
    #2D Comparison Plots
    
    h_jetptvsNPV[EtaReg]  = ROOT.TH2F('h_jetptvsNPV', ';p_{T}^{RECO};NPV', 50, 0, 500, 25, 0, 50 ) 
    h_jetetavsNPV[EtaReg]  = ROOT.TH2F('h_jetetavsNPV', ';jet eta;NPV', 50, -5.0, 5.0, 25, 0, 50 ) 
    h_jetAreavsNPV[EtaReg]  = ROOT.TH2F('h_jetAreavsNPV', ';jet Area;NPV', 50, 0, 1.0, 25, 0, 50 )

    h_NPV_ptresponse[EtaReg] = ROOT.TH2F('h_NPV_ptresponse', ';Number of Primary Vertices;p_{T}^{RECO}/p_{T}^{GEN}', 25, 0, 50, 25, 0, 2.5)
    h_NPV_aptresponse[EtaReg] = ROOT.TH2F('h_NPV_aptresponse',';Number of Primary Vertices;(p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',25, 0, 50, 25, -1.0, 1.0)
    h_NPV_mresponse[EtaReg] = ROOT.TH2F('h_NPV_mresponse',';Number of Primary Vertices;' + MRTitle,25, 0, 50, 25, -100, 100)

    
    f.cd()
    
def getptbin(x) :
    ptbins = [
        10., 30., 100., 400., 2000.
        ]
    if x < 10. :
        return None
    for i in xrange( len(ptbins) - 1 ) :
        if x >= ptbins[i] and x < ptbins[i+1] :
            return i
    return len(ptbins) - 2

def getNPVbin(x) :
    NPVbins = [
        10, 20, 30, 40
        ]
    if x < 10 :
        return None
    for i in xrange( len(NPVbins) - 1 ) :
        if x >= NPVbins[i] and x < NPVbins[i+1] :
            return i
    return len(NPVbins) - 2

NPVs = []
PTs = []
NPVsB = []
PTsB = []
NPVsF = []
PTsF = []
NPVsP = []
PTsP = []
nparts = 4
npartspt = 4
if options.dynamicBin :
    print 'Generating Bins'
    for jentry in xrange ( entries ) :
        if 100*jentry%entries == 0 :
            print str(100*jentry/entries) + '% complete'
        nc = tree.GetEntry( jentry )
        ne = Evttree.GetEntry( jentry )

        if nc <= 0 or ne <= 0 :
            continue

        if genjets.size() > 0 :
            
            if abs( genjets[0].Eta() ) < 1.479 :

                if genjets[0].Pt() > 25. :#geneJets[0].Perp() > 20. :

                    NPVsB.append(npv[0])
                    PTsB.append(genjets[0].Pt())#geneJets[0].Perp())
            elif abs( genjets[0].Eta() ) < 2.5 :

                if genjets[0].Pt() > 25. :#geneJets[0].Perp() > 20. :
                    NPVs.append(npv[0])

                    PTs.append(genjets[0].Pt())#geneJets[0].Perp())
            elif abs( genjets[0].Eta() ) < 3.0 :

                if genjets[0].Pt() > 25. :#geneJets[0].Perp() > 20. :
                    NPVsP.append(npv[0])

                    PTsP.append(genjets[0].Pt())#geneJets[0].Perp())
            else :
                if genjets[0].Pt() > 25. :#geneJets[0].Perp() > 20. :
                    NPVsF.append(npv[0])

                    PTsF.append(genjets[0].Pt())#geneJets[0].Perp())

        
    NPVs.sort()
    PTs.sort()
    NPVsB.sort()
    PTsB.sort()
    NPVsP.sort()
    PTsP.sort()
    NPVsF.sort()
    PTsF.sort()

    NPVSize = len(NPVs)
    PTSize = len(PTs)
    NPVBSize = len(NPVsB)
    PTBSize = len(PTsB)
    NPVPSize = len(NPVsP)
    PTPSize = len(PTsP)
    NPVFSize = len(NPVsF)
    PTFSize = len(PTsF)

    def dynamicBinsNPV(x) :
        dNPVbins = [ NPVs[(NPVSize/nparts)-1], NPVs[2*(NPVSize/nparts)-1], NPVs[3*(NPVSize/nparts)-1], NPVs[4*(NPVSize/nparts)-1] ]
        if x < NPVs[(NPVSize/nparts)-1]:
            return 0        
        for i in xrange( len(dNPVbins) - 1 ) :
            if x >= dNPVbins[i] and x < dNPVbins[i+1] :
                return (i+1)
        return len(dNPVbins) - 1

    def dynamicBinsPT(x) :
        dptbins = [ PTs[(PTSize/npartspt)-1], PTs[2*(PTSize/npartspt)-1], PTs[3*(PTSize/npartspt)-1], PTs[4*(PTSize/npartspt)-1] ]
        if x < PTs[(PTSize/npartspt)-1]:
            return 0        
        for i in xrange( len(dptbins) - 1 ) :
            if x >= dptbins[i] and x < dptbins[i+1] :
                return (i+1)
        return len(dptbins) - 1
    def dynamicBinsNPVB(x) :
        dNPVBbins = [ NPVsB[(NPVBSize/nparts)-1], NPVsB[2*(NPVBSize/nparts)-1], NPVsB[3*(NPVBSize/nparts)-1], NPVsB[4*(NPVBSize/nparts)-1] ]
        if x < NPVsB[(NPVBSize/nparts)-1]:
            return 0        
        for i in xrange( len(dNPVBbins) - 1 ) :
            if x >= dNPVBbins[i] and x < dNPVBbins[i+1] :
                return (i+1)
        return len(dNPVBbins) - 1

    def dynamicBinsPTB(x) :
        dptBbins = [ PTsB[(PTBSize/npartspt)-1], PTsB[2*(PTBSize/npartspt)-1], PTsB[3*(PTBSize/npartspt)-1], PTsB[4*(PTBSize/npartspt)-1] ]
        if x < PTsB[(PTBSize/npartspt)-1]:
            return 0        
        for i in xrange( len(dptBbins) - 1 ) :
            if x >= dptBbins[i] and x < dptBbins[i+1] :
                return (i+1)
        return len(dptBbins) - 1

    def dynamicBinsNPVP(x) :
        dNPVPbins = [ NPVsP[(NPVPSize/nparts)-1], NPVsP[2*(NPVPSize/nparts)-1], NPVsP[3*(NPVPSize/nparts)-1], NPVsP[4*(NPVPSize/nparts)-1] ]
        if x < NPVsP[(NPVPSize/nparts)-1]:
            return 0        
        for i in xrange( len(dNPVPbins) - 1 ) :
            if x >= dNPVPbins[i] and x < dNPVPbins[i+1] :
                return (i+1)
        return len(dNPVPbins) - 1

    def dynamicBinsPTP(x) :
        dptPbins = [ PTsP[(PTPSize/npartspt)-1], PTsP[2*(PTPSize/npartspt)-1], PTsP[3*(PTPSize/npartspt)-1], PTsP[4*(PTPSize/npartspt)-1] ]
        if x < PTsP[(PTPSize/npartspt)-1]:
            return 0        
        for i in xrange( len(dptPbins) - 1 ) :
            if x >= dptPbins[i] and x < dptPbins[i+1] :
                return (i+1)
        return len(dptPbins) - 1

    def dynamicBinsNPVF(x) :
        dNPVFbins = [ NPVsF[(NPVFSize/nparts)-1], NPVsF[2*(NPVFSize/nparts)-1], NPVsF[3*(NPVFSize/nparts)-1], NPVsF[4*(NPVFSize/nparts)-1] ]
        if x < NPVsF[(NPVFSize/nparts)-1]:
            return 0        
        for i in xrange( len(dNPVFbins) - 1 ) :
            if x >= dNPVFbins[i] and x < dNPVFbins[i+1] :
                return (i+1)
        return len(dNPVFbins) - 1

    def dynamicBinsPTF(x) :
        dptFbins = [ PTsF[(PTFSize/npartspt)-1], PTsF[2*(PTFSize/npartspt)-1], PTsF[3*(PTFSize/npartspt)-1], PTsF[4*(PTFSize/npartspt)-1] ]
        if x < PTsF[(PTFSize/npartspt)-1]:
            return 0        
        for i in xrange( len(dptFbins) - 1 ) :
            if x >= dptFbins[i] and x < dptFbins[i+1] :
                return (i+1)
        return len(dptFbins) - 1



# Loop over events
print '==================='
print 'Looping over events'
print '==================='
for jentry in xrange( entries ):

    if jentry %1000 == 0 :
        print jentry
    if 100*jentry % entries == 0 :
        print str(100*jentry/entries) + '% complete'

    # copy next entry into memory and verify
    nb = tree.GetEntry( jentry )
    na = Evttree.GetEntry( jentry )
    if nb <= 0 or na <= 0:
        continue


    # Get the list of jets, and maximum pt to decide
    # which trigger bin this should be in. 
    ptMax = -1.0
        
    PVs = npv[0]    
    #for i in xrange( jets_pt.size() ) :
    if jets.size() > 0 and genjets.size() > 0 and genjets[0].Pt() > 0.0:
        #print '%6.2f %6.2f' % ( jets_pt[i], genjets_pt[i])
        #v = ROOT.TLorentzVector( )
        #v.SetPtEtaPhiE( jets_pt[0], jets_eta[0], jets_phi[0], jets_e[0] )
        if options.algo == 'AK4PFCHS' or options.algo == 'AK8PFCHS' :
            jets[0] *= jets_jecM[0]["L1FastJet"]
            jets[0] *= jets_jecM[0]["L2Relative"]
            jets[0] *= jets_jecM[0]["L3Absolute"]
        else :
            jets[0] *= jets_jecM[0]["Uncorrected"]
    
        pt = jets[0].Pt()
        if pt < 25. :
            continue
        m = jets[0].M()
        y = jets[0].Eta()
        phi = jets[0].Phi()
        E = jets[0].E()
        genpt = genjets[0].Pt()
        genm = genjets[0].M()
        geny = genjets[0].Eta()
        genphi = genjets[0].Phi()
        genE = genjets[0].E()
        rho = (m / (pt*R)) * (m / (pt*R))
        genrho = (genm / (genpt*R)) * (genm / (genpt*R))

        if abs( y ) < 1.479 :
            f.cd("Barrel")
            EtaReg = 0
            if options.dynamicBin :
                jbin = dynamicBinsNPVB(PVs)
                ibin = dynamicBinsPTB(pt)
            else :
                jbin = getNPVbin(PVs)
                ibin = getptbin(pt)
        elif abs( y ) < 2.5 :
            f.cd("Endcap")
            EtaReg = 1
            if options.dynamicBin :
                jbin = dynamicBinsNPV(PVs)
                ibin = dynamicBinsPT(pt)
            else :
                jbin = getNPVbin(PVs)
                ibin = getptbin(pt)
        elif abs( y ) < 3.0 :
            f.cd("Endcap")
            EtaReg = 2
            if options.dynamicBin :
                jbin = dynamicBinsNPVP(PVs)
                ibin = dynamicBinsPTP(pt)
            else :
                jbin = getNPVbin(PVs)
                ibin = getptbin(pt)
        else :
            f.cd("Forward")
            EtaReg = 3
            if options.dynamicBin :
                jbin = dynamicBinsNPVF(PVs)
                ibin = dynamicBinsPTF(pt)
            else :
                jbin = getNPVbin(PVs)
                ibin = getptbin(pt)


        if ibin != None :
            h_eta_mresponses[EtaReg][ibin].Fill( abs(geny), MR(m,genm) )
            h_m_mresponses[EtaReg][ibin].Fill( genm, MR(m,genm) )            
            h_m_ptresponses[EtaReg][ibin].Fill( genm , pt/genpt )                
            h_eta_ptresponses[EtaReg][ibin].Fill( abs(geny), pt/genpt )
            h_m_ptresponses[EtaReg][npartspt+ibin].Fill( genm , (pt - genpt)/genpt )
            h_eta_ptresponses[EtaReg][npartspt+ibin].Fill( abs(geny), (pt - genpt)/genpt )
            h_NPV_ptresponses[EtaReg][ibin].Fill( PVs, (pt - genpt)/genpt )
            h_NPV_mresponses[EtaReg][ibin].Fill( PVs, MR(m,genm) )

        
        #Fill NPV binned things/
        if jbin != None :            
            h_eta_mresponses[EtaReg][npartspt+jbin].Fill( abs(geny), MR(m,genm) )
            h_pt_mresponses[EtaReg][jbin].Fill( genpt , MR(m,genm) )
            h_m_mresponses[EtaReg][npartspt+jbin].Fill( genm, MR(m,genm) )
            h_m_ptresponses[EtaReg][2*npartspt+jbin].Fill( genm , pt/genpt )
            h_pt_ptresponses[EtaReg][jbin].Fill( genpt, pt/genpt )
            h_eta_ptresponses[EtaReg][2*npartspt+jbin].Fill( abs(geny), pt/genpt )
            h_m_ptresponses[EtaReg][2*npartspt+nparts+jbin].Fill( genm , (pt - genpt)/genpt )
            h_pt_ptresponses[EtaReg][nparts+jbin].Fill( genpt, (pt-genpt)/genpt )
            h_eta_ptresponses[EtaReg][2*npartspt+nparts+jbin].Fill( abs(geny), (pt-genpt)/genpt )

        
        h_jetpt[EtaReg].Fill( pt ) 
        h_jeteta[EtaReg].Fill( y )
        h_jetphi[EtaReg].Fill( phi )
        h_jetE[EtaReg].Fill( E )
        
        h_jetArea[EtaReg].Fill( jets_Jarea[0] )
        h_genjetpt[EtaReg].Fill( genpt )
        h_genjeteta[EtaReg].Fill( geny )
        h_genjetphi[EtaReg].Fill( genphi )
        h_genjetE[EtaReg].Fill( genE )
        
        h_genjetArea[EtaReg].Fill( genjets_Jarea[0] )
        h_NPV[EtaReg].Fill( PVs )
        
        h_LUMI[EtaReg].Fill( lumi[0] )
        
        h_DeltaR_gen_jet[EtaReg].Fill( DeltaR_gen_jet[0] )
        
        h_npus[EtaReg].Fill( npus[0] )
        
        h_tnpus[EtaReg].Fill( tnpus[0] )
        
        
        #2D Comparison Plots
        
        h_jetptvsNPV[EtaReg].Fill( PVs, pt)
        h_jetetavsNPV[EtaReg].Fill( PVs, y)
        h_jetAreavsNPV[EtaReg].Fill( PVs , jets_Jarea[0] )
        
        h_NPV_ptresponse[EtaReg].Fill( PVs , pt / genpt )
        h_NPV_aptresponse[EtaReg].Fill( PVs, (pt - genpt)/genpt )
        h_NPV_mresponse[EtaReg].Fill( PVs, MR( m, genm ))

        h_pt0[EtaReg].Fill( pt )
        h_pt_ptresponse0[EtaReg].Fill( genpt, pt / genpt )
        h_pt_aptresponse0[EtaReg].Fill( genpt, (pt - genpt)/genpt )

        if pt > 25. :
            h_eta_ptresponse0[EtaReg].Fill( geny, pt / genpt ) 
            h_eta_aptresponse0[EtaReg].Fill( geny, (pt - genpt)/genpt ) 
            h_m0[EtaReg].Fill( m )
            h_m_mresponse0[EtaReg].Fill( genm, MR( m, genm) )
            h_pt_mresponse0[EtaReg].Fill( genpt, MR(m, genm) )
            h_eta_mresponse0[EtaReg].Fill( geny, MR(m,genm))
            h_rho0[EtaReg].Fill( rho )
            if genrho != 0 :
                h_rho_rhoresponse0[EtaReg].Fill(genrho, rho/genrho)

print "  "
print "EXITING FILE LOOP"
print " "

if options.dynamicBin :
    print "##############################################"
    print "Dynamically Generated Bins"
    print "__________________________"
    print "######## Barrel  #########"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "NPV Bin 0: " + str(NPVsB[0]) + " - " + str(NPVsB[(NPVBSize/nparts)-1])
    print "NPV Bin 1: " + str(NPVsB[(NPVBSize/nparts)-1]) + " - " + str(NPVsB[2*(NPVBSize/nparts)-1])
    print "NPV Bin 2: " + str(NPVsB[2*(NPVBSize/nparts)-1]) + " - " + str(NPVsB[3*(NPVBSize/nparts)-1])
    print "NPV Bin 3: " + str(NPVsB[3*(NPVBSize/nparts)-1]) + " - " + str(NPVsB[4*(NPVBSize/nparts)-1])
    print " "
    print "pt Bin 0: " + str(PTsB[0]) + " - " + str(PTsB[(PTBSize/npartspt)-1])
    print "pt Bin 1: " + str(PTsB[(PTBSize/npartspt)-1]) + " - " + str(PTsB[2*(PTBSize/npartspt)-1]) 
    print "pt Bin 2: " + str(PTsB[2*(PTBSize/npartspt)-1]) + " - " + str(PTsB[3*(PTBSize/npartspt)-1])
    print "pt Bin 3: " + str(PTsB[3*(PTBSize/npartspt)-1]) + " - " + str(PTsB[4*(PTBSize/npartspt)-1])
    print " "
    print "######## Endcap  #########"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "NPV Bin 0: " + str(NPVs[0]) + " - " + str(NPVs[(NPVSize/nparts)-1])
    print "NPV Bin 1: " + str(NPVs[(NPVSize/nparts)-1]) + " - " + str(NPVs[2*(NPVSize/nparts)-1])
    print "NPV Bin 2: " + str(NPVs[2*(NPVSize/nparts)-1]) + " - " + str(NPVs[3*(NPVSize/nparts)-1])
    print "NPV Bin 3: " + str(NPVs[3*(NPVSize/nparts)-1]) + " - " + str(NPVs[4*(NPVSize/nparts)-1])
    
    print "pt Bin 0: " + str(PTs[0]) + " - " + str(PTs[(PTSize/npartspt)-1])
    print "pt Bin 1: " + str(PTs[(PTSize/npartspt)-1]) + " - " + str(PTs[2*(PTSize/npartspt)-1]) 
    print "pt Bin 2: " + str(PTs[2*(PTSize/npartspt)-1]) + " - " + str(PTs[3*(PTSize/npartspt)-1])
    print "pt Bin 3: " + str(PTs[3*(PTSize/npartspt)-1]) + " - " + str(PTs[4*(PTSize/npartspt)-1])
    print " "
    print "##### Pre-Forward  #######"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "NPV Bin 0: " + str(NPVsP[0]) + " - " + str(NPVsP[(NPVPSize/nparts)-1])
    print "NPV Bin 1: " + str(NPVsP[(NPVPSize/nparts)-1]) + " - " + str(NPVsP[2*(NPVPSize/nparts)-1])
    print "NPV Bin 2: " + str(NPVsP[2*(NPVPSize/nparts)-1]) + " - " + str(NPVsP[3*(NPVPSize/nparts)-1])
    print "NPV Bin 3: " + str(NPVsP[3*(NPVPSize/nparts)-1]) + " - " + str(NPVsP[4*(NPVPSize/nparts)-1])
    print " "
    print "pt Bin 0: " + str(PTsP[0]) + " - " + str(PTsP[(PTPSize/npartspt)-1])
    print "pt Bin 1: " + str(PTsP[(PTPSize/npartspt)-1]) + " - " + str(PTsP[2*(PTPSize/npartspt)-1]) 
    print "pt Bin 2: " + str(PTsP[2*(PTPSize/npartspt)-1]) + " - " + str(PTsP[3*(PTPSize/npartspt)-1])
    print "pt Bin 3: " + str(PTsP[3*(PTPSize/npartspt)-1]) + " - " + str(PTsP[4*(PTPSize/npartspt)-1])
    print " "
    print "######## Forward  #########"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "NPV Bin 0: " + str(NPVsF[0]) + " - " + str(NPVsF[(NPVFSize/nparts)-1])
    print "NPV Bin 1: " + str(NPVsF[(NPVFSize/nparts)-1]) + " - " + str(NPVsF[2*(NPVFSize/nparts)-1])
    print "NPV Bin 2: " + str(NPVsF[2*(NPVFSize/nparts)-1]) + " - " + str(NPVsF[3*(NPVFSize/nparts)-1])
    print "NPV Bin 3: " + str(NPVsF[3*(NPVFSize/nparts)-1]) + " - " + str(NPVsF[4*(NPVFSize/nparts)-1])
    print " "
    print "pt Bin 0: " + str(PTsF[0]) + " - " + str(PTsF[(PTFSize/npartspt)-1])
    print "pt Bin 1: " + str(PTsF[(PTFSize/npartspt)-1]) + " - " + str(PTsF[2*(PTFSize/npartspt)-1]) 
    print "pt Bin 2: " + str(PTsF[2*(PTFSize/npartspt)-1]) + " - " + str(PTsF[3*(PTFSize/npartspt)-1])
    print "pt Bin 3: " + str(PTsF[3*(PTFSize/npartspt)-1]) + " - " + str(PTsF[4*(PTFSize/npartspt)-1])
    print " "


    BinsFile = open( BinInfoFileName, 'w')
    BinsFile.write(str(NPVsB[0]))
    BinsFile.write("\n")
    BinsFile.write(str(NPVsB[(NPVBSize/nparts)-1]))
    BinsFile.write("\n")
    BinsFile.write(str(NPVsB[2*(NPVBSize/nparts)-1]))
    BinsFile.write("\n")
    BinsFile.write(str(NPVsB[3*(NPVBSize/nparts)-1]))
    BinsFile.write("\n")
    BinsFile.write(str(NPVsB[4*(NPVBSize/nparts)-1]))
    BinsFile.write("\n")
    BinsFile.write(str(int(PTsB[0])))
    BinsFile.write("\n")
    BinsFile.write(str(int(PTsB[(PTBSize/npartspt)-1])))
    BinsFile.write("\n")
    BinsFile.write(str(int(PTsB[2*(PTBSize/npartspt)-1])))
    BinsFile.write("\n")
    BinsFile.write(str(int(PTsB[3*(PTBSize/npartspt)-1])))
    BinsFile.write("\n")
    BinsFile.write(str(int(PTsB[4*(PTBSize/npartspt)-1])))
    BinsFile.write("\n")
    BinsFile.write(str(NPVs[0]))
    BinsFile.write("\n")
    BinsFile.write(str(NPVs[(NPVSize/nparts)-1]))
    BinsFile.write("\n")
    BinsFile.write(str(NPVs[2*(NPVSize/nparts)-1]))
    BinsFile.write("\n")
    BinsFile.write(str(NPVs[3*(NPVSize/nparts)-1]))
    BinsFile.write("\n")
    BinsFile.write(str(NPVs[4*(NPVSize/nparts)-1]))
    BinsFile.write("\n")
    BinsFile.write(str(int(PTs[0])))
    BinsFile.write("\n")
    BinsFile.write(str(int(PTs[(PTSize/npartspt)-1])))
    BinsFile.write("\n")
    BinsFile.write(str(int(PTs[2*(PTSize/npartspt)-1])))
    BinsFile.write("\n")
    BinsFile.write(str(int(PTs[3*(PTSize/npartspt)-1])))
    BinsFile.write("\n")
    BinsFile.write(str(int(PTs[4*(PTSize/npartspt)-1])))
    BinsFile.write("\n")
    BinsFile.write(str(NPVsP[0]))
    BinsFile.write("\n")
    BinsFile.write(str(NPVsP[(NPVPSize/nparts)-1]))
    BinsFile.write("\n")
    BinsFile.write(str(NPVsP[2*(NPVPSize/nparts)-1]))
    BinsFile.write("\n")
    BinsFile.write(str(NPVsP[3*(NPVPSize/nparts)-1]))
    BinsFile.write("\n")
    BinsFile.write(str(NPVsP[4*(NPVPSize/nparts)-1]))
    BinsFile.write("\n")
    BinsFile.write(str(int(PTsP[0])))
    BinsFile.write("\n")
    BinsFile.write(str(int(PTsP[(PTPSize/npartspt)-1])))
    BinsFile.write("\n")
    BinsFile.write(str(int(PTsP[2*(PTPSize/npartspt)-1])))
    BinsFile.write("\n")
    BinsFile.write(str(int(PTsP[3*(PTPSize/npartspt)-1])))
    BinsFile.write("\n")
    BinsFile.write(str(int(PTsP[4*(PTPSize/npartspt)-1])))
    BinsFile.write("\n")
    BinsFile.write(str(NPVsF[0]))
    BinsFile.write("\n")
    BinsFile.write(str(NPVsF[(NPVFSize/nparts)-1]))
    BinsFile.write("\n")
    BinsFile.write(str(NPVsF[2*(NPVFSize/nparts)-1]))
    BinsFile.write("\n")
    BinsFile.write(str(NPVsF[3*(NPVFSize/nparts)-1]))
    BinsFile.write("\n")
    BinsFile.write(str(NPVsF[4*(NPVFSize/nparts)-1]))
    BinsFile.write("\n")
    BinsFile.write(str(int(PTsF[0])))
    BinsFile.write("\n")
    BinsFile.write(str(int(PTsF[(PTFSize/npartspt)-1])))
    BinsFile.write("\n")
    BinsFile.write(str(int(PTsF[2*(PTFSize/npartspt)-1])))
    BinsFile.write("\n")
    BinsFile.write(str(int(PTsF[3*(PTFSize/npartspt)-1])))
    BinsFile.write("\n")
    BinsFile.write(str(int(PTsF[4*(PTFSize/npartspt)-1])))
    BinsFile.write("\n")
    BinsFile.close()


f.cd()
f.Write()
#print "I might seg fault but I wrote all your data ^.~"
f.Close()
