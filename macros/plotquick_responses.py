#!/usr/bin/env python
from optparse import OptionParser
from ROOT import Math
parser = OptionParser()

parser.add_option('--sample', metavar='F', type='string', action='store',
                  dest='sample',
                  default='qcd',
                  help='ex: qcd ZEE')
#have to add in this feature
#parser.add_option('--algos', metavar='F', type='string', action='store',
#                  dest='type',
#                  default='qcd',
#                  help='ex: qcd ZEE')

parser.add_option('--bunchX', metavar='F', type='string', action='store',
                  dest='BX',
                  default='25ns',
                  help='Bunch Crossing ex: 25 or 50ns')
parser.add_option('--JetType', metavar='F', type='string', action='store',
                  dest='JetType',
                  default='AK4',
                  help='Jet type and radius ex: AK4 or AK8')
parser.add_option('--dynamic', '--db',
                  action='store_true',
                  default=False,
                  dest='dynamicBin',
                  help='Dynamic binning based on events per bin')
parser.add_option('--setTitles', metavar='F', type='string', action='store',
                  default=None,
                  dest='SampleTitle',
                  help='Set desired title for plots, typically indicating sample')
parser.add_option('--PP', '--Publication',
                  action='store_true',
                  default=False,
                  dest='PubPlots',
                  help='Creates Publication Style plots (one per page)')

(options, args) = parser.parse_args()
argv = []

import ROOT

ROOT.gStyle.SetOptStat(000000)
ROOT.gROOT.Macro("rootlogon.C")
if options.SampleTitle == None :
    PlotTitle = options.sample
else :
    PlotTitle = options.SampleTitle

EtaRegions=["Barrel","Endcap","PreForward","Forward"]
#EtaRegions=["Forward"]


if options.dynamicBin :
    BinInfoFileName = "BinInfo_" + options.sample + "_" +  options.JetType + "PFSK" + ".txt"
    BinInfoFile = open( BinInfoFileName , 'r')
    BPVb1 = BinInfoFile.readline()
    BPVb2 = BinInfoFile.readline()
    BPVb3 = BinInfoFile.readline()
    BPVb4 = BinInfoFile.readline()
    BPVb5 = BinInfoFile.readline()
    BPtb1 = BinInfoFile.readline()
    BPtb2 = BinInfoFile.readline()
    BPtb3 = BinInfoFile.readline()
    BPtb4 = BinInfoFile.readline()
    BPtb5 = BinInfoFile.readline()
    PVb1 = BinInfoFile.readline()
    PVb2 = BinInfoFile.readline()
    PVb3 = BinInfoFile.readline()
    PVb4 = BinInfoFile.readline()
    PVb5 = BinInfoFile.readline()
    Ptb1 = BinInfoFile.readline()
    Ptb2 = BinInfoFile.readline()
    Ptb3 = BinInfoFile.readline()
    Ptb4 = BinInfoFile.readline()
    Ptb5 = BinInfoFile.readline()
    PPVb1 = BinInfoFile.readline()
    PPVb2 = BinInfoFile.readline()
    PPVb3 = BinInfoFile.readline()
    PPVb4 = BinInfoFile.readline()
    PPVb5 = BinInfoFile.readline()
    PPtb1 = BinInfoFile.readline()
    PPtb2 = BinInfoFile.readline()
    PPtb3 = BinInfoFile.readline()
    PPtb4 = BinInfoFile.readline()
    PPtb5 = BinInfoFile.readline()
    FPVb1 = BinInfoFile.readline()
    FPVb2 = BinInfoFile.readline()
    FPVb3 = BinInfoFile.readline()
    FPVb4 = BinInfoFile.readline()
    FPVb5 = BinInfoFile.readline()
    FPtb1 = BinInfoFile.readline()
    FPtb2 = BinInfoFile.readline()
    FPtb3 = BinInfoFile.readline()
    FPtb4 = BinInfoFile.readline()
    FPtb5 = BinInfoFile.readline()
else :
    BPVb1 = 10
    BPVb2 = 20
    BPVb3 = 30
    BPVb4 = 40
    BPVb5 = 50
    BPtb1 = 30
    BPtb2 = 100
    BPtb3 = 400
    BPtb4 = 1000
    BPtb5 = 4000
    PVb1 = 10
    PVb2 = 20
    PVb3 = 30
    PVb4 = 40
    PVb5 = 50
    Ptb1 = 30
    Ptb2 = 100
    Ptb3 = 400
    Ptb4 = 1000
    Ptb5 = 4000
    PPVb1 = 10
    PPVb2 = 20
    PPVb3 = 30
    PPVb4 = 40
    PPVb5 = 50
    PPtb1 = 30
    PPtb2 = 100
    PPtb3 = 400
    PPtb4 = 1000
    PPtb5 = 4000
    FPVb1 = 10
    FPVb2 = 20
    FPVb3 = 30
    FPVb4 = 40
    FPVb5 = 50
    FPtb1 = 30
    FPtb2 = 100
    FPtb3 = 400
    FPtb4 = 1000
    FPtb5 = 4000

algos = [ 'PFCHS', 'PFPUPPI', 'PFSK' ]
colors = [1, 2, 4]
markers = [20,21,22]
hists1D = ['h_jetpt', 'h_jeteta', 'h_jetphi', 'h_jetE', 'h_jetArea', 'h_genjetpt', 'h_genjeteta', 'h_genjetphi', 'h_genjetE', 'h_genjetArea', 'h_NPV', 'h_LUMI', 'h_DeltaR_gen_jet', 'h_npus', 'h_tnpus']#,'h_nref','h_refrank']
Titles1D = [ ';p_{T}^{RECO};Number of Events',
             ';y^{RECO};Number of Events',
             ';\phi^{RECO};Number of Events',
             ';E^{RECO};Number of Events',
             ';Jet Area RECO;Number of Events',
             ';p_{T}^{GEN};Number of Events',
             ';y^{GEN};Number of Events',
             ';\phi^{GEN};Number of Events',
             ';E^{RECO};Number of Events',
             ';Jet Area GEN;Number of Events',
             ';Number of Primary Vertices;Number of Events',
             ';LUMI Number;Number of Events',
             ';Delta R;Number of Events',
             ';NPUS;Number of Events',
             ';TNPUS;Number of Events',
             #'nref;Number of Events',
             #'refrank;Number of Events'
]
#2D Comparison Plots
hists2D = ['h_jetptvsNPV', 'h_jetetavsNPV', 'h_jetAreavsNPV',]
inhists = [ 'h_pt_ptresponse0', 'h_eta_ptresponse0', 'h_m_mresponse0', 'h_pt_mresponse0', 'h_eta_mresponse0', 'h_pt_aptresponse0','h_NPV_ptresponse','h_NPV_aptresponse','h_NPV_mresponse']
inhists2 = ['h_pt_ptresponse_npvb', 'h_pt_ptresponse_npvb2', 'h_pt_ptresponse_npvb3', 'h_pt_ptresponse_npvb4',
'h_m_ptresponse_npvb','h_m_ptresponse_npvb2','h_m_ptresponse_npvb3','h_m_ptresponse_npvb4',
'h_m_mresponse_npvb','h_m_mresponse_npvb2','h_m_mresponse_npvb3','h_m_mresponse_npvb4',
'h_pt_mresponse_npvb','h_pt_mresponse_npvb2','h_pt_mresponse_npvb3','h_pt_mresponse_npvb4',
'h_eta_ptresponse_npvb','h_eta_ptresponse_npvb2','h_eta_ptresponse_npvb3','h_eta_ptresponse_npvb4',
'h_eta_mresponse_npvb','h_eta_mresponse_npvb2','h_eta_mresponse_npvb3','h_eta_mresponse_npvb4',
'h_pt_ptresponse_anpvb', 'h_pt_ptresponse_anpvb2', 'h_pt_ptresponse_anpvb3', 'h_pt_ptresponse_anpvb4', 
'h_eta_ptresponse_anpvb','h_eta_ptresponse_anpvb2','h_eta_ptresponse_anpvb3','h_eta_ptresponse_anpvb4',
'h_m_ptresponse_anpvb','h_m_ptresponse_anpvb2','h_m_ptresponse_anpvb3','h_m_ptresponse_anpvb4' ]
inhists3 = ['h_m_ptresponse_ptb','h_m_ptresponse_ptb2','h_m_ptresponse_ptb3','h_m_ptresponse_ptb4',
'h_m_mresponse_ptb','h_m_mresponse_ptb2','h_m_mresponse_ptb3','h_m_mresponse_ptb4',
'h_eta_ptresponse_ptb','h_eta_ptresponse_ptb2','h_eta_ptresponse_ptb3','h_eta_ptresponse_ptb4',
'h_eta_mresponse_ptb','h_eta_mresponse_ptb2','h_eta_mresponse_ptb3','h_eta_mresponse_ptb4', 
'h_eta_ptresponse_aptb','h_eta_ptresponse_aptb2','h_eta_ptresponse_aptb3','h_eta_ptresponse_aptb4',
'h_m_ptresponse_aptb','h_m_ptresponse_aptb2','h_m_ptresponse_aptb3','h_m_ptresponse_aptb4',
'h_NPV_ptresponse_aptb','h_NPV_ptresponse_aptb2','h_NPV_ptresponse_aptb3','h_NPV_ptresponse_aptb4', ]

ptresphists=['p','p','m','m','m','a','p','a','m']
ptresphists2 = ['p','p','p','p', 'p','p','p','p', 'm','m','m','m',  'm','m','m','m', 'p','p','p','p', 'm','m','m','m', 'a','a','a','a', 'a','a','a','a', 'a','a','a','a']
ptresphists3 = ['p','p','p','p', 'm','m','m','m', 'p','p','p','p', 'm','m','m','m', 'a','a','a','a', 'a','a','a','a', 'a','a','a','a' ]


pmax = 2.0 
pmin = 0.5
mmax = 50.0
mmin = -50.0
amax = .2
amin = -.2

pmaxR = .6 
pminR = 0.0
mmaxR = 30.0
mminR = -30.0
amaxR = 0.5
aminR = 0.0

titles1 = [';p_{T}^{GEN};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
           ';y^{GEN};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
           ';m^{GEN};Mean of (m^{RECO} - m^{GEN})',
           ';p_{T}^{GEN};Mean of (m^{RECO} - m^{GEN})',
           ';y^{GEN};Mean of (m^{RECO} - m^{GEN})',
           ';p_{T}^{GEN};Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ';N_{VTX};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
           ';N_{VTX};Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ';N_{VTX};Mean of (m^{RECO} - m^{GEN})']
titles12PU= ['Pileup Binned ' + PlotTitle + ';p_{T}^{GEN};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
             'Pileup Binned;p_{T}^{GEN};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
             'Pileup Binned;p_{T}^{GEN};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
             'Pileup Binned;p_{T}^{GEN};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
             'Pileup Binned ' + PlotTitle + ';m^{GEN};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
             'Pileup Binned;m^{GEN};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
             'Pileup Binned;m^{GEN};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
             'Pileup Binned;m^{GEN};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
             'Pileup Binned ' + PlotTitle + ';m^{GEN};Mean of (m^{RECO} - m^{GEN})',
             'Pileup Binned;m^{GEN};Mean of (m^{RECO} - m^{GEN})',
             'Pileup Binned;m^{GEN};Mean of (m^{RECO} - m^{GEN})',
             'Pileup Binned;m^{GEN};Mean of (m^{RECO} - m^{GEN})',
             'Pileup Binned ' + PlotTitle + ';p_{T}^{GEN};Mean of (m^{RECO} - m^{GEN})',
             'Pileup Binned;p_{T}^{GEN};Mean of (m^{RECO} - m^{GEN})',
             'Pileup Binned;p_{T}^{GEN};Mean of (m^{RECO} - m^{GEN})',
             'Pileup Binned;p_{T}^{GEN};Mean of (m^{RECO} - m^{GEN})',
             'Pileup Binned' + PlotTitle + ';|y^{GEN}|;Mean of p_{T}^{RECO}/p_{T}^{GEN}',
             'Pileup Binned;|y^{GEN}|;Mean of p_{T}^{RECO}/p_{T}^{GEN}',
             'Pileup Binned;|y^{GEN}|;Mean of p_{T}^{RECO}/p_{T}^{GEN}',
             'Pileup Binned;|y^{GEN}|;Mean of p_{T}^{RECO}/p_{T}^{GEN}',
             'Pileup Binned ' + PlotTitle + ';|y^{GEN}|;Mean of (m^{RECO} - m^{GEN})',
             'Pileup Binned;|y^{GEN}|;Mean of (m^{RECO} - m^{GEN})',
             'Pileup Binned;|y^{GEN}|;Mean of (m^{RECO} - m^{GEN})',
             'Pileup Binned;|y^{GEN}|;Mean of (m^{RECO} - m^{GEN})',
             'Pileup Binned ' + PlotTitle + ';p_{T}^{GEN};Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
             'Pileup Binned;p_{T}^{GEN};Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
             'Pileup Binned;p_{T}^{GEN};Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
             'Pileup Binned;p_{T}^{GEN};Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
             'Pileup Binned ' + PlotTitle + ';|y^{GEN}|;Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
             'Pileup Binned;|y^{GEN}|;Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
             'Pileup Binned;|y^{GEN}|;Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
             'Pileup Binned;|y^{GEN}|;Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
             'Pileup Binned ' + PlotTitle + ';m^{GEN};Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
             'Pileup Binned;m^{GEN};Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
             'Pileup Binned;m^{GEN};Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
             'Pileup Binned;m^{GEN};Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',             
           ]
titles12Pt= [
             'p_{T} Binned ' + PlotTitle + ';m^{GEN};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
             'p_{T} Binned;m^{GEN};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
             'p_{T} Binned;m^{GEN};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
             'p_{T} Binned;m^{GEN};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
             'p_{T} Binned ' + PlotTitle + ';m^{GEN};Mean of (m^{RECO} - m^{GEN})',
             'p_{T} Binned;m^{GEN};Mean of (m^{RECO} - m^{GEN})',
             'p_{T} Binned;m^{GEN};Mean of (m^{RECO} - m^{GEN})',
             'p_{T} Binned;m^{GEN};Mean of (m^{RECO} - m^{GEN})',
             'p_{T} Binned ' + PlotTitle + ';|y^{GEN}|;Mean of p_{T}^{RECO}/p_{T}^{GEN}',
             'p_{T} Binned;|y^{GEN}|;Mean of p_{T}^{RECO}/p_{T}^{GEN}',
             'p_{T} Binned;|y^{GEN}|;Mean of p_{T}^{RECO}/p_{T}^{GEN}',
             'p_{T} Binned;|y^{GEN}|;Mean of p_{T}^{RECO}/p_{T}^{GEN}',
             'p_{T} Binned ' + PlotTitle + ';|y^{GEN}|;Mean of (m^{RECO} - m^{GEN})',
             'p_{T} Binned;|y^{GEN}|;Mean of (m^{RECO} - m^{GEN})',
             'p_{T} Binned;|y^{GEN}|;Mean of (m^{RECO} - m^{GEN})',
             'p_{T} Binned;|y^{GEN}|;Mean of (m^{RECO} - m^{GEN})',
             'p_{T} Binned ' + PlotTitle + ';|y^{GEN}|;Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
             'p_{T} Binned;|y^{GEN}|;Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
             'p_{T} Binned;|y^{GEN}|;Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
             'p_{T} Binned;|y^{GEN}|;Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
             'p_{T} Binned ' + PlotTitle + ';m^{GEN};Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
             'p_{T} Binned;m^{GEN};Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
             'p_{T} Binned;m^{GEN};Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
             'p_{T} Binned;m^{GEN};Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
             'p_{T} Binned' + PlotTitle + ';N_{VTX};Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
             'p_{T} Binned;N_{VTX};Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
             'p_{T} Binned;N_{VTX};Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
             'p_{T} Binned;N_{VTX};Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ]
titles12= [str(PVb1) + ' - ' + str(PVb2) + 'PV ' + PlotTitle + ';p_{T}^{GEN};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
           str(PVb2) + ' - ' + str(PVb3) + 'PV;p_{T}^{GEN};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
           str(PVb3) + ' - ' + str(PVb4) + 'PV;p_{T}^{GEN};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
           str(PVb4) + ' - ' + str(PVb5) + 'PV;p_{T}^{GEN};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
           str(PVb1) + ' - ' + str(PVb2) + 'PV ' + PlotTitle + ';m^{GEN};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
           str(PVb2) + ' - ' + str(PVb3) + 'PV;m^{GEN};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
           str(PVb3) + ' - ' + str(PVb4) + 'PV;m^{GEN};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
           str(PVb4) + ' - ' + str(PVb5) + 'PV;m^{GEN};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
           str(PVb1) + ' - ' + str(PVb2) + 'PV ' + PlotTitle + ';m^{GEN};Mean of (m^{RECO} - m^{GEN})',
           str(PVb2) + ' - ' + str(PVb3) + 'PV;m^{GEN};Mean of (m^{RECO} - m^{GEN})',
           str(PVb3) + ' - ' + str(PVb4) + 'PV;m^{GEN};Mean of (m^{RECO} - m^{GEN})',
           str(PVb4) + ' - ' + str(PVb5) + 'PV;m^{GEN};Mean of (m^{RECO} - m^{GEN})',
           str(PVb1) + ' - ' + str(PVb2) + 'PV ' + PlotTitle + ';p_{T}^{GEN};Mean of (m^{RECO} - m^{GEN})',
           str(PVb2) + ' - ' + str(PVb3) + 'PV;p_{T}^{GEN};Mean of (m^{RECO} - m^{GEN})',
           str(PVb3) + ' - ' + str(PVb4) + 'PV;p_{T}^{GEN};Mean of (m^{RECO} - m^{GEN})',
           str(PVb4) + ' - ' + str(PVb5) + 'PV;p_{T}^{GEN};Mean of (m^{RECO} - m^{GEN})',
           str(PVb1) + ' - ' + str(PVb2) + 'PV ' + PlotTitle + ';|y^{GEN}|;Mean of p_{T}^{RECO}/p_{T}^{GEN}',
           str(PVb2) + ' - ' + str(PVb3) + 'PV;|y^{GEN}|;Mean of p_{T}^{RECO}/p_{T}^{GEN}',
           str(PVb3) + ' - ' + str(PVb4) + 'PV;|y^{GEN}|;Mean of p_{T}^{RECO}/p_{T}^{GEN}',
           str(PVb4) + ' - ' + str(PVb5) + 'PV;|y^{GEN}|;Mean of p_{T}^{RECO}/p_{T}^{GEN}',
           str(PVb1) + ' - ' + str(PVb2) + 'PV ' + PlotTitle + ';|y^{GEN}|;Mean of (m^{RECO} - m^{GEN})',
           str(PVb2) + ' - ' + str(PVb3) + 'PV;|y^{GEN}|;Mean of (m^{RECO} - m^{GEN})',
           str(PVb3) + ' - ' + str(PVb4) + 'PV;|y^{GEN}|;Mean of (m^{RECO} - m^{GEN})',
           str(PVb4) + ' - ' + str(PVb5) + 'PV;|y^{GEN}|;Mean of (m^{RECO} - m^{GEN})',
           str(PVb1) + ' - ' + str(PVb2) + 'PV ' + PlotTitle + ';p_{T}^{GEN};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
           str(PVb2) + ' - ' + str(PVb3) + 'PV;p_{T}^{GEN};Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           str(PVb3) + ' - ' + str(PVb4) + 'PV;p_{T}^{GEN};Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           str(PVb4) + ' - ' + str(PVb5) + 'PV;p_{T}^{GEN};Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           str(PVb1) + ' - ' + str(PVb2) + 'PV ' + PlotTitle + ';|y^{GEN}|;Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           str(PVb2) + ' - ' + str(PVb3) + 'PV;|y^{GEN}|;Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           str(PVb3) + ' - ' + str(PVb4) + 'PV;|y^{GEN}|;Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           str(PVb4) + ' - ' + str(PVb5) + 'PV;|y^{GEN}|;Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           str(PVb1) + ' - ' + str(PVb2) + 'PV ' + PlotTitle + ';m^{GEN};Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           str(PVb2) + ' - ' + str(PVb3) + 'PV;m^{GEN};Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           str(PVb3) + ' - ' + str(PVb4) + 'PV;m^{GEN};Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           str(PVb4) + ' - ' + str(PVb5) + 'PV;m^{GEN};Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
          ]
titles2 = [';p_{T}^{GEN};Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           ';y^{GEN};Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           ';m^{GEN};Resolution of (m^{RECO} - m^{GEN})',
           ';p_{T}^{GEN};Resolution of (m^{RECO} - m^{GEN})',
           ';y^{GEN};Resolution of (m^{RECO} - m^{GEN})',
           ';p_{T}^{GEN};Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ';N_{VTX};Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           ';N_{VTX};Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ';N_{VTX};Resolution of (m^{RECO} - m^{GEN})']
titles22PU= [';p_{T}^{GEN};Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           ';p_{T}^{GEN};Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           ';p_{T}^{GEN};Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           ';p_{T}^{GEN};Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           ';m^{GEN};Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           ';m^{GEN};Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           ';m^{GEN};Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           ';m^{GEN};Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           ';m^{GEN};Resolution of (m^{RECO} - m^{GEN})',
           ';m^{GEN};Resolution of (m^{RECO} - m^{GEN})',
           ';m^{GEN};Resolution of (m^{RECO} - m^{GEN})',
           ';m^{GEN};Resolution of (m^{RECO} - m^{GEN})',
           ';p_{T}^{GEN};Resolution of (m^{RECO} - m^{GEN})',
           ';p_{T}^{GEN};Resolution of (m^{RECO} - m^{GEN})',
           ';p_{T}^{GEN};Resolution of (m^{RECO} - m^{GEN})',
           ';p_{T}^{GEN};Resolution of (m^{RECO} - m^{GEN})',
           ';|y^{GEN}|;Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           ';|y^{GEN}|;Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           ';|y^{GEN}|;Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           ';|y^{GEN}|;Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           ';|y^{GEN}|;Resolution of (m^{RECO} - m^{GEN})',
           ';|y^{GEN}|;Resolution of (m^{RECO} - m^{GEN})',
           ';|y^{GEN}|;Resolution of (m^{RECO} - m^{GEN})',
           ';|y^{GEN}|;Resolution of (m^{RECO} - m^{GEN})',
           ';p_{T}^{GEN};Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ';p_{T}^{GEN};Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ';p_{T}^{GEN};Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ';p_{T}^{GEN};Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ';|y^{GEN}|;Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ';|y^{GEN}|;Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ';|y^{GEN}|;Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ';|y^{GEN}|;Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ';m^{GEN};Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ';m^{GEN};Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ';m^{GEN};Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ';m^{GEN};Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}'
           ]
titles22Pt= [';m^{GEN};Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           ';m^{GEN};Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           ';m^{GEN};Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           ';m^{GEN};Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           ';m^{GEN};Resolution of (m^{RECO} - m^{GEN})',
           ';m^{GEN};Resolution of (m^{RECO} - m^{GEN})',
           ';m^{GEN};Resolution of (m^{RECO} - m^{GEN})',
           ';m^{GEN};Resolution of (m^{RECO} - m^{GEN})',           
           ';|y^{GEN}|;Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           ';|y^{GEN}|;Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           ';|y^{GEN}|;Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           ';|y^{GEN}|;Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           ';|y^{GEN}|;Resolution of (m^{RECO} - m^{GEN})',
           ';|y^{GEN}|;Resolution of (m^{RECO} - m^{GEN})',
           ';|y^{GEN}|;Resolution of (m^{RECO} - m^{GEN})',
           ';|y^{GEN}|;Resolution of (m^{RECO} - m^{GEN})',
           ';|y^{GEN}|;Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ';|y^{GEN}|;Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ';|y^{GEN}|;Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ';|y^{GEN}|;Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ';m^{GEN};Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ';m^{GEN};Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ';m^{GEN};Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ';m^{GEN};Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ';N_{VTX};Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ';N_{VTX};Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ';N_{VTX};Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ';N_{VTX};Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}'
           ]
titles22= [str(PVb1) + ' - ' + str(PVb2) + 'PV;p_{T}^{GEN};Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           str(PVb2) + ' - ' + str(PVb3) + 'PV;p_{T}^{GEN};Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           str(PVb3) + ' - ' + str(PVb4) + 'PV;p_{T}^{GEN};Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           str(PVb4) + ' - ' + str(PVb5) + 'PV;p_{T}^{GEN};Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           str(PVb1) + ' - ' + str(PVb2) + 'PV;m^{GEN};Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           str(PVb2) + ' - ' + str(PVb3) + 'PV;m^{GEN};Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           str(PVb3) + ' - ' + str(PVb4) + 'PV;m^{GEN};Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           str(PVb4) + ' - ' + str(PVb5) + 'PV;m^{GEN};Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           str(PVb1) + ' - ' + str(PVb2) + 'PV;m^{GEN};Resolution of (m^{RECO} - m^{GEN})',
           str(PVb2) + ' - ' + str(PVb3) + 'PV;m^{GEN};Resolution of (m^{RECO} - m^{GEN})',
           str(PVb3) + ' - ' + str(PVb4) + 'PV;m^{GEN};Resolution of (m^{RECO} - m^{GEN})',
           str(PVb4) + ' - ' + str(PVb5) + 'PV;m^{GEN};Resolution of (m^{RECO} - m^{GEN})',
           str(PVb1) + ' - ' + str(PVb2) + 'PV;p_{T}^{GEN};Resolution of (m^{RECO} - m^{GEN})',
           str(PVb2) + ' - ' + str(PVb3) + 'PV;p_{T}^{GEN};Resolution of (m^{RECO} - m^{GEN})',
           str(PVb3) + ' - ' + str(PVb4) + 'PV;p_{T}^{GEN};Resolution of (m^{RECO} - m^{GEN})',
           str(PVb4) + ' - ' + str(PVb5) + 'PV;p_{T}^{GEN};Resolution of (m^{RECO} - m^{GEN})',
           str(PVb1) + ' - ' + str(PVb2) + 'PV;|y^{GEN}|;Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           str(PVb2) + ' - ' + str(PVb3) + 'PV;|y^{GEN}|;Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           str(PVb3) + ' - ' + str(PVb4) + 'PV;|y^{GEN}|;Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           str(PVb4) + ' - ' + str(PVb5) + 'PV;|y^{GEN}|;Resolution of p_{T}^{RECO}/p_{T}^{GEN}',
           str(PVb1) + ' - ' + str(PVb2) + 'PV;|y^{GEN}|;Resolution of (m^{RECO} - m^{GEN})',
           str(PVb2) + ' - ' + str(PVb3) + 'PV;|y^{GEN}|;Resolution of (m^{RECO} - m^{GEN})',
           str(PVb3) + ' - ' + str(PVb4) + 'PV;|y^{GEN}|;Resolution of (m^{RECO} - m^{GEN})',
           str(PVb4) + ' - ' + str(PVb5) + 'PV;|y^{GEN}|;Resolution of (m^{RECO} - m^{GEN})',
           str(PVb1) + ' - ' + str(PVb2) + 'PV ' + PlotTitle + ';p_{T}^{GEN};Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           str(PVb2) + ' - ' + str(PVb3) + 'PV;p_{T}^{GEN};Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           str(PVb3) + ' - ' + str(PVb4) + 'PV;p_{T}^{GEN};Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           str(PVb4) + ' - ' + str(PVb5) + 'PV;p_{T}^{GEN};Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           str(PVb1) + ' - ' + str(PVb2) + 'PV ' + PlotTitle + ';|y^{GEN}|;Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           str(PVb2) + ' - ' + str(PVb3) + 'PV;|y^{GEN}|;Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           str(PVb3) + ' - ' + str(PVb4) + 'PV;|y^{GEN}|;Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           str(PVb4) + ' - ' + str(PVb5) + 'PV;|y^{GEN}|;Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           str(PVb1) + ' - ' + str(PVb2) + 'PV ' + PlotTitle + ';m^{GEN};Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           str(PVb2) + ' - ' + str(PVb3) + 'PV;m^{GEN};Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           str(PVb3) + ' - ' + str(PVb4) + 'PV;m^{GEN};Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           str(PVb4) + ' - ' + str(PVb5) + 'PV;m^{GEN};Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ]



infiles = []


for ialgo,algo in enumerate( algos ): 
    infiles.append( ROOT.TFile( 'outplots_' + options.sample + '_' + options.JetType + algo + '.root' ) )

if options.PubPlots :
    print "hi"
elif False :#options.PubPlots :

    allhists = []
    #canvs = []
    legs = []
 
    for ihist,shist in enumerate( inhists ) :
        for EtaReg in xrange(len(EtaRegions)) :
            print 'processing shist = ' + EtaRegions[EtaReg] + "/" + shist
            canv = ROOT.TCanvas(EtaRegions[EtaReg] + "_" + shist, EtaRegions[EtaReg] + "_"+ shist, 1600, 800)
            canv2 = ROOT.TCanvas(EtaRegions[EtaReg] + "_" + shist + "_RES", EtaRegions[EtaReg] + "_"+ shist + "_RES", 1600, 800)
            leg = ROOT.TLegend(0.78, 0.75, 0.9, 0.85)
            leg.SetFillColor(0)
            leg.SetBorderSize(0)
            for iinfile,infile in enumerate(infiles) :
                print '   processing infile = ' + infile.GetName()

                hist = infile.Get( EtaRegions[EtaReg] + '/' + shist)
                allhists.append( hist )
                hist.FitSlicesY()
                hist1 = ROOT.gDirectory.Get(  shist + '_1')
                hist2 = ROOT.gDirectory.Get(  shist + '_2')
                hist1.SetName( 'proj1y_' + shist + '_' + infile.GetName() )
                hist2.SetName( 'proj2y_' + shist + '_' + infile.GetName() )
                hist1.SetMarkerColor(colors[iinfile])
                hist2.SetMarkerColor(colors[iinfile])
                hist1.SetLineColor(colors[iinfile])
                hist2.SetLineColor(colors[iinfile])
                hist1.SetMarkerStyle(markers[iinfile])
                hist2.SetMarkerStyle(markers[iinfile])        
                #hist1.SetMaximum(2.5)
                #hist1.SetMinimum(0.5)
                #hist2.SetMaximum(0.5)
                #hist2.SetMinimum(0.0)
                hist1.Sumw2()
                hist2.Sumw2()
                hist1.GetYaxis().SetTitleOffset( 1.2 )
                hist2.GetYaxis().SetTitleOffset( 1.2 )
                
                nbins = hist1.GetXaxis().GetNbins()
                #hist1.GetXaxis().SetMaximum(GetBinCenter(nbins))
                #print ' nbins= ' + str(nbins)
                hist3 = ROOT.TH1F(algos[iinfile] + '_' + EtaRegions[EtaReg] + '_' + shist + 'RES',algos[iinfile] + '_' + EtaRegions[EtaReg] + '_' + shist + 'RES',nbins,hist1.GetXaxis().GetBinCenter(0),hist1.GetXaxis().GetBinCenter(nbins))
                for n in range(nbins) : 
                    rms = hist2.GetBinContent(n)
                    mean = hist1.GetBinContent(n)
                    rmsErr = hist2.GetBinError(n)
                    meanErr = hist1.GetBinError(n)
                    #x = hist1.GetXaxis().GetBinCenter(n)            
                    if mean != 0.0 :
                        hist3.SetBinContent( n, rms/mean)
                        hist3.SetBinError( n, ROOT.Math.sqrt( (rmsErr/mean)*(rmsErr/mean) + (((rms/mean)/mean)*meanErr)*(((rms/mean)/mean)*meanErr)))
 

                hist3.SetMarkerColor(colors[iinfile])
                hist3.SetLineColor(colors[iinfile])
                hist3.SetMarkerStyle(markers[iinfile])
                hist2.SetMarkerSize(.6)
                hist1.SetMarkerSize(.6)
                
                if ptresphists[ihist] == 'p' :
                    hist1.SetMaximum(pmax)
                    hist1.SetMinimum(pmin)
                    hist2.SetMaximum(pmaxR)
                    hist2.SetMinimum(pminR)                
                elif ptresphists[ihist] == 'm' :
                    hist1.SetMaximum(mmax)
                    hist1.SetMinimum(mmin)
                    hist2.SetMaximum(mmaxR)
                    hist2.SetMinimum(mminR)
                elif ptresphists[ihist] == 'a' :
                    hist1.SetMaximum(amax)
                    hist1.SetMinimum(amin)
                    hist2.SetMaximum(0.2)
                    hist2.SetMinimum(0.05)
                else :
                    print "not sure of response type, skipping "
                    continue

                hist1.SetTitle( 'CMS ' + EtaRegions[EtaReg] + titles1[ihist] )
                hist2.SetTitle( 'CMS ' + EtaRegions[EtaReg] + titles2[ihist] )
                allhists.append( hist1 )
                allhists.append( hist3 )
                leg.AddEntry( hist1, algos[iinfile], 'p')

                canv.cd()
                if iinfile == 0 : 
                    hist1.Draw()
                else :
                    hist1.Draw('same')
                canv2.cd()
                if iinfile == 0 : 
                    hist2.Draw('E')
                else :
                    hist2.Draw('Esame')

            canv.cd()
            leg.Draw()
            legs.append(leg)
            canv.Draw()
            #canvs.append(canv)
            canv.Print('pngs/' + EtaRegions[EtaReg] + "/" + canv.GetName() + options.JetType + '_' + options.BX + '.png' )
            canv2.cd()
            leg.Draw()
            canv2.Draw()
            #canvs.append(canv2)
            canv2.Print('pngs/' + EtaRegions[EtaReg] + "/" + canv.GetName() + options.JetType + '_' + options.BX + '_RES.png' )
            #canv.Delete()
            #canv2.Delete()


    allhists2 = []
    #canvs2 = []
    legs2 = []

    ##Pileup binned plots
    colors2 = [1,2,4,6]
    markers2 = [20,21,22,23]

    for iinfile,infile in enumerate(infiles) :
        print '   processing infile = ' + infile.GetName()
        for EtaReg in xrange(len(EtaRegions)) :
            if EtaReg == 0 :
                PUBin = [ str(BPVb1) + ' to ' + str(BPVb2) + ' PV', str(BPVb2) + ' to ' + str(BPVb3), str(BPVb3) + ' to ' + str(BPVb4), str(BPVb4) + ' to ' + str(BPVb5) ]
            elif EtaReg == 1 :
                PUBin = [ str(PVb1) + ' to ' + str(PVb2) + ' PV', str(PVb2) + ' to ' + str(PVb3), str(PVb3) + ' to ' + str(PVb4), str(PVb4) + ' to ' + str(PVb5) ]
            elif EtaReg == 2 :
                PUBin = [ str(PPVb1) + ' to ' + str(PPVb2) + ' PV', str(PPVb2) + ' to ' + str(PPVb3), str(PPVb3) + ' to ' + str(PPVb4), str(PPVb4) + ' to ' + str(PPVb5) ]
            else :
                PUBin = [ str(FPVb1) + ' to ' + str(FPVb2) + ' PV', str(FPVb2) + ' to ' + str(FPVb3), str(FPVb3) + ' to ' + str(FPVb4), str(FPVb4) + ' to ' + str(FPVb5) ]
            for ihist,shist in enumerate( inhists2 ) :
                canvname = EtaRegions[EtaReg] + '_' + shist + '_PUBinned'
                print 'processing shist = ' + canvname
                nh = ihist%4
                if nh == 0 :
                    canv = ROOT.TCanvas(canvname,canvname, 1600, 800)
                    canv2 = ROOT.TCanvas(canvname + "_RES" , canvname + "_RES" , 1600, 800)
                    leg = ROOT.TLegend(0.78, 0.70, 0.9, 0.85)    
                    leg.SetFillColor(0)
                    leg.SetBorderSize(0)
        
                ROOT.gStyle.SetLabelSize( .025, "xyz")
                title12PU = titles12PU[ihist]
                title22PU = algos[iinfile] + ' ' + EtaRegions[EtaReg] + titles22PU[ihist]
                hist = infile.Get( EtaRegions[EtaReg] + '/' + shist)
                allhists.append( hist )
                hist.FitSlicesY()
                hist1 = ROOT.gDirectory.Get( shist + '_1')
                hist2 = ROOT.gDirectory.Get( shist + '_2')
                hist1.SetName( 'proj1y_' + shist + '_' + infile.GetName() )
                hist2.SetName( 'proj2y_' + shist + '_' + infile.GetName() )
                hist1.SetMarkerColor(colors2[nh])
                hist2.SetMarkerColor(colors2[nh])
                hist1.SetLineColor(colors2[nh])
                hist2.SetLineColor(colors2[nh])
                hist1.SetMarkerStyle(markers2[nh])
                hist2.SetMarkerStyle(markers2[nh])        
                hist2.SetMarkerSize(.6)
                hist1.SetMarkerSize(.6)

                #hist1.SetMaximum(1.8)
                #hist1.SetMinimum(0.5)
                #hist2.SetMaximum(0.5)
                #hist2.SetMinimum(0.0)
                hist1.SetTitle( title12PU )
                hist2.SetTitle( title22PU )

                hist1.Sumw2()
                hist2.Sumw2()

                nbins = hist1.GetXaxis().GetNbins()
                #hist1.GetXaxis().SetMaximum(GetBinCenter(nbins))
                #print ' nbins= ' + str(nbins)
                hist3 = ROOT.TH1F(algos[iinfile] + '_' + EtaRegions[EtaReg] + '_' + shist + 'RES',algos[iinfile] + '_' + EtaRegions[EtaReg] + '_' + shist + 'RES',nbins,hist1.GetXaxis().GetBinCenter(0),hist1.GetXaxis().GetBinCenter(nbins))
                for n in range(nbins) : 
                    rms = hist2.GetBinContent(n)
                    mean = hist1.GetBinContent(n)
                    rmsErr = hist2.GetBinError(n)
                    meanErr = hist1.GetBinError(n)
                    #x = hist1.GetXaxis().GetBinCenter(n)
            
                    if mean != 0.0 :
                        hist3.SetBinContent( n, rms/mean)
                        hist3.SetBinError( n, ROOT.Math.sqrt( (rmsErr/mean)*(rmsErr/mean) + (((rms/mean)/mean)*meanErr)*(((rms/mean)/mean)*meanErr)))
                    
        
                #hist1.GetXaxis().SetRange( 0, 2000)#hist1.GetXaxis().GetMaximum() )

                hist1.GetYaxis().SetTitleOffset( 1.2 )
                hist2.GetYaxis().SetTitleOffset( 1.2 )

                hist2.SetMarkerColor(colors2[nh])
                hist2.SetLineColor(colors2[nh])
                hist2.SetMarkerStyle(markers2[nh])
                hist2.SetTitle( title22PU )
                #hist3.SetMaximum(0.7)
                #hist3.SetMinimum(0.001)


                if ptresphists2[ihist] == 'p' :
                    hist1.SetMaximum(pmax)
                    hist1.SetMinimum(pmin)
                    hist2.SetMaximum(pmaxR)
                    hist2.SetMinimum(pminR)                
                elif ptresphists2[ihist] == 'm' :
                    hist1.SetMaximum(mmax)
                    hist1.SetMinimum(mmin)
                    hist2.SetMaximum(mmaxR)
                    hist2.SetMinimum(mminR)
                elif ptresphists2[ihist] == 'a' :
                    hist1.SetMaximum(amax)
                    hist1.SetMinimum(amin)
                    hist2.SetMaximum(amaxR)
                    hist2.SetMinimum(aminR)
                else :
                    print "not sure of response type, skipping "
                    continue


                allhists.append( hist1 )
                allhists.append( hist2 )
        
                allhists.append( hist3 ) 
        
                leg.AddEntry( hist1, PUBin[nh], 'p')
                
                canv.cd()
                if nh == 0 : 
                    hist1.Draw()
                else :
                    hist1.Draw('same')
                canv2.cd()
                if nh == 0 : 
                    hist2.Draw('E')
                else :
                    hist2.Draw('Esame')

                if nh == 3 :
                    canv.cd()
                    leg.Draw()
                    legs2.append(leg)
                    canv.Draw()
                    #canvs2.append(canv)
                    canv.Print('pngs/' +  EtaRegions[EtaReg] + '/NPVBinned/' + algos[iinfile] + '_' + canv.GetName() + '_' + options.JetType + '_' + options.BX + '.png' )

                    canv2.cd()
                    leg.Draw()
                    legs2.append(leg)
                    canv2.Draw()
                    #canvs2.append(canv2)
                    canv2.Print('pngs/' +  EtaRegions[EtaReg] + '/NPVBinned/' + algos[iinfile] + '_' + canv.GetName() + '_' + options.JetType + '_' + options.BX + '_RES.png' )


    #Pt Binned Plots

    for iinfile,infile in enumerate(infiles) :
        print '   processing infile = ' + infile.GetName()
        for EtaReg in xrange(len(EtaRegions)) :
            if EtaReg == 0 :
                PtBin = [ str(BPtb1) + ' to ' + str(BPtb2) + ' GeV', str(BPtb2) + ' to ' + str(BPtb3), str(BPtb3) + ' to ' + str(BPtb4), str(BPtb4) + ' to ' + str(BPtb5) ]
            elif EtaReg == 1 :
                PtBin = [ str(Ptb1) + ' to ' + str(Ptb2) + 'GeV', str(Ptb2) + ' to ' + str(Ptb3), str(Ptb3) + ' to ' + str(Ptb4), str(Ptb4) + ' to ' + str(Ptb5) ]
            elif EtaReg == 2 :
                PtBin = [ str(PPtb1) + ' to ' + str(PPtb2) + 'GeV', str(PPtb2) + ' to ' + str(PPtb3), str(PPtb3) + ' to ' + str(PPtb4), str(PPtb4) + ' to ' + str(PPtb5) ]
            else :
                PtBin = [ str(FPtb1) + ' to ' + str(FPtb2) + ' GeV', str(FPtb2) + ' to ' + str(FPtb3), str(FPtb3) + ' to ' + str(FPtb4), str(FPtb4) + ' to ' + str(FPtb5) ]
            for ihist,shist in enumerate( inhists3 ) :
                canvname = EtaRegions[EtaReg] + '_' + shist + '_PtBinned'
                print 'processing shist = ' + canvname
                nh = ihist%4
                if nh == 0 :
                    canv = ROOT.TCanvas(canvname,canvname, 1600, 800)
                    canv2 = ROOT.TCanvas(canvname + "_RES",canvname + "_RES", 1600, 800)
                     
                    leg = ROOT.TLegend(0.78, 0.70, 0.9, 0.85)    
                    leg.SetFillColor(0)
                    leg.SetBorderSize(0)
        
                ROOT.gStyle.SetLabelSize( .025, "xyz")
                title12Pt = titles12Pt[ihist]
                title22Pt = algos[iinfile] + ' ' + EtaRegions[EtaReg] + titles22Pt[ihist]
                hist = infile.Get( EtaRegions[EtaReg] + '/' + shist)
                allhists.append( hist )
                hist.FitSlicesY()
                hist1 = ROOT.gDirectory.Get( shist + '_1')
                hist2 = ROOT.gDirectory.Get( shist + '_2')
                hist1.SetName( 'proj1y_' + shist + '_' + infile.GetName() )
                hist2.SetName( 'proj2y_' + shist + '_' + infile.GetName() )
                hist1.SetMarkerColor(colors2[nh])
                hist2.SetMarkerColor(colors2[nh])
                hist1.SetLineColor(colors2[nh])
                hist2.SetLineColor(colors2[nh])
                hist1.SetMarkerStyle(markers2[nh])
                hist2.SetMarkerStyle(markers2[nh])        
                #hist1.SetMaximum(1.8)
                #hist1.SetMinimum(0.5)
                #hist2.SetMaximum(0.5)
                #hist2.SetMinimum(0.0)
                hist1.SetTitle( title12Pt )
                hist2.SetTitle( title22Pt )
                hist1.Sumw2()
                hist2.Sumw2()
                hist2.SetMarkerSize(.6)
                hist1.SetMarkerSize(.6)
                nbins = hist1.GetXaxis().GetNbins()
                #hist1.GetXaxis().SetMaximum(GetBinCenter(nbins))
                #print ' nbins= ' + str(nbins)
                
                hist3 = ROOT.TH1F(algos[iinfile] + '_' + EtaRegions[EtaReg] + '_' + canvname + 'RES',algos[iinfile] + '_' + EtaRegions[EtaReg] + '_' + canvname + 'RES',nbins,hist1.GetXaxis().GetBinCenter(0),hist1.GetXaxis().GetBinCenter(nbins))

                for n in range(nbins) :
                    rms = hist2.GetBinContent(n)
                    mean = hist1.GetBinContent(n)
                    rmsErr = hist2.GetBinError(n)
                    meanErr = hist1.GetBinError(n)
                    #x = hist1.GetXaxis().GetBinCenter(n)
            
                    if mean != 0.0 :
                        hist3.SetBinContent( n, rms/mean)
                        hist3.SetBinError( n, ROOT.Math.sqrt( (rmsErr/mean)*(rmsErr/mean) + (((rms/mean)/mean)*meanErr)*(((rms/mean)/mean)*meanErr)))
        
        
                hist1.GetYaxis().SetTitleOffset( 1.2 )
                hist2.GetYaxis().SetTitleOffset( 1.2 )

                hist2.SetMarkerColor(colors2[nh])
                hist2.SetLineColor(colors2[nh])
                hist2.SetMarkerStyle(markers2[nh])
                hist2.SetTitle( title22Pt )
                #hist3.SetMaximum(0.7)
                #hist3.SetMinimum(0.001)



                if ptresphists3[ihist] == 'p' :
                    hist1.SetMaximum(pmax)
                    hist1.SetMinimum(pmin)
                    hist2.SetMaximum(pmaxR)
                    hist2.SetMinimum(pminR)                  
                elif ptresphists3[ihist] == 'm' :
                    hist1.SetMaximum(mmax)
                    hist1.SetMinimum(mmin)
                    hist2.SetMaximum(mmaxR)
                    hist2.SetMinimum(mminR)  
                elif ptresphists3[ihist] == 'a' :
                    hist1.SetMaximum(amax)
                    hist1.SetMinimum(amin)
                    hist2.SetMaximum(amaxR)
                    hist2.SetMinimum(aminR)  
                else :
                    print "not sure of response type, skipping "
                    continue

                allhists.append( hist1 )
                allhists.append( hist2 )
        
                allhists.append( hist3 ) 
        
                leg.AddEntry( hist1, PtBin[nh], 'p')

                canv.cd()
                if nh == 0 : 
                    hist1.Draw()
                else :
                    hist1.Draw('same')
                canv2.cd()
                if nh == 0 : 
                    hist2.Draw('E')
                else :
                    hist2.Draw('Esame')

                if nh == 3 :
                    canv.cd()
                    leg.Draw()
                    legs2.append(leg)
                    canv.Draw()
                    #canvs2.append(canv)
                    canv.Print('pngs/' +  EtaRegions[EtaReg] + '/PtBinned/' + algos[iinfile] + '_' + canv.GetName() + '_' + options.JetType + '_' + options.BX + '.png' )

                    canv2.cd()
                    leg.Draw()
                    legs2.append(leg)
                    canv2.Draw()
                    #canvs2.append(canv2)
                    canv2.Print('pngs/' +  EtaRegions[EtaReg] + '/PtBinned/' + algos[iinfile] + '_' + canv.GetName() + '_' + options.JetType + '_' + options.BX + '_RES.png' )

#!!!!!!!!!!!!! ENDDDDDDDDDDDDDD


allhists = []
canvs = []
legs = []
for ihist,shist in enumerate( hists1D ) :
    continue
    for EtaReg in xrange(len(EtaRegions)) :
        print 'processing shist = ' + EtaRegions[EtaReg] + "/" + shist
        canv = ROOT.TCanvas(EtaRegions[EtaReg] + "_" + shist, EtaRegions[EtaReg] + "_"+ shist, 1600, 800)
        leg = ROOT.TLegend(0.8, 0.6, 1.05, 0.85)
    
        leg.SetFillColor(0)
        leg.SetBorderSize(0)
        for iinfile,infile in enumerate(infiles) :
            print '   processing infile = ' + infile.GetName()
        
            hist = infile.Get( EtaRegions[EtaReg] + '/' + shist)
            allhists.append( hist )
            hist.SetMarkerColor(colors[iinfile])
            hist.SetLineColor(colors[iinfile])
            hist.SetMarkerStyle(markers[iinfile])
                        
            hist.SetTitle( Titles1D[ihist] )
            
            allhists.append( hist )
            
            leg.AddEntry( hist, algos[iinfile], 'p')

            
            if iinfile == 0 : 
                hist.Draw()
            else :
                hist.Draw('same')
            
        leg.Draw()
        legs.append(leg)
        canv.Draw()
        #canvs.append(canv)
        canv.Print('pngs/' + EtaRegions[EtaReg] + "/" + canv.GetName() + options.JetType + '_' + options.BX + '.png' )
        




for ihist,shist in enumerate( inhists ) :
    if options.PubPlots :
        continue
    for EtaReg in xrange(len(EtaRegions)) :
        print 'processing shist = ' + EtaRegions[EtaReg] + "/" + shist
        canv = ROOT.TCanvas(EtaRegions[EtaReg] + "_" + shist, EtaRegions[EtaReg] + "_"+ shist, 1600, 800)
        canv.Divide(2,1)
        leg = ROOT.TLegend(0.8, 0.6, 1.05, 0.85)
    
        leg.SetFillColor(0)
        leg.SetBorderSize(0)
        for iinfile,infile in enumerate(infiles) :
            print '   processing infile = ' + infile.GetName()
        

            hist = infile.Get( EtaRegions[EtaReg] + '/' + shist)
            allhists.append( hist )
            hist.FitSlicesY()
            hist1 = ROOT.gDirectory.Get(  shist + '_1')
            hist2 = ROOT.gDirectory.Get(  shist + '_2')
            hist1.SetName( 'proj1y_' + shist + '_' + infile.GetName() )
            hist2.SetName( 'proj2y_' + shist + '_' + infile.GetName() )
            hist1.SetMarkerColor(colors[iinfile])
            hist2.SetMarkerColor(colors[iinfile])
            hist1.SetLineColor(colors[iinfile])
            hist2.SetLineColor(colors[iinfile])
            hist1.SetMarkerStyle(markers[iinfile])
            hist2.SetMarkerStyle(markers[iinfile])        
            #hist1.SetMaximum(2.5)
            #hist1.SetMinimum(0.5)
            #hist2.SetMaximum(0.5)
            #hist2.SetMinimum(0.0)
            hist1.Sumw2()
            hist2.Sumw2()
            hist1.GetYaxis().SetTitleOffset( 1.2 )
            hist2.GetYaxis().SetTitleOffset( 1.2 )

            nbins = hist1.GetXaxis().GetNbins()
            #hist1.GetXaxis().SetMaximum(GetBinCenter(nbins))
            #print ' nbins= ' + str(nbins)
            hist3 = ROOT.TH1F(algos[iinfile] + '_' + EtaRegions[EtaReg] + '_' + shist + 'RES',algos[iinfile] + '_' + EtaRegions[EtaReg] + '_' + shist + 'RES',nbins,hist1.GetXaxis().GetBinCenter(0),hist1.GetXaxis().GetBinCenter(nbins))
            for n in range(nbins) : 
                rms = hist2.GetBinContent(n)
                mean = hist1.GetBinContent(n)
                rmsErr = hist2.GetBinError(n)
                meanErr = hist1.GetBinError(n)
                #x = hist1.GetXaxis().GetBinCenter(n)            
                if mean != 0.0 :
                    hist3.SetBinContent( n, rms/mean)
                    hist3.SetBinError( n, ROOT.Math.sqrt( (rmsErr/mean)*(rmsErr/mean) + (((rms/mean)/mean)*meanErr)*(((rms/mean)/mean)*meanErr)))
 

            hist3.SetMarkerColor(colors[iinfile])
            hist3.SetLineColor(colors[iinfile])
            hist3.SetMarkerStyle(markers[iinfile])
            hist2.SetMarkerSize(.6)
            hist1.SetMarkerSize(.6)

            if ptresphists[ihist] == 'p' :
                hist1.SetMaximum(pmax)
                hist1.SetMinimum(pmin)
                hist2.SetMaximum(pmaxR)
                hist2.SetMinimum(pminR)                
            elif ptresphists[ihist] == 'm' :
                hist1.SetMaximum(mmax)
                hist1.SetMinimum(mmin)
                hist2.SetMaximum(mmaxR)
                hist2.SetMinimum(mminR)
            elif ptresphists[ihist] == 'a' :
                hist1.SetMaximum(amax)
                hist1.SetMinimum(amin)
                hist2.SetMaximum(0.2)
                hist2.SetMinimum(0.05)
            else :
                print "not sure of response type, skipping "
                continue

            hist1.SetTitle( titles1[ihist] )
            hist2.SetTitle( titles2[ihist] )
            allhists.append( hist1 )
            allhists.append( hist3 )
            leg.AddEntry( hist1, algos[iinfile], 'p')

            canv.cd(1)
            if iinfile == 0 : 
                hist1.Draw()
            else :
                hist1.Draw('same')
            canv.cd(2)
            if iinfile == 0 : 
                hist2.Draw('E')
            else :
                hist2.Draw('Esame')

        canv.cd(1)
        leg.Draw()
        legs.append(leg)
        canv.Draw()
        #canvs.append(canv)
        canv.Print('pngs/' + EtaRegions[EtaReg] + "/" + canv.GetName() + options.JetType + '_' + options.BX + '.png' )


#Do projections instead
for ihist,shist in enumerate( inhists ) :
    continue
    for EtaReg in xrange(len(EtaRegions)) :
        print 'processing shist = ' + EtaRegions[EtaReg] + "/" + shist

        for iinfile,infile in enumerate(infiles) :
            print '   processing infile = ' + infile.GetName()
            canv = ROOT.TCanvas(EtaRegions[EtaReg] + "_23" + shist, EtaRegions[EtaReg] + "_23"+ shist, 1600, 800)
            leg = ROOT.TLegend(0.8, 0.6, 1.05, 0.85)
            
            leg.SetFillColor(0)
            leg.SetBorderSize(0)


            
            hist = infile.Get( EtaRegions[EtaReg] + '/' + shist)
            nbins = hist.GetXaxis().GetNbins()
            allhists.append( hist )
            for i in xrange(nbins-1) :
                hist1 = hist.ProjectionY( shist + "_proj", i, (i+1), "")
                hist1.SetMarkerColor(colors[iinfile])
                hist1.SetLineColor(colors[iinfile])
                hist1.SetMarkerStyle(markers[iinfile])
                hist1.Sumw2()
                hist1.SetTitle( titles1[ihist] )
                allhists.append( hist1 )
                leg.AddEntry( hist1, algos[iinfile], 'l')
                hist1.Draw('L')
                leg.Draw()
                legs.append(leg)
                canv.Draw()
                canvs.append(canv)
                canv.Print('pngs/' + EtaRegions[EtaReg] + "/AlgoBinned/" + canv.GetName() + options.JetType + '_' + options.BX + '_' + algos[iinfile] + '_proj' + str(hist.GetXaxis().GetBinCenter(i)) + '.png' )
                canv.Clear()
                leg.Clear()
                hist1.Clear()


allhists2 = []
#canvs2 = []
legs2 = []


##Pileup binned plots
colors2 = [1,2,4,6]
markers2 = [20,21,22,23]

for iinfile,infile in enumerate(infiles) :
    if options.PubPlots :
        continue
    print '   processing infile = ' + infile.GetName()
    for EtaReg in xrange(len(EtaRegions)) :
        if EtaReg == 0 :
            PUBin = [ str(BPVb1) + ' to ' + str(BPVb2) + ' PV', str(BPVb2) + ' to ' + str(BPVb3), str(BPVb3) + ' to ' + str(BPVb4), str(BPVb4) + ' to ' + str(BPVb5) ]
        elif EtaReg == 1 :
            PUBin = [ str(PVb1) + ' to ' + str(PVb2) + ' PV', str(PVb2) + ' to ' + str(PVb3), str(PVb3) + ' to ' + str(PVb4), str(PVb4) + ' to ' + str(PVb5) ]
        elif EtaReg == 2 :
            PUBin = [ str(PPVb1) + ' to ' + str(PPVb2) + ' PV', str(PPVb2) + ' to ' + str(PPVb3), str(PPVb3) + ' to ' + str(PPVb4), str(PPVb4) + ' to ' + str(PPVb5) ]
        else :
            PUBin = [ str(FPVb1) + ' to ' + str(FPVb2) + ' PV', str(FPVb2) + ' to ' + str(FPVb3), str(FPVb3) + ' to ' + str(FPVb4), str(FPVb4) + ' to ' + str(FPVb5) ]
        for ihist,shist in enumerate( inhists2 ) :
            canvname = EtaRegions[EtaReg] + '_' + shist + '_PUBinned'
            print 'processing shist = ' + canvname
            nh = ihist%4
            if nh == 0 :
                canv = ROOT.TCanvas(canvname,canvname, 1600, 800)
                canv.Divide(2,1)
        
                leg = ROOT.TLegend(0.8, 0.6, 1.05, 0.85)    
                leg.SetFillColor(0)
                leg.SetBorderSize(0)
        
            ROOT.gStyle.SetLabelSize( .025, "xyz")
            title12PU = titles12PU[ihist]
            title22PU = algos[iinfile] + ' ' + EtaRegions[EtaReg] + titles22PU[ihist]
            hist = infile.Get( EtaRegions[EtaReg] + '/' + shist)
            allhists.append( hist )
            hist.FitSlicesY()
            hist1 = ROOT.gDirectory.Get( shist + '_1')
            hist2 = ROOT.gDirectory.Get( shist + '_2')
            hist1.SetName( 'proj1y_' + shist + '_' + infile.GetName() )
            hist2.SetName( 'proj2y_' + shist + '_' + infile.GetName() )
            hist1.SetMarkerColor(colors2[nh])
            hist2.SetMarkerColor(colors2[nh])
            hist1.SetLineColor(colors2[nh])
            hist2.SetLineColor(colors2[nh])
            hist1.SetMarkerStyle(markers2[nh])
            hist2.SetMarkerStyle(markers2[nh])        
            hist2.SetMarkerSize(.6)
            hist1.SetMarkerSize(.6)

            #hist1.SetMaximum(1.8)
            #hist1.SetMinimum(0.5)
            #hist2.SetMaximum(0.5)
            #hist2.SetMinimum(0.0)
            hist1.SetTitle( title12PU )
            hist2.SetTitle( title22PU )

            hist1.Sumw2()
            hist2.Sumw2()

            nbins = hist1.GetXaxis().GetNbins()
            #hist1.GetXaxis().SetMaximum(GetBinCenter(nbins))
            #print ' nbins= ' + str(nbins)
            hist3 = ROOT.TH1F(algos[iinfile] + '_' + EtaRegions[EtaReg] + '_' + shist + 'RES',algos[iinfile] + '_' + EtaRegions[EtaReg] + '_' + shist + 'RES',nbins,hist1.GetXaxis().GetBinCenter(0),hist1.GetXaxis().GetBinCenter(nbins))
            for n in range(nbins) : 
                rms = hist2.GetBinContent(n)
                mean = hist1.GetBinContent(n)
                rmsErr = hist2.GetBinError(n)
                meanErr = hist1.GetBinError(n)
                #x = hist1.GetXaxis().GetBinCenter(n)
            
                if mean != 0.0 :
                    hist3.SetBinContent( n, rms/mean)
                    hist3.SetBinError( n, ROOT.Math.sqrt( (rmsErr/mean)*(rmsErr/mean) + (((rms/mean)/mean)*meanErr)*(((rms/mean)/mean)*meanErr)))
                    
        
            #hist1.GetXaxis().SetRange( 0, 2000)#hist1.GetXaxis().GetMaximum() )

            hist1.GetYaxis().SetTitleOffset( 1.2 )
            hist2.GetYaxis().SetTitleOffset( 1.2 )

            hist2.SetMarkerColor(colors2[nh])
            hist2.SetLineColor(colors2[nh])
            hist2.SetMarkerStyle(markers2[nh])
            hist2.SetTitle( title22PU )
            #hist3.SetMaximum(0.7)
            #hist3.SetMinimum(0.001)


            if ptresphists2[ihist] == 'p' :
                hist1.SetMaximum(pmax)
                hist1.SetMinimum(pmin)
                hist2.SetMaximum(pmaxR)
                hist2.SetMinimum(pminR)                
            elif ptresphists2[ihist] == 'm' :
                hist1.SetMaximum(mmax)
                hist1.SetMinimum(mmin)
                hist2.SetMaximum(mmaxR)
                hist2.SetMinimum(mminR)
            elif ptresphists2[ihist] == 'a' :
                hist1.SetMaximum(amax)
                hist1.SetMinimum(amin)
                hist2.SetMaximum(amaxR)
                hist2.SetMinimum(aminR)
            else :
                print "not sure of response type, skipping "
                continue


            allhists.append( hist1 )
            allhists.append( hist2 )
        
            allhists.append( hist3 ) 
        
            leg.AddEntry( hist1, PUBin[nh], 'p')

            canv.cd(1)
            if nh == 0 : 
                hist1.Draw()
            else :
                hist1.Draw('same')
            canv.cd(2)
            if nh == 0 : 
                hist2.Draw('E')
            else :
                hist2.Draw('Esame')

            if nh == 3 :
                canv.cd(1)
                leg.Draw()
                legs2.append(leg)
                canv.Draw()
                #canvs2.append(canv)
                canv.Print('pngs/' +  EtaRegions[EtaReg] + '/NPVBinned/' + algos[iinfile] + '_' + canv.GetName() + '_' + options.JetType + '_' + options.BX + '.png' )


#Pt Binned Plots

for iinfile,infile in enumerate(infiles) :
    if options.PubPlots :
        continue
    print '   processing infile = ' + infile.GetName()
    for EtaReg in xrange(len(EtaRegions)) :
        if EtaReg == 0 :
            PtBin = [ str(BPtb1) + ' to ' + str(BPtb2) + ' GeV', str(BPtb2) + ' to ' + str(BPtb3), str(BPtb3) + ' to ' + str(BPtb4), str(BPtb4) + ' to ' + str(BPtb5) ]
        elif EtaReg == 1 :
            PtBin = [ str(Ptb1) + ' to ' + str(Ptb2) + 'GeV', str(Ptb2) + ' to ' + str(Ptb3), str(Ptb3) + ' to ' + str(Ptb4), str(Ptb4) + ' to ' + str(Ptb5) ]
        elif EtaReg == 2 :
            PtBin = [ str(PPtb1) + ' to ' + str(PPtb2) + 'GeV', str(PPtb2) + ' to ' + str(PPtb3), str(PPtb3) + ' to ' + str(PPtb4), str(PPtb4) + ' to ' + str(PPtb5) ]
        else :
            PtBin = [ str(FPtb1) + ' to ' + str(FPtb2) + ' GeV', str(FPtb2) + ' to ' + str(FPtb3), str(FPtb3) + ' to ' + str(FPtb4), str(FPtb4) + ' to ' + str(FPtb5) ]
        for ihist,shist in enumerate( inhists3 ) :
            canvname = EtaRegions[EtaReg] + '_' + shist + '_PtBinned'
            print 'processing shist = ' + canvname
            nh = ihist%4
            if nh == 0 :
                canv = ROOT.TCanvas(canvname,canvname, 1600, 800)
                canv.Divide(2,1)
        
                leg = ROOT.TLegend(0.8, 0.6, 1.05, 0.85)    
                leg.SetFillColor(0)
                leg.SetBorderSize(0)
        
            ROOT.gStyle.SetLabelSize( .025, "xyz")
            title12Pt = titles12Pt[ihist]
            title22Pt = algos[iinfile] + ' ' + EtaRegions[EtaReg] + titles22Pt[ihist]
            hist = infile.Get( EtaRegions[EtaReg] + '/' + shist)
            allhists.append( hist )
            hist.FitSlicesY()
            hist1 = ROOT.gDirectory.Get( shist + '_1')
            hist2 = ROOT.gDirectory.Get( shist + '_2')
            hist1.SetName( 'proj1y_' + shist + '_' + infile.GetName() )
            hist2.SetName( 'proj2y_' + shist + '_' + infile.GetName() )
            hist1.SetMarkerColor(colors2[nh])
            hist2.SetMarkerColor(colors2[nh])
            hist1.SetLineColor(colors2[nh])
            hist2.SetLineColor(colors2[nh])
            hist1.SetMarkerStyle(markers2[nh])
            hist2.SetMarkerStyle(markers2[nh])        
            #hist1.SetMaximum(1.8)
            #hist1.SetMinimum(0.5)
            #hist2.SetMaximum(0.5)
            #hist2.SetMinimum(0.0)
            hist1.SetTitle( title12Pt )
            hist2.SetTitle( title22Pt )
            hist1.Sumw2()
            hist2.Sumw2()
            hist2.SetMarkerSize(.6)
            hist1.SetMarkerSize(.6)
            nbins = hist1.GetXaxis().GetNbins()
            #hist1.GetXaxis().SetMaximum(GetBinCenter(nbins))
            #print ' nbins= ' + str(nbins)

            hist3 = ROOT.TH1F(algos[iinfile] + '_' + EtaRegions[EtaReg] + '_' + canvname + 'RES',algos[iinfile] + '_' + EtaRegions[EtaReg] + '_' + canvname + 'RES',nbins,hist1.GetXaxis().GetBinCenter(0),hist1.GetXaxis().GetBinCenter(nbins))

            for n in range(nbins) :
                rms = hist2.GetBinContent(n)
                mean = hist1.GetBinContent(n)
                rmsErr = hist2.GetBinError(n)
                meanErr = hist1.GetBinError(n)
                #x = hist1.GetXaxis().GetBinCenter(n)
            
                if mean != 0.0 :
                    hist3.SetBinContent( n, rms/mean)
                    hist3.SetBinError( n, ROOT.Math.sqrt( (rmsErr/mean)*(rmsErr/mean) + (((rms/mean)/mean)*meanErr)*(((rms/mean)/mean)*meanErr)))
        
        
            hist1.GetYaxis().SetTitleOffset( 1.2 )
            hist2.GetYaxis().SetTitleOffset( 1.2 )

            hist2.SetMarkerColor(colors2[nh])
            hist2.SetLineColor(colors2[nh])
            hist2.SetMarkerStyle(markers2[nh])
            hist2.SetTitle( title22Pt )
            #hist3.SetMaximum(0.7)
            #hist3.SetMinimum(0.001)



            if ptresphists3[ihist] == 'p' :
                hist1.SetMaximum(pmax)
                hist1.SetMinimum(pmin)
                hist2.SetMaximum(pmaxR)
                hist2.SetMinimum(pminR)                  
            elif ptresphists3[ihist] == 'm' :
                hist1.SetMaximum(mmax)
                hist1.SetMinimum(mmin)
                hist2.SetMaximum(mmaxR)
                hist2.SetMinimum(mminR)  
            elif ptresphists3[ihist] == 'a' :
                hist1.SetMaximum(amax)
                hist1.SetMinimum(amin)
                hist2.SetMaximum(amaxR)
                hist2.SetMinimum(aminR)  
            else :
                print "not sure of response type, skipping "
                continue

            allhists.append( hist1 )
            allhists.append( hist2 )
        
            allhists.append( hist3 ) 
        
            leg.AddEntry( hist1, PtBin[nh], 'p')

            canv.cd(1)
            if nh == 0 : 
                hist1.Draw()
            else :
                hist1.Draw('same')
            canv.cd(2)
            if nh == 0 : 
                hist2.Draw('E')
            else :
                hist2.Draw('Esame')

            if nh == 3 :
                canv.cd(1)
                leg.Draw()
                legs2.append(leg)
                canv.Draw()
                #canvs2.append(canv)
                canv.Print('pngs/' +  EtaRegions[EtaReg] + '/PtBinned/' + algos[iinfile] + '_' + canv.GetName() + '_' + options.JetType + '_' + options.BX + '.png' )
#Algo Seperated
for EtaReg in xrange(len(EtaRegions)) :
    if options.PubPlots :
        continue
    for ihist,shist in enumerate( inhists2 ) :
        shistLFN = EtaRegions[EtaReg] + '/' + shist
        print 'processing shistLFN = ' + shistLFN
        if ihist%4 == 0 :
            canv = ROOT.TCanvas(shistLFN,shistLFN, 1600, 800)
            canv.Divide(2,4)

            leg = ROOT.TLegend(0.7, 0.5, 1.15, 0.85)    
            leg.SetFillColor(0)
            leg.SetBorderSize(0)
        for iinfile,infile in enumerate(infiles) :
            print '   processing infile = ' + infile.GetName()
            ROOT.gStyle.SetLabelSize( .065, "xyz")

            #ROOT.gStyle.SetTitleSize( .12 )
            hist = infile.Get(shistLFN)
            allhists.append( hist )
            hist.FitSlicesY()
            hist1 = ROOT.gDirectory.Get( shist + '_1')
            hist2 = ROOT.gDirectory.Get( shist + '_2')
            hist1.SetName( 'proj1y_' + shist + '_' + infile.GetName() )
            hist2.SetName( 'proj2y_' + shist + '_' + infile.GetName() )
            hist1.SetMarkerColor(colors[iinfile])
            hist2.SetMarkerColor(colors[iinfile])
            hist1.SetLineColor(colors[iinfile])
            hist2.SetLineColor(colors[iinfile])
            hist1.SetMarkerStyle(markers[iinfile])
            hist2.SetMarkerStyle(markers[iinfile])        
            #hist1.SetMaximum(1.8)
            #hist1.SetMinimum(0.5)
            #hist2.SetMaximum(0.5)
            #hist2.SetMinimum(0.0)
            hist1.SetTitle( titles12[ihist] )
            hist2.SetTitle( titles22[ihist] )
            hist1.Sumw2()
            hist2.Sumw2()
            hist2.SetMarkerSize(.6)
            hist1.SetMarkerSize(.6)
            hist1.GetXaxis().SetTitleSize( .051 )
            hist2.GetXaxis().SetTitleSize( .051 )
            hist1.GetYaxis().SetTitleSize( .061 )
            hist2.GetYaxis().SetTitleSize( .061 )
            hist1.GetXaxis().SetTitleOffset( .97 )
            hist1.GetYaxis().SetTitleOffset( .38 )
            hist2.GetXaxis().SetTitleOffset( .97 )
            hist2.GetYaxis().SetTitleOffset( .38 ) 

            nbins = hist1.GetXaxis().GetNbins()
            #hist1.GetXaxis().SetRange( 0, hist1.GetXaxis().GetMaximum() )
            #print ' nbins= ' + str(nbins)
            hist3 = ROOT.TH1F("Resolution" + shistLFN,"Resolution" + shistLFN,nbins,hist1.GetXaxis().GetBinCenter(0),hist1.GetXaxis().GetBinCenter(nbins))    
            for n in range(nbins) :
                rms = hist2.GetBinContent(n)
                mean = hist1.GetBinContent(n)
                rmsErr = hist2.GetBinError(n)
                meanErr = hist1.GetBinError(n)
                #x = hist1.GetXaxis().GetBinCenter(n)
                if mean != 0.0 :
                    hist3.SetBinContent( n, rms/mean)
                    hist3.SetBinError( n, ROOT.Math.sqrt( (rmsErr/mean)*(rmsErr/mean) + (((rms/mean)/mean)*meanErr)*(((rms/mean)/mean)*meanErr)))

        

            hist2.SetMarkerColor(colors2[iinfile])
            hist2.SetLineColor(colors2[iinfile])
            hist2.SetMarkerStyle(markers2[iinfile])
            #hist2.SetTitle( titles22[ihist] )


            if ptresphists2[ihist] == 'p' :
                hist1.SetMaximum(pmax)
                hist1.SetMinimum(pmin)
                hist2.SetMaximum(pmaxR)
                hist2.SetMinimum(pminR) 
            elif ptresphists2[ihist] == 'm' :
                hist1.SetMaximum(mmax)
                hist1.SetMinimum(mmin)
                hist2.SetMaximum(mmaxR)
                hist2.SetMinimum(mminR) 
            elif ptresphists2[ihist] == 'a' :
                hist1.SetMaximum(amax)
                hist1.SetMinimum(amin)
                hist2.SetMaximum(amaxR)
                hist2.SetMinimum(aminR) 
            else :
                print "not sure of response type, skipping "
                continue

        
            allhists.append( hist1 )
            allhists.append( hist2 )
            allhists.append( hist3 )
            if ihist%4 == 0 :
                leg.AddEntry( hist1, algos[iinfile], 'p')

            canv.cd((2*ihist + 1)%8)
            if iinfile == 0 : 
                hist1.Draw()
            else :
                hist1.Draw('same')
            canv.cd((2*ihist)%8 + 2)
            if iinfile == 0 : 
                hist2.Draw('E')
            else :
                hist2.Draw('Esame')

        if ihist%4 == 3 :
            canv.cd(1)
            leg.Draw()
            legs2.append(leg)
            canv.Draw()
            #canvs2.append(canv)
            canv.Print('pngs/' + canv.GetName() + '_' + options.JetType + '_' + options.BX + '.png' )
            

#!!!!CUSTOM PLOTTING pt binned response versus NPV, NPV binned response versus pt for CHS and PUPPI














inhistsC = [
'h_pt_mresponse_npvb','h_pt_mresponse_npvb2','h_pt_mresponse_npvb3','h_pt_mresponse_npvb4',
'h_pt_ptresponse_anpvb', 'h_pt_ptresponse_anpvb2', 'h_pt_ptresponse_anpvb3', 'h_pt_ptresponse_anpvb4', 
]

inhists2C = ['h_NPV_ptresponse_aptb','h_NPV_ptresponse_aptb2', 'h_NPV_mresponse_ptb', 'h_NPV_mresponse_ptb2']

Ctitles1PU= [
             'Pileup Binned;p_{T}^{GEN};Mean of (m^{RECO} - m^{GEN})',
             'Pileup Binned;p_{T}^{GEN};Mean of (m^{RECO} - m^{GEN})',
             'Pileup Binned;p_{T}^{GEN};Mean of (m^{RECO} - m^{GEN})',
             'Pileup Binned;p_{T}^{GEN};Mean of (m^{RECO} - m^{GEN})',
             'Pileup Binned;p_{T}^{GEN};Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
             'Pileup Binned;p_{T}^{GEN};Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
             'Pileup Binned;p_{T}^{GEN};Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
             'Pileup Binned;p_{T}^{GEN};Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ]
Ctitles2PU= [
           ';p_{T}^{GEN};Resolution of (m^{RECO} - m^{GEN})',
           ';p_{T}^{GEN};Resolution of (m^{RECO} - m^{GEN})',
           ';p_{T}^{GEN};Resolution of (m^{RECO} - m^{GEN})',
           ';p_{T}^{GEN};Resolution of (m^{RECO} - m^{GEN})',
           
           ';p_{T}^{GEN};Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ';p_{T}^{GEN};Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ';p_{T}^{GEN};Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ';p_{T}^{GEN};Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ]


Ctitles1Pt= [
             'p_{T} Binned;N_{VTX};Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
             'p_{T} Binned;N_{VTX};Mean of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
             'p_{T} Binned;N_{VTX};Mean of (m^{RECO} - m^{GEN})',
             'p_{T} Binned;N_{VTX};Mean of (m^{RECO} - m^{GEN})',
           ]


Ctitles2Pt = [
           ';N_{VTX};Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ';N_{VTX};Resolution of (p_{T}^{RECO} - p_{T}^{GEN})/p_{T}^{GEN}',
           ';N_{VTX};Resolution of (m^{RECO} - m^{GEN})',
           ';N_{VTX};Resolution of (m^{RECO} - m^{GEN})'
           ]


Cptresphists1 = ['m','m','m','m', 'a','a','a','a' ]
Cptresphists2 = ['a','a',  'm','m']

colorsC = [8,2,4,6,3,5,7,1,9,10,11,12]
markersC = [20,21,22,23,24,25,26,27,28,29,30,31,32]
infiles2 = []


algos2 = [ 'PFCHS', 'PFPUPPI']
for ialgo,algo in enumerate( algos2 ): 
    infiles2.append( ROOT.TFile( 'outplots_' + options.sample + '_' + options.JetType + algo + '.root' ) )



  
for EtaReg in xrange(len(EtaRegions)) :
    if EtaReg == 0 :
        PUBin = [ str(BPVb1) + ' to ' + str(BPVb2) + ' PV', str(BPVb2) + ' to ' + str(BPVb3), str(BPVb3) + ' to ' + str(BPVb4), str(BPVb4) + ' to ' + str(BPVb5) ]
    elif EtaReg == 1 :
        PUBin = [ str(PVb1) + ' to ' + str(PVb2) + ' PV', str(PVb2) + ' to ' + str(PVb3), str(PVb3) + ' to ' + str(PVb4), str(PVb4) + ' to ' + str(PVb5) ]
    elif EtaReg == 2 :
        PUBin = [ str(PPVb1) + ' to ' + str(PPVb2) + ' PV', str(PPVb2) + ' to ' + str(PPVb3), str(PPVb3) + ' to ' + str(PPVb4), str(PPVb4) + ' to ' + str(PPVb5) ]
    else :
        PUBin = [ str(FPVb1) + ' to ' + str(FPVb2) + ' PV', str(FPVb2) + ' to ' + str(FPVb3), str(FPVb3) + ' to ' + str(FPVb4), str(FPVb4) + ' to ' + str(FPVb5) ]
    for ihist,shist in enumerate( inhistsC ) :
        canvname = EtaRegions[EtaReg] + '_' + shist + '_PUBinned'
        nh = ihist%4
        if nh == 0 :
            canv = ROOT.TCanvas(canvname,canvname, 1600, 800)
            canv2 = ROOT.TCanvas(canvname + "_RES" , canvname + "_RES" , 1600, 800)
            leg = ROOT.TLegend(0.78, 0.70, 0.9, 0.89)    
            leg.SetFillColor(0)
            leg.SetBorderSize(0)
            leg.SetHeader("PFCHS")
            leg2 = ROOT.TLegend(0.66, 0.70, 0.78, 0.89)    
            leg2.SetFillColor(0)
            leg2.SetBorderSize(0)
            leg2.SetHeader("PUPPI")
        for iinfile,infile in enumerate(infiles2) :
            print 'processing shist = ' + canvname
                
            ROOT.gStyle.SetLabelSize( .045, "xyz")
            
            if EtaReg == 0 :
                title12PU = EtaRegions[EtaReg] + " (0-1.479 eta) " + Ctitles1PU[ihist]
                title22PU = EtaRegions[EtaReg] + " (0-1.479 eta) " + Ctitles2PU[ihist]
            elif EtaReg == 1 :
                title12PU = EtaRegions[EtaReg] + " (1.479-2.5 eta) " + Ctitles1PU[ihist]
                title22PU = EtaRegions[EtaReg] + " (1.479-2.5 eta) " + Ctitles2PU[ihist]
            elif EtaReg == 2 :
                title12PU = EtaRegions[EtaReg] + " (2.5-3.0 eta) " + Ctitles1PU[ihist]
                title22PU = EtaRegions[EtaReg] + " (2.5-3.0 eta) " + Ctitles2PU[ihist]
            else:
                title12PU = EtaRegions[EtaReg] + " (3.0-10.0 eta) " + Ctitles1PU[ihist]
                title22PU = EtaRegions[EtaReg] + " (3.0-10.0 eta) " + Ctitles2PU[ihist]

            hist = infile.Get( EtaRegions[EtaReg] + '/' + shist)
            allhists.append( hist )
            hist.FitSlicesY()
            hist1 = ROOT.gDirectory.Get( shist + '_1')
            hist2 = ROOT.gDirectory.Get( shist + '_2')
            hist1.SetName( 'proj1y_' + shist + '_' + infile.GetName() )
            hist2.SetName( 'proj2y_' + shist + '_' + infile.GetName() )
            hist1.SetMarkerColor(colorsC[iinfile + nh*2])
            hist2.SetMarkerColor(colorsC[iinfile + nh*2])
            hist1.SetLineColor(colorsC[iinfile + nh*2])
            hist2.SetLineColor(colorsC[iinfile + nh*2])
            hist1.SetMarkerStyle(markersC[iinfile+ 2*nh])
            hist2.SetMarkerStyle(markersC[iinfile + 2*nh])        
            hist2.SetMarkerSize(.6)
            hist1.SetMarkerSize(.6)
            
            hist1.SetTitle( title12PU )
            hist2.SetTitle( title22PU )
            
            hist1.Sumw2()
            hist2.Sumw2()

            hist1.GetYaxis().SetTitleOffset( 1.2 )
            hist2.GetYaxis().SetTitleOffset( 1.2 )
            hist1.GetXaxis().SetTitleSize( .043 )
            hist2.GetXaxis().SetTitleSize( .043 )
            hist1.GetYaxis().SetTitleSize( .043 )
            hist2.GetYaxis().SetTitleSize( .043 )

            if Cptresphists1[ihist] == 'p' :
                hist1.SetMaximum(pmax)
                hist1.SetMinimum(pmin)
                hist2.SetMaximum(pmaxR)
                hist2.SetMinimum(pminR)                
            elif Cptresphists1[ihist] == 'm' :
                hist1.SetMaximum(15)
                hist1.SetMinimum(-15)
                hist2.SetMaximum(15)
                hist2.SetMinimum(0)
            elif Cptresphists1[ihist] == 'a' :
                hist1.SetMaximum(0.2)
                hist1.SetMinimum(-0.2)
                hist2.SetMaximum(0.2)
                hist2.SetMinimum(0.0)
            else :
                print "not sure of response type, skipping "
                continue


            allhists.append( hist1 )
            allhists.append( hist2 )
            if iinfile == 0 :
                leg.AddEntry( hist1, PUBin[nh], 'p')
            else :
                leg2.AddEntry( hist1, PUBin[nh], 'p')

                
            canv.cd()
            if nh == 0 and iinfile == 0 : 
                hist1.Draw()
            else :
                hist1.Draw('same')
            canv2.cd()
            if nh == 0 and iinfile == 0 : 
                hist2.Draw('E')
            else :
                hist2.Draw('Esame')

        if nh == 3 :
            canv.cd()
            leg.Draw()
            leg2.Draw()
            legs2.append(leg)
            legs2.append(leg2)
            canv.Draw()
            
            canv.Print('pngs/' +  EtaRegions[EtaReg] + '/CustomPlot_' + algos[iinfile] + '_' + canv.GetName() + '_' + options.JetType + '_' + options.BX + '.png' )

            canv2.cd()
            leg.Draw()
            leg2.Draw()
            #legs2.append(leg)
            canv2.Draw()
            
            canv2.Print('pngs/' +  EtaRegions[EtaReg] + '/CustomPlot_' + algos[iinfile] + '_' + canv.GetName() + '_' + options.JetType + '_' + options.BX + '_RES.png' )


#!!! Pt Binned Customs
for EtaReg in xrange(len(EtaRegions)) :
    if EtaReg == 0 :
        PtBin = [ str(BPtb1) + ' to ' + str(BPtb2) + ' GeV', str(BPtb2) + ' to ' + str(BPtb3), str(BPtb3) + ' to ' + str(BPtb4), str(BPtb4) + ' to ' + str(BPtb5) ]
    elif EtaReg == 1 :
        PtBin = [ str(Ptb1) + ' to ' + str(Ptb2) + ' GeV', str(Ptb2) + ' to ' + str(Ptb3), str(Ptb3) + ' to ' + str(Ptb4), str(Ptb4) + ' to ' + str(Ptb5) ]
    elif EtaReg == 2 :
        PtBin = [ str(PPtb1) + ' to ' + str(PPtb2) + ' GeV', str(PPtb2) + ' to ' + str(PPtb3), str(PPtb3) + ' to ' + str(PPtb4), str(PPtb4) + ' to ' + str(PPtb5) ]
    else :
        PtBin = [ str(FPtb1) + ' to ' + str(FPtb2) + ' GeV', str(FPtb2) + ' to ' + str(FPtb3), str(FPtb3) + ' to ' + str(FPtb4), str(FPtb4) + ' to ' + str(FPtb5) ]
    for ihist,shist in enumerate( inhists2C ) :
        canvname = EtaRegions[EtaReg] + '_' + shist + '_PtBinned'
        nh = ihist%2
        if nh == 0 :
            canv = ROOT.TCanvas(canvname,canvname, 1600, 800)
            canv2 = ROOT.TCanvas(canvname + "_RES" , canvname + "_RES" , 1600, 800)
            leg = ROOT.TLegend(0.8, 0.77, 0.9, 0.89)    
            leg.SetFillColor(0)
            leg.SetBorderSize(0)
            leg.SetHeader("PFCHS")
            leg2 = ROOT.TLegend(0.7, 0.77, 0.8, 0.89)    
            leg2.SetFillColor(0)
            leg2.SetBorderSize(0)
            leg2.SetHeader("PUPPI")
        for iinfile,infile in enumerate(infiles2) :
            print 'processing shist = ' + canvname
                
            ROOT.gStyle.SetLabelSize( .045, "xyz")
            
            if EtaReg == 0 :
                title12Pt = EtaRegions[EtaReg] + " (0-1.479 eta) " + Ctitles1Pt[ihist]
                title22Pt = EtaRegions[EtaReg] + " (0-1.479 eta) " + Ctitles2Pt[ihist]
            elif EtaReg == 1 :
                title12Pt = EtaRegions[EtaReg] + " (1.479-2.5 eta) " + Ctitles1Pt[ihist]
                title22Pt = EtaRegions[EtaReg] + " (1.479-2.5 eta) " + Ctitles2Pt[ihist]
            elif EtaReg == 2 :
                title12Pt = EtaRegions[EtaReg] + " (2.5-3.0 eta) " + Ctitles1Pt[ihist]
                title22Pt = EtaRegions[EtaReg] + " (2.5-3.0 eta) " + Ctitles2Pt[ihist]
            else:
                title12Pt = EtaRegions[EtaReg] + " (3.0-10.0 eta) " + Ctitles1Pt[ihist]
                title22Pt = EtaRegions[EtaReg] + " (3.0-10.0 eta) " + Ctitles2Pt[ihist]

            hist = infile.Get( EtaRegions[EtaReg] + '/' + shist)
            allhists.append( hist )
            hist.FitSlicesY()
            hist1 = ROOT.gDirectory.Get( shist + '_1')
            hist2 = ROOT.gDirectory.Get( shist + '_2')
            hist1.SetName( 'proj1y_' + shist + '_' + infile.GetName() )
            hist2.SetName( 'proj2y_' + shist + '_' + infile.GetName() )
            hist1.SetMarkerColor(colorsC[iinfile + nh*2])
            hist2.SetMarkerColor(colorsC[iinfile + nh*2])
            hist1.SetLineColor(colorsC[iinfile + nh*2])
            hist2.SetLineColor(colorsC[iinfile + nh*2])
            hist1.SetMarkerStyle(markersC[iinfile+ 2*nh])
            hist2.SetMarkerStyle(markersC[iinfile + 2*nh])        
            hist2.SetMarkerSize(.6)
            hist1.SetMarkerSize(.6)
            
            hist1.SetTitle( title12Pt )
            hist2.SetTitle( title22Pt )
            hist1.GetXaxis().SetTitleSize( .043 )
            hist2.GetXaxis().SetTitleSize( .043 )
            hist1.GetYaxis().SetTitleSize( .043 )
            hist2.GetYaxis().SetTitleSize( .043 )


            hist1.Sumw2()
            hist2.Sumw2()

            hist1.GetYaxis().SetTitleOffset( 1.2 )
            hist2.GetYaxis().SetTitleOffset( 1.2 )

            if Cptresphists2[ihist] == 'p' :
                hist1.SetMaximum(pmax)
                hist1.SetMinimum(pmin)
                hist2.SetMaximum(pmaxR)
                hist2.SetMinimum(pminR)                
            elif Cptresphists2[ihist] == 'm' :
                hist1.SetMaximum(15)
                hist1.SetMinimum(-15)
                hist2.SetMaximum(15)
                hist2.SetMinimum(0)
            elif Cptresphists2[ihist] == 'a' :
                hist1.SetMaximum(0.20)
                hist1.SetMinimum(-0.20)
                hist2.SetMaximum(0.2)
                hist2.SetMinimum(0.0)
            else :
                print "not sure of response type, skipping "
                continue


            allhists.append( hist1 )
            allhists.append( hist2 )
            if iinfile == 0 :
                leg.AddEntry( hist1, PtBin[nh], 'p')
            else :
                leg2.AddEntry( hist1, PtBin[nh], 'p')

                
            canv.cd()
            if nh == 0 and iinfile == 0 : 
                hist1.Draw()
            else :
                hist1.Draw('same')
            canv2.cd()
            if nh == 0 and iinfile == 0 : 
                hist2.Draw('E')
            else :
                hist2.Draw('Esame')

        if nh == 1 :
            canv.cd()
            leg.Draw()
            leg2.Draw()
            legs2.append(leg)
            legs2.append(leg2)
            canv.Draw()
            
            canv.Print('pngs/' +  EtaRegions[EtaReg] + '/CustomPlot_' + algos[iinfile] + '_' + canv.GetName() + '_' + options.JetType + '_' + options.BX + '.png' )

            canv2.cd()
            leg.Draw()
            leg2.Draw()
            legs2.append(leg)
            canv2.Draw()
            
            canv2.Print('pngs/' +  EtaRegions[EtaReg] + '/CustomPlot_' + algos[iinfile] + '_' + canv.GetName() + '_' + options.JetType + '_' + options.BX + '_RES.png' )
