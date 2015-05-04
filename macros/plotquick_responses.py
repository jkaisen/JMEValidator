#!/usr/bin/env python
from optparse import OptionParser
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
 
(options, args) = parser.parse_args()
argv = []

import ROOT

ROOT.gStyle.SetOptStat(000000)
ROOT.gROOT.Macro("rootlogon.C")

algos = [ 'PFchs', 'PUPPI', 'SK' ]
colors = [1, 2, 4]
markers = [20,21,22]
inhists = [ 'h_pt_ptresponse0', 'h_pt_etaresponse0', 'h_m_mresponse0', 'h_m_ptresponse0', 'h_m_etaresponse0' ]
inhists2 = ['h_pt_ptresponse_npv10_20', 'h_pt_ptresponse_npv20_30', 'h_pt_ptresponse_npv30_40', 'h_pt_ptresponse_npv40_50', 'h_m_ptresponse_npv10_20','h_m_ptresponse_npv20_30','h_m_ptresponse_npv30_40','h_m_ptresponse_npv40_50','h_m_mresponse_npv10_20','h_m_mresponse_npv20_30','h_m_mresponse_npv30_40','h_m_mresponse_npv40_50','h_pt_mresponse_npv10_20','h_pt_mresponse_npv20_30','h_pt_mresponse_npv30_40','h_pt_mresponse_npv40_50'
 ]
titles1 = [';p_{T}^{GEN};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
           ';y^{GEN};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
           ';m^{GEN};Mean of m^{RECO}/m^{GEN}',
           ';p_{T}^{GEN};Mean of m^{RECO}/m^{GEN}',
           ';y^{GEN};Mean of m^{RECO}/m^{GEN}']
titles12= [';p_{T}^{GEN};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
           ';p_{T}^{GEN};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
           ';p_{T}^{GEN};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
           ';p_{T}^{GEN};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
           ';m^{GEN};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
           ';m^{GEN};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
           ';m^{GEN};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
           ';m^{GEN};Mean of p_{T}^{RECO}/p_{T}^{GEN}',
           ';m^{GEN};Mean of m^{RECO}/m^{GEN}',
           ';m^{GEN};Mean of m^{RECO}/m^{GEN}',
           ';m^{GEN};Mean of m^{RECO}/m^{GEN}',
           ';m^{GEN};Mean of m^{RECO}/m^{GEN}',
           ';p_{T}^{GEN};Mean of m^{RECO}/m^{GEN}',
           ';p_{T}^{GEN};Mean of m^{RECO}/m^{GEN}',
           ';p_{T}^{GEN};Mean of m^{RECO}/m^{GEN}',
           ';p_{T}^{GEN};Mean of m^{RECO}/m^{GEN}',
           ]
titles2 = [';p_{T}^{GEN};Width of p_{T}^{RECO}/p_{T}^{GEN}',
           ';y^{GEN};Width of p_{T}^{RECO}/p_{T}^{GEN}',
           ';m^{GEN};Width of m^{RECO}/m^{GEN}',
           ';p_{T}^{GEN};Width of m^{RECO}/m^{GEN}',
           ';y^{GEN};Width of m^{RECO}/m^{GEN}']
titles22= [';p_{T}^{GEN};Width of p_{T}^{RECO}/p_{T}^{GEN}',
           ';p_{T}^{GEN};Width of p_{T}^{RECO}/p_{T}^{GEN}',
           ';p_{T}^{GEN};Width of p_{T}^{RECO}/p_{T}^{GEN}',
           ';p_{T}^{GEN};Width of p_{T}^{RECO}/p_{T}^{GEN}',
           ';m^{GEN};Width of p_{T}^{RECO}/p_{T}^{GEN}',
           ';m^{GEN};Width of p_{T}^{RECO}/p_{T}^{GEN}',
           ';m^{GEN};Width of p_{T}^{RECO}/p_{T}^{GEN}',
           ';m^{GEN};Width of p_{T}^{RECO}/p_{T}^{GEN}',
           ';m^{GEN};Width of m^{RECO}/m^{GEN}',
           ';m^{GEN};Width of m^{RECO}/m^{GEN}',
           ';m^{GEN};Width of m^{RECO}/m^{GEN}',
           ';m^{GEN};Width of m^{RECO}/m^{GEN}',
           ';p_{T}^{GEN};Width of m^{RECO}/m^{GEN}',
           ';p_{T}^{GEN};Width of m^{RECO}/m^{GEN}',
           ';p_{T}^{GEN};Width of m^{RECO}/m^{GEN}',
           ';p_{T}^{GEN};Width of m^{RECO}/m^{GEN}',
           ]

infiles = []


for ialgo,algo in enumerate( algos ): 
    infiles.append( ROOT.TFile( 'outplots_' + options.sample + '_' + options.JetType + algo + '.root' ) )


allhists = []
canvs = []
legs = []
for ihist,shist in enumerate( inhists ) :
    print 'processing shist = ' + shist
    canv = ROOT.TCanvas(shist,shist, 1600, 800)
    canv.Divide(2,1)
    leg = ROOT.TLegend(0.6, 0.6, 0.85, 0.85)
    
    leg.SetFillColor(0)
    leg.SetBorderSize(0)
    for iinfile,infile in enumerate(infiles) :
        print '   processing infile = ' + infile.GetName()

        hist = infile.Get(shist)
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
        hist1.SetMaximum(2.5)
        hist1.SetMinimum(0.5)
        hist2.SetMaximum(2.5)
        hist2.SetMinimum(0.0)
        hist1.SetTitle( titles1[ihist] )
        hist2.SetTitle( titles2[ihist] )
        allhists.append( hist1 )
        allhists.append( hist2 )
        leg.AddEntry( hist1, algos[iinfile], 'p')

        canv.cd(1)
        if iinfile == 0 : 
            hist1.Draw()
        else :
            hist1.Draw('same')
        canv.cd(2)
        if iinfile == 0 : 
            hist2.Draw()
        else :
            hist2.Draw('same')

    canv.cd(1)
    leg.Draw()
    legs.append(leg)
    canv.Draw()
    canvs.append(canv)
    canv.Print('pngs/' + canv.GetName() + options.JetType + '_' + options.BX + '.png' )
    canv.Print('pdfs/' + canv.GetName() + options.JetType + '_' + options.BX + '.pdf' )


allhists2 = []
canvs2 = []
legs2 = []

for ihist,shist in enumerate( inhists2 ) :
    print 'processing shist = ' + shist
    if ihist%4 == 0 :
        canv = ROOT.TCanvas(shist,shist, 1600, 800)
        canv.Divide(2,4)

    leg = ROOT.TLegend(0.6, 0.6, 0.85, 0.85)    
    leg.SetFillColor(0)
    leg.SetBorderSize(0)
    for iinfile,infile in enumerate(infiles) :
        print '   processing infile = ' + infile.GetName()

        hist = infile.Get(shist)
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
        hist1.SetMaximum(2.5)
        hist1.SetMinimum(0.5)
        hist2.SetMaximum(2.5)
        hist2.SetMinimum(0.0)
        hist1.SetTitle( titles12[ihist] )
        hist2.SetTitle( titles22[ihist] )
        allhists.append( hist1 )
        allhists.append( hist2 )
        leg.AddEntry( hist1, algos[iinfile], 'p')

        canv.cd((2*ihist + 1)%8)
        if iinfile == 0 : 
            hist1.Draw()
        else :
            hist1.Draw('same')
        canv.cd((2*ihist)%8 + 2)
        if iinfile == 0 : 
            hist2.Draw()
        else :
            hist2.Draw('same')


    if ihist%4 == 3 :
        canv.cd(1)
        leg.Draw()
        legs2.append(leg)
        canv.Draw()
        canvs2.append(canv)
        canv.Print('pngs/' + canv.GetName() + '_' + options.JetType + '_' + options.BX + '.png' )
        canv.Print('pdfs/' + canv.GetName() + '_' + options.JetType + '_' + options.BX + '.pdf' )
    
