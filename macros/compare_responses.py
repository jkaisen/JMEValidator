#!/usr/bin/env python


import ROOT

ROOT.gStyle.SetOptStat(000000)
ROOT.gROOT.Macro("rootlogon.C")

ROOT.gROOT.ForceStyle()

f = ROOT.TFile("outplots_qcd_AK4PFchs.root")

release = '7.4.0pre9'

styles = [ 20, 24, 21, 25, 22 ]
colors = [ ROOT.kGreen+2, ROOT.kBlack, ROOT.kOrange-3, ROOT.kBlue, ROOT.kRed+1]
titles = [
    'p_{T} = 10 GeV',
    'p_{T} = 30 GeV',
    'p_{T} = 100 GeV',
    'p_{T} = 400 GeV',
    'p_{T} = 2000 GeV',
    ]

pthistnames = [
    'h_pt_etaresponse_pt10_30',
    'h_pt_etaresponse_pt30_100',
    'h_pt_etaresponse_pt100_400',
    'h_pt_etaresponse_pt400_2000',
    'h_pt_etaresponse_pt2000_inf',
  ]

mhistnames = [
    'h_m_etaresponse_pt10_30',
    'h_m_etaresponse_pt30_100',
    'h_m_etaresponse_pt100_400',
    'h_m_etaresponse_pt400_2000',
    'h_m_etaresponse_pt2000_inf',
    ]

cpt = ROOT.TCanvas('cpt','cpt')

pthists = []
ptprofs = []

ptleg = ROOT.TLegend(0.2,0.16, 0.84, 0.3)
ptleg.SetFillColor(0)
ptleg.SetBorderSize(0)
ptleg.SetNColumns(2)

for i,s in enumerate(pthistnames) :
    h = f.Get(s)
    h.SetMarkerStyle( styles[i] )
    h.SetMarkerColor( colors[i] )
    h.SetLineColor( colors[i] )
    px = h.ProfileX()
    pthists.append( h )
    ptprofs.append(px)


for index in [0, 3, 1, 4, 2] :
    ptleg.AddEntry( ptprofs[index], titles[index], 'p')


for iprof, prof in enumerate(ptprofs) :
    if iprof == 0 :
        prof.Draw()
        prof.SetMaximum(1.3)
        prof.SetMinimum(0.5)
        prof.SetTitle( release + ';|#eta^{GEN}|;Simulated Jet p_{T} Response')
    else :
        prof.Draw('same')

ptleg.Draw()
cpt.Print('ptresponse_' + release + '.png', "png")
cpt.Print('ptresponse_' + release + '.pdf', "pdf")
        
cm = ROOT.TCanvas('cm','cm')

mhists = []
mprofs = []

mleg = ROOT.TLegend(0.2,0.16, 0.84, 0.3)
mleg.SetFillColor(0)
mleg.SetBorderSize(0)
mleg.SetNColumns(2)

for i,s in enumerate(mhistnames) :
    h = f.Get(s)
    h.SetMarkerStyle( styles[i] )
    h.SetMarkerColor( colors[i] )
    h.SetLineColor( colors[i] )
    px = h.ProfileX()
    mhists.append( h )    
    mprofs.append(px)

for index in [0, 3, 1, 4, 2] :
    mleg.AddEntry( mprofs[index], titles[index], 'p')


for iprof, prof in enumerate(mprofs) :
    if iprof == 0 :
        prof.Draw()
        prof.SetMaximum(2.0)
        prof.SetMinimum(0.0)
        prof.SetTitle( release + ';|#eta^{GEN}|;Simulated Jet Mass Response')
    else :
        prof.Draw('same')

mleg.Draw()
cm.Print('mresponse_' + release + '.png', "png")
cm.Print('mresponse_' + release + '.pdf', "pdf")
