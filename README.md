# Chromium auto updater for windows
This package will download and install the latest version of chromium for windows.

**Please note:** You still need to run this package from task manager by targeting `main.py`.

-----

## Requirements
- Python 3

-----

## Installing
After downloading the package, you need to copy the file **json/config.example.json** to **json/config.json** and enter the full path _(install_path)_ where chromium will be installed.
Example:
```json
{
  "url": "https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/",
  "file": "chrome-win.zip",
  "local_file": "chromium.zip",
  "install_path": "C:\\Users\\YourUserName\\chromium"
}
```

**Please note:** Make sure to escape backslashes.

-----

## License
The MIT License (MIT). Please see [License File](https://github.com/.../blob/master/LICENSE.md) for more information.
