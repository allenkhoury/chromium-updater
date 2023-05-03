from classes import file
from classes import parser

# Generate LAST_CHANGE url
latest_version_url = parser.get_latest_version_url()

# Get the latest version from LAST_CHANGE
latest_version = file.open_file(latest_version_url)

# Construct url
update_url = parser.get_update_url(latest_version)

# Download file
file_status = file.download_file(update_url)

# install and clean downloaded data
if file_status:
    file.install_file()
