#!/usr/bin/env python
# Ripped and adapted from http://wlav.web.cern.ch/wlav/pyroot/tpytree.html

from optparse import OptionParser
parser = OptionParser()

parser.add_option('--infile', metavar='F', type='string', action='store',
                  dest='infile',
                  default='test_qcd.root',
                  help='Input file')

parser.add_option('--algo', metavar='F', type='string', action='store',
                  default='AK4PFchs',
                  dest='algo',
                  help='Algorithm to use. Options are AK4PFchs, AK4PUPPI, AK4SK, and also for AK8')


parser.add_option('--sample', metavar='F', type='string', action='store',
                  default='qcd',
                  dest='sample',
                  help='Sample, only used for output root file name')

parser.add_option('--dynamic', '--db',
                  action='store_true',
                  default=False,
                  dest='dynamicBin',
                  help='Dynamic binning based on events per bin')

(options, args) = parser.parse_args()
argv = []



import ROOT
import array

# open the file
tree = ROOT.TChain( 'nt_' + options.algo + '/t' )

tree.Add( options.infile )


if '4' in options.algo :
    R = 0.4
else :
    R = 0.8
    
entries = tree.GetEntries()

# Get the AK8 jets
jets_pt = ROOT.std.vector('float')()
jets_eta = ROOT.std.vector('float')()
jets_phi = ROOT.std.vector('float')()
jets_e = ROOT.std.vector('float')()
jets_jec = ROOT.std.vector('float')()
genjets_pt = ROOT.std.vector('float')()
genjets_eta = ROOT.std.vector('float')()
genjets_phi = ROOT.std.vector('float')()
genjets_e = ROOT.std.vector('float')()

npv = array.array('I',[0])

# Turn off all branches but the ones we want

tree.SetBranchAddress('jtpt', jets_pt)
tree.SetBranchAddress('jteta', jets_eta)
tree.SetBranchAddress('jtphi', jets_phi)
tree.SetBranchAddress('jte', jets_e)
tree.SetBranchAddress('jtjec', jets_jec)
tree.SetBranchAddress('refpt', genjets_pt)
tree.SetBranchAddress('refeta', genjets_eta)
tree.SetBranchAddress('refphi', genjets_phi)
tree.SetBranchAddress('refe', genjets_e)
tree.SetBranchAddress('npv', npv)


# get a file to write hists to
f = ROOT.TFile("outplots_" + options.sample + "_" + options.algo + ".root", "RECREATE")

# Make histograms
h_pt0 = ROOT.TH1F("h_pt0", "Leading Jet p_{T};p_{T} (GeV);Number", 300, 0, 3000)
h_pt_ptresponse0 = ROOT.TH2F('h_pt_ptresponse0', 'p_{T}^{RECO} / p_{T}^{GEN};p_{T}^{GEN}', 150, 0, 1500, 25, 0, 2.5 )
h_pt_etaresponse0 = ROOT.TH2F('h_pt_etaresponse0', 'p_{T}^{RECO} / p_{T}^{GEN};#eta^{GEN}', 50, -5.0, 5.0, 25, 0, 2.5 )

h_m0 = ROOT.TH1F("h_m0", "Leading Jet m;m (GeV);Number", 250, 0, 500)
h_m_mresponse0 = ROOT.TH2F('h_m_mresponse0', 'm^{RECO} / m^{GEN};m^{GEN}', 25, 0, 250, 25, 0, 2.5 )
h_m_ptresponse0 = ROOT.TH2F('h_m_ptresponse0', 'm^{RECO} / m^{GEN};p_{T}^{GEN}', 50, 0, 1500, 25, 0, 2.5 )
h_m_etaresponse0 = ROOT.TH2F('h_m_etaresponse0', 'm^{RECO} / m^{GEN};#eta^{GEN}', 50, -5.0, 5.0, 25, 0, 2.5 )

h_rho0 = ROOT.TH1F("h_rho0", "Leading Jet #left(#frac{m}{p_{T}R}#right)^{2};#rho;Number", 250, 0, 1.0)
h_rho_rhoresponse0 = ROOT.TH2F("h_rho_rhoresponse0", "Leading Jet #left(#frac{m}{p_{T}R}#right)^{2} Response;#rho_{GEN};#rho_{RECO}/#rho{GEN}", 50, 0, 1, 25, 0, 2.5)


h_pt_etaresponse_pt10_30     = ROOT.TH2F('h_pt_etaresponse_pt10_30',    'p_{T}^{RECO} / p_{T}^{GEN};|#eta^{GEN}|', 50, 0.0, 5.0, 25, 0, 2.5 )
h_pt_etaresponse_pt30_100    = ROOT.TH2F('h_pt_etaresponse_pt30_100',   'p_{T}^{RECO} / p_{T}^{GEN};|#eta^{GEN}|', 50, 0.0, 5.0, 25, 0, 2.5 )
h_pt_etaresponse_pt100_400   = ROOT.TH2F('h_pt_etaresponse_pt100_400',  'p_{T}^{RECO} / p_{T}^{GEN};|#eta^{GEN}|', 50, 0.0, 5.0, 25, 0, 2.5 )
h_pt_etaresponse_pt400_2000  = ROOT.TH2F('h_pt_etaresponse_pt400_2000', 'p_{T}^{RECO} / p_{T}^{GEN};|#eta^{GEN}|', 50, 0.0, 5.0, 25, 0, 2.5 )
h_pt_etaresponse_pt2000_inf  = ROOT.TH2F('h_pt_etaresponse_pt2000_inf', 'p_{T}^{RECO} / p_{T}^{GEN};|#eta^{GEN}|', 50, 0.0, 5.0, 25, 0, 2.5 )
h_pt_etaresponse_npv10_20    = ROOT.TH2F('h_pt_etaresponse_npv10_20',   ';|#eta^{GEN}|;m^{RECO} / m^{GEN}', 25, 0.0, 5.0, 25, 0, 2.5 )
h_pt_etaresponse_npv20_30   = ROOT.TH2F('h_pt_etaresponse_npv20_30',  ';;|#eta^{GEN}|m^{RECO} / m^{GEN}', 25, 0.0, 5.0, 25, 0, 2.5 )
h_pt_etaresponse_npv30_40  = ROOT.TH2F('h_pt_etaresponse_npv30_40', ';|#eta^{GEN}|;m^{RECO} / m^{GEN}', 25, 0.0, 5.0, 25, 0, 2.5 )
h_pt_etaresponse_npv40_50  = ROOT.TH2F('h_pt_etaresponse_npv40_50', ';|#eta^{GEN}|;m^{RECO} / m^{GEN}', 25, 0.0, 5.0, 25, 0, 2.5 )

h_pt_etaresponses = [
    h_pt_etaresponse_pt10_30,
    h_pt_etaresponse_pt30_100,
    h_pt_etaresponse_pt100_400,
    h_pt_etaresponse_pt400_2000,
    h_pt_etaresponse_pt2000_inf,
    h_pt_etaresponse_npv10_20,
    h_pt_etaresponse_npv20_30,
    h_pt_etaresponse_npv30_40,
    h_pt_etaresponse_npv40_50
        ]

h_m_etaresponse_pt10_30     = ROOT.TH2F('h_m_etaresponse_pt10_30',    ';|#eta^{GEN}|;m^{RECO} / m^{GEN}', 50, 0.0, 5.0, 25, 0, 2.5 )
h_m_etaresponse_pt30_100    = ROOT.TH2F('h_m_etaresponse_pt30_100',   ';|#eta^{GEN}|;m^{RECO} / m^{GEN}', 50, 0.0, 5.0, 25, 0, 2.5 )
h_m_etaresponse_pt100_400   = ROOT.TH2F('h_m_etaresponse_pt100_400',  ';|#eta^{GEN}|;m^{RECO} / m^{GEN}', 50, 0.0, 5.0, 25, 0, 2.5 )
h_m_etaresponse_pt400_2000  = ROOT.TH2F('h_m_etaresponse_pt400_2000', ';|#eta^{GEN}|;m^{RECO} / m^{GEN}', 50, 0.0, 5.0, 25, 0, 2.5 )
h_m_etaresponse_pt2000_inf  = ROOT.TH2F('h_m_etaresponse_pt2000_inf', ';|#eta^{GEN}|;m^{RECO} / m^{GEN}', 50, 0.0, 5.0, 25, 0, 2.5 )
h_m_etaresponse_npv10_20    = ROOT.TH2F('h_m_etaresponse_npv10_20',   ';|#eta^{GEN}|;m^{RECO} / m^{GEN}', 25, 0.0, 5.0, 25, 0, 2.5 )
h_m_etaresponse_npv20_30   = ROOT.TH2F('h_m_etaresponse_npv20_30',  ';|#eta^{GEN}|;m^{RECO} / m^{GEN}', 25, 0.0, 5.0, 25, 0, 2.5 )
h_m_etaresponse_npv30_40  = ROOT.TH2F('h_m_etaresponse_npv30_40', ';|#eta^{GEN}|;m^{RECO} / m^{GEN}', 25, 0.0, 5.0, 25, 0, 2.5 )
h_m_etaresponse_npv40_50  = ROOT.TH2F('h_m_etaresponse_npv40_50', ';|#eta^{GEN}|;m^{RECO} / m^{GEN}', 25, 0.0, 5.0, 25, 0, 2.5 )

h_m_etaresponses = [
    h_m_etaresponse_pt10_30,
    h_m_etaresponse_pt30_100,
    h_m_etaresponse_pt100_400,
    h_m_etaresponse_pt400_2000,
    h_m_etaresponse_pt2000_inf,
    h_m_etaresponse_npv10_20,
    h_m_etaresponse_npv20_30,
    h_m_etaresponse_npv30_40,
    h_m_etaresponse_npv40_50
        ]
    #was 0 to 1500 and 0 to 100
h_pt_ptresponse_npv10_20 = ROOT.TH2F('h_pt_ptresponse_npv10_20', ';p_{T}^{GEN};p_{T}^{RECO} / p_{T}^{GEN}', 25, 0, 500, 25, 0, 2.5 )
h_m_ptresponse_npv10_20 = ROOT.TH2F('h_m_ptresponse_npv10_20', ';m_{T}^{GEN};p_{T}^{RECO} / p_{T}^{GEN}', 25, 0, 100, 25, 0, 2.5 )
h_m_mresponse_npv10_20 = ROOT.TH2F('h_m_mresponse_npv10_20', ';m^{GEN};m^{RECO} / m^{GEN}', 25, 0, 100, 25, 0, 2.5 )
h_pt_mresponse_npv10_20 = ROOT.TH2F('h_pt_mresponse_npv10_20', ';p_{T}^{GEN};m^{RECO} / m^{GEN}', 25, 0, 500, 25, 0, 2.5 )

h_pt_ptresponse_npv20_30 = ROOT.TH2F('h_pt_ptresponse_npv20_30', ';p_{T}^{GEN};p_{T}^{RECO} / p_{T}^{GEN}', 25, 0, 500, 25, 0, 2.5 )
h_m_ptresponse_npv20_30 = ROOT.TH2F('h_m_ptresponse_npv20_30', ';m_{T}^{GEN};p_{T}^{RECO} / p_{T}^{GEN}', 25, 0, 100, 25, 0, 2.5 )
h_m_mresponse_npv20_30 = ROOT.TH2F('h_m_mresponse_npv20_30', ';m^{GEN};m^{RECO} / m^{GEN}', 25, 0, 100, 25, 0, 2.5 )
h_pt_mresponse_npv20_30 = ROOT.TH2F('h_pt_mresponse_npv20_30', ';p_{T}^{GEN};m^{RECO} / m^{GEN}', 25, 0, 500, 25, 0, 2.5 )

h_pt_ptresponse_npv30_40 = ROOT.TH2F('h_pt_ptresponse_npv30_40', ';p_{T}^{GEN};p_{T}^{RECO} / p_{T}^{GEN}', 25, 0, 500, 25, 0, 2.5 )
h_m_ptresponse_npv30_40 = ROOT.TH2F('h_m_ptresponse_npv30_40', ';m_{T}^{GEN};p_{T}^{RECO} / p_{T}^{GEN}', 25, 0, 100, 25, 0, 2.5 )
h_m_mresponse_npv30_40 = ROOT.TH2F('h_m_mresponse_npv30_40', ';m^{GEN};m^{RECO} / m^{GEN}', 25, 0, 100, 25, 0, 2.5 )
h_pt_mresponse_npv30_40 = ROOT.TH2F('h_pt_mresponse_npv30_40', ';p_{T}^{GEN};m^{RECO} / m^{GEN}', 25, 0, 500, 25, 0, 2.5 )

h_pt_ptresponse_npv40_50 = ROOT.TH2F('h_pt_ptresponse_npv40_50', ';p_{T}^{GEN};p_{T}^{RECO} / p_{T}^{GEN}', 25, 0, 500, 25, 0, 2.5 )
h_m_ptresponse_npv40_50 = ROOT.TH2F('h_m_ptresponse_npv40_50', ';m_{T}^{GEN};p_{T}^{RECO} / p_{T}^{GEN}', 25, 0, 100, 25, 0, 2.5 )
h_m_mresponse_npv40_50 = ROOT.TH2F('h_m_mresponse_npv40_50', ';m^{GEN};m^{RECO} / m^{GEN}', 25, 0, 100, 25, 0, 2.5 )
h_pt_mresponse_npv40_50 = ROOT.TH2F('h_pt_mresponse_npv40_50', ';p_{T}^{GEN};m^{RECO} / m^{GEN}', 25, 0, 500, 25, 0, 2.5 )

h_pt_ptresponses = [
h_pt_ptresponse_npv10_20,
h_pt_ptresponse_npv20_30,
h_pt_ptresponse_npv30_40,
h_pt_ptresponse_npv40_50
]

h_m_ptresponses = [
h_m_ptresponse_npv10_20,
h_m_ptresponse_npv20_30,
h_m_ptresponse_npv30_40,
h_m_ptresponse_npv40_50
]

h_m_mresponses = [
h_m_mresponse_npv10_20,
h_m_mresponse_npv20_30,
h_m_mresponse_npv30_40,
h_m_mresponse_npv40_50
]

h_pt_mresponses = [
h_pt_mresponse_npv10_20,
h_pt_mresponse_npv20_30,
h_pt_mresponse_npv30_40,
h_pt_mresponse_npv40_50
]



def getptbin(x) :
    ptbins = [
        10., 30., 100., 400., 2000., 13000.
        ]
    if x < 10. :
        return None
    for i in xrange( len(ptbins) - 1 ) :
        if x >= ptbins[i] and x < ptbins[i+1] :
            return i
    return len(ptbins) - 2

def getNPVbin(x) :
    NPVbins = [
        10, 20, 30, 40, 50
        ]
    if x < 10 :
        return None
    for i in xrange( len(NPVbins) - 1 ) :
        if x >= NPVbins[i] and x < NPVbins[i+1] :
            return i
    return len(NPVbins) - 2

NPVs = []
PTs = []
nparts = 4
npartspt = 5
if options.dynamicBin :
    for jentry in xrange ( entries ) :
        nc = tree.GetEntry( jentry )
        if nc <= 0 :
            continue


        geneJets = []
        NPVs.append(npv[0])
        for i in xrange( jets_pt.size() ) :
            g = ROOT.TLorentzVector( )
            g.SetPtEtaPhiE( genjets_pt[i], genjets_eta[i], genjets_phi[i], genjets_e[i] )
            geneJets.append(g)


        if len(geneJets) > 0 and geneJets[0].Perp() > 20. :
            PTs.append(geneJets[0].Perp())

    NPVs.sort()
    PTs.sort()

    NPVSize = len(NPVs)
    PTSize = len(PTs)


    def dynamicBinsNPV(x) :
        dNPVbins = [ NPVs[(NPVSize/nparts)-1], NPVs[2*(NPVSize/nparts)-1], NPVs[3*(NPVSize/nparts)-1], NPVs[4*(NPVSize/nparts)-1] ]
        if x < NPVs[(NPVSize/nparts)-1]:
            return 0        
        for i in xrange( len(dNPVbins) - 1 ) :
            if x >= dNPVbins[i] and x < dNPVbins[i+1] :
                return (i+1)
        return len(dNPVbins) - 1

    def dynamicBinsPT(x) :
        dptbins = [ PTs[(PTSize/npartspt)-1], PTs[2*(PTSize/npartspt)-1], PTs[3*(PTSize/npartspt)-1], PTs[4*(PTSize/npartspt)-1], PTs[5*(PTSize/npartspt)-1] ]
        if x < PTs[(PTSize/npartspt)-1]:
            return 0        
        for i in xrange( len(dptbins) - 1 ) :
            if x >= dptbins[i] and x < dptbins[i+1] :
                return (i+1)
        return len(dptbins) - 1



# Loop over events
for jentry in xrange( entries ):

    if jentry %1000 == 0 :
        print jentry

    # copy next entry into memory and verify
    nb = tree.GetEntry( jentry )
    if nb <= 0:
        continue


    # Get the list of jets, and maximum pt to decide
    # which trigger bin this should be in. 
    ptMax = -1.0
    goodJets = []
    genJets = []
        
    PVs = npv[0]
    
    
    
    if options.dynamicBin :
        jbin = dynamicBinsNPV(PVs)
    else :
        jbin = getNPVbin(PVs)

    #print ' jbin ' + str(jbin) + ' npv ' + str(PVs)
    for i in xrange( jets_pt.size() ) :
        #print '%6.2f %6.2f' % ( jets_pt[i], genjets_pt[i])
        v = ROOT.TLorentzVector( )
        v.SetPtEtaPhiE( jets_pt[i], jets_eta[i], jets_phi[i], jets_e[i] )
        v *= jets_jec[i]
        goodJets.append(v)
        g = ROOT.TLorentzVector( )
        g.SetPtEtaPhiE( genjets_pt[i], genjets_eta[i], genjets_phi[i], genjets_e[i] )
        genJets.append(g)
        
    
    if len(goodJets) > 0 and genJets[0].Perp() > 0.0 :
        pt = goodJets[0].Perp()
        if pt < 30. :
            continue
        m = goodJets[0].M()
        y = goodJets[0].Eta()        
        genpt = genJets[0].Perp()
        genm = genJets[0].M()
        geny = genJets[0].Eta()
        rho = (m / (pt*R)) * (m / (pt*R))
        genrho = (genm / (genpt*R)) * (genm / (genpt*R))

        if options.dynamicBin :
            ibin = dynamicBinsPT(pt)
        else :
            ibin = getptbin(pt)
        if ibin != None :
            #print 'pt = ' + str(pt) + ', ijbin = ' + str(ibin)
            h_pt_etaresponses[ibin].Fill( abs(geny), pt/genpt )
            h_m_etaresponses[ibin].Fill( abs(geny), m / genm )
        

        
        #Fill NPV binned things
        if jbin != None :
            h_pt_etaresponses[5+jbin].Fill( abs(geny), pt/genpt )
            h_m_etaresponses[5+jbin].Fill( abs(geny), m / genm )
            h_pt_ptresponses[jbin].Fill( genpt, pt/genpt )
            h_m_ptresponses[jbin].Fill( genm , pt/genpt )
            h_m_mresponses[jbin].Fill( genm, m/genm )
            h_pt_mresponses[jbin].Fill( genpt , m/genm )


        if abs( y ) < 1.3 : 
            h_pt0.Fill( pt )
            h_pt_ptresponse0.Fill( genpt, pt / genpt )
            
        if pt > 30. :
            h_pt_etaresponse0.Fill( geny, pt / genpt )            

        if pt > 200.0 and abs(y) < 1.3 :
            h_m0.Fill( m )
            h_m_mresponse0.Fill( genm, m / genm )
            h_m_ptresponse0.Fill( genpt, m / genm )
            h_m_etaresponse0.Fill( geny, m / genm )
            h_rho0.Fill( rho )
            h_rho_rhoresponse0.Fill(genrho, rho/genrho)
            
print "EXITING"

if options.dynamicBin :
    print "NPV Bin 0: " + str(NPVs[0]) + " - " + str(NPVs[(NPVSize/nparts)-1])
    print "NPV Bin 1: " + str(NPVs[(NPVSize/nparts)-1]) + " - " + str(NPVs[2*(NPVSize/nparts)-1])
    print "NPV Bin 2: " + str(NPVs[2*(NPVSize/nparts)-1]) + " - " + str(NPVs[3*(NPVSize/nparts)-1])
    print "NPV Bin 3: " + str(NPVs[3*(NPVSize/nparts)-1]) + " - " + str(NPVs[4*(NPVSize/nparts)-1])
    
    print "pt Bin 0: " + str(PTs[0]) + " - " + str(PTs[(PTSize/npartspt)-1])
    print "pt Bin 1: " + str(PTs[(PTSize/npartspt)-1]) + " - " + str(PTs[2*(PTSize/npartspt)-1]) 
    print "pt Bin 2: " + str(PTs[2*(PTSize/npartspt)-1]) + " - " + str(PTs[3*(PTSize/npartspt)-1])
    print "pt Bin 3: " + str(PTs[3*(PTSize/npartspt)-1]) + " - " + str(PTs[4*(PTSize/npartspt)-1])
    print "pt Bin 4: " + str(PTs[4*(PTSize/npartspt)-1]) + " - " + str(PTs[5*(PTSize/npartspt)-1])

f.cd()
f.Write()
f.Close()
