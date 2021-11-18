import configparser

CONF_FILE = 'settings.conf'

# Config file parser
parser = configparser.RawConfigParser(allow_no_value=True)
parser.read(CONF_FILE)

mongo_uri = parser.get("MONGO", "mongo_uri")
application_db = parser.get("MONGO", "application_db")
string_collection = parser.get("MONGO", "string_collection")

app_host = parser.get("SERVICE", "host")
app_port = parser.get("SERVICE", "port")
