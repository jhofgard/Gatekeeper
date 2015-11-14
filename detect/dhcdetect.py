from isc_dhcp_leases.iscdhcpleases import IscDhcpLeases



def detect(oldlist):
    """

    :rtype: tuple of lists
    """
    checkthese = []
    tmplist = []
    leasepath = '/var/insecure.lease'
    leasefile = IscDhcpLeases(leasepath)
    leaselist = leasefile.get()
    for lease in leaselist:
        if lease.valid:
            tmplist.append(lease.id)
            if lease.ip in oldlist:  # TODO: Decide on things
                continue
            checkthese.append(lease.ip)
    lostlist = list(set(oldlist) - set(tmplist))
    return (tmplist, checkthese, lostlist)
