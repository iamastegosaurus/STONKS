def get_lookups(row):

    lookups = {
        "netrevenue": "NR",
        "revenues": "NR",
        "revenue": "NR",
        "totalrevenue": "NR",
        "netsales": "NR",
        "totalnetrevenue": "NR",
        "netrevenues": "NR",
        "totalrevenues": "NR",
        "totalnetsales": "NR",

        "costofsales": "COGS",
        "costofrevenue": "COGS",
        "merchandisecosts": "COGS",
        "costofgoodssold": "COGS",
        "totalcostofrevenue": "COGS",
        "costofproductssold": "COGS",
        "costofrevenuecor": "COGS",

        "marketinggeneralandadministrative": "SGA",
        "sellinginformationalandadministrativeexpenses": "SGA",
        "sellinggeneralandadministrative": "SGA",
        "salesgeneralandadministrative": "SGA",
        "sellinggeneralandadministrativeexpenses": "SGA",
        "sellinggeneralandadministrativeexpense": "SGA",
        "generalandadministrative": "SGA",
        "sellinggeneral&administrativeexpenses": "SGA",
        "othersellinggeneralandadministrativeexpense": "SGA",
        "sellinggeneralandadministrativesg&a": "SGA",

        "researchanddevelopment": "RND",
        "researchanddevelopmentexpenses": "RND",
        "researchanddevelopmentexpense": "RND",
        "researchanddevelopmentcosts": "RND",
        "researchdevelopmentandrelatedexpenses": "RND",
        "researchanddevelopmentr&d": "RND",

        "totaloperatingexpenses": "OE",
        "totaloperatingcostsandexpenses": "OE",

        "operatingincome": "OI",
        "operatingprofit": "OI",
        "operatingloss": "OI",
        "operatingincomeloss": "OI",
        "operatingearnings": "OI",
        "earningsfromcontinuingoperations": "OI",

        "netincome": "NI",
        "netincomeattributabletocompany": "NI",
        "netearnings": "NI",
        "netearningsloss": "NI",
        "netloss": "NI",
        "netincomeloss": "NI",
        "netincomelossattributabletocompany": "NI",
        "netlossincomeattributabletocompany": "NI",
        "netearningsattributabletocontrollinginterests": "NI",
        "incomefromcontinuingoperationsattributabletocommonshareowners": "NI",
        "netincomeattributabletocommonshareowners": "NI",


        "dilutedshares": "SHARES",
        "weightedaveragesharesdiluted": "SHARES",
        "dilutedshares": "SHARES",
        "dilutedinshares": "SHARES",
        "diluted": "SHARES",
        "denominatorfordilutedearningslosspershare": "SHARES",
        "weightedaveragedilutedsharesoutstandinginshares": "SHARES",
        "averagenumberofcommonsharesoutstandingplusdilutivecommonstockoptionsinshares": "SHARES",
        "averagenumberofcommonsharesoutstandingplusdilutivecommonstockoptions": "SHARES",
        "weightedaveragesharesusedindilutedpersharecomputation": "SHARES",
        "weightedaveragesharesoutstandingdiluted": "SHARES",

        # fucking autodesk 
        "weightedaveragesharesusedincomputingdilutednetlosspershareshares": "SHARES",
        "weightedaveragesharesusedincomputingdilutednetlosspershareinshares": "SHARES",
        "weightedaveragesharesusedincomputingdilutednetincomelosspershareinshares": "SHARES",
        "weightedaveragesharesusedincomputingdilutednetincomelosspershareshares": "SHARES",
        "weightedaveragesharesusedincomputingdilutednetincomepershareinshares": "SHARES",
        "dilutedweightedaverageshares": "SHARES",

        "cashandcashequivalents": "CCE",
        "cashandequivalents": "CCE",
        "cashcashequivalentsrestrictedcashandrestrictedcashequivalents": "CCE",

        "accountsreceivable": "AR",
        "receivablesnet": "AR",
        "accountsandnotesreceivablenet": "AR",
        "accountsreceivablenet": "AR",
        "accountsreceivablenetofallowancefordoubtfulaccounts": "AR",
        "tradereceivables": "AR",
        "tradereceivablesnet": "AR",
        "accountsandnotesreceivable": "AR",

        "inventories": "IN",
        "inventoriesnet": "IN",
        "merchandiseinventories": "IN",
        "totalinventories": "IN",
        "inventoriesatcostnotinexcessofmarket": "IN",
        "inventoriesandcontractsinprogressnet": "IN",

        "totalcurrentassets": "TCA",
        "totalassets": "TA",

        "totalcurrentliabilities": "TCL",
        "totalliabilities": "TL",

        "totalequity": "TSHE",
        "totalstockholdersequity": "TSHE",
        "totalstockholdersequitydeficit": "TSHE",
        "totalstockholdersdeficit": "TSHE",
        "totalstockholdersdeficitequity": "TSHE",
        "totalshareholdersequity": "TSHE",
        "totalshareholdersinvestment": "TSHE",
        "totalshareholdersequitydeficit": "TSHE",

        "totalliabilitiesandequity": "TLSHE",
        "liabilitiesandequity": "TLSHE",
        "totalliabilitiesandstockholdersequity": "TLSHE",
        "totalliabilitiesandstockholdersequitydeficit": "TLSHE",
        "totalliabilitiesandstockholdersdeficit": "TLSHE",
        "totalliabilitiesandstockholdersdeficitequity": "TLSHE",
        "totalliabilitiestemporaryequityandstockholdersequity": "TLSHE",
        "totalliabilitiesandshareholdersequity": "TLSHE",
        "totalliabilitiesandshareholdersinvestment": "TLSHE",
        "totalliabilitiestemporaryequityandshareholdersequity": "TLSHE",
        "totalliabilitiesconvertibledebtconversionobligationandshareholdersequity": "TLSHE",
        "totalliabilitiesandshareholdersequitydeficit": "TLSHE",
        "totalliabilitiesredeemablenoncontrollinginterestandequity": "TLSHE",

    }

    fuzzylookups = {
        "cashandcashequivalents": "cashandcashequivalents",
        "accountsreceivable": "accountsreceivable",
        "costofproductssold": "costofgoodssold",
        "netincomeattributableto": "netincomeattributabletocompany",
        "netincomelossattributableto": "netincomeattributabletocompany",
        "netlossincomeattributableto": "netincomeattributabletocompany",
        "netearningslossattributableto": "netincomeattributabletocompany",

        "commonsharesoutstandingdiluted": "dilutedshares",

    }

    avoid = { # values from fuzzylookups
        "netincomeattributabletocompany": ["less", "share", "stock", "noncontrolling"]
    }
    r = str(row).lower()
    replace_chars = [',', '(', ')', '.', '-', '–', ' ', "'", '’']
    for c in replace_chars:
        r = r.replace(c, '')
    if r in lookups.keys():
        return lookups[r]
    else:
        for fzy in fuzzylookups.keys():
            if fzy in r:
                if fuzzylookups[fzy] in avoid.keys():
                    for a in avoid[fuzzylookups[fzy]]:
                        if a in r:
                            return -1
                return lookups[fuzzylookups[fzy]]

        return -1