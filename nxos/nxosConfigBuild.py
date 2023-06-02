# Jeff Comer
# script to build nxos device configurations
# Example input file is vars/<branch>/nxos/nxosDevVars.csv.csv

import sys, getopt, csv
from nxosOps import nxosAddFeature


def main(argv):
    """
    Main execution routine

    :return: None
    """

    username = ""
    password = ""
    userArg = ""
    pwArg = ""

    argDict = {"username":"","password":"","infile":""}
    try:
      opts, args = getopt.getopt(argv,"hu:p:i:",["username","password","infile="])
    except getopt.GetoptError:
      print('nxosConfigBuild.py -u <username> -p <password> -i <inputcsv>')
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print('nxosConfigBuild.py -u <username> -p <password> -i <inputcsv>')
         sys.exit()
      elif opt in ("-u", "--username"):
         userArg = arg
         argDict["username"] = userArg
      elif opt in ("-p", "--password"):
         pwArg = arg
         argDict["password"] = pwArg
      elif opt in ("-i", "--infile"):
         infileArg = arg
         argDict["infile"] = infileArg
    return argDict

if __name__ == '__main__':
    nxosData = main(sys.argv[1:])
    addFeature = nxosAddFeature(nxosData)