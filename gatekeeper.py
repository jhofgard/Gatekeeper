from auth import server

if __name__ == '__main__':
    version = "0.0.1"
    print "Welcome to DMZ scanning code version: " + version
    iplist = []
    # Spin up server
    server.app.run(
        host="0.0.0.0",
        port=int("8080"),
        debug=True
    )
    while True:
# Detect
# iplist, newIps, lostIps) = dhcdetect.detect(iplist)
# Scan
# for ip in newIps:


# Approve

# Auth
