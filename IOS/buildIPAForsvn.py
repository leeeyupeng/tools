PROJECT_NAME=sys.argv[4];
PROJECT_PATH=sys.argv[3];
SVN_VERSION = sys.argv[5];

os.system("autoIPA.sh " + PROJECT_NAME + " " + SVN_VERSION);